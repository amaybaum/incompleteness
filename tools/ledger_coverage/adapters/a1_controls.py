"""A1 control runner: the real-tree controls (sec. 10.3), the A1 adversarial controls (sec. 10.2), the sec. 11
countercontrols, the four-tree controls on real objects (sec. 13) and Z9g, compared with the preregistered
expectations of the A1 controls file.

The A1 configuration and its records are unreviewed drafts, so every run here uses the control harness: the
configuration is admitted without its review chain and each result says so. Under the review chain the same
configuration is refused (ERROR CONFIG_UNREVIEWED); control CHAIN-REFUSAL shows it. Mutant trees, ledgers and
evidence exist only in memory or under the output directory.

The configuration does not land with the tool (design sec. 16.2): it belongs in the retirement plan's record
directory, frozen with the plan at F. A staged draft is given with --staged-config FILE and --config REV:PATH,
where PATH is its path in the plan's record directory; the runner builds an in-memory stand-in for F, REV's tree
plus the staged file at PATH, and reads the configuration from it. The predicted main carries only the tool's
landing.

`--main REV` names the `main` commit the sec. 13.4 sequencing safeguard (RT-L2) and the drift classes are measured
against; it is required, and the runner exits with status 2 when it is absent or unresolvable.

Usage: python3 -I -B tools/ledger_coverage/adapters/a1_controls.py --repo DIR --config REV:PATH
       --staged-config FILE --main REV --out DIR [--only ID,ID] [--skip-sweeps]
"""
import argparse
import collections
import hashlib
import io
import json
import os
import sys
import tempfile
import time

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

from ledger_coverage.engine import cli, gitobj, execution as exmod, pipeline as pl, purity, util  # noqa: E402
from ledger_coverage.engine import profiles as prf, rules as rulemod, records as rec  # noqa: E402
from ledger_coverage.adapters import control_records  # noqa: E402

E = 'e837e3dbaa605efc867a213f3345cee14c36d8f5'
H = '53c6601a10419b6b333cc992474272501ab542af'
T = '14ac71b4b0a0c0aa2d7068d6799a73f474097060'
P = '4c79be642ca631573f06b444903be75ec4f5e2b6'
WM = '413b0bb88f39cad901befcf4684355c7ee39480b'
PL = 'verification/audits/foundations/a1exit-deletion-20261121/'
LEDGER = P + ':' + PL + 'ledger.json'
EDITS = P + ':' + PL + 'edits.json'
FULL = 'book/The-Incompleteness-of-Observation-FULL.md'
WF = '.github/workflows/a1exit-trial-verify.yml'
# the workflow that tool.workflow pins, the one path of the tool landing outside tools/ and its audit directory
WORKFLOW_PATH = '.github/workflows/ledger-coverage.yml'


def sha(b):
    return hashlib.sha256(b).hexdigest()


def rev_parse(repo_path, rev):
    """The full id of a revision of the runner's own checkout (the runner names its inputs by ref; the tool reads
    only full ids)."""
    import subprocess
    r = subprocess.run(['git', '-C', repo_path, 'rev-parse', '--verify', '--quiet', rev + '^{commit}'],
                       capture_output=True, text=True)
    if r.returncode:
        raise ValueError('%s does not resolve to a commit' % rev)
    return r.stdout.strip()


def simulated_freeze(repo, rev, path, staged_bytes):
    """An in-memory stand-in for F: rev's tree with the staged configuration at its plan-directory path."""
    return repo.derive(rev, {path: staged_bytes}, parents=[rev],
                       subject='stand-in for F: the staged configuration in the plan record directory')


class A1:
    def __init__(self, repo_path, config_ref, out_root, staged=None, main=None):
        self.base = gitobj.GitRepo(repo_path)
        self.main = main  # the main commit the safeguard is measured against (--main)
        self.repo = gitobj.Overlay(self.base)
        self.repo_path = repo_path
        rev, self.cpath = config_ref.split(':', 1)
        self.crev = rev if rev in self.repo.mem else self.base.resolve(rev_parse(repo_path, rev))
        self.tool_rev = self.crev
        if staged is not None:
            with open(staged, 'rb') as f:
                self.crev = simulated_freeze(self.repo, self.crev, self.cpath, f.read())
        data = self.repo.read(self.crev, self.cpath)
        self.csha = sha(data) if data is not None else None
        # the tool's record directory: where the configuration's controls file lies
        cfg = json.loads(data) if data is not None else {}
        self.ad = (cfg.get('controls') or {}).get('path', self.cpath).rsplit('/', 1)[0] + '/'
        self.out_root = out_root
        self.n = 0
        from ledger_coverage.adapters import a1exit_exact_edit as le
        self.led = le.load(self.base.read(P, PL + 'ledger.json'), {'edits': self.base.read(P, PL + 'edits.json')})
        self.results = {}
        self.rec = control_records.Recorder('a1-controls', out_root)
        self.runs_of = {}

    def out(self):
        self.n += 1
        return os.path.join(self.out_root, 'run%03d' % self.n)

    def run(self, args, harness=True, control=None, case=None, mutation=None, bindings=None, baseline=None):
        out = self.out()
        argv = args[:1] + ['--config', '%s:%s' % (self.crev, self.cpath), '--out', out,
                           '--repo', self.repo_path] + args[1:]
        t = time.time()
        err = io.StringIO()
        code, res = cli.run(argv, repo=self.repo, harness=harness, stderr=err, control=control)
        # R6.GATE.7: every tool run is retained as evidence of the control recorded next
        self.rec.capture(argv, code, out, case=case, mutation=mutation, bindings=bindings,
                         stderr=err.getvalue() if code == 64 else None, baseline=baseline)
        return code, res or {}, round(time.time() - t, 1)

    def record(self, cid, passed, expected, actual, **extra):
        """B6: {id, expected, predicate, actual, status}; status PASS or FAIL (NOT RUN and SKIP are set
        explicitly by the controls that cannot run)."""
        d = {'id': cid, 'passed': bool(passed), 'expected': expected, 'actual': actual,
             'status': 'PASS' if passed else 'FAIL',
             'predicate': extra.pop('predicate', 'the boolean computed for this id in a1_controls.py')}
        d.update(extra)
        self.results[cid] = d
        self.runs_of[cid] = self.rec.take()

    # helpers
    def lines(self, c, f):
        return util.lines_of(self.repo.read(c, f).decode())

    def add_eof(self, f, text, at=T):
        """X' = at plus `text` appended to f as its own paragraph, with a zero-length splice at the end of f at H
        (added text)."""
        text = '\n' + text
        h = self.base.read(H, f)
        led = dict(self.led)
        led['splices'] = list(self.led['splices']) + [{
            'id': 'CTRL', 'file': f, 'start': len(h), 'end': len(h), 'old_sha256': sha(b''), 'new': text,
            'new_bytes': text.encode(), 'new_sha256': sha(text.encode()), 'kind': 'ptr'}]
        x = self.repo.derive(at, {f: self.repo.read(at, f) + text.encode()}, parents=[H], subject='control X')
        return x, led


def classes(res):
    return sorted({i['class'] for i in res.get('items', [])})


def items_on(res, f, ln):
    return [i for i in res.get('items', []) if i.get('file') == f and i.get('line') == ln]


def dl(res):
    ln, sl = set(), set()
    per, alt = collections.Counter(), collections.Counter()
    for i in res.get('items', []):
        if i['class'] != 'deny-match':
            continue
        if i.get('level') == 'line':
            ln.add((i['file'], i['line']))
            per[i['rule_id']] += 1
            for a in i.get('alternatives', []):
                alt['%s%s' % (i['rule_id'], a if i['rule_id'] == 'DR-1' else '')] += 1
        elif i.get('level') == 'sentence':
            for x in range(i['line'], i['last_line'] + 1):
                sl.add((i['file'], x))
    return ln, sl, per, alt


# ---- real-tree controls ------------------------------------------------------------------------------------

def rt_record(a):
    code, res, t = a.run(['record', '--pin', E, '--record', H])
    rc = res.get('record_checks') or {}
    a.record('RT-A', code == 0 and rc.get('anchors') == 697 and not rc.get('ck_errors'), 'PASS; 0 errors; 697 anchors',
             {'exit': code, 'outcome': res.get('outcome'), 'equalities': rc.get('equalities'),
              'ck_errors': rc.get('ck_errors'), 'extended_unmapped': rc.get('extended_unmapped'),
              'frozen_self_test': rc.get('frozen_self_test'), 'anchors': rc.get('anchors'), 'seconds': t})
    code, res, t = a.run(['record', '--pin', H, '--record', H])
    a.record('X1', code == 65 and res.get('stop', {}).get('class') == 'PIN_MISMATCH', 'ERROR PIN_MISMATCH, exit 65',
             {'exit': code, 'stop': res.get('stop', {}).get('class')})
    # M7-M9: altered frozen record files are refused at integrity (the record tree is pinned)
    R = 'verification/audits/foundations/a1exit-ledger-20261120/'
    sm = json.loads(a.base.read(H, R + 'sitemap.json'))
    sm['sites'][0]['row'] = 'X-99'
    r7 = a.repo.derive(H, {R + 'sitemap.json': (json.dumps(sm, indent=1, ensure_ascii=False) + '\n').encode()})
    code7, res7, _ = a.run(['record', '--pin', E, '--record', r7])
    led_md = a.base.read(H, R + 'LEDGER.md').replace(b'| X-00 |', b'| X-0O |', 1)
    r8 = a.repo.derive(H, {R + 'LEDGER.md': led_md})
    code8, res8, _ = a.run(['record', '--pin', E, '--record', r8])
    # the replay itself, on the altered materializations, reports the equalities false
    from ledger_coverage.adapters import python_frozen_replay as rp

    class Rd:
        def __init__(self, c):
            self.c = c

        def __call__(self, commit, path):
            return a.repo.read(commit, path)

        def listing(self, commit, dirs):
            return [(d, [(p, a.repo.read_blob(b)) for p, b in sorted(a.repo.paths(commit).items())
                         if p.startswith(d + '/')]) for d in dirs]
    corpus = [p for p in a.base.paths(E) if p.endswith('.md') and p.count('/') == 1 and
              p.split('/')[0] in ('papers', 'book')]
    rr7 = rp.replay(Rd(r7), E, r7, R + 'ledger_check.py', corpus, tempfile.mkdtemp(dir=a.out_root))
    rr8 = rp.replay(Rd(r8), E, r8, R + 'ledger_check.py', corpus, tempfile.mkdtemp(dir=a.out_root))
    eq7 = {e['name']: e['equal'] for e in rr7['equalities']}
    eq8 = {e['name']: e['equal'] for e in rr8['equalities']}
    a.record('M7', code7 == 65 and eq7.get('rebuild_equal') is False,
             'FAILS rebuild_equal false (v1); under v5.1 the pinned record tree refuses the altered record first',
             {'cli': (code7, res7.get('stop', {}).get('class')), 'replay_equalities': eq7})
    a.record('M8', code8 == 65 and eq8.get('render_equal') is False, 'FAILS render_equal false (v1); refused at integrity',
             {'cli': (code8, res8.get('stop', {}).get('class')), 'replay_equalities': eq8})
    a.record('M9', code7 == 65 and res7.get('stop', {}).get('class') == 'RECORD_TREE_MISMATCH', 'ERROR record tree',
             {'cli': (code7, res7.get('stop', {}).get('class'))})
    rows = json.loads(a.base.read(H, R + 'rows.json'))
    j = next(r for r in rows['rows'] if r['disposition'] == 'J')
    j['s1'] = 'Yes'
    rj = a.repo.derive(H, {R + 'rows.json': (json.dumps(rows, indent=1, ensure_ascii=False) + '\n').encode()})
    rrj = rp.replay(Rd(rj), E, rj, R + 'ledger_check.py', corpus, tempfile.mkdtemp(dir=a.out_root))
    a.record('S11-2c', rrj['ck_errors'] and any(e.startswith('CK5') for e in rrj['ck_errors']),
             'J row with S1 Yes gives FAIL (op A record_checks)', {'ck_errors': (rrj['ck_errors'] or [])[:3]})


