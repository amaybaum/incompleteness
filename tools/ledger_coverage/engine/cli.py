"""Command line, stages and result assembly (sec. 2.1, 5)."""
import argparse
import hashlib
import json
import os
import posixpath
import re
import subprocess
import sys

from . import config as cfgmod
from . import context as ctxmod
from . import delegation as delmod
from . import execution as exmod
from . import outcome as oc
from . import peredit
from . import profiles as prmod
from . import pipeline as pl
from . import reconcile as rcmod
from . import recon_route
from . import category3 as c3
from . import findings as fd
from . import records as rec
from . import rules as rulemod
from . import util
from . import checker
from . import host as hostmod
from .. import record_authority
from .gitobj import GitRepo, Overlay, Unresolvable, first_parent_chain, full_id, regular_modes

here = os.path.dirname(os.path.abspath(__file__))


class UsageError(Exception):
    pass


class Parser(argparse.ArgumentParser):
    def error(self, message):
        raise UsageError(message)

    def exit(self, status=0, message=None):
        raise UsageError(message or 'exit')

    def print_help(self, file=None):
        raise UsageError('help requested:\n' + self.format_help())


def build_parser():
    p = Parser(prog='ledger_coverage.py', add_help=True)
    sub = p.add_subparsers(dest='op')

    def common(sp):
        sp.add_argument('--config', required=True, help='F:path of the configuration record')
        sp.add_argument('--freeze', default=None, help='the plan commit F, a full id (sec. 6.3)')
        sp.add_argument('--out', required=True)
        sp.add_argument('--repo', default=None)

    r = sub.add_parser('record')
    common(r)
    r.add_argument('--pin', required=True)
    r.add_argument('--record', required=True)
    c = sub.add_parser('coverage')
    common(c)
    c.add_argument('--commit', required=True)
    c.add_argument('--segment', action='append', default=[])
    c.add_argument('--hp', action='append', default=[])
    c.add_argument('--classify', action='append', default=[])
    c.add_argument('--check', action='append', default=[])
    c.add_argument('--final', action='store_true')
    e = sub.add_parser('execution')
    common(e)
    e.add_argument('--scientific-base', required=True)
    e.add_argument('--candidate', required=True)
    e.add_argument('--certified', default=None)
    e.add_argument('--main', default=None)
    e.add_argument('--record-base', default=None)
    e.add_argument('--landing', default=None)
    e.add_argument('--ledger', required=True)
    e.add_argument('--edits', default=None)
    e.add_argument('--delegation', default=None)
    e.add_argument('--evidence', default=None)
    e.add_argument('--classify', action='append', default=[])
    t = sub.add_parser('terms')
    common(t)
    t.add_argument('--commit', required=True)
    t.add_argument('--base', default=None)
    t.add_argument('--ledger', default=None)
    t.add_argument('--profile', default=None)
    t.add_argument('--check', default=None)
    t.add_argument('--final', action='store_true')
    t.add_argument('--scope', default=None)
    t.add_argument('--rules', action='append', default=[])
    t.add_argument('--classify', action='append', default=[])
    rp = sub.add_parser('replay')
    rp.add_argument('--snapshot', required=True, help='a committed landing record (oi-ledger-landing/1)')
    rp.add_argument('--out', required=True)
    rp.add_argument('--repo', default=None)
    cu = sub.add_parser('custody', help='the R6.CUST.10 gate check of the OBL-29 custody record at a commit')
    cu.add_argument('--commit', required=True)
    cu.add_argument('--out', required=True)
    cu.add_argument('--repo', default=None)
    s = sub.add_parser('self-test')
    s.add_argument('--out', required=True)
    s.add_argument('--repo', default=None)
    z = sub.add_parser('purity-lint')
    z.add_argument('--out', required=True)
    z.add_argument('--repo', default=None)
    z.add_argument('--config', default=None, help='commit:path of a configuration whose values and profiles are linted')
    return p


def out_guard(out, repo_path):
    real = os.path.realpath(out)
    if os.path.exists(real):
        if not os.path.isdir(real) or os.listdir(real):
            raise UsageError('--out must not exist or must be an empty directory')
    trees = []
    if repo_path:
        r = subprocess.run(['git', '-C', repo_path, 'worktree', 'list', '--porcelain'], capture_output=True,
                           text=True)
        for line in r.stdout.splitlines():
            if line.startswith('worktree '):
                trees.append(os.path.realpath(line[9:]))
    for t in trees:
        if real == t or real.startswith(t.rstrip('/') + '/'):
            raise UsageError('--out lies inside a worktree of the repository: %s' % t)
    return real


def engine_identity():
    files = {}
    for name in sorted(os.listdir(here)):
        if name.endswith('.py') or name.endswith('.json'):
            with open(os.path.join(here, name), 'rb') as f:
                files['engine/' + name] = util.sha256(f.read())
    sdir = os.path.join(here, 'schemas')
    if os.path.isdir(sdir):
        for name in sorted(os.listdir(sdir)):
            with open(os.path.join(sdir, name), 'rb') as f:
                files['engine/schemas/' + name] = util.sha256(f.read())
    entry = os.path.join(os.path.dirname(os.path.dirname(here)), 'ledger_coverage.py')
    if os.path.exists(entry):
        with open(entry, 'rb') as f:
            files['entry'] = util.sha256(f.read())
    return {'blob_sha256': util.sha256(util.canonical(files)), 'modules': files}


def split_ref(s):
    if ':' not in s:
        raise UsageError('expected rev:path, got %r' % s)
    a, b = s.split(':', 1)
    return a, b


def resolve(repo, rev):
    """A role commit: a full 40-hex id read through the verified reader; a ref name is never resolved (GV1)."""
    try:
        return repo.resolve(rev)
    except Unresolvable as exc:
        raise oc.Stop(oc.error, 'UNRESOLVABLE', str(exc))


# ---- records used by a run ------------------------------------------------------------------------------

class RecordSet:
    def __init__(self, loaded, harness):
        self.loaded = loaded
        self.harness = harness
        self.used = []
        self.items = []

    def admit(self, repo, refspec, kind):
        """A record named on the command line: read from the object store; admitted only through the chain."""
        rev, path = split_ref(refspec)
        commit = resolve(repo, rev)
        try:
            data = repo.read(commit, path)
        except Unresolvable as exc:
            self.items.append(oc.make_item('RECORD', 'record-invalid', path, None, {'why': 'not a regular file'},
                                           detail=str(exc)))
            return None
        if data is None:
            raise oc.Stop(oc.error, 'SOURCE_CHANGED', 'record %s not present at %s' % (path, commit[:12]))
        sha = util.sha256(data)
        doc = json.loads(data.decode('utf-8'))
        ref = {'path': path, 'blob_sha256': sha}
        self.used.append(dict(ref, kind=kind))
        if self.harness:
            doc['_ref'] = ref
            return doc
        if sha not in self.loaded.admitted:
            self.items.append(oc.make_item('RECORD', 'record-invalid', path, None,
                                           {'sha': sha, 'why': 'not referenced by the configuration'},
                                           detail='a record not referenced by the frozen configuration is never '
                                                  'used for a decision'))
            return None
        st = self.loaded.store
        if st.get(ref) is None:
            st.by_sha[sha] = (path, doc)
        probs = rec.lint_chain(ref, st, self.loaded.admitted)
        if probs:
            self.items.append(oc.make_item('RECORD', 'record-invalid', path, None, {'sha': sha, 'why': probs[0]},
                                           detail=probs))
            return None
        doc['_ref'] = ref
        return doc


def rule_files(loaded, harness, ctx_lookup):
    """Admitted allow rules and rule-file items (sec. 6.2, 6.3)."""
    items = []
    allow = []
    seen_ids = {}
    for ref, doc in loaded.rule_files:
        if doc is None or doc.get('schema') != rulemod.rules_schema:
            items.append(oc.make_item('RECORD', 'record-invalid', ref['path'], None, {'why': 'schema'}))
            continue
        # record lint runs in every admission mode, the control harness included (design r6, OBL-28 C-29)
        probs = rec.lint_chain(ref, loaded.store, loaded.admitted)
        sup = doc.get('supersedes')
        old_rules = {}
        od = None
        if sup:
            # the predecessor is read from the object store at or before F (sec. 6.3, DI-2)
            od = loaded.store.resolve(sup)
            if od is None:
                probs.append('broken supersedes chain')
            else:
                old_rules = {r['id']: r for r in od.get('rules', [])}
        for r in doc.get('rules', []):
            other = seen_ids.get(r['id'])
            if other is not None and other != ref['path'] and not (sup and sup.get('path') == other):
                probs.append('rule id %s reused' % r['id'])
            seen_ids[r['id']] = ref['path']
            if r.get('kind') == peredit.params_kind:
                src = ctx_lookup['checker']()
                lint = r.get('lint') or {}
                try:
                    sp = prmod.extract(
                        'python-ast-call-arg', {'function': lint.get('sentence_function'),
                                                'call': lint.get('sentence_call'), 'arg': 0}, src) if src else None
                except Exception as exc:  # an extraction fault is a lint failure of the params rule
                    sp = None
                    probs.append('%s: splitter not extractable: %s' % (r['id'], exc))
                probs += peredit.lint_params(r, src, sp)
                probs += peredit.check_examples(r, ctx_lookup['profiles']())
                continue
            probs += rulemod.lint_rule(r, ctx_lookup['profile'], ctx_lookup['sentence'], ctx_lookup['deny'],
                                       ctx_lookup['control_input'])
        widen = rulemod.file_widening(od, doc)
        wp = rec.widening_review_problems(ref, loaded.store, loaded.admitted, rec.reviewers_of(ref, loaded.store),
                                          doc.get('author'), sup, widen) if widen else []
        if wp and (not harness or ctx_lookup.get('force_widening')):
            probs.append('widening without a valid widening review (%s): %s' % ('; '.join(widen[:3]), wp[0]))
        if probs:
            items.append(oc.make_item('RECORD', 'record-invalid', ref['path'], None, {'why': probs[0]},
                                      detail=probs[:20]))
            continue
        allow += [r for r in doc.get('rules', []) if r.get('kind') == 'allow']
    return allow, items


# ---- the run -------------------------------------------------------------------------------------------

