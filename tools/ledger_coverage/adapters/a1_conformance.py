"""A1 controls of the design (v6.0e) on real objects: W1 option B (WB1-WB15), the per-edit unit and
the plan checker's selection (S11-56, S11-57a-d, S11-58a-k), the reconciliation conditions and the landing
composition (N3-N18, with N10 and N11 pinned to main 8e9b8334 and T1'), and the pinned side-change classes (R18,
R19). Every run uses the control harness (the A1 records are unreviewed drafts); mutant trees, ledgers and
records exist only in memory. Each control is reported as {id, expected, predicate, actual, status}.

Usage: python3 -I -B tools/ledger_coverage/adapters/a1_conformance.py --repo DIR --config REV:PATH --staged-config FILE
       --out DIR (PATH: the staged configuration's path in the plan's record directory; see a1_controls.py)
"""
import argparse
import copy
import io
import json
import os
import sys
import types

here = os.path.dirname(os.path.abspath(__file__))
tools = os.path.dirname(os.path.dirname(here))
if 'ledger_coverage' not in sys.modules:
    # the package is loaded by its location, as the entry point loads it; no directory is put on sys.path
    import importlib.util
    _pkg = os.path.dirname(here)
    _spec = importlib.util.spec_from_file_location('ledger_coverage', os.path.join(_pkg, '__init__.py'),
                                                   submodule_search_locations=[_pkg])
    sys.modules['ledger_coverage'] = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(sys.modules['ledger_coverage'])

from ledger_coverage.engine import cli, execution as exmod, peredit, pipeline as pl, reconcile as rc  # noqa: E402
from ledger_coverage.engine import rules as rulemod, util  # noqa: E402
from ledger_coverage.adapters import a1_controls as a1c, a1exit_exact_edit as le  # noqa: E402

H, T, P, E = a1c.H, a1c.T, a1c.P, a1c.E
PL = a1c.PL
M = '8e9b83341cf5bc7fd9fb260892d0385fc9bfab4d'
CH19 = 'book/ch19-open-problems.md'
FULL = a1c.FULL
RESULTS = []


def check(cid, expected, predicate, actual, holds):
    RESULTS.append({'id': cid, 'expected': expected, 'predicate': predicate, 'actual': actual,
                    'status': 'PASS' if holds else 'FAIL'})


def sha(b):
    return util.sha256(b)


def w1c_sentence(a, commit, path):
    rules = json.loads(a.repo.read(a.crev, a.ad + 'rules/w1-w2-allow-v1.json'))
    w1c = [r for r in rules['rules'] if r['id'] == 'W1-c'][0]
    fp = [f for f in w1c['fingerprints'] if f['file'] == path][0]
    sents = util.sentences_of(a.lines(commit, path), a1c_abbrev(a), 2)
    for k, (s, x, y) in enumerate(sents):
        if util.sha256(s) == fp['sentence_sha256']:
            return s, sents[k - 1][0], sents[k + 1][0], x
    raise RuntimeError('W1-c sentence not found')


def a1c_abbrev(a):
    return json.loads(a.repo.read(a.crev, a.cpath))['sentence']['abbreviations']


def items_at(res, path, line):
    return sorted({i['class'] for i in res.get('items', []) if i.get('file') == path and i.get('line') == line})


def hit_state(res, path, line):
    return [h.get('state') for h in res.get('hits', []) if h['file'] == path and h['line'] == line]


def line_of(text, needle):
    for n, l in enumerate(text.split('\n'), 1):
        if needle in l:
            return n
    return None