def rt_coverage(a):
    code, res, t = a.run(['coverage', '--commit', E])
    a.record('RT-E', code == 0 and res.get('site_counts') == {'unchanged': 697}, 'PASS; 697 unchanged',
             {'exit': code, 'site_counts': res.get('site_counts'), 'hit_counts': res.get('hit_counts'), 'seconds': t})
    code, res, t = a.run(['coverage', '--commit', H])
    fc = res.get('finding_counts', {})
    nonhp = [i for i in res.get('items', []) if i['decision'] == 'FAIL' and i['obligation'] != 'HP']
    ind = [i for i in res.get('items', []) if i['class'] == 'context-structure-changed' and i['obligation'] != 'HP']
    want_struct = sorted(['book/The-Incompleteness-of-Observation-FULL.md:706', 'book/The-Incompleteness-of-'
                          'Observation-FULL.md:708', 'book/ch02-substratum.md:76', 'book/ch02-substratum.md:78',
                          'papers/Substratum.md:94', 'papers/Substratum.md:253', 'papers/Main.md:741'])
    got_struct = sorted(i['subject'].split('@')[0] for i in res.get('items', [])
                        if i['class'] == 'context-structure-changed' and i['obligation'] == 'HP')
    a.record('RT-H0', code == 20 and not nonhp and not ind and fc.get('HP/FAIL/hp-unadjudicated') == 113 and
             fc.get('HP/FAIL/context-meaning-unverified') == 7 and got_struct == want_struct,
             'FAIL; every FAIL and indicator item HP; 113 hp-unadjudicated; 7 HP context-meaning-unverified; 7 HP '
             'context-structure-changed (FULL:706, FULL:708, ch02:76, ch02:78, Substratum.md:94, :253, Main.md:741)',
             {'exit': code, 'finding_counts': fc, 'structure_sites': sorted(i['subject'] for i in res['items']
                                                                            if i['class'] == 'context-structure-changed')},
             predicate='exit 20; no non-HP FAIL or indicator item; counts 113 and 7; the 7 structure sites as listed',
             reference_difference='7 HP context-structure-changed, not 3: the 4 further sites (FULL:706, ch02:76, '
                                  'Substratum.md:94, :253) are unique at E and H and rewritten in H..T1\'; the '
                                  'reference population required uniqueness at T1\' as well (sec. 14).')
    seg = ['--segment', '%s..%s' % (E, H), '--segment', '%s..%s=%s' % (H, T, LEDGER)]
    code, res, t = a.run(['coverage', '--commit', T] + seg)
    fc = res.get('finding_counts', {})
    sites = res.get('sites', [])
    moved = sum(1 for s in sites for x in s['statuses'] if x['segment'].startswith(H[:8]) and x['status'] == 'moved')
    shared = sum(1 for s in sites if s['region_shared_with'])
    splices = sorted({x for s in sites for x in s['region_splices']})
    line_sites = [s for s in sites if s['line_splices']]
    hp_struct = sum(1 for i in res.get('items', []) if i['class'] == 'context-structure-changed' and
                    i['obligation'] == 'HP')
    ok = (code == 20 and fc.get('HP/FAIL/hp-unadjudicated') == 113 and fc.get('HP/FAIL/context-meaning-unverified') == 7
          and hp_struct == 7
          and fc.get('RET/FAIL/untracked-hp-overlap') == 19 and fc.get('RET/FAIL/context-meaning-unverified') == 5
          and fc.get('RET/REVIEW_REQUIRED/context-structure-changed') == 3 and not any('deny' in k for k in fc)
          and res['site_counts'].get('authorized-replacement') == 197 and res['site_counts'].get('authorized-removal') == 4
          and moved == 168 and shared == 22 and len(res.get('merger_groups', [])) == 9 and len(splices) == 31
          and (res.get('region_lines') or {}).get('count') == 215)
    a.record('RT-T0', ok, 'FAIL; HP 113/7/3; RET 19/5/3; deny 0; 383 unchanged (168 moved), 197 replaced, 4 removed; '
                          '215 region lines; 9 merger groups, 22 sites',
             {'exit': code, 'finding_counts': fc, 'site_counts': res.get('site_counts'), 'moved_H_T': moved,
              'merger_groups': len(res.get('merger_groups', [])), 'shared_sites': shared,
              'region_splices_distinct': len(splices), 'line_attributed_sites': len(line_sites),
              'hit_counts': res.get('hit_counts'), 'region_lines': res.get('region_lines')},
             predicate='exit 20; HP 113/7 and 7 HP structure REVIEWs; RET 19/5/3; no deny; 197 replaced, 4 removed; '
                       '168 moved; 22 shared sites in 9 groups; 31 region splices; region_lines.count == 215 (the '
                       'LF-inclusive site span, sec. 5)')
    a.results['RT-T'] = {'id': 'RT-T', 'passed': False, 'status': 'NOT RUN', 'predicate': None,
                         'expected': 'PASS only when every record verifies; any missing '
                                     'record leaves REVIEW_REQUIRED or FAIL. Reported NOT RUN while no reviewed record '
                                     'exists (sec. 10.4)',
                         'actual': {'note': 'no reviewed record exists; RT-T0 shows the result without them',
                                    'exit': code}}


def rt_terms(a):
    for c, name in ((H, 'H'), (E, 'E'), (T, 'T1p')):
        code, res, t = a.run(['terms', '--commit', c, '--profile', 'DR-1,DR-3,DR-4,DR-5'])
        ln, sl, per, alt = dl(res)
        a.results.setdefault('RT-DR', {'passed': True, 'expected': 'H: DR-1 61 (a 6, b 2, c 55), DR-3 0, DR-4 28, '
                                                                   'DR-5 1, 86 lines; E: 95; T1\': 0 / 0', 'actual': {}})
        a.results['RT-DR']['actual'][name] = {'exit': code, 'distinct_lines': len(ln), 'per_rule_lines': dict(per),
                                              'alternatives': dict(alt), 'with_sentence_lines': len(ln | sl)}
        if name == 'H':
            targets = [('DR-1', 'a', FULL, 6504), ('DR-1', 'a', 'book/glossary.md', 13),
                       ('DR-1', 'b', 'book/ch09-universality.md', 104), ('DR-1', 'c', FULL, 718),
                       ('DR-4', 'a', 'papers/Substratum.md', 92), ('DR-5', 'a', 'papers/Main.md', 736)]
            hit = []
            for rid, al, f, l in targets:
                hit.append(any(i['rule_id'] == rid and al in i.get('alternatives', []) and i.get('level') == 'line'
                               for i in items_on(res, f, l)))
            a.results['RT-DR']['actual']['targets_by_rule_id'] = hit
            ok = len(ln) == 86 and dict(per) == {'DR-1': 61, 'DR-4': 28, 'DR-5': 1} and all(hit) and \
                alt.get('DR-1a') == 6 and alt.get('DR-1b') == 2 and alt.get('DR-1c') == 55
        elif name == 'E':
            ok = len(ln) == 95
        else:
            ok = code == 0 and not ln and not sl
        a.results['RT-DR']['passed'] &= ok
    # RT-DR3W: control-only scan of AGENTS.md with DR-3 alone
    cfg = json.loads(a.repo.read(a.crev, a.cpath))
    controls = json.loads(a.repo.read(a.crev, cfg['controls']['path']))
    inputs = {i['id']: i for i in controls['control_inputs']}
    dr3 = [p for p in cfg['profiles'] if p['name'] == 'DR-3'][0]
    prof, _ = prf.load_profile(dr3, lambda s: a.repo.read(s.get('commit') or a.crev, s['path']))
    got = {}
    for key in ('agents-md-at-H', 'agents-md-at-T1p'):
        spec = inputs[key]
        data = a.repo.read(spec['commit'], spec['path'])
        assert sha(data) == spec['sha256']
        ss = util.sentences_of(util.lines_of(data.decode()), cfg['sentence']['abbreviations'], 2)
        got[key] = [(s1, s2) for s, s1, s2 in ss if prof.matches(s)]
    hgot = got['agents-md-at-H']
    a.record('RT-DR3W', len(hgot) == 1 and hgot[0][0] == 37 and hgot[0][1] >= 38 and not got['agents-md-at-T1p'],
             'exactly one DR-3 sentence at H starting on line 37 and including lines 37-38; 0 at T1\'', got)
    for c, name, want in ((T, 'T1p', (7, 4)), (H, 'H', (14, 179))):
        code, res, t = a.run(['terms', '--commit', c, '--profile', 'item7-literal'])
        lit = collections.Counter(x for i in res.get('items', []) for x in i.get('literals', []))
        rep = res.get('reports', {}).get('item7-literal', {}).get('report_regex_lines')
        n = len(res.get('items', []))
        a.results.setdefault('RT-I7', {'passed': True, 'expected': 'FAIL at both; T1\': 7 / 0 / 0, A1 4; H: 11 / 1 / 2, '
                                                                   'A1 179', 'actual': {}})
        a.results['RT-I7']['actual'][name] = {'exit': code, 'lines': n, 'literals': dict(lit), 'A1_lines': rep}
        a.results['RT-I7']['passed'] &= code == 20 and (n, rep) == want
    # RT-I7A and V3
    retired = retired_lines(a)
    for c, name in ((H, 'H'), (T, 'T1p')):
        code, res, t = a.run(['terms', '--commit', c, '--base', H, '--ledger', LEDGER, '--check', 'item7', '--final'],
                             control={'without_allow_rules': True})
        ln, sl, per, alt = dl(res)
        fu = {(i['file'], i['line']) for i in res.get('items', []) if i['class'] == 'final-unclassified'}
        act = {'exit': code, 'deny_lines': len(ln), 'deny_lines_with_sentences': len(ln | sl),
               'final_unclassified': len(fu), 'fail_lines': len(ln | fu), 'fail_lines_with_sentences': len(ln | sl | fu)}
        if name == 'H':
            only_review = [x for x in retired if x not in fu and x not in ln]
            act['retired_lines'] = len(retired)
            act['retired_FAIL'] = sum(1 for x in retired if x in fu or x in ln)
            act['retired_only_review'] = only_review
            ok = code == 20 and act['deny_lines'] == 86 and act['final_unclassified'] == 123 and \
                act['fail_lines'] == 209 and act['deny_lines_with_sentences'] == 93 and \
                act['fail_lines_with_sentences'] == 216 and len(retired) == 95 and not only_review
        else:
            act['lines'] = sorted('%s:%d' % x for x in fu)
            ok = code == 20 and act['deny_lines'] == 0 and act['final_unclassified'] == 12
        a.results.setdefault('RT-I7A', {'passed': True, 'expected': 'H: 86 deny + 123 final-unclassified = 209 (93 / '
                                                                    '216 with sentences); all 95 retired lines FAIL. '
                                                                    'T1\': 0 deny; 12 final-unclassified',
                                        'actual': {}})
        a.results['RT-I7A']['actual'][name] = act
        a.results['RT-I7A']['passed'] &= ok
    # V3 countercontrol: one retired line restored to REVIEW would be visible
    a.results['V3-countercontrol'] = v3_countercontrol(a, retired)
    code, res, t = a.run(['terms', '--commit', T, '--base', H, '--ledger', LEDGER, '--check', 'item7'])
    hits = res.get('hits', [])
    w_pass = sorted('%s:%d' % (h['file'], h['line']) for h in hits if h['state'] == 'PASS')
    resid = [h for h in hits if 'resid' in h['profiles'] and h['state'] != 'PASS']
    F_ = FULL
    w1_lines = [('papers/SM.md', 1394), ('book/ch09-universality.md', 137), ('book/ch19-open-problems.md', 198),
                ('book/ch19-open-problems.md', 212), (F_, 2554), (F_, 5270), (F_, 5284)]
    w2_lines = [('book/appendix-b-derivations.md', 235), ('book/appendix-b-derivations.md', 246), (F_, 5914),
                (F_, 5925)]
    st_of = {(h['file'], h['line']): h['state'] for h in hits}
    gr58 = st_of.get(('papers/GR.md', 58))
    others = {'p0-core', 'p0-para', 'ledger-ext', 'ptr', 'repo', 'count-grep'}
    # "hit by no other review profile": every review profile evaluated on the same tree (repo with its scope)
    c_all, r_all, _ = a.run(['terms', '--commit', T, '--base', H, '--ledger', LEDGER, '--profile',
                             ','.join(sorted(others | {'resid'})), '--scope',
                             '%s:%srecords/repo-scope-v1.json' % (a.crev, a.ad)])
    prof_at = {(h['file'], h['line']): set(h['profiles']) for h in r_all.get('hits', [])}
    resid_only = [h for h in resid if not prof_at.get((h['file'], h['line']), set()) & others]
    a.record('RT-D', not any(i['class'] == 'deny-match' for i in res.get('items', [])) and
             all(st_of.get(k) == 'PASS' for k in w1_lines + w2_lines) and gr58 == 'REVIEW_REQUIRED' and
             len(resid) == 45 and len(resid_only) == 17,
             '0 deny; all 7 W1 lines (W1-c with its allowance) and the 4 W2 lines PASS with their rules; GR.md:58 '
             'REVIEW without its record (PASS with it: RT-D-gr58); 45 resid lines REVIEW, 17 hit by no other profile',
             {'exit': code, 'finding_counts': res.get('finding_counts'), 'pass_lines': w_pass,
              'resid_review_lines': len(resid), 'resid_only_lines': len(resid_only), 'gr58': gr58,
              'w1_w2_states': {'%s:%d' % k: st_of.get(k) for k in w1_lines + w2_lines},
              'rule_negative': sorted(i['subject'] for i in res.get('items', []) if i['class'] == 'rule-negative-match')},
             reference_difference=None,
             predicate='no deny-match; the 11 W1/W2 hit states are PASS; GR.md:58 REVIEW_REQUIRED; 45 resid REVIEW lines '
                       'of which 17 carry no other review profile')
    code, res, t = a.run(['terms', '--commit', T, '--base', H, '--ledger', LEDGER, '--check', 'item7',
                          '--classify', '%s:%srecords/gr58-hit-classification-v1.json' % (a.crev, a.ad)])
    gr = [h for h in res.get('hits', []) if h['file'] == 'papers/GR.md' and h['line'] == 58]
    a.record('RT-D-gr58', gr and gr[0]['state'] == 'PASS', 'GR.md:58 PASS with its record',
             {'gr58': gr[0] if gr else None})
    # item 11 (repo) with the scope record
    code, res, t = a.run(['terms', '--commit', T, '--check', 'item11', '--scope',
                          '%s:%srecords/repo-scope-v1.json' % (a.crev, a.ad), '--final'])
    fu = [i for i in res.get('items', []) if i['class'] == 'final-unclassified']
    corpus_fu = [i for i in fu if i['file'].startswith(('papers/', 'book/'))]
    a.record('item11-T1p', code == 20, 'FAIL final-unclassified for each of the 176 lines (sec. 8.2) until each has '
                                       'an exact rule', {'exit': code, 'final_unclassified': len(fu),
                                                         'of_them_corpus': len(corpus_fu),
                                                         'hit_pass': sum(1 for h in res.get('hits', [])
                                                                         if h['state'] == 'PASS')})


