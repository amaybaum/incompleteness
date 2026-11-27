"""WIP / UNVERIFIED staging draft, not frozen, not reviewed, not adopted.

OBL-1 and OBL-2 parity comparisons of design r6 (r13) sec. 32 (checklist item 4.10, #1169 comment 7207860923):
the ledger-coverage engine's per-edit `register` / `register-caps` / `infinity` unit and its edit-to-splice
binding, compared with the plan's frozen checker P (`edits_check.py`) run as itself.

OBL-1 (R6.PROF.12, E-115): the engine implements items 5 and 6 as P's `static_new`, `inf_key` and `sentences`
define them, per edit and per pair of the edit list.
  1a  P's sentence regex (the argument of `re.split` in `sentences`) equals the params rule's `splitter`, and both
      split every `old`, `old_step2`, `new` and `new_step2` text of the edit list identically.
  1b  the A1 edit list: the engine's per-edit findings equal `static_new`'s (register, caps, infinity), as
      multisets of (edit id, token) and (edit id, assertion, sentence prefix).
  1c  crafted regression cases, one per branch of `static_new` that items 5 and 6 read.
  1d  a seeded random enumeration of edit lists built from register, caps, infinity and neutral fragments.
OBL-2 (E-122, E-124, E-1357, E-1358): recomputation of the parity measurements.
  2a  the A1 edit list at H: number of edits, retained edits (old equal to new), splices bound; the engine's
      correspondence reports no error, and P's own selection applied in list order reproduces each ledgered
      file's expected_sha256.
  2b  a seeded random enumeration over the alphabet "ab ": P's selection and application against the engine's
      correspondence, with splices built from P's application by a mapping this script implements itself.

The random generators are this script's own, seeded; their counts are new measurements of the same comparison.
The design-time figures 2822 / 16905 / 273 and 4000 came from scripts that were not retained, and this script does
not reproduce them (README of a1exit-staging-drafts-20261127, stop S-5).

Every input is read by git object id and checked against its pinned sha256: P from `main`
(design r6 directory, inputs/edits_check.py), the ledger and edit list by their R6.EVID.8 blob ids, H, and the
params rule file and the engine modules from the tool tree given (imported, never changed). Run with `python3 -I`.
Output: one JSON document on stdout, deterministic for fixed inputs; exit status 0 when every comparison holds
(no difference anywhere), 1 otherwise.

Usage: python3 -I obl12_parity.py --repo <git dir> --tool <tree holding tools/ledger_coverage>
           [--checker COMMIT:PATH --checker-sha SHA256] [--params COMMIT:PATH --params-sha SHA256]
           [--random-1d N] [--random-2b N] [--seed S]
"""
import argparse
import ast
import hashlib
import json
import random
import re
import subprocess
import sys
import types

H = '53c6601a10419b6b333cc992474272501ab542af'
LEDGER_BLOB, LEDGER_SHA = 'ba37c1cdb560cb5fceeeb2b46a3091c832b4a80e', \
    '2055e68f2343d00cec93bc35ecbccae21d46d1da154ee1a842663f1e4fec32b5'
EDITS_BLOB, EDITS_SHA = 'ec384fdfbc12937b860e2f226355e8c5d94820a5', \
    '528f146d03b29cbc3d7dc29948e3dd1d4cd26f4d36e6e009f032e24f9462dec1'
CHECKER = ('3e73633308bdef99f65f6117733aaf86097c7b22',
           'verification/audits/foundations/a1exit-design-r6-20261125/inputs/edits_check.py')
CHECKER_SHA = '2856e58c65817865a57fc34851ab3319d1cdda86f72f76a77fc6c063b2f1d98c'
PARAMS = (None, 'verification/audits/foundations/ledger-coverage-tool-20261123/rules/register-infinity-params-v1.json')
PARAMS_SHA = '05149ba694dd4017ad27dd60c02810403ec7351036776bea212768ba9ebc509f'
# the engine files whose behaviour is compared; their digests are part of the output
ENGINE_FILES = ('tools/ledger_coverage/engine/peredit.py', 'tools/ledger_coverage/engine/profiles.py',
                'tools/ledger_coverage/engine/util.py', 'tools/ledger_coverage/adapters/a1exit_exact_edit.py')
