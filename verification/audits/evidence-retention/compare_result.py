#!/usr/bin/env python3
"""compare_result.py -- compares an archived expected result with a reproduction, and fails closed.

    python3 -I compare_result.py EXPECTED.json REPRODUCED.json --tree DIR
    python3 -I compare_result.py --self-test [EXPECTED.json]

EXPECTED.json is a results.json of the evidence-retention archive. REPRODUCED.json is the output of
extract_result.py on the output of `lake --rehash build` and `tools/release_gate.py` at the expected commit.
--tree is that commit's checked-out tree. Each governed module's `#print axioms` lines are read from its source
there, not from the expected result, so the count a reproduction must reach is derived independently of the
archive; without --tree the comparison fails.

Only deterministic results are compared: build success, the release gate's steps and verdict, each governed
module's `#print axioms` reports, and the failure markers. Timestamps, durations, cache behaviour, job counts
and the order of output are not compared. Every mismatch, missing item or extraction failure is a failure:
there is no partial credit and nothing is skipped.

Rules:
  C1  the reproduction has a build line and it reports success;
  C2  the reproduction has a release-gate block whose verdict is PASS, with exactly the expected steps, each
      with the expected status and summary;
  C3  for each governed module, against its source at the commit: a module recorded absent is absent from the
      source and reports nothing; otherwise the module is in the source, the expected result's #print axioms
      lines are the source's, and the reproduction reports exactly one report for each #print axioms line of
      the source and no other; a complete module reports exactly the expected declarations, and a partial or
      none module at least them, each with exactly the expected axioms; and every reproduced axiom of a
      governed module is one of propext, Classical.choice and Quot.sound;
  C4  every failure marker is absent from the reproduction when the expected result has none.
"""
import json
import os
import re
import sys

PERMITTED = {'propext', 'Classical.choice', 'Quot.sound'}
PRINT = re.compile(r'^#print axioms\b')


def print_lines(text):
    """The 1-based lines of a Lean source that hold a `#print axioms` command."""
    return {i + 1 for i, l in enumerate(text.split('\n')) if PRINT.match(l)}


def expand(spans):
    return {n for a, b in (spans or []) for n in range(a, b + 1)}


def compare(expected, rep, source):
    """source(mod) is the module's text at the commit, or None if the module is not there."""
    fails = []
    F = fails.append
    exp = expected.get('expected', {})
    if not rep.get('build') or not rep['build'].get('success'):
        F('C1 the reproduction has no successful build line')
    if not exp.get('build_success'):
        F('C1 the expected result does not record a successful build')
    g, eg = rep.get('gate'), exp.get('gate') or {}
    if not g or not g.get('verdict'):
        F('C2 the reproduction has no release-gate verdict')
    else:
        if not g['verdict'].get('pass'):
            F('C2 the reproduced release gate did not pass: %s' % g['verdict'].get('text'))
        if g['verdict'].get('text') != eg.get('verdict'):
            F('C2 the verdict line differs: reproduced %r, expected %r' % (g['verdict'].get('text'), eg.get('verdict')))
        got = {s['name']: s for s in g.get('steps', [])}
        want = {s['name']: s for s in eg.get('steps', [])}
        if not want:
            F('C2 the expected result records no gate steps')
        for name, s in want.items():
            if name not in got:
                F('C2 gate step %s is missing from the reproduction' % name)
            elif got[name]['status'] != s['status'] or got[name]['summary'] != s['summary']:
                F('C2 gate step %s differs: reproduced %s %r, expected %s %r' % (
                    name, got[name]['status'], got[name]['summary'], s['status'], s['summary']))
        for name in got:
            if name not in want:
                F('C2 gate step %s is not in the expected result' % name)
    mods = exp.get('modules') or {}
    if not isinstance(mods, dict):
        F('C3 the expected result has no module table')
        mods = {}
    for mod, em in mods.items():
        reps = rep.get('reports', {}).get(mod, [])
        got = {}
        for r in reps:
            if r.get('unclosed'):
                F('C3 %s: the reproduced report of %s has an unclosed axiom list' % (mod, r['name']))
            got[r['name']] = r['axioms']
        want = {r['name']: r['axioms'] for r in em.get('reports', [])}
        st = em.get('status')
        text = source(mod)
        if st not in ('complete', 'partial', 'none', 'absent'):
            F('C3 %s: unknown status %r' % (mod, st))
            continue
        if st == 'absent':
            if text is not None:
                F('C3 %s is recorded as absent at the commit but is in its source' % mod)
            if reps:
                F('C3 %s is recorded as absent but the reproduction reports it' % mod)
            continue
        if text is None:
            F('C3 %s is not in the source at the commit' % mod)
            continue
        src = print_lines(text)
        if expand(em.get('print_lines')) != src:
            F('C3 %s: the expected result\'s #print axioms lines differ from the source at the commit (%d there)' % (mod, len(src)))
        lines = sorted(r['line'] for r in reps)
        if sorted(src) != lines:
            F('C3 %s: the reproduction reports %d line(s), the source at the commit has %d #print axioms command(s)%s' % (
                mod, len(lines), len(src), '' if len(lines) == len(set(lines)) else ', with a line reported twice'))
        for name, ax in want.items():
            if name not in got:
                F('C3 %s: expected report of %s is missing from the reproduction' % (mod, name))
            elif got[name] != ax:
                F('C3 %s: %s depends on %s, expected %s' % (mod, name, got[name], ax))
        if st == 'complete':
            for name in got:
                if name not in want:
                    F('C3 %s: the reproduction reports %s, which the complete expected result does not' % (mod, name))
        for name, ax in got.items():
            if ax is not None and not set(ax) <= PERMITTED:
                F('C3 %s: %s depends on an axiom outside the permitted three: %s' % (mod, name, sorted(set(ax) - PERMITTED)))
    em = exp.get('markers') or {}
    rm = rep.get('markers') or {}
    for k in ('sorryAx', 'Lean.ofReduceBool', "declaration uses 'sorry'", 'error:'):
        if k not in em:
            F('C4 the expected result records no %s marker count' % k)
        elif em[k] == 0 and rm.get(k, None) != 0:
            F('C4 the reproduction has %r %s marker(s); the expected result has none' % (rm.get(k), k))
    return fails


