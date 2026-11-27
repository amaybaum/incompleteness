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
CONTROL_EFFECT = {'conclusions': 'none', 'assessment': 'control fixture: the change on main touches no planned edit',
                  'method': 'control: every condition recomputed from git objects', 'verdict': 'no-effect'}
RD2 = 'verification/audits/syn-recon-b/'
EDITS = [('# synthetic', ['# synthetic', '', 'Preface line one.'])]


def jb(o):
    return sf.jb(o)


def sha(b):
    return util.sha256(b)


class World:
    """One synthetic post-freeze world. pre_change: the ledgered file's change on M is made before F (F descends from
    it), so no commit on M after F changes it (POSTF-2)."""

    def __init__(self, r, pre_change=False, side=False, config_records=None, variant=None, edits=None, first_id=1):
        self.r = r
        syn = self.syn = sf.Syn()
        repo = self.repo = syn.repo
        edits = edits or EDITS
        self.edits = edits
        pd = sf.patch_doc(syn.H, edits, first_id)
        base = {'patch_sha': sha(pd), 'files': {'syn/patch.json': pd}}
        h_doc = repo.read(syn.H, sf.DOC)
        changed = {sf.DOC: h_doc.replace(b'Closing words of the file.', b'Closing words, changed on main.')}
        if side:
            changed['notes/side.txt'] = b'a side change on main\n'
        x_doc = sf.apply_text(h_doc.decode(), edits).encode()
        # the delegated class artifact-hash/1 of the synthetic configuration: the digest of the candidate's document
        self.X = repo.derive(syn.H, {sf.DOC: x_doc, 'out/digest.txt': (sha(x_doc) + '\n').encode()},
                             parents=[syn.H], subject='X')
        if config_records:
            base = dict(base, extra={'records': None})
        if variant:
            v = variant(self)
            base = dict(base, extra=dict(base.get('extra') or {}, **v.get('extra', {})),
                        files=dict(base['files'], **v.get('files', {})), add_records=v.get('add_records', []))
        c, p, s, files = syn.build(base)
        self.build_spec = base
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
        doc = rcmod.draft(self.repo, self.ctx, self.syn.H, self.M, self.X, self.led, sf.DOC,
                          scientific_effect=dict(CONTROL_EFFECT))
        doc.update(record_id='syn-recon', author=sf.WRITER, supersedes=None, M=self.M, X=self.X)
        doc.update(upd)
        return doc

    def review(self, path, data, reviewer=sf.REVIEWER):
        doc = json.loads(data)
        return jb({'schema': rec.review_schema, 'reviewer': reviewer, 'reviewed': {'path': path,
                                                                                   'blob_sha256': sha(data)},
                   'method': 'read every object the record names',
                   'verdicts': [{'item': i, 'verdict': 'accept', 'reason': ''} for i in rec.item_ids(doc)]})

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

    def run(self, classify=(), harness=False, main=None, extra=(), stderr=None):
        tail = ['--scientific-base', self.syn.H, '--candidate', self.X, '--ledger', None, '--delegation', None,
                '--main', main or self.M] + list(extra)
        for c in classify:
            tail += ['--classify', c]
        if harness:
            argv = list(tail)
            argv[argv.index(None)] = '%s:syn/patch.json' % self.c
            argv[argv.index(None)] = '%s:syn/delegation.json' % self.c
            return self.r.cli(self.repo, ['execution'] + argv, self.c, self.p, None, harness=True, stderr=stderr)
        w = hf.World(self.repo, self.syn.H)
        F = hf.freeze(self.repo, self.c, self.p)
        argv = list(tail)
        argv[argv.index(None)] = '%s:syn/patch.json' % F
        argv[argv.index(None)] = '%s:syn/delegation.json' % F
        full = ['execution', '--config', '%s:%s' % (F, self.p), '--out', self.r.out()] + w.args(F) + argv
        return cli.run(full, repo=self.repo, stderr=stderr or io.StringIO(), control=w.control(w.checkout()), environ={})


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
             'H': rcmod.entry_binding(doc, e).get('ledger_base'), 'M': doc.get('M'), 'C': doc.get('X')}
            for e in doc.get('paths') or []]
    return {'drift': drift, 'records': recs, 'roles': {'H': w.syn.H, 'M': w.M, 'C': w.X}}