def category3(a, repo, cfg, loaded, H, M, led, recon, route_cands, ex, result, records):
    # design r6 R6.RECON.26 (findings of the first kind) and R6.RECON.27
    """Scan M's tree, the records the run reads and the scanned sets of F's tree and of each record commit the run
    names; block the run where a finding applies and no reassessment the configuration cites lifts it."""
    pinned = (cfg['roles'].get('side_change_classes') or {}) if isinstance(cfg.get('roles'), dict) else {}
    pinned_doc = loaded.store.get(pinned) if pinned.get('path') else None
    F = resolve(repo, a.freeze) if a.freeze else None
    scope = recon_route.Scope(repo, H, M, None, F, records.harness, pinned_doc,
                              posixpath.dirname(split_ref(a.config)[1]), led['files'], lambda p: False, [])
    schemas = rcmod.reconciliation_schemas
    # R6.OBL29.4: the presence-based discharge conditions (the repair's current entry and review) read M's scan with
    # its existing selector
    m_scan = recon_route.scanned(repo, M, scope)
    # R6.OBL29.1, .2, .5, .7: detection reads the cumulative record set over every tree reachable through any parent
    # from M, F and each named REV, with the fixed selector, plus the records the run reads
    revs = sorted({c[1] for c in route_cands})
    try:
        cum = c3.Cumulative(repo, [M] + ([F] if F else []) + revs, schemas, recon_route.audits_root)
        # the records the run reads explicitly: reconciliation records, and the review records the configuration
        # references (R6.OBL29.1)
        explicit_reviews = []
        for r_ in cfg['records']:
            d_ = loaded.store.get(r_) if isinstance(r_, dict) else None
            if isinstance(d_, dict) and d_.get('schema') == rec.review_schema:
                explicit_reviews.append(dict(d_, _ref={'path': r_['path'], 'blob_sha256': r_['blob_sha256']},
                                             _source=loaded.ref['commit']))

        def explicit_at(ref):
            for r_ in recon:
                if r_.get('_ref') == {'path': (ref or {}).get('path'), 'blob_sha256': (ref or {}).get('blob_sha256')}:
                    return {k: v for k, v in r_.items() if k not in ('_ref', '_source')}
            return None
        found = c3.unique(cum.findings() + c3.findings_of_records(
            recon + explicit_reviews, schemas, lambda ref: cum.record_at(ref) or explicit_at(ref)))
    except Unresolvable as exc:
        raise oc.Stop(oc.error, 'UNRESOLVABLE', 'the cumulative record set cannot be read: %s' % exc)
    out = []
    # the ordinary malformed-nonfinding lint of the current snapshot at M (R6.OBL29.2, R6.RECON.35): a class (b) or
    # (c) file without an invalidation signal, with the existing selector (tool-landing prefixes and the plan's record
    # directory excluded unless the run reads the file)
    read_paths = {(r.get('_ref') or {}).get('path') for r in recon}
    for path in cum.malformed_at(M, lambda q: q not in read_paths and (
            any(q.startswith(x) for x in scope.prefixes) or (scope.plan_dir and q.startswith(scope.plan_dir)))):
        out.append(oc.make_item('RECORD', 'record-invalid', path, None, {'why': 'malformed record'},
                                detail=['a malformed record (R6.RECON.35 class (b) or (c)) at M']))
    anchors = [F] if F else (revs or [M])
    rcache = {}

    def resolve_cfg(ref):
        """R6.RECON.33: a configuration reference resolves at the newest commit on the anchor's first-parent chain
        whose tree holds the path with a blob of that sha256."""
        key = (ref.get('path'), ref.get('blob_sha256'))
        if key not in rcache:
            rcache[key] = None
            for anchor in anchors:
                c = anchor
                while c and rcache[key] is None:
                    try:
                        b = repo.read(c, ref['path'])
                    except Unresolvable:
                        b = None
                    if b is not None and util.sha256(b) == ref['blob_sha256']:
                        try:
                            rcache[key] = (json.loads(b.decode('utf-8')), c)
                        except (ValueError, UnicodeDecodeError):
                            pass
                        break
                    ps = repo.parents(c)
                    c = ps[0] if ps else None
        return rcache[key]

    def ledger_of(ref, commit):
        try:
            other = cfgmod.load(repo, commit, ref['path'], ref['blob_sha256'], None, 'harness')
            return load_adapter_input(repo, other, 'ledger')
        except Exception as exc:  # any failure to read the named configuration's ledger
            raise fd.Unsettled('Form (ii): the ledger of a named configuration other than the run\'s cannot be read '
                               '(%s); the design does not say what follows' % exc)
    findings = []
    blocked = []
    bound = {}

    def fkey(f):
        return ((f['record'] or {}).get('path'), (f['record'] or {}).get('blob_sha256'), f['kind'], f.get('item'),
                f['path'])
    try:
        bview = c3.Binding(repo, M, cfg, {'path': loaded.ref['path'], 'blob_sha256': loaded.ref['blob_sha256']}, led,
                           resolve_cfg, ledger_of, record_at=lambda ref: cum.record_at(ref) or explicit_at(ref),
                           cfg_commit=loaded.ref['commit'])
        for f in found:
            present, wit = cum.witness(f['record'] or {}, M, revs, F)
            entry = f.get('entry')
            if not isinstance(entry, dict) or not isinstance(entry.get('side_change_commits'), list):
                # a malformed finding, or one with no readable entry: a run-level block (owner decision 5 of
                # 2026-11-27), with FAIL record-invalid; its evidence and provenance stay in the result
                form = list(f.get('form') or []) + ['the finding has no readable entry with side_change_commits; it '
                                                    'blocks at run level']
                bound[fkey(f)] = ([], True, form, present)
            else:
                applies = c3.in_m(repo, M, entry['side_change_commits'])
                edits, run_level, form = c3.bind(f, bview) if applies else ([], False, list(f.get('form') or []))
                bound[fkey(f)] = (edits, run_level, form, present)
            findings.append({'record': f['record'], 'item': f.get('item'), 'kind': f['kind'], 'path': f['path'],
                             'class': f.get('class'), 'present_at_M': present, 'witness': wit})
    except fd.Unsettled as exc:
        raise oc.Stop(oc.error, 'DESIGN_UNSETTLED', str(exc))
    except Unresolvable as exc:
        raise oc.Stop(oc.error, 'UNRESOLVABLE', 'a category-3 input cannot be read: %s' % exc)
    # OBL-29 custody (R6.CUST.1-.9): checked at effective M whenever the configuration cites a reassessment
    custody = None
    if any(isinstance(r, dict) and r.get('kind') == 'reassessment' for r in cfg['records']):
        from .. import record_authority as ra_
        from . import custody as cust
        try:
            chk = cust.Check(repo, M, F, ra_.custody_path, ra_.custody_bootstrap_blob, cum, recon_route.audits_root,
                             cfgmod.read_pin_table, recon_route.audits_root)
            chk.tool_landing_id = ra_.tool_landing_class_id
            chk.ledger_files = context_ledger_files(repo)

            def load_context_config(f_, cref_):
                return cfgmod.load(repo, f_, cref_['path'], cref_['blob_sha256'], None, 'harness')
            chk.replayer = lambda c_, m_, rev_: c3.replay_run(repo, c_, m_, rev_, load_context_config, schemas,
                                                              recon_route.audits_root)
            custody = chk.run()
        except fd.Unsettled as exc:
            raise oc.Stop(oc.error, 'DESIGN_UNSETTLED', str(exc))
        except cust.Unimplemented as exc:
            raise oc.Stop(oc.error, 'NOT_IMPLEMENTED', str(exc))
        except Unresolvable as exc:
            raise oc.Stop(oc.error, 'UNRESOLVABLE', 'a custody object cannot be read: %s' % exc)
        for p_ in custody.get('problems') or []:
            out.append(oc.make_item('RECORD', 'record-invalid', ra_.custody_path, None,
                                    {'custody': p_['item'], 'why': p_['why']},
                                    detail=['%s: %s' % (p_['item'], p_['why'])]))
    applying = []
    for r in cfg['records']:
        if r.get('kind') != 'reassessment':
            continue
        d = loaded.store.get(r)
        probs = c3.reassessment_problems(repo, M, led, d, r, loaded.store, loaded.admitted, found, m_scan, schemas,
                                         cum, run_level=lambda f: bound.get(fkey(f), ([], False))[1],
                                         custody=custody)
        if probs:
            out.append(oc.make_item('RECORD', 'record-invalid', r['path'], None,
                                    {'sha': r.get('blob_sha256'), 'why': probs[0]}, detail=probs))
        else:
            applying.append((d, r))
    # r9 sec. 2.2 over the witnesses custody supplies (R6.CUST.6): a discharge blocked by one is inapplicable
    if custody is not None and custody.get('status') == 'established' and chk.witnesses and applying:
        try:
            wblocked, rows = c3.custody_decisions(repo, chk.witnesses, applying, loaded, m_scan, cum, schemas)
        except Unresolvable as exc:
            raise oc.Stop(oc.error, 'UNRESOLVABLE', 'a custody witness input cannot be read: %s' % exc)
        custody['decisions'] = rows
        gone = set()
        for (d_, r_), W, clauses in wblocked:
            gone.add(id(r_))
            wr = c3.witness_report(W)
            out.append(oc.make_item('RECORD', 'record-invalid', r_['path'], None,
                                    {'sha': r_.get('blob_sha256'), 'why': 'blocked by a custody witness',
                                     'witness': wr},
                                    detail=['blocked by the %s witness of context %s, run %s, against %s (%s): '
                                            'clauses %s' % (W['kind'], W['context'], W['run'],
                                                            W['disputed'].get('path'),
                                                            ', '.join(x['path'] for x in wr['forming']),
                                                            ', '.join(clauses))],
                                    witness=wr))
        applying = [(d_, r_) for d_, r_ in applying if id(r_) not in gone]
    lifted = c3.lifting(applying)
    wit_of = {fkey(f): x['witness'] for f, x in zip(found, findings)}
    for f in found:
        edits, run_level, form, present = bound[fkey(f)]
        hits = [e for e in edits if not lifted(f, e)]
        if run_level and not lifted(f, None):
            hits.append(None)
        for e in hits:
            blocked.append((f, e))
        # a form failure: FAIL record-invalid for a finding present at M, and for a historical-only finding while it
        # binds and lacks an applying discharge (R6.OBL29.2)
        if form and (present or hits):
            out.append(oc.make_item('RECORD', 'record-invalid', (f['record'] or {}).get('path'), None,
                                    {'finding': f['record'], 'item': f.get('item'), 'why': form[0]},
                                    detail=['a form failure of a category-3 finding: %s' % x for x in form],
                                    # its evidence and provenance (owner decision 5): the record's path and blob, its
                                    # kind and detection class, and the witness commit that supplies it
                                    evidence={'finding': f['record'], 'item': f.get('item'), 'kind': f['kind'],
                                              'class': f.get('class'), 'source': wit_of.get(fkey(f))}))
    out += c3.blocked_items(repo, H, M, blocked, getattr(ex, 'dispositions', []))
    explicit = [{'path': (r.get('_ref') or {}).get('path'), 'blob_sha256': (r.get('_ref') or {}).get('blob_sha256'),
                 'source': r.get('_source')} for r in recon + explicit_reviews]
    result['category3_read_domain'] = cum.read_domain(explicit)
    result['category3'] = {'custody': custody if custody is not None else {'status': 'not-required'},
                           'findings': findings,
                           'blocked': [{'record': f['record'], 'item': f.get('item'), 'path': f['path'], 'edit': e}
                                       for f, e in blocked],
                           'reassessments': [r for _d, r in applying]}
    return out