# the A1 configuration's specs of the three per-edit profiles (pattern hashes as staged)
PROFILE_SPECS = [
    ('register', 'REG', None, 'fae2274866d3a161c52750c7046c8336fb05f8bcaabe98c1291268a56f75e946'),
    ('register-caps', 'CAPS', ('tokens', 'CAPS_OK'), '1e0fc5a833f5361c2d89d45a16016b636e164ebe4e589bb7c0aaf31dc5443014'),
    ('infinity', 'INF', ('spans', 'NEUTRAL'), 'd6c4e97a4075e45982602d152b01171527ac8fd26e0aca14c2e5649ae94c07e5'),
]


def sha(b):
    return hashlib.sha256(b).hexdigest()


class Git:
    def __init__(self, repo):
        self.repo = repo

    def run(self, *a):
        r = subprocess.run(['git', '-C', self.repo] + list(a), capture_output=True)
        return r.stdout if r.returncode == 0 else None

    def blob(self, oid, want):
        b = self.run('cat-file', 'blob', oid)
        if b is None or sha(b) != want:
            raise SystemExit('blob %s missing or not sha256 %s' % (oid, want))
        return b

    def show(self, commit, path, want=None):
        b = self.run('show', '%s:%s' % (commit, path))
        if b is None or (want is not None and sha(b) != want):
            raise SystemExit('%s:%s missing or not sha256 %s' % (commit, path, want))
        return b


def load_p(src):
    """P's checker as itself: its own source executed in a fresh module, nothing retyped."""
    mod = types.ModuleType('p_edits_check')
    mod.__file__ = '/nonexistent/a1exit-deletion-20261121/edits_check.py'
    exec(compile(src.decode('utf-8'), 'edits_check.py', 'exec'), mod.__dict__)
    return mod


def p_split_regex(src):
    for node in ast.walk(ast.parse(src.decode('utf-8'))):
        if isinstance(node, ast.FunctionDef) and node.name == 'sentences':
            for c in ast.walk(node):
                if isinstance(c, ast.Call) and getattr(c.func, 'attr', None) == 'split':
                    return ast.literal_eval(c.args[0])
    return None


def p_findings(P, edits):
    inf, reg, caps, _ = P.static_new({'edits': edits})
    return {'register': sorted(list(x) for x in reg), 'register-caps': sorted(list(x) for x in caps),
            'infinity': sorted(list(x) for x in inf)}


def engine_findings(adapter, peredit, params, profiles, edits):
    led = {'schema': adapter.LEDGER_SCHEMA, 'base': None, 'splices': [], 'files': {}}
    doc = {'schema': adapter.EDITS_SCHEMA, 'edits': edits}
    loaded = adapter.load(json.dumps(led).encode(), {'edits': json.dumps(doc).encode()}, read=None)
    rec, _ = peredit.evaluate(loaded, params, profiles)
    if not rec or not rec.get('evaluated'):
        return None
    return {k: sorted(list(x) for x in v) for k, v in rec['findings'].items()}