def retired_lines(a):
    import re
    out = []
    lit = ('Fourteen', 'six structural', 'sixth of')
    for f in sorted(p for p in a.base.paths(H) if p.endswith('.md') and p.count('/') == 1 and
                    p.split('/')[0] in ('papers', 'book')):
        hl = a.lines(H, f)
        tl = set(a.lines(T, f)) if a.base.blob_id(T, f) else set()
        for i, l in enumerate(hl, 1):
            if (re.search(r'\bA1\b', l) or any(x in l for x in lit)) and l not in tl:
                out.append((f, i))
    # less the deny lines (the design's 95 match no deny rule)
    code, res, t = a.run(['terms', '--commit', H, '--profile', 'DR-1,DR-3,DR-4,DR-5'])
    ln, sl, per, alt = dl(res)
    return [x for x in out if x not in ln]


def v3_countercontrol(a, retired):
    """Both directions: under item 7 without --final the retired lines are REVIEW, with --final FAIL."""
    code, res, t = a.run(['terms', '--commit', H, '--base', H, '--ledger', LEDGER, '--check', 'item7'],
                         control={'without_allow_rules': True})
    rv = {(i['file'], i['line']) for i in res.get('items', []) if i['class'] == 'unclassified'}
    return {'passed': all(x in rv for x in retired) and code == 20,
            'expected': 'without --final each of the 95 is REVIEW (unclassified); with --final FAIL (RT-I7A)',
            'actual': {'review_without_final': sum(1 for x in retired if x in rv)}}


# ---- adversarial controls on a T1'-style X -----------------------------------------------------------------

def v_controls(a):
    def terms_added(cid, f, text, check='item7', final=False, profile=None, expect=None, line_expect=None,
                    without_rules=False, extra=None):
        x, led = a.add_eof(f, text)
        args = ['terms', '--commit', x, '--base', H, '--ledger', LEDGER]
        args += ['--profile', profile] if profile else ['--check', check]
        if final:
            args.append('--final')
        ctl = {'overrides': {'ledger': led}}
        if without_rules:
            ctl['without_allow_rules'] = True
        code, res, t = a.run(args, control=ctl)
        n0 = len(a.lines(T, f)) + 1
        new = [n0 + k + 1 for k in range(text.count('\n'))]
        its = [i for i in res.get('items', []) if i.get('file') == f and i.get('line') in new]
        hits = [h for h in res.get('hits', []) if h['file'] == f and h['line'] in new]
        return code, res, its, hits
    # deny controls
    for cid, f, text, rule, alt in [
            ('V1', 'book/appendix-b-derivations.md', 'The six structural properties of the substratum are listed in Chapter 2.\n', 'DR-1', 'b'),
            ('V3', 'book/appendix-b-derivations.md', '(A1) the substratum is finite in total\n', 'DR-4', 'a'),
            ('V5', 'book/appendix-b-derivations.md', '**(A1) Finiteness.** The configuration space is finite.\n', 'DR-4', 'a'),
            ('V9', 'papers/GR.md', 'Six structural assumptions define the substratum.\n', 'DR-1', 'a'),
            ('V10', 'papers/GR.md', 'the six structural conditions on the substratum\n', 'DR-1', 'a'),
            ('V11', 'papers/GR.md', 'six structural premises of the framework\n', 'DR-1', 'a'),
            ('V12', 'papers/GR.md', 'the six substratum posits\n', 'DR-1', 'a'),
            ('V13', 'papers/GR.md', 'the structural assumptions A1 through A6\n', 'DR-1', 'c'),
            ('V16', 'papers/GR.md', 'posit A1 (finiteness) holds\n', 'DR-4', 'a'),
            ('V17', 'papers/GR.md', 'A1 (Finiteness): the configuration space is finite\n', 'DR-4', 'a'),
            ('V18', 'papers/GR.md', '(A1) Finiteness. The configuration space S is finite.\n', 'DR-4', 'a'),
            ('V19', 'papers/GR.md', 'The posit ledger has 14 items.\n', 'DR-5', 'a'),
            ('V20', 'papers/GR.md', 'the six structural properties of the bijection, the first being finiteness of S\n', 'DR-3', None)]:
        code, res, its, hits = terms_added(cid, f, text)
        deny = [i for i in its if i['class'] == 'deny-match']
        ok = code == 20 and any(i['rule_id'] == rule and (alt is None or alt in i.get('alternatives', []))
                                for i in deny)
        a.record(cid, ok, 'FAIL deny-match by %s%s' % (rule, alt or ''), {'exit': code, 'deny': sorted(
            {(i['rule_id'], tuple(i.get('alternatives', [])), i.get('level')) for i in deny})})
    v14 = []
    for t_ in ('A1--A6\n', 'A1—A6\n', '(A1)–(A6)\n', 'A1, ..., A6\n'):
        code, res, its, hits = terms_added('V14', 'papers/GR.md', t_)
        v14.append(any(i['rule_id'] == 'DR-1' and 'c' in i.get('alternatives', []) for i in its))
    a.record('V14', all(v14), 'FAIL deny-match DR-1c, each of four', v14)
    code, res, its, hits = terms_added('V6', 'papers/GR.md',
                                       'the six structural properties of the substratum, including finiteness\n')
    rids = {i['rule_id'] for i in its if i['class'] == 'deny-match'}
    a.record('V6', code == 20 and {'DR-1', 'DR-3'} <= rids, 'FAIL deny-match DR-1b and DR-3', sorted(rids))
    code, res, its, hits = terms_added('V22', 'papers/Main.md', 'Fourteen items, of unequal weight, and not fourteen '
                                                                'independent physical assumptions.\n')
    rids = {i['rule_id'] for i in its if i['class'] == 'deny-match'}
    code_l, res_l, its_l, _ = terms_added('V22b', 'papers/Main.md', 'Fourteen items, of unequal weight, and not '
                                                                     'fourteen independent physical assumptions.\n',
                                          profile='item7-literal')
    a.record('V22', 'DR-5' in rids and code_l == 20, 'FAIL deny-match DR-5; the literal item 7 fails too',
             {'rules': sorted(rids), 'literal_exit': code_l})
    # residuals and resid
    for cid, f, text, exp in [('V4', 'papers/GR.md', "the framework's sixth structural property, finiteness of the bijection\n", 'PASS'),
                              ('V27', 'papers/GR.md', "The framework's sixth structural property is finiteness of the substratum\n", 'PASS'),
                              ('V15', 'papers/GR.md', "the substratum's sixth axiom, finiteness\n", 'REVIEW'),
                              ('V21', 'papers/GR.md', 'one of the posits is that the configuration space is finite\n', 'REVIEW')]:
        code, res, its, hits = terms_added(cid, f, text)
        if exp == 'PASS':
            ok = not its and not hits
            # the original literal item 7 misses it too
            c2, r2, i2, h2 = terms_added(cid, f, text, profile='item7-literal')
            ok = ok and not i2
        else:
            ok = [i['class'] for i in its] == ['unclassified'] and all(h['profiles'] == ['resid'] for h in hits)
        a.record(cid, ok, exp + (' (no hit); accepted residual (sec. 1, sec. 15 items 2 and 3)' if exp == 'PASS'
                                 else ' unclassified via resid only'),
                 {'items': [(i['class'], i.get('profiles')) for i in its], 'hits': [h['profiles'] for h in hits]})
    gl = a.lines(H, 'book/glossary.md')[12]
    mut = gl.replace("The sixth of the framework's structural assumptions A1–A6",
                     "The framework's sixth structural property is finiteness of the substratum")
    code, res, its, hits = terms_added('V27b', 'book/glossary.md', mut + '\n')
    a.record('V27-glossary', not its and not hits, 'PASS (no hit) as the edited glossary.md:13 line',
             {'items': [(i['class'], i.get('rule_id')) for i in its], 'hits': [h['profiles'] for h in hits],
              'line': mut[:140]})
    res26 = []
    for text, key in [('a finite set with a deterministic bijection on it\n', 'b'),
                      ('the substratum is a finite set with a bijection on it\n', 'b'),
                      ('We take the substratum to be finite.\n', 'b'), ('the universe is assumed finite\n', 'b'),
                      ('The substratum is assumed to have a finite number of states.\n', 'c')]:
        code, res, its, hits = terms_added('V26', 'papers/GR.md', text)
        ok = [i['class'] for i in its] == ['unclassified'] and hits and key in hits[0]['keys'].get('resid', [])
        res26.append((ok, hits[0]['keys'] if hits else None))
    a.record('V26', all(x[0] for x in res26), 'REVIEW unclassified each, resid (b, b, b, b, c)', res26)
    # item 7 with --final: V23, V24, V25
    l136 = a.lines(H, 'book/ch02-substratum.md')[135] + '\n'
    code, res, its, hits = terms_added('V23', 'book/ch02-substratum.md', l136, final=True)
    a.record('V23', code == 20 and [i['class'] for i in its] == ['final-unclassified'] and
             not any(i['class'] == 'deny-match' for i in its), 'FAIL final-unclassified (ptr hit; no deny)',
             [(i['class'], i.get('profiles')) for i in its])
    code, res, its, hits = terms_added('V24', 'papers/GR.md', 'six structural hypotheses\n', final=True)
    a.record('V24', code == 20 and [i['class'] for i in its] == ['final-unclassified'],
             'FAIL final-unclassified (count-grep hit; no deny)', [(i['class'], i.get('profiles')) for i in its])
    c1, r1, i1, h1 = terms_added('V25', 'book/ch02-substratum.md', l136)
    c2, r2, i2, h2 = terms_added('V25', 'papers/GR.md', 'six structural hypotheses\n')
    c3, r3, i3, h3 = terms_added('V25', 'papers/GR.md', 'one of the posits is that the configuration space is finite\n',
                                 final=True)
    w2 = [h for h in r3.get('hits', []) if h['file'] == 'book/appendix-b-derivations.md' and h['line'] in (235, 246)]
    ok = [i['class'] for i in i1] == ['unclassified'] and [i['class'] for i in i2] == ['unclassified'] and \
        [i['class'] for i in i3] == ['unclassified'] and w2 and all(h['state'] == 'PASS' for h in w2)
    a.record('V25', ok, 'without --final REVIEW; W2 line with its rule under --final PASS; resid-only stays REVIEW '
                        'under --final', {'v23': [i['class'] for i in i1], 'v24': [i['class'] for i in i2],
                                          'resid_final': [i['class'] for i in i3],
                                          'w2_states': [h['state'] for h in w2]})
    # V2 and V7a-c: edits of the W1-d sentence (ch19:212)
    ch = 'book/ch19-open-problems.md'
    t19 = a.lines(T, ch)
    old = "The framework's six structural properties of the bijection (developed across Chapters 5-7) further narrow it."
    assert old in t19[211]
    v2 = t19[211].replace(old, "The framework's six structural properties of the bijection, one of which is total "
                               "finiteness, further narrow it.")

    def edited(f, ln, new, profile=None, check='item7'):
        lines = a.lines(T, f)
        lines[ln - 1] = new
        x = a.repo.derive(T, {f: ('\n'.join(lines) + '\n').encode()}, parents=[H])
        args = ['terms', '--commit', x] + (['--profile', profile] if profile else ['--check', check])
        code, res, t = a.run(args)
        return code, res, items_on(res, f, ln)
    code, res, its = edited(ch, 212, v2)
    a.record('V2', code == 20 and any(i['class'] == 'deny-match' and i['rule_id'] == 'DR-3'
                                      for i in res.get('items', []) if i.get('file') == ch),
             'FAIL deny-match DR-3', sorted({(i['class'], str(i.get('rule_id'))) for i in res.get('items', [])
                                             if i.get('file') == ch}))
    code, res, its = edited(ch, 212, v2, profile='count-grep,ptr')
    a.record('V7a', [i['class'] for i in its] == ['rule-negative-match'] and its[0]['rule_id'] == 'W1-d',
             "FAIL rule-negative-match (W1's negative matcher)", [(i['class'], i.get('rule_id')) for i in its])
    code, res, its, hits = terms_added('V7b', 'papers/GR.md', "The framework's six structural properties of the "
                                                              "bijection, one of which is total finiteness, further "
                                                              "narrow it.\n", profile='p0-core,count-grep')
    a.record('V7b', [i['class'] for i in its] == ['unclassified'] and set(its[0]['profiles']) == {'p0-core', 'count-grep'},
             'REVIEW unclassified (p0-core and count-grep hits, no rule)', [(i['class'], i.get('profiles')) for i in its])
    ch9 = 'book/ch09-universality.md'
    v7c = a.lines(T, ch9)[136].replace('generation count', 'generation number')
    code, res, its = edited(ch9, 137, v7c, profile='count-grep')
    a.record('V7c', [i['class'] for i in its] == ['rule-fingerprint-mismatch'], 'REVIEW rule-fingerprint-mismatch',
             [(i['class'], i.get('rule_id')) for i in its])
    a.record('S1r', [i['class'] for i in its] == ['rule-fingerprint-mismatch'], 'REVIEW rule-fingerprint-mismatch',
             'as V7c')
    lines = a.lines(T, ch)
    del lines[211]
    x = a.repo.derive(T, {ch: ('\n'.join(lines) + '\n').encode()}, parents=[H])
    code, res, t = a.run(['terms', '--commit', x, '--profile', 'count-grep'])
    a.record('S2r', any(i['class'] == 'rule-stale' and i['rule_id'] == 'W1-d' for i in res.get('items', [])),
             'REVIEW rule-stale', sorted({(i['class'], i.get('rule_id')) for i in res.get('items', [])}))
    # L1-L4
    lines = a.lines(T, ch)
    x = a.repo.derive(T, {ch: ('\n'.join(lines[:205] + ['filler %d.' % k for k in range(40)] + lines[205:]) + '\n').encode()},
                      parents=[H])
    code, res, t = a.run(['terms', '--commit', x, '--profile', 'count-grep'])
    w = [h for h in res.get('hits', []) if h['file'] == ch and h['line'] == 252]
    a.record('L1', w and w[0]['state'] == 'PASS' and w[0].get('rule_id') == 'W1-d', 'PASS (W1 rule)',
             w[0] if w else None)
    ap = 'book/appendix-b-derivations.md'
    al = a.lines(T, ap)
    x = a.repo.derive(T, {ap: ('\n'.join(['moved %d.' % k for k in range(7)] + al) + '\n').encode()}, parents=[H])
    code, res, t = a.run(['terms', '--commit', x, '--profile', 'ptr'])
    w = [h for h in res.get('hits', []) if h['file'] == ap and h['line'] in (242, 253)]
    a.record('L2', len(w) == 2 and all(h['state'] == 'PASS' for h in w), 'PASS (W2 rule)', [h['state'] for h in w])
    code, res, its, hits = terms_added('L3', ch, old + '\n', profile='count-grep')
    a.record('L3', [i['class'] for i in its] == ['rule-overreach'], 'FAIL rule-overreach', [i['class'] for i in its])
    code, res, its, hits = terms_added('L4', 'papers/GR.md', old + '\n', profile='count-grep')
    a.record('L4', [i['class'] for i in its] == ['unclassified'], 'REVIEW unclassified', [i['class'] for i in its])
    # N-W: no deny rule matches a W1 or W2 line, or Main.md:738, at T1'
    code, res, t = a.run(['terms', '--commit', T, '--profile', 'DR-1,DR-3,DR-4,DR-5'])
    a.record('N-W', code == 0, 'no deny match', {'exit': code})