def line_patch_control(r, check, capture):
    """R6.RECON.13: evaluate RC8 twice against one candidate and one entry."""
    positive = ('the synthetic line-patch ledger stating expected_sha256 equal to the sha256 of the candidate\'s '
                'patched bytes (positive)')
    negative = 'countercase: the same ledger with a wrong expected_sha256'
    w = World(r)
    candidate = w.repo.read(w.X, sf.DOC)
    candidate_digest = w.repo.read(w.X, 'out/digest.txt')
    doc = w.record()
    entry = doc['paths'][0]
    original = w.led['files'][sf.DOC]
    # Change the normalized expected hash only. The adapter's raw ledger view also holds the file entry and
    # supplies the binding checked by RC13. A deepcopy would preserve the alias and perturb RC13 as well.
    altered = dict(original, expected_sha256='0' * 64)
    bad_ledger = dict(w.led, files={**w.led['files'], sf.DOC: altered})
    context = {'H': w.syn.H, 'M': w.M, 'X': w.X, 'classes': [], 'record_refs': {}}
    verdicts = {}
    for name, ledger in ((positive, w.led), (negative, bad_ledger)):
        evaluation = rcmod.evaluate(w.repo, w.ctx, w.syn.H, w.M, w.X, ledger, doc, entry, [], {})
        # The line-patch adapter's ledger has one non-JSON value per splice: its replacement bytes.
        retained = dict(ledger, splices=[dict(s, new_bytes=s['new_bytes'].hex()) for s in ledger['splices']])
        capture('line-patch RC8 evaluation', {'operation': 'execution', 'context': context,
                'candidate_blob': w.repo.blob_id(w.X, sf.DOC), 'record': doc, 'ledger': retained,
                'evaluation': evaluation}, case=name)
        verdicts[name] = evaluation['holds'].get('RC8')
    check('LINE-PATCH-RC8', 'RC8 holds only with the patched candidate hash',
          'candidate SHA-256 matches the stated hash and the evaluator changes its RC8 verdict', verdicts,
          original['expected_sha256'] == sha(candidate) and verdicts[positive] is True and verdicts[negative] is False,
          files={'candidate.bin': candidate, 'candidate-digest.bin': candidate_digest},
          procedure={'name': 'line-patch-rc8', 'lib': 'oracle', 'tool_output': ['case01.result.json', 'case02.result.json'],
                     'oracle_output': 'candidate.bin', 'candidate_digest': 'candidate-digest.bin'})


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
    rb_p1_control(r, check)

    def restored():
        """The POSTF-1 input, run again, as the restored case of POSTF-2 to POSTF-5."""
        w0 = World(r)
        rv, pth, _ = w0.standard()
        w0.run(['%s:%s' % (rv, pth)])
        return pth

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
                     RD + 'rec.review2.json': w_.review(pth, data, reviewer='session.fixture-reviewer-c')})
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

    def bad_object():
        # an on-disk object store holding a loose object whose content does not hash to its id; the verified reader
        # refuses it (ERROR UNRESOLVABLE)
        import os
        import subprocess
        import tempfile
        import zlib
        from ledger_coverage.engine import gitobj
        w_ = World(r)
        d = tempfile.mkdtemp(prefix='postf4-store-', dir=r.out_root)
        subprocess.run(['git', 'init', '-q', d], check=True)
        body = b'tree 4b825dc642cb6eb9a060e54bf8d69288fbee4904\n\nsynthetic commit\n'
        real = b'commit %d\x00' % len(body) + body
        fake = gitobj.object_id('commit', body.replace(b'synthetic', b'another'))
        od = os.path.join(d, '.git', 'objects', fake[:2])
        os.makedirs(od, exist_ok=True)
        with open(os.path.join(od, fake[2:]), 'wb') as f:
            f.write(zlib.compress(real))
        w_.repo.base = gitobj.GitRepo(d)
        return w_.run(['%s:%s' % (fake, RD + 'rec.json')]) + (None,)

    def config_recon_variant(doc_of):
        # a configuration referencing a reconciliation record (with its review); doc_of(World) drafts it from the
        # main and candidate commits, which do not depend on the configuration
        w0 = World(r)
        cdoc = doc_of(w0)
        b = jb(cdoc)
        ref = {'path': 'syn/cfg/recon.json', 'blob_sha256': sha(b)}
        files = {ref['path']: b}
        review = sf.Syn.chain(None, files, ref['path'], sf.REVIEWER)

        def variant(w_):
            return {'files': files, 'add_records': [dict(ref, kind='reconciliation')] + review}
        return variant, ref

    def supersedes_config():
        variant, ref = config_recon_variant(lambda w0: w0.record(record_id='syn-cfg-recon'))
        w_ = World(r, variant=variant)
        rv, pth, _ = w_.standard(w_.record(record_id='syn-cfg-recon', supersedes=ref))
        return w_.run(['%s:%s' % (rv, pth)]) + (pth,)

    def config_and_admitted():
        variant, ref = config_recon_variant(lambda w0: w0.record(record_id='syn-cfg-recon', M=w0.syn.H))
        w_ = World(r, variant=variant)
        rv, pth, _ = w_.standard()
        code, res = w_.run(['%s:%s' % (rv, pth)])
        res4['_config_record_invalid'] = invalid(res, ref['path'])
        return code, res, pth

    for name, fn in ((POSTF4[12], bad_object), (POSTF4[15], supersedes_config), (POSTF4[16], config_and_admitted)):
        case4(name, fn)
    for name, fn in ((POSTF4[0], no_review), (POSTF4[1], two_reviews), (POSTF4[2], self_review),
                     (POSTF4[3], superseded_elsewhere), (POSTF4[4], fork), (POSTF4[5], absent_predecessor),
                     (POSTF4[6], earlier_parent), (POSTF4[7], two_parents), (POSTF4[8], outside_change),
                     (POSTF4[9], two_revs), (POSTF4[10], two_records), (POSTF4[11], abbreviated),
                     (POSTF4[13], other_m), (POSTF4[14], other_x)):
        case4(name, fn)
    rp4 = restored()
    names4.append(('restored', {'record': rp4}))
    want_drift = {POSTF4[10], POSTF4[13], POSTF4[14], POSTF4[16]}
    cases4 = {k: v for k, v in res4.items() if not k.startswith('_')}
    ok4 = all('error' not in v and v['exit'] == 20 and v['invalid'] and (k not in want_drift or 'base-drift' in
                                                                       v['classes'])
              for k, v in cases4.items() if k != POSTF4[12]) and \
        cases4.get(POSTF4[12], {}).get('stop') == 'UNRESOLVABLE' and res4.get('_config_record_invalid') is True
    check('POSTF-4', 'the record commit and lineage conditions of the post-freeze route: each violation FAIL '
          'record-invalid (an unverifiable object ERROR UNRESOLVABLE)', 'every case as its expectation states; the '
          'configuration-referenced record of the last case is record-invalid as well', {'cases': res4,
                                                                                         'built_cases_hold': ok4},
          ok4, cases=names4)

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
                      'review_lint_passes': not invalid(res, pth) and not invalid(res, pth[:-5] + '.review.json'),
                      'fail_items': sorted({i['class'] for i in (res or {}).get('items', []) if i['decision'] == 'FAIL'}),
                      'review_classes': sorted({i['class'] for i in (res or {}).get('items', [])
                                                if i['decision'] == 'REVIEW_REQUIRED'})}
        namesb.append((name, {'record': pth}))
    bind_case(BIND[0])
    bind_case(BIND[1], wb.record(M=wb.syn.H))
    bind_case(BIND[2], wb.record(X=wb.syn.H))
    bind_case(BIND[3], wb.record(M=None, X=None))
    bind_case(BIND[4], reviewer=sf.WRITER)
    bind_case(BIND[5], parent=wb.syn.H)

    # owner decision of 2026-11-26 (#1169 comment 7186638587, item 8): delegated classes are not exempted, and an
    # unrelated failure beside the reconciled drift keeps its own outcome. Diagnostic runs, not expectation cases.
    def unrelated(name, w, extra_files, extra_classify):
        rv, pth, data = w.standard(extra=extra_files)
        code, res = w.run(['%s:%s' % (rv, pth)] + [c % rv for c in extra_classify], harness=True)
        sc = [x for x in (res or {}).get('side_changes') or [] if x.get('path') == sf.DOC]
        resb[name] = {'exit': code, 'classes': classes(res), 'outcome': (res or {}).get('outcome'),
                      'drift_state': 'reconciled' if sc and sc[0].get('reconciled') else 'unresolved'}
        namesb.append(None)
    hit = jb({'schema': 'oi-hit-classification/1', 'record_id': 'syn-unrelated', 'author': sf.WRITER,
              'supersedes': None, 'classifications': []})
    unrelated(BIND_DIAG[0], World(r), {RD2 + 'unrelated.json': hit}, ['%s:' + RD2 + 'unrelated.json'])
    ws = World(r)
    ws.M = ws.repo.derive(ws.M, {'notes/side.txt': b'an unrelated side change on main\n'}, parents=[ws.M],
                          subject='unrelated side change')
    unrelated(BIND_DIAG[1], ws, None, [])
    diag_ok = resb[BIND_DIAG[0]]['drift_state'] == 'reconciled' and resb[BIND_DIAG[0]]['exit'] == 20 and \
        'record-invalid' in resb[BIND_DIAG[0]]['classes'] and \
        resb[BIND_DIAG[1]]['exit'] == 20 and 'side-change-unclassified' in resb[BIND_DIAG[1]]['classes'] and \
        'base-drift' in resb[BIND_DIAG[1]]['classes']
    # amendment 5: the positive case is drift reconciled, no FAIL item, and REVIEW_REQUIRED only from delegated
    # classes
    pos_items = resb[BIND[0]].get('review_classes', [])
    okb = resb[BIND[0]]['drift_state'] == 'reconciled' and resb[BIND[0]]['exit'] in (0, 10) and \
        not resb[BIND[0]].get('fail_items') and all(c == 'delegated-evidence-missing' for c in pos_items) and \
        all(resb[k]['drift_state'] == 'unresolved' and resb[k]['exit'] == 20 for k in BIND[1:]) and \
        all(resb[k]['invalid'] for k in BIND[4:]) and diag_ok
    resb['not_built'] = [BIND_PLANTED]
    resb['built_cases_hold'] = okb
    okb = False  # the planted case is not built
    check('RTL2-BIND', "the binding of R6.RECON.21 in the control harness: only a reviewed record naming the run's M "
          "and X, passing record lint and read from a REV tied to the run, reconciles", 'positive reconciled and PASS; '
          'every countercase unresolved', resb, okb, cases=namesb,
          attested={n: {'drift_state_in': [v['drift_state']]} for n, v in resb.items() if n in BIND},
          files={'rtl2-drift.json': proc_in['drift'], 'rtl2-records.json': proc_in['records'],
                 'rtl2-roles.json': proc_in['roles']},
          procedure={'name': 'rtl2-binding', 'lib': 'rtl2', 'drift': 'rtl2-drift.json',
                     'records': 'rtl2-records.json', 'roles': 'rtl2-roles.json'})
    return out


