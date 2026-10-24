"""Replay the scoped checkpoint without modifying its tracked scientific files."""
from pathlib import Path
import hashlib
import json
import py_compile
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    require(sys.argv[1:] in ([], ['--latest']), 'usage: replay.py [--latest]')
    for line in (ROOT / 'SHA256SUMS').read_text().splitlines():
        expected, name = line.split('  ', 1)
        require(digest(ROOT / name) == expected, 'manifest mismatch: ' + name)
    reviewed = json.loads((ROOT / 'parallel_v3/review/INPUT-HASHES.json').read_text())
    for name, expected in reviewed.items():
        require(digest(ROOT / name) == expected, 'reviewed bytes changed: ' + name)
    current_review = json.loads((ROOT / 'junction_v4/review/INPUT-HASHES.json').read_text())
    prefix = 'repo_checkpoint/payload/'
    for name, expected in current_review.items():
        if name.startswith(prefix):
            require(digest(ROOT / name[len(prefix):]) == expected,
                    'new reviewed bytes changed: ' + name)
    tests = [('continuation', 'checks'), ('continuation', 'symbolic')]
    tests += [('parallel_v3/' + track, 'checks') for track in
              ('aux_routing', 'history_control', 'direct_reset', 'new_geometry')]
    tests += [('parallel_v3/review', name) for name in
              ('checks', 'sidecar_check', 'gadgets_check', 'contract_check',
               'geometry_check', 'herald_check')]
    tests += [('parallel_v3/integration', 'tagged_contract')]
    tests += [('junction_v4', 'checks'), ('junction_v4/review', 'checks')]
    tests += [('six_source_v5/period', 'checks'), ('six_source_v5', 'checks'),
              ('six_source_v5/review', 'checks')]
    tests += [('outward_v6', 'checks'), ('outward_v6', 'correction_checks'),
              ('outward_v6/review', 'checks')]
    tests += [('reset_v7', 'probe'), ('reset_v7/review', 'checks')]
    tests += [('reset_v8', 'probe'), ('reset_v8/review', 'checks')]
    tests += [('history_v9', 'checks'), ('history_v9/review', 'checks'),
              ('reset_v9', 'checks'), ('reset_v9/review', 'checks'),
              ('reset_v9/review', 'history_corollary')]
    retained_v10 = [('branch_v10', 'checks'), ('branch_v10/review', 'checks'),
              ('herald_v10', 'checks'), ('herald_v10/review', 'checks'),
              ('layout_v10', 'checks'), ('layout_v10/review', 'checks'),
              ('branch_v10/local-controller', 'checks', [], 'single-result.json'),
              ('branch_v10/local-controller', 'checks', ['--symmetric'], 'symmetric-result.json'),
              ('branch_v10/local-controller/review', 'checks'),
              ('phase_joint_v10', 'checks'), ('phase_joint_v10/review', 'checks')]
    latest = [(folder, 'checks', [], 'result.json') for folder in (
        'native_v11', 'native_v11/review',
        'transport_audit_v1', 'transport_audit_v1/review',
        'history_v11', 'history_v11/review',
        'native_pool_v11', 'native_pool_v11/review')]
    tests = latest if sys.argv[1:] == ['--latest'] else tests + retained_v10 + latest
    with tempfile.TemporaryDirectory(prefix='native-y-replay-') as directory:
        work = Path(directory) / 'checkpoint'
        shutil.copytree(ROOT, work, ignore=shutil.ignore_patterns('__pycache__'))
        for source in work.rglob('*.py'):
            py_compile.compile(str(source), doraise=True)
        for spec in tests:
            folder, name = spec[:2]
            arguments = spec[2] if len(spec) > 2 else []
            explicit_output = spec[3] if len(spec) > 3 else None
            script = work / folder / (name + '.py')
            output_name = 'review-normal.out' if folder == 'junction_v4/review' else name + '.out'
            if folder in ('reset_v7', 'reset_v7/review', 'reset_v8'):
                output_name = 'results.json'
            if folder in ('reset_v8/review', 'reset_v9', 'reset_v9/review'):
                output_name = 'result.json'
            if folder in ('history_v9', 'history_v9/review'):
                output_name = 'results.json'
            if name == 'history_corollary':
                output_name = 'history-corollary-result.json'
            if folder.startswith(('branch_v10', 'herald_v10', 'phase_joint_v10')):
                output_name = 'result.json'
            if folder.startswith('layout_v10'):
                output_name = 'results.json'
            if explicit_output:
                output_name = explicit_output
            expected = (work / folder / output_name).read_bytes()
            for options in ([], ['-O']):
                result = subprocess.run(
                    [sys.executable, *options, str(script), *arguments], cwd=work,
                    capture_output=True, timeout=180)
                require(result.returncode == 0,
                        'checker failed: ' + folder + '/' + name + '\n' +
                        result.stderr.decode(errors='replace'))
                require(result.stdout == expected,
                        'recorded output mismatch: ' + folder + '/' + name)
            label = folder + '/' + name + (' ' + ' '.join(arguments) if arguments else '')
            print('PASS: ' + label + ' normal/-O/recorded', flush=True)
    print('PASS: checkpoint replay', flush=True)


if __name__ == '__main__':
    main()