def pipeline_rule_controls(a, cfg, allow_ref, deny_ref, allow, deny, w1, rec, st):
    """B6: A1r-A11r run the mutated rule file through the pipeline (op D at T1', item 7) and require an emitted
    FAIL record-invalid naming that rule file (A5r: FAIL deny-match), not a truthy lint result."""
    import copy as cp
    dr1 = [r for r in deny['rules'] if r['id'] == 'DR-1'][0]
    dr5 = [r for r in deny['rules'] if r['id'] == 'DR-5'][0]

    def allow_mut(fn):
        d = cp.deepcopy(allow)
        d['supersedes'] = {'path': allow_ref['path'], 'blob_sha256': allow_ref['blob_sha256']}
        for r in d['rules']:
            if r['id'] == w1['id']:
                fn(r)
        return allow_ref['path'], d

    def deny_mut(fn, sup=True):
        d = cp.deepcopy(deny)
        if sup:
            d['supersedes'] = {'path': deny_ref['path'], 'blob_sha256': deny_ref['blob_sha256']}
        for r in d['rules']:
            if r['id'] in ('DR-1', 'DR-5'):
                fn(r)
        return deny_ref['path'], d

    def fp_swap(r):
        r['fingerprints'][0] = dict(r['fingerprints'][0], sentence_sha256=sha(b'another sentence'))
    muts = {
        'A1r': ('widening (added files)', allow_mut(lambda r: r['scope'].update(files=r['scope']['files'] +
                                                                                  ['book/x.md']))),
        'A2r': ('widening (a changed, shorter literal)', allow_mut(lambda r: r['matcher'].update(
            literal='six structural'))),
        'A3r': ('widening (fingerprint swap, count unchanged)', allow_mut(fp_swap)),
        'A6r': ('lint: the literal does not cover the trigger', allow_mut(lambda r: r['matcher'].update(
            literal='further narrow it'))),
        'A8r': ('lint: no negative example', allow_mut(lambda r: r.update(negative_examples=[]))),
        'A9r': ('deny widening (changed pattern) and its own negative example matched', deny_mut(
            lambda r: r['patterns'].update(a=r['patterns']['a'] + '|structural propert') if r['id'] == 'DR-1'
            else None)),
        'A10r': ('deny widening (narrower scope)', deny_mut(lambda r: r.update(scope=['papers/Main.md'])
                                                            if r['id'] == 'DR-1' else None)),
        'A11r': ('lint: the countercontrol does not match', deny_mut(lambda r: r.update(countercontrol=[
            {'commit': H, 'path': 'papers/Main.md', 'line': 1, 'alternative': 'a'}]) if r['id'] == 'DR-5' else None,
            sup=False)),
    }
    # the clean baseline of the restored cases (OBL-20): the same run with no rule file replaced
    a.run(['terms', '--commit', T, '--check', 'item7'], control={'force_widening': True}, case='baseline')
    baseline = a.rec.take()[0]
    for cid, (what, (path, doc)) in sorted(muts.items()):
        def repl(files, path=path, doc=doc):
            return [(r, doc if r['path'] == path else d) for r, d in files]
        code, res, t = a.run(['terms', '--commit', T, '--check', 'item7'],
                             control={'replace_rule_files': repl, 'force_widening': True},
                             mutation=[{'path': path, 'before': None, 'after': sha(doc) if isinstance(doc, bytes)
                                        else None}], bindings={'rule_file': path})
        # the restored case: the unmutated tree, the same command and flags, compared with the clean baseline
        a.run(['terms', '--commit', T, '--check', 'item7'], control={'force_widening': True}, case='restored',
              baseline=baseline, bindings={'rule_file': path})
        ri = sorted({i['class'] for i in res.get('items', []) if i.get('subject') == path})
        a.record(cid, code == 20 and ri == ['record-invalid'], what + ' -> FAIL record-invalid, emitted by the pipeline',
                 {'exit': code, 'classes_for_the_rule_file': ri,
                  'why': [i.get('detail') for i in res.get('items', []) if i.get('subject') == path][:1]},
                 predicate='exit == 20 and the classes of the items naming the rule file == [record-invalid]')
    # A4r: a widening review written by the rule's author is rejected; through the pipeline no admitted widening
    # review exists, so the widened file is record-invalid
    path, doc = muts['A1r'][1]
    probs = rec.widening_review_problems({'path': 'r.json', 'blob_sha256': sha(b'{}')}, st, set(st.by_sha), set(),
                                         w1['author'], None, ['W1-d:added files'])

    def repl4(files):
        return [(r, doc if r['path'] == path else d) for r, d in files]
    code, res, t = a.run(['terms', '--commit', T, '--check', 'item7'],
                         control={'replace_rule_files': repl4, 'force_widening': True})
    ri = sorted({i['class'] for i in res.get('items', []) if i.get('subject') == path})
    a.record('A4r', code == 20 and ri == ['record-invalid'] and any('author' in p for p in probs),
             'a widening review by the author is rejected -> FAIL record-invalid',
             {'exit': code, 'classes': ri, 'review_problems': probs[:2]},
             predicate='exit == 20, record-invalid for the rule file, and the author-written review is rejected')
    # A7r: a reused rule id in a second admitted rule file
    dup = dict(allow, record_id='dup', supersedes=None, rules=[dict(w1)])

    def repl7(files):
        return list(files) + [({'path': a.ad + 'rules/dup.json', 'blob_sha256': sha(util.canonical(dup))}, dup)]
    code, res, t = a.run(['terms', '--commit', T, '--check', 'item7'], control={'replace_rule_files': repl7})
    ri = sorted({i['class'] for i in res.get('items', []) if i.get('subject') == a.ad + 'rules/dup.json'})
    a.record('A7r', code == 20 and ri == ['record-invalid'], 'a reused rule id -> FAIL record-invalid',
             {'exit': code, 'classes': ri}, predicate='exit == 20 and record-invalid for the second file')


