#!/usr/bin/env python3
"""Frozen adoption controls; no imports from the checker or Lean implementation."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

META = {'d': 'f2415108601a9c36bb985b3374c56f0eb34c2962', 'family': {'name': 'Finite stopped-channel protocols constructed from primitive resources (round OI-FINITE-PROTOCOL-1, reconstruction)', 'modules': ['BridgeFiniteProtocol'], 'status': 'kernel-only', 'manuscript': [], 'note': 'Conditional finite-depth availability through InstAvail readout, op, bind, coarse and discard. The actual uniformly attached ancilla is reset internally. From Architecture and explicit circuit/reset/correction memberships, finite_protocol_available constructs every finite depth; balanced_stopped_formula derives the O14 channel formula and balanced_finite_available combines availability with it. finite_protocol_spectator additionally requires ContextStable and LabelInvariant. No AvailableChannelApproximation sequence is a premise. Primitive memberships, convergence, availability of a limit, physical state/test identification, validity or preservation of an arbitrary pair cone, arbitrary finite-carrier reconstruction and unconditional OI reconstruction remain unestablished here. Carried by no manuscript.'}, 'workflow_splices': [['  # Act 42. Two shards run on every event;', "  probes_oifiniteprotocol1:\n    name: Numerical probes / OI finite protocol\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n        with:\n          fetch-depth: 0\n      - uses: actions/setup-python@v5\n        with:\n          python-version: '3.11'\n      - name: Exact finite protocol controls\n        run: python3 -I -B verification/lean/oi_finite_protocol_check.py\n      - name: Adoption control mutation tests\n        run: python3 -I -B verification/programmes/oi-qm/reconstruction/round-oi-finite-protocol-1/controls.py --self-test\n\n  # Act 42. Two shards run on every event;"], ['probes_oichannel1, probes_a42_witness', 'probes_oichannel1, probes_oifiniteprotocol1, probes_a42_witness'], ['          OICHANNEL1_RESULT: ${{ needs.probes_oichannel1.result }}\n', '          OICHANNEL1_RESULT: ${{ needs.probes_oichannel1.result }}\n          OIFINITEPROTOCOL1_RESULT: ${{ needs.probes_oifiniteprotocol1.result }}\n'], ['          echo "oichannel1=${OICHANNEL1_RESULT}"\n', '          echo "oichannel1=${OICHANNEL1_RESULT}"\n          echo "oifiniteprotocol1=${OIFINITEPROTOCOL1_RESULT}"\n'], ['          test "${OICHANNEL1_RESULT}" = success\n', '          test "${OICHANNEL1_RESULT}" = success\n          test "${OIFINITEPROTOCOL1_RESULT}" = success\n']], 'roadmap_splice': ['- **K3 — the operations. CONDITIONAL** on reaching complex matrix kinematics. A quantum\n  architecture — an architecture that is context-, label- and dagger-stable and drives the\n  elementary transitions (`DrivesElementary`) — generates a theory carrying every finite\n  endomorphic quantum operation (`genTheory_qm_of_quantumArchitecture`), through composite unitary\n  control (`control_of_lieRank`) and the full instruments (`fullInstruments_of_control`). The typed\n  characterization covers the finite rectangular Kraus endpoint (`typed_determined_iff`).\n', '- **K3 — the operations. CONDITIONAL** on reaching complex matrix kinematics. A quantum\n  architecture — an architecture that is context-, label- and dagger-stable and drives the\n  elementary transitions (`DrivesElementary`) — generates a theory carrying every finite\n  endomorphic quantum operation (`genTheory_qm_of_quantumArchitecture`), through composite unitary\n  control (`control_of_lieRank`) and the full instruments (`fullInstruments_of_control`). The typed\n  characterization covers the finite rectangular Kraus endpoint (`typed_determined_iff`). Round OI-FINITE-PROTOCOL-1 constructs every finite\n  stopped-channel depth from an architecture and explicit circuit/reset/correction\n  memberships (`finite_protocol_available`); its balanced circuit obeys the all-depth\n  formula (`balanced_stopped_formula`) and yields conditional availability\n  (`balanced_finite_available`). The ancilla starts uniformly mixed and is reset inside\n  the protocol. Spectator extension additionally requires `ContextStable` and\n  `LabelInvariant` (`finite_protocol_spectator`). Primitive memberships, convergence and\n  availability of a limiting drive, physical state/test identification and preservation\n  of an arbitrary pair cone remain separate obligations. K3 retains its conditional status.\n'], 'body_sha256': '016c8e724c73ae358fbcae3646c0b7e975beed3ddd8056d9197bf2f79a27b847', 'pins': {'verification/lean-mathlib/OIBridge/BridgeFiniteProtocol.lean': {'sha256': 'd350d235b1b8b1379f9ea9dafcdb6be7a9f256f0eda96633ff119a7904c7cce4', 'blob': 'baf7a6d421597b115d588b824524e3bc38a946d6'}, 'verification/lean/oi_finite_protocol_check.py': {'sha256': '5a4f0862b953e4d07e201ecbe03291d0cfa6e6df615dd4b6f25f723052927839', 'blob': 'ef104005b47ef5323a2a937d5df3c7c993f972d4'}, 'verification/lean-mathlib/OIBridge.lean': {'sha256': 'db19e164d0843cddffa1e8a5f281911b0742e9f1b5dc794fc287333ddc75847a', 'blob': '03a29e2fd41634103d6a274f3fb36056ed5b6826'}, 'verification/lean-manuscript-census.json': {'sha256': '0803c812cafeffbbbd7b211e5d9420ab3372f29ac31fe35655ad471192423aa9', 'blob': '88206432a44074cbd1bfb46fff1847d2dcb425f4'}, '.github/workflows/verify.yml': {'sha256': '05020b877f667199f647ce50b00e446670e2e1fea37854e5a00972b879eb089d', 'blob': 'c2203af2f9f668442561f02e6a936c736378d362'}, 'verification/ROADMAP.md': {'sha256': '971b868db5e81ca7eaad17dd1d39c97558a4553f3ddad9e16162bd65312af615', 'blob': 'ba7b23d4f1b0a2b78722dbc15b3fc51193f147d8'}}, 'anchors': {'verification/lean-mathlib/OIBridge.lean': 'e5af9614009889dab616d7f02f75bb395f1ae1fb01307f46ef82d3b282b4c313', 'verification/lean-manuscript-census.json': 'cdadb02e0463366c036834f2ca58ae904ad70e05dfe981fd1f37d9bc928e0bbf', '.github/workflows/verify.yml': 'bd71bdc270753be8296c4a5c9723e23673c2f8acdaa9417fb70a6ddd6cbe2443', 'verification/ROADMAP.md': 'a64835c2107131530f2396311b3e8fa291bc690462ffbbde225f3479d89a2c2c', 'verification/lean-mathlib/OIBridge/ImplementationLocality.lean': '4e5b4b22298dfba7b0ee7ba26109ef3090eb48b23227734bb26bbf6834a545ac', 'verification/lean-mathlib/OIBridge/OperationalValidity.lean': 'ba316747d23820f75f4bbd25105d87a85febb3bd1d0eaa123913b629b34f05f0'}}
ROUND = 'verification/programmes/oi-qm/reconstruction/round-oi-finite-protocol-1/'
MODULE = 'verification/lean-mathlib/OIBridge/BridgeFiniteProtocol.lean'
PROBE = 'verification/lean/oi_finite_protocol_check.py'
WORKFLOW = '.github/workflows/verify.yml'
AGGREGATE = 'verification/lean-mathlib/OIBridge.lean'
REGISTRY = 'verification/lean-manuscript-census.json'
ROADMAP = 'verification/ROADMAP.md'
OUTPUT_SHA = 'f33e3c97bd1baa7f4b583f798cf0ecdec185860d37f69523f31128e4131d35e1'
RESULT = '''# OI-FINITE-PROTOCOL-1 — finite stopped protocol from primitive resources

Outcome: OI-FINITE-PROTOCOL-1-PROVED

Every finite stopped-channel depth is InstAvail from Architecture and explicit circuit/reset/correction memberships, using the existing readout, op, bind, coarse and discard rules. The uniformly mixed ancilla is reset inside the protocol. The balanced circuit's corrected branches and all-depth stopped formula are proved for every input matrix. No available approximation sequence is a premise.

Spectator availability additionally requires ContextStable and LabelInvariant. Primitive memberships, convergence, availability of a limiting drive, physical state/test identification and validity or preservation of an arbitrary pair cone remain separate obligations. K2 remains open, K3 remains conditional, and arbitrary finite-carrier reconstruction and the full operation/instrument correspondence retain their existing obligations. This package does not establish unconditional OI reconstruction or full-model independence.

Exact controls: FINITE-PROTOCOL: PASS; 10 groups; 36 stopped matrix-unit cases
Arithmetic is in Q(i). Replay is byte-identical, stderr is empty and exit code is zero. Removing reset, removing correction and continuing after success each disagrees with the intended map on the 0,1 matrix unit. These finite controls do not prove the universal theorem.

The adopted module is kernel-only and imports only existing main ImplementationLocality and Mathlib tactics. Its proof body is unchanged from the measured #810 design head 708153423ffb5ea4fe27663654431650b5a2e48a. Historical design measurements and new predictive evidence are recorded separately in the preregistration; neither is an F/E attestation.

F: {F}
F workflow run: {F_RUN}
S1: {S1}
S1 workflow run: {S1_RUN}

Successful Build and fourteen standard named axiom reports without sorryAx are required, alongside all-green exact-head host checks before E designation. Owner E designation and host attestations are recorded in the receipt. Local content controls do not certify host facts.
'''


def sha(data):
    return hashlib.sha256(data).hexdigest()


def git(*args):
    return subprocess.check_output(['git', *args])


def originals():
    data = {p: git('show', META['d'] + ':' + p) for p in META['anchors']}
    if any(sha(data[p]) != digest for p, digest in META['anchors'].items()):
        raise ValueError('D anchor mismatch')
    return data


def expected(original):
    output = {}
    aggregate = original[AGGREGATE]
    anchor = b'import OIBridge.ImplementationLocality\n'
    if aggregate.count(anchor) != 1:
        raise ValueError('non-unique aggregate anchor')
    output[AGGREGATE] = aggregate.replace(anchor, anchor + b'import OIBridge.BridgeFiniteProtocol\n')
    registry = json.loads(original[REGISTRY])
    registry['families'].append(META['family'])
    output[REGISTRY] = (json.dumps(registry, indent=2, ensure_ascii=False) + '\n').encode()
    workflow = original[WORKFLOW].decode()
    for old, new in META['workflow_splices']:
        if workflow.count(old) != 1:
            raise ValueError('non-unique workflow anchor')
        workflow = workflow.replace(old, new)
    output[WORKFLOW] = workflow.encode()
    roadmap = original[ROADMAP].decode()
    old, new = META['roadmap_splice']
    if roadmap.count(old) != 1:
        raise ValueError('non-unique roadmap anchor')
    output[ROADMAP] = roadmap.replace(old, new).encode()
    return output


def result_ok(data, freeze_id, s1_id):
    text = data.decode(errors='replace')
    names = {}
    for field, pattern in [('F', '[0-9a-f]{40}'), ('S1', '[0-9a-f]{40}'),
                           ('F_RUN', '[1-9][0-9]*'), ('S1_RUN', '[1-9][0-9]*')]:
        label = {'F_RUN': 'F workflow run', 'S1_RUN': 'S1 workflow run'}.get(field, field)
        match = re.search('^' + label + ': (' + pattern + ')$', text, re.M)
        if not match:
            return False
        names[field] = match.group(1)
    return (names['F'] == freeze_id and names['S1'] == s1_id
            and text == RESULT.format(**names))


def failures(files, original, freeze, output, stderr, rc, required, freeze_id, s1_id):
    errors = []
    rebuilt = expected(original)
    for path, pin in META['pins'].items():
        wanted = rebuilt[path] if path in rebuilt else None
        pinned_sha = pin['sha256']
        if path == ROADMAP and not required:
            wanted = original[path]
            pinned_sha = META['anchors'][ROADMAP]
        actual = files.get(path, b'')
        if sha(actual) != pinned_sha:
            errors.append('pin:' + path)
        if wanted is not None:
            if actual != wanted:
                errors.append(path)
    module = files.get(MODULE, b'')
    body = module.split(b'-/', 1)[1] if b'-/' in module else b''
    if sha(body) != META['body_sha256']:
        errors.append('body')
    if files.get(ROUND + 'preregistration.md') != freeze:
        errors.append('freeze')
    control_hash = re.search(rb'^Controls SHA256: ([0-9a-f]{64})$', freeze, re.M)
    if (not control_hash or sha(files.get(ROUND + 'controls.py', b'')).encode() != control_hash.group(1)):
        errors.append('controls')
    population = {p[len(ROUND):] for p in files if p.startswith(ROUND)}
    if population != {'preregistration.md', 'controls.py'} | ({'result.md'} if required else set()):
        errors.append('population')
    if rc or stderr or sha(output) != OUTPUT_SHA:
        errors.append('measurement')
    if required and not result_ok(files.get(ROUND + 'result.md', b''), freeze_id, s1_id):
        errors.append('result')
    return errors


def self_test(probe):
    original = originals()
    # Immutable blobs reconstruct the original execution, so later changes to shared
    # aggregator/workflow/registry/roadmap cannot invalidate this round's fixture.
    rebuilt = expected(original)
    files = {p: rebuilt[p] if p in rebuilt else git('cat-file', 'blob', pin['blob'])
             for p, pin in META['pins'].items()}
    source = Path(probe).read_bytes()
    if sha(source) != META['pins'][PROBE]['sha256']:
        raise ValueError('live owned checker mismatch')
    proc = subprocess.run([sys.executable, '-I', '-B', probe], capture_output=True)
    control_bytes = Path(__file__).read_bytes()
    freeze = ('fixture\nControls SHA256: ' + sha(control_bytes) + '\n').encode()
    f, s1 = '1' * 40, '2' * 40
    files.update({ROUND+'preregistration.md': freeze, ROUND+'controls.py': control_bytes,
                  ROUND+'result.md': RESULT.format(F=f, S1=s1, F_RUN='1', S1_RUN='2').encode()})
    def run(values, required=True, out=proc.stdout, err=proc.stderr, rc=proc.returncode, freeze_id=f):
        return failures(values, original, freeze, out, err, rc, required, freeze_id, s1)
    if run(files):
        raise ValueError('S2 fixture failed ' + str(run(files)))
    s1_files = dict(files)
    del s1_files[ROUND+'result.md']
    s1_files[ROADMAP] = original[ROADMAP]
    if run(s1_files, False):
        raise ValueError('S1 fixture failed')
    mutations = 0
    for path in META['pins']:
        changed = dict(files); changed[path] += b'changed\n'
        if not run(changed):
            raise ValueError('file mutation missed ' + path)
        mutations += 1
    for path, value in [(ROUND+'preregistration.md', b'changed'),
                        (ROUND+'controls.py', b'changed'),
                        (ROUND+'extra', b'new'),
                        (ROUND+'result.md', files[ROUND+'result.md'] + b'OI implies QM.\n')]:
        changed = dict(files); changed[path] = value
        if not run(changed):
            raise ValueError('record mutation missed ' + path)
        mutations += 1
    for out, err, rc in [(b'PASS', b'', 0), (proc.stdout, b'error', 0), (proc.stdout, b'', 1)]:
        if 'measurement' not in run(files, out=out, err=err, rc=rc):
            raise ValueError('measurement mutation missed')
        mutations += 1
    if 'result' not in run(files, freeze_id='3'*40):
        raise ValueError('wrong F missed')
    mutations += 1
    # A self-consistent reconstruction must still fail if its declared immutable
    # pin is stale. Exercise metadata corruption, restoring scope after each check.
    for path in [AGGREGATE, REGISTRY, WORKFLOW, ROADMAP]:
        original_pin = META['pins'][path]['sha256']
        try:
            META['pins'][path]['sha256'] = '0' * 64
            if 'pin:' + path not in run(files):
                raise ValueError('stale shared pin missed ' + path)
        finally:
            META['pins'][path]['sha256'] = original_pin
        mutations += 1
    original_roadmap_anchor = META['anchors'][ROADMAP]
    try:
        META['anchors'][ROADMAP] = '0' * 64
        if 'pin:' + ROADMAP not in run(s1_files, False):
            raise ValueError('stale S1 roadmap anchor pin missed')
    finally:
        META['anchors'][ROADMAP] = original_roadmap_anchor
    mutations += 1
    print(f'controls self-test: PASS; S1/S2 fixtures and {mutations} rejected mutations')


def check(head, freeze_id):
    original = originals()
    if git('diff', '--name-only', META['d'], freeze_id).decode().splitlines() != [ROUND+'preregistration.md']:
        raise ValueError('D-to-F delta is not preregistration alone')
    git('merge-base', '--is-ancestor', freeze_id, head)
    commits = git('rev-list', '--reverse', head, '^'+freeze_id).decode().splitlines()
    if not commits:
        raise ValueError('execution is empty')
    prior = freeze_id
    allowed = set(META['pins']) | {ROUND+'controls.py', ROUND+'result.md'}
    for commit in commits:
        parents = git('show', '-s', '--format=%P', commit).decode().split()
        if parents != [prior]:
            raise ValueError('execution not linear')
        changed = set(git('diff', '--name-only', prior, commit).decode().splitlines())
        if not changed <= allowed:
            raise ValueError('changed path outside execution scope')
        prior = commit
    names = git('ls-tree', '-r', '--name-only', head, '--', ROUND).decode().splitlines()
    files = {p: git('show', head+':'+p) for p in set(META['pins']) | set(names)}
    fixed = git('show', freeze_id+':'+ROUND+'preregistration.md')
    if Path(PROBE).read_bytes() != files[PROBE] or Path(__file__).read_bytes() != files[ROUND+'controls.py']:
        raise ValueError('running sources differ from checked object')
    proc = subprocess.run([sys.executable, '-I', '-B', PROBE], capture_output=True)
    errors = failures(files, original, fixed, proc.stdout, proc.stderr, proc.returncode,
                      ROUND+'result.md' in files, freeze_id, commits[0])
    if errors:
        raise ValueError('controls failed: '+','.join(errors))
    print('controls: PASS')
    print(proc.stdout.decode(), end='')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('head', nargs='?')
    parser.add_argument('--freeze')
    parser.add_argument('--self-test', action='store_true')
    parser.add_argument('--probe', default=PROBE)
    args = parser.parse_args()
    try:
        if args.self_test:
            self_test(args.probe)
        elif args.head and args.freeze:
            check(args.head, args.freeze)
        else:
            parser.error('head and --freeze, or --self-test, required')
    except (ValueError, subprocess.CalledProcessError) as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