def regression_cases():
    """One edit list per branch of static_new that items 5 and 6 read (E-1358's regression set, restated)."""
    c = []

    def e(i, old, new, kind='ptr', **kw):
        d = {'id': 'R%03d' % i, 'kind': kind, 'file': 'x.md', 'site': 'x.md:%d' % i, 'part': 1, 'mirror_of': None,
             'old': old, 'new': new}
        d.update(kw)
        return d
    c.append(('register added', [e(1, 'The bound holds.', 'The bound now holds.')]))
    c.append(('register kept', [e(2, 'It was corrected.', 'It is corrected.')]))
    c.append(('register case-insensitive', [e(3, 'x', 'Formerly x.')]))
    c.append(('caps added on a ptr edit', [e(4, 'see the ledger', 'see the NEW ledger')]))
    c.append(('caps added on a manuscript edit (not scanned)', [e(5, 'see', 'see THE', kind='manuscript')]))
    c.append(('caps whitelisted', [e(6, 'see', 'see QFT and CPTP')]))
    c.append(('caps in a LaTeX command', [e(7, 'x', '\\ABC x')]))
    c.append(('infinity added', [e(8, 'S is finite.', 'The substratum is infinite.')]))
    c.append(('infinity carried over', [e(9, 'The universe is infinite.', 'The universe is infinite, as stated.')]))
    c.append(('infinity via the A1 rewrite', [e(10, 'If A1 fails, then.', 'If finiteness fails, then.')]))
    c.append(('infinity via the A1 (finiteness) rewrite', [e(11, 'A1 (finiteness) fails here.',
                                                             'Finiteness fails here.')]))
    c.append(('neutral disclaimer', [e(12, 'x', 'We assume neither that the substratum is finite nor that the '
                                              'substratum is infinite.')]))
    c.append(('infinity outside the neutral span', [e(13, 'x', 'Neither the substratum is finite nor the substratum '
                                                             'is infinite; the lattice is infinite.')]))
    c.append(('two equal assertions, one old', [e(14, 'S is infinite.', 'S is infinite. S is infinite.')]))
    c.append(('sentence split at a semicolon', [e(15, 'a; b', 'a; the universe is infinite')]))
    c.append(('second pair with new_step2', [e(16, 'a', 'b', old_step2='c', new_step2='c, now infinitely many')]))
    c.append(('second pair whose new_step2 equals its old_step2', [e(17, 'a', 'b', old_step2='c is infinite',
                                                                   new_step2='c is infinite')]))
    c.append(('key normalization (whitespace, emphasis)', [e(18, 'is  *infinite* x', 'is infinite x')]))
    c.append(('lean-docstring kind', [e(19, 'x', 'the thermodynamic limit, now', kind='lean-docstring')]))
    c.append(('consistency kind caps', [e(20, 'x', 'XYZ now', kind='consistency')]))
    c.append(('handoff kind caps', [e(21, 'x', 'ABCD', kind='handoff')]))
    c.append(('several edits, one list', [e(22, 'a', 'now a'), e(23, 'b', 'NEWS b'), e(24, 'c', 'c is infinite')]))
    c.append(('empty replacement', [e(25, 'The universe is infinite.', '')]))
    c.append(('key rule: two wordings of finiteness failing', [e(26, 'If finiteness of S fails, then.',
                                                                 'If finiteness fails, then.')]))
    return c


FRAG = None


def random_edits(rng, n_edits):
    global FRAG
    if FRAG is None:
        FRAG = ['the substratum', 'is infinite', 'is not finite', 'infinitely many', 'thermodynamic limit',
                'neither the substratum is finite nor the substratum is infinite', 'A1', 'A1 (finiteness)',
                'finiteness', 'fails', 'now', 'formerly', 'Corrected', 'the reader should note', 'QFT', 'ABC', 'NEW',
                'XYZW', 'lattice', 'set', 'S', '.', ';', ':', '?', ',', 'and', 'holds', 'infinite lattice',
                'of infinite extent', 'regardless of cardinality', 'no finite bound', 'used to']
    kinds = ['ptr', 'consistency', 'handoff', 'manuscript', 'repo-active', 'lean-docstring']

    def text():
        return ' '.join(rng.choice(FRAG) for _ in range(rng.randint(0, 8)))
    out = []
    for i in range(n_edits):
        d = {'id': 'Q%03d' % i, 'kind': rng.choice(kinds), 'file': 'x.md', 'site': 'x.md:%d' % i, 'part': 1,
             'mirror_of': None, 'old': text(), 'new': text()}
        if rng.random() < 0.5:
            d['old_step2'], d['new_step2'] = text(), text()
        out.append(d)
    return out


# ---- OBL-2 2b: P's application mapped back to the base by this script's own bookkeeping ----------------------

def p_apply(P, edits, base):
    """P's check(): every edit has a unique variant at the base; then each is applied in list order to the running
    copy with P's own `variant`. Returns (applied?, [(edit, old, new, running offset)])."""
    for e in edits:
        if P.variant(e, base)[0] is None:
            return False, []
    sim, steps = base, []
    for e in edits:
        o, n, _ = P.variant(e, sim)
        if o is None:
            return False, steps
        p = sim.index(o)
        steps.append((e, o, n, p))
        sim = sim[:p] + n + sim[p + len(o):]
    return True, steps