def rule_lint_controls(a):
    """A1r-A11r and A5r on the drafted A1 rule files, with a synthetic review chain in memory."""
    cfg = json.loads(a.repo.read(a.crev, a.cpath))
    allow_ref = [r for r in cfg['rules'] if 'allow' in r['path']][0]
    deny_ref = [r for r in cfg['rules'] if 'deny' in r['path']][0]
    allow = json.loads(a.repo.read(a.crev, allow_ref['path']))
    deny = json.loads(a.repo.read(a.crev, deny_ref['path']))
    w1 = [r for r in allow['rules'] if r['id'] == 'W1-d'][0]
    loaded = cfgmod_loaded(a)
    ctx = pl.RunContext(a.repo, cfg, loaded.profiles, [], {}, None)
    lk = cli.lookups(ctx, loaded)

    def lint(r):
        return rulemod.lint_rule(r, lk['profile'], lk['sentence'], lk['deny'], lk['control_input'])
    base_ok = lint(w1) == []
    res = {}
    res['A1r'] = bool(rulemod.allow_widening(w1, dict(w1, scope={'files': w1['scope']['files'] + ['book/x.md']})))
    res['A2r'] = bool(rulemod.allow_widening(w1, dict(w1, matcher=dict(w1['matcher'], literal='six structural'))))
    fp = dict(w1['fingerprints'][0], sentence_sha256=sha(b'another sentence'))
    res['A3r'] = bool(rulemod.allow_widening(w1, dict(w1, fingerprints=[fp, w1['fingerprints'][1]])))
    st = rec.Store([('r.json', b'{}'), ('w.json', util.canonical({'schema': rec.review_schema, 'kind': 'widening',
                                                                   'reviewer': w1['author'],
                                                                   'reviewed': {'path': 'r.json',
                                                                                'blob_sha256': sha(b'{}')},
                                                                   'verdicts': [{'item': 'x', 'verdict': 'accept'}]}))])
    res['A4r'] = not rec.widening_review_ok({'path': 'r.json', 'blob_sha256': sha(b'{}')}, st,
                                            set(st.by_sha), set(), w1['author'])
    res['A6r'] = bool(lint(dict(w1, matcher=dict(w1['matcher'], literal='further narrow it'))))
    res['A8r'] = bool(lint(dict(w1, negative_examples=[])))
    dr1 = [r for r in deny['rules'] if r['id'] == 'DR-1'][0]
    wide = dict(dr1, patterns=dict(dr1['patterns'], a=dr1['patterns']['a'] + '|structural propert'))
    res['A9r'] = bool(rulemod.deny_widening(dr1, wide)) and bool(lint(wide))
    res['A10r'] = bool(rulemod.deny_widening(dict(dr1, scope=['papers/Main.md', 'book/ch01-observation.md']),
                                             dict(dr1, scope=['papers/Main.md'])))
    dr5 = [r for r in deny['rules'] if r['id'] == 'DR-5'][0]
    res['A11r'] = bool(lint(dict(dr5, countercontrol=[{'commit': H, 'path': 'papers/Main.md', 'line': 1,
                                                       'alternative': 'a'}]))) and lint(dr5) == []
    ids = {}
    for f in (allow, deny):
        for r in f['rules']:
            ids.setdefault(r['id'], 0)
            ids[r['id']] += 1
    res['A7r'] = True
    loaded2 = cfgmod_loaded(a)
    dup = dict(allow, record_id='dup', rules=[dict(w1)])
    loaded2.rule_files = list(loaded2.rule_files) + [({'path': 'dup.json', 'blob_sha256': sha(util.canonical(dup))}, dup)]
    allow_rules, items = cli.rule_files(loaded2, True, lk)
    res['A7r'] = any('reused' in str(i.get('detail')) for i in items)
    # A5r: an allow rule fingerprinting a sentence that a deny rule matches
    v20 = "The framework's six structural properties of the bijection, one of which is total finiteness, further narrow it."
    lines = a.lines(T, 'book/ch19-open-problems.md')
    lines[211] = lines[211].replace("The framework's six structural properties of the bijection (developed across "
                                    "Chapters 5-7) further narrow it.", v20)
    x = a.repo.derive(T, {'book/ch19-open-problems.md': ('\n'.join(lines) + '\n').encode()}, parents=[H])
    sents = util.sentences_of(lines, cfg['sentence']['abbreviations'], 2)
    k = [i for i, s in enumerate(sents) if s[0] == v20][0]
    bad = dict(w1, id='W1-z', matcher=dict(w1['matcher'], negative=[]),
               fingerprints=[{'file': 'book/ch19-open-problems.md', 'sentence_sha256': sha(v20.encode()),
                              'context_sha256': rulemod.sentence_context_sha(sents, k)}], max_instances=1)

    def replace(rfs):
        out = []
        for r, d in rfs:
            if d and any(x.get('kind') == 'allow' for x in d.get('rules', [])):
                d = dict(d, rules=[bad])
            out.append((r, d))
        return out
    code, resx, t = a.run(['terms', '--commit', x, '--profile', 'count-grep,DR-3'], control={'replace_rule_files': replace})
    on = items_on(resx, 'book/ch19-open-problems.md', 212)
    res['A5r'] = any(i['class'] == 'deny-match' for i in on)
    a.record('A5r', res['A5r'] and base_ok, 'FAIL deny-match (a fingerprinted sentence a deny rule matches)',
             {'deny_match_on_line': res['A5r'], 'unmutated_rule_lints_clean': base_ok},
             predicate='a deny-match item on ch19:212 emitted by the pipeline')
    pipeline_rule_controls(a, cfg, allow_ref, deny_ref, allow, deny, w1, rec, st)
    return
    exp = {'A1r': 'widening (added files)', 'A2r': 'widening (literal)', 'A3r': 'widening (fingerprint swap)',
           'A4r': 'widening review by the author rejected', 'A5r': 'FAIL deny-match', 'A6r': 'lint: literal does not '
           'cover the trigger', 'A7r': 'reused id', 'A8r': 'lint: no negative example', 'A9r': 'deny widening and '
           'its own negative example matched', 'A10r': 'deny widening (narrower scope)', 'A11r': 'lint: countercontrol '
           'does not match'}
    for k_, v in res.items():
        a.record(k_, v and base_ok, exp[k_] + ' -> FAIL record-invalid (A5r: deny-match)', {'detected': v,
                                                                                            'unmutated_rule_lints_clean': base_ok})


def cfgmod_loaded(a):
    from ledger_coverage.engine import config as cfgmod
    return cfgmod.load(a.repo, a.crev, a.cpath, a.csha, 'terms', 'harness')


# ---- op C: RT-C, G, sec. 11 countercontrols, four trees ------------------------------------------------------

def drift_classes(a):
    """In-memory draft class records for the two side changes on main that are not this tool's (the trial
    workflow and the tool configuration file), each pinned to its blob at main; they belong to the drift records,
    not to this directory (one definition per class id, S7)."""
    if getattr(a, '_drift', None):
        return a._drift
    classes = []
    for cid, path in (('trial-workflow', WF), ('tool-configuration', '.claude/settings.json')):
        b = a.repo.read(a.main, path)
        classes.append({'id': cid, 'pins': [{'path': path, 'git_blob': a.repo.blob_id(a.main, path),
                                             'blob_sha256': sha(b)}]})
    doc = {'schema': 'oi-side-change-classes/1', 'record_id': 'control-drift-classes', 'author': 'control-writer',
           'supersedes': None, 'classes': classes}
    c = a.repo.derive(a.crev, {a.ad + 'records/control-drift-classes.json': (json.dumps(doc) + '\n').encode()},
                      parents=a.repo.parents(a.crev), subject='control class records')
    a._drift = '%s:%srecords/control-drift-classes.json' % (c, a.ad)
    return a._drift


def exec_args(a, x=T, extra=()):
    return ['execution', '--scientific-base', H, '--candidate', x, '--ledger', LEDGER, '--edits', EDITS,
            '--delegation', '%s:%sdelegation-draft.json' % (a.crev, a.ad),
            '--classify', '%s:%srecords/side-change-classes-v4.json' % (a.crev, a.ad),
            '--classify', drift_classes(a)] + list(extra)