BIND_DIAG = ['diagnostic: the positive record beside an unrelated unreviewed record named by --classify (FAIL '
             'record-invalid expected, the drift still reconciled)',
             'diagnostic: the positive record beside an unrelated side change on M, in its own commit, that no class pins '
             '(FAIL expected: side-change-unclassified, and base-drift, since RC11 needs every side change classified)']
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
    'an admitted record whose supersedes names a reconciliation record the configuration references',
    'a reconciliation record the configuration references and an admitted record, naming different commits M, covering one path (each record-invalid; neither applies)',
]
POSTF5 = ['PATH under a prefix of the tool-landing class', "PATH inside the plan's record directory",
          'PATH a ledgered path', 'PATH a corpus path', 'PATH outside verification/audits/',
          "the review record in a directory other than the record's"]
BIND = [
    "a reviewed reconciliation record bound to the run: ledger_base the run's H, naming the run's M and X, its m and x the path's blobs at the run's M and C (positive: drift reconciled; REVIEW_REQUIRED only from delegated classes)",
    "countercase: the same record naming a commit other than the run's M",
    "countercase: the same record naming a commit other than the run's X",
    'countercase: the same record with M and X null',
    "countercase: the same record, in harness mode, with a review record whose reviewer equals the record's author (record lint fails)",
    "countercase: the same record read from a REV whose single parent is neither M0 nor the run's M",
]
# amendment 5's planted non-delegated REVIEW case: not built (op C runs no review profile; the planted unclassified
# hit arises only from the reconciled-state trial, R6.RECON.23, which this tool revision does not implement)
BIND_PLANTED = 'countercase: the same reconciled drift with a planted non-delegated REVIEW item that touches no reconciliation (an unclassified review hit on an unledgered line): the drift stays reconciled and the positive predicate (REVIEW_REQUIRED only from delegated classes) fails'


# RECORD-BASE (design r6 as amended by amendment 4: R6.RECON.2 (c), R6.RECON.21, R6.GATE.16)
RB = ["a run on a predicted M built from M0 by in-memory commits adding tool-landing paths whose blobs equal their pins, "
      "named with --record-base M0; REV's single parent is M0 (positive)",
      "countercase: REV's parent is the predicted M",
      "countercase: REV's parent is an intermediate in-memory commit (RT-O9 shape)",
      "countercase: REV's parent is an ancestor of M0",
      "countercase: a ledgered, corpus, unclassified or reconciliation-directory change lies between M0 and M",
      "countercase: a merge lies between M0 and M",
      "countercase: a change between M0 and M that a later step reverts (the aggregate diff is empty for it)",
      "countercase: a pin path of the tool-landing class with a different blob, or deleted",
      "countercase: --record-base names an in-memory commit",
      "countercase: the configuration lies in a directory that is not an authorized record directory",
      "countercase: a reviewed class record named by --classify whose prefixes cover the offending change",
      "countercase: --record-base given in a chain-admitted run",
      "countercase: the result's inputs.record_base differs from the runner's pinned main commit"]
# the reason each countercase must give (its check), so that a countercase cannot pass for another check's reason
RB_WHY = {RB[1]: "the record commit's parent is not the run's record base",
          RB[2]: "the record commit's parent is not the run's record base",
          RB[3]: "the record commit's parent is not the run's record base",
          RB[4]: 'is neither a tool-landing path nor in an authorized plan record directory',
          RB[5]: 'has 2 parents, not one',
          RB[6]: 'but not in the aggregate diff',
          RB[7]: 'the tool-landing class',
          RB[8]: 'the record base is an in-memory commit',
          RB[9]: 'syn/cfg/extra.json is neither a tool-landing path nor in an authorized plan record directory',
          RB[10]: 'misc/x.txt is neither a tool-landing path nor in an authorized plan record directory',
          RB[12]: 'M does not descend from the record base by in-memory commits'}
RB_TOOL = 'tools/syn-tool/'
RB_PIN = RB_TOOL + 'entry.py'
RB_PIN_BYTES = b'x = 2\n'
RB_NOTE = RB_TOOL + 'note.md'
RB_LANDING = {RB_PIN: RB_PIN_BYTES, RB_NOTE: b'tool note\n'}


def rb_variant(w):
    """The synthetic configuration with a side-change class record whose class tool-landing has the prefix RB_TOOL and
    a pin for each path of RB_LANDING; the configuration pins it as roles.side_change_classes."""
    from ledger_coverage import record_authority as ra
    doc = {'schema': 'oi-side-change-classes/1', 'record_id': 'syn-tool-landing', 'author': sf.WRITER,
           'supersedes': None, 'classes': [{'id': ra.tool_landing_class_id, 'prefixes': [RB_TOOL],
                                            'reason': 'synthetic tool landing',
                                            'pins': [{'path': p, 'blob_sha256': sha(b)}
                                                     for p, b in sorted(RB_LANDING.items())]}]}
    b = jb(doc)
    ref = {'path': 'syn/cfg/classes.json', 'blob_sha256': sha(b)}
    files = {ref['path']: b}
    review = sf.Syn.chain(None, files, ref['path'], sf.REVIEWER)
    return {'files': files, 'add_records': [dict(ref, kind='side-change-classes')] + review,
            'extra': {'roles': {'scientific_base': w.syn.H, 'pin': w.syn.pin, 'side_change_classes': ref}}}


def rb_world(r):
    """A World whose main commit M0 lies in the object store (an inner reader) and whose predicted M is built on it by
    in-memory commits of the outer reader: the shape of RT-L2's predicted M."""
    from ledger_coverage.engine import gitobj
    w = World(r, variant=rb_variant)
    inner = w.repo
    w.repo = gitobj.Overlay(inner)
    # M0 is a commit of the object store (the inner reader) holding an earlier version of the pinned tool file
    w.M0 = inner.derive(w.M, {RB_PIN: b'x = 1\n'}, parents=[w.M], subject='main with an earlier tool file')
    w.I = w.repo.derive(w.M0, {RB_NOTE: RB_LANDING[RB_NOTE]}, parents=[w.M0], subject='tool landing, step 1')
    w.M = w.repo.derive(w.I, {RB_PIN: RB_PIN_BYTES}, parents=[w.I], subject='tool landing, step 2')
    loaded = cfgmod.load(w.repo, w.c, w.p, None, 'execution', 'harness')
    w.ctx = pl.RunContext(w.repo, loaded.config, loaded.profiles, [], {}, None)
    return w