def run(argv, repo=None, harness=False, stderr=None, extra_records=(), preflight_fn=None, control=None,
        environ=None):
    """Returns (exit status, result dict or None). Nothing is written except under --out. A harness run (an
    in-process control) writes control-result.json with "harness": true, never result.json (X11)."""
    stderr = stderr if stderr is not None else sys.stderr
    try:
        a = build_parser().parse_args(argv)
        if not a.op:
            raise UsageError('a subcommand is required')
        repo_path = getattr(a, 'repo', None) or os.getcwd()
        out = out_guard(a.out, repo_path if repo is None or isinstance(repo, GitRepo) else None)
        if a.op in ('self-test', 'purity-lint'):
            from . import selftest
            return selftest.cli(a, out)
        if a.op == 'replay':
            from . import replay
            return replay.cli(a, out, repo, stderr)
        if a.op == 'custody':
            return custody_gate(a, out, repo, repo_path, argv)
        if getattr(a, 'final', False) and not getattr(a, 'check', None):
            raise UsageError('--final requires --check')
    except UsageError as exc:
        msg = {'schema': oc.result_schema, 'outcome': oc.usage, 'exit_status': 64, 'message': str(exc)}
        stderr.write(json.dumps(msg, sort_keys=True) + '\n')
        return 64, None
    result = {'schema': oc.result_schema, 'operation': a.op, 'engine': engine_identity(), 'preflight': [],
              'record_checks': None, 'items': [], 'invocation': invocation(argv)}
    if harness or (control or {}).get('host') is not None:
        result['harness'] = True
    try:
        if repo is None:
            try:
                repo = Overlay(GitRepo(repo_path))
            except Unresolvable as exc:
                raise oc.Stop(oc.error, 'UNRESOLVABLE', str(exc))
        try:
            res = stages(a, repo, harness, result, extra_records, preflight_fn, control or {},
                         os.environ if environ is None else environ)
        except util.EncodingFault as exc:
            raise oc.Stop(oc.error, 'ENCODING', str(exc))
        except Unresolvable as exc:
            raise oc.Stop(oc.error, 'UNRESOLVABLE', str(exc))
    except oc.Stop as s:
        if s.outcome == oc.usage:
            stderr.write(json.dumps({'schema': oc.result_schema, 'outcome': oc.usage, 'exit_status': 64,
                                     'message': s.message}, sort_keys=True) + '\n')
            return 64, None
        result.update(outcome=s.outcome, exit_status=oc.exit_codes[s.outcome],
                      stop={'class': s.cls, 'message': s.message, 'detail': s.detail})
        oc.annotate(result)
        write(out, result, harness)
        return result['exit_status'], result
    oc.annotate(res)
    write(out, res, harness)
    return res['exit_status'], res


def invocation(argv):
    """The arguments that decide the result, without --out (for the offline replay)."""
    out, skip = [], False
    for x in argv:
        if skip:
            skip = False
            continue
        if x in ('--out', '--repo'):
            skip = True
            continue
        if x.startswith('--out=') or x.startswith('--repo='):
            continue
        out.append(x)
    return out


def context_ledger_files(repo):
    """files(context) -> the set of ledgered paths of a custody context's configuration, read at its freeze through
    the configuration's own ledger adapter (R6.RECON.1), or None when they cannot be read."""
    def files(c_):
        try:
            other = cfgmod.load(repo, c_['f'], c_['config']['path'], c_['config']['blob_sha256'], None, 'harness')
            led = load_adapter_input(repo, other, 'ledger')
            return set((led.get('files') or {}).keys())
        except Exception:  # an unreadable ledger leaves the directory undecided (custody-run-shape)
            return None
    return files


def custody_gate(a, out, repo, repo_path, argv):
    """R6.CUST.10: at the commit under check as M, R6.CUST.2 for the version in its tree, R6.CUST.4, the mechanical
    parts of R6.CUST.5 (c1) for freeze entries, (c3), (c4)'s second clause and (c5), the second and third clauses of
    (c2), and R6.CUST.8; it does not require a close for every context and establishes nothing for a run. Exit 0 when
    every clause holds, 20 with record-invalid items otherwise, 65 on an unreadable object or an unsettled clause."""
    from .. import record_authority as ra_
    from . import custody as cust
    res = {'schema': oc.result_schema, 'operation': 'custody', 'engine': engine_identity(), 'preflight': [],
           'record_checks': None, 'items': [], 'invocation': invocation(argv)}
    try:
        if repo is None:
            repo = Overlay(GitRepo(repo_path))
        M = resolve(repo, a.commit)
        cum = c3.Cumulative(repo, [M], rcmod.reconciliation_schemas, recon_route.audits_root)
        chk = cust.Check(repo, M, None, ra_.custody_path, ra_.custody_bootstrap_blob, cum, recon_route.audits_root,
                         cfgmod.read_pin_table, recon_route.audits_root)
        chk.tool_landing_id = ra_.tool_landing_class_id
        chk.ledger_files = context_ledger_files(repo)
        rep = chk.run(gate=True)
        # the gate checks (c4)'s second clause only (an unfrozen entry names a discharge-bearing configuration): the
        # first clause's "unaccounted for" failures are dropped. The pin-rule failure ("the only cover of a
        # configuration pinned after it") is kept, although R6.CUST.10's text names only (c4)'s second clause: a
        # deliberate, stricter choice (an entry the pin rule refuses can never be repaired once it lands, R-C4),
        # put to the owner
        rep['problems'] = [p for p in rep['problems'] if not (p['item'] == 'custody-incomplete' and
                                                              'unaccounted for' in p['why'])]
        rep['status'] = 'established' if not rep['problems'] else 'unestablished'
        res['custody'] = rep
        res['items'] = oc.sort_items([oc.make_item('RECORD', 'record-invalid', ra_.custody_path, None,
                                                   {'custody': p['item'], 'why': p['why']},
                                                   detail=['%s: %s' % (p['item'], p['why'])])
                                      for p in rep['problems']])
        outc = oc.compute(res['preflight'], None, res['items'])
    except (fd.Unsettled, cust.Unimplemented) as exc:
        res['stop'] = {'class': 'DESIGN_UNSETTLED', 'message': str(exc)}
        outc = oc.error
    except Unresolvable as exc:
        res['stop'] = {'class': 'UNRESOLVABLE', 'message': str(exc)}
        outc = oc.error
    res['outcome'] = outc
    res['exit_status'] = oc.exit_codes[outc]
    write(out, res)
    return res['exit_status'], res


def write(out, result, harness=False):
    os.makedirs(out, exist_ok=True)
    mode = ((result.get('config') or {}).get('admission') or {}).get('mode')
    name = 'control-result.json' if harness or result.get('harness') else \
        'replay-result.json' if mode == 'replay' else 'result.json'
    with open(os.path.join(out, name), 'w', encoding='utf-8') as f:
        f.write(util.dump_result(result))


def admission(a, repo, harness, control, crev, cpath, environ):
    """Sec. 6.3: configuration admission from F, then execution identity. Returns (admission, table) for config.load,
    `table` being the blobs F's pin table admits ({path: bytes}). Outside the harness every failure refuses as a
    configuration-unreviewed error, before anything is evaluated; a run outside a host job never reaches "chain"
    (point 3)."""
    def refuse(msg, **d):
        raise oc.Stop(oc.error, 'CONFIG_UNREVIEWED', msg, d)
    if control.get('replay_snapshot') is not None:
        snap = control['replay_snapshot']
        if not a.freeze or a.freeze != snap.get('freeze') or crev != a.freeze:
            refuse('the replay names another plan commit than its snapshot')
        F, table, admitted, pt_ref, _ = freeze_admission(repo, a.freeze, crev, cpath, refuse)
        if pt_ref != snap.get('pin_table'):
            refuse('the pin table at F differs from the snapshot\'s')
        return {'mode': 'replay', 'snapshot': snap}, admitted
    sim = control.get('host')
    if harness and sim is None:
        return {'mode': 'control-harness'}, None
    if not a.freeze:
        refuse('no --freeze: the configuration is admitted only from the plan commit F (sec. 6.3)',
               simulated_host=sim is not None)
    F, table, admitted, pt_ref, cfg = freeze_admission(repo, a.freeze, crev, cpath, refuse)
    if sim is not None:
        # an in-process control on an in-memory host: the whole of sec. 6.3 runs, the result is a control artefact
        # (control-harness, with the simulated snapshot), never "chain"
        host, run_id, read_repo = sim, control.get('run_id'), control.get('repo_id')
        checkout = control['checkout'] if 'checkout' in control else None
    else:
        det = hostmod.RestHost.detect(environ)
        if det is None:
            refuse('a run outside a host CI job cannot reach chain admission (configuration admission point 3)')
        host, run_id, read_repo = det
        checkout = disk_checkout(refuse)
    snap = execution_identity(host, run_id, read_repo, repo, cfg, checkout, refuse, simulated=sim is not None)
    review = [p for p, b in sorted(admitted.items()) if _reviews(b, cpath, util.sha256(table_bytes(admitted, cpath)))]
    snap.update(freeze=F, pin_table=pt_ref,
                configuration={'path': cpath, 'blob_sha256': util.sha256(table_bytes(admitted, cpath))},
                configuration_review=[{'path': p, 'blob_sha256': util.sha256(admitted[p])} for p in review])
    if sim is not None:
        return {'mode': 'control-harness', 'simulated_chain': {'host': 'in-memory control host',
                                                               'snapshot': snap}}, admitted
    return {'mode': 'chain', 'snapshot': snap}, admitted