def ex_controls(a):
    code, res, t = a.run(exec_args(a))
    fc = res.get('finding_counts', {})
    non_deleg = {k: v for k, v in fc.items() if not k.startswith('DELEGATED')}
    a.record('RT-C', code == 10 and not non_deleg, 'candidate checks as sec. 11; PASS only with contract evidence; '
                                                   'without it REVIEW delegated-evidence-missing',
             {'exit': code, 'finding_counts': fc, 'checks': res.get('checks'), 'seconds': t,
              'delegation': res.get('delegation')})
    # G1: tex evidence whose candidate is an abbreviation
    ev = tempfile.mkdtemp(dir=a.out_root)
    with open(os.path.join(ev, 'tex-preserve-check.json'), 'w') as f:
        json.dump({'schema': 'a1exit-checker-result-v1', 'checker': 'preserve_check.py', 'plan': None, 'base': H,
                   'ledger_base': H, 'candidate': T[:8], 'exit': 0, 'verdict': 'pass', 'checks': []}, f)
    code, res, t = a.run(exec_args(a, extra=['--evidence', ev]))
    a.record('G1', any(i['class'] == 'delegated-evidence-invalid' and 'tex' in i['subject'] for i in res.get('items', [])),
             'FAIL delegated-evidence-invalid', sorted(i['subject'][:80] for i in res.get('items', [])
                                                       if i['class'] == 'delegated-evidence-invalid'))
    a.record('G2', any(i['class'] == 'delegated-evidence-missing' for i in a.run(exec_args(a))[1].get('items', [])),
             'REVIEW delegated-evidence-missing', 'as RT-C')
    lj = 'verification/coverage/LEDGER.json'
    x = a.repo.derive(T, {lj: a.repo.read(T, lj).replace(b'"id": "MAIN:L-3"', b'"id": "MAIN:L-3x"', 1)}, parents=[H])
    code, res, t = a.run(exec_args(a, x))
    a.record('G3', any(i['class'] == 'delegated-evidence-invalid' and 'coverage-ledger' in i['subject']
                       for i in res.get('items', [])), 'FAIL', sorted(i['subject'][:90] for i in res.get('items', [])
                                                                      if i['class'] == 'delegated-evidence-invalid'))
    # sec. 11 countercontrols
    sp = [s for s in a.led['splices'] if s['file'] == 'papers/Main.md'][0]
    hm, tm = a.base.read(H, 'papers/Main.md'), a.base.read(T, 'papers/Main.md')
    reverted = exmod.sg.apply_splices(hm, [s for s in a.led['splices'] if s['file'] == 'papers/Main.md' and s is not sp])
    x = a.repo.derive(T, {'papers/Main.md': reverted}, parents=[H])
    code, res, t = a.run(exec_args(a, x))
    a.record('S11-1', 'unauthorized-edit' in classes(res), 'FAIL unauthorized-edit', classes(res))
    for cid, word, rule in (('S11-5', ' no longer', 'register'), ('S11-6', ' is infinite', 'infinity')):
        s0 = [s for s in a.led['splices'] if s['file'] == 'papers/GR.md' and s['new']][0]
        led = dict(a.led)
        led['splices'] = [dict(s, new=s['new'] + word, new_bytes=(s['new'] + word).encode(),
                               new_sha256=sha((s['new'] + word).encode())) if s is s0 else s for s in a.led['splices']]
        gx = exmod.sg.apply_splices(a.base.read(H, 'papers/GR.md'), [s for s in led['splices'] if s['file'] == 'papers/GR.md'])
        x = a.repo.derive(T, {'papers/GR.md': gx}, parents=[H])
        code, res, t = a.run(exec_args(a, x), control={'overrides': {'ledger': led}})
        a.record(cid, any(i['class'] == 'deny-match' and i.get('rule_id') == rule for i in res.get('items', [])),
                 'FAIL deny-match (%s)' % rule, sorted({(i['class'], str(i.get('rule_id'))) for i in res.get('items', [])
                                                        if not i['class'].startswith('delegated')}))
    mirror = [m for m in a.led['mirrors'] if m['mirror_of']][0]
    led = dict(a.led)
    led['splices'] = [dict(s, new=s['new'] + ' x', new_bytes=(s['new'] + ' x').encode(),
                           new_sha256=sha((s['new'] + ' x').encode())) if s['id'] == mirror['id'] else s
                      for s in a.led['splices']]
    code, res, t = a.run(exec_args(a), control={'overrides': {'ledger': led}})
    a.record('S11-8', 'mirror-mismatch' in classes(res), 'FAIL mirror-mismatch', classes(res))
    cen = 'verification/lean-manuscript-census.json'
    css = [s for s in a.led['splices'] if s['file'] == cen]
    x = a.repo.derive(T, {cen: exmod.sg.apply_splices(a.base.read(H, cen), css[1:])}, parents=[H])
    code, res, t = a.run(exec_args(a, x))
    a.record('S11-9', 'unauthorized-edit' in classes(res), 'FAIL unauthorized-edit (%d census splices)' % len(css),
             classes(res))
    lean = sorted(f for f in a.led['files'] if f.endswith('.lean'))[0]
    x = a.repo.derive(T, {lean: a.repo.read(T, lean) + b'\ndef controlDefinition : Nat := 1\n'}, parents=[H])
    code, res, t = a.run(exec_args(a, x))
    a.record('S11-10', 'lean-code-change' in classes(res), 'FAIL lean-code-change', classes(res))
    gp = [e for e in a.led['raw']['edits'] if e.get('kind') == 'guard-pin' and e.get('targets')][0]
    x = a.repo.derive(T, {gp['file']: a.base.read(H, gp['file'])}, parents=[H])
    code, res, t = a.run(exec_args(a, x))
    a.record('S11-12', 'pin-broken' in classes(res) or 'pin-target-missing' in classes(res),
             'FAIL pin-broken (a guard-pin splice dropped)', classes(res))
    x = a.repo.derive(T, {'tools/new_active_control.py': b'# the A1 premise holds here\n'}, parents=[H])
    code, res, t = a.run(['terms', '--commit', x, '--check', 'item11', '--scope',
                          '%s:%srecords/repo-scope-v1.json' % (a.crev, a.ad), '--final'])
    a.record('S11-11', any(i['class'] == 'final-unclassified' and i['file'] == 'tools/new_active_control.py'
                           for i in res.get('items', [])), 'FAIL final-unclassified', 'new active file')
    x = a.repo.derive(T, {'README.md': a.repo.read(T, 'README.md') + b'extra\n'}, parents=[H])
    code, res, t = a.run(exec_args(a, x))
    a.record('S11-14', 'unauthorized-change' in classes(res), 'FAIL unauthorized-change', classes(res))
    sc = 'verification/audits/manuscript/bell-operational-reconciliation-20261029/sc42-integration-result.json'
    ev = tempfile.mkdtemp(dir=a.out_root)
    with open(os.path.join(ev, 'sc42-rerun.json'), 'w') as f:
        json.dump({'candidate': T, 'verbose_exit': 0, 'verbose_equal': False, 'self_test_equal': True}, f)
    code, res, t = a.run(exec_args(a, extra=['--evidence', ev]))
    a.record('S11-13', any(i['class'] == 'delegated-evidence-invalid' and i['subject'].startswith('sc42')
                           for i in res.get('items', [])),
             'FAIL (the re-execution does not reproduce the hand-edited file)',
             'control evidence states verbose_equal false')
    ev = tempfile.mkdtemp(dir=a.out_root)
    with open(os.path.join(ev, 'ci-host-run.json'), 'w') as f:
        json.dump({'head_sha': H, 'jobs': []}, f)
    code, res, t = a.run(exec_args(a, extra=['--evidence', ev]))
    a.record('S11-3', any(i['class'] == 'delegated-evidence-invalid' and i['subject'].startswith('ci')
                          for i in res.get('items', [])), 'FAIL delegated-evidence-invalid (another head_sha)', '')
    ev = tempfile.mkdtemp(dir=a.out_root)
    with open(os.path.join(ev, 'proof-census.json'), 'w') as f:
        json.dump({'entries': [{'id': 'MAIN:L-3', 'fingerprint': '0000'}]}, f)
    code, res, t = a.run(exec_args(a, extra=['--evidence', ev]))
    a.record('S11-4', any(i['class'] == 'delegated-evidence-invalid' and 'coverage-ledger' in i['subject']
                          for i in res.get('items', [])), 'FAIL (one STALE value differs from the census)', '')
    # sec. 11 row 2 countercontrols at E
    f = 'book/ch18-beyond.md'
    el = a.lines(E, f)
    x = a.repo.derive(E, {f: ('\n'.join(el) + '\nA new line on total finiteness.\n').encode()}, parents=[E])
    code, res, t = a.run(['coverage', '--commit', x])
    nl = len(a.lines(E, f)) + 1  # the appended line
    on = [i['class'] for i in items_on(res, f, nl)]
    a.record('S11-2a', on == ['unclassified'], 'unclassified new site gives REVIEW_REQUIRED',
             {'items_on_new_line': on, 'run_outcome': res.get('outcome'),
              'note': 'the mutant of E is not E, so the deny profiles run on it (sec. 2.3) and its retired forms '
                      'give deny-match FAILs as well'})
    p3 = [s for s in json.loads(a.base.read(H, 'verification/audits/foundations/a1exit-ledger-20261120/sitemap.json'))['sites']
          if s['owner'] == 'Q3 propagation'][0]
    el = a.lines(E, p3['file'])
    del el[p3['line'] - 1]
    x = a.repo.derive(E, {p3['file']: ('\n'.join(el) + '\n').encode()}, parents=[E])
    code, res, t = a.run(['coverage', '--commit', x])
    sid = '%s:%d@%s' % (p3['file'], p3['line'], E[:8])
    a.record('S11-2b', [i['class'] for i in res.get('items', []) if i['subject'] == sid] == ['missing'],
             'dropped Phase-3 site gives FAIL missing', [i['class'] for i in res.get('items', []) if i['subject'] == sid])


def tree_controls(a, tool_files):
    from ledger_coverage.engine import execution as ex
    code, res, t = a.run(exec_args(a, extra=['--main', WM]))
    side = res.get('side_changes', [])
    a.record('RT-X', code == 10 and [(s['path'], s['class']) for s in side] == [(WF, 'trial-workflow')] and
             not any(i['obligation'] == 'RET' for i in res.get('items', [])),
             'one side change (the trial workflow) classified; no RET item from it',
             {'exit': code, 'side_changes': side, 'finding_counts': res.get('finding_counts')})
    L = ex.compose_landing(a.repo, H, WM, T, a.led, a.repo)
    code, res, t = a.run(exec_args(a, extra=['--main', WM, '--landing', L]))
    wf_equal = a.repo.blob_id(L, WF) == a.repo.blob_id(WM, WF)
    Lb = a.repo.derive(L, {WF: a.repo.read(H, WF)}, parents=[WM, T])
    code_b, res_b, t = a.run(exec_args(a, extra=['--main', WM, '--landing', Lb]))
    a.record('RT-L', code == 10 and not any(i['obligation'] == 'MAIN' for i in res.get('items', [])) and wf_equal and
             'landing-drops-main-change' in classes(res_b),
             "composition PASS; the workflow at L equals W's blob; the mutant with H's copy FAILs "
             'landing-drops-main-change', {'exit': code, 'mutant': classes(res_b)})
    main = a.main
    out = {}
    for label, M in (('main', main),):
        if M is None:
            continue
        code, res, t = a.run(exec_args(a, extra=['--main', M]))
        out[label] = {'M': M, 'exit': code, 'side_changes': res.get('side_changes'),
                      'main_items': sorted((i['class'], i['subject']) for i in res.get('items', [])
                                           if i['obligation'] == 'MAIN')}
        Mp = a.repo.derive(M, tool_files, parents=[M], subject='predicted main with the tool landing')
        from ledger_coverage.engine import reconcile as rcm
        loaded = cfgmod_loaded(a)
        ctx_ = pl.RunContext(a.repo, loaded.config, loaded.profiles, [], {}, None)
        led_ = __import__('ledger_coverage.adapters.a1exit_exact_edit', fromlist=['x']).load(
            a.base.read(P, PL + 'ledger.json'), {'edits': a.base.read(P, PL + 'edits.json')})
        mb = a.repo.read(M, 'AGENTS.md')
        hdr = mb.find('## \u00a7A.49'.encode())
        rdoc = rcm.draft(a.repo, ctx_, H, Mp, T, led_, 'AGENTS.md', [(hdr, len(mb))] if hdr > 0 else [])
        rc_ = a.repo.derive(a.crev, {a.ad + 'records/control-recon.json': (json.dumps(rdoc) + '\n').encode()},
                            parents=a.repo.parents(a.crev), subject='control reconciliation record')
        recon_arg = ['--classify', '%s:%srecords/control-recon.json' % (rc_, a.ad)]
        code, res, t = a.run(exec_args(a, extra=['--main', Mp]))
        out['predicted_without_reconciliation'] = {
            'exit': code, 'main_items': sorted((i['class'], i['subject']) for i in res.get('items', [])
                                               if i['obligation'] == 'MAIN')}
        code, res, t = a.run(exec_args(a, extra=['--main', Mp] + recon_arg))
        sc = {e['path']: e for e in res.get('side_changes') or []}
        out['landed_paths'] = len(tool_files)
        out['landed_unbound'] = sorted(p for p in tool_files if (sc.get(p) or {}).get('class') in (None, 'base-drift'))
        out['landed_classes'] = dict(collections.Counter(str((sc.get(p) or {}).get('class')) for p in tool_files))
        out['agents_md'] = {k: (sc.get('AGENTS.md') or {}).get(k) for k in ('class', 'reconciled')}
        out['predicted'] = {'exit': code, 'side_changes': res.get('side_changes'),
                            'main_items': sorted((i['class'], i['subject']) for i in res.get('items', [])
                                                 if i['obligation'] == 'MAIN'), 'admission': res.get('config', {}).get('admission')}
        L2 = ex.compose_landing(a.repo, H, Mp, T, a.led, a.repo)
        code, res, t = a.run(exec_args(a, extra=['--main', Mp, '--landing', L2] + recon_arg))
        out['predicted_with_landing'] = {'exit': code, 'main_items': sorted(
            (i['class'], i['subject']) for i in res.get('items', []) if i['obligation'] == 'MAIN')}
        code, res, t = a.run(exec_args(a, extra=['--main', Mp]), harness=False)
        out['predicted_chain_admission'] = {'exit': code, 'stop': res.get('stop', {}).get('class')}
    drift = out.get('predicted', {}).get('main_items', [])
    raw = out.get('predicted_without_reconciliation', {}).get('main_items', [])
    a.record('RT-L2', not any(c == 'base-drift' for c, _ in drift) and
             not any(c == 'side-change-unclassified' for c, _ in drift) and
             out.get('landed_paths', 0) > 0 and not out.get('landed_unbound') and
             ('base-drift', 'AGENTS.md') in raw and out.get('agents_md') == {'class': 'base-drift', 'reconciled': True},
             'every side change classified and no base-drift (sec. 13.4 sequencing safeguard)', out,
             predicate='at the predicted main (main plus the tool landing only; the configuration is read from the '
                       'stand-in for F): every landed path is a side change classified by an exact blob (tool-landing '
                       'or the configuration\'s pin of the class record); no base-drift and no '
                       'side-change-unclassified among the MAIN items with the drafted reconciliation record; and the '
                       'real AGENTS.md drift is shown: base-drift without that record, base-drift reconciled with it',
             finding='Predicted main = %s (--main) plus this tool\'s landing files (the configuration not among '
                     'them, design sec. 16.2), with the drafted reconciliation record for AGENTS.md and pinned classes '
                     'for the trial workflow and .claude/settings.json.' % a.main[:8])
    # R6.GATE.16: with no drift at the predicted main RT-L2 holds without a record; with drift it is NOT RUN until
    # a reviewed reconciliation record exists (a run on the drafted record does not establish the safeguard). This
    # runner has no input for a reviewed record, so a drifted RT-L2 is recorded NOT RUN, its runs on the drafted
    # record kept as diagnostics in the evidence.
    if any(c == 'base-drift' for c, _ in raw):
        a.results['RT-L2'].update(passed=False, status='NOT RUN',
                                  drafted_record_value=a.results['RT-L2']['passed'],
                                  not_run_reason='no reviewed reconciliation record exists; the drafted AGENTS.md '
                                                 'record is unreviewed (R6.GATE.16)')
    if main is not None:
        rt_o9(a, Mp, recon_arg)