def rb_p1_control(r, check):
    """R6.RECON.2 (c): the default record base is the run's M."""
    positive_case = ("a record commit whose single parent is the run's M and which adds the record and its review "
                     'record in one reconciliation directory (positive; the same input as POSTF-1)')
    negative_case = ("countercase: without --record-base, a record commit whose parent lies below the run's M across "
                     'only permitted tool-landing additions (pinned paths with matching blobs); the route of '
                     '--record-base M0 would admit such a base, the default route, whose base is M, does not')
    w = World(r)
    rev, path, _ = w.standard()
    pos_code, pos = w.run(['%s:%s' % (rev, path)])

    predicted = rb_world(r)
    older_rev, older_path, _ = predicted.standard(parent=predicted.M0)
    neg_code, neg = predicted.run(['%s:%s' % (older_rev, older_path)], harness=True)

    check('RB-P1', 'the default record base is M',
          'the record on M is admitted without record-invalid, and the record below M is refused with exit 20',
          {'cases': {positive_case: {'exit': pos_code, 'classes': classes(pos)},
                     negative_case: {'exit': neg_code, 'classes': classes(neg)}}},
          admitted(pos, path) and 'record-invalid' not in classes(pos) and
          neg_code == 20 and invalid(neg, older_path),
          cases=[(positive_case, {'record': path}), (negative_case, {'record': older_path})])


def res_base(res):
    return ((res or {}).get('inputs') or {}).get('record_base')


def rb_gate_case(res, roles_m0):
    """The gate's rtl2 procedure (R6.GATE.16) over one retained result and the runner's pinned main: the rt_l2 value."""
    import os
    import tempfile
    from ledger_coverage.gate import control_gate as cg
    d = tempfile.mkdtemp(prefix='rb-gate-')
    files = {'result.json': res, 'drift.json': [], 'records.json': [],
             'roles.json': {'H': 'a' * 40, 'M': 'b' * 40, 'C': 'c' * 40, 'M0': roles_m0}}
    man = {'schema': cg.SCHEMA_MAN, 'id': 'RECORD-BASE', 'files': {}, 'cases': [{'case': '', 'result_file': 'result.json',
                                                     'argv': ['execution', '--record-base', res_base(res)]}],
           'procedure': {'lib': 'rtl2', 'drift': 'drift.json', 'records': 'records.json', 'roles': 'roles.json'}}
    for n, v in files.items():
        b = jb(v)
        with open(os.path.join(d, n), 'wb') as f:
            f.write(b)
        man['files'][n] = sha(b)
    with open(os.path.join(d, 'manifest.json'), 'wb') as f:
        f.write(jb(man))
    found = []
    actual = cg.eval_procedure({'procedure': {'lib': 'rtl2'}}, cg.Evidence(d, '.', 'RECORD-BASE'), found)
    return actual.get('rt_l2'), found


def rb_controls(r, check):
    res, names, att = {}, [], {}

    def run(name, parent=None, base=None, extra_files=None, w=None, classify=(), harness=True, binding=True):
        """One op C run on a predicted M; parent(w) gives REV's parent (default M0), base the --record-base."""
        w = w or rb_world(r)
        rv, pth, data = w.standard(parent=parent(w) if parent else w.M0, extra=extra_files)
        err = io.StringIO()
        code, out = w.run(['%s:%s' % (rv, pth)] + list(classify), harness=harness,
                          extra=['--record-base', base or w.M0], stderr=err)
        res[name] = {'exit': code, 'classes': classes(out), 'invalid': invalid(out, pth),
                     'admitted': admitted(out, pth), 'record_base': ((out or {}).get('inputs') or {}).get('record_base'),
                     'stop': ((out or {}).get('stop') or {}).get('class'),
                     'usage': (json.loads(err.getvalue() or 'null') or {}).get('message') if code == 64 else None,
                     'why': [d for i in (out or {}).get('items', []) if i['class'] == 'record-invalid'
                             and i.get('subject') == pth for d in (i.get('detail') or [])][:1]}
        names.append((name, {'record': pth} if binding else {}))
        return w, out

    w0, out0 = run(RB[0])
    att[RB[0]] = {'equals': 'inputs.record_base is M0'} if res[RB[0]]['record_base'] == w0.M0 else {}
    run(RB[1], parent=lambda w: w.M)
    run(RB[2], parent=lambda w: w.I)
    run(RB[3], parent=lambda w: w.repo.parents(w.M0)[0])

    def top(ch, merge=False, revert=None):
        w = rb_world(r)
        if merge:
            # the merge brings in only a tool-landing path, so that only the single-parent check can refuse it
            side = w.repo.derive(w.M0, {RB_TOOL + 'side.txt': b'side\n'}, parents=[w.M0], subject='side')
            w.M = w.repo.derive(w.M, {RB_TOOL + 'side.txt': b'side\n'}, parents=[w.M, side], subject='merge')
        elif revert is not None:
            mid = w.repo.derive(w.M, ch, parents=[w.M], subject='a change')
            w.M = w.repo.derive(mid, revert, parents=[mid], subject='its revert')
        else:
            w.M = w.repo.derive(w.M, ch, parents=[w.M], subject='a further change')
        return w
    w = rb_world(r)
    h_doc = w.repo.read(w.M0, sf.DOC)
    subs = [('ledgered', {sf.DOC: h_doc + b'One more line on main.\n'}), ('corpus', {'doc/other.md': b'corpus\n'}),
            ('unclassified', {'misc/x.txt': b'x\n'}),
            ('reconciliation directory', {RD2 + 'x.json': jb({'schema': 'oi-reconciliation/2', 'record_id': 'x'})})]
    for k, (label, ch) in enumerate(subs):
        run(RB[4] if k == 0 else '%s (%s)' % (RB[4], label), w=top(ch))
    run(RB[5], w=top(None, merge=True))
    run(RB[6], w=top({'misc/y.txt': b'y\n'}, revert={'misc/y.txt': None}))
    run(RB[7], w=top({RB_PIN: b'x = 3\n'}))
    w = rb_world(r)
    w.M = w.repo.derive(w.I, {RB_PIN: None}, parents=[w.I], subject='tool landing deleting the pinned file')
    run('%s (deleted)' % RB[7], w=w)
    w = rb_world(r)
    run(RB[8], parent=lambda w: w.I, base=w.I, w=w)
    run(RB[9], w=top({'syn/cfg/extra.json': b'{}\n'}))
    # a reviewed class record named by --classify, whose prefixes cover misc/
    w = top({'misc/x.txt': b'x\n'})
    cls = {'schema': 'oi-side-change-classes/1', 'record_id': 'syn-misc', 'author': sf.WRITER, 'supersedes': None,
           'classes': [{'id': 'misc', 'prefixes': ['misc/'], 'reason': 'synthetic'}]}
    cb = jb(cls)
    cpath = 'syn/late/classes.json'
    crev = w.repo.derive(w.M, {cpath: cb, 'syn/late/classes.review.json': w.review(cpath, cb)}, parents=[w.M])
    run(RB[10], w=w, classify=['%s:%s' % (crev, cpath)])
    run(RB[11], harness=False, binding=False)
    # the run names a record base other than the runner's pinned main M0 (the main commit M0 is built on); the gate's
    # rtl2 comparison of that result with M0 gives FAIL, and of the positive result with M0 gives PASS
    w = rb_world(r)
    _, out12 = run(RB[12], base=w.repo.parents(w.M0)[0], w=w)
    wrong = rb_gate_case(out12, w.M0)
    right = rb_gate_case(out0, w0.M0)
    unnamed = rb_gate_case(out0, None)
    res[RB[12]].update(rt_l2_wrong_base=wrong[0], rt_l2_right_base=right[0], findings_wrong_base=wrong[1],
                       findings_right_base=right[1], rt_l2_no_m0=unnamed[0], findings_no_m0=unnamed[1])
    att[RB[12]] = {'rt_l2_status': wrong[0]}
    neg = [k for k in res if k not in (RB[0], RB[11])]
    ok = 'base-drift' not in res[RB[0]]['classes'] and res[RB[0]]['admitted'] and not res[RB[0]]['invalid'] and \
        res[RB[0]]['record_base'] == w0.M0 and \
        all(res[k]['exit'] == 20 and res[k]['invalid'] for k in neg) and \
        all(res[k]['why'] and next(v for c, v in RB_WHY.items() if k == c or k.startswith(c + ' (')) in res[k]['why'][0] and
            (k.endswith('(deleted)') or 'is deleted' not in res[k]['why'][0]) for k in neg) and \
        all('is deleted' in res[k]['why'][0] for k in neg if k.endswith('(deleted)')) and \
        unnamed[0] == 'FAIL' and \
        res[RB[11]]['exit'] == 64 and res[RB[11]]['usage'] == '--record-base in a chain-admitted run' and \
        wrong[0] == 'FAIL' and right[0] == 'PASS'
    check('RECORD-BASE', 'the record base of a run on a predicted M is named with --record-base M0 and admitted only '
          'after the tool establishes it from git objects; the gate compares it with the pinned main',
          'positive admitted with inputs.record_base M0; every countercase record-invalid; USAGE in a chain-admitted '
          "run; the gate's rt_l2 FAIL for a different base and PASS for M0", res, ok,
          cases=names, attested=att)