def synth(expected):
    """A reproduction equal to the expected result: the positive control of the self-test."""
    exp = expected['expected']
    rep = {'build': {'success': True, 'jobs': 0, 'line': 1},
           'gate': {'steps': [dict(s, served_line=0) for s in exp['gate']['steps']],
                    'verdict': {'text': exp['gate']['verdict'], 'pass': True, 'served_line': 0}},
           'reports': {}, 'markers': dict(exp['markers'])}
    for mod, em in exp['modules'].items():
        if em['status'] == 'absent':
            continue
        reps = [{'line': r['line'], 'name': r['name'], 'axioms': r['axioms'], 'served_line': 0} for r in em['reports']]
        if em['status'] in ('partial', 'none'):
            # the full output at the commit reports every #print axioms command
            have = {r['line'] for r in reps}
            for a, b in em['print_lines']:
                for n in range(a, b + 1):
                    if n not in have:
                        reps.append({'line': n, 'name': 'synth.%s.%d' % (mod, n), 'axioms': sorted(PERMITTED), 'served_line': 0})
        rep['reports'][mod] = reps
    return rep


def synth_source(expected):
    """Module sources whose #print axioms lines are the expected result's: the self-test's stand-in for git."""
    srcs = {}
    for mod, em in expected['expected']['modules'].items():
        if em['status'] == 'absent':
            continue
        lines = expand(em['print_lines'])
        n = max(lines) if lines else 1
        srcs[mod] = '\n'.join('#print axioms X%d' % i if i in lines else '-- line %d' % i for i in range(1, n + 1)) + '\n'
    return srcs


