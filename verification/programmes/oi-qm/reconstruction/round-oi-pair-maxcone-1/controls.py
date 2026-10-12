#!/usr/bin/env python3
"""Frozen content controls for OI-PAIR-MAXCONE-1; host attestations are checked separately."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

D = 'f2415108601a9c36bb985b3374c56f0eb34c2962'
ROUND = 'verification/programmes/oi-qm/reconstruction/round-oi-pair-maxcone-1/'
PROBE = 'verification/lean/oi_maxcone_check.py'
SUPPORT = 'verification/lean/oi_maxcone_gaussian.py'
WORKFLOW = '.github/workflows/verify.yml'
ROOT = 'verification/lean-mathlib/OIBridge.lean'
REGISTRY = 'verification/lean-manuscript-census.json'
ROADMAP = 'verification/ROADMAP.md'
PIN = {'verification/lean-mathlib/OIBridge/EqvK2Schema.lean': 'c76991ba337ac3ac58a41eaa88c46af62e59a374117b31edecabaec9309f6a3e', 'verification/lean-mathlib/OIBridge/EqvK2Converse.lean': '58f97ca9a371b3d14148328a2816f953e6adc0d1067ea383cc802460aae26d56', 'verification/lean-mathlib/OIBridge/EqvK2Block.lean': '081b99696c104d6e3c4d50d6b9f1b7d5133976f89c9d5410ae5d3067a5b1d0ac', 'verification/lean-mathlib/OIBridge/EqvK2Generation.lean': '42c9e313ee35d7f5ee16cf0bee2abde2ad17867d6eaf65a76e5abb2be469c6d3', 'verification/lean-mathlib/OIBridge/BridgeDictionary.lean': 'f32304db1803ee31141f3a805ac9c15c7ea7c02042e6e2234c77f3863850e065', 'verification/lean-mathlib/OIBridge/BridgeConverge.lean': 'f1c43d1ca223c8a924a1afee55ee97a661e49079ec757c80df53aa5637de7c42', 'verification/lean-mathlib/OIBridge/EqvK2MaxCone.lean': '9222038440f742856480706c27569611bed15b82f650b3eab76c9c61e258169f', 'verification/lean-mathlib/OIBridge.lean': 'a031136f6c7eddc7c9d5cc0162119dfcd9bb5fa2ec8be996628a99cc94a400c8', 'verification/lean/oi_maxcone_check.py': 'd322c9139666c00821fbf85bb2c63dbf5b977ce329dca180bbf652b55c7ca72a', 'verification/lean/oi_maxcone_gaussian.py': '8e4573f6f5a916202cc5770809809bbbbabd682cc2aefd5d3e4567d2b0282df1', 'verification/lean-manuscript-census.json': 'd23abaf21d73f2410d932f47ff6f29e68fe3d12f482714c462c6276d807eb547', '.github/workflows/verify.yml': '62fb29a5348e02828044c4e34d8a1281b00c20d4c7e0a5de9aefc5ab43d1535d'}
PIN_BLOB = {'verification/lean-mathlib/OIBridge/EqvK2Schema.lean': 'c634beb82193eb7372ccaf498dba56dd2ec8538c', 'verification/lean-mathlib/OIBridge/EqvK2Converse.lean': 'f01fc607eab88d8d8ffe24b48d164830e2dad3e6', 'verification/lean-mathlib/OIBridge/EqvK2Block.lean': '23c74144073ef001d69c718f1fa3c0be5b8c1896', 'verification/lean-mathlib/OIBridge/EqvK2Generation.lean': '1251afd7aa8667cf73fb8b19a669e6a3d7bb026e', 'verification/lean-mathlib/OIBridge/BridgeDictionary.lean': 'f997b33ec7ff8402246c7250d38f3e935e4f92df', 'verification/lean-mathlib/OIBridge/BridgeConverge.lean': 'e1647b1dc6585073b5b27be2b5e7e13ac803eb0c', 'verification/lean-mathlib/OIBridge/EqvK2MaxCone.lean': '5b4b98c8e81e21eb002de25383eada381b65e3dd', 'verification/lean-mathlib/OIBridge.lean': '281b6a52412ea3e51cb412997c9984d5806bad82', 'verification/lean/oi_maxcone_check.py': '09d2abcd66f0e230b1a1895e015cb3183297f900', 'verification/lean/oi_maxcone_gaussian.py': 'eff710c93f2211b90472eec8f6d3d5884e3c9421', 'verification/lean-manuscript-census.json': 'dd59b8938c12d87be9d3a007900eca2c3020518a', '.github/workflows/verify.yml': '7c85970db08f8326ff3bca86c62cebab1e3159db'}
BASE_HASH = {'.github/workflows/verify.yml': 'bd71bdc270753be8296c4a5c9723e23673c2f8acdaa9417fb70a6ddd6cbe2443', 'verification/lean-mathlib/OIBridge.lean': 'e5af9614009889dab616d7f02f75bb395f1ae1fb01307f46ef82d3b282b4c313', 'verification/lean-manuscript-census.json': 'cdadb02e0463366c036834f2ca58ae904ad70e05dfe981fd1f37d9bc928e0bbf', 'verification/ROADMAP.md': 'a64835c2107131530f2396311b3e8fa291bc690462ffbbde225f3479d89a2c2c', 'verification/lean-mathlib/OIBridge/OperationalValidity.lean': 'ba316747d23820f75f4bbd25105d87a85febb3bd1d0eaa123913b629b34f05f0', 'verification/lean-mathlib/OIBridge/ImplementationLocality.lean': '4e5b4b22298dfba7b0ee7ba26109ef3090eb48b23227734bb26bbf6834a545ac'}
OUTPUT_SHA = '492bfc19254a39193222a90e828dc16c4ae58bc434bb00c90f03931c6a0adeee'
ROADMAP_SHA = 'a6a4e9e7f5d1e3e363c9abef34e1123002fb1a9494c65bef690450f833b3e160'
FAMILY = {'name': 'conditional pair-cone reconstruction using exact block generation, explicit cone closure and product-test positivity (round OI-PAIR-MAXCONE-1)', 'modules': ['EqvK2Schema', 'EqvK2Converse', 'EqvK2Block', 'EqvK2Generation', 'BridgeDictionary', 'BridgeConverge', 'EqvK2MaxCone'], 'status': 'kernel-only', 'manuscript': [], 'note': "Conditional pair-level infrastructure on W 3. EqvK2MaxCone.subset_Q3_of_maxCone_block uses maxCone and block invariance for the upper inclusion; Q3_subset_of_products_cone_block uses products, addition, nonnegative scaling and block invariance for the lower. pairCone_eq_Q3_of_drive_maxCone assembles equality using E19's exact CNOT/full-flow/cyclic generation. The two block and generator equivalences have separately named witnesses. pairCone_eq_Q3_of_sharp_available obtains the upper bound from product-test validity on an available family containing sharpFamily 3; it assumes neither full affine effect availability nor EffectsOn in that direction. Self-duality, closedness and assumed ReachPure are absent from the replacement headlines. The six auxiliary modules supply the measured dictionary, generation, reachability and conditional transfer identities. This family is carried by no manuscript. The state/test identification, products and cone structure, pair validity, CNOT invariance and the full-flow/cyclic invariance remain explicit premises; no bare OI source, arbitrary finite-carrier reconstruction or full-model independence is asserted. Record: verification/programmes/oi-qm/reconstruction/round-oi-pair-maxcone-1/."}
SPLICES = [['  # Act 42. Two shards run on every event;', "  probes_oimaxcone:\n    name: Numerical probes / OI pair maxCone\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n        with:\n          fetch-depth: 0\n      - uses: actions/setup-python@v5\n        with:\n          python-version: '3.11'\n      - name: Exact maxCone and cone controls\n        run: python3 -I -B verification/lean/oi_maxcone_check.py\n      - name: Native control mutation tests\n        run: python3 -I -B verification/programmes/oi-qm/reconstruction/round-oi-pair-maxcone-1/controls.py --self-test\n\n  # Act 42. Two shards run on every event;"], ['probes_oichannel1, probes_a42_witness', 'probes_oichannel1, probes_oimaxcone, probes_a42_witness'], ['          OICHANNEL1_RESULT: ${{ needs.probes_oichannel1.result }}\n', '          OICHANNEL1_RESULT: ${{ needs.probes_oichannel1.result }}\n          OIMAXCONE_RESULT: ${{ needs.probes_oimaxcone.result }}\n'], ['          echo "oichannel1=${OICHANNEL1_RESULT}"\n', '          echo "oichannel1=${OICHANNEL1_RESULT}"\n          echo "oimaxcone=${OIMAXCONE_RESULT}"\n'], ['          test "${OICHANNEL1_RESULT}" = success\n', '          test "${OICHANNEL1_RESULT}" = success\n          test "${OIMAXCONE_RESULT}" = success\n']]
ROADMAP_SPLICE = ("- **K2 — the composite. OPEN.** Read-only research has mapped a candidate `d = 3` composition\n  route, but no governed round records the classification or the cone theorem. Its obligations\n  include local tomography, which DIM-1's carrier `W d` encodes as a premise, the composite cone,\n  local actions compatible with it, the formal composition theorem, the antiunitary and\n  complete-positivity bridge, and the relation to the K3 machinery; all are open. K2 does not\n  discharge H-Bell.", "- **K2 — the composite. OPEN.** OI-PAIR-MAXCONE-1 records the conditional two-token cone theorem:\n  a set containing the products of `eball 3`, closed under addition and nonnegative scaling,\n  contained in `maxCone`, and invariant under CNOT and the full rotation/cyclic actions is `Q3`\n  (`pairCone_eq_Q3_of_drive_maxCone`). Product-test validity on an available family containing\n  the sharp tests suffices for the upper bound (`pairCone_eq_Q3_of_sharp_available`). The\n  hypotheses remain explicit; the theorem does not derive them for the observer's pair cone.\n  Local tomography, the physical state/test identification and cone realization, the sources of\n  compatible local actions, composition beyond two tokens, the antiunitary and complete-positivity\n  bridge, and the relation to the K3 machinery remain open. K2 does not discharge H-Bell.")

RESULT_TEMPLATE = '''# OI-PAIR-MAXCONE-1 — conditional pair-cone theorem

Outcome: OI-PAIR-MAXCONE-1-PROVED

For a set of two-token tables containing every product state of eball 3 and closed under addition and nonnegative scaling, the maxCone upper bound together with CNOT and full rotation/cyclic invariance implies K=Q3. The upper inclusion uses maxCone and block invariance; the lower uses products and cone closure. Available sharp product tests suffice for the upper bound. These conditional statements use neither self-duality nor closedness nor an assumed ReachPure witness.

The block and generator equivalences have separate witnesses: blockInvariant_of_eq_Q3 / pairCone_eq_Q3_of_block_maxCone, and driveInvariant_of_eq_Q3 / pairCone_eq_Q3_of_drive_maxCone. The physical state/test identification, product preparation and cone realization, validity of product tests on the actual pair, enough available tests, and preservation by the gate and full rotation/cyclic actions retain their source obligations. A one-angle or channel-limit route retains its own closure assumptions.

The finite controls do not show that OI implies QM. Nothing here sources H3; neither physical sourcing nor full-model independence is labelled kernel-certified. The 118 reached rows and 68 NOT REACHED rows remain distinct; the latter are unresolved. Arbitrary finite-carrier reconstruction and the full operation/instrument correspondence remain open.

Exact controls: MAXCONE-EXACT: PASS; 2743 finite exact checks
The checker uses Q(i), replay is byte-identical, and its three mutations are rejected. Finite witnesses are not universal proofs. Density states fail scaling; the rank-three-excluded PSD family fails addition; the expanded kappa family fails a product test; the zero cone fails product inclusion; the separable family fails CNOT invariance. Whole-family statements have written proofs in the preregistration at their stated scope.

Design evidence: core 4d7d71d6, run 38205087980, 13 standard axiom reports; sharp-test refinement bbcdbab5, run 38205760341, 16 standard axiom reports. Both Build steps succeeded and their release gates failed only the seven unregistered design modules' census. Predictive execution evidence is recorded in the preregistration. The execution includes the matching proof bodies, truthful conditional headers, the kernel-only registry family, the exact checker and control shard. Six E19 dependency bodies are unchanged; the new MaxCone proof body is unchanged from the measured refinement.

F: {F}
F workflow run: {F_RUN}
S1: {S1}
S1 workflow run: {S1_RUN}

The execution's sixteen named MaxCone axiom reports must be standard, with no sorryAx, and all required host checks must be green before E designation. The owner's E designation and its exact-head workflow attestation are recorded outside this result note and in the receipt. The proof is conditional mathematics; this package supplies no unconditional reconstruction or full-model independence result.
'''


def sha(body):
    return hashlib.sha256(body).hexdigest()


def git(*args):
    return subprocess.check_output(['git', *args])


def workflow(base):
    text = base.decode()
    for old, new in SPLICES:
        if text.count(old) != 1:
            raise ValueError('W: splice anchor is not unique')
        text = text.replace(old, new)
    return text.encode()


def roadmap(base):
    old, new = ROADMAP_SPLICE
    text = base.decode()
    if text.count(old) != 1:
        raise ValueError('M: roadmap anchor is not unique')
    return text.replace(old, new).encode()


def render_result(f, frun, s1, srun):
    return RESULT_TEMPLATE.format(F=f, F_RUN=frun, S1=s1, S1_RUN=srun).encode()


def result_fields(body):
    pattern = re.escape(RESULT_TEMPLATE)
    for key, expression in [('F', '[0-9a-f]{40}'), ('S1', '[0-9a-f]{40}'),
                            ('F_RUN', '[1-9][0-9]*'), ('S1_RUN', '[1-9][0-9]*')]:
        pattern = pattern.replace(re.escape('{' + key + '}'), '(?P<' + key + '>' + expression + ')')
    match = re.fullmatch(pattern, body.decode())
    return match.groupdict() if match else None


def failures(files, original, freeze, output, stderr, rc, required, f=None, s1=None):
    errors = []
    for path, digest in BASE_HASH.items():
        if sha(original.get(path, b'')) != digest:
            errors.append('D')
    for path, digest in PIN.items():
        if sha(files.get(path, b'')) != digest:
            errors.append('P')
    if files.get(WORKFLOW) != workflow(original[WORKFLOW]):
        errors.append('W')
    anchor = b'import OIBridge.RelcSelectC5\n'
    expected_root = original[ROOT].replace(anchor, anchor + b'import OIBridge.EqvK2MaxCone\n')
    if original[ROOT].count(anchor) != 1 or files.get(ROOT) != expected_root:
        errors.append('H')
    try:
        expected = json.loads(original[REGISTRY])
        expected['families'].append(FAMILY)
        if json.loads(files.get(REGISTRY, b'')) != expected:
            errors.append('J')
    except (ValueError, KeyError):
        errors.append('J')
    for path in original:
        if path not in (WORKFLOW, ROOT, REGISTRY, ROADMAP) and files.get(path) != original[path]:
            errors.append('L')
    roadmap_digest = ROADMAP_SHA if required else BASE_HASH[ROADMAP]
    expected_roadmap = roadmap(original[ROADMAP]) if required else original[ROADMAP]
    if sha(files.get(ROADMAP, b'')) != roadmap_digest or files.get(ROADMAP) != expected_roadmap:
        errors.append('M')
    if files.get(ROUND + 'preregistration.md') != freeze:
        errors.append('F')
    control_hash = re.search(rb'^Controls SHA256: ([0-9a-f]{64})$', freeze, re.M)
    if not control_hash or sha(files.get(ROUND + 'controls.py', b'')) != control_hash.group(1).decode():
        errors.append('C')
    names = {'preregistration.md', 'controls.py'} | ({'result.md'} if required else set())
    if {p[len(ROUND):] for p in files if p.startswith(ROUND)} != names:
        errors.append('R')
    if rc or stderr or sha(output) != OUTPUT_SHA:
        errors.append('V')
    if required:
        fields = result_fields(files.get(ROUND + 'result.md', b''))
        if fields is None or (f and fields['F'] != f) or (s1 and fields['S1'] != s1):
            errors.append('S')
    return sorted(set(errors))


def self_test(root, base_root):
    root = Path(root)
    original = {p: (Path(base_root) / p).read_bytes() if base_root else git('show', D + ':' + p)
                for p in BASE_HASH}
    # CI replays the frozen fixture, rather than permanently pinning the live
    # shared workflow, registry, aggregator or kernel at every later head.
    # The local pre-freeze fixture uses the staged files before these blobs
    # have been published. The two owned checker files remain live regression
    # inputs, and the independent checker is actually executed below.
    files = {p: (root / p).read_bytes() if base_root else git('cat-file', 'blob', PIN_BLOB[p])
             for p in PIN}
    for p in (PROBE, SUPPORT):
        files[p] = (root / p).read_bytes()
    files.update({p: original[p] for p in original if p not in files and p != ROADMAP})
    files[ROADMAP] = roadmap(original[ROADMAP])
    controls = Path(__file__).read_bytes()
    pre = root / ROUND / 'preregistration.md'
    freeze = pre.read_bytes() if pre.exists() else ('Controls SHA256: ' + sha(controls) + '\n').encode()
    files[ROUND + 'preregistration.md'] = freeze
    files[ROUND + 'controls.py'] = controls
    f, s1 = 'a' * 40, 'b' * 40
    files[ROUND + 'result.md'] = render_result(f, 1, s1, 2)
    proc = subprocess.run([sys.executable, '-I', '-B', str(root / PROBE)], capture_output=True)
    def test(current, out=proc.stdout, err=proc.stderr, rc=proc.returncode):
        return failures(current, original, freeze, out, err, rc, True, f, s1)
    if test(files):
        raise ValueError('positive fixture fails ' + str(test(files)))
    stage1 = dict(files)
    stage1.pop(ROUND + 'result.md')
    stage1[ROADMAP] = original[ROADMAP]
    if failures(stage1, original, freeze, proc.stdout, proc.stderr, proc.returncode, False):
        raise ValueError('stage-one positive fixture fails')
    mutations = [(p, b'changed', 'P') for p in PIN]
    mutations += [(WORKFLOW, original[WORKFLOW], 'W'), (ROOT, original[ROOT], 'H'),
                  (REGISTRY, original[REGISTRY], 'J'), (ROADMAP, original[ROADMAP], 'M'),
                  (ROUND + 'preregistration.md', b'changed', 'F'),
                  (ROUND + 'controls.py', b'changed', 'C'), (ROUND + 'extra', b'extra', 'R'),
                  (ROUND + 'result.md', files[ROUND + 'result.md'] + b'It establishes unconditional reconstruction.', 'S'),
                  (ROUND + 'result.md', render_result('c' * 40, 1, s1, 2), 'S')]
    anchor = next(p for p in original if p not in (WORKFLOW, ROOT, REGISTRY, ROADMAP))
    mutations.append((anchor, b'changed', 'L'))
    for p, value, code in mutations:
        changed = dict(files)
        changed[p] = value
        if code not in test(changed):
            raise ValueError('mutation escaped ' + code + ' at ' + p)
    for out, err, rc in [(b'PASS', b'', 0), (proc.stdout, b'error', 0), (proc.stdout, b'', 1)]:
        if 'V' not in test(files, out, err, rc):
            raise ValueError('output mutation escaped')
    print('controls self-test: PASS; two positive fixtures and ' + str(len(mutations) + 3) + ' mutations')


def check(head, freeze):
    original = {p: git('show', D + ':' + p) for p in BASE_HASH}
    names = git('ls-tree', '-r', '--name-only', head, '--', ROUND).decode().splitlines()
    paths = set(PIN) | set(BASE_HASH) | set(names)
    files = {p: git('show', head + ':' + p) for p in paths}
    fixed = git('show', freeze + ':' + ROUND + 'preregistration.md')
    changed = set(git('diff', '--name-only', D, head).decode().splitlines())
    allowed = set(PIN) | {ROADMAP, ROUND + 'preregistration.md', ROUND + 'controls.py', ROUND + 'result.md'}
    if not changed <= allowed:
        raise ValueError('G: changed path outside declared scope')
    if git('diff', '--name-only', D, freeze).decode().splitlines() != [ROUND + 'preregistration.md']:
        raise ValueError('G: freeze delta is not the preregistration alone')
    subprocess.run(['git', 'merge-base', '--is-ancestor', freeze, head], check=True)
    ancestry = git('rev-list', '--reverse', '--parents', freeze + '..' + head).decode().splitlines()
    if not ancestry or any(len(line.split()) != 2 for line in ancestry):
        raise ValueError('T: execution is not linear after F')
    s1 = ancestry[0].split()[0]
    for path in (PROBE, SUPPORT):
        if Path(path).read_bytes() != files[path]:
            raise ValueError('P: local checker/support differs from checked object')
    if Path(__file__).read_bytes() != files[ROUND + 'controls.py']:
        raise ValueError('C: running controls differ from checked object')
    proc = subprocess.run([sys.executable, '-I', '-B', PROBE], capture_output=True)
    required = ROUND + 'result.md' in files
    failed = failures(files, original, fixed, proc.stdout, proc.stderr, proc.returncode,
                      required, freeze, s1)
    if failed:
        raise ValueError('controls failed: ' + ','.join(failed))
    print('controls: PASS')
    sys.stdout.write(proc.stdout.decode())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('head', nargs='?')
    parser.add_argument('--freeze')
    parser.add_argument('--self-test', action='store_true')
    parser.add_argument('--root', default='.')
    parser.add_argument('--base-root')
    args = parser.parse_args()
    try:
        if args.self_test:
            self_test(args.root, args.base_root)
        elif args.head and args.freeze:
            check(args.head, args.freeze)
        else:
            parser.error('head and --freeze, or --self-test, required')
    except (ValueError, subprocess.CalledProcessError) as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