# RECON-BLOCK (design r6 as amended by amendments 3 and 4: R6.RECON.25, R6.RECON.26; first kind of finding only)
BLOCK = ["a reviewed entry whose scientific_effect verdict is invalidates, naming an edit id of the path",
         "a reviewed entry of an unledgered corpus path whose verdict invalidates an edit of a ledgered path",
         "the same, with a later record superseding it whose verdict is no-effect",
         "the same, with every other drifted path reconciled",
         "the blocking record landed on main, and a later run naming a REV whose tree omits it in the reconciliation "
         "directory it used, or a chain run without --classify",
         "a writer's verdict no-effect with a non-author review whose verdict on the scientific_effect finds "
         "invalidation, naming the invalidated edit id and its sha256",
         "the same review finding, followed by a new record of the same path with verdict no-effect and an accepting "
         "review",
         "a later commit on M reverting the invalidating change, the plan unchanged",
         "a revert of the path to exactly H's bytes with no other drifted path (a run-level item names the path)",
         "a reviewed repair of the change landed on M and recorded by its own reconciliation record entry, the plan "
         "unchanged",
         "a new configuration version with a new freeze whose ledger still carries the invalidated edit-list entry "
         "unchanged",
         "countercase: the same entry with verdict no-effect (positive)",
         "countercase: the run under a revised plan, a new configuration whose ledger changes the invalidated edit's "
         "edit-list entry (positive)",
         "countercase: the run under a revised plan whose ledger no longer carries the invalidated edit, the finding "
         "and the repair still on M (positive)"]
OTHER = 'doc/other.md'
EDITS_REWORDED = [('# synthetic', ['# synthetic', '', 'Preface line one, reworded.'])]
EDITS_OTHER = [('Remark two notes a side fact.', ['Remark two notes another fact.'])]


def invalidating(w, path, M=None, edit='E1'):
    """A finding of the first kind: the writer's entry for `path` with verdict invalidates, naming the edit of the
    world's ledger as {id, sha256} (the amendment-3 reading of `invalidated`)."""
    M = M or w.M
    # the r13 form of a first-kind finding (R6.RECON.26 Form (ii) and (iii)): each invalidated element carries its
    # target at H, and the effect names the configuration it was assessed under
    sps = [x for x in w.led.get('splices') or [] if x.get('id') == edit]
    target = {'path': sps[0]['file'], 'start_H': sps[0]['start'], 'old_sha256': sps[0]['old_sha256']} if sps else None
    elem = {'id': edit, 'sha256': rcmod.edit_key(w.led, edit)}
    if target is not None:
        elem['target'] = target
    eff = dict(CONTROL_EFFECT, conclusions=[edit], verdict='invalidates', invalidated=[elem],
               configuration={'path': w.p, 'blob_sha256': sha(w.files[w.p])},
               assessment='control fixture: the change on main invalidates the basis of the planned edit')
    doc = rcmod.draft(w.repo, w.ctx, w.syn.H, M, w.X, w.led, path, scientific_effect=eff)
    doc.update(record_id='syn-finding-' + path.replace('/', '-'), author=sf.WRITER, supersedes=None, M=M, X=w.X)
    return doc


def land(w, docs, subject='land records on main'):
    """A commit on main adding each (path, doc) with its review record in its directory; it becomes w.M."""
    files = {}
    for path, doc in docs:
        data = jb(doc)
        files[path] = data
        files[path[:-5] + '.review.json'] = w.review(path, data)
    w.M = w.repo.derive(w.M, files, parents=[w.M], subject=subject)
    return w.M


