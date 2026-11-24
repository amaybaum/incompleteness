"""Dry run of selected run blocks of the committed workflow (read from the CI commit), in a temporary workspace whose
`ci` is the CI worktree. Usage: python3 -I dryrun.py WORKDIR CI_WT STEP_NAME[=SED_EXPR] ..."""
import os, subprocess, sys, yaml, json
work, ciwt = sys.argv[1], sys.argv[2]
wf = subprocess.run(['git', '-C', ciwt, 'show', 'HEAD:.github/workflows/ledger-coverage-suite-ci.yml'], capture_output=True, text=True, check=True).stdout
job = yaml.safe_load(wf)['jobs']['suite']
steps = {s.get('name'): s for s in job['steps']}
os.makedirs(os.path.join(work, 'rt'), exist_ok=True)
if not os.path.exists(os.path.join(work, 'ci')):
    os.symlink(ciwt, os.path.join(work, 'ci'))
genv = os.path.join(work, 'github_env'); gpath = os.path.join(work, 'github_path')
open(genv, 'a').close(); open(gpath, 'a').close()
sha = subprocess.run(['git', '-C', ciwt, 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()
base = dict(os.environ, **job['env'], GITHUB_WORKSPACE=work, RUNNER_TEMP=os.path.join(work, 'rt'), GITHUB_ENV=genv,
            GITHUB_PATH=gpath, GITHUB_EVENT_NAME='push', GITHUB_REF='refs/heads/' + job['env']['BRANCH'], GITHUB_SHA=sha)
for arg in sys.argv[3:]:
    name, _, sed = arg.partition('=')
    run = steps[name]['run']
    if sed:
        old, new = sed.split('=>')
        assert run.count(old) == 1, (name, old)
        run = run.replace(old, new)
    env = dict(base)
    for line in open(genv).read().splitlines():
        k, v = line.split('=', 1); env[k] = v
    p = subprocess.run(['bash', '--noprofile', '--norc', '-eo', 'pipefail', '-c', run], env=env, cwd=work, capture_output=True, text=True)
    print('== %s: exit %d' % (name, p.returncode)); print(p.stdout[-1500:]); print(p.stderr[-1500:])
    if p.returncode: sys.exit(1)
