"""NP-AVG-1 Stage 0 evidence driver (toys, planted sets, small windows, S6 only).
Usage: python3 -I -B s0run.py <evidence-dir>
Runs every check, compares normal and -O output where the output is deterministic,
and writes <evidence-dir>/runs/* and <evidence-dir>/RUN-MANIFEST.json and .md."""
import hashlib
import json
import os
import platform
import subprocess
import sys
import time

CODE = os.path.dirname(os.path.abspath(__file__))


def sha(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        h.update(f.read())
    return h.hexdigest()


def main():
    ev = os.path.abspath(sys.argv[1])
    runs = os.path.join(ev, 'runs')
    os.makedirs(runs, exist_ok=True)
    py = sys.executable
    steps = [
        ('controls_frozen_full', [py, '-I', '-B', os.path.join(CODE, 's0controls.py')], True),
        ('s6_po8_proofcheck', [py, '-I', '-B', os.path.join(CODE, 's0s6.py')], True),
        ('mutants_quick', [py, '-I', '-B', os.path.join(CODE, 's0mutants.py')], False),
        ('mutants_full', [py, '-I', '-B', os.path.join(CODE, 's0mutants.py'), '--full'], False),
        ('toy_rerun_L4', [py, '-I', '-B', os.path.join(ev, 'rerun.py'), ev], False),
        ('toy_planted', [py, '-I', '-B', os.path.join(ev, 'planted.py'), ev], False),
        ('toy_radius_mutants', [py, '-I', '-B', os.path.join(ev, 'radius_mutants.py'), ev], False),
        ('toy_exact_small', [py, '-I', '-B', os.path.join(ev, 'exact_small.py'), ev], False),
    ]
    rec = []
    for name, cmd, check_O in steps:
        t0 = time.time()
        p = subprocess.run(cmd, capture_output=True, text=True, cwd=runs)
        dur = round(time.time() - t0)
        out = os.path.join(runs, name + '.out')
        with open(out, 'w') as f:
            f.write(p.stdout)
        entry = {'step': name, 'command': ' '.join(os.path.relpath(c, ev) if c.startswith(ev) else
                                                   (os.path.relpath(c, os.path.dirname(ev)) if c.startswith(os.path.dirname(ev)) else c)
                                                   for c in cmd),
                 'exit': p.returncode, 'seconds': dur, 'stdout_sha256': sha(out),
                 'stderr_tail': p.stderr[-300:]}
        if check_O:
            cmdO = [cmd[0], '-I', '-B', '-O'] + cmd[3:]
            q = subprocess.run(cmdO, capture_output=True, text=True, cwd=runs)
            entry['O_mode_identical'] = (q.stdout == p.stdout and q.returncode == p.returncode)
        rec.append(entry)
        print(name, entry['exit'], dur, 's', file=sys.stderr)
    files = {}
    for d, label in ((CODE, 'stage0-code'), (ev, 'stage0-design-r2')):
        for fn in sorted(os.listdir(d)):
            if fn.endswith('.py'):
                files[label + '/' + fn] = sha(os.path.join(d, fn))
    manifest = {'python': sys.version.split()[0], 'platform': platform.platform(),
                'note': 'toys, planted sets, small exhaustive windows and the S6 reference structure only; '
                        'v8 configuration class not run (s0geom refuses it)',
                'code_sha256': files, 'steps': rec}
    with open(os.path.join(ev, 'RUN-MANIFEST.json'), 'w') as f:
        json.dump(manifest, f, indent=1, sort_keys=True)
    lines = ['# Stage 0 run manifest', '', 'Python %s on %s.' % (manifest['python'], manifest['platform']), '',
             manifest['note'] + '.', '', '| step | command | exit | s | -O identical | stdout SHA-256 |',
             '| --- | --- | --- | --- | --- | --- |']
    for e in rec:
        lines.append('| %s | `%s` | %d | %d | %s | `%s` |' % (e['step'], e['command'], e['exit'], e['seconds'],
                                                            e.get('O_mode_identical', 'n/a'), e['stdout_sha256']))
    lines += ['', '| file | SHA-256 |', '| --- | --- |'] + ['| %s | `%s` |' % kv for kv in files.items()]
    with open(os.path.join(ev, 'RUN-MANIFEST.md'), 'w') as f:
        f.write('\n'.join(lines) + '\n')


if __name__ == '__main__':
    main()
