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
    for line in (ROOT / 'SHA256SUMS').read_text().splitlines():
        expected, name = line.split('  ', 1)
        require(digest(ROOT / name) == expected, 'manifest mismatch: ' + name)
    reviewed = json.loads((ROOT / 'parallel_v3/review/INPUT-HASHES.json').read_text())
    for name, expected in reviewed.items():
        require(digest(ROOT / name) == expected, 'reviewed bytes changed: ' + name)
    tests = [('continuation', 'checks'), ('continuation', 'symbolic')]
    tests += [('parallel_v3/' + track, 'checks') for track in
              ('aux_routing', 'history_control', 'direct_reset', 'new_geometry')]
    tests += [('parallel_v3/review', name) for name in
              ('checks', 'sidecar_check', 'gadgets_check', 'contract_check',
               'geometry_check', 'herald_check')]
    tests += [('parallel_v3/integration', 'tagged_contract')]
    tests += [('junction_v4', 'checks')]
    with tempfile.TemporaryDirectory(prefix='native-y-replay-') as directory:
        work = Path(directory) / 'checkpoint'
        shutil.copytree(ROOT, work, ignore=shutil.ignore_patterns('__pycache__'))
        for source in work.rglob('*.py'):
            py_compile.compile(str(source), doraise=True)
        for folder, name in tests:
            script = work / folder / (name + '.py')
            expected = (work / folder / (name + '.out')).read_bytes()
            for options in ([], ['-O']):
                result = subprocess.run(
                    [sys.executable, *options, str(script)], cwd=work,
                    capture_output=True, timeout=180)
                require(result.returncode == 0,
                        'checker failed: ' + folder + '/' + name + '\n' +
                        result.stderr.decode(errors='replace'))
                require(result.stdout == expected,
                        'recorded output mismatch: ' + folder + '/' + name)
            print('PASS: ' + folder + '/' + name + ' normal/-O/recorded', flush=True)
    print('PASS: checkpoint replay', flush=True)


if __name__ == '__main__':
    main()