def map_to_base(steps):
    """Base spans of each applied step, or None for a step whose occurrence touches an earlier replacement's image.
    The bookkeeping is a list of (base start, base end, running start, running end) of replaced spans."""
    reps, spans = [], []
    for e, o, n, p in steps:
        q = p + len(o)
        inside = [r for r in reps if not (q <= r[2] or p >= r[3]) or (p == q and r[2] < p < r[3])]
        if inside:
            spans.append(None)
            delta = len(n) - len(o)
            reps = [(a, b, c + (delta if c >= q else 0), d + (delta if d >= q else 0)) for a, b, c, d in reps]
            continue
        shift = sum(r[3] - r[2] - (r[1] - r[0]) for r in reps if r[3] <= p)
        bs, be = p - shift, q - shift
        spans.append((bs, be))
        delta = len(n) - len(o)
        reps = [(a, b, c + (delta if c >= q else 0), d + (delta if d >= q else 0)) for a, b, c, d in reps]
        reps.append((bs, be, p, p + len(n)))
    return spans


def obl2_random(P, adapter, rng, n):
    tally = {'P applies, splices representable, engine accepts': 0,
             'P refuses, engine refuses': 0,
             'P applies, an edit chained (no representable splice), engine refuses': 0,
             'difference': 0}
    diffs = []
    for i in range(n):
        base = ''.join(rng.choice('ab ') for _ in range(rng.randint(1, 10)))
        edits = []
        for j in range(rng.randint(1, 3)):
            def s(k):
                return ''.join(rng.choice('ab ') for _ in range(rng.randint(1, k)))
            d = {'id': 'E%d' % j, 'file': 'f', 'site': 'f:%d' % j, 'part': 1, 'mirror_of': None, 'old': s(3),
                 'new': s(3)}
            if rng.random() < 0.6:
                d['old_step2'], d['new_step2'] = s(3), s(3)
            edits.append(d)
        ok, steps = p_apply(P, edits, base)
        spans = map_to_base(steps) if ok else []
        splices = []
        if ok:
            for (e, o, nn, _), sp in zip(steps, spans):
                if sp is not None and o != nn:
                    splices.append({'id': e['id'], 'file': 'f', 'start': sp[0], 'end': sp[1], 'new': nn})
        errs = adapter.correspondence(edits, splices, lambda b, f: base.encode() if f == 'f' else None, 'B')
        if ok and all(sp is not None for sp in spans):
            # the splices must also reproduce P's text
            t = base
            for sp in sorted(splices, key=lambda z: z['start'], reverse=True):
                t = t[:sp['start']] + sp['new'] + t[sp['end']:]
            sim = base
            for e, o, nn, p in steps:
                sim = sim[:p] + nn + sim[p + len(o):]
            if not errs and t == sim:
                tally['P applies, splices representable, engine accepts'] += 1
                continue
        elif not ok and errs:
            tally['P refuses, engine refuses'] += 1
            continue
        elif ok and errs:
            tally['P applies, an edit chained (no representable splice), engine refuses'] += 1
            continue
        tally['difference'] += 1
        if len(diffs) < 5:
            diffs.append({'case': i, 'base': base, 'edits': edits, 'P_applies': ok, 'engine_errors': errs})
    return tally, diffs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', required=True)
    ap.add_argument('--tool', required=True)
    ap.add_argument('--checker', default='%s:%s' % CHECKER)
    ap.add_argument('--checker-sha', default=CHECKER_SHA)
    ap.add_argument('--params', default=None, help='COMMIT:PATH; default: the tool tree\'s params rule file')
    ap.add_argument('--params-sha', default=PARAMS_SHA)
    ap.add_argument('--random-1d', type=int, default=4000)
    ap.add_argument('--random-2b', type=int, default=20000)
    ap.add_argument('--seed', type=int, default=20261127)
    a = ap.parse_args()
    sys.path.insert(0, a.tool + '/tools')
    from ledger_coverage.engine import peredit, profiles as pr
    from ledger_coverage.adapters import a1exit_exact_edit as adapter

    g = Git(a.repo)
    cc, cp = a.checker.split(':', 1)
    psrc = g.show(cc, cp, a.checker_sha)
    if a.params:
        pc, pp = a.params.split(':', 1)
        pbytes = g.show(pc, pp, a.params_sha)
    else:
        with open(a.tool + '/' + PARAMS[1], 'rb') as fh:
            pbytes = fh.read()
        if sha(pbytes) != a.params_sha:
            raise SystemExit('params rule file is not sha256 %s' % a.params_sha)
    params = [r for r in json.loads(pbytes)['rules'] if r.get('kind') == peredit.params_kind][0]
    ledger_b = g.blob(LEDGER_BLOB, LEDGER_SHA)
    edits_b = g.blob(EDITS_BLOB, EDITS_SHA)
    led = json.loads(ledger_b)
    edits = json.loads(edits_b)['edits']
    P = load_p(psrc)

    out = {'inputs': {'H': H, 'checker': {'ref': a.checker, 'sha256': a.checker_sha},
                      'params_sha256': a.params_sha, 'ledger_sha256': LEDGER_SHA, 'edits_sha256': EDITS_SHA,
                      'seed': a.seed, 'random_1d': a.random_1d, 'random_2b': a.random_2b,
                      'engine_files_sha256': {m: sha(open(a.tool + '/' + m, 'rb').read()) for m in ENGINE_FILES}},
           'OBL-1': {}, 'OBL-2': {}}
    ok = True

    # profiles extracted from P's own blob, pattern hashes compared with the configuration's pins
    profiles = {}
    pins = {}
    for name, sel, minus, pin in PROFILE_SPECS:
        src = {'commit': cc, 'path': cp, 'extractor': {'kind': 'python-ast-assign', 'selector': sel},
               'blob_sha256': a.checker_sha}
        spec = {'name': name, 'kind': 'deny', 'applies_to': 'added-text', 'scope': 'ledgered', 'source': src}
        if minus:
            spec['except'] = {'mode': minus[0], 'source': dict(src, extractor={'kind': 'python-ast-assign',
                                                                               'selector': minus[1]})}
        prof, h = pr.load_profile(spec, lambda s: psrc)
        profiles[name] = prof
        pins[name] = h == pin
    out['OBL-1']['profile_pins_hold'] = pins
    ok &= all(pins.values())

    # 1a splitter
    rx = p_split_regex(psrc)
    texts = [e[k] for e in edits for k in ('old', 'new', 'old_step2', 'new_step2') if k in e]
    same_split = all(P.sentences(t) == re.split(params['splitter'], t) for t in texts)
    out['OBL-1']['1a'] = {'checker_regex_equals_params_splitter': rx == params['splitter'],
                          'texts_split': len(texts), 'identical_splits': same_split}
    ok &= rx == params['splitter'] and same_split

    # 1b A1 edit list
    pf = p_findings(P, edits)
    ef = engine_findings(adapter, peredit, params, profiles, edits)
    out['OBL-1']['1b'] = {'edits': len(edits), 'P_counts': {k: len(v) for k, v in pf.items()},
                          'engine_counts': {k: len(v) for k, v in (ef or {}).items()}, 'equal': ef == pf}
    ok &= ef == pf

    # 1c crafted regression cases
    rows = []
    for label, case in regression_cases():
        pfc, efc = p_findings(P, case), engine_findings(adapter, peredit, params, profiles, case)
        rows.append({'case': label, 'P_counts': {k: len(v) for k, v in pfc.items()}, 'equal': efc == pfc})
    out['OBL-1']['1c'] = {'cases': len(rows), 'differences': sum(1 for r in rows if not r['equal']), 'rows': rows}
    ok &= all(r['equal'] for r in rows)

    # 1d random enumeration
    rng = random.Random(a.seed)
    diff1, nonempty = 0, 0
    first = []
    for i in range(a.random_1d):
        case = random_edits(rng, rng.randint(1, 3))
        pfc, efc = p_findings(P, case), engine_findings(adapter, peredit, params, profiles, case)
        nonempty += any(pfc.values())
        if efc != pfc:
            diff1 += 1
            if len(first) < 5:
                first.append({'case': i, 'edits': case, 'P': pfc, 'engine': efc})
    out['OBL-1']['1d'] = {'cases': a.random_1d, 'cases_with_findings': nonempty, 'differences': diff1,
                          'first_differences': first}
    ok &= diff1 == 0

    # 2a A1 at H
    def read(commit, path):
        return g.run('show', '%s:%s' % (commit, path))
    loaded = adapter.load(ledger_b, {'edits': edits_b, 'checker': psrc}, read=read)
    retained = sorted(e['id'] for e in edits if e['old'] == e['new'] and ('old_step2' not in e))
    files = sorted({e['file'] for e in edits})
    texts_h = {f: read(H, f).decode('utf-8') for f in files}
    sim = dict(texts_h)
    lost = []
    for e in edits:
        o, n, _ = P.variant(e, sim[e['file']])
        if o is None:
            lost.append(e['id'])
            continue
        sim[e['file']] = sim[e['file']].replace(o, n, 1)
    exp = {f: led['files'][f]['expected_sha256'] for f in files if f in led['files']}
    reproduced = sorted(f for f in exp if sha(sim[f].encode('utf-8')) == exp[f])
    edit_ids = {e['id'] for e in edits}
    bound = sorted(s['id'] for s in led['splices'] if s['id'] in edit_ids)
    out['OBL-2']['2a'] = {'edits': len(edits), 'splices': len(led['splices']), 'splices_bound_to_an_edit': len(bound),
                          'retained_edits': retained, 'edits_with_old_step2': sum(1 for e in edits if 'old_step2' in e),
                          'engine_errors': [list(x) for x in loaded['errors']],
                          'P_lost_edits': lost, 'edited_files': len(files),
                          'files_reproducing_expected_sha256': len(reproduced), 'files_with_expected_sha256': len(exp)}
    ok &= not loaded['errors'] and not lost and len(reproduced) == len(exp)

    # 2b random selection and refusal
    rng2 = random.Random(a.seed + 1)
    tally, diffs = obl2_random(P, adapter, rng2, a.random_2b)
    out['OBL-2']['2b'] = {'cases': a.random_2b, 'tally': tally, 'first_differences': diffs}
    ok &= tally['difference'] == 0

    # countercontrols: each perturbation of the engine's inputs, or of the splices, must be detected
    def n_diff(prm):
        n = 0
        for _, case in regression_cases():
            if engine_findings(adapter, peredit, prm, profiles, case) != p_findings(P, case):
                n += 1
        return n
    cc_rows = {
        'caps_kinds without ptr': n_diff(dict(params, caps_kinds=[k for k in params['caps_kinds'] if k != 'ptr'])),
        'splitter without the semicolon': n_diff(dict(params, splitter=params['splitter'].replace(';', ''))),
        'old_rewrite replacement changed': n_diff(dict(params, old_rewrite=dict(params['old_rewrite'],
                                                                                 replacement='the bound'))),
        'key rule removed': n_diff(dict(params, key_rules=[])),
        'second-pair key changed': n_diff(dict(params, pairs_key='old_step2_')),
    }
    # an accepted random case with one splice shifted by one byte is refused by the engine
    rng3 = random.Random(a.seed + 2)
    shifted, tried = 0, 0
    while tried < 200:
        base = ''.join(rng3.choice('ab ') for _ in range(rng3.randint(3, 10)))
        e = {'id': 'E0', 'file': 'f', 'site': 'f:0', 'part': 1, 'mirror_of': None,
             'old': base[1:3], 'new': 'b' + base[1:3]}
        okp, steps = p_apply(P, [e], base)
        if not okp:
            continue
        sp = map_to_base(steps)[0]
        tried += 1
        bad = [{'id': 'E0', 'file': 'f', 'start': sp[0] + 1, 'end': sp[1] + 1, 'new': e['new']}]
        if adapter.correspondence([e], bad, lambda b, f: base.encode(), 'B'):
            shifted += 1
    cc_rows['shifted splice refused (of 200 accepted cases)'] = shifted
    out['countercontrols'] = cc_rows
    cc_ok = all(v > 0 for k, v in cc_rows.items() if not k.startswith('shifted')) and shifted == 200
    out['countercontrols_detected'] = cc_ok
    ok &= cc_ok

    out['holds'] = bool(ok)
    sys.stdout.write(json.dumps(out, indent=1, sort_keys=True, ensure_ascii=False) + '\n')
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