def table_bytes(admitted, path):
    return admitted.get(path) or b''


def _reviews(b, path, sha):
    try:
        d = json.loads(b.decode('utf-8'))
    except (ValueError, UnicodeDecodeError):
        return False
    return isinstance(d, dict) and d.get('schema') == rec.review_schema and \
        d.get('reviewed') == {'path': path, 'blob_sha256': sha}


def freeze_admission(repo, freeze, crev, cpath, refuse):
    """Configuration admission points 1-2: F a full id read through the verified reader; the configuration read only
    from F's tree; the pin table derived from the plan's file of record pins beside it (its last Record pins
    subsection), listing the configuration and its review record with their sha256. Returns (F, table, admitted blobs,
    pin table {path, blob_sha256}, the configuration as parsed)."""
    try:
        F = repo.resolve(full_id(freeze))
    except Unresolvable as exc:
        refuse('the plan commit F cannot be read: %s' % exc)
    if crev != F:
        refuse('the configuration is read from F only (--config F:path)')
    rec_dir = cpath.rsplit('/', 1)[0] + '/' if '/' in cpath else ''
    prereg = rec_dir + 'PREREG.md'
    try:
        data = repo.read(F, cpath)
        pt = repo.read(F, prereg)
    except Unresolvable as exc:
        refuse('a configuration admission read failed: %s' % exc)
    if data is None:
        refuse('no configuration at %s in F' % cpath)
    if pt is None:
        refuse('no file of record pins beside the configuration in F: %s' % prereg)
    try:
        table = cfgmod.read_pin_table(pt)
    except cfgmod.PinTableError as exc:
        refuse('the pin table cannot be read: %s' % exc)
    if table.get(cpath[len(rec_dir):]) != util.sha256(data):
        refuse('the last Record pins subsection of %s has no row with the configuration and its sha256' % prereg)
    admitted = cfgmod.admitted_by_table(repo, F, rec_dir, table)
    if not any(_reviews(b, cpath, util.sha256(data)) for b in admitted.values()):
        refuse('no review record of the configuration is listed in the pin table of %s' % prereg)
    try:
        cfg = json.loads(data.decode('utf-8'))
    except (ValueError, UnicodeDecodeError) as exc:
        refuse('the configuration cannot be read: %s' % exc)
    if not isinstance(cfg, dict) or cfgmod.tool_problems(cfg.get('tool'), cfg.get('repository_id')):
        refuse('the configuration\'s tool pins or repository id cannot be read')
    return F, table, admitted, {'path': prereg, 'blob_sha256': util.sha256(pt)}, cfg


def disk_checkout(refuse):
    """{path: bytes} of the entry point and every file under the tool's package directory in the checkout the tool
    runs from, read without following a link; a non-regular entry, or a parent that is not a real directory, refuses
    (execution identity point 2)."""
    entry, pkg = cfgmod.tool_layout()
    pkg_dir = os.path.dirname(here)
    root = os.path.dirname(os.path.dirname(pkg_dir))
    out = {}
    d = pkg_dir
    while d != root:
        if os.path.islink(d) or not os.path.isdir(d):
            refuse('%s is not a real directory in the checkout' % d)
        d = os.path.dirname(d)

    def walk(p, rel):
        if os.path.islink(p):
            refuse('a non-regular entry in the checkout: %s' % rel)
        if os.path.isdir(p):
            with os.scandir(p) as it:
                names = sorted(e.name for e in it)
            for n in names:
                walk(os.path.join(p, n), rel + '/' + n)
        elif os.path.isfile(p):
            with open(p, 'rb') as f:
                out[rel] = f.read()
        else:
            refuse('a non-regular entry in the checkout: %s' % rel)
    try:
        walk(os.path.join(root, entry), entry)
        walk(pkg_dir, pkg.rstrip('/'))
    except OSError as exc:
        refuse('the checkout cannot be read: %s' % exc)
    return out


def execution_identity(host, run_id, read_repo, repo, cfg, checkout, refuse, simulated=False):
    """Sec. 6.3, execution identity points 1, 2, the `uses:` rule of point 5, and point 6. Returns the snapshot's run
    and tool fields. `checkout` is {path: bytes} of the checkout the tool runs from (None in a control: T's own
    files)."""
    try:
        run = host.run_record(run_id, read_repo)
    except hostmod.HostUnavailable as exc:
        refuse('the run record cannot be read: %s' % exc, simulated_host=simulated)
    keys = ('repository_id', 'head_repository_id', 'event', 'head_branch', 'workflow_path', 'head_sha')
    if not isinstance(run, dict) or any(run.get(k) is None for k in keys):
        refuse('the run record cannot be read or is incomplete', simulated_host=simulated)
    rid = cfg['repository_id']
    if run['repository_id'] != rid or run['head_repository_id'] != rid:
        refuse('the run\'s repository or head repository is not the configuration\'s repository_id (point 1)')
    if run['event'] not in ('push', 'workflow_dispatch'):
        refuse('the run\'s event %r is not push or workflow_dispatch (point 1)' % run['event'])
    if run['head_branch'] != 'main':
        refuse('the run\'s head branch is not main (point 6)')
    try:
        T = repo.resolve(full_id(run['head_sha']))
        ents = repo.entries(T)
    except Unresolvable as exc:
        refuse('the tool commit T cannot be read: %s' % exc)
    entry, pkg = cfgmod.tool_layout()
    pins = {f['path']: f['blob_sha256'] for f in cfg['tool']['files']}
    mine = {p: e for p, e in ents.items() if p == entry or p.startswith(pkg)}
    if set(mine) != set(pins):
        refuse('T\'s tool files differ from the configuration\'s tool.files (point 2)',
               extra=sorted(set(mine) - set(pins))[:20], missing=sorted(set(pins) - set(mine))[:20])
    blobs = {}
    for p in sorted(mine):
        if mine[p][0] not in regular_modes:
            refuse('%s is not a regular file at T (point 2)' % p)
        try:
            blobs[p] = repo.read(T, p)
        except Unresolvable as exc:
            refuse('a tool file at T cannot be read: %s' % exc)
        if util.sha256(blobs[p]) != pins[p]:
            refuse('%s at T differs from its tool pin (point 2)' % p)
    wf = cfg['tool']['workflow']
    if run['workflow_path'] != wf['path']:
        refuse('the run\'s workflow path is not tool.workflow.path (point 2)')
    try:
        wfb = repo.read(T, wf['path'])
    except Unresolvable as exc:
        refuse('the workflow at T cannot be read: %s' % exc)
    if wfb is None or util.sha256(wfb) != wf['blob_sha256']:
        refuse('the workflow at T differs from tool.workflow (point 2)')
    bad = checker.uses_line_problems(wfb)
    if bad:
        refuse('the workflow at T fails the uses: line rule (point 5): line %d, %s' % bad[0])
    if checkout is None:
        checkout = blobs
    if set(checkout) != set(blobs) or any(checkout[p] != blobs[p] for p in blobs):
        refuse('the checkout the tool runs from differs from T\'s tool files (point 2)',
               differs=sorted(set(checkout) ^ set(blobs) | {p for p in blobs if checkout.get(p) != blobs[p]})[:20])
    return {'run': {k: run[k] for k in ('run_id',) + keys if k in run}, 'tool_commit': T,
            'tool_blobs': {p: util.sha256(b) for p, b in sorted(blobs.items())},
            'workflow': {'path': wf['path'], 'blob_sha256': util.sha256(wfb)}}


