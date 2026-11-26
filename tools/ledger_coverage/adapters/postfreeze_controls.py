"""Controls of the post-freeze route (design r6 as amended by amendment 1): POSTF-1 to POSTF-5 and RTL2-BIND, on the
synthetic configuration and an in-memory host (R6.RECON.2 (a)-(g), R6.RECON.21, OBL-28 C-29).

Every scenario is built from git objects in memory: the plan commit F, a main commit M that changes the ledgered file
after F (outside the patched line), a candidate X, and a reconciliation record drafted by the engine from those
objects (engine/reconcile.py draft) with its review record, both added by a record commit REV whose single parent is
M. Each case is one op C run; the runs are named as the expectation cases of their row. Called by
conformance_controls.py with its `check`.
"""
import copy
import io
import json

from ledger_coverage.engine import cli, config as cfgmod, pipeline as pl, reconcile as rcmod, records as rec, util
from ledger_coverage.adapters import host_fixture as hf, synthetic_fixture as sf

RD = 'verification/audits/syn-recon/'
RD2 = 'verification/audits/syn-recon-b/'
EDITS = [('# synthetic', ['# synthetic', '', 'Preface line one.'])]


def jb(o):
    return sf.jb(o)


def sha(b):
    return util.sha256(b)


class World:
    """One synthetic post-freeze world. pre_change: the ledgered file's change on M is made before F (F descends from
    it), so no commit on M after F changes it (POSTF-2)."""

    def __init__(self, r, pre_change=False, side=False, config_records=None):
        self.r = r
        syn = self.syn = sf.Syn()
        repo = self.repo = syn.repo
        pd = sf.patch_doc(syn.H, EDITS)
        base = {'patch_sha': sha(pd), 'files': {'syn/patch.json': pd}}
        h_doc = repo.read(syn.H, sf.DOC)
        changed = {sf.DOC: h_doc.replace(b'Closing words of the file.', b'Closing words, changed on main.')}
        if side:
            changed['notes/side.txt'] = b'a side change on main\n'
        x_doc = sf.apply_text(h_doc.decode(), EDITS).encode()
        # the delegated class artifact-hash/1 of the synthetic configuration: the digest of the candidate's document
        self.X = repo.derive(syn.H, {sf.DOC: x_doc, 'out/digest.txt': (sha(x_doc) + '\n').encode()},
                             parents=[syn.H], subject='X')
        if config_records:
            base = dict(base, extra={'records': None})
        c, p, s, files = syn.build(base)
        self.p = p
        if pre_change:
            self.M = repo.derive(syn.H, changed, parents=[syn.H], subject='main change before F')
            self.c = repo.derive(self.M, {k: v for k, v in files.items()}, parents=[self.M], subject='plan at M')
        else:
            self.M = repo.derive(syn.H, changed, parents=[syn.H], subject='main change after F')
            self.c = c
        self.files = files
        loaded = cfgmod.load(repo, c, p, None, 'execution', 'harness')
        self.ctx = pl.RunContext(repo, loaded.config, loaded.profiles, [], {}, None)
        self.led = cli.load_adapter_input(repo, loaded, 'ledger', '%s:syn/patch.json' % c)

    def record(self, **upd):
        doc = rcmod.draft(self.repo, self.ctx, self.syn.H, self.M, self.X, self.led, sf.DOC)
        doc.update(record_id='syn-recon', author=sf.WRITER, supersedes=None, M=self.M, X=self.X)
        doc.update(upd)
        return doc

    def review(self, path, data, reviewer=sf.REVIEWER):
        doc = json.loads(data)
        return jb({'schema': rec.review_schema, 'reviewer': reviewer, 'reviewed': {'path': path,
                                                                                   'blob_sha256': sha(data)},
                   'method': 'read every object the record names',
                   'verdicts': [{'item': i, 'verdict': 'accept'} for i in rec.item_ids(doc)]})

    def rev(self, files, parent=None, parents=None):
        parent = parent or self.M
        return self.repo.derive(parent, files, parents=parents or [parent], subject='record commit')

    def standard(self, doc=None, path=RD + 'rec.json', reviewer=sf.REVIEWER, review_path=None, extra=None,
                 parent=None, parents=None):
        """REV with the record (and, unless review_path is False, its review in the record's directory)."""
        data = jb(doc if doc is not None else self.record())
        files = {path: data}
        if review_path is not False:
            files[review_path or path[:-5] + '.review.json'] = self.review(path, data, reviewer)
        files.update(extra or {})
        return self.rev(files, parent, parents), path, data

    def run(self, classify=(), harness=False, main=None):
        tail = ['--scientific-base', self.syn.H, '--candidate', self.X, '--ledger', None, '--delegation', None,
                '--main', main or self.M]
        for c in classify:
            tail += ['--classify', c]
        if harness:
            argv = list(tail)
            argv[argv.index(None)] = '%s:syn/patch.json' % self.c
            argv[argv.index(None)] = '%s:syn/delegation.json' % self.c
            return self.r.cli(self.repo, ['execution'] + argv, self.c, self.p, None, harness=True)
        w = hf.World(self.repo, self.syn.H)
        F = hf.freeze(self.repo, self.c, self.p)
        argv = list(tail)
        argv[argv.index(None)] = '%s:syn/patch.json' % F
        argv[argv.index(None)] = '%s:syn/delegation.json' % F
        full = ['execution', '--config', '%s:%s' % (F, self.p), '--out', self.r.out()] + w.args(F) + argv
        return cli.run(full, repo=self.repo, stderr=io.StringIO(), control=w.control(w.checkout()), environ={})