def wb_controls(a):
    s, prev, nxt, ln = w1c_sentence(a, T, CH19)
    text = a.repo.read(T, CH19).decode()
    full = a.repo.read(T, FULL).decode()

    def run(files, extra=(), control=None, profile=None):
        x = a.repo.derive(T, {k: v.encode() for k, v in files.items()}, parents=[H], subject='WB')
        sel = ['--profile', profile] if profile else ['--check', 'item7']
        code, res, _ = a.run(['terms', '--commit', x] + sel + list(extra), control=control)
        return x, code, res
    _, code, res = run({})
    l_full = line_of(full, s)
    wb1 = {'ch19': hit_state(res, CH19, ln), 'full': hit_state(res, FULL, l_full),
           'items': items_at(res, CH19, ln) + items_at(res, FULL, l_full)}
    check('WB1', 'the W1-c sentence at T1\' in ch19:198 and FULL:5270, with negative_allowance {finit: 1}: PASS, both '
          'lines', "both hits PASS and no item on either line", wb1,
          wb1['ch19'] == ['PASS'] and wb1['full'] == ['PASS'] and not wb1['items'])
    _, code, res = run({CH19: text.replace(s, s.replace('the notion of', 'the finite notion of', 1))})
    check('WB2', 'one more word containing finit in the fingerprinted sentence: FAIL rule-negative-match',
          "the line has rule-negative-match", items_at(res, CH19, ln), 'rule-negative-match' in items_at(res, CH19, ln))
    t3 = text.rstrip('\n') + '\n\n' + s + '\n'
    _, code, res = run({CH19: t3})
    end = len(t3.rstrip('\n').split('\n'))
    check('WB3', 'the fingerprinted sentence copied unchanged to another paragraph of a file in W1-c\'s scope: FAIL '
          'rule-negative-match at the copy; the original still PASS', "copy line rule-negative-match; original line "
          "no item", {'copy': items_at(res, CH19, end), 'original': items_at(res, CH19, ln)},
          'rule-negative-match' in items_at(res, CH19, end) and not items_at(res, CH19, ln))
    other = 'book/ch02-the-substratum.md' if a.repo.read(T, 'book/ch02-the-substratum.md') else \
        [p for p in a.repo.paths(T) if p.startswith('book/ch0') and p.endswith('.md')][0]
    ot = a.repo.read(T, other).decode().rstrip('\n') + '\n\n' + s + '\n'
    _, code, res = run({other: ot})
    end4 = len(ot.rstrip('\n').split('\n'))
    check('WB4', 'the fingerprinted sentence copied to a file outside every W1 rule\'s scope: REVIEW_REQUIRED '
          'unclassified', "the copy's line has unclassified and no FAIL class", {'file': other,
                                                                                 'items': items_at(res, other, end4)},
          items_at(res, other, end4) == ['unclassified'])
    t5 = text.replace(s + ' ', '', 1).rstrip('\n') + '\n\n' + s + '\n'
    _, code, res = run({CH19: t5})
    end5 = len(t5.rstrip('\n').split('\n'))
    stale = [i for i in res.get('items', []) if i['class'] == 'rule-stale' and i.get('rule_id') == 'W1-c']
    check('WB5', 'the fingerprinted sentence moved to another paragraph of the same file: FAIL rule-negative-match at the '
          'new location; REVIEW_REQUIRED rule-stale for the fingerprint', "new line rule-negative-match and a W1-c "
          "rule-stale item", {'new': items_at(res, CH19, end5), 'stale': len(stale)},
          'rule-negative-match' in items_at(res, CH19, end5) and len(stale) >= 1)
    _, code, res = run({CH19: text.replace(s, s.replace('periodic', 'cyclic', 1))})
    check('WB6', 'a near-copy at the fingerprinted location, one other word changed, one finit word kept: FAIL '
          'rule-negative-match', "the line has rule-negative-match", items_at(res, CH19, ln),
          'rule-negative-match' in items_at(res, CH19, ln))
    _, code, res = run({CH19: text.replace(s, s.replace('a finite periodic', 'a periodic', 1))})
    check('WB7', 'the fingerprinted sentence with its one finit word removed: REVIEW_REQUIRED rule-fingerprint-mismatch',
          "the line has rule-fingerprint-mismatch and no FAIL class", items_at(res, CH19, ln),
          items_at(res, CH19, ln) == ['rule-fingerprint-mismatch'])
    _, code, res = run({CH19: '\n' * 40 + text})
    check('WB8', 'the fingerprinted sentence and its neighbours shifted by 40 lines: PASS', "no item on the shifted line "
          "and its hit PASS", {'items': items_at(res, CH19, ln + 40), 'hit': hit_state(res, CH19, ln + 40)},
          not items_at(res, CH19, ln + 40) and hit_state(res, CH19, ln + 40) == ['PASS'])
    trio = '%s %s %s' % (prev, s, nxt)
    f9 = full.rstrip('\n') + '\n\n' + trio + '\n'
    _, code, res = run({FULL: f9})
    end9 = len(f9.rstrip('\n').split('\n'))
    check('WB9', 'two sentences matching one fingerprint in one file, so that one allowance is claimed twice: the '
          'claim at the larger byte offset gets no allowance (FAIL rule-negative-match)', "the later copy has "
          "rule-negative-match; the fingerprinted line has none", {'later': items_at(res, FULL, end9),
                                                               'fingerprinted': items_at(res, FULL, l_full)},
          'rule-negative-match' in items_at(res, FULL, end9) and not items_at(res, FULL, l_full))
    # WB10/WB11: lint through the pipeline: a mutated W1-c rule file gives record-invalid
    rp = a.ad + 'rules/w1-w2-allow-v1.json'
    base_rules = json.loads(a.repo.read(a.crev, rp))

    def with_w1c(mut):
        doc = copy.deepcopy(base_rules)
        for r in doc['rules']:
            if r['id'] == 'W1-c':
                mut(r)

        def repl(files):
            return [(ref, doc if ref['path'] == rp else d) for ref, d in files]
        _, code, res = run({}, control={'replace_rule_files': repl})
        return code, sorted({i['class'] for i in res.get('items', []) if i.get('subject') == rp})
    wb10 = {}
    for name, al in (('two', {'finit': 2}), ('zero', {'finit': 0}), ('axiom', {'axiom': 1})):
        def m(r, al=al):
            for f in r['fingerprints']:
                f['negative_allowance'] = dict(al)
        wb10[name] = with_w1c(m)
    check('WB10', 'lint: a W1-c allowance of 2, of 0, or naming axiom: FAIL record-invalid', "each mutant gives exit "
          "20 with record-invalid for the rule file", wb10,
          all(v[0] == 20 and v[1] == ['record-invalid'] for v in wb10.values()))

    def drop(r):
        for f in r['fingerprints']:
            f.pop('negative_allowance', None)
    wb11 = with_w1c(drop)
    check('WB11', 'lint: a rule whose fingerprinted sentence fails its own rule (W1-c with no allowance): FAIL '
          'record-invalid', "exit 20 with record-invalid for the rule file", wb11,
          wb11[0] == 20 and wb11[1] == ['record-invalid'])
    # WB12 is V7a (sec. 10.2: V2 with DR-3 removed from the profile set) on the W1-c sentence: item 7's profile set
    # less DR-3, so step 3 (the rule's negative matcher) is reached; deny-first order (sec. 6.2) is unchanged
    s12 = s.replace('of the bijection)', 'of the bijection, one of which is total finiteness,)', 1)
    cfg = json.loads(a.repo.read(a.crev, a.cpath))
    v7a = [n for n in [c for c in cfg['checks'] if c['id'] == 'item7'][0]['profiles'] if n != 'DR-3']
    _, code, res = run({CH19: text.replace(s, s12)}, profile=','.join(v7a))
    its = [(i['class'], str(i.get('rule_id'))) for i in res.get('items', [])
           if i.get('file') == CH19 and i.get('line') == ln]
    check('WB12', 'V7a on the W1-c sentence (", one of which is total finiteness,"): FAIL rule-negative-match',
          "profile set = item7 less DR-3 (%s); exit 20; the line has rule-negative-match of W1-c and no deny-match"
          % ','.join(v7a), {'exit': code, 'items': its},
          code == 20 and ('rule-negative-match', 'W1-c') in its and not [x for x in its if x[0] == 'deny-match'])
    lines = text.split('\n')
    para = lines[ln - 1]
    t13 = '\n'.join(lines[:ln - 1] + lines[ln:]).rstrip('\n') + '\n\n' + para + '\n'
    _, code, res = run({CH19: t13})
    end13 = len(t13.rstrip('\n').split('\n'))
    check('WB13', 'the fingerprinted sentence moved with both of its neighbours to another section of the same file: PASS',
          "the moved line has no item and its hit PASS; no W1-c rule-stale",
          {'items': items_at(res, CH19, end13), 'hit': hit_state(res, CH19, end13),
           'stale': [i['subject'] for i in res.get('items', []) if i['class'] == 'rule-stale']},
          not items_at(res, CH19, end13) and hit_state(res, CH19, end13) == ['PASS'] and
          not [i for i in res.get('items', []) if i['class'] == 'rule-stale' and i.get('rule_id') == 'W1-c'])
    t14 = text.rstrip('\n') + '\n\n' + trio + '\n'
    end14 = len(t14.rstrip('\n').split('\n'))
    runs = []
    for _ in range(2):
        _, code, res = run({CH19: t14})
        runs.append({'fingerprinted': items_at(res, CH19, ln), 'later': items_at(res, CH19, end14)})
    check('WB14', 'the fingerprinted sentence with both neighbours duplicated in the same file: the copy at the smaller '
          'byte offset PASSes, the later copy FAILs rule-negative-match, on every run',
          "in two runs: fingerprinted line no item, later copy rule-negative-match, identical", runs,
          runs[0] == runs[1] and not runs[0]['fingerprinted'] and 'rule-negative-match' in runs[0]['later'])
    _, code, res = run({CH19: text.replace(s, s.replace('the notion of', 'the Finiteness notion of', 1))})
    check('WB15', '"Finiteness" (capitalized) added to a W1 sentence at its fingerprinted location: FAIL '
          'rule-negative-match (case-insensitive negatives)', "the line has rule-negative-match",
          items_at(res, CH19, ln), 'rule-negative-match' in items_at(res, CH19, ln))


