#!/usr/bin/env python3
"""compare_result.py -- compares an archived expected result with a reproduction, and fails closed.

    python3 -I compare_result.py EXPECTED.json REPRODUCED.json [--tree DIR]
    python3 -I compare_result.py --self-test [EXPECTED.json]

EXPECTED.json is a results.json of the evidence-retention archive. REPRODUCED.json is the output of
extract_result.py on the output of `lake --rehash build` and `tools/release_gate.py` at the expected commit.
--tree is that commit's checked-out tree, used to confirm that a module recorded as absent is absent.

Only deterministic results are compared: build success, the release gate's steps and verdict, each governed
module's `#print axioms` reports, and the failure markers. Timestamps, durations, cache behaviour, job counts
and the order of output are not compared. Every mismatch, missing item or extraction failure is a failure:
there is no partial credit and nothing is skipped.

Rules:
  C1  the reproduction has a build line and it reports success;
  C2  the reproduction has a release-gate block whose verdict is PASS, with exactly the expected steps, each
      with the expected status and summary;
  C3  for each governed module: an absent module is absent from the tree and reports nothing; a complete
      module reports exactly the expected declarations with exactly the expected axioms; a partial or none
      module reports every expected declaration with its expected axioms and as many reports as the module
      has `#print axioms` commands; and every reproduced axiom of a governed module is one of propext,
      Classical.choice and Quot.sound;
  C4  every failure marker is absent from the reproduction when the expected result has none.
"""
import json
import os
import sys

PERMITTED = {'propext', 'Classical.choice', 'Quot.sound'}


def compare(expected, rep, module_exists=None):
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
        if st == 'absent':
            if module_exists is not None and module_exists(mod):
                F('C3 %s is recorded as absent at the commit but exists in the tree' % mod)
            if reps:
                F('C3 %s is recorded as absent but the reproduction reports it' % mod)
            continue
        if module_exists is not None and not module_exists(mod):
            F('C3 %s is not in the tree at the commit' % mod)
        for name, ax in want.items():
            if name not in got:
                F('C3 %s: expected report of %s is missing from the reproduction' % (mod, name))
            elif got[name] != ax:
                F('C3 %s: %s depends on %s, expected %s' % (mod, name, got[name], ax))
        if st == 'complete':
            for name in got:
                if name not in want:
                    F('C3 %s: the reproduction reports %s, which the complete expected result does not' % (mod, name))
        elif st in ('partial', 'none'):
            prints = em.get('prints')
            if prints is None:
                F('C3 %s: a %s module records no #print axioms count' % (mod, st))
            elif len(got) != prints:
                F('C3 %s: the reproduction has %d reports, the module has %d #print axioms commands' % (mod, len(got), prints))
        else:
            F('C3 %s: unknown status %r' % (mod, st))
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


def self_test(expected):
    import copy
    ok = True
    exp = expected['expected']
    tree = {m for m, em in exp['modules'].items() if em['status'] != 'absent'}
    exists = lambda m: m in tree
    partial = next((m for m, em in exp['modules'].items() if em['status'] in ('partial', 'none')), None)
    complete = next((m for m, em in exp['modules'].items() if em['status'] == 'complete' and em['reports']), None)
    absent = next((m for m, em in exp['modules'].items() if em['status'] == 'absent'), None)

    def case(name, mut_e=None, mut_r=None, rule=None, exists_fn=exists):
        nonlocal ok
        e = copy.deepcopy(expected)
        if mut_e:
            mut_e(e)
        r = synth(expected)
        if mut_r:
            mut_r(r)
        fails = compare(e, r, exists_fn)
        good = (not fails) if rule is None else any(f.startswith(rule + ' ') for f in fails)
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
    if complete:
        case('a report missing from a complete module', mut_r=lambda r: r['reports'][complete].pop(0), rule='C3')
        case('a report with a changed axiom set', mut_r=lambda r: r['reports'][complete][0].__setitem__('axioms', ['propext']), rule='C3')
        case('a report with an axiom outside the permitted three',
             mut_r=lambda r: r['reports'][complete][0].__setitem__('axioms', ['propext', 'sorryAx']), rule='C3')
        case('an extra report in a complete module',
             mut_r=lambda r: r['reports'][complete].append({'line': 1, 'name': 'extra', 'axioms': ['propext'], 'served_line': 0}), rule='C3')
        case('an unclosed axiom list in the reproduction', mut_r=lambda r: r['reports'][complete][0].__setitem__('unclosed', True), rule='C3')
        case('a complete module missing from the tree', exists_fn=lambda m: m != complete, rule='C3')
        case('an expected report whose axioms were altered', mut_e=lambda e: e['expected']['modules'][complete]['reports'][0].__setitem__('axioms', ['propext']), rule='C3')
        case('an expected report that was removed', mut_e=lambda e: e['expected']['modules'][complete]['reports'].pop(0), rule='C3')
    if partial:
        case('an expected report missing from a partial module', mut_r=lambda r: r['reports'][partial].pop(0), rule='C3')
        case('a partial module with fewer reports than #print axioms commands', mut_r=lambda r: r['reports'][partial].pop(), rule='C3')
        case('a new report in a partial module with an unpermitted axiom',
             mut_r=lambda r: r['reports'][partial][-1].__setitem__('axioms', ['Classical.choice', 'Lean.ofReduceBool']), rule='C3')
        case('a partial module without a #print axioms count', mut_e=lambda e: e['expected']['modules'][partial].__setitem__('prints', None), rule='C3')
    if absent:
        case('an absent module that exists in the tree', exists_fn=lambda m: True, rule='C3')
        case('an absent module that the reproduction reports',
             mut_r=lambda r: r['reports'].__setitem__(absent, [{'line': 1, 'name': 'x', 'axioms': ['propext'], 'served_line': 0}]), rule='C3')
    case('a module of unknown status', mut_e=lambda e: next(iter(e['expected']['modules'].values())).__setitem__('status', 'maybe'), rule='C3')
    case('a sorryAx marker in the reproduction', mut_r=lambda r: r['markers'].__setitem__('sorryAx', 1), rule='C4')
    case('an error marker in the reproduction', mut_r=lambda r: r['markers'].__setitem__('error:', 2), rule='C4')
    case('an expected result without marker counts', mut_e=lambda e: e['expected'].__setitem__('markers', {}), rule='C4')
    case('an empty reproduction (extraction failure)', mut_r=lambda r: r.clear(), rule='C1')
    print('self-test: %s' % ('OK' if ok else 'FAILED'))
    return 0 if ok else 1


def tree_module_exists(tree):
    return lambda mod: os.path.isfile(os.path.join(tree, 'verification', 'lean-mathlib', mod))


if __name__ == '__main__':
    args = sys.argv[1:]
    if args and args[0] == '--self-test':
        p = args[1] if len(args) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ci', '38855576525', 'results.json')
        sys.exit(self_test(json.load(open(p, encoding='utf-8'))))
    if len(args) < 2:
        print(__doc__)
        sys.exit(2)
    expected = json.load(open(args[0], encoding='utf-8'))
    rep = json.load(open(args[1], encoding='utf-8'))
    exists = tree_module_exists(args[args.index('--tree') + 1]) if '--tree' in args else None
    fails = compare(expected, rep, exists)
    for f in fails:
        print('FAIL  %s' % f)
    print('REPRODUCTION  %s (%d failure(s)) for run %s at %s' % ('HOLDS' if not fails else 'FAILS', len(fails),
                                                                 expected.get('run', {}).get('id'), expected.get('run', {}).get('head_sha', '')[:12]))
    sys.exit(1 if fails else 0)
