"""Runner evidence contract (design r6, R6.GATE.5 and R6.GATE.7), shared by the control runners.

A runner creates one `Recorder` per job. Each tool run the runner makes is captured with `capture` (argv, exit
status, the `--out` directory's result file and listing, read at capture time), or with `wrap_cli`, which captures
every in-process call of `cli.run`; an in-process stage that has no command line (an Execution, a coverage or
terms stage of the engine controls) is captured with `capture_doc`, its argv recorded as `['in-process', label]`
and its result document built by `stage_doc` with the tool's own outcome function. `record` then closes a control:
it writes the captured runs' exit status, result file and `--out` listing into `evidence/<job>/<id>/`, writes the
control's `manifest.json` (`oi-control-evidence/1`: per case the argv, exit file, result file, `--out` listing,
input mutation, bindings, attested values; the sha256 of every file) and adds `{id, status, actual, predicate,
evidence}` to the job's records. `write` writes `control-records.json` (`oi-control-records/1`). Status is PASS,
FAIL or NOT RUN; there is no SKIP.

Case names: a run captured with `case=NAME` (or named afterwards with `name_last`) is the evidence of the
expectation case NAME (`restored` for the restored tree). An unnamed first run is the row's single case ``;
further unnamed runs are kept as `run2`, `run3`, ... and decide nothing. The gate reads only this evidence, never
the runner's status or actual; attested values are the runner's statements, checked by the gate for integrity
only.
"""
import hashlib
import json
import os
import shutil

SCHEMA_REC = 'oi-control-records/1'
SCHEMA_MAN = 'oi-control-evidence/1'
STATUSES = ('PASS', 'FAIL', 'NOT RUN')
RESULT_NAMES = ('result.json', 'control-result.json', 'replay-result.json')


def _sha(b):
    return hashlib.sha256(b).hexdigest()


def _safe(cid):
    return ''.join(c if c.isalnum() or c in '-_.' else '_' for c in cid)


def stage_doc(items, preflight=None, record_checks=None, operation=None, **extra):
    """The result document of an in-process stage: its items, and the outcome and exit status that the tool's own
    outcome function (engine/outcome.py, sec. 7 precedence) gives them. `extra` adds stage facts (side changes,
    compositions, sites) under their result-schema names."""
    from ledger_coverage.engine import outcome as oc
    items = list(items or [])
    stop = extra.pop('stop', None)
    o = oc.compute(list(preflight or []), record_checks, items)
    if stop is not None:
        # a stage that ended in oc.Stop: the stop's outcome, as the tool's writer reports it
        o = stop.outcome
        extra['stop'] = {'class': stop.cls, 'message': stop.message, 'detail': stop.detail}
    doc = {'schema': oc.result_schema, 'operation': operation, 'outcome': o, 'exit_status': oc.exit_codes[o],
           'preflight': list(preflight or []), 'record_checks': record_checks, 'items': items, 'in_process': True}
    doc.update(extra)
    return doc


class RunMap(dict):
    """A control-result dict whose every assignment of a control id (a key not starting with `_`) takes the runs
    captured since the previous assignment as that control's evidence (`runs_of[id]`)."""

    def __init__(self, recorder, runs_of):
        dict.__init__(self)
        self.recorder = recorder
        self.runs_of = runs_of

    def __setitem__(self, k, v):
        if self.recorder is not None and not str(k).startswith('_'):
            self.runs_of.setdefault(k, []).extend(self.recorder.take())
        dict.__setitem__(self, k, v)