def classes(res):
    return sorted({i['class'] for i in (res or {}).get('items', [])})


def invalid(res, path):
    return any(i['class'] == 'record-invalid' and i.get('subject') == path for i in (res or {}).get('items', []))


def drift(res):
    return 'base-drift' in classes(res)


def admitted(res, path):
    return any(x.get('path') == path for x in ((res or {}).get('inputs') or {}).get('classify_records') or [])


def listing_ok(res, path):
    rows = [x for x in ((res or {}).get('inputs') or {}).get('classify_records') or [] if x.get('path') == path]
    return bool(rows) and all(rows[0].get(k) for k in ('rev', 'path', 'sha256')) and \
        bool((rows[0].get('review') or {}).get('path')) and bool((rows[0].get('review') or {}).get('sha256'))


def rtl2_inputs(res, w, path, doc):
    """The rtl2 procedure's inputs, derived from the run's result: the drifted paths (side changes of class
    base-drift), each reconciliation record the run used with `reviewed` and `review_lint_passes` (no record-invalid
    item names the record or its review) and the H, M and C it names, and the run's roles (C = X)."""
    items = (res or {}).get('items') or []
    names = {i.get('subject') for i in items if i.get('class') == 'record-invalid'}
    lint_ok = path not in names and (path[:-5] + '.review.json') not in names
    used = [x for x in ((res or {}).get('inputs') or {}).get('classify_records') or [] if x.get('path') == path]
    drift = sorted(x.get('path') for x in (res or {}).get('side_changes') or [] if x.get('class') == 'base-drift')
    recs = [{'path': e.get('path'), 'reviewed': bool(used and used[0].get('review')), 'review_lint_passes': lint_ok,
             'H': (doc.get('ledger_binding') or {}).get('ledger_base'), 'M': doc.get('M'), 'C': doc.get('X')}
            for e in doc.get('paths') or []]
    return {'drift': drift, 'records': recs, 'roles': {'H': w.syn.H, 'M': w.M, 'C': w.X}}


