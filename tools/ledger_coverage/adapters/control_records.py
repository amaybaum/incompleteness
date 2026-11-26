"""Runner evidence contract (design r6, R6.GATE.5 and R6.GATE.7), shared by the control runners.

A runner creates one `Recorder` per job. Each tool run the runner makes is captured with `capture` (argv, exit
status, the `--out` directory); `record` then closes a control: it copies the captured runs' exit status, result
file and `--out` listing into `evidence/<job>/<id>/`, writes the control's `manifest.json`
(`oi-control-evidence/1`: per case the argv, exit file, result file, `--out` listing, input mutation, bindings;
the sha256 of every file) and adds `{id, status, actual, predicate, evidence}` to the job's records. `write`
writes `control-records.json` (`oi-control-records/1`). Status is PASS, FAIL or NOT RUN; there is no SKIP.

Case names: a run captured with `case=NAME` is the evidence of the expectation case NAME (`restored` for the
restored tree). An unnamed first run is the row's single case ``; further unnamed runs are kept as `run2`,
`run3`, ... and decide nothing. The gate reads only this evidence, never the runner's status or actual.
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


class Recorder(object):
    def __init__(self, job, out_dir):
        self.job = job
        self.out_dir = out_dir
        self.records = []
        self.ids = set()
        self.pending = []

    def capture(self, argv, code, out=None, case=None, mutation=None, bindings=None, stderr=None, baseline=None):
        """One tool run. `out` is its --out directory (or None); `stderr` the USAGE stderr JSON text, if any;
        `baseline` an earlier captured run whose result this case is compared with (restored cases)."""
        self.pending.append({'argv': [str(a) for a in argv], 'exit': code, 'out': out, 'case': case,
                             'mutation': list(mutation or []), 'bindings': dict(bindings or {}), 'stderr': stderr,
                             'baseline': baseline})

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
            if run['exit'] is not None:
                entry['exit_file'] = put(tag + '.exit', ('%d\n' % run['exit']).encode())
            listing = []
            if run['out'] and os.path.isdir(run['out']):
                listing = sorted(os.listdir(run['out']))
                for rn in RESULT_NAMES:
                    p = os.path.join(run['out'], rn)
                    if os.path.isfile(p):
                        with open(p, 'rb') as f:
                            entry['result_file'] = put(tag + '.' + rn, f.read())
                        break
            if run['stderr'] and 'result_file' not in entry:
                entry['result_file'] = put(tag + '.stderr.json', run['stderr'].encode())
            entry['out_listing'] = put(tag + '.out-listing.json', (json.dumps(listing) + '\n').encode())
            b = run.get('baseline')
            if b and b.get('out') and os.path.isdir(b['out']):
                for rn in RESULT_NAMES:
                    p = os.path.join(b['out'], rn)
                    if os.path.isfile(p):
                        with open(p, 'rb') as f:
                            entry['baseline_file'] = put(tag + '.baseline.' + rn, f.read())
                        entry['baseline_argv'] = b['argv']
                        break
            if attested and name in attested:
                entry['attested'] = put(tag + '.attested.json',
                                        (json.dumps(attested[name], sort_keys=True, default=str) + '\n').encode())
            man['cases'].append(entry)
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

    def write(self, name='control-records.json'):
        p = os.path.join(self.out_dir, name)
        with open(p, 'w') as f:
            json.dump({'schema': SCHEMA_REC, 'job': self.job, 'records': self.records}, f, indent=1,
                      sort_keys=True, default=str)
            f.write('\n')
        return p