# ---- the per-edit unit and the plan checker's selection ------------------------------------------------------

def p_module(a):
    src = a.repo.read(P, PL + 'edits_check.py')
    mod = types.ModuleType('p_edits_check')
    mod.__file__ = os.path.join(tools, 'p_edits_check.py')
    exec(compile(src.decode('utf-8'), 'p_edits_check', 'exec'), mod.__dict__)
    return mod


def unit_of(a):
    loaded = a1c.cfgmod_loaded(a)
    params = peredit.find_params([(r, d) for r, d in loaded.rule_files])
    return peredit.Unit(params, loaded.profiles), params


def ours(unit, params, edits):
    units = [{'id': e['id'], 'file': e.get('file', 'f'), 'kind': e.get('kind'), 'pairs': le.pairs_of(e),
              'raw_keys': sorted(e)} for e in edits]
    res = unit.run(peredit.unit_pairs(units, params['pairs_key']))
    return {k: len(v) for k, v in res.items()}


def theirs(p, edits):
    inf, reg, caps, ids = p.static_new({'edits': edits})
    return {'register': len(reg), 'register-caps': len(caps), 'infinity': len(inf)}


def splice_for(text, e, pair):
    o, n = pair
    i = text.index(o)
    hb = len(text[:i].encode('utf-8'))
    return {'id': e['id'], 'file': 'f.md', 'start': hb, 'end': hb + len(o.encode('utf-8')),
            'old_sha256': sha(o.encode('utf-8')), 'new': n, 'new_bytes': n.encode('utf-8'),
            'new_sha256': sha(n.encode('utf-8'))}


def correspond(text, edits, splices):
    data = text.encode('utf-8')
    return le.correspondence(edits, splices, lambda c, f: data if f == 'f.md' else None, 'H')


