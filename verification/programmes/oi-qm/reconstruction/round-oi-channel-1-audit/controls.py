#!/usr/bin/env python3
"""Frozen controls for OI-CHANNEL-1; no network and no imported probe code."""
import argparse
import hashlib
from pathlib import Path
import re
import subprocess
import sys

ROUND = 'verification/programmes/oi-qm/reconstruction/round-oi-channel-1-audit/'
PROBE = 'verification/lean/oi_channel1_check.py'
WORKFLOW = '.github/workflows/verify.yml'
D = '9f9f8257a980a1819fbbc1dc0019917cf8678626'
PROBE_SHA = '9937b6ffca6cf570cf7e1c3267ba1525ead48ada4d5f1e92959ec0f603baebff'
OUTPUT_SHA = 'ec73839a23e1c2e051140ff9b56d47bbda4f9b55e37963ca1256500b36642da5'
READING = ('The finite stopped circuit realizes the channel formula at depths 0 through 6 by exact arithmetic. '
           'The all-depth recurrence and the universal cone arguments are written proofs. '
           'Transfer to an arbitrary pair cone and the general-k InstAvail witness remain additional obligations. '
           'This audit does not establish unconditional quantum reconstruction or full-model independence.')


def sha(b):
    return hashlib.sha256(b).hexdigest()


def git(*args):
    return subprocess.check_output(['git', *args])


def predicted_workflow(base):
    text = base.decode()
    anchor = '  # Act 42. Two shards run on every event;'
    job = ('  probes_oichannel1:\n'
           '    name: Numerical probes / OI channel protocol\n'
           '    runs-on: ubuntu-latest\n'
           '    steps:\n'
           '      - uses: actions/checkout@v4\n'
           '        with:\n'
           '          fetch-depth: 0\n'
           '      - uses: actions/setup-python@v5\n'
           '        with:\n'
           "          python-version: '3.11'\n"
           '      - name: Exact channel and cone controls\n'
           '        run: python3 -I -B verification/lean/oi_channel1_check.py\n'
           '      - name: Audit control mutation tests\n'
           '        run: python3 -I -B '+ROUND+'controls.py --self-test\n\n')
    replacements = [
        (anchor, job + anchor),
        ('probes_kt4prem1, probes_a42_witness', 'probes_kt4prem1, probes_oichannel1, probes_a42_witness'),
        ('          KT4PREM1_RESULT: ${{ needs.probes_kt4prem1.result }}\n',
         '          KT4PREM1_RESULT: ${{ needs.probes_kt4prem1.result }}\n'
         '          OICHANNEL1_RESULT: ${{ needs.probes_oichannel1.result }}\n'),
        ('          echo "kt4prem1=${KT4PREM1_RESULT}"\n',
         '          echo "kt4prem1=${KT4PREM1_RESULT}"\n'
         '          echo "oichannel1=${OICHANNEL1_RESULT}"\n'),
        ('          test "${KT4PREM1_RESULT}" = success\n',
         '          test "${KT4PREM1_RESULT}" = success\n'
         '          test "${OICHANNEL1_RESULT}" = success\n'),
    ]
    for old, new in replacements:
        if text.count(old) != 1:
            raise ValueError('workflow splice anchor is not unique')
        text = text.replace(old, new)
    return text.encode()


def failures(files, original, freeze, output, stderr, rc, result_required):
    errors = []
    if sha(files.get(PROBE, b'')) != PROBE_SHA:
        errors.append('P')
    if files.get(WORKFLOW) != predicted_workflow(original[WORKFLOW]):
        errors.append('W')
    for path in original:
        if path != WORKFLOW and files.get(path) != original[path]:
            errors.append('L')
    if files.get(ROUND+'preregistration.md') != freeze:
        errors.append('F')
    control_hash = re.search(r'^Controls SHA256: ([0-9a-f]{64})$', freeze.decode(), re.M)
    if not control_hash or sha(files.get(ROUND+'controls.py', b'')) != control_hash.group(1):
        errors.append('C')
    expected = {'preregistration.md', 'controls.py'} | ({'result.md'} if result_required else set())
    actual = {p[len(ROUND):] for p in files if p.startswith(ROUND)}
    if actual != expected:
        errors.append('R')
    if rc or stderr or sha(output) != OUTPUT_SHA:
        errors.append('V')
    if result_required:
        result = files.get(ROUND+'result.md', b'').decode()
        if result.count('Outcome: OI-CHANNEL-1-READ') != 1 or result.count(READING) != 1:
            errors.append('S')
        if 'CHANNEL-CHECK: PASS; 17 checks; 140 matrix-unit cases' not in result:
            errors.append('S')
        rest = result.replace(READING, '').lower()
        if any(x in rest for x in ('establishes unconditional', 'kernel-certified', 'sources h3',
                                  'full-model independence established', 'oi implies qm')):
            errors.append('S')
    return sorted(set(errors))