def stages(a, repo, harness, result, extra_records, preflight_fn, control, environ):
    # admission (sec. 6.3), then integrity: configuration, adapters, profiles, records
    crev, cpath = split_ref(a.config)
    adm, table = admission(a, repo, harness, control, crev, cpath, environ)
    if getattr(a, 'record_base', None) is not None and (adm.get('mode') == 'chain' or adm.get('simulated_chain')):
        # amendment 4: the record base of a predicted M is a control-harness input only; refused before the
        # configuration load and the preflight, so that USAGE takes precedence (sec. 7)
        raise oc.Stop(oc.usage, 'USAGE', '--record-base in a chain-admitted run')
    loaded = cfgmod.load(repo, crev, cpath, None, a.op, 'harness' if harness else 'chain', extra_records, adm, table)
    cfg = loaded.config
    rec_adm = dict(loaded.admission)
    result['config'] = {'config_id': cfg['config_id'], 'version': cfg['version'], 'path': cpath,
                        'commit': loaded.ref['commit'], 'blob_sha256': loaded.ref['blob_sha256'],
                        'admission': rec_adm}
    if getattr(loaded, 'transition', None):
        t = loaded.transition
        result['transition'] = {'descriptor': t['descriptor'], 'base': t['base'], 'tips': t['tips'],
                                'prior': t['prior']}
    result['adapters'] = loaded.adapter_records
    result['profiles'] = loaded.profile_records
    result['rule_files'] = [{'path': r['path'], 'blob_sha256': r['blob_sha256']} for r, _ in loaded.rule_files]
    result['hp_merges'] = cfg['hp_obligations']
    # controls
    from . import selftest
    pf = (preflight_fn or selftest.preflight)()
    result['preflight'] = pf
    if any(not p['passed'] for p in pf):
        raise oc.Stop(oc.void, 'PREFLIGHT_FAILED', 'a preflight control failed', {'failed': [p['id'] for p in pf
                                                                                              if not p['passed']]})
    if getattr(a, 'record_base', None) is not None:
        result.setdefault('inputs', {})['record_base'] = a.record_base
    records = RecordSet(loaded, harness)
    indicators = ctxmod.Indicators(cfg['indicators'])
    ctx = pl.RunContext(repo, cfg, loaded.profiles, [], {}, indicators)
    lookup = lookups(ctx, loaded)
    if harness and control.get('overrides'):
        loaded.control_overrides = control['overrides']
        result['control'] = 'adapter output replaced in memory by the control: %s' % sorted(control['overrides'])
    if harness and control.get('without_allow_rules'):
        loaded.rule_files = [(r, d) for r, d in loaded.rule_files
                             if not any(x.get('kind') == 'allow' for x in (d or {}).get('rules', []))]
        result['control'] = 'allow-rule files withheld (a "no records" control)'
    if harness and control.get('replace_rule_files') is not None:
        loaded.rule_files = control['replace_rule_files'](loaded.rule_files)
        result['control'] = 'rule files replaced in memory by the control'
    lookup['force_widening'] = bool(harness and control.get('force_widening'))
    allow, rule_items = rule_files(loaded, harness and not control.get('lint_chain'), lookup)
    ctx.allow_rules = allow
    bad = {i['subject'] for i in rule_items}
    ctx.edit_params = peredit.find_params([(r, d) for r, d in loaded.rule_files if r['path'] not in bad])
    loaded.ctx = ctx
    items = list(rule_items)
    op = a.op
    if op == 'record':
        body = op_record(a, repo, ctx, loaded, result)
    elif op == 'coverage':
        body = op_coverage(a, repo, ctx, loaded, records, result)
    elif op == 'terms':
        body = op_terms(a, repo, ctx, loaded, records, result)
    else:
        body = op_execution(a, repo, ctx, loaded, records, result, control)
    items += body + records.items
    if getattr(a, 'final', False):
        chk = ctx.check(a.check[0] if isinstance(a.check, list) else a.check)
        if chk is None or not chk.get('final_profiles'):
            raise oc.Stop(oc.usage, 'USAGE', '--final with a check that has no final profiles')
        items = oc.apply_final(items, chk['final_profiles'])
    items = oc.sort_items(items)
    result['records_used'] = sorted(records.used, key=lambda r: (r['path'], r['blob_sha256']))
    result['items'] = items
    result['finding_counts'] = counts(items)
    outc = oc.compute(result['preflight'], result['record_checks'], items)
    result['outcome'] = outc
    result['exit_status'] = oc.exit_codes[outc]
    finish_snapshot(result)
    return result


def finish_snapshot(result):
    """The evaluated commits and the delegated evidence enter the admission snapshot, then its own sha256."""
    adm = result.get('config', {}).get('admission') or {}
    snap = adm.get('snapshot') or (adm.get('simulated_chain') or {}).get('snapshot')
    if snap is None:
        return
    if adm.get('mode') == 'replay':
        adm['snapshot_sha256'] = util.fingerprint(snap)
        return
    snap['evaluated'] = result.get('roles') or result.get('evaluated')
    snap['delegated_evidence'] = (result.get('delegation') or {}).get('evidence_record')
    snap['invocation'] = result.get('invocation')
    adm['snapshot_sha256'] = util.fingerprint(snap)


def counts(items):
    c = {}
    for i in items:
        k = '%s/%s/%s' % (i['obligation'], i['decision'], i['class'])
        c[k] = c.get(k, 0) + 1
    return dict(sorted(c.items()))


def lookups(ctx, loaded):
    controls = loaded.controls or {}
    inputs = {i['id']: i for i in controls.get('control_inputs', [])}

    def profile(name):
        return ctx.profiles.get(name)

    def sentence(commit, path, sha):
        if ctx.repo.blob_id(commit, path) is None:
            return None
        sents = ctx.sentences(commit, path)
        for k, (s, _, _) in enumerate(sents):
            if util.sha256(s) == sha:
                neigh = [sents[j][0] for j in (k - 1, k + 1) if 0 <= j < len(sents)]
                return s, neigh, rulemod.sentence_context_sha(sents, k)
        return None

    def control_input(cc):
        if 'control_input' in cc:
            spec = inputs.get(cc['control_input'])
            if spec is None:
                return None
            data = ctx.repo.read(spec['commit'], spec['path'])
            if data is None or util.sha256(data) != spec['sha256']:
                return None
            lines = util.lines_of(data.decode('utf-8'))
        else:
            data = ctx.repo.read(cc['commit'], cc['path'])
            if data is None:
                return None
            lines = util.lines_of(data.decode('utf-8'))
        if 'sentence_line' in cc:
            for s, a, b in util.sentences_of(lines, ctx.abbrev, ctx.splitter):
                if a == cc['sentence_line']:
                    return s
            return None
        return lines[cc['line'] - 1] if 0 < cc['line'] <= len(lines) else None

    deny = [p for p in ctx.profiles.values() if p.kind == 'deny' and p.applies_to == 'tree']

    def checker():
        led = (loaded.config.get('adapters') or {}).get('ledger') or {}
        for c in led.get('companion', []):
            if c.get('role') == 'checker':
                return cfgmod.read_ref(ctx.repo, c.get('commit') or loaded.ref['commit'],
                                       {'path': c['path'], 'blob_sha256': c['blob_sha256']}, 'checker companion')
        return None
    return {'profile': profile, 'sentence': sentence, 'control_input': control_input, 'deny': deny,
            'checker': checker, 'profiles': lambda: ctx.profiles}


def declared_sites(repo, loaded):
    """Sites declared in the configuration (no site map): located at the pin by their unique line hash."""
    cfg = loaded.config
    pin = cfg['roles']['pin']
    out = []
    for s in cfg.get('sites', []):
        data = repo.read(pin, s['file'])
        lines = util.lines_of(util.decode(data, s['file'])) if data is not None else []
        hits = [i for i, l in enumerate(lines) if util.sha256(l) == s['line_sha256']]
        if len(hits) != 1:
            raise oc.Stop(oc.error, 'CONFIG_INCONSISTENT', 'declared site %s is not unique at the pin' % s['site_id'])
        out.append({'file': s['file'], 'line': hits[0] + 1, 'carried': s['carried'],
                    'context_field_value': s[cfg['context_mapping']['source_field']], 'quote': None})
    return {'pin': pin, 'sites': out, 'override_anchors': {}, 'read_entries': [], 'errors': []}


def load_adapter_input(repo, loaded, iface, rev_path=None):
    """Reads an adapter's main input and companions by their pins; returns the adapter's output."""
    ov = getattr(loaded, 'control_overrides', {}).get(iface)
    if ov is not None:
        return ov
    if iface == 'sitemap' and loaded.config['adapters'].get('sitemap') is None and 'sites' in loaded.config:
        return declared_sites(repo, loaded)
    spec = loaded.config['adapters'][iface]
    if spec is None:
        raise oc.Stop(oc.error, 'CONFIG_UNSUPPORTED', 'no %s adapter configured' % iface)
    if rev_path:
        rev, path = split_ref(rev_path)
        commit = resolve(repo, rev)
        if path != spec['path']:
            raise oc.Stop(oc.error, 'SOURCE_CHANGED', '%s path differs from the configuration' % iface)
    else:
        commit = spec.get('commit') or loaded.ref['commit']
    data = cfgmod.read_ref(repo, commit, {'path': spec['path'], 'blob_sha256': spec['blob_sha256']}, iface)
    comps = {}
    for c in spec.get('companion', []):
        ccommit = c.get('commit') or commit
        comps[c['role']] = cfgmod.read_ref(repo, ccommit, {'path': c['path'], 'blob_sha256': c['blob_sha256']},
                                           '%s companion %s' % (iface, c['role']))
    out = loaded.modules[iface].load(data, comps, lambda c, p: repo.read(c, p))
    errs = out.get('errors', [])
    if errs:
        kind = errs[0][0]
        cls = 'SOURCE_CHANGED' if kind in ('schema', 'correspondence') else 'EDITS_HASH_MISMATCH' \
            if kind == 'edits_sha256' else 'LEDGER_INTEGRITY'
        detail = {'errors': [e[1] for e in errs[:20]]}
        if kind == 'correspondence' and getattr(loaded, 'ctx', None) is not None:
            # the per-edit result of items 5 and 6 is computed and recorded even on a refusal (sec. 6.1, C4)
            rec_, _ = peredit.evaluate(out, loaded.ctx.edit_params, loaded.ctx.profiles)
            detail['per_edit'] = rec_
        raise oc.Stop(oc.error, cls, errs[0][1], detail)
    return out


def per_edit(ctx, led, result):
    rec_, items = peredit.evaluate(led, getattr(ctx, 'edit_params', None), ctx.profiles)
    if rec_ is not None:
        result['per_edit'] = rec_
    return items


# ---- op A ------------------------------------------------------------------------------------------------

def op_record(a, repo, ctx, loaded, result):
    cfg = loaded.config
    pin = resolve(repo, a.pin)
    rc = resolve(repo, a.record)
    sm = load_adapter_input(repo, loaded, 'sitemap')
    if pin != sm['pin'] or pin != cfg['roles'].get('pin'):
        raise oc.Stop(oc.error, 'PIN_MISMATCH', 'the pin is not the record\'s pin',
                      {'expected_pin': sm['pin'], 'candidate': pin})
    rp = cfg['adapters']['replay']
    rdir = rp['module_path'].rsplit('/', 1)[0]
    if repo.tree_id(rc, rdir) != rp['record_tree']:
        raise oc.Stop(oc.error, 'RECORD_TREE_MISMATCH', 'record tree differs at the record commit')
    out_root = os.path.join(os.path.realpath(a.out), 'replay')
    os.makedirs(out_root, exist_ok=True)

    class Reader:
        def __call__(self, commit, path):
            return repo.read(commit, path)

        def listing(self, commit, dirs):
            res = []
            for d in dirs:
                files = [(p, repo.read_blob(b)) for p, b in sorted(repo.paths(commit).items())
                         if p.startswith(d + '/')]
                res.append((d, files))
            return res

    rr = loaded.modules['replay'].replay(Reader(), pin, rc, rp['module_path'], ctx.corpus(pin), out_root)
    sites = pl.build_sites(_with_sitemap(ctx, sm))
    pin_findings = []
    for s in sites:
        if s['pin_count'] != 1:
            pin_findings.append('%s: pin line not unique' % s['site_id'])
    for key, anchor in sm.get('override_anchors', {}).items():
        f, ln = key.rsplit(':', 1)
        if anchor is not None:
            lines = ctx.ft(pin, f).lines
            if not (0 < int(ln) <= len(lines)) or anchor not in lines[int(ln) - 1]:
                pin_findings.append('%s: override anchor not in its pin line' % key)
    holds = all(e['equal'] for e in rr['equalities']) and not rr['errors'] and rr['self_test'] and \
        not pin_findings and len(rr['equalities']) == 5
    anchors = [{'site_id': s['site_id'], 'anchor_sha256': s['anchor_sha256'], 'pin_count': s['pin_count'],
                'ordinal': s['ordinal'], 'context_sha256': s['pin_context_sha256']} for s in sites]
    result['record_checks'] = {'holds': holds, 'equalities': rr['equalities'], 'errors': rr['errors'],
                               'frozen_self_test': rr['self_test'], 'ck_errors': rr.get('ck_errors'),
                               'extended_unmapped': rr.get('extended_unmapped'), 'pin_findings': pin_findings,
                               'anchors': len(anchors), 'anchors_sha256': util.fingerprint(anchors)}
    result['covered_paths'] = ctx.corpus(pin)
    return []