def s11_controls(a):
    p = p_module(a)
    unit, params = unit_of(a)
    # S11-56: items 5 and 6 at T1' on P's edits.json
    code, res, _ = a.run(['terms', '--commit', T, '--base', H, '--ledger', a1c.LEDGER, '--check', 'item5'])
    ours56 = (res.get('per_edit') or {}).get('counts')
    edits = json.loads(a.repo.read(P, PL + 'edits.json'))['edits']
    theirs56 = theirs(p, edits)
    led = copy.deepcopy(a.led)
    led.update(le.load(a.repo.read(P, PL + 'ledger.json'), {'edits': a.repo.read(P, PL + 'edits.json'),
                                                             'checker': a.repo.read(P, PL + 'edits_check.py')}))
    mut5 = copy.deepcopy(led)
    mut5['edit_units'][0]['pairs'] = [[mut5['edit_units'][0]['pairs'][0][0],
                                       mut5['edit_units'][0]['pairs'][0][1] + ' This is now settled.']]
    mut6 = copy.deepcopy(led)
    mut6['edit_units'][1]['pairs'] = [[mut6['edit_units'][1]['pairs'][0][0],
                                       mut6['edit_units'][1]['pairs'][0][1] + ' The lattice is infinite.']]
    c5, r5, _ = a.run(['terms', '--commit', T, '--base', H, '--ledger', a1c.LEDGER, '--check', 'item5'],
                      control={'overrides': {'ledger': mut5}})
    c6, r6, _ = a.run(['terms', '--commit', T, '--base', H, '--ledger', a1c.LEDGER, '--check', 'item6'],
                      control={'overrides': {'ledger': mut6}})
    check('S11-56', 'items 5 and 6 at T1\': register, register-caps and infinity on P\'s per-edit unit give 0 '
          'findings each, equal to P\'s static_new on P\'s edits.json; the mutants of rows 5 and 6 FAIL',
          "the tool's per-edit counts equal P's (all 0) and both mutants exit 20 with deny-match",
          {'tool': ours56, 'P': theirs56, 'row5': (c5, (r5.get('per_edit') or {}).get('counts')),
           'row6': (c6, (r6.get('per_edit') or {}).get('counts'))},
          ours56 == theirs56 == {'register': 0, 'register-caps': 0, 'infinity': 0} and c5 == 20 and c6 == 20 and
          'deny-match' in {i['class'] for i in r5['items']} and 'deny-match' in {i['class'] for i in r6['items']})
    # S11-57a/b: a two-variant edit whose unapplied variant adds "now" / "no longer"
    out57 = {}
    for name, word, holder in (('a', 'now ', 'old'), ('b', 'no longer ', 'old'), ('b-H-holds-step2', 'no longer ',
                                                                                    'old_step2')):
        e = {'id': 'E1', 'file': 'f.md', 'kind': 'prose', 'old': 'The bound holds.', 'new': 'The bound holds.',
             'old_step2': 'The bound stays.', 'new_step2': 'The bound %sstays.' % word}
        text = 'Intro. %s End.' % (e['old'] if holder == 'old' else e['old_step2'])
        sel = le.select(e, text)
        ps = p.variant(e, text)
        sps = [] if sel[0] == sel[1] else [splice_for(text, e, sel)]
        errs = correspond(text, [e], sps)
        per_splice = ours(unit, params, [{'id': 'E1', 'kind': 'prose', 'old': sel[0], 'new': sel[1]}])
        out57[name] = {'tool': ours(unit, params, [e]), 'P': theirs(p, [e]), 'per_splice': per_splice,
                       'selected_equal': (sel[0], sel[1]) == (ps[0], ps[1]), 'refused': bool(errs)}
    check('S11-57a', 'a two-variant edit, selected variant unchanged, unapplied variant adds "now": FAIL deny-match '
          '(register), as P (register 1); the per-splice unit alone would PASS',
          "tool register == P register == 1 and the per-splice unit gives 0", out57['a'],
          out57['a']['tool']['register'] == out57['a']['P']['register'] == 1 and
          out57['a']['per_splice']['register'] == 0)
    check('S11-57b', 'the same with "no longer"; also at an H holding old_step2: FAIL deny-match, as P, at both',
          "tool equals P with register 1 at both, with P's selection", {k: out57[k] for k in ('b', 'b-H-holds-step2')},
          all(out57[k]['tool'] == out57[k]['P'] and out57[k]['tool']['register'] == 1 and out57[k]['selected_equal']
              for k in ('b', 'b-H-holds-step2')))
    # S11-57c: one splice covering two edits
    e1 = {'id': 'E1', 'file': 'f.md', 'kind': 'prose', 'old': 'It holds now.', 'new': 'It holds.'}
    e2 = {'id': 'E2', 'file': 'f.md', 'kind': 'prose', 'old': 'Next part.', 'new': 'Next part now.'}
    text = 'A. It holds now. Next part. B.'
    whole_old = 'It holds now. Next part.'
    i = text.index(whole_old)
    one = {'id': 'E1', 'file': 'f.md', 'start': i, 'end': i + len(whole_old), 'old_sha256': sha(whole_old.encode()),
           'new': 'It holds. Next part now.', 'new_bytes': b'It holds. Next part now.',
           'new_sha256': sha(b'It holds. Next part now.')}
    errs = correspond(text, [e1, e2], [one])
    check('S11-57c', 'one splice covering two edits (one deletes "now", the other adds it): ERROR SOURCE_CHANGED; '
          'evaluated per edit, FAIL deny-match (register), as P', "the correspondence refuses and the per-edit "
          "register count equals P's (1)", {'refusal': [m for _, m in errs][:3], 'tool': ours(unit, params, [e1, e2]),
                                           'P': theirs(p, [e1, e2])},
          bool(errs) and ours(unit, params, [e1, e2]) == theirs(p, [e1, e2]) and
          theirs(p, [e1, e2])['register'] == 1)
    e = {'id': 'E1', 'file': 'f.md', 'kind': 'prose', 'old': 'The bound holds.',
         'new': 'The bound holds; the lattice is infinite.'}
    check('S11-57d', '"The bound holds; the lattice is infinite." as an added pair: split as P\'s splitter does; the '
          'result equals P\'s static_new', "P's splitter gives two sentences and the tool's infinity count equals P's",
          {'split': unit.split.split(e['new']), 'tool': ours(unit, params, [e]), 'P': theirs(p, [e])},
          len(unit.split.split(e['new'])) == 2 and ours(unit, params, [e]) == theirs(p, [e]))
    # S11-58a-f: selection and refusal on one two-variant edit
    e = {'id': 'E1', 'file': 'f.md', 'kind': 'prose', 'old': 'alpha one.', 'new': 'alpha now one.',
         'old_step2': 'beta two.', 'new_step2': 'beta two now.'}
    cases = {'a': 'x alpha one. y', 'b': 'x beta two. y', 'c': 'x gamma. y', 'd': 'x alpha one. beta two. y',
             'e': 'x alpha one. alpha one. beta two. y', 'f': 'x alpha one. alpha one. beta two. beta two. y'}
    out58 = {}
    for k, text in cases.items():
        sel = le.select(e, text)
        ps = p.variant(e, text)
        sps = [splice_for(text, e, sel)] if sel else []
        errs = correspond(text, [e], sps)
        out58[k] = {'tool_selected': sel[0] if sel else None, 'P_selected': ps[0], 'refused': bool(errs),
                    'items_equal': ours(unit, params, [e]) == theirs(p, [e])}
    want = {'a': 'alpha one.', 'b': 'beta two.', 'c': None, 'd': 'alpha one.', 'e': 'beta two.', 'f': None}
    check('S11-58a-f', 'one two-variant edit with H holding old once, old_step2 only, neither, both once, old twice and '
          'old_step2 once, both ambiguous: selection, refusal (ERROR SOURCE_CHANGED in c and f) and items 5-6 equal '
          'to P\'s', "the tool's selection equals P's and the expected one in each case; refusal exactly in c and f; "
          "items equal", out58,
          all(out58[k]['tool_selected'] == out58[k]['P_selected'] == want[k] and out58[k]['refused'] == (k in 'cf')
              and out58[k]['items_equal'] for k in cases))
    text_g = cases['e']  # old twice, old_step2 once: P selects (old_step2, new_step2)
    errs_g = correspond(text_g, [e], [splice_for(text_g, e, (e['old'], e['new']))])
    check('S11-58g', 'a splice built for (old, new) while P selects (old_step2, new_step2): ERROR SOURCE_CHANGED',
          "the correspondence refuses", [m for _, m in errs_g][:2], bool(errs_g))
    e1 = {'id': 'E1', 'file': 'f.md', 'kind': 'prose', 'old': 'red fox', 'new': 'blue fox'}
    e2 = {'id': 'E2', 'file': 'f.md', 'kind': 'prose', 'old': 'red fox jumps', 'new': 'red fox runs'}
    text = 'the red fox jumps.'
    errs_h = correspond(text, [e1, e2], [splice_for(text, e1, ('red fox', 'blue fox'))])
    check('S11-58h', 'an earlier edit that destroys a later edit\'s old: ERROR SOURCE_CHANGED, as P reports the edit '
          'lost', "the correspondence refuses naming E2 as lost", [m for _, m in errs_h][:2],
          any(m.startswith('E2') and 'lost' in m for _, m in errs_h))
    e = {'id': 'E1', 'file': 'f.md', 'kind': 'prose', 'old': 'aa', 'new': 'b'}
    text = 'xaaay'
    sp = splice_for(text, e, ('aa', 'b'))
    errs_i = correspond(text, [e], [sp])
    check('S11-58i', 'old = "aa" in "xaaay" (non-overlapping count 1): selected at offset 1, as P selects; accepted',
          "selected, splice at offset 1, no refusal", {'start': sp['start'], 'refusal': [m for _, m in errs_i],
                                                       'P': p.variant(e, text)[2]},
          sp['start'] == 1 and not errs_i and p.variant(e, text)[0] == 'aa')
    e1 = {'id': 'E1', 'file': 'f.md', 'kind': 'prose', 'old': 'cat fox', 'new': 'fox cat'}
    e2 = {'id': 'E2', 'file': 'f.md', 'kind': 'prose', 'old': 'cat', 'new': 'dog'}
    text = 'cat fox.'
    errs_j = correspond(text, [e1, e2], [splice_for(text, e1, ('cat fox', 'fox cat'))])
    check('S11-58j', 'chained edits (edit 2\'s only occurrence after edit 1 lies inside edit 1\'s image): ERROR '
          'SOURCE_CHANGED naming edit 2 (chained); P\'s items 5 and 6 recorded', "a refusal naming E2 as chained",
          {'refusal': [m for _, m in errs_j][:2], 'P': theirs(p, [e1, e2])},
          any(m.startswith('E2') and 'chained' in m for _, m in errs_j))
    e1 = {'id': 'E1', 'file': 'f.md', 'kind': 'prose', 'old': 'ab q', 'new': 'xy'}
    e2 = {'id': 'E2', 'file': 'f.md', 'kind': 'prose', 'old': 'qc', 'new': 'Q', 'old_step2': 'yc', 'new_step2': 'Q'}
    text = 'ab qc'
    errs_k = correspond(text, [e1, e2], [splice_for(text, e1, ('ab q', 'xy'))])
    run = le.Running(text)
    run.replace_first('ab q', 'xy')
    p_text = text.replace('ab q', 'xy', 1)
    p_sel = p.variant(e2, p_text)
    p_text = p_text.replace(p_sel[0], p_sel[1], 1)
    check('S11-58k', 'chained across the image boundary (H "ab qc", edit 1 "ab q"->"xy", edit 2 qc/yc): ERROR '
          'SOURCE_CHANGED naming edit 2 (chained); P applies the list, with result "xQ"',
          "a refusal naming E2 as chained, and P's application gives 'xQ'",
          {'refusal': [m for _, m in errs_k][:2], 'P_result': p_text},
          any(m.startswith('E2') and 'chained' in m for _, m in errs_k) and p_text == 'xQ')