class Recorder(object):
    def __init__(self, job, out_dir):
        self.job = job
        self.out_dir = out_dir
        self.records = []
        self.ids = set()
        self.pending = []

    def capture(self, argv, code, out=None, case=None, mutation=None, bindings=None, stderr=None, baseline=None,
                attested=None):
        """One tool run. `out` is its --out directory (or None); `stderr` the USAGE stderr JSON text, if any;
        `baseline` an earlier captured run whose result this case is compared with (restored cases). The result
        file and the --out listing are read now, so a later run that reuses the directory cannot change them."""
        run = {'argv': [str(a) for a in argv], 'exit': code, 'case': case, 'mutation': list(mutation or []),
               'bindings': dict(bindings or {}), 'stderr': stderr, 'baseline': baseline, 'listing': [],
               'result': None, 'attested': attested, 'out_exists': bool(out) and os.path.isdir(out)}
        if out and os.path.isdir(out):
            run['listing'] = sorted(os.listdir(out))
            for rn in RESULT_NAMES:
                p = os.path.join(out, rn)
                if os.path.isfile(p):
                    with open(p, 'rb') as f:
                        run['result'] = (rn, f.read())
                    break
        self.pending.append(run)
        return run

    def capture_doc(self, label, doc, case=None, mutation=None, bindings=None, baseline=None, attested=None, raw=None):
        """An in-process evaluation (no command line): `doc` is the result document the evaluated stage produced
        (its items, and the outcome and exit status the tool's precedence gives them); `label` names the stage.
        The argv is recorded as ['in-process', label] so the evidence never reads as a command-line run.
        A consumer supplies `raw` when the original input bytes are themselves part of what it verifies."""
        data = raw if raw is not None else (json.dumps(doc, indent=1, sort_keys=True, default=str) + '\n').encode()
        run = {'argv': ['in-process', label], 'exit': doc.get('exit_status'), 'case': case,
               'mutation': list(mutation or []), 'bindings': dict(bindings or {}), 'stderr': None,
               'baseline': baseline, 'listing': ['result.json'], 'result': ('result.json', data),
               'attested': attested}
        self.pending.append(run)
        return run

    def discard(self):
        self.pending = []

    def take(self):
        """The runs captured since the last call, removed from the pending list."""
        runs, self.pending = self.pending, []
        return runs

    def record(self, cid, status, actual, predicate, files=None, procedure=None, attested=None):
        if status not in STATUSES:
            raise ValueError('status %r of %s is not PASS, FAIL or NOT RUN' % (status, cid))
        if cid in self.ids:
            raise ValueError('control %s recorded twice in job %s' % (cid, self.job))
        self.ids.add(cid)
        rel = os.path.join('evidence', self.job, _safe(cid))
        d = os.path.join(self.out_dir, rel)
        if os.path.exists(d):
            shutil.rmtree(d)
        os.makedirs(d)
        man = {'schema': SCHEMA_MAN, 'id': cid, 'job': self.job, 'files': {}, 'cases': []}

        def put(name, data):
            with open(os.path.join(d, name), 'wb') as f:
                f.write(data)
            man['files'][name] = _sha(data)
            return name

        unnamed = 0
        for i, run in enumerate(self.pending, 1):
            name = run['case']
            if name is None:
                unnamed += 1
                name = '' if unnamed == 1 else 'run%d' % unnamed
            tag = 'case%02d' % i
            entry = {'case': name, 'argv': run['argv'], 'mutation': run['mutation'], 'bindings': run['bindings']}
            if 'out_exists' in run and run['argv'][:1] != ['in-process']:
                entry['out_dir_exists'] = run['out_exists']
            if run['exit'] is not None:
                entry['exit_file'] = put(tag + '.exit', ('%d\n' % run['exit']).encode())
            if run.get('result'):
                rn, data = run['result']
                entry['result_file'] = put(tag + '.' + rn, data)
            if run['stderr'] and 'result_file' not in entry:
                entry['result_file'] = put(tag + '.stderr.json', run['stderr'].encode())
            entry['out_listing'] = put(tag + '.out-listing.json', (json.dumps(run['listing']) + '\n').encode())
            b = run.get('baseline')
            if b and b.get('result'):
                rn, data = b['result']
                entry['baseline_file'] = put(tag + '.baseline.' + rn, data)
                entry['baseline_argv'] = b['argv']
            att = dict(run.get('attested') or {})
            if attested and name in attested:
                att.update(attested[name])
            if att:
                # values the runner states for this case (DESIGN-r6.md sec. 16, L1): checked for integrity only
                entry['attested'] = put(tag + '.attested.json',
                                        (json.dumps(att, sort_keys=True, default=str) + '\n').encode())
            man['cases'].append(entry)
        if isinstance(procedure, dict) and 'run_cases' in procedure:
            # a procedure that names its runs by case: each case's retained result file
            by_case = {e['case']: e.get('result_file') for e in man['cases']}
            procedure = dict(procedure)
            procedure['runs'] = [by_case.get(c) for c in procedure.pop('run_cases')]
        for name, data in sorted((files or {}).items()):
            put(name, data if isinstance(data, bytes) else
                (json.dumps(data, indent=1, sort_keys=True, default=str) + '\n').encode())
        if procedure is not None:
            man['procedure'] = procedure
        with open(os.path.join(d, 'manifest.json'), 'w') as f:
            json.dump(man, f, indent=1, sort_keys=True)
            f.write('\n')
        self.records.append({'id': cid, 'status': status, 'actual': actual, 'predicate': predicate,
                             'evidence': rel})
        self.pending = []
        return rel

    def wrap_cli(self, cli):
        """Captures every in-process call of `cli.run` (argv, exit status, --out result and listing, the USAGE
        stderr) until the returned function restores it."""
        real = cli.run
        rec = self

        def run(argv, *args, **kw):
            code, res = real(argv, *args, **kw)
            argv = list(argv)
            out = argv[argv.index('--out') + 1] if '--out' in argv[:-1] else None
            err = kw.get('stderr')
            text = err.getvalue() if code == 64 and hasattr(err, 'getvalue') else None
            rec.capture(argv, code, out, stderr=text or None)
            return code, res
        cli.run = run
        return lambda: setattr(cli, 'run', real)

    def name_last(self, case, **kw):
        """Names the last captured run as expectation case `case` (and sets its bindings or mutation)."""
        if self.pending:
            self.pending[-1]['case'] = case
            for k, v in kw.items():
                self.pending[-1][k] = v
        return self.pending[-1] if self.pending else None

    def write(self, name='control-records.json'):
        p = os.path.join(self.out_dir, name)
        with open(p, 'w') as f:
            json.dump({'schema': SCHEMA_REC, 'job': self.job, 'records': self.records}, f, indent=1,
                      sort_keys=True, default=str)
            f.write('\n')
        return p