def self_test(probe_path, workflow_path):
    probe = Path(probe_path).read_bytes()
    base = Path(workflow_path).read_bytes() if workflow_path else git('show', D+':'+WORKFLOW)
    proc = subprocess.run([sys.executable, '-I', '-B', probe_path], capture_output=True)
    original = {WORKFLOW: base, 'kernel-source': b'unchanged kernel'}
    freeze = ('frozen prospective scope\nControls SHA256: '+sha(b'controls')+'\n').encode()
    files = {PROBE: probe, WORKFLOW: predicted_workflow(base), 'kernel-source': original['kernel-source'],
             ROUND+'preregistration.md': freeze, ROUND+'controls.py': b'controls',
             ROUND+'result.md': ('Outcome: OI-CHANNEL-1-READ\n'+READING+
                               '\nCHANNEL-CHECK: PASS; 17 checks; 140 matrix-unit cases\n').encode()}
    def run(f, out=proc.stdout, err=proc.stderr, rc=proc.returncode):
        return failures(f, original, freeze, out, err, rc, True)
    if run(files):
        raise ValueError('positive fixture fails '+str(run(files)))
    mutations = [(PROBE, b'changed', 'P'), (WORKFLOW, base, 'W'), ('kernel-source', b'changed', 'L'),
                 (ROUND+'preregistration.md', b'changed', 'F'), (ROUND+'extra', b'extra', 'R'),
                 (ROUND+'result.md', b'overstated result', 'S'), (ROUND+'controls.py', b'changed', 'C'),
                 (ROUND+'result.md', files[ROUND+'result.md']+b'It establishes unconditional reconstruction.', 'S')]
    for path, value, code in mutations:
        changed = dict(files); changed[path] = value
        if code not in run(changed):
            raise ValueError('mutation missed '+code)
    for out, err, rc in [(b'PASS', b'', 0), (proc.stdout, b'error', 0), (proc.stdout, b'', 1)]:
        if 'V' not in run(files, out, err, rc):
            raise ValueError('output mutation missed V')
    print('controls self-test: PASS; positive fixture and 11 mutations')


def check(head, freeze):
    paths = [WORKFLOW, 'verification/lean-mathlib/OIBridge/OperationalValidity.lean',
             'verification/lean-mathlib/OIBridge/ImplementationLocality.lean']
    original = {p: git('show', D+':'+p) for p in paths}
    names = git('ls-tree', '-r', '--name-only', head, '--', ROUND).decode().splitlines()
    files = {p: git('show', head+':'+p) for p in set(paths+[PROBE]+names)}
    fixed = git('show', freeze+':'+ROUND+'preregistration.md')
    execution = git('diff', '--name-only', D, head).decode().splitlines()
    allowed = {PROBE, WORKFLOW, ROUND+'preregistration.md', ROUND+'controls.py', ROUND+'result.md'}
    if not set(execution) <= allowed:
        raise ValueError('G: changed path outside scope')
    frozen = git('diff', '--name-only', D, freeze).decode().splitlines()
    if frozen != [ROUND+'preregistration.md']:
        raise ValueError('G: freeze delta is not the preregistration alone')
    on_disk = Path(PROBE).read_bytes()
    if on_disk != files[PROBE]:
        raise ValueError('P: local probe differs from checked object')
    if Path(__file__).read_bytes() != files[ROUND+'controls.py']:
        raise ValueError('C: running controls differ from checked object')
    proc = subprocess.run([sys.executable, '-I', '-B', PROBE], capture_output=True)
    required = ROUND+'result.md' in files
    failed = failures(files, original, fixed, proc.stdout, proc.stderr, proc.returncode, required)
    if failed:
        raise ValueError('controls failed: '+','.join(failed))
    print('controls: PASS')
    sys.stdout.write(proc.stdout.decode())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('head', nargs='?')
    parser.add_argument('--freeze')
    parser.add_argument('--self-test', action='store_true')
    parser.add_argument('--probe', default=PROBE)
    parser.add_argument('--workflow')
    args = parser.parse_args()
    try:
        if args.self_test:
            self_test(args.probe, args.workflow)
        elif args.head and args.freeze:
            check(args.head, args.freeze)
        else:
            parser.error('head and --freeze, or --self-test, required')
    except (ValueError, subprocess.CalledProcessError) as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