# ---- reconciliation N3-N18, R18, R19 on real objects ----------------------------------------------------------

class Recon:
    def __init__(self, a):
        self.a = a
        self.repo = a.repo
        loaded = a1c.cfgmod_loaded(a)
        self.ctx = pl.RunContext(a.repo, loaded.config, loaded.profiles, [], {}, None)
        self.led = le.load(a.repo.read(P, PL + 'ledger.json'), {'edits': a.repo.read(P, PL + 'edits.json')})
        self.path = 'AGENTS.md'
        m = a.repo.read(M, self.path)
        hdr = m.find(b'## \xc2\xa7A.49')
        self.protected = [(hdr, len(m))] if hdr > 0 else []
        self.classes = [self.cls('trial-workflow', '.github/workflows/a1exit-trial-verify.yml', M),
                        self.cls('tool-configuration', '.claude/settings.json', M)]
        self.rec = rc.draft(a.repo, self.ctx, H, M, T, self.led, self.path, self.protected, self.classes, {})

    def cls(self, cid, path, commit):
        return {'id': cid, 'pins': [{'path': path, 'git_blob': self.repo.blob_id(commit, path),
                                     'blob_sha256': sha(self.repo.read(commit, path))}]}

    def run(self, rec=None, m=M, L=None, h=H, classes=None, cand=False):
        e = exmod.Execution(self.ctx, h, T, self.led, None, m, L, T, classes if classes is not None else self.classes,
                            [rec] if rec else [])
        corp = set(self.ctx.corpus(H)) | set(self.ctx.corpus(m))
        e.main_role(set(self.led['files']) | corp)
        if L:
            e.landing()
        return e

    def failed(self, e):
        return [x for s_ in e.side_changes for ev in (s_.get('record_conditions') or []) for x in ev['failed']]