def _with_sitemap(ctx, sm):
    ctx.sitemap = sm
    return ctx


# ---- op B ------------------------------------------------------------------------------------------------

def parse_segments(a, repo, ctx, loaded, commit):
    cfg = loaded.config
    pin = cfg['roles']['pin']
    specs = a.segment or (['%s..%s' % (pin, commit)] if commit != pin else [])
    segs = []
    for s in specs:
        led = None
        if '=' in s:
            rng, lref = s.split('=', 1)
        else:
            rng, lref = s, None
        if '..' not in rng:
            raise UsageError('segment must be from..to')
        f, t = rng.split('..', 1)
        f, t = resolve(repo, f), resolve(repo, t)
        seg = {'from': f, 'to': t}
        hp = [o for o in cfg['hp_obligations'] if o['segment'] == [f, t]]
        if lref:
            led = load_adapter_input(repo, loaded, 'ledger', lref)
            pl.check_ledger(repo, f, led)
            seg.update(kind='ledgered', ledger=led)
        elif hp:
            chain = first_parent_chain(repo, f, t)
            if chain is None:
                raise oc.Stop(oc.error, 'CONFIG_INCONSISTENT', 'HP segment endpoints not on one first-parent chain')
            par = {}
            prev = f
            for c in chain:
                par[c] = prev
                prev = c
            seg.update(kind='hp', chain=chain, parent_of=par, merges={m['commit'] for m in hp[0]['merges']},
                       obligation='HP')
        else:
            seg.update(kind='unledgered')
        segs.append(seg)
    return segs


def op_coverage(a, repo, ctx, loaded, records, result):
    commit = resolve(repo, a.commit)
    result['evaluated'] = {'commit': commit}
    sm = load_adapter_input(repo, loaded, 'sitemap')
    ctx.sitemap = sm
    for f in ctx.corpus(commit):
        ctx.ft(commit, f)
    try:
        segs = parse_segments(a, repo, ctx, loaded, commit)
    except UsageError as exc:
        raise oc.Stop(oc.usage, 'USAGE', str(exc))
    hp_recs, ctx_recs, hit_recs = [], [], []
    for r in a.hp:
        d = records.admit(repo, r, 'hp')
        if d is not None:
            hp_recs += [dict(x, _ref=d['_ref']) for x in d.get('sites', [])]
    for r in a.classify:
        d = records.admit(repo, r, 'classification')
        if d is None:
            continue
        if d.get('schema') == 'oi-context-adjudication/1':
            ctx_recs += d.get('entries', [d])
        else:
            hit_recs += [dict(x, _ref=d['_ref']) for x in d.get('classifications', [d])]
    # R6.RECON.33 for coverage (A1 staging amendment r2, sec. 1): exactly one explicit --check naming a check of the
    # admitted configuration; a missing, repeated or unknown selection is USAGE. No default check exists.
    if len(a.check) != 1:
        raise oc.Stop(oc.usage, 'USAGE', 'coverage takes exactly one --check (%d given)' % len(a.check))
    chk = ctx.check(a.check[0])
    if chk is None:
        raise oc.Stop(oc.usage, 'USAGE', 'unknown check %s' % a.check[0])
    cv = pl.Coverage(ctx, commit, segs, chk, {'hp': hp_recs, 'context': ctx_recs}, hit_recs).run()
    items = list(cv.items)
    review = [ctx.profiles[n] for n in chk['profiles'] if ctx.profiles[n].kind == 'review'
              and ctx.profiles[n].applies_to == 'tree']
    led_segs = [s for s in segs if s['kind'] == 'ledgered']
    added = {}
    if led_segs:
        added = pl.added_lines(ctx, commit, led_segs[-1]['ledger'], ctx.corpus(commit))
    deny = [] if commit in ctx.retired_form_trees else \
        [p for p in ctx.profiles.values() if p.kind == 'deny']
    held = pl.held_lines(cv.states)
    region_info = hit_regions(ctx, cv, segs, commit)
    prior_unheld = set()
    pin_unheld = set()
    if segs:
        prior = segs[-1]['from']
        if len(cv.snapshots) > 1:
            prior_held = cv.snapshots[-2][1]
        else:
            prior_held = {(st.site['file'], st.site['pin_lineno']): st.site['site_id'] for st in cv.states}
        pt = pl.Terms(ctx, prior, review, [], hit_records=())
        pt.review(held=prior_held)
        prior_unheld = {(h['file'], ctx.ft(prior, h['file']).lines[h['line'] - 1]) for h in pt.hits
                        if h['state'] != 'PASS'}
        pin = ctx.config['roles']['pin']
        pz = pl.Terms(ctx, pin, review, [], hit_records=())
        pz.review(held={(st.site['file'], st.site['pin_lineno']): 1 for st in cv.states})
        pin_unheld = {(h['file'], ctx.ft(pin, h['file']).lines[h['line'] - 1]) for h in pz.hits
                      if h['state'] != 'PASS'}
    stexts = pl.splice_texts(ctx, led_segs[-1]['from'], commit, led_segs[-1]['ledger']) if led_segs else None
    tm = pl.Terms(ctx, commit, review + [p for p in ctx.profiles.values() if p.kind == 'review'
                                         and p.applies_to == 'added-text' and p.name in chk['profiles']],
                  deny, added=added, hit_records=hit_recs, check=chk, splice_texts=stexts)
    tm.deny()
    if led_segs and any(p.applies_to == 'added-text' for p in deny):
        items += per_edit(ctx, led_segs[-1]['ledger'], result)
    seg_name = segs[-1]['name'] if segs else None
    for h_key in list(region_info):
        region_info[h_key].setdefault('segment', seg_name)
    # pre-existing attribution for unheld hits outside replacement images
    ri = dict(region_info)
    for path in ctx.corpus(commit):
        lines = ctx.ft(commit, path).lines
        for ln, l in enumerate(lines, 1):
            if (path, ln) in ri or (path, ln) in held:
                continue
            if (path, l) in prior_unheld:
                origin_hp = any(s['kind'] == 'hp' for s in segs[:-1]) and (path, l) not in pin_unheld
                ri[(path, ln)] = {'pre_existing': True, 'segment': seg_name,
                                  'obligation': 'HP' if origin_hp else 'TERMS'}
            elif segs and segs[-1]['kind'] == 'hp':
                ri[(path, ln)] = {'pre_existing': False, 'segment': seg_name, 'obligation': 'HP'}
    tm.review(held=held, region_info=ri)
    tm.stale_rules() if ctx.allow_rules else None
    items += tm.items
    result['sites'] = sorted((dict({k: v for k, v in so.items() if k != 'provenance_adjudicated'},
                                   state=site_state(so)) for so in cv.site_out.values()), key=lambda s: s['site_id'])
    result['hits'] = sorted(tm.hits, key=lambda h: (h['file'], h['line']))
    result['file_conformance'] = getattr(cv, 'file_conformance', [])
    result['segments'] = [{'name': s['name'], 'from': s['from'], 'to': s['to'], 'kind': s['kind']} for s in segs]
    result['site_counts'] = site_counts(cv)
    result['hit_counts'] = hit_counts(tm.hits)
    result['merger_groups'] = [list(x) for x in getattr(cv, 'merger_groups', [])]
    if led_segs:
        rl = cv.region_lines.get(led_segs[-1]['name'], set())
        result['region_lines'] = {'segment': led_segs[-1]['name'], 'count': len(rl)}
    result['profiles_evaluated'] = {commit: sorted({p.name for p in tm.review_profiles} |
                                                   {p.name for p in deny})}
    result['covered_paths'] = ctx.corpus(commit)
    return items


def hit_regions(ctx, cv, segs, commit):
    """Line attribution at the commit: replacement images (with the replaced-region test) and historical regions."""
    info = {}
    led_segs = [s for s in segs if s['kind'] == 'ledgered']
    if led_segs:
        seg = led_segs[-1]
        led = seg['ledger']
        imgs = pl.image_lines(ctx, commit, led, ctx.corpus(commit))
        by_id = {sp['id']: sp for sp in led['splices']}
        for path, lines in imgs.items():
            frm = ctx.ft(seg['from'], path)
            for ln, ids in lines.items():
                parts = []
                for i in ids:
                    sp = by_id[i]
                    a = util.line_of_offset(frm.data, sp['start']) - 1
                    b = util.line_of_offset(frm.data, max(sp['start'], sp['end'] - 1)) - 1
                    parts.extend(frm.lines[a:b + 1])
                info[(path, ln)] = {'class': None, 'splices': sorted(ids), 'from_region': '\n'.join(parts),
                                    'segment': seg['name'], 'obligation': 'TERMS'}
    for st in cv.states:
        if st.hp and getattr(st, 'region_found', False) and not getattr(st, 'adjudicated', False) and \
                not cv.site_out[st.site['site_id']]['hp_overlap']:
            occ = ctx.ft(commit, st.file).occurrences(st.block) if st.block else []
            if len(occ) == 1:
                for k in range(len(st.block)):
                    info[(st.file, occ[0] + 1 + k)] = {'class': 'unclassified', 'obligation': 'HP',
                                                       'segment': cv.segments[0]['name'] if cv.segments else None,
                                                       'hp_site': st.site['site_id']}
    return info


