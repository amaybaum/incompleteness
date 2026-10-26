"""NP-AVG-1 Stage 0 Layer 2: the bounded local evidence driver (toy, planted and small-window
instances, S6's carrier, and v8 configuration combinatorics; never a closure on v8's class).

Usage: python3 -I -B l2run.py <layer2/design>
Runs every step in order, retains each step's stdout and stderr in design/runs/, keeps the
toy run's structured files in design/toyrun/, the kappa calibration repeats in design/kappa/ and the
overhead measurement in design/overhead/, compares normal and -O runs where the output is
deterministic (stdout, or the files a step writes), and writes design/RUN-MANIFEST.json and
.md with the commands, exit codes, durations, -O identity and SHA-256 values. Verdicts in the
manifest are exit statuses; the structured files carry the detail.
"""
import hashlib
import json
import os
import platform
import shutil
import subprocess
import sys
import tempfile
import time

CODE = os.path.dirname(os.path.abspath(__file__))
R5 = os.path.join(os.path.dirname(os.path.dirname(CODE)), 'code-r5')
E1CHECK = os.path.join(os.path.dirname(os.path.dirname(CODE)), 'amendments', 'E1-check')
CI = os.path.join(os.path.dirname(CODE), 'ci')


def sha(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    ev = os.path.abspath(sys.argv[1])
    runs, W, K, OV = (os.path.join(ev, 'runs'), os.path.join(ev, 'toyrun'), os.path.join(ev, 'kappa'),
                      os.path.join(ev, 'overhead'))
    for d in (runs, W, K, OV):
        if os.path.isdir(d):
            shutil.rmtree(d)
        os.makedirs(d)
    scratch = tempfile.mkdtemp(prefix='l2run-')
    py = sys.executable

    def c(fn, *a):
        return [py, '-I', '-B', os.path.join(CODE, fn)] + list(a)

    def dz(fn, *a):
        return [py, '-I', '-B', os.path.join(ev, fn)] + list(a)
    # (name, command, O-check): True = compare stdout and exit; a list = compare those file pairs
    # after an -O run; False = no -O run (timings, or steps that only spawn subprocesses).
    steps = [
        ('manifest_verify', c('l2manifest.py', '--verify'), True),
        ('l2_selftest', c('l2selftest.py'), True),
        ('calibration_planted', c('l2calib.py', '--out', os.path.join(W, 'calib.json')), False),
        ('dryrun_toy', c('l2plan.py', '--profile', 'toy', '--calib', os.path.join(W, 'calib.json'), '--shared-tips',
                         '--out', os.path.join(W, 'dryrun.json')), True),
        ('dryrun_v8_plan_no_closure', c('l2plan.py', '--profile', 'v8'), True),
        ('dryrun_v8_estimate', c('l2plan.py', '--profile', 'v8', '--calib', os.path.join(W, 'calib.json')), False),
        ('preflight_toy_quick', c('l2preflight.py', '--profile', 'toy', '--workdir', W, '--quick'), False),
        ('mutants_quick', c('l2mutants.py', '--workdir', W), False),
        ('s1a_toy', c('l2s1a.py', '--profile', 'toy', '--workdir', W), [('s1a.json', 's1a.O.json')]),
    ]
    for s in range(4):
        steps.append(('shard_toy_%d' % s, c('l2enum.py', '--profile', 'toy', '--shard', str(s), '--workdir', W),
                      [('shard-%d.json' % s, 'shard-%d.O.json' % s)]))
    steps += [
        ('merge_toy', c('l2merge.py', '--profile', 'toy', '--workdir', W), [('result.json', 'result.O.json')]),
        ('certificate_toy', c('l2cert.py', '--profile', 'toy', '--workdir', W), True),
        ('crosscheck_toy_counts', dz('crosscheck.py', W, R5), True),
        ('e1check_replay', dz('e1check_replay.py', E1CHECK), True),
        ('code_r5_equivalence_quick', dz('r5_equivalence.py', R5, W), False),
        ('planted_survivor_path', dz('planted_shard.py', CODE), True),
        ('refusal_probe_v8', dz('refusal_probe.py', CODE, scratch), True),
        ('kappa_calibration_repeats', dz('kappa_calibration.py', CODE, os.path.join(K, 'calibration-repeats.json')),
         False),
        ('overhead_measure', dz('overhead_measure.py', CODE, os.path.join(OV, 'overhead.json')), False),
        ('survivor_cap_measure', dz('survivor_cap_measure.py', CODE, os.path.join(K, 'calibration-repeats.json'),
                                    os.path.join(OV, 'survivor-cap.json')), False),
        ('ci_calibration_local_check', dz('ci_local_check.py', CI, scratch), True),
    ]
    env = dict(os.environ, TMPDIR=scratch)
    g = ['git', '-c', 'gc.auto=0', '-c', 'maintenance.auto=false', '-C', CODE]
    head = subprocess.run(g + ['rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip() or None
    clean = subprocess.run(g + ['status', '--porcelain', '--untracked-files=all', '--', os.path.dirname(CODE)],
                           capture_output=True, text=True).stdout.strip() == ''
    rec = []

    def rel(x):
        if x.startswith(R5):
            return 'stage0/code-r5' + x[len(R5):]
        if x.startswith(CI):
            return 'stage0/layer2/ci' + x[len(CI):]
        if x.startswith(E1CHECK):
            return 'stage0/amendments/E1-check' + x[len(E1CHECK):]
        if x.startswith(CODE):
            return 'stage0/layer2/code' + x[len(CODE):]
        if x.startswith(ev):
            return 'stage0/layer2/design' + x[len(ev):]
        if x.startswith(scratch):
            return '<scratch>' + x[len(scratch):]
        return 'python3' if x == py else x
    try:
        for name, cmd, check_O in steps:
            t0 = time.time()
            p = subprocess.run(cmd, capture_output=True, text=True, cwd=runs, env=env)
            dur = round(time.time() - t0)
            out = os.path.join(runs, name + '.out')
            with open(out, 'w') as f:
                f.write(p.stdout)
            with open(os.path.join(runs, name + '.err'), 'w') as f:
                f.write(p.stderr)
            entry = {'step': name, 'command': ' '.join(rel(x) for x in cmd), 'exit': p.returncode, 'seconds': dur,
                     'stdout_sha256': sha(out), 'stderr_sha256': sha(os.path.join(runs, name + '.err')),
                     'retained_stdout': 'stage0/layer2/design/runs/%s.out' % name,
                     'retained_stderr': 'stage0/layer2/design/runs/%s.err' % name}
            if check_O:
                q = subprocess.run([cmd[0], '-I', '-B', '-O'] + cmd[3:], capture_output=True, text=True, cwd=runs,
                                   env=env)
                if check_O is True:
                    entry['O_mode_identical'] = q.stdout == p.stdout and q.returncode == p.returncode
                else:
                    entry['O_mode_identical'] = q.returncode == p.returncode and all(
                        sha(os.path.join(W, a)) == sha(os.path.join(W, b)) for a, b in check_O)
                    entry['O_compared_files'] = check_O
            rec.append(entry)
            print(name, entry['exit'], dur, 's', file=sys.stderr)
    finally:
        shutil.rmtree(scratch, ignore_errors=True)
    files = {}
    for d, label in ((CODE, 'stage0/layer2/code'), (ev, 'stage0/layer2/design'), (CI, 'stage0/layer2/ci')):
        for fn in sorted(os.listdir(d)):
            if fn.endswith('.py') or fn.endswith('.yml') or fn == 'LAYER2-MANIFEST.json':
                files[label + '/' + fn] = sha(os.path.join(d, fn))
    toy = {'stage0/layer2/design/toyrun/' + fn: sha(os.path.join(W, fn)) for fn in sorted(os.listdir(W))}
    kap = {'stage0/layer2/design/kappa/' + fn: sha(os.path.join(K, fn)) for fn in sorted(os.listdir(K))}
    kap.update({'stage0/layer2/design/overhead/' + fn: sha(os.path.join(OV, fn)) for fn in sorted(os.listdir(OV))})
    manifest = {'python': sys.version.split()[0], 'platform': platform.platform(),
                'note': 'NP-AVG-1 Stage 0 Layer 2 design evidence (WIP / UNREVIEWED, not frozen): toy, planted and '
                        'small-window instances, S6\'s carrier and v8 configuration combinatorics only; no closure '
                        'on v8\'s configuration class (the v8 profile is refused without an authorization artifact). '
                        'The quick mutant campaign is local; the full campaign is CI-only and pending owner-approved '
                        'dispatch. Timing steps (calibration_planted, dryrun_v8_estimate, kappa_calibration_repeats, overhead_measure, '
                        'survivor_cap_measure) '
                        'are not deterministic. Commit caveat (L2-R5): this evidence was produced on an uncommitted working tree; '
                        'the structured files record the HEAD at run time (field commit) and tree_clean = false, '
                        'so they are design evidence only. At the Layer-2 freeze the evidence is regenerated at a '
                        'recorded commit.',
                'head_at_run': head, 'tree_clean_at_run': clean,
                'code_sha256': files, 'toyrun_sha256': toy, 'kappa_sha256': kap, 'steps': rec}
    with open(os.path.join(ev, 'RUN-MANIFEST.json'), 'w') as f:
        json.dump(manifest, f, indent=1, sort_keys=True)
        f.write('\n')
    lines = ['# Stage 0 Layer 2 run manifest (design evidence)', '',
             'Python %s on %s.' % (manifest['python'], manifest['platform']), '', manifest['note'], '',
             'HEAD at run: `%s`; Layer-2 tree clean at run: %s.' % (head, clean), '',
             '| step | command | exit | s | -O identical | stdout SHA-256 |', '| --- | --- | --- | --- | --- | --- |']
    for e in rec:
        lines.append('| %s | `%s` | %d | %d | %s | `%s` |' % (e['step'], e['command'], e['exit'], e['seconds'],
                                                            e.get('O_mode_identical', 'n/a'), e['stdout_sha256']))
    lines += ['', '| file | SHA-256 |', '| --- | --- |'] + ['| %s | `%s` |' % kv for kv in files.items()]
    lines += ['', '| toy-run file | SHA-256 |', '| --- | --- |'] + ['| %s | `%s` |' % kv for kv in toy.items()]
    lines += ['', '| kappa calibration file | SHA-256 |', '| --- | --- |'] + ['| %s | `%s` |' % kv for kv in kap.items()]
    with open(os.path.join(ev, 'RUN-MANIFEST.md'), 'w') as f:
        f.write('\n'.join(lines) + '\n')


if __name__ == '__main__':
    main()