def n_controls(a):
    rcn = Recon(a)
    repo, path, rec = rcn.repo, rcn.path, rcn.rec
    comp = repo.read(M, path)
    e = rcn.run(rec)
    base = [i for i in e.items if i.get('file') == path]
    # N3 with the full candidate comparison
    ex = cli.candidate_with_and_without(rcn.ctx, H, T, rcn.led, None, M, None, T, rcn.classes, [rec])
    check('N3', 'a valid reconciliation record naming a ledgered path that X changes (AGENTS.md: D296 at X, a later '
          'section added on M): the record applies; no record-invalid; op C\'s items on X identical with and '
          'without it', "no item for AGENTS.md at M (RC1-RC13 hold), no record-invalid, and the with/without items on X "
          "are identical", {'items': [i['class'] for i in base], 'failed': rcn.failed(e),
                            'x_identity': ex.x_identity,
                            'record_invalid': [i for i in ex.items if i['class'] == 'record-invalid']},
          not base and not rcn.failed(e) and ex.x_identity['identical'] and
          not [i for i in ex.items if i['class'] == 'record-invalid'])

    def named(cid, expected, cond, mut_rec=None, **kw):
        r = mut_rec(copy.deepcopy(rec)) if mut_rec else rec
        e_ = rcn.run(r, **kw)
        f = rcn.failed(e_)
        drift = [i for i in e_.items if i['class'] == 'base-drift' and i.get('file') == path]
        check(cid, expected, "the record does not apply: base-drift for AGENTS.md, and the failed conditions include "
              + cond, {'failed': f, 'base_drift': bool(drift)}, cond in f and bool(drift))
        return e_

    def entry(r, **upd):
        r['paths'][0].update(upd)
        return r
    named('N4', 'the record with its ledger_binding altered by one byte: does not apply (base-drift), naming RC13',
          'RC13', lambda r: dict(r, ledger_binding=dict(r['ledger_binding'], files_entry_sha256='0' + r[
              'ledger_binding']['files_entry_sha256'][1:])))
    M5 = repo.derive(M, {path: comp + b'\n'}, parents=[M], subject='one more main commit')
    named('N5', 'M with one more first-parent commit changing the path: does not apply, naming RC1', 'RC1', m=M5)
    named('N6', 'a protected range at M altered by one byte (the recorded range shifted by one byte): does not '
          'apply, naming RC9', 'RC9', lambda r: entry(r, protected=[dict(r['paths'][0]['protected'][0],
                                                                       start_M=r['paths'][0]['protected'][0]['start_M']
                                                                       + 1)]))
    named('N7', 'the path\'s blob at M differs from the record\'s m: does not apply, naming RC2', 'RC2',
          lambda r: entry(r, m='0' * 40))
    old = repo.read(H, path)[rcn.led['splices'][[s['file'] for s in rcn.led['splices']].index(path)]['start']:
                             rcn.led['splices'][[s['file'] for s in rcn.led['splices']].index(path)]['end']]
    M8 = repo.derive(M, {path: comp + b'\n' + old + b'\n'}, parents=[M], subject='old bytes twice at M')
    named('N8', 'a splice\'s old bytes occurring twice at M: does not apply, naming RC4', 'RC4', m=M8)
    named('N9', 'the record\'s l differs from the composed blob: does not apply, naming RC7', 'RC7',
          lambda r: entry(r, l='0' * 40))
    H12 = repo.derive(H, {path: repo.read(H, path) + b'\n' + old + b'\n'}, parents=repo.parents(H),
                      subject='old bytes twice at H (synthetic copy)')
    e12 = exmod.Execution(rcn.ctx, H12, T, rcn.led, None, M, None, T, rcn.classes, [rec])
    ev12 = rc.evaluate(repo, rcn.ctx, H12, M, T, rcn.led, rec, rec['paths'][0], rcn.classes, {})
    check('N12', 'the record\'s RC3: D296\'s old bytes made to occur twice at H in a synthetic copy: does not apply, '
          'naming RC3', "the evaluated failed conditions include RC3", ev12['failed'], 'RC3' in ev12['failed'])
    M13 = repo.derive(M, {path: b'inserted line\n' + comp}, parents=[M], subject='insertion before D296')
    named('N13', 'an insertion on M before D296\'s offset while the record states the identity translation: does not '
          'apply, naming RC5', 'RC5', m=M13)
    named('N14', 'the record\'s approved text differs from the ledger\'s new: does not apply, naming RC6', 'RC6',
          lambda r: entry(r, splices=[dict(r['paths'][0]['splices'][0], new_sha256='0' * 64)]))
    named('N15', 'the record\'s x differs from the ledger\'s expected_sha256 for the path: does not apply, naming RC8',
          'RC8', lambda r: entry(r, x_sha256='0' * 64))
    other = [f for f in rcn.led['files'] if f != path and f.startswith('papers/')][0]
    M16 = repo.derive(M, {other: repo.read(M, other) + b'\n'}, parents=[M], subject='another ledgered file')
    e16 = named('N16', 'another ledgered file changed on M: does not apply, naming RC10; that file is base-drift',
                'RC10', m=M16)
    check('N16-file', 'the other ledgered file is base-drift', "base-drift for that file",
          other, any(i['class'] == 'base-drift' and i.get('file') == other for i in e16.items))
    M17 = repo.derive(M, {'x/unclassified.txt': b'x\n'}, parents=[M], subject='unclassified path')
    named('N17', 'a changed path on M not covered by a pinned class: does not apply, naming RC11', 'RC11', m=M17)
    e18 = named('N18', 'the record\'s changes_decisions_on_X non-empty: does not apply, naming RC12; the record is '
                'record-invalid', 'RC12', lambda r: dict(r, changes_decisions_on_X=['a decision']))
    check('N18-record', 'the record is record-invalid', "a record-invalid item", [i['class'] for i in e18.items],
          'record-invalid' in [i['class'] for i in e18.items])
    # N10 and N11: the S6 probe, pinned
    x_blob = repo.blob_id(T, path)
    L10 = repo.derive(M, {path: repo.read(T, path)}, parents=[M, T], subject='landing keeping X\'s AGENTS.md')
    rec10 = entry(copy.deepcopy(rec), l=x_blob)
    e10 = rcn.run(rec10, L=L10)
    comp_blob = rc.blob_id_of(rc.compose(repo, H, M, path, [s for s in rcn.led['splices'] if s['file'] == path])[0])
    cl10 = sorted({i['class'] for i in e10.items if path in (i.get('file') or '') or path in str(i.get('subject'))})
    check('N10', 'M = 8e9b8334, X = T1\', L\'s AGENTS.md = X\'s blob 9f4fc3e8 (drops M\'s inserted section), a record '
          'whose l names that blob; reference composition 86d79863: FAIL landing-conflict-unresolved for AGENTS.md '
          'and record-invalid for the record; the composition is evaluated regardless of the record',
          "x blob 9f4fc3e8..., composed blob 86d79863..., and both classes for AGENTS.md",
          {'x_blob': x_blob, 'composed': comp_blob, 'classes': cl10, 'm_blob': repo.blob_id(M, path)},
          x_blob == '9f4fc3e830707c90ffc105842d26d5b51f01760b' and
          comp_blob == '86d79863821f3f8cdad86771008b2df89fd1961a' and
          repo.blob_id(M, path).startswith('6b1280fa') and
          'landing-conflict-unresolved' in cl10 and 'record-invalid' in cl10)
    L11 = exmod.compose_landing(repo, H, M, T, rcn.led, repo)
    e11 = rcn.run(rec, L=L11)
    cl11 = [i['class'] for i in e11.items if path in (i.get('file') or '') or path in str(i.get('subject'))]
    check('N11', 'the same M, X and reference, L\'s AGENTS.md equal to 86d79863 and the record\'s l equal to it: PASS '
          'for the path', "L's blob is 86d79863... and no item names AGENTS.md",
          {'l_blob': repo.blob_id(L11, path), 'items': cl11},
          repo.blob_id(L11, path) == '86d79863821f3f8cdad86771008b2df89fd1961a' and not cl11)
    # the configuration route (owner: the record is frozen with the plan and referenced by the configuration)
    cfg = json.loads(repo.read(a.crev, a.cpath))
    classes_doc = {'schema': 'oi-side-change-classes/1', 'record_id': 'n3-classes', 'author': 'control-writer',
                   'supersedes': None, 'classes': rcn.classes}
    rp, cp = a.ad + 'records/n3-reconciliation.json', a.ad + 'records/n3-classes.json'
    rb, cb = (json.dumps(rec, indent=1) + '\n').encode(), (json.dumps(classes_doc, indent=1) + '\n').encode()
    cfg['records'] = [r_ for r_ in cfg['records'] if r_.get('kind') != 'side-change-classes'] + [
        {'kind': 'side-change-classes', 'path': cp, 'blob_sha256': sha(cb)},
        {'kind': 'reconciliation', 'path': rp, 'blob_sha256': sha(rb)}]
    cfg['roles']['side_change_classes'] = {'path': cp, 'blob_sha256': sha(cb)}
    cfgb = (json.dumps(cfg, indent=1, ensure_ascii=False) + '\n').encode()
    c2 = repo.derive(a.crev, {rp: rb, cp: cb, a.cpath: cfgb}, parents=repo.parents(a.crev), subject='route')
    old_c, old_s = a.crev, a.csha
    a.crev, a.csha = c2, sha(cfgb)
    try:
        code, res, _ = a.run(['execution', '--scientific-base', H, '--candidate', T, '--ledger', a1c.LEDGER,
                              '--edits', a1c.EDITS, '--delegation', '%s:%sdelegation-draft.json' % (c2, a.ad),
                              '--main', M, '--landing', L11])
    finally:
        a.crev, a.csha = old_c, old_s
    on = [i['class'] for i in res.get('items', []) if path in str(i.get('file')) or path in str(i.get('subject'))]
    check('N3-config-route', 'a reconciliation record referenced by the configuration (frozen with the plan) is loaded '
          'from it: AGENTS.md is reconciled at M and composed at the landing', "op C (harness) gives no item naming "
          "AGENTS.md and records the composition 86d79863...", {'exit': code, 'items': on, 'stop': (res.get('stop') or
                                                                                                    {}).get('message'),
                                                                 'compositions': res.get('landing_compositions')},
          not on and any(x.get('composed_blob') == '86d79863821f3f8cdad86771008b2df89fd1961a'
                         for x in res.get('landing_compositions') or []))
    # R18, R19
    bad = [dict(rcn.classes[0], pins=[dict(rcn.classes[0]['pins'][0], blob_sha256='0' * 64)]), rcn.classes[1]]
    e18c = rcn.run(rec, classes=bad)
    check('R18', 'a classified side-change path whose blob at M differs from its class pin: REVIEW_REQUIRED '
          'side-change-unclassified', "side-change-unclassified for the workflow path",
          [i['class'] for i in e18c.items], any(i['class'] == 'side-change-unclassified' and
                                                 i.get('file') == '.github/workflows/a1exit-trial-verify.yml'
                                                 for i in e18c.items))
    M19 = repo.derive(M, {'tools/ledger_coverage/extra.py': b'x = 1\n', 'tools/ledger_coverage/listed.py': b'y\n'},
                      parents=[M], subject='tool landing on M')
    tool = {'id': 'tool-landing', 'prefixes': ['tools/ledger_coverage/'],
            'pins': [{'path': 'tools/ledger_coverage/listed.py', 'git_blob': None, 'blob_sha256': '0' * 64}]}
    e19 = rcn.run(None, m=M19, classes=rcn.classes + [tool])
    u19 = sorted(i.get('file') for i in e19.items if i['class'] == 'side-change-unclassified')
    check('R19', 'a path under the tool-landing prefix on M that the class does not list, and separately a listed path '
          'whose blob differs from its pin: REVIEW_REQUIRED side-change-unclassified each',
          "side-change-unclassified for both tool paths", u19,
          u19 == ['tools/ledger_coverage/extra.py', 'tools/ledger_coverage/listed.py'])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', required=True)
    ap.add_argument('--config', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--only', default=None)
    ap.add_argument('--staged-config', default=None,
                    help='the staged configuration file; --config REV:PATH names its path in the plan directory')
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)
    a = a1c.A1(args.repo, args.config, args.out, args.staged_config)
    groups = [('WB', wb_controls), ('S11', s11_controls), ('N', n_controls)]
    for name, fn in groups:
        if args.only and name not in args.only.split(','):
            continue
        try:
            fn(a)
        except Exception as exc:
            import traceback
            RESULTS.append({'id': '%s-group' % name, 'expected': 'the group runs', 'predicate': None,
                            'actual': '%s: %s %s' % (type(exc).__name__, exc, traceback.format_exc()[-1500:]),
                            'status': 'FAIL'})
    summary = {}
    for r in RESULTS:
        summary[r['status']] = summary.get(r['status'], 0) + 1
    doc = {'schema': 'oi-control-report/1', 'controls': sorted(RESULTS, key=lambda x: x['id']), 'summary': summary}
    with open(os.path.join(args.out, 'a1-conformance.json'), 'w', encoding='utf-8') as f:
        f.write(json.dumps(doc, indent=1, sort_keys=True, default=str) + '\n')
    print(json.dumps(summary, sort_keys=True))
    for r in doc['controls']:
        if r['status'] != 'PASS':
            print(r['status'], r['id'], json.dumps(r['actual'], default=str)[:400])


if __name__ == '__main__':
    main()
