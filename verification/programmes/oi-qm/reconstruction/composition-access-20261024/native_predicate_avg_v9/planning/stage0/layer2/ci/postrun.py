"""NP-AVG-1 Stage 0 Layer 2: the post-run check of the CI calibration and u_cal's preregistered
statistic (PROPOSAL; run locally after a launch, never in CI).

Usage: python3 -I -B postrun.py --code <layer2/code> --authorized-sha SHA --out FILE
                                --launch RUN.json JOBS.json DIR [--launch RUN.json JOBS.json DIR ...]
RUN.json is the host's record of the workflow run (gh api repos/OWNER/REPO/actions/runs/ID), JOBS.json
its jobs (.../actions/runs/ID/jobs), DIR the downloaded calib-*.json files of that run. Several
launches (CI-6: spread over time) are pooled.

1. Identity (CI-1). For every launch: the run's head_sha equals the owner-named SHA, its branch is
   ci-calibration/np-avg-1-stage0, its event is push, and every calibration's GITHUB_SHA and
   GITHUB_RUN_ID equal the run's. Any failure: VOID.
2. Count. At least 20 calibrations in all, or VOID (owner's ruling).
3. u_cal, as preregistered before any CI data (CI-CALIBRATION-PROPOSAL.md section 4; CI-3):
   - for each calibration, the v8 estimate's known terms K_i (l2plan.estimate on the v8 dry run's
     context-size histogram, without the C7 inputs or the survivor cap: the dry run's standing
     computation, no enumeration);
   - s = the sample standard deviation of log K_i over the n calibrations, pooled over every launch
     and every CPU model (the run would draw its jobs from the same fleet; the per-model split is
     reported, not used);
   - s_U = the one-sided 95 % upper confidence bound on the standard deviation:
     s_U = s * sqrt((n - 1) / chi2_{0.05, n-1}), chi2's lower 5 % quantile by Wilson-Hilferty;
   - u_cal = exp(2.3263 * sqrt(2) * s_U), the 99th percentile of the ratio of two independent
     lognormal draws at that bound, rounded up to three decimals.
   The empirical 99th percentile of the ordered-pair ratios and the point estimate exp(2.3263 *
   sqrt(2) * s) are reported for information only. The statistic is conservative for the campaign
   total, whose many jobs average runner noise, and about right for a single job.
4. Per-job fixed overhead (CI-5): for each calibration job, the host's job duration minus the
   script's own wall-clock time; median, 90th percentile and maximum, and the guard and aggregate
   jobs' durations. It measures budget.campaign.per_job_fixed_overhead_seconds.
Prints and writes JSON; exit 0 iff 1 and 2 hold."""
import calendar
import json
import math
import os
import statistics
import sys
import time

args = sys.argv[1:]
code = args[args.index('--code') + 1]
auth = args[args.index('--authorized-sha') + 1]
out_path = args[args.index('--out') + 1]
launches = []
for i, a in enumerate(args):
    if a == '--launch':
        launches.append(tuple(args[i + 1:i + 4]))
sys.path.insert(0, code)
import l2config as CFG   # noqa: E402
import l2plan as PLAN    # noqa: E402

BRANCH = 'ci-calibration/np-avg-1-stage0'
Z99, Z05 = 2.3263, -1.6449


def ts(s):
    return calendar.timegm(time.strptime(s, '%Y-%m-%dT%H:%M:%SZ'))


def chi2_lower(p_z, k):
    """chi-square quantile by Wilson-Hilferty, at the standard-normal quantile p_z, k degrees of freedom."""
    return k*(1 - 2/(9*k) + p_z*math.sqrt(2/(9*k)))**3