def rt_o9(a, Mp, recon_arg):
    """RT-O9 (design amendment r4, A.9): the predicted main plus the plan's record directory as it stands at a
    stand-in F that holds that directory (P's plan files and the staged configuration). The expected set is computed
    from the stand-in F's tree, independently of the run, and compared exactly with the run's record-directory
    entries."""
    from ledger_coverage import record_authority
    from ledger_coverage.engine import reconcile as rcm
    d = PL.rstrip('/')
    pfiles = {p: a.base.read(P, p) for p in a.base.paths(P) if rcm.inside(d, p)}
    pfiles[a.cpath] = a.repo.read(a.crev, a.cpath)
    F9 = a.repo.derive(a.crev, pfiles, parents=a.repo.parents(a.crev),
                       subject='stand-in for F holding the plan record directory')
    expected = {p: [mode, oid, sha(a.repo.read(F9, p))] for p, (mode, oid) in a.repo.entries(F9).items()
                if rcm.inside(d, p)}
    M9 = a.repo.derive(Mp, {p: a.repo.read(F9, p) for p in expected}, parents=[Mp],
                       subject='predicted main with the tool landing and the plan record directory')
    code, res, t = a.run(exec_args(a, extra=['--main', M9, '--freeze', F9] + recon_arg))
    got = {}
    for e in res.get('side_changes') or []:
        if e.get('class') == rcm.record_directory_class:
            r9 = e.get('record_directory') or {}
            got[e['path']] = [r9.get('mode'), r9.get('m'), r9.get('m_sha256')]
    unc = sorted(i['subject'] for i in res.get('items', []) if i['class'] == 'side-change-unclassified')
    rdsum = res.get('record_directory') or {}
    out = {'exit': code, 'stop': res.get('stop'), 'directory': d,
           'authorized': d in record_authority.authorized_record_directories, 'expected_paths': len(expected),
           'record_directory': rdsum, 'missing': sorted(set(expected) - set(got)),
           'extra': sorted(set(got) - set(expected)),
           'differing': sorted(p for p in set(expected) & set(got) if expected[p] != got[p]),
           'side_change_unclassified': unc,
           'base_drift': sorted(i['subject'] for i in res.get('items', []) if i['class'] == 'base-drift'),
           'rt_l2': (a.results.get('RT-L2') or {}).get('status')}
    # RT-O9 runs its own record-directory checks; its dependent clause (no base-drift, RT-L2 PASS) is RT-O9-L2,
    # NOT RUN while RT-L2 is (R6.GATE.15)
    a.record('RT-O9', not res.get('stop') and out['authorized'] and len(expected) > 0 and got == expected and
             rdsum.get('state') == 'active' and rdsum.get('unequal') == {} and not unc,
             'the plan record directory at the predicted main classified record-directory exactly as the stand-in F '
             'holds it; no side-change-unclassified; RT-L2 still PASS', out,
             predicate='the expected set (every entry inside the directory at the stand-in F, with its mode, blob id '
                       'and sha256, computed from that tree) equals the run\'s record-directory entries exactly (none '
                       'missing, none extra, modes and hashes equal); A.5 finds no unequal path; no '
                       'side-change-unclassified among the items',
             finding='Predicted main = %s plus the tool landing plus the plan record directory of a stand-in F (P\'s '
                     'plan files and the staged configuration), with the drafted AGENTS.md reconciliation record.'
                     % a.main[:8])
    dep = (a.results.get('RT-L2') or {}).get('status')
    a.results['RT-O9-L2'] = {'id': 'RT-O9-L2', 'passed': dep == 'PASS' and not out['base_drift'],
                             'status': 'NOT RUN' if dep == 'NOT RUN' else
                             ('PASS' if dep == 'PASS' and not out['base_drift'] else 'FAIL'),
                             'expected': 'no base-drift at the predicted main with the record directory, and RT-L2 PASS',
                             'predicate': 'RT-L2 PASS and no base-drift among the items of the RT-O9 run',
                             'actual': {'rt_l2': dep, 'base_drift': out['base_drift'],
                                        'note': 'NOT RUN while RT-L2 is NOT RUN (R6.GATE.15)'}}


# ---- K1: the reference graph of the landing and the freeze ---------------------------------------------------

def git_blob(b):
    return hashlib.sha1(b'blob %d\x00' % len(b) + b).hexdigest()


def reference_graph(nodes, required):
    """Edges path -> path: A's bytes name B's current blob (its sha256 or git blob id), plus the edges a rule
    requires (`required`: {path: [paths]}), which must hold whatever the bytes are. Returns (edges, cycle)."""
    ids = {}
    for q, b in nodes.items():
        ids[q] = (sha(b), git_blob(b))
    edges = {q: set() for q in nodes}
    for q, b in nodes.items():
        text = b.decode('utf-8', 'replace')
        for r, (h, g) in ids.items():
            if r != q and (h in text or g in text):
                edges[q].add(r)
    for q, rs in required.items():
        edges.setdefault(q, set()).update(r for r in rs if r != q)
    state, stack = {}, []

    def visit(q):
        state[q] = 1
        stack.append(q)
        for r in sorted(edges.get(q, ())):
            if state.get(r) == 1:
                return stack[stack.index(r):] + [r]
            if r not in state:
                got = visit(r)
                if got:
                    return got
        stack.pop()
        state[q] = 2
        return None
    for q in sorted(edges):
        if q not in state:
            got = visit(q)
            if got:
                return edges, got
    return edges, None


def k1_graph(a, tool_files):
    """The full reference graph: configuration -> records, rules and reviews; F's pin table -> configuration and its
    review; class record -> every other landed path. The reviews do not exist yet; the graph places them where the
    design puts records frozen with the plan (sec. 6.3, 16.2), as in-memory fixtures only. The actual layout must be
    acyclic; two countercontrols place a record in the landing that names a blob the class record must pin, and must
    give a cycle."""
    cfg_b = a.repo.read(a.crev, a.cpath)
    cfg = json.loads(cfg_b)
    rec_dir = a.cpath.rsplit('/', 1)[0] + '/'
    cls_path = cfg['roles']['side_change_classes']['path']

    def jb(o):
        return (json.dumps(o, indent=1, sort_keys=True) + '\n').encode()

    def review(path, b, reviewer):
        return jb({'schema': 'oi-review-record/1', 'reviewer': reviewer, 'reviewed': {'path': path,
                   'blob_sha256': sha(b)}, 'method': 'graph fixture', 'verdicts': [{'item': '*', 'verdict': 'accept'}]})

    def layout(landed, cls_review_dir):
        """nodes and required edges for one placement. cls_review_dir: where the class record's review lies."""
        nodes = dict(landed)
        cls_b = nodes[cls_path]
        rk_p = cls_review_dir + 'reviews/class-record.review.json'
        rk = review(cls_path, cls_b, 'reviewer-fixture')
        nodes[rk_p] = rk
        c2 = dict(cfg, records=list(cfg['records']) + [{'kind': 'review', 'path': rk_p, 'blob_sha256': sha(rk)}])
        c2b = jb(c2)
        if a.cpath in landed:
            # the configuration in the landing: its bytes as landed are the ones the class record pins
            c2b = landed[a.cpath]
        nodes[a.cpath] = c2b
        rc_p = rec_dir + 'reviews/config.review.json'
        rc = review(a.cpath, c2b, 'reviewer-fixture')
        nodes[rc_p] = rc
        pt_p = rec_dir + 'PREREG.md'
        nodes[pt_p] = ('### 1.1 Record pins\n\n' + ''.join('| `%s` | `%s` |\n' % (q[len(rec_dir):], sha(nodes[q]))
                                                           for q in (a.cpath, rc_p))).encode()
        required = {cls_path: [q for q in landed if q != cls_path] + ([rk_p] if rk_p in landed else []),
                    pt_p: [a.cpath, rc_p], a.cpath: [cls_path, rk_p], rc_p: [a.cpath], rk_p: [cls_path]}
        return nodes, required
    out = {}
    nodes, req = layout(dict(tool_files), rec_dir)
    edges, cyc = reference_graph(nodes, req)
    out['actual'] = {'nodes': len(nodes), 'edges': sum(len(v) for v in edges.values()), 'cycle': cyc,
                     'config_in_landing': a.cpath in tool_files,
                     'config_edges': sorted(edges[a.cpath])[:20], 'pin_table_edges': sorted(edges[rec_dir + 'PREREG.md'])}
    # countercontrol 1: the configuration landed with the tool (the class record must pin it)
    landed1 = dict(tool_files)
    landed1[a.cpath] = cfg_b
    n1, r1 = layout(landed1, rec_dir)
    out['config_landed'] = {'cycle': reference_graph(n1, r1)[1]}
    # countercontrol 2: the class record's review landed with the tool
    tool_ad = a.ad
    n2, r2 = layout(dict(tool_files), tool_ad)
    landed2 = {q: n2[q] for q in list(tool_files) + [tool_ad + 'reviews/class-record.review.json']}
    n2, r2 = layout(landed2, tool_ad)
    out['class_review_landed'] = {'cycle': reference_graph(n2, r2)[1]}
    a.record('K1-GRAPH', cyc is None and out['actual']['config_in_landing'] is False and
             bool(out['config_landed']['cycle']) and bool(out['class_review_landed']['cycle']),
             'the reference graph of the tool landing and the freeze has no cycle, including through review records; '
             'placing the configuration, or the class record\'s review, in the landing gives a cycle', out,
             predicate='no cycle in the actual layout (configuration not landed; reviews in the plan record '
                       'directory); a cycle in each countercontrol layout')


def chain_refusal(a):
    code, res, t = a.run(['coverage', '--commit', E], harness=False)
    code2, res2, t2 = a.run(['coverage', '--commit', E, '--freeze', a.crev], harness=False)
    a.record('CHAIN-REFUSAL', code == 65 and res.get('stop', {}).get('class') == 'CONFIG_UNREVIEWED' and
             code2 == 65 and res2.get('stop', {}).get('class') == 'CONFIG_UNREVIEWED',
             'the unreviewed draft configuration is refused under the review chain: ERROR CONFIG_UNREVIEWED, without '
             '--freeze and with the stand-in for F (no pin table lists the draft, and it has no review)',
             {'without_freeze': {'exit': code, 'stop': res.get('stop')},
              'with_stand_in_F': {'exit': code2, 'stop': res2.get('stop')}})


