"""GEOM-ODD-1 controls preflight: one control under its wall-clock cap.

usage: run_control.py <control> <cap-seconds> <result.json>

The cap covers the whole control: the pool emission, the generator and the exact verification, measured from this
script's start on a monotonic clock. The generator gets the cap less VERIFY_RESERVE seconds and is killed at that
point if it has not exited (below a 720 s cap the reserve is a third of the cap); the verifier gets what remains and is killed at the cap. The workflow wraps this script in
`timeout --signal=KILL <cap + 60>` as a backstop, so a hung interpreter cannot outlive the job. The control passes
(exit 0) iff the verifier prints PASS on the generator's candidate within the cap. A timeout, a missing candidate or a
verifier FAIL is a failed control, and the result says which.

The result file holds deterministic fields only (no times): the control, the cap, the outcome, the generator status,
the candidate's sha256 and the verifier's report. Elapsed times go to the log.
"""
import hashlib
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY_RESERVE = 240                # at the frozen 1200 s cap; min(240, cap // 3) below it


def run(cmd, timeout):
    try:
        p = subprocess.run(cmd, timeout=max(1, timeout), capture_output=True, text=True)
        sys.stdout.write(p.stdout)
        sys.stderr.write(p.stderr)
        return p.returncode
    except subprocess.TimeoutExpired as e:
        for stream, data in ((sys.stdout, e.stdout), (sys.stderr, e.stderr)):
            if data:
                stream.write(data if isinstance(data, str) else data.decode('utf-8', 'replace'))
        return 'timeout'


def main(argv):
    control, cap, out_path = argv[1], int(argv[2]), argv[3]
    t0 = time.monotonic()
    work = os.path.dirname(os.path.abspath(out_path))
    pool = os.path.join(work, 'pool-%s.json' % control)
    cand = os.path.join(work, 'candidate-%s.json' % control)
    report = os.path.join(work, 'verify-%s.json' % control)
    result = {'control': control, 'cap_seconds': cap}
    py = [sys.executable, '-I']
    rc = run(py + [os.path.join(HERE, 'controls_verify.py'), '--emit-pool', control, pool], cap)
    if rc != 0:
        result.update(outcome='FAIL', reason='pool emission: %s' % rc)
    else:
        gen_budget = cap - min(VERIFY_RESERVE, cap // 3) - (time.monotonic() - t0)
        rc = run(py + [os.path.join(HERE, 'controls_gen.py'), pool, cand, str(gen_budget - 15)], gen_budget)
        print('generator exit %s at %.0f s' % (rc, time.monotonic() - t0), flush=True)
        if rc != 0 or not os.path.exists(cand):
            result.update(outcome='FAIL', reason='generator: %s' % rc, generator_status=None)
        else:
            c = json.load(open(cand))
            result['generator_status'] = c.get('status')
            result['candidate_sha256'] = hashlib.sha256(open(cand, 'rb').read()).hexdigest() if c.get('G') else None
            if c.get('G') is None:
                result.update(outcome='FAIL', reason='no candidate within the cap')
            else:
                left = cap - (time.monotonic() - t0)
                rc = run(py + [os.path.join(HERE, 'controls_verify.py'), '--verify', control, cand, report], left)
                print('verifier exit %s at %.0f s' % (rc, time.monotonic() - t0), flush=True)
                if rc == 'timeout':
                    result.update(outcome='FAIL', reason='verification exceeded the cap')
                else:
                    result['verifier'] = json.load(open(report))
                    within = time.monotonic() - t0 <= cap
                    ok = rc == 0 and result['verifier'].get('verdict') == 'PASS' and within
                    result.update(outcome='PASS' if ok else 'FAIL',
                                  reason=None if ok else ('verifier FAIL' if within else 'cap exceeded'))
    json.dump(result, open(out_path, 'w'), indent=1, sort_keys=True)
    print('CONTROL %s %s (%s) at %.0f s' % (control, result['outcome'], result.get('reason'), time.monotonic() - t0))
    return 0 if result['outcome'] == 'PASS' else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv))