# design r6, R6.PIPE.7 (unresolved) and R6.HP.7 (provenance-adjudicated)
def site_state(so):
    """A site's state: unresolved for a site that tracking cannot locate (it stays unresolved in later segments);
    provenance-adjudicated for a site its HP adjudication resolves (distinct from every segment status); else its
    last segment status."""
    last = so['statuses'][-1]['status'] if so['statuses'] else None
    # an authorized removal and an HP site keep their own state (an HP site's region is decided by its walk)
    if 'current' in so and so['current'] is None and last != 'authorized-removal' and not so.get('hp_steps'):
        return 'unresolved'
    if so.get('provenance_adjudicated'):
        return 'provenance-adjudicated'
    return so['statuses'][-1]['status'] if so['statuses'] else ('hp' if so.get('hp_steps') else 'unchanged')


def site_counts(cv):
    c = {}
    for so in cv.site_out.values():
        last = site_state(so)
        c[last] = c.get(last, 0) + 1
    return dict(sorted(c.items()))


def hit_counts(hits):
    c = {}
    for h in hits:
        k = h['state'] + ('/' + h['cls'] if h.get('cls') else '')
        c[k] = c.get(k, 0) + 1
    return dict(sorted(c.items()))


# ---- op D ------------------------------------------------------------------------------------------------

def op_terms(a, repo, ctx, loaded, records, result):
    commit = resolve(repo, a.commit)
    result['evaluated'] = {'commit': commit}
    if a.profile and a.check:
        raise oc.Stop(oc.usage, 'USAGE', '--profile and --check are exclusive')
    if a.check:
        chk = ctx.check(a.check)
        if chk is None:
            raise oc.Stop(oc.usage, 'USAGE', 'unknown check %s' % a.check)
        names = chk['profiles']
    elif a.profile:
        names = [n.strip() for n in a.profile.split(',') if n.strip()]
        chk = None
    else:
        # no check is defined as a default (R6.RECON.33: `default_for` is CONFIG_INVALID); the terms syntax without
        # --check or --profile stays as it was for a configuration without a default (staging r2 leaves it open)
        chk = None
        names = [p for p in ctx.profiles]
    for n in names:
        if n not in ctx.profiles:
            raise oc.Stop(oc.usage, 'USAGE', 'unknown profile %s' % n)
    profs = [ctx.profiles[n] for n in names]
    added = {}
    stexts = None
    if a.base or a.ledger:
        if not (a.base and a.ledger):
            raise oc.Stop(oc.usage, 'USAGE', '--base and --ledger go together')
        base = resolve(repo, a.base)
        led = load_adapter_input(repo, loaded, 'ledger', a.ledger)
        if led['base'] != base:
            raise oc.Stop(oc.error, 'SCIENTIFIC_BASE_MISMATCH', 'ledger base is not --base')
        if commit != base:
            added = pl.added_lines(ctx, commit, led, ctx.corpus(commit))
            stexts = pl.splice_texts(ctx, base, commit, led)
            if any(p.applies_to == 'added-text' and p.kind == 'deny' for p in profs):
                records.items.extend(i for i in per_edit(ctx, led, result)
                                     if set(i.get('profiles', [])) <= set(names))
    scope_paths = None
    if any(p.spec.get('scope') == 'repo' for p in profs):
        if not a.scope:
            raise oc.Stop(oc.usage, 'USAGE', 'a repo-scoped profile needs --scope')
        sd = records.admit(repo, a.scope, 'scope')
        if sd is None:
            scope_paths = []
        else:
            scope_paths = scope_from_record(repo, commit, sd)
    for r in a.rules:
        rv, rp = split_ref(r)
        if not any(x['path'] == rp for x, _ in loaded.rule_files):
            records.items.append(oc.make_item('RECORD', 'record-invalid', rp, None,
                                              {'why': 'rule file not referenced by the configuration'}))
    hit_recs = []
    for r in a.classify:
        d = records.admit(repo, r, 'classification')
        if d is not None:
            hit_recs += [dict(x, _ref=d['_ref']) for x in d.get('classifications', [d])]
    review = [p for p in profs if p.kind == 'review']
    deny = [p for p in profs if p.kind == 'deny']
    counter = [p for p in profs if p.kind == 'countercontrol']
    tm = pl.Terms(ctx, commit, review, deny, added=added, hit_records=hit_recs, check=chk, scope_paths=scope_paths,
                  splice_texts=stexts)
    tm.deny()
    tm.review()
    if ctx.allow_rules:
        tm.stale_rules()
    items = list(tm.items)
    reports = {}
    for p in counter:
        n = 0
        for path in ctx.corpus(commit):
            for ln, l in enumerate(ctx.ft(commit, path).lines, 1):
                m = p.matches(l)
                if m:
                    n += 1
                    items.append(oc.make_item('TERMS', 'item7-literal-match', '%s:%d' % (path, ln), None,
                                              {'literal': sorted({k for k, _, _ in m})}, file=path, line=ln,
                                              literals=sorted({l[x:y] for _, x, y in m}), profiles=[p.name]))
        rep = p.spec.get('report_regex')
        if rep:
            rx = re.compile(rep)
            reports[p.name] = {'report_regex_lines': sum(1 for path in ctx.corpus(commit)
                                                         for l in ctx.ft(commit, path).lines if rx.search(l))}
    result['reports'] = reports
    result['hits'] = sorted(tm.hits, key=lambda h: (h['file'], h['line']))
    result['hit_counts'] = hit_counts(tm.hits)
    result['profiles_evaluated'] = {commit: sorted(names)}
    result['covered_paths'] = sorted(set(ctx.corpus(commit)) | set(scope_paths or []))
    result['added_text_lines'] = sum(len(v) for v in added.values())
    return items


def scope_from_record(repo, commit, sd):
    """Paths of a scope record (oi-scope/1): tracked text files less its excluded prefixes, files and patterns."""
    ex_pref = tuple(sd.get('exclude_prefixes', []))
    ex_file = set(sd.get('exclude_files', []))
    keep_rx = [re.compile(x) for x in sd.get('include_patterns_within_excluded', [])]
    gen_rx = [re.compile(x) for x in sd.get('exclude_patterns', [])]
    out = []
    for p, bid in sorted(repo.paths(commit).items()):
        if p in ex_file or any(rx.search(p) for rx in gen_rx):
            continue
        if p.startswith(ex_pref) and not any(rx.search(p) for rx in keep_rx):
            continue
        data = repo.read_blob(bid)
        if b'\x00' in data:
            continue
        try:
            data.decode('utf-8')
        except UnicodeDecodeError:
            continue
        out.append(p)
    return out


# ---- op C ------------------------------------------------------------------------------------------------

def candidate_with_and_without(ctx, H, X, led, dele, M, L, C, side, recon, record_refs=None):
    """Op C's candidate checks on X; with reconciliation records they are run without the records as well, and
    any difference is record-invalid (S2, N2). Returns the Execution."""
    ex = exmod.Execution(ctx, H, X, led, dele, M, L, C, side, recon)
    ex.record_refs = record_refs or {}
    ex.integrity()
    ex.candidate()
    ex.x_identity = None
    if recon:
        bare = exmod.Execution(ctx, H, X, led, dele, M, L, C, side, ())
        bare.integrity()
        bare.candidate()
        with_r = sorted(i['fingerprint'] for i in ex.items)
        without = sorted(i['fingerprint'] for i in bare.items)
        ex.x_identity = {'with': len(with_r), 'without': len(without), 'identical': with_r == without}
        if with_r != without:
            for r in recon:
                ex.item('RECORD', 'record-invalid', (r.get('_ref') or {}).get('path') or r.get('record_id'),
                        {'why': 'changes X'},
                        detail='op C\'s items on X differ with and without the reconciliation records (S2)')
    return ex


def native_env(a, repo, F, control):
    """The native execution environment (B2): clones are made only inside a host CI job, or when an in-process
    control asks for them on its own small repository; a replay takes every run from the snapshot."""
    if control.get('replay_evidence') is not None:
        return delmod.Native(repo, None, os.path.realpath(a.out), F, False, replay=control['replay_evidence'])
    det = hostmod.RestHost.detect(control.get('environ', os.environ))
    enabled = bool(control.get('native')) or det is not None
    # host-run evidence is read in the configuration's repository and filtered by its id (sec. 7.2)
    host, repo_id = (control.get('host'), control.get('repo_id')) if control.get('native') else \
        ((det[0], getattr(a, '_repository_id', None)) if det else (None, None))
    repo_path = control.get('repo_path') or getattr(a, 'repo', None) or os.getcwd()
    why = None if enabled else 'a local run: no disposable clone is made (sec. A.40)'
    return delmod.Native(repo, repo_path, os.path.realpath(a.out), F, enabled, host, repo_id, why)