def self_test(expected):
    import copy
    ok = True
    exp = expected['expected']
    srcs = synth_source(expected)
    partial = next((m for m, em in exp['modules'].items() if em['status'] in ('partial', 'none')), None)
    partial_r = next((m for m, em in exp['modules'].items() if em['status'] == 'partial' and em['reports']), None)
    complete = next((m for m, em in exp['modules'].items() if em['status'] == 'complete' and em['reports']), None)
    absent = next((m for m, em in exp['modules'].items() if em['status'] == 'absent'), None)

    def case(name, mut_e=None, mut_r=None, rule=None, src=None, msg=None):
        nonlocal ok
        e = copy.deepcopy(expected)
        if mut_e:
            mut_e(e)
        r = synth(expected)
        if mut_r:
            mut_r(r)
        s = dict(srcs)
        if src:
            src(s)
        fails = compare(e, r, s.get)
        # with msg, the case passes only if that site's own message fired, so the case isolates the site
        good = (not fails) if rule is None else any(f.startswith(rule + ' ') and (msg is None or msg in f) for f in fails)
        ok &= good
        print('%s self: %s%s' % ('PASS' if good else 'FAIL', name, '' if rule is None else ' (%s)' % rule))
        if not good:
            print('      got: %s' % fails[:3])

    case('a reproduction equal to the expected result passes')
    case('a reproduction without a build line', mut_r=lambda r: r.__setitem__('build', None), rule='C1')
    case('a reproduction whose build failed', mut_r=lambda r: r['build'].__setitem__('success', False), rule='C1')
    case('a reproduction without a gate block', mut_r=lambda r: r.__setitem__('gate', None), rule='C2')
    case('a reproduced gate that did not pass', mut_r=lambda r: r['gate']['verdict'].update(pass_=None) or r['gate']['verdict'].__setitem__('pass', False), rule='C2')
    case('a gate step missing from the reproduction', mut_r=lambda r: r['gate']['steps'].pop(0), rule='C2')
    case('a gate step whose status differs', mut_r=lambda r: r['gate']['steps'][0].__setitem__('status', 'FAIL'), rule='C2')
    case('a gate step whose summary differs (a changed count)', mut_r=lambda r: r['gate']['steps'][-1].__setitem__('summary', 'x'), rule='C2')
    case('an extra gate step in the reproduction', mut_r=lambda r: r['gate']['steps'].append({'name': 'extra', 'status': 'PASS', 'summary': ''}), rule='C2')
    case('an expected result with no gate steps', mut_e=lambda e: e['expected']['gate'].__setitem__('steps', []), rule='C2')
    case('an expected result recording no successful build', mut_e=lambda e: e['expected'].__setitem__('build_success', False),
         rule='C1', msg='does not record a successful build')
    case('a passing verdict whose line differs from the expected one',
         mut_r=lambda r: r['gate']['verdict'].__setitem__('text', r['gate']['verdict']['text'] + ' (altered)'),
         rule='C2', msg='the verdict line differs')
    case('no gate steps in the expected result or the reproduction', mut_e=lambda e: e['expected']['gate'].__setitem__('steps', []),
         mut_r=lambda r: r['gate'].__setitem__('steps', []), rule='C2', msg='records no gate steps')
    case('a module table that is not a table', mut_e=lambda e: e['expected'].__setitem__('modules', ['not a table']),
         rule='C3', msg='has no module table')
    if complete:
        case('a report missing from a complete module', mut_r=lambda r: r['reports'][complete].pop(0), rule='C3')
        case('a report with a changed axiom set', mut_r=lambda r: r['reports'][complete][0].__setitem__('axioms', ['propext']), rule='C3')
        case('a report with an axiom outside the permitted three',
             mut_r=lambda r: r['reports'][complete][0].__setitem__('axioms', ['propext', 'sorryAx']), rule='C3')
        case('an extra report in a complete module',
             mut_r=lambda r: r['reports'][complete].append({'line': 1, 'name': 'extra', 'axioms': ['propext'], 'served_line': 0}), rule='C3')
        case('an unclosed axiom list in the reproduction', mut_r=lambda r: r['reports'][complete][0].__setitem__('unclosed', True), rule='C3')
        case('a complete module missing from the source', src=lambda s: s.pop(complete), rule='C3')
        case('a source with one more #print axioms than the reproduction reports',
             src=lambda s: s.__setitem__(complete, s[complete] + '#print axioms Extra\n'), rule='C3')
        case('expected #print axioms lines that differ from the source',
             mut_e=lambda e: e['expected']['modules'][complete].__setitem__('print_lines', [[1, 1]]), rule='C3')
        case('a reproduced report at a line with no #print axioms in the source',
             mut_r=lambda r: r['reports'][complete][0].__setitem__('line', 10 ** 6), rule='C3')
        case('an expected report whose axioms were altered', mut_e=lambda e: e['expected']['modules'][complete]['reports'][0].__setitem__('axioms', ['propext']), rule='C3')
        case('an expected report that was removed', mut_e=lambda e: e['expected']['modules'][complete]['reports'].pop(0), rule='C3')
        case('a recorded declaration renamed at its own line in a complete module',
             mut_r=lambda r: r['reports'][complete][0].__setitem__('name', 'renamed.declaration'), rule='C3',
             msg='is missing from the reproduction')
    if partial:
        case('an expected report missing from a partial module', mut_r=lambda r: r['reports'][partial].pop(0), rule='C3')
        case('a partial module with fewer reports than its source\'s #print axioms commands',
             mut_r=lambda r: r['reports'][partial].pop(), rule='C3')
        case('a partial module whose archived count was inflated, the source unchanged',
             mut_e=lambda e: e['expected']['modules'][partial].__setitem__('prints', 10 ** 4), mut_r=None, rule=None)
        case('a new report in a partial module with an unpermitted axiom',
             mut_r=lambda r: r['reports'][partial][-1].__setitem__('axioms', ['Classical.choice', 'Lean.ofReduceBool']), rule='C3')
        case('a partial module\'s line reported twice',
             mut_r=lambda r: r['reports'][partial].append(dict(r['reports'][partial][0], name='dup')), rule='C3')
    if partial_r:
        # the line count, the axioms and the module's status are unchanged, so only the per-declaration rule can see it
        case('a recorded declaration renamed at its own line in a partial module',
             mut_r=lambda r: r['reports'][partial_r][0].__setitem__('name', 'renamed.declaration'), rule='C3',
             msg='is missing from the reproduction')
    if absent:
        case('an absent module that is in the source', src=lambda s: s.__setitem__(absent, '#print axioms Y\n'), rule='C3')
        case('an absent module that the reproduction reports',
             mut_r=lambda r: r['reports'].__setitem__(absent, [{'line': 1, 'name': 'x', 'axioms': ['propext'], 'served_line': 0}]), rule='C3')
    case('a module of unknown status', mut_e=lambda e: next(iter(e['expected']['modules'].values())).__setitem__('status', 'maybe'), rule='C3')
    case('a sorryAx marker in the reproduction', mut_r=lambda r: r['markers'].__setitem__('sorryAx', 1), rule='C4')
    case('an error marker in the reproduction', mut_r=lambda r: r['markers'].__setitem__('error:', 2), rule='C4')
    case('an expected result without marker counts', mut_e=lambda e: e['expected'].__setitem__('markers', {}), rule='C4')
    case('an empty reproduction (extraction failure)', mut_r=lambda r: r.clear(), rule='C1')
    print('self-test: %s' % ('OK' if ok else 'FAILED'))
    return 0 if ok else 1