def block_controls(r, check):
    res, names = {}, []

    def run(name, w, classify=(), harness=True, binding=None):
        code, out = w.run(list(classify), harness=harness)
        d = next((x for x in (out or {}).get('dispositions') or [] if x.get('path') == sf.DOC), None)
        blocked = [i for i in (out or {}).get('items', []) if i['class'] == 'retirement-blocked']
        res[name] = {'exit': code, 'classes': classes(out), 'doc_disposition': (d or {}).get('disposition'),
                     'doc_reconciled': any(x.get('path') == sf.DOC and x.get('reconciled')
                                           for x in (out or {}).get('side_changes') or []),
                     'blocked': [(i.get('subject'), bool((i.get('fp') or i.get('fingerprint_data') or {}))) for i in
                                 blocked],
                     'run_level': [i.get('subject') for i in blocked if 'run-level' in str(i.get('detail'))],
                     'category3': (out or {}).get('category3')}
        names.append((name, binding or {}))
        return out

    # 1: the finding on the ledgered path, landed on main
    w = World(r)
    land(w, [(RD + 'finding.json', invalidating(w, sf.DOC))])
    run(BLOCK[0], w)
    # 2: a corpus path the ledger does not list, its entry invalidating the ledgered edit
    w = World(r)
    w.M = w.repo.derive(w.M, {OTHER: b'# other\n\nA corpus file changed on main.\n'}, parents=[w.M], subject='corpus')
    fin = invalidating(w, OTHER)
    land(w, [(RD + 'finding.json', fin)])
    run(BLOCK[1], w)
    # 3: a later record superseding it with verdict no-effect
    later = rcmod.draft(w.repo, w.ctx, w.syn.H, w.M, w.X, w.led, OTHER, scientific_effect=dict(CONTROL_EFFECT))
    fin_ref = {'path': RD + 'finding.json', 'blob_sha256': sha(jb(fin))}
    later.update(record_id=fin['record_id'], author=sf.WRITER, supersedes=fin_ref, M=w.M, X=w.X)
    land(w, [(RD2 + 'later.json', later)], 'a superseding record')
    run(BLOCK[2], w)
    # 4: every other drifted path reconciled: the finding and a reviewed no-effect record of the ledgered path, both
    # added by the record commit REV the run names (no record landed on main, so no unclassified side change)
    w = World(r)
    w.M = w.repo.derive(w.M, {OTHER: b'# other\n\nA corpus file changed on main.\n'}, parents=[w.M], subject='corpus')
    f4 = invalidating(w, OTHER)
    f4b = jb(f4)
    rv, pth, _ = w.standard(w.record(), path=RD2 + 'doc.json',
                            extra={RD + 'finding.json': f4b, RD + 'finding.review.json': w.review(RD + 'finding.json',
                                                                                                f4b)})
    run(BLOCK[3], w, ['%s:%s' % (rv, pth), '%s:%s' % (rv, RD + 'finding.json')])
    # 5: the finding on main; a chain run without --classify
    w = World(r)
    land(w, [(RD + 'finding.json', invalidating(w, sf.DOC))])
    run(BLOCK[4], w, harness=False)
    # 8: a later commit reverting the change, another path still drifted
    w = World(r)
    land(w, [(RD + 'finding.json', invalidating(w, sf.DOC))])
    h_doc = w.repo.read(w.syn.H, sf.DOC)
    w.M = w.repo.derive(w.M, {sf.DOC: h_doc, OTHER: b'# other\n\nstill drifted.\n'}, parents=[w.M], subject='revert')
    run(BLOCK[7], w)
    # 9: a revert to exactly H's bytes, no other drifted path
    w = World(r)
    land(w, [(RD + 'finding.json', invalidating(w, sf.DOC))])
    w.M = w.repo.derive(w.M, {sf.DOC: w.repo.read(w.syn.H, sf.DOC)}, parents=[w.M], subject='revert to H')
    run(BLOCK[8], w, binding={'path': sf.DOC})
    # 10: a reviewed repair landed and recorded by its own no-effect entry
    w = World(r)
    land(w, [(RD + 'finding.json', invalidating(w, sf.DOC))])
    w.M = w.repo.derive(w.M, {sf.DOC: w.repo.read(w.M, sf.DOC).replace(b'changed on main', b'repaired on main')},
                        parents=[w.M], subject='repair')
    rep = w.record(record_id='syn-repair')
    land(w, [(RD2 + 'repair.json', rep)], 'the repair record')
    run(BLOCK[9], w)
    # 11: a new configuration version whose ledger still carries the edit unchanged
    w = World(r, variant=lambda w_: {'extra': {'version': 2}})
    land(w, [(RD + 'finding.json', invalidating(w, sf.DOC))])
    run(BLOCK[10], w)
    # 12: the same entry with verdict no-effect
    w = World(r)
    land(w, [(RD + 'finding.json', w.record(record_id='syn-no-effect'))])
    run(BLOCK[11], w)
    # 13: a revised plan whose ledger rewords the edit (same id, same old line); the finding names the edit as the
    # original plan worded it. Amendment 4 keys the block by the edit id, so the block stays (the row's expectation
    # predates amendment 4)
    orig = rcmod.edit_key(World(r).led, 'E1')
    w = World(r, edits=EDITS_REWORDED)
    f13 = invalidating(w, sf.DOC)
    f13['paths'][0]['scientific_effect']['invalidated'][0]['sha256'] = orig
    land(w, [(RD + 'finding.json', f13)])
    run(BLOCK[12], w)
    # 14: a revised plan whose ledger no longer carries the edit (another edit, another id), finding and repair on M
    w = World(r, edits=EDITS_OTHER, first_id=2)
    eff = dict(CONTROL_EFFECT, conclusions='none', verdict='invalidates',
               invalidated=[{'id': 'E1', 'sha256': rcmod.edit_key(World(r).led, 'E1')}])
    f14 = rcmod.draft(w.repo, w.ctx, w.syn.H, w.M, w.X, w.led, sf.DOC, scientific_effect=eff)
    f14.update(record_id='syn-finding-old-plan', author=sf.WRITER, supersedes=None, M=w.M, X=w.X)
    land(w, [(RD + 'finding.json', f14)])
    run(BLOCK[13], w)
    not_built = [BLOCK[5], BLOCK[6]]
    blocked_cases = [BLOCK[k] for k in (0, 1, 2, 3, 4, 7, 8, 9, 10)]
    ok = all(res[k]['exit'] == 20 and 'retirement-blocked' in res[k]['classes'] for k in blocked_cases) and \
        res[BLOCK[8]]['run_level'] == [sf.DOC] and res[BLOCK[0]]['doc_disposition'] == 'retirement-blocked' and \
        res[BLOCK[3]]['doc_reconciled'] and \
        'retirement-blocked' not in res[BLOCK[11]]['classes'] and \
        'retirement-blocked' not in res[BLOCK[13]]['classes']
    res['built_cases_hold'] = ok
    res['case_13_blocked'] = 'retirement-blocked' in res[BLOCK[12]]['classes']
    res['not_built'] = not_built
    ok = ok and not not_built and not res['case_13_blocked']
    check('RECON-BLOCK', 'a reviewed finding that a change invalidates a planned edit blocks the retirement (first '
          'kind of finding; amendment 4 keying by edit id)', 'each blocking case FAIL retirement-blocked; the '
          'countercases not blocked; the review-finding cases not built (a design decision is pending)', res, ok,
          cases=names)


# BLOCK-KEY and REASSESS-FORM (design r6 as amended by amendment 4: R6.RECON.26, R6.RECON.27, R6.CFG.4)
BK = ["the edit's wording changed in a revised configuration (new bytes or reason; the same id and target), no "
      "reassessment cited",
      "the edit id renamed in a revised configuration, the rename recorded under AGENTS.md sec. A.48 item 3",
      "the edit id renamed with no recorded migration (the target unchanged)",
      "a scientific repair landed on M, the original frozen configuration unchanged",
      "an applying reassessment exists on M, the original frozen configuration (which does not cite it) unchanged",
      "a revised configuration citing a reassessment whose edit_sha256 differs from the edit as now worded",
      "a configuration of the same retirement in a new config_id lineage, carrying the edit, citing no reassessment",
      "an unrecorded rename on a new H: the edit renumbered, start_H moved, its old bytes unchanged",
      "a retirement renamed (new name and Issue) in a configuration that supersedes the blocked plan",
      "two findings on one edit, the revised configuration citing an applying reassessment that names only one of "
      "them",
      "countercase: a revised configuration, frozen anew, citing an applying reassessment of the edit as now worded "
      "(positive)",
      "countercase: a revised configuration that removes the edit (neither its id, a migrated id nor its target "
      "remains), citing no reassessment (positive)"]
RF = ["a reassessment with no non-author review, or whose reviewer equals its author",
      "a reassessment naming no finding, or a path that holds no finding at M",
      "a reassessment whose repair names no commit on M's first-parent chain",
      "a reassessment with an empty re-derivation of the edit's justification",
      "a reassessment whose verdict is not no-effect",
      "a reassessment cited under kind reassessment but failing record lint (a schema error)",
      "a reassessment whose repair entry is absent from M, or has no accepting non-author review",
      "a reassessment whose reviewer is the author of the repair's reconciliation record entry"]