EXPECTATIONS = os.path.join('verification', 'audits', 'foundations', 'a1exit-design-r6-20261125', 'EXPECTATIONS.json')


def expectation_ids(repo_root=None):
    """The row ids of the expectation file in the runner's own tree (empty when the file is absent)."""
    root = repo_root or os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    try:
        with open(os.path.join(root, EXPECTATIONS), encoding='utf-8') as f:
            return {r['id'] for r in json.load(f)['rows']}
    except (OSError, ValueError, KeyError, TypeError):
        return set()


class LocalSuite(object):
    """The evidence contract for a local control suite whose cases are mostly sub-cases of no expectation row
    (obl29, custody, adjudication, staging, sessions). Every in-process `cli.run` is captured from `start`; `case`
    closes a case, taking the runs captured since the previous one; `write` records, with their evidence, the cases
    whose id is an expectation row, and writes `control-records.json`. The other cases stay in the suite's own
    report; recorded to the gate they would be ids the expectation file does not hold."""

    def __init__(self, job):
        self.rec = Recorder(job, None)
        self.runs = {}

    def start(self):
        from ledger_coverage.engine import cli
        return self.rec.wrap_cli(cli)

    def case(self, cid):
        self.runs.setdefault(cid, []).extend(self.rec.take())

    def write(self, out_dir, results, repo_root=None):
        rows = expectation_ids(repo_root)
        self.rec.out_dir = out_dir
        for r in results:
            if r['id'] in rows and r['id'] not in self.rec.ids:
                self.rec.pending = self.runs.get(r['id'], [])
                self.rec.record(r['id'], r['status'] if r['status'] in STATUSES else 'FAIL', r.get('actual'),
                                r.get('predicate') or r.get('expected'), attested=r.get('attested'))
        return self.rec.write()