def postf_controls(r, check):
    out = {}
    # POSTF-1 (both directions)
    w = World(r)
    REV, path, data = w.standard()
    code, res = w.run(['%s:%s' % (REV, path)])
    pos = {'exit': code, 'classes': classes(res), 'admitted': admitted(res, path), 'listing': listing_ok(res, path)}
    code0, res0 = w.run()
    neg = {'exit': code0, 'classes': classes(res0)}
    att = {'equals': 'inputs.classify_records lists the record with its rev, path and sha256 and the path and sha256 '
                     'of its review record'} if pos['listing'] else {}
    check('POSTF-1', 'a reviewed reconciliation record admitted by the post-freeze route reconciles the path; without '
          'it the path is base-drift', 'with: admitted and listed, no record-invalid, no base-drift; without: FAIL '
          'base-drift', {'with': pos, 'without': neg},
          pos['admitted'] and pos['listing'] and 'record-invalid' not in pos['classes'] and
          'base-drift' not in pos['classes'] and code0 == 20 and 'base-drift' in neg['classes'],
          cases=[(POSTF1_POS, {'record': path}), (POSTF1_NEG, {})], attested={POSTF1_POS: att})
    out['restored'] = (REV, path)

    def restored():
        """The POSTF-1 input, run again, as the restored case of POSTF-2 to POSTF-5."""
        w0 = World(r)
        rv, pth, _ = w0.standard()
        w0.run(['%s:%s' % (rv, pth)])
        return pth

    # the line-patch adapter's expected_sha256, in both directions: the stated value (the sha256 of the patched
    # content) lets RC8 hold; a wrong value makes RC8 fail (coordinator's safeguard for option 1)
    doc_ok = w.record()
    entry = doc_ok['paths'][0]
    ok_ev = rcmod.evaluate(w.repo, w.ctx, w.syn.H, w.M, w.X, w.led, doc_ok, entry, [], {})
    bad_led = copy.deepcopy(w.led)
    bad_led['files'][sf.DOC]['expected_sha256'] = '0' * 64
    bad_ev = rcmod.evaluate(w.repo, w.ctx, w.syn.H, w.M, w.X, bad_led, doc_ok, entry, [], {})
    x_bytes = w.repo.read(w.X, sf.DOC)
    check('LINE-PATCH-RC8', "the line-patch ledger's expected_sha256 is the sha256 of the patched content, and RC8 "
          'reads it: the stated value holds RC8, a wrong value fails it',
          'expected_sha256 equals sha256 of the candidate document; RC8 holds with it and fails with a wrong value',
          {'stated': w.led['files'][sf.DOC]['expected_sha256'], 'candidate_sha256': sha(x_bytes),
           'rc8_stated': ok_ev['holds'].get('RC8'), 'rc8_wrong': bad_ev['holds'].get('RC8')},
          w.led['files'][sf.DOC]['expected_sha256'] == sha(x_bytes) and ok_ev['holds'].get('RC8') is True and
          bad_ev['holds'].get('RC8') is False)

    # POSTF-2
    w2 = World(r, pre_change=True)
    REV2, p2, _ = w2.standard()
    c2, r2 = w2.run(['%s:%s' % (REV2, p2)])
    rp = restored()
    check('POSTF-2', 'a record whose covered path M changed only before F: FAIL record-invalid and base-drift',
          'record-invalid for the record and base-drift', {'exit': c2, 'classes': classes(r2)},
          c2 == 20 and invalid(r2, p2) and drift(r2),
          cases=[(POSTF2_CASE, {'record': p2}), ('restored', {'record': rp})])

    # POSTF-3
    w3 = World(r, side=True)
    base_run = None
    results = {}
    hit = {'schema': 'oi-hit-classification/1', 'record_id': 'syn-hits', 'author': sf.WRITER, 'supersedes': None,
           'classifications': [{'id': 'h1', 'file': sf.DOC, 'line_sha256': sha(b'Closing words, changed on main.'),
                                'segment': None, 'profiles': ['beta-word'], 'semantic_classification': 'unrelated',
                                'author': sf.WRITER}]}
    hp = {'schema': 'oi-hp-adjudication/1', 'record_id': 'syn-hp', 'author': sf.WRITER, 'supersedes': None,
          'sites': [{'site_id': '%s:7@%s' % (sf.DOC, w3.syn.pin[:8]), 'steps': [],
                     'carried': {'row': 'r', 'code': 'c', 'owner': 'o'}, 'semantic_classification': 'restated',
                     'author': sf.WRITER}]}
    cls = {'schema': 'oi-side-change-classes/1', 'record_id': 'syn-classes-late', 'author': sf.WRITER,
           'supersedes': None, 'classes': [{'id': 'late-notes', 'reason': 'synthetic', 'pins': [
               {'path': 'notes/side.txt', 'git_blob': w3.repo.blob_id(w3.M, 'notes/side.txt'),
                'blob_sha256': sha(w3.repo.read(w3.M, 'notes/side.txt'))}]}]}
    names = []
    for case, doc in ((POSTF3_HIT, hit), (POSTF3_HP, hp), (POSTF3_CLS, cls)):
        rv, pth, _ = w3.standard(doc, path=RD + doc['record_id'] + '.json')
        code, res = w3.run(['%s:%s' % (rv, pth)])
        results[case] = {'exit': code, 'classes': classes(res), 'invalid': invalid(res, pth)}
        names.append((case, {'record': pth}))
    REVr, pr_, datar = w3.standard()
    revpath = pr_[:-5] + '.review.json'
    code, res = w3.run(['%s:%s' % (REVr, revpath)])
    results[POSTF3_REVIEW] = {'exit': code, 'classes': classes(res), 'invalid': invalid(res, revpath)}
    names.append((POSTF3_REVIEW, {'record': revpath}))
    w3.run()
    base_run = len(names)
    w3.run()
    names += [('baseline', {}), ('restored', {})]
    check('POSTF-3', 'a record of another kind written after F, or a review named as the primary record: FAIL '
          'record-invalid, never used', 'each case record-invalid (and the late class record leaves the side change '
          'unclassified)', results,
          all(v['exit'] == 20 and v['invalid'] for v in results.values()) and
          'side-change-unclassified' in results[POSTF3_CLS]['classes'],
          cases=names, baseline_of={'restored': 'baseline'})
    del base_run

    # POSTF-4
    res4, names4 = {}, []

    def case4(name, fn):
        try:
            code, res, pth = fn()
        except Exception as exc:  # a scenario that cannot be built is a failed case, not a pass
            res4[name] = {'error': '%s: %s' % (type(exc).__name__, exc)}
            names4.append(None)
            return
        res4[name] = {'exit': code, 'classes': classes(res), 'invalid': invalid(res, pth) if pth else None,
                      'stop': ((res or {}).get('stop') or {}).get('class')}
        names4.append((name, {'record': pth} if pth else {}))

    def no_review():
        w_ = World(r)
        rv, pth, _ = w_.standard(review_path=False)
        return w_.run(['%s:%s' % (rv, pth)]) + (pth,)

    def two_reviews():
        w_ = World(r)
        data = jb(w_.record())
        pth = RD + 'rec.json'
        rv = w_.rev({pth: data, RD + 'rec.review.json': w_.review(pth, data),
                     RD + 'rec.review2.json': w_.review(pth, data, reviewer='reviewer-c')})
        return w_.run(['%s:%s' % (rv, pth)]) + (pth,)

    def self_review():
        w_ = World(r)
        rv, pth, _ = w_.standard(reviewer=sf.WRITER)
        return w_.run(['%s:%s' % (rv, pth)]) + (pth,)

    def superseded_elsewhere():
        w_ = World(r)
        data = jb(w_.record())
        pth = RD + 'rec.json'
        later = w_.record(supersedes={'path': pth, 'blob_sha256': sha(data)})
        ld = jb(later)
        rv = w_.rev({pth: data, RD + 'rec.review.json': w_.review(pth, data), RD2 + 'rec.json': ld,
                     RD2 + 'rec.review.json': w_.review(RD2 + 'rec.json', ld)})
        return w_.run(['%s:%s' % (rv, pth)]) + (pth,)

    def fork():
        w_ = World(r)
        pred = jb(w_.record())
        pp = RD + 'pred.json'
        a = jb(w_.record(supersedes={'path': pp, 'blob_sha256': sha(pred)}, statement='a'))
        b = jb(w_.record(supersedes={'path': pp, 'blob_sha256': sha(pred)}, statement='b'))
        rv = w_.rev({pp: pred, RD + 'pred.review.json': w_.review(pp, pred), RD + 'rec.json': a,
                     RD + 'rec.review.json': w_.review(RD + 'rec.json', a), RD2 + 'rec.json': b,
                     RD2 + 'rec.review.json': w_.review(RD2 + 'rec.json', b)})
        return w_.run(['%s:%s' % (rv, RD + 'rec.json')]) + (RD + 'rec.json',)

    def absent_predecessor():
        w_ = World(r)
        doc = w_.record(supersedes={'path': RD + 'gone.json', 'blob_sha256': '0' * 64})
        rv, pth, _ = w_.standard(doc)
        return w_.run(['%s:%s' % (rv, pth)]) + (pth,)

    def earlier_parent():
        w_ = World(r)
        rv, pth, _ = w_.standard(parent=w_.syn.H)
        return w_.run(['%s:%s' % (rv, pth)]) + (pth,)

    def two_parents():
        w_ = World(r)
        rv, pth, _ = w_.standard(parents=[w_.M, w_.syn.H])
        return w_.run(['%s:%s' % (rv, pth)]) + (pth,)

    def outside_change():
        w_ = World(r)
        rv, pth, _ = w_.standard(extra={'notes/extra.txt': b'outside a reconciliation directory\n'})
        return w_.run(['%s:%s' % (rv, pth)]) + (pth,)

    def two_revs():
        w_ = World(r)
        rv, pth, _ = w_.standard()
        rv2, _, _ = w_.standard(extra={RD2 + 'readme.json': b'{}\n'})
        return w_.run(['%s:%s' % (rv, pth), '%s:%s' % (rv2, pth)]) + (pth,)

    def two_records():
        w_ = World(r)
        a = jb(w_.record())
        b = jb(w_.record(record_id='syn-recon-b'))
        rv = w_.rev({RD + 'rec.json': a, RD + 'rec.review.json': w_.review(RD + 'rec.json', a),
                     RD2 + 'rec.json': b, RD2 + 'rec.review.json': w_.review(RD2 + 'rec.json', b)})
        return w_.run(['%s:%s' % (rv, RD + 'rec.json')]) + (RD + 'rec.json',)

    def abbreviated():
        w_ = World(r)
        rv, pth, _ = w_.standard()
        return w_.run(['%s:%s' % (rv[:12], pth)]) + (pth,)

    def other_m():
        w_ = World(r)
        rv, pth, _ = w_.standard(w_.record(M=w_.syn.H))
        return w_.run(['%s:%s' % (rv, pth)]) + (pth,)

    def other_x():
        w_ = World(r)
        rv, pth, _ = w_.standard(w_.record(X=w_.syn.H))
        return w_.run(['%s:%s' % (rv, pth)]) + (pth,)

    for name, fn in ((POSTF4[0], no_review), (POSTF4[1], two_reviews), (POSTF4[2], self_review),
                     (POSTF4[3], superseded_elsewhere), (POSTF4[4], fork), (POSTF4[5], absent_predecessor),
                     (POSTF4[6], earlier_parent), (POSTF4[7], two_parents), (POSTF4[8], outside_change),
                     (POSTF4[9], two_revs), (POSTF4[10], two_records), (POSTF4[11], abbreviated),
                     (POSTF4[13], other_m), (POSTF4[14], other_x)):
        case4(name, fn)
    # not built here, so the gate records missing evidence for them: the commit object that does not hash to its id
    # (the in-memory store does not verify ids; it needs an on-disk object store) and the two cases over
    # configuration-referenced records (the synthetic configuration references no reconciliation record)
    rp4 = restored()
    names4.append(('restored', {'record': rp4}))
    want_drift = {POSTF4[10], POSTF4[13], POSTF4[14]}
    ok4 = all('error' not in v and v['exit'] == 20 and v['invalid'] and (k not in want_drift or 'base-drift' in
                                                                       v['classes'])
              for k, v in res4.items())
    check('POSTF-4', 'the record commit and lineage conditions of the post-freeze route: each violation FAIL '
          'record-invalid (an unverifiable object ERROR UNRESOLVABLE)', 'every built case as its expectation states; '
          'the unverifiable-object case and the two configuration-referenced cases are not built', {'cases': res4, 'built_cases_hold': ok4},
          # two listed cases are not built here, so the row cannot hold whatever the built cases give
          False, cases=names4)

    # POSTF-5
    res5, names5 = {}, []
    for name, pth, rvp in ((POSTF5[0], 'tools/ledger_coverage/syn-rec.json', None),
                           (POSTF5[1], 'syn/cfg/rec.json', None),
                           (POSTF5[2], sf.DOC, None),
                           (POSTF5[3], 'doc/rec.json', None),
                           (POSTF5[4], 'notes/rec.json', None),
                           (POSTF5[5], RD + 'rec.json', RD2 + 'rec.review.json')):
        w_ = World(r)
        try:
            rv, p_, _ = w_.standard(path=pth, review_path=rvp)
            code, res = w_.run(['%s:%s' % (rv, p_)])
            res5[name] = {'exit': code, 'invalid': invalid(res, p_), 'classes': classes(res)}
            names5.append((name, {'record': p_}))
        except Exception as exc:
            res5[name] = {'error': '%s: %s' % (type(exc).__name__, exc)}
            names5.append(None)
    rp5 = restored()
    names5.append(('restored', {'record': rp5}))
    check('POSTF-5', 'a post-freeze record outside a reconciliation directory, or its review elsewhere: FAIL '
          'record-invalid', 'every case record-invalid', res5,
          all('error' not in v and v['exit'] == 20 and v['invalid'] for v in res5.values()), cases=names5)

    # RTL2-BIND (control harness; procedure rtl2)
    resb, namesb = {}, []
    wb = World(r)

    proc_in = {}

    def bind_case(name, doc=None, reviewer=sf.REVIEWER, parent=None):
        rv, pth, data = wb.standard(doc, reviewer=reviewer, parent=parent)
        code, res = wb.run(['%s:%s' % (rv, pth)], harness=True)
        if name == BIND[0]:
            proc_in.update(rtl2_inputs(res, wb, pth, json.loads(data)))
        sc = [x for x in (res or {}).get('side_changes') or [] if x.get('path') == sf.DOC]
        state = 'reconciled' if sc and sc[0].get('reconciled') else ('none' if not sc else 'unresolved')
        resb[name] = {'exit': code, 'classes': classes(res), 'drift_state': state, 'invalid': invalid(res, pth),
                      'review_lint_passes': not invalid(res, pth) and not invalid(res, pth[:-5] + '.review.json')}
        namesb.append((name, {'record': pth}))
    bind_case(BIND[0])
    bind_case(BIND[1], wb.record(M=wb.syn.H))
    bind_case(BIND[2], wb.record(X=wb.syn.H))
    bind_case(BIND[3], wb.record(M=None, X=None))
    bind_case(BIND[4], reviewer=sf.WRITER)
    bind_case(BIND[5], parent=wb.syn.H)
    okb = resb[BIND[0]]['drift_state'] == 'reconciled' and resb[BIND[0]]['exit'] == 0 and \
        all(resb[k]['drift_state'] == 'unresolved' and resb[k]['exit'] == 20 for k in BIND[1:]) and \
        all(resb[k]['invalid'] for k in BIND[4:])
    check('RTL2-BIND', "the binding of R6.RECON.21 in the control harness: only a reviewed record naming the run's M "
          "and X, passing record lint and read from a REV tied to the run, reconciles", 'positive reconciled and PASS; '
          'every countercase unresolved', resb, okb, cases=namesb,
          attested={n: {'drift_state_in': [v['drift_state']]} for n, v in resb.items()},
          files={'rtl2-drift.json': proc_in['drift'], 'rtl2-records.json': proc_in['records'],
                 'rtl2-roles.json': proc_in['roles']},
          procedure={'name': 'rtl2-binding', 'lib': 'rtl2', 'drift': 'rtl2-drift.json',
                     'records': 'rtl2-records.json', 'roles': 'rtl2-roles.json'})
    return out