RA_PATH = 'syn/cfg/reassessment.json'
REPAIR_AUTHOR = 'session.fixture-writer-r'


def finding_world(r, variant=None, edits=None, two=False, first_id=1, extra_elems=None):
    """A World whose main carries the change, a landed finding on it (and with two=True a second one, in another
    reconciliation directory), then a repair of the change recorded by its own reviewed no-effect entry. Commit ids
    are content hashes, so the same construction in another World yields the same main commits."""
    w = World(r, variant=variant, edits=edits, first_id=first_id)
    orig = rcmod.edit_key(World(r).led, 'E1')
    f = invalidating(w, sf.DOC, edit='E1') if first_id == 1 else invalidating(World(r), sf.DOC)
    f['paths'][0]['scientific_effect']['invalidated'][0]['sha256'] = orig
    # the finding names the base world's configuration and target, so that the main commits are the same whatever
    # configuration variant cites a reassessment of it (the two-pass constructions below rely on this)
    base = invalidating(World(r), sf.DOC)
    f['paths'][0]['scientific_effect']['configuration'] = base['paths'][0]['scientific_effect']['configuration']
    if 'target' in base['paths'][0]['scientific_effect']['invalidated'][0]:
        f['paths'][0]['scientific_effect']['invalidated'][0]['target'] = \
            base['paths'][0]['scientific_effect']['invalidated'][0]['target']
    # the base world's configuration, which the finding names, lands on main so that it resolves (R6.RECON.33) and
    # the finding binds by its own Forms; an unresolvable configuration binds every configuration at run level (r13
    # Amendment 7, every-configuration binding)
    bw = World(r)
    w.M = w.repo.derive(w.M, {q: b for q, b in bw.files.items() if isinstance(b, bytes)}, parents=[w.M],
                        subject='the base configuration lands')
    if extra_elems:
        f['paths'][0]['scientific_effect']['invalidated'] += [dict(x) for x in extra_elems]
    docs = [(RD + 'finding.json', f)]
    if two:
        f2 = dict(f, record_id='syn-finding-two')
        docs.append((RD2 + 'finding-two.json', f2))
    land(w, docs)
    w.findings = [{'path': p, 'blob_sha256': sha(jb(d))} for p, d in docs]
    w.M = w.repo.derive(w.M, {sf.DOC: w.repo.read(w.M, sf.DOC).replace(b'changed on main', b'repaired on main')},
                        parents=[w.M], subject='repair')
    w.repair_commit = w.M
    rep = w.record(record_id='syn-repair', author=REPAIR_AUTHOR)
    rp = 'verification/audits/syn-repair/repair.json'
    land(w, [(rp, rep)], 'the repair record')
    w.repair_entry = {'path': rp, 'blob_sha256': sha(jb(rep))}
    return w


def reassessment(w, edit_sha=None, **upd):
    doc = {'schema': 'oi-reassessment/1', 'record_id': 'syn-reassessment', 'author': sf.WRITER, 'supersedes': None,
           'finding': dict(w.findings[0], item=sf.DOC),
           'repair': {'commits': [w.repair_commit], 'entry': dict(w.repair_entry, entry_path=sf.DOC)},
           'edit': {'id': 'E1', 'sha256': edit_sha or rcmod.edit_key(w.led, 'E1')},
           'rederivation': 'control fixture: the planned edit re-derived at the repaired state; the check re-run',
           'verdict': 'no-effect'}
    doc.update(upd)
    return doc


def cite(doc, reviewer=sf.REVIEWER, review=True):
    """A configuration variant citing the reassessment with kind reassessment, its review beside it."""
    def variant(w_):
        b = jb(doc)
        files = {RA_PATH: b}
        recs = [{'kind': 'reassessment', 'path': RA_PATH, 'blob_sha256': sha(b)}]
        if review:
            rv = jb({'schema': rec.review_schema, 'reviewer': reviewer,
                     'reviewed': {'path': RA_PATH, 'blob_sha256': sha(b)}, 'method': 'read',
                     'verdicts': [{'item': i, 'verdict': 'accept'} for i in rec.item_ids(doc)]})
            files[RA_PATH[:-5] + '.review.json'] = rv
            recs.append({'kind': 'review', 'path': RA_PATH[:-5] + '.review.json', 'blob_sha256': sha(rv)})
        return {'files': files, 'add_records': recs}
    return variant


def bk_controls(r, check):
    res, names, rf, rnames = {}, [], {}, []

    def run(store, nm, name, w):
        code, out = w.run([], harness=True)
        inv = [i for i in (out or {}).get('items', []) if i['class'] == 'record-invalid' and i.get('subject') == RA_PATH]
        store[name] = {'exit': code, 'classes': classes(out),
                       'blocked': [i.get('subject') for i in (out or {}).get('items', [])
                                   if i['class'] == 'retirement-blocked'],
                       'reassessment_invalid': [d for i in inv for d in (i.get('detail') or [])][:1],
                       'reassessments': ((out or {}).get('category3') or {}).get('reassessments')}
        nm.append((name, {}))

    def revised(mk, two=False, reviewer=sf.REVIEWER, review=True, edits=EDITS_REWORDED):
        # two passes: the first World gives the finding, the repair commit and entry the reassessment names (the
        # main commits and records do not depend on the configuration); the second cites it
        w1 = finding_world(r, edits=edits, two=two)
        return finding_world(r, variant=cite(mk(w1), reviewer, review), edits=edits, two=two)

    run(res, names, BK[0], finding_world(r, edits=EDITS_REWORDED))
    run(res, names, BK[3], finding_world(r))
    run(res, names, BK[4], finding_world(r))  # the original configuration cites nothing
    run(res, names, BK[5], revised(lambda w1: reassessment(w1, edit_sha='0' * 64)))
    run(res, names, BK[6], finding_world(r, variant=lambda w_: {'extra': {'config_id': 'synthetic-other-lineage'}}))
    run(res, names, BK[8], finding_world(r, variant=lambda w_: {'extra': {'retirement': {'name': 'renamed',
                                                                                         'issue': 'other'}}}))
    run(res, names, BK[9], revised(lambda w1: reassessment(w1), two=True))
    run(res, names, BK[10], revised(lambda w1: reassessment(w1)))
    run(res, names, BK[11], finding_world(r, edits=EDITS_OTHER, first_id=2))
    not_built = [BK[1], BK[2], BK[7]]
    blocked = [BK[k] for k in (0, 3, 4, 5, 6, 8, 9)]
    built_ok = all(res[k]['exit'] == 20 and 'retirement-blocked' in res[k]['classes'] for k in blocked) and \
        'retirement-blocked' not in res[BK[10]]['classes'] and not res[BK[10]]['reassessment_invalid'] and \
        res[BK[10]]['reassessments'] and 'retirement-blocked' not in res[BK[11]]['classes'] and \
        res[BK[5]]['reassessment_invalid'] and not res[BK[9]]['reassessment_invalid']
    res['built_cases_hold'] = built_ok
    res['not_built'] = not_built
    check('BLOCK-KEY', 'the block is keyed by the edit id; wording changes and repairs do not lift it; a revised plan '
          'proceeds by removing the edit or citing an applying reassessment', 'each blocking case FAIL '
          'retirement-blocked; the two countercases not blocked; the migration and target cases not built (a design '
          'decision is pending)', res, built_ok and not not_built, cases=names)

    # REASSESS-FORM: a revised configuration citing a reassessment that fails one condition keeps the block
    def bad(case, mk, reviewer=sf.REVIEWER, review=True):
        run(rf, rnames, case, revised(mk, reviewer=reviewer, review=review))
    bad(RF[0], lambda w1: reassessment(w1), review=False)
    bad(RF[1], lambda w1: reassessment(w1, finding={'path': RD + 'none.json', 'blob_sha256': '0' * 64}))
    bad(RF[2], lambda w1: reassessment(w1, repair={'commits': ['0' * 40], 'entry': w1.repair_entry}))
    bad(RF[3], lambda w1: reassessment(w1, rederivation=''))
    bad(RF[4], lambda w1: reassessment(w1, verdict='invalidates'))
    # a field error of the record (no supersedes field), which record lint refuses; an unknown schema id is a
    # configuration error instead (CONFIG_INVALID, sec. 16.2)
    bad(RF[5], lambda w1: {k: v for k, v in reassessment(w1).items() if k != 'supersedes'})
    bad(RF[6], lambda w1: reassessment(w1, repair={'commits': [w1.repair_commit],
                                                   'entry': {'path': 'verification/audits/x/none.json',
                                                             'blob_sha256': '0' * 64}}))
    bad(RF[7], lambda w1: reassessment(w1), reviewer=REPAIR_AUTHOR)
    run(rf, rnames, 'restored', revised(lambda w1: reassessment(w1)))
    neg = [k for k in rf if k != 'restored']
    ok = all(rf[k]['exit'] == 20 and 'retirement-blocked' in rf[k]['classes'] and
             ('record-invalid' in rf[k]['classes']) for k in neg) and \
        'retirement-blocked' not in rf['restored']['classes'] and 'record-invalid' not in rf['restored']['classes']
    check('REASSESS-FORM', "a cited reassessment's form, review and citation are checked; a failure keeps the block",
          'each case FAIL record-invalid for the reassessment and retirement-blocked; restored: neither', rf, ok,
          cases=rnames)