problems, cals, jobs_over, other_jobs = [], [], [], {}
for runp, jobsp, d in launches:
    with open(runp) as f:
        run = json.load(f)
    with open(jobsp) as f:
        jobs = json.load(f).get('jobs', [])
    if run.get('head_sha') != auth:
        problems.append('run %s: head_sha %s is not the authorized SHA' % (run.get('id'), run.get('head_sha')))
    if run.get('head_branch') != BRANCH or run.get('event') != 'push':
        problems.append('run %s: branch or event' % run.get('id'))
    jdur = {}
    for j in jobs:
        if j.get('started_at') and j.get('completed_at'):
            jdur[j['name']] = ts(j['completed_at']) - ts(j['started_at'])
    for name, sec in jdur.items():
        if not name.startswith('calibrate'):
            other_jobs.setdefault(name, []).append(sec)
    for fn in sorted(f for f in os.listdir(d) if f.startswith('calib-') and f.endswith('.json')):
        with open(os.path.join(d, fn)) as f:
            c = json.load(f)
        ident = c.get('run_identity') or {}
        if ident.get('GITHUB_SHA') != auth or str(ident.get('GITHUB_RUN_ID')) != str(run.get('id')):
            problems.append('%s: run identity differs from the authorized run' % fn)
        cals.append(c)
        w = c.get('wall_clock_utc') or {}
        job = jdur.get('calibrate (%s)' % c.get('index'))
        if job is not None and w.get('script_start') and w.get('script_end'):
            jobs_over.append(job - (ts(w['script_end']) - ts(w['script_start'])))
if len(cals) < 20:
    problems.append('%d calibrations; at least 20 are required' % len(cals))
res = {'schema': 'np-avg-1/stage0/layer2/ci-postrun/1', 'authorized_sha': auth, 'launches': len(launches),
       'calibrations': len(cals), 'problems': problems}
if not problems:
    sp = PLAN.Space(CFG.profile('v8'))
    N = sp.n_records()
    _, so, po = sp.orbits_burnside()
    hist = PLAN.context_histogram(sp)
    K = [PLAN.estimate(sp, hist, so + po, N, c, CFG.profile('v8'))['known_terms_runner_seconds'] for c in cals]
    n = len(K)
    s = statistics.stdev(math.log(k) for k in K)
    s_u = s*math.sqrt((n - 1)/chi2_lower(Z05, n - 1))
    u_cal = math.exp(Z99*math.sqrt(2)*s_u)
    ratios = sorted(a/b for i, a in enumerate(K) for j, b in enumerate(K) if i != j)
    per_cpu = {}
    for c, k in zip(cals, K):
        per_cpu.setdefault(str(c['runner'].get('cpu_model')), []).append(k)
    res.update({
        'known_terms_runner_seconds': K, 'sigma_log': round(s, 5), 'sigma_log_upper_95': round(s_u, 5),
        'u_cal': '%.3f' % (math.ceil(u_cal*1000)/1000),
        'u_cal_rule': 'exp(2.3263 sqrt(2) s_U), s_U the one-sided 95 % upper bound on sigma (chi-square, '
                      'Wilson-Hilferty), pooled; rounded up to three decimals',
        'information_only': {'point_estimate': round(math.exp(Z99*math.sqrt(2)*s), 4),
                             'empirical_p99_of_ratios': round(ratios[math.ceil(0.99*len(ratios)) - 1], 4)},
        'per_cpu_model': {k: {'calibrations': len(v), 'median_known_terms': int(statistics.median(v))}
                          for k, v in sorted(per_cpu.items())},
        'per_job_fixed_overhead_seconds': None if not jobs_over else {
            'jobs': len(jobs_over), 'median': statistics.median(jobs_over),
            'p90': sorted(jobs_over)[int(0.9*(len(jobs_over) - 1))], 'max': max(jobs_over)},
        'other_job_seconds': other_jobs})
res['verdict'] = 'HOLDS' if not problems else 'VOID'
with open(out_path, 'w') as f:
    f.write(json.dumps(res, indent=1, sort_keys=True) + '\n')
print(json.dumps({k: res.get(k) for k in ('verdict', 'calibrations', 'u_cal', 'problems')}, sort_keys=True))
sys.exit(0 if not problems else 2)