POSTF1_POS = ("a reviewed reconciliation record naming the run's M and X and its review record, in one reconciliation "
              "directory of a record commit REV whose single parent is M and which adds only those two files, named by "
              "--classify REV:PATH, covering a ledgered path changed on M by a commit that is not an ancestor of F, "
              "every condition RC1-RC13 holding (positive)")
POSTF1_NEG = 'countercase: the same run without the reconciliation record'
POSTF2_CASE = ('a reviewed reconciliation record named by --classify REV:PATH whose covered path is changed on M only by '
               'commits that are ancestors of F')
POSTF3_HIT = 'a reviewed hit-classification record written after F, named by --classify REV:PATH from a reconciliation directory'
POSTF3_HP = 'a reviewed HP adjudication written after F, named the same way'
POSTF3_CLS = ('a reviewed side-change class record written after F, named the same way, pinning a path changed on M by a '
              'commit that is not an ancestor of F')
POSTF3_REVIEW = 'the review record of a reviewed reconciliation record named as the primary record by --classify REV:PATH'
POSTF4 = [
    "no review record naming the record's blob in the same directory of REV's tree",
    "two review records naming the record's blob in that directory",
    "a review record whose reviewer equals the record's author",
    "a record in another reconciliation directory of REV's tree supersedes the record",
    "two records in two different reconciliation directories of REV's tree supersede the same predecessor",
    "the record's supersedes names a predecessor that is not present at its path in REV's tree",
    'a REV whose single parent is an earlier main commit than M, the superseding record being absent there',
    'a REV with two parents',
    "a REV whose tree differs from its parent's at a path outside every reconciliation directory",
    'two --classify arguments naming different REVs',
    "two reviewed records added by REV in two reconciliation directories, with different record_id values, both naming "
    "the run's M and covering one path, neither superseding the other",
    'a REV that is an abbreviated commit id',
    'a REV naming a commit object whose content does not hash to its id',
    "an admitted record naming a commit other than the run's M, its blobs satisfying RC1-RC13 at the run's M",
    "an admitted record naming a commit other than the run's X, its blobs satisfying RC1-RC13",
]
POSTF5 = ['PATH under a prefix of the tool-landing class', "PATH inside the plan's record directory",
          'PATH a ledgered path', 'PATH a corpus path', 'PATH outside verification/audits/',
          "the review record in a directory other than the record's"]
BIND = ["a reviewed reconciliation record bound to the run: ledger_base the run's H, naming the run's M and X, its m and x "
        "the path's blobs at the run's M and C (positive)",
        "countercase: the same record naming a commit other than the run's M",
        "countercase: the same record naming a commit other than the run's X",
        'countercase: the same record with M and X null',
        "countercase: the same record, in harness mode, with a review record whose reviewer equals the record's author "
        "(record lint fails)",
        "countercase: the same record read from a REV whose single parent is neither M0 nor the run's M"]
