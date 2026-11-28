"""A1 controls of the design (v6.0e) on real objects: W1 option B (WB1-WB15), the per-edit unit and
the plan checker's selection (S11-56, S11-57a-d, S11-58a-k), the reconciliation conditions and the landing
composition (N3-N18, with N10 and N11 pinned to main 8e9b8334 and the representative build), and the side-change classes (R18,
R19). Every run uses the control harness (the A1 records are unreviewed drafts); mutant trees, ledgers and
records exist only in memory. Each control is reported as {id, expected, predicate, actual, status}.

Usage: python3 -I -B tools/ledger_coverage/adapters/a1_conformance.py --repo DIR --config REV:PATH --staged-config FILE
       --out DIR [--tool-revision HEAD] [--fixed-config REV:PATH] (see a1_controls.py for the configuration path)
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
from ledger_coverage.engine import outcome as oc, rules as rulemod, util  # noqa: E402
from ledger_coverage.adapters import a1_controls as a1c, a1exit_exact_edit as le  # noqa: E402
from ledger_coverage.adapters import control_records  # noqa: E402

H, T, P, E = a1c.H, a1c.T, a1c.P, a1c.E
PL = a1c.PL
M = '8e9b83341cf5bc7fd9fb260892d0385fc9bfab4d'
CH19 = 'book/ch19-open-problems.md'
FULL = a1c.FULL
RESULTS = []
# the writer's scientific effect of the control fixture records (design r6 amendment 3, R6.RECON.25)
CONTROL_EFFECT = {'conclusions': 'none', 'assessment': 'control fixture: the change on main touches no planned edit',
                  'method': 'control: every condition recomputed from git objects', 'verdict': 'no-effect'}
# R6.GATE.7: the tool runs (and in-process stage results) captured since the previous check are its evidence
REC = None
RUNS = {}
FILES = {}


# per control id: the procedure of its manifest (R6.GATE.8)
PROCS = {}


def check(cid, expected, predicate, actual, holds):
    RESULTS.append({'id': cid, 'expected': expected, 'predicate': predicate, 'actual': actual,
                    'status': 'PASS' if holds else 'FAIL'})
    if REC is not None:
        RUNS.setdefault(cid, []).extend(REC.take())


def exec_doc(e, label, attested=None):
    """Captures an in-process Execution's items, side changes and compositions as a stage result."""
    if REC is not None:
        e.captured = REC.capture_doc(label, control_records.stage_doc(
            e.items, operation='execution', side_changes=getattr(e, 'side_changes', None),
            landing_compositions=getattr(e, 'compositions', None)), attested=attested(e) if callable(attested)
            else attested)
    return e


def sha(b):
    return util.sha256(b)