def z9g(a):
    cfg = json.loads(a.repo.read(a.crev, a.cpath))
    values = purity.config_values(a.repo.read, a.crev, cfg)
    from ledger_coverage.adapters import synthetic_fixture as sf
    syn = sf.Syn()
    pd = sf.patch_doc(syn.H, [])
    c, p, s, files = syn.build({'patch_sha': sha(pd), 'files': {'syn/patch.json': pd}})
    values |= purity.string_values(json.loads(files[p]))
    loaded = cfgmod_loaded(a)
    profs = [pp for pp in loaded.profiles.values() if pp.kind in ('review', 'deny')]
    found = purity.lint_engine(values, profs)
    a.record('Z9g', not found, 'the real engine tree: lint PASS', found[:40])
    # Z9h: 'guard-pin' planted in an engine module, with the adapter companions in the value set
    src = open(os.path.join(tools, 'ledger_coverage', 'engine', 'outcome.py')).read() + "\nPLANTED = 'guard-pin'\n"
    planted = purity.lint_sources({'engine/outcome.py': src}, values, [])
    dotted = purity.lint_sources({'engine/outcome.py': "X = '%s.json'\n" % hashlib.sha1(b'z9').hexdigest()},
                                 set(), [])
    a.record('Z9h', any('guard-pin' in f for f in planted) and 'guard-pin' in values and bool(dotted),
             "'guard-pin' planted in an engine module, with the adapter companions in the value set: lint FAIL",
             {'planted': planted[:3], 'in_value_set': 'guard-pin' in values, 'dotted_40_hex': dotted[:2]},
             predicate="a finding names the planted literal, which occurs in the companions' values; a planted "
                       "40-hex file name is a finding too (the allowlist exempts only its listed values)")
    return values


def sweeps(a):
    """SW1 (697 sites at E) and SW2 (584 sites at H): one token deleted, exactly one FAIL naming that site."""
    from ledger_coverage.engine import context as ctxmod
    loaded = cfgmod_loaded(a)
    cfg = loaded.config
    sm = cli.load_adapter_input(a.repo, loaded, 'sitemap')
    ctx = pl.RunContext(a.repo, cfg, loaded.profiles, [], {}, ctxmod.Indicators(cfg['indicators']), sitemap=sm)
    sites = pl.build_sites(ctx)
    chain = gitobj.first_parent_chain(a.repo, E, H)
    par = {}
    prev = E
    for c in chain:
        par[c] = prev
        prev = c
    merges = {m['commit'] for m in cfg['hp_obligations'][0]['merges']}
    hp_seg = {'from': E, 'to': H, 'kind': 'hp', 'chain': chain, 'parent_of': par, 'merges': merges, 'obligation': 'HP'}
    base_cv = pl.Coverage(ctx, H, [dict(hp_seg)], None, {}, []).run()
    hp_sites = {k for k, so in base_cv.site_out.items() if so.get('hp_steps')}
    baseline = {}
    base_tuples = {}
    for i in base_cv.items:
        if i['decision'] == 'FAIL':
            baseline.setdefault(i['subject'], set()).add(i['class'])
        base_tuples.setdefault(i['subject'], set()).add((i['obligation'], i['class'], i['segment'], i['fingerprint']))
    res = {}
    for name, base_commit, todo in (('SW1', E, sites), ('SW2', H, [s for s in sites if s['site_id'] not in hp_sites])):
        bad = []
        bad_delta = []
        t0 = time.time()
        for s in todo:
            f = s['file']
            lines = list(ctx.ft(base_commit, f).lines)
            if base_commit == E:
                idx = s['pin_lineno'] - 1
            else:
                idx = [st.start for st in base_cv.states if st.site['site_id'] == s['site_id']][0]
            toks = lines[idx].split(' ')
            nz = [k for k, x in enumerate(toks) if x]
            k = nz[-1]
            lines[idx] = ' '.join(toks[:k] + toks[k + 1:])
            x = a.repo.derive(base_commit, {f: ('\n'.join(lines) + '\n').encode()}, parents=[base_commit])
            segs = [{'from': E, 'to': x, 'kind': 'unledgered'}] if base_commit == E else \
                [dict(hp_seg), {'from': H, 'to': x, 'kind': 'unledgered'}]
            cv = pl.Coverage(ctx, x, segs, None, {}, []).run()
            mine = [i for i in cv.items if i['subject'] == s['site_id'] and i['decision'] == 'FAIL']
            if base_commit == H:
                # D2: items compared by (obligation, class, segment, fingerprint); exactly one new FAIL, RET
                # unauthorized-change in segment H..X; the items naming the site at the unmutated H unchanged
                allt = {(i['obligation'], i['class'], i['segment'], i['fingerprint']) for i in cv.items
                        if i['subject'] == s['site_id']}
                prev_t = base_tuples.get(s['site_id'], set())
                new_t = [t_ for t_ in allt - prev_t if t_[1] == 'unauthorized-change' or
                         any(i['decision'] == 'FAIL' and (i['obligation'], i['class'], i['segment'], i['fingerprint'])
                             == t_ for i in cv.items)]
                last = cv.segments[-1]['name']
                if not (len(new_t) == 1 and new_t[0][:3] == ('RET', 'unauthorized-change', last) and prev_t <= allt):
                    bad.append((s['site_id'], sorted(map(list, allt - prev_t))[:3]))
            elif len(mine) != 1:
                bad.append((s['site_id'], [i['class'] for i in mine]))
            pre = baseline.get(s['site_id'], set()) if base_commit == H else set()
            new = [i for i in mine if i['class'] not in pre]
            if len(new) != 1:
                bad_delta.append((s['site_id'], [i['class'] for i in new]))
            ctx._ft = {k_: v for k_, v in ctx._ft.items() if k_[0] in (E, H) or k_[0] in par}
        res[name] = {'sites': len(todo), 'not_exactly_one_fail': bad,
                     'not_exactly_one_new_fail_against_the_unmutated_tree': bad_delta,
                     'seconds': round(time.time() - t0, 1)}
        a.record(name, not bad and len(todo) == (697 if name == 'SW1' else 584),
                 'exactly one FAIL naming each site (697 at E)' if name == 'SW1' else
                 'for each of the 584 sites at H, exactly one new FAIL naming it (RET, unauthorized-change, segment '
                 'H..X), the items naming it at the unmutated H unchanged; items compared by (obligation, class, '
                 'segment, fingerprint)', res[name],
                 predicate='SW1: exactly one FAIL item names each site' if name == 'SW1' else
                 'per site: allt - prev_t holds exactly one new FAIL tuple (RET, unauthorized-change, last segment) and '
                 'prev_t is a subset of allt; 584 sites')


def engine_identity_y8(a, syn_engine):
    code, res, t = a.run(['coverage', '--commit', E])
    a.record('Y8', res.get('engine', {}).get('blob_sha256') == syn_engine,
             'identical engine hash recorded for the A1 and the synthetic configuration',
             {'a1': res.get('engine', {}).get('blob_sha256'), 'synthetic': syn_engine})


PREDICATES = {
    'RT-DR': "terms --profile DR-1,DR-3,DR-4,DR-5: at H 86 distinct deny lines, per rule DR-1 61 / DR-4 28 / DR-5 1, "
             "DR-1 alternatives a 6 / b 2 / c 55, and the six named lines hit at line level by their rule; at E 95 "
             "lines; at T1' exit 0 with no line or sentence match",
    'RT-I7': "terms --profile item7-literal: exit 20 at both; (items, A1 report lines) == (7, 4) at T1' and (14, 179) "
             "at H",
    'RT-I7A': "terms --check item7 --final without allow rules: at H exit 20, 86 deny lines, 123 final-unclassified, "
              "209 FAIL lines (93 / 216 with sentences), 95 retired lines, none of them only REVIEW; at T1' exit 20, "
              "0 deny lines, 12 final-unclassified",
    'V3-countercontrol': "terms --check item7 at H without --final and without allow rules: exit 20 and every one of "
                         "the 95 retired lines is an unclassified REVIEW item",
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', required=True)
    ap.add_argument('--config', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--only', default=None)
    ap.add_argument('--skip-sweeps', action='store_true')
    ap.add_argument('--overlay-from-disk', action='store_true',
                    help='test the working files: overlay tools/ledger_coverage* and the audit directory on HEAD')
    ap.add_argument('--syn-engine', default=None)
    ap.add_argument('--staged-config', default=None,
                    help='the staged configuration file; --config REV:PATH names its path in the plan directory')
    ap.add_argument('--main', default=None,
                    help='required: the main commit the sequencing safeguard (RT-L2) and the drift classes use')
    args = ap.parse_args()
    if not args.main:
        ap.error('--main is required: the main commit the sequencing safeguard is measured against')
    try:
        main_c = gitobj.GitRepo(args.repo).resolve(rev_parse(args.repo, args.main))
    except Exception as exc:
        ap.error('--main %s does not resolve: %s' % (args.main, exc))
    os.makedirs(args.out, exist_ok=True)
    out_root = tempfile.mkdtemp(prefix='a1-controls-', dir=args.out)
    cref = args.config
    tool_files = {}
    rev, cpath = cref.split(':', 1)
    probe = A1(args.repo, cref, out_root, args.staged_config, main_c)
    ad = probe.ad.rstrip('/')
    if args.overlay_from_disk:
        for root in ('tools/ledger_coverage', ad):
            for dp, dn, fn in os.walk(os.path.join(args.repo, root)):
                dn[:] = [d for d in dn if d != '__pycache__']
                for f in fn:
                    p = os.path.relpath(os.path.join(dp, f), args.repo)
                    tool_files[p] = open(os.path.join(dp, f), 'rb').read()
        tool_files['tools/ledger_coverage.py'] = open(os.path.join(args.repo, 'tools/ledger_coverage.py'), 'rb').read()
        tool_files[WORKFLOW_PATH] = open(os.path.join(args.repo, WORKFLOW_PATH), 'rb').read()
        a = A1(args.repo, '%s:%s' % (rev_parse(args.repo, rev), cpath), out_root, args.staged_config, main_c)
        wt = a.repo.derive(a.crev, tool_files, subject='working files')
        a.crev = wt
        a.csha = sha(a.repo.read(wt, cpath))
    else:
        a = probe
        head = a.tool_rev
        for p, b in a.base.paths(head).items():
            if p.startswith(('tools/ledger_coverage/', ad + '/')) or p in ('tools/ledger_coverage.py', WORKFLOW_PATH):
                tool_files[p] = a.base.read_blob(b)
    groups = [('chain', chain_refusal), ('record', rt_record), ('coverage', rt_coverage), ('terms', rt_terms),
              ('v', v_controls), ('rules', rule_lint_controls), ('exec', ex_controls),
              ('trees', lambda x: tree_controls(x, tool_files)), ('k1', lambda x: k1_graph(x, tool_files)),
              ('z9g', z9g)]
    if args.syn_engine:
        groups.append(('y8', lambda x: engine_identity_y8(x, args.syn_engine)))
    if not args.skip_sweeps:
        groups.append(('sweeps', sweeps))
    only = set(args.only.split(',')) if args.only else None
    timing = {}
    for name, fn in groups:
        if only and name not in only:
            continue
        t = time.time()
        try:
            fn(a)
        except Exception as exc:
            import traceback
            a.results['%s-group-error' % name] = {'passed': False, 'expected': 'no exception',
                                                  'actual': traceback.format_exc()[-3000:]}
        timing[name] = round(time.time() - t, 1)
    # sec. 10.4: every control carries a status and its predicate
    for cid, v in a.results.items():
        v.setdefault('status', 'PASS' if v.get('passed') else 'FAIL')
        if not v.get('predicate'):
            v['predicate'] = PREDICATES.get(cid, 'the boolean computed for this id in a1_controls.py')
    summary = {'controls': a.results, 'timing_seconds': timing,
               'passed': sum(1 for v in a.results.values() if v.get('passed')),
               'failed': sorted(k for k, v in a.results.items() if not v.get('passed'))}
    # R6.GATE.5 and R6.GATE.7: one record per control with its retained evidence, read by the gate
    a.rec.out_dir = args.out
    for cid in sorted(a.results):
        v = a.results[cid]
        a.rec.pending = a.runs_of.get(cid, [])
        st = v['status'] if v['status'] in ('PASS', 'FAIL', 'NOT RUN') else 'FAIL'
        a.rec.record(cid, st, v.get('actual'), v['predicate'])
    a.rec.write()
    with open(os.path.join(args.out, 'a1-controls.json'), 'w') as f:
        json.dump(summary, f, indent=1, sort_keys=True, default=str)
    print(json.dumps({'passed': summary['passed'], 'failed': summary['failed'], 'timing': timing}, indent=1))
    return 0 if not summary['failed'] else 1


if __name__ == '__main__':
    sys.exit(main())