def tree_source(tree):
    def get(mod):
        p = os.path.join(tree, 'verification', 'lean-mathlib', mod)
        return open(p, encoding='utf-8').read() if os.path.isfile(p) else None
    return get


if __name__ == '__main__':
    args = sys.argv[1:]
    if args and args[0] == '--self-test':
        if len(args) > 1:
            paths = args[1:]
        else:
            # BG-3's E, and for each module status the first expected result that has it, so every case runs
            ci = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ci')
            paths = [os.path.join(ci, '38855576525', 'results.json')]
            for want in ('complete', 'partial', 'none', 'absent'):
                for d in sorted(os.listdir(ci)):
                    p = os.path.join(ci, d, 'results.json')
                    if any(m['status'] == want for m in json.load(open(p, encoding='utf-8'))['expected']['modules'].values()):
                        if p not in paths:
                            paths.append(p)
                        break
        rc = 0
        for p in paths:
            print('== %s' % os.path.relpath(p, os.path.dirname(os.path.abspath(__file__))))
            rc |= self_test(json.load(open(p, encoding='utf-8')))
        print('comparator self-test: %s (%d expected result(s))' % ('OK' if rc == 0 else 'FAILED', len(paths)))
        sys.exit(rc)
    if len(args) < 2:
        print(__doc__)
        sys.exit(2)
    expected = json.load(open(args[0], encoding='utf-8'))
    rep = json.load(open(args[1], encoding='utf-8'))
    if '--tree' not in args:
        print('FAIL  --tree is required: the #print axioms lines are read from the commit\'s source')
        sys.exit(1)
    fails = compare(expected, rep, tree_source(args[args.index('--tree') + 1]))
    for f in fails:
        print('FAIL  %s' % f)
    print('REPRODUCTION  %s (%d failure(s)) for run %s at %s' % ('HOLDS' if not fails else 'FAILS', len(fails),
                                                                 expected.get('run', {}).get('id'), expected.get('run', {}).get('head_sha', '')[:12]))
    sys.exit(1 if fails else 0)