def w1c_sentence(a, commit, path):
    rules = json.loads(a.repo.read(a.crev, a1c.allow_rule_path(a, 'W1-c')))
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

    def run(files, extra=(), control=None, profile=None, bindings=None, mutation=None):
        x = a.repo.derive(T, {k: v.encode() for k, v in files.items()}, parents=[H], subject='WB')
        sel = ['--profile', profile] if profile else ['--check', 'item7']
        if bindings is not None and mutation is None:
            mutation = [{'path': path, 'before': a.repo.blob_id(T, path), 'after': a.repo.blob_id(x, path)}
                        for path in sorted(files)]
        code, res, _ = a.run(['terms', '--commit', x] + sel + list(extra), control=control,
                             bindings=bindings, mutation=mutation)
        return x, code, res
    # the clean baseline of the restored cases (OBL-20): the unmutated tree, the same command and flags
    run({})
    clean = REC.name_last('baseline') if REC is not None else None

    def wb_check(cid, *args, profile=None, clean_run=None):
        # the restored case of every WB row: the same run on the unmutated tree, compared with the clean baseline
        run({}, profile=profile)
        if REC is not None:
            REC.name_last('restored', baseline=clean if clean_run is None else clean_run)
        return check(cid, *args)
    _, code, res = run({})
    l_full = line_of(full, s)
    wb1 = {'ch19': hit_state(res, CH19, ln), 'full': hit_state(res, FULL, l_full),
           'items': items_at(res, CH19, ln) + items_at(res, FULL, l_full)}
    wb_check('WB1', 'the W1-c sentence at T1\' in ch19:198 and FULL:5270, with negative_allowance {finit: 1}: PASS, both '
          'lines', "both hits PASS and no item on either line", wb1,
          wb1['ch19'] == ['PASS'] and wb1['full'] == ['PASS'] and not wb1['items'])
    x, code, res = run({CH19: text.replace(s, s.replace('the notion of', 'the finite notion of', 1))})
    if REC is not None:
        REC.name_last('', bindings={'planted': '%s:%d' % (CH19, ln)},
                      mutation=[{'path': CH19, 'before': a.repo.blob_id(T, CH19),
                                 'after': a.repo.blob_id(x, CH19)}])
    wb_check('WB2', 'one more word containing finit in the fingerprinted sentence: FAIL rule-negative-match',
          "the line has rule-negative-match", items_at(res, CH19, ln), 'rule-negative-match' in items_at(res, CH19, ln))
    t3 = text.rstrip('\n') + '\n\n' + s + '\n'
    _, code, res = run({CH19: t3})
    end = len(t3.rstrip('\n').split('\n'))
    wb_check('WB3', 'the fingerprinted sentence copied unchanged to another paragraph of a file in W1-c\'s scope: FAIL '
          'rule-negative-match at the copy; the original still PASS', "copy line rule-negative-match; original line "
          "no item", {'copy': items_at(res, CH19, end), 'original': items_at(res, CH19, ln)},
          'rule-negative-match' in items_at(res, CH19, end) and not items_at(res, CH19, ln))
    other = 'book/ch02-the-substratum.md' if a.repo.read(T, 'book/ch02-the-substratum.md') else \
        [p for p in a.repo.paths(T) if p.startswith('book/ch0') and p.endswith('.md')][0]
    ot = a.repo.read(T, other).decode().rstrip('\n') + '\n\n' + s + '\n'
    _, code, res = run({other: ot})
    end4 = len(ot.rstrip('\n').split('\n'))
    wb_check('WB4', 'the fingerprinted sentence copied to a file outside every W1 rule\'s scope: REVIEW_REQUIRED '
          'unclassified', "the copy's line has unclassified and no FAIL class", {'file': other,
                                                                                 'items': items_at(res, other, end4)},
          items_at(res, other, end4) == ['unclassified'])
    t5 = text.replace(s + ' ', '', 1).rstrip('\n') + '\n\n' + s + '\n'
    _, code, res = run({CH19: t5})
    end5 = len(t5.rstrip('\n').split('\n'))
    stale = [i for i in res.get('items', []) if i['class'] == 'rule-stale' and i.get('rule_id') == 'W1-c']
    wb_check('WB5', 'the fingerprinted sentence moved to another paragraph of the same file: FAIL rule-negative-match at the '
          'new location; REVIEW_REQUIRED rule-stale for the fingerprint', "new line rule-negative-match and a W1-c "
          "rule-stale item", {'new': items_at(res, CH19, end5), 'stale': len(stale)},
          'rule-negative-match' in items_at(res, CH19, end5) and len(stale) >= 1)
    planted = {'planted': '%s:%d' % (CH19, ln)}
    _, code, res = run({CH19: text.replace(s, s.replace('periodic', 'cyclic', 1))}, bindings=planted)
    wb_check('WB6', 'a near-copy at the fingerprinted location, one other word changed, one finit word kept: FAIL '
          'rule-negative-match', "the line has rule-negative-match", items_at(res, CH19, ln),
          'rule-negative-match' in items_at(res, CH19, ln))
    _, code, res = run({CH19: text.replace(s, s.replace('a finite periodic', 'a periodic', 1))}, bindings=planted)
    wb_check('WB7', 'the fingerprinted sentence with its one finit word removed: REVIEW_REQUIRED rule-fingerprint-mismatch',
          "the line has rule-fingerprint-mismatch and no FAIL class", items_at(res, CH19, ln),
          items_at(res, CH19, ln) == ['rule-fingerprint-mismatch'])
    _, code, res = run({CH19: '\n' * 40 + text})
    wb_check('WB8', 'the fingerprinted sentence and its neighbours shifted by 40 lines: PASS', "no item on the shifted line "
          "and its hit PASS", {'items': items_at(res, CH19, ln + 40), 'hit': hit_state(res, CH19, ln + 40)},
          not items_at(res, CH19, ln + 40) and hit_state(res, CH19, ln + 40) == ['PASS'])
    trio = '%s %s %s' % (prev, s, nxt)
    f9 = full.rstrip('\n') + '\n\n' + trio + '\n'
    _, code, res = run({FULL: f9})
    end9 = len(f9.rstrip('\n').split('\n'))
    wb_check('WB9', 'two sentences matching one fingerprint in one file, so that one allowance is claimed twice: the '
          'claim at the larger byte offset gets no allowance (FAIL rule-negative-match)', "the later copy has "
          "rule-negative-match; the fingerprinted line has none", {'later': items_at(res, FULL, end9),
                                                               'fingerprinted': items_at(res, FULL, l_full)},
          'rule-negative-match' in items_at(res, FULL, end9) and not items_at(res, FULL, l_full))
    # WB10/WB11: lint through the pipeline: a mutated W1-c rule file gives record-invalid
    rp = a1c.allow_rule_path(a, 'W1-c')
    base_rules = json.loads(a.repo.read(a.crev, rp))

    def with_w1c(mut, retain_mutation=False):
        doc = copy.deepcopy(base_rules)
        for r in doc['rules']:
            if r['id'] == 'W1-c':
                mut(r)
        bindings, mutation = None, None
        if retain_mutation:
            variant = a.repo.derive(a.crev, {rp: util.canonical(doc)}, parents=[a.crev], subject='WB rule mutation')
            doc = json.loads(a.repo.read(variant, rp))
            bindings = {'rule_file': rp}
            mutation = [{'path': rp, 'before': a.repo.blob_id(a.crev, rp), 'after': a.repo.blob_id(variant, rp)}]

        def repl(files):
            return [(ref, doc if ref['path'] == rp else d) for ref, d in files]
        _, code, res = run({}, control={'replace_rule_files': repl}, bindings=bindings, mutation=mutation)
        return code, sorted({i['class'] for i in res.get('items', []) if i.get('subject') == rp})
    wb10 = {}
    for name, al in (('two', {'finit': 2}), ('zero', {'finit': 0}), ('axiom', {'axiom': 1})):
        def m(r, al=al):
            for f in r['fingerprints']:
                f['negative_allowance'] = dict(al)
        wb10[name] = with_w1c(m)
    wb_check('WB10', 'lint: a W1-c allowance of 2, of 0, or naming axiom: FAIL record-invalid', "each mutant gives exit "
          "20 with record-invalid for the rule file", wb10,
          all(v[0] == 20 and v[1] == ['record-invalid'] for v in wb10.values()))

    def drop(r):
        for f in r['fingerprints']:
            f.pop('negative_allowance', None)
    wb11 = with_w1c(drop, retain_mutation=True)
    wb_check('WB11', 'lint: a rule whose fingerprinted sentence fails its own rule (W1-c with no allowance): FAIL '
          'record-invalid', "exit 20 with record-invalid for the rule file", wb11,
          wb11[0] == 20 and wb11[1] == ['record-invalid'])
    # WB12 is V7a (sec. 10.2: V2 with DR-3 removed from the profile set) on the W1-c sentence: item 7's profile set
    # less DR-3, so step 3 (the rule's negative matcher) is reached; deny-first order (sec. 6.2) is unchanged
    s12 = s.replace('of the bijection)', 'of the bijection, one of which is total finiteness,)', 1)
    profile = a1c.item7_without_dr3(a)
    run({}, profile=profile)
    clean_wb12 = REC.name_last('baseline') if REC is not None else None
    _, code, res = run({CH19: text.replace(s, s12)}, profile=profile, bindings=planted)
    its = [(i['class'], str(i.get('rule_id'))) for i in res.get('items', [])
           if i.get('file') == CH19 and i.get('line') == ln]
    wb_check('WB12', 'V7a on the W1-c sentence (", one of which is total finiteness,"): FAIL rule-negative-match',
          "profile set = item7 less DR-3 (%s); exit 20; the line has rule-negative-match of W1-c and no deny-match"
          % profile, {'exit': code, 'items': its},
          code == 20 and ('rule-negative-match', 'W1-c') in its and not [x for x in its if x[0] == 'deny-match'],
          profile=profile, clean_run=clean_wb12)
    lines = text.split('\n')
    para = lines[ln - 1]
    t13 = '\n'.join(lines[:ln - 1] + lines[ln:]).rstrip('\n') + '\n\n' + para + '\n'
    _, code, res = run({CH19: t13})
    end13 = len(t13.rstrip('\n').split('\n'))
    wb_check('WB13', 'the fingerprinted sentence moved with both of its neighbours to another section of the same file: PASS',
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
    wb_check('WB14', 'the fingerprinted sentence with both neighbours duplicated in the same file: the copy at the smaller '
          'byte offset PASSes, the later copy FAILs rule-negative-match, on every run',
          "in two runs: fingerprinted line no item, later copy rule-negative-match, identical", runs,
          runs[0] == runs[1] and not runs[0]['fingerprinted'] and 'rule-negative-match' in runs[0]['later'])
    _, code, res = run({CH19: text.replace(s, s.replace('the notion of', 'the Finiteness notion of', 1))},
                       bindings=planted)
    wb_check('WB15', '"Finiteness" (capitalized) added to a W1 sentence at its fingerprinted location: FAIL '
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
        self.repo = a.repo
        loaded = a1c.cfgmod_loaded(a)
        self.ctx = pl.RunContext(a.repo, loaded.config, loaded.profiles, [], {}, None)
        self.led = le.load(a.repo.read(P, PL + 'ledger.json'), {'edits': a.repo.read(P, PL + 'edits.json')})
        self.path = 'AGENTS.md'
        self.protected, self.classes = reconciliation_scope(a.repo, self.path)
        self.rec = rc.draft(a.repo, self.ctx, H, M, T, self.led, self.path, self.protected, self.classes, {},
                            scientific_effect=CONTROL_EFFECT)

    def run(self, rec=None, m=M, L=None, h=H, classes=None, x=T):
        e = reconcile_execution(self.ctx, h, m, x, self.led, classes if classes is not None else self.classes, rec, L)
        return exec_doc(e, 'execution main role%s (a1_conformance.Recon.run)' % (' and landing' if L else ''))

    def failed(self, e):
        return [x for s_ in e.side_changes for ev in (s_.get('record_conditions') or []) for x in ev['failed']]


def reconciliation_scope(repo, path):
    main = repo.read(M, path)
    hdr = main.find(b'## \xc2\xa7A.49')
    protected = [(hdr, len(main))] if hdr > 0 else []
    classes = []
    for cid, p in (('trial-workflow', a1c.WF), ('tool-configuration', '.claude/settings.json')):
        classes.append({'id': cid, 'pins': [{'path': p, 'git_blob': repo.blob_id(M, p),
                                            'blob_sha256': sha(repo.read(M, p))}]})
    return protected, classes


def reconcile_execution(ctx, h, m, x, ledger, classes, record, landing):
    e = exmod.Execution(ctx, h, x, ledger, None, m, landing, x, classes, [record] if record else [])
    e.main_role(set(ledger['files']) | set(ctx.corpus(h)) | set(ctx.corpus(m)))
    if landing:
        e.landing()
    return e


class FixedReads(a1c.ReadLog):
    """Keep actual input reads as well as the X_rep scope attribution."""

    def __init__(self, repo, candidate=None):
        super().__init__(repo, candidate)
        self.by_commit = {}

    def read(self, cid, path):
        self.by_commit.setdefault(cid, set()).add(path)
        return super().read(cid, path)

    def evidence(self):
        return {'paths': {cid: sorted(paths) for cid, paths in sorted(self.by_commit.items())},
                'blobs': sorted(self.blobs)}


def n10_n11(a):
    """Evaluate the fixed representative pair with one explicit configuration and one ledger/edit pair."""
    fixed = copy.copy(a)
    fixed.main = a.base.resolve(M)
    build_reads = fixed.base = fixed.repo = FixedReads(a.repo)
    path = 'AGENTS.md'
    config_bytes = build_reads.read(a.crev, a.cpath)
    config = json.loads(config_bytes)
    ledger_bytes, edits_bytes, delegation = a1c.rep_inputs(fixed)
    ledger = le.load(ledger_bytes, {'edits': edits_bytes})
    h = ledger['base']
    roles = config['roles']
    if ledger['errors'] or h != H or roles['scientific_base'] != h or roles['record_commit'] != h or roles['pin'] != E:
        raise a1c.RepRefused('N10/N11 require the fixed representative ledger base and configuration roles')
    build_reads.resolve(E)
    if sha(config_bytes) != a.csha or build_reads.mode(a.crev, a.cpath) != '100644':
        raise a1c.RepRefused('N10/N11 configuration differs from the selected regular-file input')
    # Check the same source pair against both of its build outputs and both landing inputs.
    inputs = {}
    for name, data, blob, digest in (
            ('ledger', ledger_bytes, a1c.REP_LEDGER_GIT, '2055e68f2343d00cec93bc35ecbccae21d46d1da154ee1a842663f1e4fec32b5'),
            ('edits', edits_bytes, a1c.REP_EDITS_GIT, '528f146d03b29cbc3d7dc29948e3dd1d4cd26f4d36e6e009f032e24f9462dec1')):
        source = a.ad + 'rep/' + name + '.json'
        if build_reads.entries(a.tool_rev).get(source) != ('100644', blob) or sha(data) != digest:
            raise a1c.RepRefused('N10/N11 tool revision does not carry the pinned %s mode and bytes' % name)
        inputs[name] = {'path': source, 'copy_at': PL + name + '.json', 'mode': '100644', 'git_blob': blob,
                        'blob_sha256': digest}
    dref = config['delegation']
    delegation_bytes = build_reads.read(a.crev, dref['path'])
    if dref.get('commit') not in (None, a.crev) or delegation_bytes is None or \
            sha(delegation_bytes) != dref['blob_sha256'] or build_reads.mode(a.crev, dref['path']) != '100644':
        raise a1c.RepRefused('N10/N11 require the pinned regular-file delegation')
    source = 'tools/ledger_coverage/adapters/rep_build.py'
    source_bytes = build_reads.read(a.tool_rev, source)
    builder_pins = [ref['blob_sha256'] for ref in config['tool']['files'] if ref['path'] == source]
    if source_bytes is None or build_reads.mode(a.tool_rev, source) != '100644' or builder_pins != [sha(source_bytes)]:
        raise a1c.RepRefused('N10/N11 representative builder differs from its configuration pin')
    runner_path = 'tools/ledger_coverage/adapters/a1_conformance.py'
    runner_bytes = build_reads.read(a.tool_rev, runner_path)
    with open(__file__, 'rb') as f:
        if runner_bytes != f.read() or build_reads.mode(a.tool_rev, runner_path) != '100644':
            raise a1c.RepRefused('N10/N11 runner bytes differ from the tool revision')
    builder, imports = a1c.rep_builder(source_bytes)
    x, changes = a1c.build_x_rep(fixed, source=source_bytes)
    problems = a1c.rep_conforms(fixed, x, changes)
    if problems:
        raise a1c.RepRefused('N10/N11 representative build differs: %s' % '; '.join(problems))

    def entry(repo, commit, p):
        return {'commit': commit, 'path': p, 'mode': repo.mode(commit, p), 'git_blob': repo.blob_id(commit, p)}

    markers = []
    for p in builder.delegated_paths(delegation):
        if p in ledger['files']:
            continue
        base, main, candidate = [entry(build_reads, rev, p) for rev in (h, M, x)]
        marker = build_reads.read(x, p)
        if candidate['mode'] != '100644' or marker != builder.MARKER % p.encode('utf-8') or \
                marker in (build_reads.read(h, p), build_reads.read(M, p)):
            raise a1c.RepRefused('N10/N11 representative marker differs from its law at %s' % p)
        markers.append({'H_rep': base, 'M': main, 'X_rep': candidate, 'blob_sha256': sha(marker)})
    if not markers:
        raise a1c.RepRefused('N10/N11 require the delegated-path markers')

    setup = FixedReads(a.repo, x)
    ctx = pl.RunContext(setup, config, {}, [], {}, None)
    protected, classes = reconciliation_scope(setup, path)
    good_record = rc.draft(setup, ctx, h, M, x, ledger, path, protected, classes, {}, scientific_effect=CONTROL_EFFECT)
    correct = exmod.compose_landing(setup, h, M, x, ledger, a.repo)
    wrong = a.repo.derive(correct, {path: setup.read(x, path)}, parents=[M, x], subject='landing keeping X\'s AGENTS.md')
    wrong_record = copy.deepcopy(good_record)
    wrong_record['paths'][0]['l'] = setup.blob_id(x, path)
    wrong_entries, correct_entries = setup.entries(wrong), setup.entries(correct)
    pair_delta = sorted(p for p in set(wrong_entries) | set(correct_entries)
                        if wrong_entries.get(p) != correct_entries.get(p))
    if pair_delta != [path] or any(setup.mode(rev, path) != '100644' for rev in (h, M, x, wrong, correct)):
        raise a1c.RepRefused('N10/N11 landings must differ at the regular-file AGENTS.md alone')
    he, me = setup.entries(h), setup.entries(M)
    side = sorted(p for p in set(he) | set(me) if he.get(p) != me.get(p))
    corpus = sorted(set(ctx.corpus(h)) | set(ctx.corpus(M)) | set(ctx.corpus(x)))
    for name, data in (('ledger', ledger_bytes), ('edits', edits_bytes)):
        pin = inputs[name]
        copies = [entry(setup, rev, pin['copy_at']) for rev in (x, wrong, correct)]
        if any(copy_entry['mode'] != pin['mode'] or copy_entry['git_blob'] != pin['git_blob'] or
               setup.read(copy_entry['commit'], copy_entry['path']) != data for copy_entry in copies):
            raise a1c.RepRefused('N10/N11 representative %s copy has different mode or bytes' % name)
        pin['copies'] = copies

    x_blob = setup.blob_id(x, path)
    m_blob = setup.blob_id(M, path)
    scope_text = 'side changes H..M, the ledgered and corpus path sets, and the candidate blobs on drifted paths'
    composed = '86d79863821f3f8cdad86771008b2df89fd1961a'
    common = {'scope': 'fixed representative reconciliation control', 'tool': a.tool_rev, 'H_rep': h, 'E': E, 'M': M,
              'X_rep': x, 'X_rep_tree': setup.tree_id(x), 'X_rep_parents': setup.parents(x), 'inputs': inputs,
              'configuration': {**entry(setup, a.crev, a.cpath), 'blob_sha256': sha(config_bytes)},
              'delegation': {**entry(setup, a.crev, dref['path']), 'blob_sha256': sha(delegation_bytes)},
              'builder': {**entry(setup, a.tool_rev, source), 'blob_sha256': sha(source_bytes), 'imports': imports},
              'runner': {**entry(setup, a.tool_rev, runner_path), 'blob_sha256': sha(runner_bytes)},
              'markers': markers, 'protected_ranges': protected, 'classes': classes,
              'ledgered_paths': sorted(ledger['files']), 'corpus_paths': corpus, 'side_change_paths': side,
              'landing_pair_delta': pair_delta,
              'build_reads': build_reads.evidence(), 'setup_reads': setup.evidence()}
    for cid, landing, record in (('N10', wrong, wrong_record), ('N11', correct, good_record)):
        log = FixedReads(a.repo, x)
        ctx = pl.RunContext(log, config, {}, [], {}, None)
        e = reconcile_execution(ctx, h, M, x, ledger, classes, record, landing)
        read = log.read_at(fixed)
        outside = sorted(set(read) - set(ledger['files']) - set(corpus) - set(side))
        scope = {'read_at_X_rep': len(read), 'paths': read, 'outside_scope': outside}
        l_blob = log.blob_id(landing, path)
        comp_blob = next((c['composed_blob'] for c in e.compositions if c['path'] == path), None)
        outcomes = sorted({i['class'] for i in e.items if i.get('file') == path or path in str(i.get('subject'))})
        attested = {'L_blob': l_blob, 'composed_blob': comp_blob, 'composition_evaluated': comp_blob is not None,
                    'representative_candidate': a1c.REP_CANDIDATE}
        if not outside and path in read:
            attested['scanned_paths_within'] = scope_text
        exec_doc(e, 'execution main role and landing (a1_conformance.n10_n11)', attested=attested)
        FILES[cid] = {'configuration.json': config_bytes, 'delegation.json': delegation_bytes,
                      'fixed-inputs.json': dict(common, L=landing, L_tree=log.tree_id(landing),
                                                L_parents=log.parents(landing), read_scope=scope,
                                                execution_reads=log.evidence(),
                                                AGENTS=[entry(log, rev, path) for rev in (h, M, x, landing)]),
                      'reconciliation.json': record}
        actual = {'x_blob': x_blob, 'm_blob': m_blob, 'l_blob': l_blob, 'composed': comp_blob, 'classes': outcomes,
                  'X_rep': x, 'scope': scope}
        bound = (not outside and path in read and comp_blob == composed and
                 x_blob == '9f4fc3e830707c90ffc105842d26d5b51f01760b' and
                 m_blob == '6b1280fa92fa30e36555e9afd30cc0d6e992f5bb')
        if cid == 'N10':
            check(cid, 'the landing keeps X_rep\'s AGENTS.md and the record predicts it; FAIL the landing and record',
                  'the composed blob is 86d79863, the landing blob is 9f4fc3e8 and both failures name AGENTS.md',
                  actual, bound and l_blob == x_blob and
                  {'landing-conflict-unresolved', 'record-invalid'} <= set(outcomes))
        else:
            check(cid, 'the landing and record carry the reference composition of AGENTS.md; PASS for the path',
                  'the landing blob is 86d79863 and no item names AGENTS.md', dict(actual, items=outcomes),
                  bound and l_blob == composed and record['paths'][0]['l'] == composed and not outcomes)
    return correct


def n_controls(a, fixture=None):
    rcn = Recon(a)
    repo, path, rec = rcn.repo, rcn.path, rcn.rec
    comp = repo.read(M, path)
    e = rcn.run(rec)
    clean = getattr(e, 'captured', None)

    def restored():
        """The restored case (OBL-20): the same evaluation with the valid record on the unmutated M, X and
        classes, compared with the clean run."""
        rcn.run(rec)
        if REC is not None:
            REC.name_last('restored', baseline=clean)
    base = [i for i in e.items if i.get('file') == path]
    # N3 with the full candidate comparison
    ex = cli.candidate_with_and_without(rcn.ctx, H, T, rcn.led, None, M, None, T, rcn.classes, [rec])
    exec_doc(ex, 'op C candidate comparison with and without the record (cli.candidate_with_and_without)')
    bare = exmod.Execution(rcn.ctx, H, T, rcn.led, None, M, None, T, rcn.classes, ())
    bare.integrity()
    bare.candidate()
    exec_doc(bare, 'op C candidate checks on X without the record')
    if REC is not None:
        REC.pending[-2]['case'], REC.pending[-1]['case'] = 'with the record', 'without the record'
    PROCS['N3'] = {'name': 'with-without-record', 'lib': 'rel-equal',
                   'run_cases': ['with the record', 'without the record']}
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
        restored()
        f = rcn.failed(e_)
        drift = [i for i in e_.items if i['class'] == 'base-drift' and i.get('file') == path]
        check(cid, expected, "the record does not apply: base-drift for AGENTS.md, and the failed conditions include "
              + cond, {'failed': f, 'base_drift': bool(drift)}, cond in f and bool(drift))
        return e_

    def entry(r, **upd):
        r['paths'][0].update(upd)
        return r
    named('N4', 'the record with its ledger_binding altered by one byte: does not apply (base-drift), naming RC13',
          'RC13', lambda r: entry(r, ledger_binding=dict(r['paths'][0]['ledger_binding'], files_entry_sha256='0' + r[
              'paths'][0]['ledger_binding']['files_entry_sha256'][1:])))
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
    # the execution main role with the synthetic copy as its scientific base and M's tree on a first-parent child
    # of it, retained as the row's run
    M12 = repo.derive(M, {}, parents=[H12], subject="M's tree over the synthetic copy")
    try:
        e12 = rcn.run(rec, h=H12, m=M12)
        f12 = rcn.failed(e12)
        drift12 = any(i['class'] == 'base-drift' and i.get('file') == path for i in e12.items)
        stop12 = None
    except oc.Stop as exc:
        f12, drift12, stop12 = [], False, '%s: %s' % (exc.cls, exc)
        if REC is not None:
            REC.capture_doc('execution main role (a1_conformance.Recon.run)', {'items': [], 'stop': {
                'class': exc.cls, 'message': str(exc)}, 'exit_status': None})
    restored()
    ev12 = rc.evaluate(repo, rcn.ctx, H12, M, T, rcn.led, rec, rec['paths'][0], rcn.classes, {})
    check('N12', 'the record\'s RC3: D296\'s old bytes made to occur twice at H in a synthetic copy: does not apply, '
          'naming RC3', "the execution's failed conditions include RC3, with base-drift for the path; the direct "
          "evaluation agrees", {'failed': f12, 'base_drift': drift12, 'stop': stop12, 'evaluated': ev12['failed']},
          'RC3' in f12 and drift12 and 'RC3' in ev12['failed'])
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
    exec_doc(e16, 'execution main role, N16 (the other ledgered file)')
    if REC is not None:
        REC.name_last('', bindings={'other_ledgered_file': other})
    restored()
    check('N16-file', 'the other ledgered file is base-drift', "base-drift for that file",
          other, any(i['class'] == 'base-drift' and i.get('file') == other for i in e16.items))
    M17 = repo.derive(M, {'x/unclassified.txt': b'x\n'}, parents=[M], subject='unclassified path')
    named('N17', 'a changed path on M not covered by a pinned class: does not apply, naming RC11', 'RC11', m=M17)
    e18 = named('N18', 'the record\'s changes_decisions_on_X non-empty: does not apply, naming RC12; the record is '
                'record-invalid', 'RC12', lambda r: dict(r, changes_decisions_on_X=['a decision']))
    exec_doc(e18, 'execution main role, N18 (the record)')
    restored()
    check('N18-record', 'the record is record-invalid', "a record-invalid item", [i['class'] for i in e18.items],
          'record-invalid' in [i['class'] for i in e18.items])
    L11 = n10_n11(fixture or a)
    # the configuration route (owner: the record is frozen with the plan and referenced by the configuration)
    cfg = json.loads(repo.read(a.crev, a.cpath))
    classes_doc = {'schema': 'oi-side-change-classes/1', 'record_id': 'n3-classes', 'author': 'session.fixture-control-writer',
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
    workflow, configuration = rcn.classes
    pin = workflow['pins'][0]
    workflow_path = pin['path']
    bad = [dict(workflow, pins=[dict(pin, blob_sha256='0' * 64)]), configuration]
    e18c = rcn.run(rec, classes=bad)
    if REC is not None:
        REC.name_last('', bindings={'workflow_path': workflow_path})
    restored()
    workflow_review = any(i['class'] == 'side-change-unclassified' and i['decision'] == 'REVIEW_REQUIRED' and
                          i.get('file') == workflow_path for i in e18c.items)
    drift_fail = any(i['class'] == 'base-drift' and i['decision'] == 'FAIL' for i in e18c.items)
    check('R18', 'a workflow pin mismatch on M with ledgered drift: the workflow needs review and drift fails',
          'REVIEW_REQUIRED side-change-unclassified at the workflow and FAIL base-drift',
          {'workflow': workflow_path, 'workflow_review': workflow_review, 'drift_fail': drift_fail},
          workflow_review and drift_fail)
    extra_p, listed_p = 'tools/ledger_coverage/extra.py', 'tools/ledger_coverage/listed.py'
    # M is a child of H that carries the tool landing alone, so no ledgered drift enters the outcome
    M19 = repo.derive(H, {listed_p: b'y\n'}, parents=[H], subject='tool landing on M')
    M19u = repo.derive(M19, {extra_p: b'x = 1\n'}, parents=[M19], subject='an unlisted tool path on M')

    def tool(blob_sha256, git_blob):
        return {'id': 'tool-landing', 'prefixes': ['tools/ledger_coverage/'],
                'pins': [{'path': listed_p, 'git_blob': git_blob, 'blob_sha256': blob_sha256}]}
    good = tool(sha(b'y\n'), repo.blob_id(M19, listed_p))
    # separately: an unlisted path under the prefix (the listed path matching its pin), and the listed path whose
    # blob differs from its pin (no unlisted path)
    e19u = rcn.run(None, m=M19u, classes=rcn.classes + [good])
    if REC is not None:
        REC.name_last('unlisted path under the tool-landing prefix')
    e19b = rcn.run(None, m=M19, classes=rcn.classes + [tool('0' * 64, None)])
    if REC is not None:
        REC.name_last('listed path with a differing blob')
    # restored: the same run on M with the listed path matching its pin, against a clean run of it
    c19 = rcn.run(None, m=M19, classes=rcn.classes + [good])
    if REC is not None:
        REC.name_last('baseline')
    r19 = rcn.run(None, m=M19, classes=rcn.classes + [good])
    if REC is not None:
        REC.name_last('restored', baseline=getattr(c19, 'captured', None))

    def unclassified(e_):
        return sorted(i.get('file') for i in e_.items if i['class'] == 'side-change-unclassified')
    u19 = {'unlisted': unclassified(e19u), 'differing_blob': unclassified(e19b), 'restored': unclassified(r19)}
    check('R19', 'a path under the tool-landing prefix on M that the class does not list, and separately a listed path '
          'whose blob differs from its pin: REVIEW_REQUIRED side-change-unclassified each',
          "side-change-unclassified for the unlisted path, and separately for the listed path; none when the listed "
          "path matches its pin", u19,
          u19 == {'unlisted': [extra_p], 'differing_blob': [listed_p], 'restored': []})


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', required=True)
    ap.add_argument('--config', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--only', default=None)
    ap.add_argument('--staged-config', default=None,
                    help='the staged configuration file; --config REV:PATH names its path in the plan directory')
    ap.add_argument('--tool-revision', help='full checkout HEAD when the configuration is on a distinct revision')
    ap.add_argument('--fixed-config', help='full REV:PATH of the N10/N11 configuration when distinct from --config')
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)
    a = a1c.A1(args.repo, args.config, args.out, args.staged_config)
    if args.tool_revision is not None or args.fixed_config is not None:
        head = a1c.rev_parse(args.repo, 'HEAD')
        if args.tool_revision is not None and args.tool_revision != head:
            ap.error('--tool-revision must be the full checkout HEAD')
        a.tool_rev = a.base.resolve(head)
    fixture = None
    if args.fixed_config is not None:
        revision, sep, path = args.fixed_config.partition(':')
        if not sep or not path or len(revision) != 40 or any(ch not in '0123456789abcdef' for ch in revision):
            ap.error('--fixed-config must name a full commit id and a configuration path')
        fixture = a1c.A1(args.repo, args.fixed_config, args.out)
        fixture.base, fixture.repo, fixture.tool_rev = a.base, a.repo, a.tool_rev
    global REC
    REC = a.rec = control_records.Recorder('a1-conformance', args.out)
    groups = [('WB', wb_controls), ('S11', s11_controls), ('N', lambda runner: n_controls(runner, fixture))]
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
    # R6.GATE.5 and R6.GATE.7: one record per control with its retained evidence, read by the gate
    done = set()
    not_due = a1c.rules_not_due(a, args.repo)
    for r in doc['controls']:
        if r['id'] in done:
            continue
        done.add(r['id'])
        REC.pending = RUNS.get(r['id'], [])
        REC.record(r['id'], 'NOT RUN' if r['id'] in not_due else r['status'], r['actual'],
                   r['predicate'] or r['expected'], files=FILES.get(r['id']), procedure=PROCS.get(r['id']))
    REC.write()
    print(json.dumps(summary, sort_keys=True))
    for r in doc['controls']:
        if r['status'] != 'PASS':
            print(r['status'], r['id'], json.dumps(r['actual'], default=str)[:400])


if __name__ == '__main__':
    main()