def op_execution(a, repo, ctx, loaded, records, result, control=None):
    control = control or {}
    cfg = loaded.config
    a._repository_id = cfg['repository_id']
    H = resolve(repo, a.scientific_base)
    if H != cfg['roles']['scientific_base']:
        raise oc.Stop(oc.error, 'SCIENTIFIC_BASE_MISMATCH', '--scientific-base is not the configured base')
    X = resolve(repo, a.candidate)
    led = load_adapter_input(repo, loaded, 'ledger', a.ledger)
    comp = [c for c in cfg['adapters']['ledger'].get('companion', []) if c['role'] == 'edits']
    if comp or a.edits:
        if not a.edits or not comp or split_ref(a.edits)[1] != comp[0]['path']:
            raise oc.Stop(oc.error, 'SOURCE_CHANGED', '--edits is not the configured edit list')
    dele = None
    if a.delegation:
        drev, dpath = split_ref(a.delegation)
        dref = cfg['delegation']
        if dref is None or dref['path'] != dpath:
            raise oc.Stop(oc.error, 'SOURCE_CHANGED', '--delegation is not the configured contract')
        data = cfgmod.read_ref(repo, resolve(repo, drev), dref, 'delegation contract')
        mods = {k.split(':', 1)[1]: v for k, v in loaded.modules.items() if k.startswith('delegation:')}
        dele = delmod.Delegation(json.loads(data.decode('utf-8')), mods)
    side, recon, class_docs = [], [], []
    record_refs = {}
    for r in cfg['records']:
        d = loaded.store.get(r)
        kind = r.get('kind')
        if kind == 'side-change-classes' and (d is None or d.get('schema') != 'oi-side-change-classes/1'):
            continue
        if kind == 'reconciliation' and (d is None or d.get('schema') not in rcmod.reconciliation_schemas):
            continue
        if kind not in ('side-change-classes', 'reconciliation'):
            continue
        # side-change class records and reconciliation records referenced by the configuration (sec. 6.3, 13.1,
        # 16.2) have their chain linted like any record the run uses; a failing record is record-invalid and is
        # not used
        # in every admission mode, the control harness included (OBL-28 C-29)
        probs = rec.lint_chain(r, loaded.store, loaded.admitted)
        # a class without its id field is a field error in every mode (sec. 6.3); it is never used
        probs = probs or ['record %s: %s' % (r['path'], m) for m in rec.item_list_problems(d)[:1]] or \
            ['record %s: %s entry %d lacks its id field' % ((r['path'],) + m) for m in rec.entries_without_id(d)[:1]]
        if probs:
            records.items.append(oc.make_item('RECORD', 'record-invalid', r['path'], None,
                                              {'sha': r['blob_sha256'], 'why': probs[0]}, detail=probs))
        elif kind == 'side-change-classes':
            class_docs.append(d)
            side += d.get('classes', [])
            record_refs[r['path']] = r['blob_sha256']
        else:
            recon.append(dict(d, _ref={'path': r['path'], 'blob_sha256': r['blob_sha256']},
                              _source=loaded.ref['commit']))
    # the --classify records (sec. 22): a reconciliation record reaches the run only by the post-freeze route of
    # R6.RECON.2; a review record is never a primary record; in the control harness every other record kind is
    # linted at its record commit (OBL-28 C-29)
    route_cands = []
    for r in a.classify:
        rev_text, rpath = split_ref(r)
        if not re.fullmatch(r'[0-9a-f]{40}', rev_text):
            records.items.append(oc.make_item('RECORD', 'record-invalid', rpath, None,
                                              {'why': 'the record commit is not a full commit id'},
                                              detail='a --classify record commit must be a full commit id'))
            continue
        rev = resolve(repo, rev_text)
        try:
            data = repo.read(rev, rpath)
        except Unresolvable as exc:
            records.items.append(oc.make_item('RECORD', 'record-invalid', rpath, None, {'why': 'not a regular file'},
                                              detail=str(exc)))
            continue
        if data is None:
            raise oc.Stop(oc.error, 'SOURCE_CHANGED', 'record %s not present at %s' % (rpath, rev[:12]))
        try:
            doc = json.loads(data.decode('utf-8'))
        except (ValueError, UnicodeDecodeError):
            doc = None
        schema = doc.get('schema') if isinstance(doc, dict) else None
        if schema in recon_route.recon_schemas:
            records.used.append({'path': rpath, 'blob_sha256': util.sha256(data), 'kind': 'classification'})
            route_cands.append((rev_text, rev, rpath, data, doc))
            continue
        if schema == recon_route.review_schema:
            records.used.append({'path': rpath, 'blob_sha256': util.sha256(data), 'kind': 'classification'})
            records.items.append(oc.make_item('RECORD', 'record-invalid', rpath, None,
                                              {'sha': util.sha256(data), 'why': 'a review record named as the '
                                                                                'primary record'}))
            continue
        d = records.admit(repo, r, 'classification')
        if d is None:
            continue
        if records.harness:
            probs = recon_route.lint_classified(repo, rev, rpath, data, d, None)
            if probs:
                records.items.append(oc.make_item('RECORD', 'record-invalid', rpath, None,
                                                  {'sha': d['_ref']['blob_sha256'], 'why': probs[0]}, detail=probs))
                continue
        if d.get('schema') == 'oi-side-change-classes/1':
            missing = rec.item_list_problems(d) or ['%s entry %d lacks its id field' % m
                                                    for m in rec.entries_without_id(d)]
            if missing:
                records.items.append(oc.make_item('RECORD', 'record-invalid', d['_ref']['path'], None,
                                                  {'sha': d['_ref']['blob_sha256'], 'why': missing[0]}))
                continue
            if d['_ref']['path'] not in record_refs:
                class_docs.append(d)
                side += d.get('classes', [])
                record_refs[d['_ref']['path']] = d['_ref']['blob_sha256']
    M = resolve(repo, a.main) if a.main else None
    if route_cands:
        if M is None:
            for c in route_cands:
                records.items.append(oc.make_item('RECORD', 'record-invalid', c[2], None,
                                                  {'sha': util.sha256(c[3]), 'why': 'no --main: nothing to reconcile'}))
        else:
            pinned = (cfg['roles'].get('side_change_classes') or {}) if isinstance(cfg.get('roles'), dict) else {}
            pinned_doc = loaded.store.get(pinned) if pinned.get('path') else None
            scope = recon_route.Scope(repo, H, M, X, resolve(repo, a.freeze) if a.freeze else None, records.harness,
                                      pinned_doc, posixpath.dirname(split_ref(a.config)[1]), led['files'],
                                      ctx.in_corpus, recon, record_base=a.record_base)
            got, listing, clash = recon_route.admit(repo, route_cands, scope, records.items)
            if clash:
                # (e): a configuration-referenced record that shares a path with another is not used either
                for r_ in [x for x in recon if (x.get('_ref') or {}).get('blob_sha256') in clash]:
                    records.items.append(oc.make_item('RECORD', 'record-invalid', r_['_ref']['path'], None,
                                                      {'sha': r_['_ref']['blob_sha256'],
                                                       'why': 'another record covers one of its paths'}))
                recon = [x for x in recon if (x.get('_ref') or {}).get('blob_sha256') not in clash]
            recon += got
            result.setdefault('inputs', {})['classify_records'] = listing
    dup = rcmod.duplicate_class_ids(class_docs)
    if dup:
        raise oc.Stop(oc.error, 'CONFIG_INCONSISTENT', 'side-change class id defined more than once: %s' % dup[:3])
    L = resolve(repo, a.landing) if a.landing else None
    C = resolve(repo, a.certified) if a.certified else None
    ex = candidate_with_and_without(ctx, H, X, led, dele, M, L, C, side, recon, record_refs)
    if recon:
        result['reconciliation_x_identity'] = ex.x_identity
    if C and C != X:
        chain = first_parent_chain(repo, X, C)
        if chain is None:
            ex.item('RET', 'candidate-parent', C, {'c': C}, detail='C does not descend linearly from X')
        else:
            ex.commits_after(chain, resolve(repo, a.freeze) if a.freeze else None)
            # the tree of C is then checked as a whole, as X is (deduplicated by fingerprint)
            whole = exmod.Execution(ctx, H, C, led, dele, M, L, C, side, ())
            whole.candidate(C, chain[-2] if len(chain) > 1 else X)
            have = {i['fingerprint'] for i in ex.items}
            for i in whole.items:
                if i['fingerprint'] not in have:
                    ex.items.append(dict(i, tree='C'))
    pin_rules = led.get('pin_rules') or {'min_len': 20, 'skip_prefixes': [], 'ok': []}
    ex.pins(pin_rules)
    # deny profiles on the candidate (added text for added-text profiles)
    added = pl.added_lines(ctx, X, led, ctx.corpus(X))
    deny = [p for p in ctx.profiles.values() if p.kind == 'deny']
    tm = pl.Terms(ctx, X, [], deny, added=added, splice_texts=pl.splice_texts(ctx, H, X, led))
    tm.deny()
    items = list(ex.items) + list(tm.items) + per_edit(ctx, led, result)
    if dele is not None:
        F = resolve(repo, a.freeze) if a.freeze else None
        roles = {'scientific_base': H, 'candidate': X, 'freeze': F, 'certified': C,
                 'ledger_sha256': cfg['adapters']['ledger']['blob_sha256']}
        env = native_env(a, repo, F, control)
        supplied = {}
        if a.evidence and os.path.isdir(a.evidence):
            for name in sorted(os.listdir(a.evidence)):
                p_ = os.path.join(a.evidence, name)
                if os.path.isfile(p_):
                    supplied[name] = open(p_, 'rb').read()
        di, rep_ = dele.verify(repo, roles, env, led, supplied)
        items += di
        result['delegation'] = rep_
    else:
        items.append(oc.make_item('DELEGATED', 'delegated-evidence-missing', 'delegation contract', None,
                                  {'why': 'no contract given'}))
    if M:
        if a.freeze:
            # amendment r4, A.4 and A.7: the record-directory rule, evaluated only by an operation that evaluates M
            # with F
            ex.record_dir_args = {'freeze': resolve(repo, a.freeze), 'cpath': split_ref(a.config)[1],
                                  'authorized': record_authority.authorized_record_directories}
        corp = set(ctx.corpus(H)) | set(ctx.corpus(M))
        rp = cfg['adapters'].get('replay') or {}
        rdir = rp.get('module_path', '').rsplit('/', 1)[0] if rp else None
        ex.main_role(set(led['files']) | corp, rp.get('record_tree'), rdir)
        # the main role's own items: MAIN, and RECORD for a record entry's form or RC12 (amendment 3)
        items += [i for i in ex.items if i['obligation'] in ('MAIN', 'RECORD') and i not in items]
        items += category3(a, repo, cfg, loaded, H, M, led, recon, route_cands, ex, result, records)
        result['side_changes'] = ex.side_changes
        result['dispositions'] = getattr(ex, 'dispositions', [])
        if ex.rd is not None:
            result['record_directory'] = ex.rd.summary()
    if L:
        if not M:
            raise oc.Stop(oc.usage, 'USAGE', '--landing needs --main')
        before = len(ex.items)
        ex.landing(re.compile(r'\.(tex|pdf)$'))
        items += ex.items[before:]
    result['checks'] = ex.checks
    if ex.compositions:
        result['landing_compositions'] = ex.compositions
    result['roles'] = {'H': H, 'X': X, 'M': M, 'L': L, 'C': C or X}
    result['covered_paths'] = sorted(set(repo.paths(H)) | set(repo.paths(X)))
    return items
