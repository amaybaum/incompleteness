"""verdict.py STEP: applies STEP's decision rule (stated in the workflow header) to its exit status and its result
files, writes STEP.verdict.json in the evidence directory and exits 1 when the rule fails, so that the step's
conclusion carries the verdict."""
import json
import os
import sys

LCS = os.environ['LCS']
EV = os.path.join(LCS, 'ev')
OUT = os.path.join(LCS, 'out')
MUT = os.path.join(LCS, 'mutwork')
# the survivors of the local mutation run at the tool commit
LOCAL_SURVIVORS = {'c2:D02', 'v60e:V05', 'v60e:I06', 'v60e:C08', 'v60e:H03', 'v60e:P01', 'cache:K08'}


def load(path):
    with open(path) as f:
        return json.load(f)


def rows(controls):
    """{id: status} from a list of {id, status} rows or a {id: {status}} map; a repeated id is an error."""
    out = {}
    items = controls.items() if isinstance(controls, dict) else [(c['id'], c) for c in controls]
    for cid, c in items:
        if cid in out:
            raise ValueError('control id %s repeated' % cid)
        out[cid] = c['status']
    return out


def main():
    step = sys.argv[1]
    reasons = []
    extra = {}
    controls = None

    def need(cond, why):
        if not cond:
            reasons.append(why)

    try:
        with open(os.path.join(EV, step + '.exit')) as f:
            rc = int(f.read().strip())
    except Exception as exc:
        rc = None
        reasons.append('no exit status: %r' % exc)
    try:
        if step == '1-self-test':
            need(rc == 0, 'exit %s' % rc)
            controls = {}
            for c in load(os.path.join(OUT, 'st', 'result.json'))['controls']:
                if c['id'] in controls:
                    raise ValueError('control id %s repeated' % c['id'])
                controls[c['id']] = 'PASS' if c['passed'] is True else 'FAIL'
            need(controls and all(v == 'PASS' for v in controls.values()), 'a self-test control did not pass')
        elif step == '2-purity':
            need(rc == 0, 'exit %s' % rc)
            d = load(os.path.join(OUT, 'p', 'result.json'))
            controls = {'outcome': d['outcome']}
            need(d['outcome'] == 'PASS', 'outcome %s' % d['outcome'])
        elif step == '3-synthetic':
            need(rc == 0, 'exit %s' % rc)
            d = load(os.path.join(EV, '3-synthetic.stdout'))
            controls = {k: ('PASS' if v is True else 'FAIL') for k, v in d.items() if not k.startswith('_')}
            extra['informational'] = {k: v for k, v in d.items() if k.startswith('_')}
            need(controls and all(v == 'PASS' for v in controls.values()), 'a synthetic control is not true')
        elif step == '4-conformance':
            need(rc == 0, 'exit %s' % rc)
            controls = rows(load(os.path.join(OUT, 'conf', 'conformance-controls.json'))['controls'])
            nr = sorted(k for k, v in controls.items() if v == 'NOT RUN')
            need(nr == ['G-A1', 'TR5'], 'NOT RUN set %s' % nr)
            bad = sorted(k for k, v in controls.items() if v not in ('PASS', 'NOT RUN'))
            need(not bad, 'not PASS: %s' % bad)
        elif step == '5-a1-conformance':
            need(rc == 0, 'exit %s' % rc)
            controls = rows(load(os.path.join(OUT, 'a1c', 'a1-conformance.json'))['controls'])
            bad = sorted(k for k, v in controls.items() if v != 'PASS')
            need(controls and not bad, 'not PASS: %s' % bad)
        elif step == '6a-a1-controls-no-main':
            need(rc == 2, 'exit %s, expected 2 (usage)' % rc)
            need(not os.path.exists(os.path.join(OUT, 'a1-nomain', 'a1-controls.json')), 'a result file was written')
        elif step == '6-a1-controls':
            d = load(os.path.join(OUT, 'a1', 'a1-controls.json'))
            controls = rows(d['controls'])
            nr = sorted(k for k, v in controls.items() if v == 'NOT RUN')
            need(nr == ['RT-T'], 'NOT RUN set %s' % nr)
            bad = sorted(k for k, v in controls.items() if v not in ('PASS', 'NOT RUN'))
            need(not bad, 'not PASS: %s' % bad)
            need(sorted(d['failed']) == nr, 'failed list %s differs from the NOT RUN set' % d['failed'])
            need(rc == (1 if d['failed'] else 0), 'exit %s inconsistent with the failed list' % rc)
            extra['timing_seconds'] = d.get('timing_seconds')
        elif step == '8-y8':
            need(rc == 0, 'exit %s' % rc)
            d = load(os.path.join(OUT, 'y8', 'a1-controls.json'))
            controls = rows(d['controls'])
            need(controls.get('Y8') == 'PASS', 'Y8 %s' % controls.get('Y8'))
            need(d['failed'] == [], 'failed %s' % d['failed'])
            extra['y8_actual'] = d['controls'].get('Y8', {}).get('actual')
        elif step == '9-mutation':
            need(rc == 0, 'exit %s' % rc)
            d = load(os.path.join(MUT, 'results.json'))
            base = load(os.path.join(MUT, 'base.json'))
            nr = sorted(k for k, v in base.items() if v == 'NOT RUN')
            need(nr == ['conformance/G-A1', 'conformance/TR5'], 'base NOT RUN set %s' % nr)
            bad = sorted(k for k, v in base.items() if v not in ('PASS', 'NOT RUN'))
            need(not bad, 'base not PASS: %s' % bad)
            controls = {}
            for m in d['mutants']:
                if m['id'] in controls:
                    raise ValueError('mutant id %s repeated' % m['id'])
                controls[m['id']] = m['status']
            na = sorted(k for k, v in controls.items() if v == 'NOT APPLIED')
            need(na == ['v60e:U01'], 'NOT APPLIED set %s' % na)
            surv = sorted(k for k, v in controls.items() if v == 'SURVIVED')
            need(set(surv) <= LOCAL_SURVIVORS, 'survivors killed in the local run: %s' % sorted(set(surv) - LOCAL_SURVIVORS))
            other = sorted(k for k, v in controls.items() if v not in ('KILLED', 'SURVIVED', 'NOT APPLIED'))
            need(not other, 'unknown status: %s' % other)
            extra.update(counts=d['counts'], base_counts=d['base_counts'], survived=surv, not_applied=na,
                         killed=sum(1 for v in controls.values() if v == 'KILLED'),
                         killed_here_survived_locally=sorted(k for k in LOCAL_SURVIVORS if controls.get(k) == 'KILLED'))
        elif step in ('lean-install', '7-release-gate'):
            need(rc == 0, 'exit %s' % rc)
        elif step == 'lean-build':
            need(rc == 0, 'exit %s' % rc)
            with open(os.path.join(EV, 'lean-build.tree-status')) as f:
                s = f.read()
            need(s == '', 'the worktree changed: %s' % s[:400])
        else:
            reasons.append('no rule for step %s' % step)
    except Exception as exc:
        reasons.append('unreadable result: %s: %s' % (type(exc).__name__, exc))
    v = {'step': step, 'exit': rc, 'pass': not reasons, 'reasons': reasons, 'controls': controls, 'extra': extra}
    with open(os.path.join(EV, step + '.verdict.json'), 'w') as f:
        json.dump(v, f, indent=1, sort_keys=True, default=str)
    print('%s %s %s' % (step, 'PASS' if not reasons else 'FAIL', '; '.join(reasons)))
    return 0 if not reasons else 1


if __name__ == '__main__':
    sys.exit(main())