# RECON-SCI (design r6 as amended by amendment 3: R6.RECON.25, R6.RECON.1), as op C runs through the post-freeze
# route, so that the review-dependent cases are record lint at admission
SCI_CORPUS_PY = 'doc/check.py'


def sci_world(r):
    """A World whose corpus also holds doc/*.py (an executed path), changed on main in its own commit."""
    w = World(r, variant=lambda w_: {'extra': {'corpus': {'patterns': [r'^doc/[^/]+\.md$', r'^doc/[^/]+\.py$']}}})
    w.M = w.repo.derive(w.M, {SCI_CORPUS_PY: b'print("synthetic check")\n'}, parents=[w.M], subject='executed path')
    return w


def sci_controls(r, check):
    from ledger_coverage.adapters import recon_controls as rcc
    SCI = rcc.SCI
    res, names = {}, []

    def run(name, w, docs, review=None, binding_path=None):
        files = {}
        for path, doc in docs:
            data = jb(doc)
            files[path] = data
            files[path[:-5] + '.review.json'] = (review or w.review)(path, data)
        rv = w.rev(files)
        code, out = w.run(['%s:%s' % (rv, p) for p, _d in docs], harness=True)
        bp = binding_path or docs[0][0]
        bad = any(i['class'] == 'record-invalid' and (i.get('subject') == bp or
                                                      str(i.get('subject', '')).startswith(bp + ':'))
                  for i in (out or {}).get('items', []))
        res[name] = {'exit': code, 'classes': classes(out), 'invalid': bad, 'admitted': admitted(out, bp),
                     'why': [d for i in (out or {}).get('items', []) if i['class'] == 'record-invalid'
                             and str(i.get('subject', '')).startswith(bp) for d in
                             (i.get('detail') if isinstance(i.get('detail'), list) else [i.get('detail')])][:2]}
        names.append((name, {'record': bp}))

    def py_rec(w, eff):
        d = rcmod.draft(w.repo, w.ctx, w.syn.H, w.M, w.X, w.led, SCI_CORPUS_PY, scientific_effect=eff)
        d.update(record_id='syn-py', author=sf.WRITER, supersedes=None, M=w.M, X=w.X)
        return d

    def both(w, py_eff=None, doc_mut=None):
        """The two drifted paths of sci_world, each with its own record (the ledgered one first)."""
        a = w.record()
        if doc_mut is not None:
            doc_mut(a)
        b = py_rec(w, py_eff or dict(CONTROL_EFFECT, method='control: the check re-run at the composed blob %s'
                                     % _l_of(w)))
        return [(RD + 'doc.json', a), (RD2 + 'py.json', b)]

    w = sci_world(r)
    run(SCI[0], w, both(w, doc_mut=lambda d: d['paths'][0].pop('scientific_effect', None)))
    w = sci_world(r)
    run(SCI[1], w, both(w, doc_mut=lambda d: d['paths'][0].update(
        scientific_effect=dict(CONTROL_EFFECT, conclusions=['NO-SUCH-EDIT']))))
    w = sci_world(r)
    run(SCI[2], w, both(w, doc_mut=lambda d: d['paths'][0].update(scientific_effect=dict(CONTROL_EFFECT, method=''))))
    w = sci_world(r)

    def rejecting(path, data, reviewer=sf.REVIEWER):
        doc = json.loads(data)
        return jb({'schema': rec.review_schema, 'reviewer': reviewer, 'reviewed': {'path': path,
                                                                                   'blob_sha256': sha(data)},
                   'method': 'read every object the record names',
                   'verdicts': [{'item': i, 'verdict': 'reject' if i.endswith(':scientific_effect') else 'accept'}
                                for i in rec.item_ids(doc)]})
    run(SCI[3], w, both(w), review=rejecting)
    w = sci_world(r)
    run(SCI[4], w, both(w), review=lambda p, d: w.review(p, d, reviewer=sf.WRITER))
    w = sci_world(r)
    run(SCI[5], w, both(w, doc_mut=lambda d: d['paths'][0]['scientific_effect'].pop('verdict')))
    w = sci_world(r)
    run(SCI[6], w, both(w, py_eff=dict(CONTROL_EFFECT, method='control: nothing re-run')),
        binding_path=RD2 + 'py.json')
    # restored: a valid entry of an unledgered corpus path whose conclusions name an edit id of another path
    w = sci_world(r)
    run('restored', w, both(w, py_eff=dict(CONTROL_EFFECT, conclusions=['E1'],
                                           method='control: the check re-run at the composed blob %s' % _l_of(w))),
        binding_path=RD2 + 'py.json')
    neg = [k for k in res if k != 'restored']
    ok = all(res[k]['exit'] == 20 and res[k]['invalid'] for k in neg) and res['restored']['admitted'] and \
        not res['restored']['invalid']
    check('RECON-SCI', "scientific verification is the reviewer's: the tool checks the form of each entry's "
          'scientific_effect and its review', 'each case record-invalid for the record; restored admitted', res, ok,
          cases=names)


def _l_of(w):
    """The composed blob l of the executed path at w's main (its bytes at M: an unledgered corpus path)."""
    return w.repo.blob_id(w.M, SCI_CORPUS_PY)
