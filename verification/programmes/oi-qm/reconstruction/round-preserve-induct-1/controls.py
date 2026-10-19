#!/usr/bin/env python3
"""Round PRESERVE-INDUCT-1 -- the round's own static controls and verdict (draft, before F).

It reads nothing but the repository, through git, and certifies nothing on its own: the Lean kernel,
the axiom audit and the release gate establish the mathematics, the governed probe and its
independent check the exact layer, and the V3 verifier the protocol. What it checks is that the
execution carries the frozen surface of the two modules, the statement-level design invariants the
preregistration asserts, the frozen execution blobs and the frozen workflow, import and census
edits, the retained evidence the preregistration pins, the evidence archive's pending citations of
this record kept as the archive records them, none of the excluded phrases, and no change outside
the governed paths.

    python3 -I controls.py --self-test                    the checker's own controls, on a synthetic
                                                          D/F/E fixture, the preregistration beside
                                                          this file and the historical objects it
                                                          cites, read at D through git
    python3 -I controls.py candidate <X>                  the controls that need no F, on the
                                                          candidate execution tree of commit X
    python3 -I controls.py axioms <LOG>                   the bridge job's fail-closed step: the
                                                          ten axiom reports of LOG
    python3 -I controls.py check <E> --freeze <F> [--stage E|S1]
                                                          the static controls at E (stage E, the
                                                          default) or at the first execution commit
                                                          (stage S1)
    python3 -I controls.py verdict <E> --freeze <F> [--axioms LOG]
                                                          the cell tokens from the measurements at E:
                                                          the static controls, the probe and the
                                                          independent check at their blobs at E, each
                                                          run with python3 -I -B, and the axiom reports
                                                          of E's exact-head bridge log

The four design parameters (NS, SPLICES, FAMILIES, PROBE_SPEC) are set; with any of them None the
controls that depend on it fail closed. Neither this file nor any file of the round other than the
preregistration names the research builds' run numbers: the evidence archive admits them only in
the record it awaits (R13), so this file reads them from the archive and the preregistration.

The self-test reads no file of the working tree but this one and the preregistration beside it:
the cited objects (the landed declarations, the cited ROADMAP span and the archive's pending
citations) are read at D through git, so a later change to the working tree cannot alter that
fixture, and it fails closed when D is not in the repository's history. The candidate execution
tree is tested separately, by `candidate` on a commit and by `check` at E.
Exit 1 on any failure, 2 on a usage error.
"""
import ast
import contextlib
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import tempfile
import types

D = 'ec36234cb98a30ecb4681e118ff9ccb82e19aa6d'
ROUND = 'PRESERVE-INDUCT-1'
RDIR = 'verification/programmes/oi-qm/reconstruction/round-preserve-induct-1/'
PREREG = RDIR + 'preregistration.md'
RESULT = RDIR + 'result.md'
CONTROLS = RDIR + 'controls.py'
FRUN = 'evidence/f-run/'
CORE = 'verification/lean-mathlib/OIBridge/PreservationInduction.lean'
INST = 'verification/lean-mathlib/OIBridge/PreservationInductionInstances.lean'
PROBE = 'verification/lean/preserve_induct1_probe.py'
INDEP = 'verification/lean/preserve_induct1_indep_check.py'
ROOT = 'verification/lean-mathlib/OIBridge.lean'
REGISTRY = 'verification/lean-manuscript-census.json'
WORKFLOW = '.github/workflows/verify.yml'
LEGACY = 'verification/infrastructure/legacy-records.json'
RECEIPT = 'verification/receipts/PRESERVE-INDUCT-1.json'
ARCHIVE = 'verification/audits/evidence-retention/'
RESEARCH_MARKS = ('ResearchDesign', 'PreservationInductionDesign')

ROUND_BLOCK = ['round ' + ROUND, 'kind non-sealing', 'record-directory ' + RDIR]
GOVERNED = [('record', 'AM', RDIR), ('record', 'AM', RECEIPT), ('execution', 'A', CORE),
            ('execution', 'A', INST), ('execution', 'A', PROBE), ('execution', 'A', INDEP),
            ('execution', 'M', ROOT), ('execution', 'M', REGISTRY), ('execution', 'M', WORKFLOW)]
FROZEN_PATHS = {CONTROLS, CORE, INST, PROBE, INDEP}
RET_TITLE = 'Retained evidence (§A.42).'
HISTORICAL = {'core-build', 'instance-build'}  # an archived expected result, a digest or a recorded gap
REQUIRED_PIN = 'predicted-tree'                                          # a digest only
EVIDENCE_ROWS = HISTORICAL | {REQUIRED_PIN}
GAP, NONE, ARCHIVED = 'GAP', 'NONE', 'ARCHIVED'
# Each historical row is bound to the archive entry whose pending citation awaits this record on the
# row's line (the line of the preregistration that cites the build's run, beside its head).
HIST_LINES = {'core-build': 69, 'instance-build': 127}
# sha256 of each cited line's text (no newline), byte-identical to those lines of #831's head 65b85147:
# control A requires the citation on exactly that line with exactly that text.
HIST_LINE_SHA256 = {69: '2892155d251408c8f5da1ab66639303103de9a7fae97d56309eaef697c7af473',
                    127: 'bf84b537a746956779fd48b78843c1d0226f516c8a201c9b2ddc5ca2c2f1a8e3'}
# Line spans the preregistration cites outside the landed objects: (path, first, last, sha256 of the lines
# joined by newlines with a final newline, at D). S2 and the self-test require exactly these lines.
ROADMAP = 'verification/ROADMAP.md'
CITED_SPANS = [(ROADMAP, 1125, 1129, 'bfcc4fd0c5ebc02e2f9d65c99b52eb3d899f33d8e19c47be00dafa2e32305e50')]
NINTH = INDEP  # the ninth governed path, whose exact content the preregistration names
# Owner decision of 2026-10-17: the replacement drafting chain cites #831 and imports none of its commits.
OLD_CHAIN = {'5f614d60c3234cf35bc9b15e892388d576f77aa1', '65b85147f85aa01770e0e60551152bc5f1d9ef29'}
SUPERSEDED_CITE = ('65b85147f85aa01770e0e60551152bc5f1d9ef29', 'https://github.com/amaybaum/incompleteness/pull/831')
SYMPY_PIN = '1.14.0'

# The surface the preregistration names (sections "Research-design definition and theorem budget").
CORE_NAMES = ['CarrierConeFamily', 'AdditiveClosure', 'PreservesCarrier', 'PrimitivePreservation',
              'UniformAttachPreservation', 'AncillaDiscardPreservation', 'finite_sum_mem',
              'instAvail_preserves', 'instAvail_sum_preserves', 'instAvail_spectator_preserves',
              'instAvail_transport_preserves']
INST_NAMES = ['quantumCone', 'classicalCone', 'classicalClass', 'classicalCone_iff', 'quantum_additive',
              'quantum_conj', 'quantum_primitive', 'attachBlock', 'attachBlock_apply', 'uniformAttach_eq_blocks',
              'quantum_attach', 'ptraceAnc_eq_blocks', 'quantum_discard', 'quantum_instAvail',
              'quantum_fullClass', 'classical_additive', 'classical_conj', 'classical_primitive',
              'classical_attach', 'classical_discard', 'classical_readProj', 'classical_instAvail',
              'classical_native_readout']
INST_EXAMPLES = 2
CORE_IMPORTS = ['import OIBridge.ImplementationLocality']
INST_IMPORTS = ['import OIBridge.PreservationInduction', 'import OIBridge.StructuralClosure']
HEADLINE = 'instAvail_preserves'
COR_PRINTS = ['instAvail_sum_preserves', 'instAvail_spectator_preserves', 'instAvail_transport_preserves']
CORE_PRINTS = [HEADLINE] + COR_PRINTS
INST_PRINTS = ['quantum_instAvail', 'classical_instAvail', 'quantum_attach', 'quantum_discard',
               'classical_readProj', 'classical_native_readout']
ARMS = ['op', 'readout', 'coarse', 'bind', 'discard']
FIELDS = {'AdditiveClosure': ['zero_mem', 'add_mem'], 'PrimitivePreservation': ['op', 'readout']}
COROLLARY_USES = {'instAvail_sum_preserves': [HEADLINE],
                  'instAvail_spectator_preserves': [HEADLINE, 'instAvail_spectator'],
                  'instAvail_transport_preserves': [HEADLINE, 'instAvail_transport']}
CORE_EXCLUDED = r'PosSemidef|IsHermitian|Convex|IsClosed|\btrace\b|instAvail_trace|↔|\bIff\b|\breach'
FORBIDDEN = r'\b(sorry|admit|native_decide|axiom|implemented_by|extern)\b'

# Landed objects at D (file, line, name); their blobs at E are D's.
LP = 'verification/lean-mathlib/OIBridge/'
LANDED = [
    (LP + 'ImplementationLocality.lean', 244, 'ImplementationClass'),
    (LP + 'ImplementationLocality.lean', 256, 'readProj'),
    (LP + 'ImplementationLocality.lean', 268, 'InstAvail'),
    (LP + 'ImplementationLocality.lean', 317, 'instAvail_trace'),
    (LP + 'ImplementationLocality.lean', 359, 'ContextStable'),
    (LP + 'ImplementationLocality.lean', 364, 'LabelInvariant'),
    (LP + 'ImplementationLocality.lean', 374, 'fullClass'),
    (LP + 'ImplementationLocality.lean', 644, 'instAvail_transport'),
    (LP + 'ImplementationLocality.lean', 789, 'instAvail_spectator'),
    (LP + 'ImplementationLocality.lean', 820, 'instAvail_withSpectator'),
    (LP + 'OperationalAssembly.lean', 453, 'ptraceAnc'),
    (LP + 'OperationalAssembly.lean', 492, 'uniformAttach'),
    (LP + 'OperationalAssembly.lean', 515, 'discardWith'),
    (LP + 'MonoidalCompletion.lean', 360, 'conjChannel'),
    (LP + 'ReferenceExtension.lean', 131, 'amplRefL'),
    (LP + 'SpectatorBridge.lean', 348, 'transport'),
    (LP + 'StructuralClosure.lean', 180, 'substratumClass'),
    (LP + 'StructuralClosure.lean', 261, 'substratumClass_contextStable'),
    (LP + 'StructuralClosure.lean', 275, 'substratumClass_labelInvariant'),
]
ROOT_LINES = ['import OIBridge.PreservationInduction', 'import OIBridge.PreservationInductionInstances']
PHRASES = ['OI supplies', 'sources the preservation premises', 'preservation is derived from OI',
           'compatibility is derived', 'K2 is closed', 'P0 is closed', 'F2 is closed', 'OI implies QM',
           'the probe proves']
ALLOWED_AXIOMS = {'propext', 'Classical.choice', 'Quot.sound'}
BAD_LOG = ('sorryAx', 'Lean.ofReduceBool', 'Lean.trustCompiler')

# The design parameters (preregistration items 2-5); None fails the dependent controls closed.
NS = 'OIBridge.PreservationInduction'   # the adopted namespace (item 2): S1, verdict
# [(old, new)] edits to verify.yml at D, each anchored once (item 5): W
SPLICES = [
    ('  # Act 42. Two shards run on every event; the exclusion shards, about six CPU-hours between them,\n',
     '  probes_preserveinduct1:\n'
     '    name: Numerical probes / PRESERVE-INDUCT-1 preservation induction\n'
     '    runs-on: ubuntu-latest\n'
     '    steps:\n'
     '      # fetch-depth: 0 is load-bearing: the control self-test reads its historical fixture at D\n'
     '      - uses: actions/checkout@v4\n'
     '        with:\n'
     '          fetch-depth: 0\n'
     '\n'
     '      - uses: actions/setup-python@v5\n'
     '        with:\n'
     "          python-version: '3.11'\n"
     '\n'
     '      - name: Install the exact-algebra dependency\n'
     '        run: pip install sympy==1.14.0\n'
     '\n'
     '      - name: PRESERVE-INDUCT-1 exact probe\n'
     '        working-directory: verification/lean\n'
     '        run: |\n'
     '          echo "=== preserve_induct1_probe.py ==="\n'
     '          python3 -I -B preserve_induct1_probe.py\n'
     '\n'
     '      - name: PRESERVE-INDUCT-1 independent exact check\n'
     '        working-directory: verification/lean\n'
     '        run: |\n'
     '          echo "=== preserve_induct1_indep_check.py ==="\n'
     '          python3 -I -B preserve_induct1_indep_check.py\n'
     '\n'
     '      - name: PRESERVE-INDUCT-1 control mutation tests\n'
     '        run: python3 -I -B verification/programmes/oi-qm/reconstruction/round-preserve-induct-1/controls.py --self-test\n'
     '\n'
     '  # Act 42. Two shards run on every event; the exclusion shards, about six CPU-hours between them,\n'),
    ('probes_bg2, ', 'probes_bg2, probes_preserveinduct1, '),
    ('          BG2_RESULT: ${{ needs.probes_bg2.result }}\n',
     '          BG2_RESULT: ${{ needs.probes_bg2.result }}\n'
     '          PRESERVEINDUCT1_RESULT: ${{ needs.probes_preserveinduct1.result }}\n'),
    ('          echo "bg2=${BG2_RESULT}"\n',
     '          echo "bg2=${BG2_RESULT}"\n'
     '          echo "preserveinduct1=${PRESERVEINDUCT1_RESULT}"\n'),
    ('          test "${BG2_RESULT}" = success\n',
     '          test "${BG2_RESULT}" = success\n'
     '          test "${PRESERVEINDUCT1_RESULT}" = success\n'),
    # the ten axiom reports printed again by the bridge job's final step, whose block (opened by the step's own
    # line naming the checked-out SHA) is the only place verdict reads them; the step fails closed (controls.py
    # axioms) unless each is reported once within the three allowed axioms
    ('      - name: Release gate\n        run: python3 tools/release_gate.py\n',
     '      - name: Release gate\n        run: python3 tools/release_gate.py\n'
     '\n'
     '      # PRESERVE-INDUCT-1: the round\'s ten axiom reports again, at the end of the job log. The step\n'
     '      # fails unless each of the ten is reported exactly once, within propext, Classical.choice and\n'
     '      # Quot.sound, and the output carries no sorryAx, Lean.ofReduceBool or Lean.trustCompiler.\n'
     '      - name: PRESERVE-INDUCT-1 axiom reports\n'
     '        working-directory: verification/lean-mathlib\n'
     '        run: |\n'
     '          set -euo pipefail\n'
     '          head=$(git rev-parse HEAD)\n'
     '          echo "preserve_induct1 axioms: step at ${head}"\n'
     '          log="$RUNNER_TEMP/preserve-induct1-axioms.log"\n'
     '          lake env lean OIBridge/PreservationInduction.lean 2>&1 | tee "$log"\n'
     '          lake env lean OIBridge/PreservationInductionInstances.lean 2>&1 | tee -a "$log"\n'
     '          python3 -I -B ../programmes/oi-qm/reconstruction/round-preserve-induct-1/controls.py axioms "$log"\n'),
]
# the census families appended for the two modules (item 3): J
FAMILIES = [
    {
        "name": "conditional preservation of an independently given carrier cone family by every InstAvail derivation (round PRESERVE-INDUCT-1, reconstruction)",
        "modules": [
            "PreservationInduction"
        ],
        "status": "kernel-only",
        "manuscript": [],
        "note": "instAvail_preserves: AdditiveClosure (zero and addition only), PrimitivePreservation (separate op and readout fields), UniformAttachPreservation and AncillaDiscardPreservation imply that every branch of every InstAvail family preserves C S; one induction over op, readout, coarse, bind and discard. The sum, spectator and transport corollaries display their extra hypotheses; transport concerns the destination carrier's cone and does not identify it with a reindexing. The four premises are hypotheses: the family supplies no physical source for them, no compatibility principle and no part of the P1 — F2 extension. This family is carried by no manuscript. Record: verification/programmes/oi-qm/reconstruction/round-preserve-induct-1/."
    },
    {
        "name": "positive semidefinite and nonnegative diagonal instances of the preservation induction (round PRESERVE-INDUCT-1, reconstruction)",
        "modules": [
            "PreservationInductionInstances"
        ],
        "status": "kernel-only",
        "manuscript": [],
        "note": "quantumCone (positive semidefinite) satisfies every premise for every implementation class (quantum_instAvail, quantum_fullClass); classicalCone (positive semidefinite and diagonal) satisfies them for the monomial class substratumClass (classical_instAvail), which admits every reindexed native register readout (classical_readProj, classical_native_readout). Comparisons for the conditional theorem only: no physical preparation family is shown to satisfy the premises, and no claim that every classical stochastic instrument is available. This family is carried by no manuscript. Record: verification/programmes/oi-qm/reconstruction/round-preserve-induct-1/."
    }
]
# the probe's and the independent check's codes, counts, final lines and stdout digests, the mutations,
# the shared manifest digest and the SymPy pin (item 4): Q-EXACT, and W for the pin
PROBE_SPEC = {
    'sympy': '1.14.0',
    'manifest': 'a1f82e289ba07a4c60dd6b56396dcdf7c0c217b2ff49a8d779f1c4e923842ea9',
    'probe': {'codes': ['CONSTRUCTORS', 'ISOMETRY', 'READOUT', 'ATTACH', 'AGGREGATE', 'EMPTY', 'NONVACUOUS',
                        'BRANCH-PSD', 'BRANCH-DIAG', 'RELABEL', 'COUNTER-HADAMARD', 'COUNTER-READOUT',
                        'COUNTER-DISCARD', 'MANIFEST', 'MUTATION-RULE'],
              'n': 127, 'final': 'preserve_induct1_probe: OK -- 127 checks',
              'stdout_sha256': 'e862be79cbac1d73b0afc45a9bff14067f2fc96566b3a387211f04f3014f94d7'},
    'indep': {'codes': ['I-TRACE', 'I-EMPTY', 'I-PSD', 'I-DIAG', 'I-HADAMARD', 'I-READOUT', 'I-DISCARD',
                        'I-SEPARATE', 'I-MANIFEST'],
              'n': 47, 'final': 'preserve_induct1_indep_check: OK -- 47 checks',
              'stdout_sha256': '4031a930ff47634992177e42bcc59455b922d217a0b221d0d83f98159226e72f'},
    'mutations': ['readout-as-isometry: op-isometry', 'aggregate-for-branch: branch-cone',
                  'discard-enlarged-premise-dropped: branch-cone', 'labels-as-cone-transport: branch-cone',
                  'availability-as-source: branch-cone', 'pure-for-uniform: attach-cone',
                  'empty-fibre-dropped: empty-fibre', 'discard-omits-sum: aggregate-trace'],
}
PENDING = ('NS', 'SPLICES', 'FAMILIES', 'PROBE_SPEC')

REQUIRED = {'E': ['C1', 'C2', 'S1', 'S2', 'S3', 'S4', 'W', 'I', 'J', 'P', 'R', 'A', 'G', 'T'],
            'S1': ['C1', 'C2', 'P', 'R', 'A', 'G', 'T']}
STAGES = tuple(REQUIRED)
CELLS = [('Q-CORE', 'PRESERVE-INDUCT-CORE-PROVED', 'PRESERVE-INDUCT-CORE-NOT-ESTABLISHED'),
         ('Q-COR', 'PRESERVE-INDUCT-COROLLARIES-PROVED', 'PRESERVE-INDUCT-COROLLARIES-NOT-ESTABLISHED'),
         ('Q-EXACT', 'PRESERVE-INDUCT-EXACT-CHECKED', 'PRESERVE-INDUCT-EXACT-NOT-ESTABLISHED')]
READ, NOT_READ = 'PRESERVE-INDUCT-1-READ', 'PRESERVE-INDUCT-1-NOT-READ'
POSITIVE = [c[1] for c in CELLS] + [READ]
SELF_CHECKS = 59  # the number of self-checks; a dropped self-check fails the count

FAIL = []
RAN = []
GIT_CWD = None  # the self-test sets it to this file's directory, so its reads at D need no particular cwd


def report(name, ok, detail=''):
    ok = ok is True
    print(('PASS ' if ok else 'FAIL ') + name + (('  ' + detail) if detail else ''))
    RAN.append(name)
    if not ok:
        FAIL.append(name)
    return ok


def git(*args):
    return subprocess.run(['git'] + list(args), capture_output=True, text=True, check=True, cwd=GIT_CWD).stdout


def show(commit, path):
    r = subprocess.run(['git', 'show', '%s:%s' % (commit, path)], capture_output=True, text=True, cwd=GIT_CWD)
    return r.stdout if r.returncode == 0 else None


def blob(commit, path):
    r = subprocess.run(['git', 'rev-parse', '--verify', '-q', '%s:%s' % (commit, path)],
                       capture_output=True, text=True, cwd=GIT_CWD)
    return r.stdout.strip() if r.returncode == 0 and r.stdout.strip() else None


def is_ancestor(a, b):
    return subprocess.run(['git', 'merge-base', '--is-ancestor', a, b], capture_output=True,
                          cwd=GIT_CWD).returncode == 0


def has_commit(c):
    return subprocess.run(['git', 'cat-file', '-e', '%s^{commit}' % c], capture_output=True,
                          cwd=GIT_CWD).returncode == 0


def has_token(out, tok):
    return re.search(r'(?<![\w-])%s(?![\w-])' % re.escape(tok), out) is not None


def flat(s):
    return ' '.join(s.split())


def uncomment(text):
    out, i, n, depth = [], 0, len(text), 0
    while i < n:
        if text.startswith('/-', i):
            depth += 1; i += 2; continue
        if depth:
            if text.startswith('-/', i):
                depth -= 1; i += 2
            else:
                if text[i] == '\n':
                    out.append('\n')
                i += 1
            continue
        if text.startswith('--', i):
            j = text.find('\n', i); i = n if j < 0 else j; continue
        out.append(text[i]); i += 1
    return ''.join(out)


# ---------------------------------------------------------------- the preregistration's frozen tables

def fenced(prereg, info):
    """The bodies of every block opened by exactly ```info."""
    return re.findall(r'^```%s\n(.*?)^```$' % re.escape(info), prereg or '', re.S | re.M)


def governed(prereg):
    """[(class, ops, path)] of the single v3-governed-paths block, or None when absent or malformed."""
    blocks = fenced(prereg, 'v3-governed-paths')
    if len(blocks) != 1:
        return None
    out = []
    for ln in blocks[0].splitlines():
        if not ln.strip() or ln.startswith('#'):
            continue
        parts = ln.split(' ')
        if len(parts) != 3 or parts[0] not in ('record', 'execution') or not parts[1] or \
                any(c not in 'AMD' for c in parts[1]):
            return None
        out.append(tuple(parts))
    return out or None


def round_block(prereg):
    blocks = fenced(prereg, 'v3-round')
    return [ln for ln in blocks[0].splitlines() if ln.strip()] if len(blocks) == 1 else None


def table_after(prereg, title):
    """The rows of the table that directly follows the bold paragraph `title` (one blank line between), as lists
    of cells; [] when the paragraph or its table is absent. It never reaches a later table."""
    m = re.search(r'\*\*%s\*\*[^\n]*(?:\n[^\n|][^\n]*)*\n\n((?:\|[^\n]*\n)+)' % re.escape(title), prereg or '')
    if not m:
        return []
    rows = [[c.strip() for c in ln.strip().strip('|').split('|')] for ln in m.group(1).splitlines()]
    return [r for r in rows[2:] if r]


def pinned(prereg, title, width):
    """{path: digest or None (pending)} from a two-column pin table; None when a row is malformed or repeated."""
    out = {}
    for r in table_after(prereg, title):
        if len(r) != 2 or not re.fullmatch(r'`[^`]+`', r[0]):
            return None
        path, cell = r[0].strip('`'), r[1]
        if path in out:
            return None
        if re.fullmatch(r'`[0-9a-f]{%d}`' % width, cell):
            out[path] = cell.strip('`')
        elif cell.startswith('pending'):
            out[path] = None
        else:
            return None
    return out


def frozen_blobs(prereg):
    return pinned(prereg, 'Frozen execution blobs.', 40)


def retention(prereg):
    """{row label: (file, digest)} from the three-column retention table; None when a row is malformed or repeated.
    file: a record-relative `evidence/...` path, a repository path retained on main (`verification/...`, outside
    the record directory), ARCHIVED (`archive`: the expected result the evidence archive holds for the row's
    pending citation, found by its digest), None (pending) or NONE (a gap row names no file). digest: sha256,
    None (pending) or GAP (`gap:` and what is missing). Admitted pairs: (path, digest), (path or None, None),
    (ARCHIVED, digest) on a historical row, (NONE, GAP)."""
    out = {}
    for r in table_after(prereg, RET_TITLE):
        if len(r) != 3 or not re.fullmatch(r'`[a-z0-9-]+`', r[0]) or r[0].strip('`') in out:
            return None
        f, h = r[1], r[2]
        if re.fullmatch(r'`[^`\s]+`', f):
            path = f.strip('`')
            if not (path.startswith('evidence/') or (path.startswith('verification/') and not path.startswith(RDIR))):
                return None
        elif f.startswith('pending'):
            path = None
        elif f == 'archive':
            path = ARCHIVED
        elif f == 'none':
            path = NONE
        else:
            return None
        if re.fullmatch(r'`[0-9a-f]{64}`', h):
            dig = h.strip('`')
        elif h.startswith('pending'):
            dig = None
        elif re.match(r'gap: \S', h):
            dig = GAP
        else:
            return None
        if not ((dig not in (None, GAP) and path not in (None, NONE)) or (dig is None and path not in (NONE, ARCHIVED))
                or (path == NONE and dig == GAP)) or (path == ARCHIVED and r[0].strip('`') not in HISTORICAL):
            return None
        out[r[0].strip('`')] = (path, dig)
    return out


def resolve(path):
    return RDIR + path if path.startswith('evidence/') else path


def record_files(rows):
    """The record-relative files the digest rows name."""
    return {p for p, h in rows.values() if h not in (None, GAP) and p not in (None, NONE, ARCHIVED)
            and p.startswith('evidence/')}


def landed_table(prereg):
    rows = table_after(prereg, "S2's landed objects at D.")
    out = []
    for r in rows:
        m = len(r) == 2 and re.fullmatch(r'`([^`]+)` \| `([A-Za-z]+\.lean):(\d+)`', r[0] + ' | ' + r[1])
        if not m:
            return None
        out.append((LP + m.group(2), int(m.group(3)), m.group(1)))
    return out


def frozen_surface(prereg):
    """(core block, instances block) from the section '## The statement surface (frozen', else None."""
    m = re.search(r'^## The statement surface \(frozen.*?(?=^## |\Z)', prereg or '', re.S | re.M)
    if not m:
        return None
    blocks = fenced(m.group(0), 'lean')
    return tuple(blocks) if len(blocks) == 2 and all(b.strip() for b in blocks) else None


def span_digest(text, first, last):
    """sha256 of lines first..last of text joined by newlines with a final newline; None when text is too short."""
    lines = (text or '').split('\n')
    if lines and lines[-1] == '':
        lines.pop()
    if text is None or first < 1 or len(lines) < last:
        return None
    return hashlib.sha256(('\n'.join(lines[first - 1:last]) + '\n').encode('utf-8')).hexdigest()


LEAN_CITE = re.compile(r'([A-Za-z]+\.lean):(\d+)|(?<![\w:/.])\(?:(\d+)\)?|ROADMAP :(\d+)[\u2013-](\d+)')


def prose_citations(prereg):
    """([(file name, line)], [(path, first, last)], problems): every line citation in the preregistration outside
    fenced blocks. A bare `:N` cites the .lean file last named in its paragraph; one with none named is a problem."""
    body = re.sub(r'^```.*?^```$', '', prereg or '', flags=re.S | re.M)
    cites, spans, probs = [], [], []
    for para in re.split(r'\n\s*\n', body):
        cur = None
        for m in LEAN_CITE.finditer(para):
            if m.group(1):
                cur = m.group(1)
                cites.append((cur, int(m.group(2))))
            elif m.group(3):
                if cur is None:
                    probs.append('a bare :%s with no .lean file named before it' % m.group(3))
                else:
                    cites.append((cur, int(m.group(3))))
            else:
                spans.append((ROADMAP, int(m.group(4)), int(m.group(5))))
    return cites, spans, probs


def citation_problems(prereg):
    """Every prose line citation is a pinned landed object (file and line) or a pinned span; [] means pass."""
    cites, spans, probs = prose_citations(prereg)
    pinned_lines = {(os.path.basename(path), line) for path, line, _ in LANDED}
    probs += ['%s:%d is not a pinned landed object' % c for c in cites if c not in pinned_lines]
    probs += ['%s:%d-%d is not a pinned span' % s for s in spans if s not in [x[:3] for x in CITED_SPANS]]
    if not cites or not spans:
        probs.append('no line citation found (%d lines, %d spans)' % (len(cites), len(spans)))
    return probs


def pinned_lines_table(prereg):
    """[(cited text, lines, sha256)] of the table after '**Pinned line citations.**'; None when a row is malformed."""
    out = []
    for r in table_after(prereg, 'Pinned line citations.'):
        m = len(r) == 3 and re.fullmatch(r'`([0-9a-f]{64})`', r[2])
        if not m:
            return None
        out.append((r[0], r[1], m.group(1)))
    return out


def pinned_lines_expected():
    """The table the preregistration must carry: CITED_SPANS, then HIST_LINE_SHA256 in line order."""
    return ([('`%s` at `D`' % p, '%d\u2013%d' % (a, b), h) for p, a, b, h in CITED_SPANS]
            + [('this file', str(n), h) for n, h in sorted(HIST_LINE_SHA256.items())])


def spans_problems(read):
    """Each pinned span has its digest in read(path); [] means pass."""
    return ['%s:%d-%d at D' % (p, a, b) for p, a, b, h in CITED_SPANS if span_digest(read(p), a, b) != h]


def ninth_table(prereg):
    """{property: cell} of the table after '**The ninth governed path.**', or None when absent or repeated."""
    out = {}
    for r in table_after(prereg, 'The ninth governed path.'):
        if len(r) != 2 or r[0] in out:
            return None
        out[r[0]] = r[1]
    return out or None


def ticks(cell):
    return re.findall(r'`([^`]+)`', cell or '')


def py_imports(text):
    """The sorted module names a Python source imports, at any depth; None when it does not parse."""
    try:
        tree = ast.parse(text or '')
    except SyntaxError:
        return None
    mods = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            mods |= {a.name for a in node.names}
        elif isinstance(node, ast.ImportFrom):
            mods.add(node.module or '')
    return sorted(mods)


def ninth_problems(prereg, spec, text=None, check_text=False):
    """The ninth governed path's named content: the table names its path and governed entry, the blob the
    frozen-blob table pins, and the codes, check count, final line and stdout digest of spec['indep']; with
    check_text, the file's own blob, sha256, byte count and imports. [] means pass."""
    tab = ninth_table(prereg)
    if tab is None:
        return ['the ninth governed path table is absent or malformed']
    s = (spec or {}).get('indep') or {}
    fb = frozen_blobs(prereg) or {}
    want = {'path': [NINTH], 'governed entry': ['execution A ' + NINTH], 'blob': [fb.get(NINTH) or '?'],
            'codes': s.get('codes') or ['?'], 'checks': [str(s.get('n'))], 'final line': [s.get('final') or '?'],
            'stdout sha256': [s.get('stdout_sha256') or '?']}
    probs = ['%s: %s, not %s' % (k, ticks(tab.get(k)), v) for k, v in want.items() if ticks(tab.get(k)) != v]
    if ('execution', 'A', NINTH) not in (governed(prereg) or []):
        probs.append('the governed-path block does not add the ninth path')
    if set(tab) != set(want) | {'sha256', 'bytes', 'imports'}:
        probs.append('table rows %s' % sorted(tab))
    if check_text:
        if text is None:
            return probs + ['the ninth path is absent']
        b = text.encode('utf-8')
        got = {'blob': [git_blob_id(text)], 'sha256': [hashlib.sha256(b).hexdigest()], 'bytes': [str(len(b))],
               'imports': py_imports(text)}
        probs += ['%s: file has %s, table %s' % (k, v, ticks(tab.get(k))) for k, v in got.items()
                  if ticks(tab.get(k)) != v]
    return probs


# ---------------------------------------------------------------- the archive's pending citations of this record

HEXANY = re.compile(r'(?<![0-9A-Fa-f])[0-9A-Fa-f]{7,}(?![0-9A-Fa-f])')
LETTERS = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
ALNUM = LETTERS | set('0123456789')


def run_mentions(line, run):
    """'free', 'embedded' or None: how line names run, matched with no digit beside it. An occurrence is
    embedded when a letter stands beside it, or a joiner (- _ .) that is itself beside a letter or digit."""
    kinds = []
    for m in re.finditer(r'(?<![0-9])%s(?![0-9])' % re.escape(run), line):
        s, e = m.start(), m.end()
        b, b2 = line[s - 1:s], line[max(s - 2, 0):max(s - 1, 0)]
        a, a2 = line[e:e + 1], line[e + 1:e + 2]
        kinds.append('embedded' if b in LETTERS or a in LETTERS or (b and b in '-_.' and b2 in ALNUM)
                     or (a and a in '-_.' and a2 in ALNUM) else 'free')
    return None if not kinds else 'free' if 'free' in kinds else 'embedded'


def head_beside(lines, n, head):
    """[] when lines n-1..n+1 state head as the run's head: the full id is a word there and every other hex word
    of 7 to 63 digits is a form of it (a word of decimal digits only counts at 40 digits); else the problems."""
    win = [lines[k - 1] for k in (n - 1, n, n + 1) if 1 <= k <= len(lines)]
    words = [w for l in win for w in HEXANY.findall(l)]
    other = sorted({w for w in words if len(w) < 64 and (len(w) > 40 or (
        w.lower() != head if len(w) == 40 else not w.isdigit() and not head.startswith(w.lower())))})
    probs = ['another head beside line %d: %s' % (n, ', '.join(other))] if other else []
    return probs + ([] if head in words else ['the full head is not beside line %d' % n])


def names_run(commit, run):
    """The paths of commit's tree outside the archive that name run (no digit beside it); None if git fails."""
    r = subprocess.run(['git', 'grep', '--full-name', '-l', '-E', '(^|[^0-9])%s([^0-9]|$)' % run, commit, '--', ':/',
                        ':(top,exclude)' + ARCHIVE.rstrip('/')], capture_output=True, text=True, cwd=GIT_CWD)
    if r.returncode not in (0, 1):
        return None
    return {l.split(':', 1)[1] for l in r.stdout.splitlines() if l.strip()}


def archive_citations(read, names):
    """Control A. read(path) gives a file's text at the commit (None if absent), names(run) the paths outside the
    archive naming run. The archive's research-build entries and retained commits whose pending citation awaits
    this round must name this preregistration; each run is cited free-standing on exactly its recorded line and
    on no other line of the record, with its head (run.json's head_sha) beside it and no other head; no other
    file names the run; each retained commit awaiting the round is the head of one of those runs; and the
    recorded lines are HIST_LINES. Returns (problems, {line: entry})."""
    probs, bound = [], {}
    try:
        man = json.loads(read(ARCHIVE + 'manifest.json') or 'null')
        objs = json.loads(read(ARCHIVE + 'objects/manifest.json') or 'null')
    except ValueError:
        return ['an archive manifest is not JSON'], bound
    if not isinstance(man, dict) or not isinstance(objs, dict):
        return ['an archive manifest is absent'], bound
    prereg = read(PREREG)
    lines = (prereg or '').split('\n')
    aw = lambda e: e.get('awaiting_citation') if isinstance(e, dict) and isinstance(e.get('awaiting_citation'), dict) else {}
    ents = [e for e in man.get('entries') or [] if aw(e).get('round') == ROUND]
    heads = {}
    for e in ents:
        a, run = aw(e), str(e.get('run_id'))
        try:
            head = json.loads(read(ARCHIVE + 'ci/%s/run.json' % run) or 'null').get('head_sha')
        except (ValueError, AttributeError):
            head = None
        n = a.get('line')
        if a.get('record') != PREREG or not isinstance(n, int) or not re.fullmatch(r'[0-9a-f]{40}', str(head)):
            probs.append('%s: a pending citation without this record, a line or a head' % e.get('id'))
            continue
        cited = {k: c for k, c in ((k, run_mentions(l, run)) for k, l in enumerate(lines, 1)) if c}
        if cited != {n: 'free'}:
            probs.append('%s: the record names its run on %s, not free-standing on line %d alone' % (
                e.get('id'), sorted(cited.items()), n))
        text = lines[n - 1] if 1 <= n <= len(lines) else None
        if text is None or hashlib.sha256(text.encode('utf-8')).hexdigest() != HIST_LINE_SHA256.get(n):
            probs.append('%s: line %d is not the pinned citation text' % (e.get('id'), n))
        probs += ['%s: %s' % (e.get('id'), x) for x in head_beside(lines, n, head)]
        other = names(run)
        if other is None or other - {PREREG}:
            probs.append('%s: another file names its run: %s' % (e.get('id'), sorted((other or {'?'}) - {PREREG})))
        heads[head] = run
        bound[n] = e
    for o in objs.get('objects') or []:
        a = aw(o)
        if a.get('round') == ROUND and (a.get('record') != PREREG or heads.get(o.get('oid')) != str(a.get('run'))):
            probs.append('retained commit %s: its pending citation is not the head of an awaited run of this record'
                         % str(o.get('oid'))[:12])
    if sorted(bound) != sorted(HIST_LINES.values()):
        probs.append('the pending citations await lines %s, not %s' % (sorted(bound), sorted(HIST_LINES.values())))
    return probs, bound


def archived_ok(bound, label, digest, read_d, read_e, blob_d, blob_e):
    """An ARCHIVED historical row: the entry bound to the row's line holds a results.json with this digest, present
    at D and unchanged at E."""
    e = bound.get(HIST_LINES.get(label))
    files = [f for f in (e or {}).get('files') or [] if f.get('sha256') == digest
             and str(f.get('path', '')).endswith('/results.json')]
    if len(files) != 1:
        return False
    q = ARCHIVE + files[0]['path']
    t = read_e(q)
    return t is not None and hashlib.sha256(t.encode('utf-8')).hexdigest() == digest \
        and blob_d(q) is not None and blob_d(q) == blob_e(q)


# ---------------------------------------------------------------- Lean text

DECL = re.compile(r"^(?:noncomputable )?(def|abbrev|theorem|structure|inductive)\s+([A-Za-z_][\w.']*)", re.M)
BOUNDARY = re.compile(r"^(?:(?:noncomputable )?(?:def|abbrev|theorem|structure|inductive)\s|example\b|#|end\b|"
                      r"namespace\b|open\b|section\b|attribute\b|variable\b)")


def theorem_surface(lines):
    buf = []
    for l in lines:
        if ':=' in l:
            buf.append(l.split(':=', 1)[0]); break
        if l.rstrip().endswith(' where'):
            buf.append(l.rstrip()[:-len(' where')]); break
        buf.append(l)
    return flat('\n'.join(buf))


def chunks(code):
    """[(kind, name, lines)] for each declaration and example; a chunk ends at the next boundary line."""
    lines, out, cur = code.split('\n'), [], None
    for l in lines:
        m = DECL.match(l)
        if m or l.startswith('example'):
            cur = (m.group(1), m.group(2), [l]) if m else ('example', '', [l])
            out.append(cur)
        elif cur is not None and (BOUNDARY.match(l) or not l.strip()):
            cur = None if BOUNDARY.match(l) or cur[0] not in ('theorem', 'example') else cur
            if cur is not None:
                cur[2].append(l)
        elif cur is not None:
            cur[2].append(l)
    return out


def features(text):
    """What S1 compares: imports, namespace and open lines, declarations in order with their surfaces (a
    theorem's or example's up to its first ':=' or trailing 'where'; any other declaration's whole text up to
    a blank line), examples, prints."""
    code = uncomment(text)
    lines = [l.strip() for l in code.splitlines() if l.strip()]
    decls, examples = [], []
    for kind, name, ls in chunks(code):
        if kind in ('theorem', 'example'):
            surface = theorem_surface(ls)
        else:
            surface = flat('\n'.join(l for l in ls if l.strip()))
        (examples if kind == 'example' else decls).append((kind, name, surface))
    return {'imports': [l for l in lines if l.startswith('import ')],
            'scopes': [l for l in lines if re.match(r'(namespace|end|section)\b', l)],
            'opens': [l for l in lines if l.startswith('open ')],
            'decls': decls, 'examples': examples,
            'prints': [l for l in lines if l.startswith('#')]}


def body(text, name):
    for kind, n, ls in chunks(uncomment(text)):
        if n == name:
            joined = '\n'.join(ls)
            return joined.split(':=', 1)[1] if ':=' in joined else ''
    return None


def render_block(text):
    """The frozen-block form of a module: its code, blank lines dropped, with every theorem's and example's
    proof removed (a proof runs to the next boundary line, as in chunks())."""
    res, i, lines = [], 0, uncomment(text).split('\n')
    is_thm = lambda l: (DECL.match(l) is not None and DECL.match(l).group(1) == 'theorem') or l.startswith('example')
    while i < len(lines):
        l = lines[i]
        if is_thm(l):
            j = i
            while j < len(lines):
                if ':=' in lines[j]:
                    res.append(lines[j].split(':=', 1)[0].rstrip() + ' :='); break
                if lines[j].rstrip().endswith(' where'):
                    res.append(lines[j].rstrip()[:-len(' where')] + ' :='); break
                res.append(lines[j]); j += 1
            j += 1
            while j < len(lines) and not BOUNDARY.match(lines[j]):
                j += 1
            i = j
            continue
        if l.strip():
            res.append(l)
        i += 1
    return '\n'.join(res) + '\n'


def header_of(module):
    m = re.search(r'/-!(.*?)-/', module or '', re.S)
    return m.group(1) if m else ''


# ---------------------------------------------------------------- the controls

def s1(core, inst, surface, ns):
    """S1 surface. Returns a list of problems; [] means pass."""
    if surface is None:
        return ['frozen surface pending (no statement-surface section with two lean blocks)']
    if ns is None:
        return ['namespace pending (NS)']
    probs = []
    for label, text, block, names, imports, prints in (
            ('core', core, surface[0], CORE_NAMES, CORE_IMPORTS, CORE_PRINTS),
            ('instances', inst, surface[1], INST_NAMES, INST_IMPORTS, INST_PRINTS)):
        if not text:
            probs.append(label + ' module absent'); continue
        have, want = features(text), features(block)
        if [n for _, n, _ in want['decls']] != names:
            probs.append(label + ': frozen block does not declare the preregistration\'s names in order')
        if want['imports'] != imports or want['prints'] != ['#print axioms ' + p for p in prints]:
            probs.append(label + ': frozen block imports or prints differ from the preregistration')
        if want['scopes'] != ['namespace ' + ns, 'end ' + ns]:
            probs.append(label + ': frozen block namespace is not ' + ns)
        if label == 'instances' and len(want['examples']) != INST_EXAMPLES:
            probs.append('instances: frozen block does not carry the two examples')
        for k in ('imports', 'scopes', 'opens', 'decls', 'examples', 'prints'):
            if have[k] != want[k]:
                probs.append('%s: %s differ from the frozen block' % (label, k))
        if re.search(FORBIDDEN, uncomment(text)):
            probs.append(label + ': forbidden token')
    return probs


def s3(core, inst):
    """S3 statement-level design invariants of the preregistration. Returns a list of problems."""
    if not core or not inst:
        return ['a module is absent']
    probs, cc, ic = [], uncomment(core), uncomment(inst)
    if re.search(CORE_EXCLUDED, cc):
        probs.append('core: PSD, Hermiticity, convexity, closedness, trace, reachability or an iff appears')
    for name, fields in FIELDS.items():
        ch = [ls for k, n, ls in chunks(cc) if n == name and k == 'structure']
        got = [m.group(1) for l in (ch[0][1:] if len(ch) == 1 else []) for m in [re.match(r'^  (\w+) :', l)] if m]
        if got != fields:
            probs.append('%s fields %s, not %s' % (name, got, fields))
    hb = body(core, HEADLINE)
    arms = re.findall(r'^  \| (\w+)\b', hb or '', re.M)
    if hb is None or 'induction h with' not in hb or arms != ARMS:
        probs.append('the headline is not one induction on h with the five arms in order (%s)' % arms)
    for name, uses in COROLLARY_USES.items():
        b = body(core, name)
        if b is None or not all(re.search(r'\b%s\b' % u, b) for u in uses):
            probs.append('%s does not apply %s' % (name, ' to '.join(uses)))
    if any(mark in t for mark in RESEARCH_MARKS for t in (cc, ic)):
        probs.append('a research import or namespace remains')
    for k, n, ls in chunks(ic):
        if k in ('def', 'abbrev') and 'CarrierConeFamily' in ls[0] and re.search(r'InstAvail|reach', '\n'.join(ls)):
            probs.append('%s defines a preparation family through availability' % n)
    return probs


def s4(texts):
    return [(name, p) for name, t in texts for p in PHRASES if t and p.lower() in t.lower()]


def s2(E, prereg):
    """S2: each landed object on its pinned line with D's blob at E; each pinned span with its digest at D and
    D's blob at E; every prose line citation of the preregistration pinned. [] means pass."""
    probs = []
    for path, line, name in LANDED:
        bd, be = blob(D, path), blob(E, path)
        text = (show(E, path) or '').splitlines()
        found = len(text) >= line and re.match(r'(noncomputable )?(def|abbrev|theorem|structure|inductive) %s\b'
                                               % re.escape(name), text[line - 1])
        if bd is None or bd != be or not found:
            probs.append('%s:%d %s (blob at D %s, at E %s)' % (path, line, name, bd, be))
    probs += spans_problems(lambda q: show(D, q))
    probs += ['%s changed after D' % p for p, _, _, _ in CITED_SPANS if blob(D, p) is None or blob(D, p) != blob(E, p)]
    return probs + citation_problems(prereg)


def workflow(base, splices):
    if base is None or not splices:
        return None
    text = base
    for old, new in splices:
        if not old or text.count(old) != 1 or old == new:
            return None
        text = text.replace(old, new)
    return text


def pin_ok(splices, spec):
    """With the probe spec pending, False. When it names SymPy, the text the splices add installs exactly
    sympy==<pin> and names lowercase `sympy` in no other form; otherwise the splices add no sympy install."""
    if not splices or not spec:
        return False
    added = ''.join(new.replace(old, '', 1) if old in new else new for old, new in splices)
    forms = re.findall(r'\bsympy\b[=<>!~]*[\w.*]*', added)
    if spec.get('sympy'):
        return spec['sympy'] == SYMPY_PIN and bool(forms) and all(f == 'sympy==' + SYMPY_PIN for f in forms)
    return not forms


def root_expected(base):
    """D's root with ROOT_LINES inserted directly after its last import line; None when that is undefined."""
    if base is None:
        return None
    lines = base.split('\n')
    idx = [i for i, l in enumerate(lines) if l.startswith('import ')]
    if not idx or any(l in lines for l in ROOT_LINES):
        return None
    return '\n'.join(lines[:idx[-1] + 1] + ROOT_LINES + lines[idx[-1] + 1:])


def registry_ok(base, head, families):
    if base is None or head is None or not families:
        return False
    try:
        want = json.loads(base)
        want['families'].extend(families)
        return json.loads(head) == want
    except (ValueError, KeyError, TypeError, AttributeError):
        return False


def authorized(status, path, entries):
    cands = [e for e in entries if path == e[2] or (e[2].endswith('/') and path.startswith(e[2]))]
    if not cands:
        return False
    e = max(cands, key=lambda e: len(e[2]))
    return ('M' if status == 'T' else status) in e[1]


def g(diff_lines, entries):
    bad = []
    for ln in diff_lines:
        status, _, path = ln.partition('\t')
        if not path or not authorized(status[:1], path, entries) or path == LEGACY:
            bad.append(ln)
    return bad


def record_ok(names, files, at_e):
    rel = {n[len(RDIR):] for n in names if n.startswith(RDIR)}
    want = {'preregistration.md', 'controls.py'} | set(files) | ({'result.md'} if at_e else set())
    extra = {r for r in rel - want if not r.startswith('amendments/') and not r.startswith(FRUN)}
    frun = any(r.startswith(FRUN) for r in rel)
    return not (want - rel) and not extra and frun


def check(E, F, stage='E'):
    """Runs and prints the static controls of `stage`. Each control records its own outcome when it runs; the
    result maps exactly the codes that recorded one ({code: passed}). A code that never ran is absent, and
    verdict and main treat an absent code as failed. An unknown stage is refused."""
    if stage not in STAGES:
        raise ValueError('check: unknown stage %r (expected one of %s)' % (stage, ', '.join(STAGES)))
    outcomes = {}

    def record(code, name, ok, detail=''):
        ok = ok is True
        report(code + ' ' + name, ok, detail)
        outcomes[code] = outcomes.get(code, True) and ok

    at_e = stage == 'E'
    prereg_F, prereg_E = show(F, PREREG), show(E, PREREG)
    pf = prereg_F or ''
    record('C1', 'the preregistration at E is the one at F, with this round\'s D, declaration and #831 citation',
           prereg_F is not None and prereg_F == prereg_E and ('D: `%s`' % D) in pf
           and round_block(pf) == ROUND_BLOCK and all(c in pf for c in SUPERSEDED_CITE))
    fb = frozen_blobs(pf)
    want = FROZEN_PATHS if at_e else {CONTROLS}
    pend = sorted(p for p, b in (fb or {}).items() if b is None)
    bad = sorted(p for p in want if fb and fb.get(p) and blob(E, p) != fb[p])
    nprobs = ninth_problems(pf, PROBE_SPEC, show(E, NINTH), True) if at_e else []
    record('C2', 'the frozen execution blobs at ' + stage + (' and the ninth path\'s named content' if at_e else ''),
           fb is not None and set(fb) == FROZEN_PATHS and not pend and not bad and not nprobs,
           ('pending %s' % pend if pend else '') + (' differ %s' % bad if bad else '') + ' '.join(nprobs))
    rows = retention(pf)
    ppend = sorted(l for l, (p, h) in (rows or {}).items() if p is None or h is None)
    gbad = sorted(l for l, (p, h) in (rows or {}).items() if h == GAP and l not in HISTORICAL)

    aprobs, bound = archive_citations(lambda q: show(E, q), lambda run: names_run(E, run))

    def digest_ok(p, h):
        if p == ARCHIVED:
            return archived_ok(bound, label_of[(p, h)], h, lambda q: show(D, q), lambda q: show(E, q),
                               lambda q: blob(D, q), lambda q: blob(E, q))
        q = resolve(p)
        t = show(E, q)
        ok = t is not None and hashlib.sha256(t.encode('utf-8')).hexdigest() == h
        # a file retained on main outside the record directory is there at D and unchanged at E
        return ok and (p.startswith('evidence/') or (blob(D, q) is not None and blob(D, q) == blob(E, q)))
    label_of = {v: l for l, v in (rows or {}).items()}
    pbad = sorted(l for l, (p, h) in (rows or {}).items() if p not in (None, NONE) and h not in (None, GAP)
                  and not digest_ok(p, h))
    ngap = sum(h == GAP for _, h in (rows or {}).values())
    record('P', 'the retention rows at F: digests present at %s, gaps only on historical rows' % stage,
           rows is not None and set(rows) == EVIDENCE_ROWS and not ppend and not gbad and not pbad,
           str(ppend + gbad + pbad) if ppend or gbad or pbad else '%d digest(s), %d gap(s)' % (len(rows) - ngap, ngap))
    names = [x for x in git('ls-tree', '-r', '--name-only', E, '--', RDIR).splitlines() if x.strip()]
    record('R', 'the record directory holds exactly the frozen files, the record-relative evidence and evidence/f-run/',
           rows is not None and record_ok(names, record_files(rows or {}), at_e))
    record('A', "the archive's pending citations of this record stand as the archive records them", not aprobs,
           '; '.join(aprobs) if aprobs else '%d run(s) cited on their recorded lines only' % len(bound))
    diff = [x for x in git('diff', '--no-renames', '--name-status', D, E).splitlines() if x.strip()]
    gp = governed(pf)
    badg = g(diff, gp or [])
    record('G', 'every change from D lies in the governed paths at F; no receipt yet; the legacy manifest untouched',
           gp == GOVERNED and bool(diff) and not badg and blob(E, RECEIPT) is None
           and blob(D, LEGACY) is not None and blob(D, LEGACY) == blob(E, LEGACY),
           str(badg) if badg else '%d paths' % len(diff))
    fdelta = [x for x in git('diff', '--name-only', D, F).splitlines() if x.strip()]
    pre = [x for x in git('rev-list', '--parents', '%s..%s' % (D, F)).splitlines() if x.strip()]
    lin = [x for x in git('rev-list', '--parents', '%s..%s' % (F, E)).splitlines() if x.strip()]
    record('T', 'delta(D, F) is the control plane, drafted linearly from D without #831\'s commits; the execution '
           'is linear after F',
           PREREG in fdelta and all(p == PREREG or p.startswith(RDIR + 'amendments/') for p in fdelta)
           and bool(pre) and all(len(x.split()) == 2 for x in pre) and is_ancestor(D, F)
           and not any(x.split()[0] in OLD_CHAIN for x in pre)
           and bool(lin) and all(len(x.split()) == 2 for x in lin) and is_ancestor(F, E))
    if not at_e:
        return outcomes
    core, inst = show(E, CORE), show(E, INST)
    probs = s1(core, inst, frozen_surface(pf), NS)
    record('S1', 'surface: the two modules equal the frozen blocks', not probs, '; '.join(probs))
    probs = s2(E, pf)
    record('S2', 'the landed objects and cited spans on their pinned lines, unchanged from D; the prose citations '
           'pinned', not probs, '; '.join(probs))
    probs = s3(core, inst)
    record('S3', 'the statement-level design invariants', not probs, '; '.join(probs))
    result = show(E, RESULT)
    hits = s4([('core header', header_of(core)), ('instances header', header_of(inst)), ('result note', result)])
    present = bool(header_of(core).strip()) and bool(header_of(inst).strip()) and bool((result or '').strip())
    record('S4', 'both module headers and the result note present, with no excluded phrase', present and not hits,
           str(hits) if hits else ('' if present else 'a header or the result note is absent'))
    wd, we = workflow(show(D, WORKFLOW), SPLICES), show(E, WORKFLOW)
    record('W', 'the workflow at E is D\'s with the frozen splices, installing the probe spec\'s SymPy pin',
           wd is not None and we is not None and we == wd and pin_ok(SPLICES, PROBE_SPEC),
           'splices pending (SPLICES)' if SPLICES is None else ('probe spec pending (PROBE_SPEC)' if PROBE_SPEC is None
                                                                else ''))
    rd, re_ = root_expected(show(D, ROOT)), show(E, ROOT)
    record('I', 'the two import lines after D\'s last import', rd is not None and re_ is not None and re_ == rd)
    record('J', 'the census at E is D\'s with the frozen families', registry_ok(show(D, REGISTRY), show(E, REGISTRY),
                                                                                   FAMILIES),
           'families pending (FAMILIES)' if FAMILIES is None else '')
    return outcomes


def passed(results, stage='E'):
    """True only when every code required at `stage` recorded an explicit True; absent or non-bool means failed."""
    return stage in REQUIRED and isinstance(results, dict) and all(results.get(c) is True for c in REQUIRED[stage])


def run_probe(E):
    """The probe and the independent check, each at its blob at E, extracted alone and run with python3 -I -B from
    its own directory: {'probe': (rc, stdout, stderr), 'indep': (rc, stdout, stderr)}."""
    with tempfile.TemporaryDirectory() as tmp:
        arch = subprocess.run(['git', 'archive', E, PROBE, INDEP], capture_output=True, check=True).stdout
        subprocess.run(['tar', '-x', '-C', tmp], input=arch, check=True)
        out = {}
        for key, path in (('probe', PROBE), ('indep', INDEP)):
            r = subprocess.run([sys.executable, '-I', '-B', os.path.join(tmp, path)], capture_output=True, text=True,
                               cwd=os.path.join(tmp, os.path.dirname(path)))
            out[key] = (r.returncode, r.stdout, r.stderr)
        return out


def script_ok(res, s):
    """One script's rule: exit 0, empty stderr, no FAIL line, every frozen code passing, the frozen check count
    with no failures, the frozen final line and the frozen stdout digest (the byte replay)."""
    if not isinstance(s, dict) or not s.get('codes') or not isinstance(s.get('n'), int) or not s.get('final') \
            or not re.fullmatch(r'[0-9a-f]{64}', s.get('stdout_sha256') or ''):
        return False
    if not (isinstance(res, tuple) and len(res) == 3):
        return False
    rc, out, err = res
    ok = rc == 0 and not err and not re.search(r'^FAIL\b', out, re.M)
    ok &= hashlib.sha256(out.encode('utf-8')).hexdigest() == s['stdout_sha256']
    ok &= all(re.search(r'^PASS %s \(\d+\)$' % re.escape(c), out, re.M) for c in s['codes'])
    ok &= ('checks: %d, failures: 0' % s['n']) in out and out.rstrip().endswith(s['final'])
    return bool(ok)


def probe_ok(res, spec):
    """Q-EXACT's rule: both scripts by their own rule; the probe prints the SymPy pin and rejects every frozen
    mutation; both print the frozen sample-manifest digest (the two implementations agree on every entry of
    every final branch)."""
    if not spec or not isinstance(res, dict) or not re.fullmatch(r'[0-9a-f]{64}', spec.get('manifest') or ''):
        return False
    ok = script_ok(res.get('probe'), spec.get('probe')) and script_ok(res.get('indep'), spec.get('indep'))
    if not ok:
        return False
    pout, iout = res['probe'][1], res['indep'][1]
    line = 'SAMPLE-MANIFEST-SHA256 %s' % spec['manifest']
    ok &= all(re.search(r'^%s$' % line, o, re.M) is not None for o in (pout, iout))
    if spec.get('sympy'):
        ok &= spec['sympy'] == SYMPY_PIN and re.search(r'^SYMPY %s$' % re.escape(SYMPY_PIN), pout, re.M) is not None
    muts = spec.get('mutations') or []
    ok &= bool(muts) and all(re.search(r'^REJECTED %s$' % re.escape(m), pout, re.M) for m in muts)
    ok &= len(re.findall(r'^REJECTED ', pout, re.M)) == len(muts)
    ok &= re.search(r'^mutations: %d rejected, 0 survived, 0 undecided$' % len(muts), pout, re.M) is not None
    ok &= re.search(r'^(ACCEPTED|SURVIVED|UNDECIDED) ', pout, re.M) is None
    return bool(ok)


TIMESTAMP = re.compile(r'^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d\.\d+Z ', re.M)


def untimestamped(log):
    """A served job log without each line's leading timestamp (as extract_result.py reads it), so a report that
    Lean wraps across lines parses whole."""
    return TIMESTAMP.sub('', log or '')


def reports_in(log, ns):
    """{name: [axiom set per report]} of every report of namespace ns in log (timestamps removed); {} with no ns."""
    rep = {}
    if not ns:
        return rep
    pat = re.compile(r"'%s\.([\w']+)' (?:depends on axioms: \[([^\]]*)\]|does not depend on any axioms)" % re.escape(ns))
    for m in pat.finditer(untimestamped(log)):
        rep.setdefault(m.group(1), []).append({a.strip() for a in (m.group(2) or '').split(',') if a.strip()})
    return rep


def axioms_from(log, ns):
    """{name: union of its reported axioms} in log."""
    return {n: set().union(*v) for n, v in reports_in(log, ns).items()}


STEP_MARK = re.compile(r'^preserve_induct1 axioms: step at (\S*)$', re.M)
GATE_OK = 'preserve_induct1 axioms: OK -- %d reports' % len(CORE_PRINTS + INST_PRINTS)
GATE_FAILED = re.compile(r'^preserve_induct1 axioms: FAILED', re.M)
STEP_END = re.compile(r'^(?:##\[group\]Run |Post job cleanup\.)', re.M)
CHECKOUT_SHA = re.compile(r'^\[command\]/usr/bin/git log -1 --format=%H\n(\S*)$', re.M)


def step_block(log, sha, ns=None):
    """(block, problems) of E's served bridge-job log, its timestamps removed. The block is the final step's
    output: from the step's one line 'preserve_induct1 axioms: step at <SHA>' to the next step header or the
    job's cleanup. Problems: no such line or more than one; its SHA not `sha`, E's full SHA; a checkout line
    (`git log -1 --format=%H`) naming another SHA; a FAILED line of the gate anywhere in the log; in the block, an
    `##[error]` line, a BAD_LOG token, or not exactly one OK line of the gate after the block's last report.
    The block is None when no single marker is found."""
    text = untimestamped(log)
    probs = []
    if not re.fullmatch(r'[0-9a-f]{40}', sha or ''):
        probs.append('E has no full SHA')
    marks = list(STEP_MARK.finditer(text))
    if len(marks) != 1:
        return None, probs + ['%d step marker line(s), not one' % len(marks)]
    if marks[0].group(1) != sha:
        probs.append('the step ran at %s, not at E' % (marks[0].group(1)[:12] or '?'))
    probs += ['the checkout names %s, not E' % s[:12] for s in CHECKOUT_SHA.findall(text) if s != sha]
    if GATE_FAILED.search(text):
        probs.append('the axiom gate printed FAILED')
    rest = text[marks[0].end():]
    end = STEP_END.search(rest)
    block = rest[:end.start()] if end else rest
    if re.search(r'^##\[error\]', block, re.M):
        probs.append('an error line in the step')
    bad = [b for b in BAD_LOG if b in block]
    if bad:
        probs.append('%d forbidden token(s) in the step' % len(bad))
    oks = [m.start() for m in re.finditer(r'^%s$' % re.escape(GATE_OK), block, re.M)]
    last = max([m.end() for m in re.finditer(r"'%s\.[\w']+' (?:depends on axioms: \[[^\]]*\]|does not depend on any "
                                             r"axioms)" % re.escape(ns or NS or '-'), block)] or [0])
    if len(oks) != 1 or oks[0] < last:
        probs.append('%d OK line(s) of the gate%s, not one after the last report'
                     % (len(oks), ' (one before a report)' if oks and oks[-1] < last else ''))
    return block, probs


def lean_cells(log, sha, ns):
    """(Q-CORE, Q-COR, problems, reports): the Lean cells from the final step's block only. Each read report is
    in the block exactly once and within ALLOWED_AXIOMS; any problem of step_block fails both cells."""
    block, probs = step_block(log or '', sha, ns)
    rep = reports_in(block or '', ns)
    clean = lambda n: len(rep.get(n, [])) == 1 and rep[n][0] <= ALLOWED_AXIOMS
    ok = block is not None and not probs and bool(ns)
    core = ok and clean(HEADLINE) and all(clean(n) for n in INST_PRINTS)
    cor = ok and clean(HEADLINE) and all(clean(n) for n in INST_PRINTS + COR_PRINTS)
    return core, cor, probs, rep


def full_sha(c):
    """E's full commit id, or None."""
    r = subprocess.run(['git', 'rev-parse', '--verify', '-q', '%s^{commit}' % c], capture_output=True, text=True,
                       cwd=GIT_CWD)
    return r.stdout.strip() if r.returncode == 0 else None


def verdict(E, F, axlog, check_fn=None, probe_fn=None):
    """Every positive token is gated on every static control required at E: if any fails or is not reported,
    the failed controls are printed, the probe is not run, no axiom report is read, every cell prints
    NOT-ESTABLISHED, the round prints NOT-READ and the result is False. The Lean cells read only the final
    bridge-job step's block of axlog (step_block). check_fn and probe_fn default to check and run_probe."""
    results = (check_fn or check)(E, F)
    results = results if isinstance(results, dict) else {}
    failed = [c for c in REQUIRED['E'] if results.get(c) is not True]
    if failed:
        print('STATIC CONTROLS FAILED: ' + ', '.join(failed))
        print('probe not run and axiom reports not read: a required static control failed')
        got = (False, False, False)
    else:
        res = (probe_fn or run_probe)(E)
        for key in ('probe', 'indep'):
            r = res.get(key) if isinstance(res, dict) else None
            print((r[1] if isinstance(r, tuple) and len(r) == 3 else '%s: no output' % key).rstrip())
        try:
            log = open(axlog, encoding='utf-8', errors='replace').read() if axlog else ''
        except OSError:
            log = ''
        core, cor, sprobs, rep = lean_cells(log, full_sha(E), NS)
        for p_ in sprobs:
            print('final bridge step: ' + p_)
        got = (core, cor, probe_ok(res, PROBE_SPEC))
        print('axiom reports read from the final bridge step: %d of %d prints' % (
            len([p for p in CORE_PRINTS + INST_PRINTS if p in rep]), len(CORE_PRINTS + INST_PRINTS)))
    for (cell, pos, neg), ok in zip(CELLS, got):
        print('TOKEN %-7s %s' % (cell, pos if ok is True else neg))
    short = [c for (c, _, _), ok in zip(CELLS, got) if ok is not True]
    print('earned reading: %s' % ('full (every cell positive)' if not short else 'not full (%s not positive)'
                                  % ', '.join(short)))
    print('%s (static controls failed: %s)' % (NOT_READ, ', '.join(failed)) if failed else READ)
    return not failed


def axioms_gate(log, ns):
    """The bridge job's fail-closed step: [(name, ok, detail)]. Each of the ten printed names is reported exactly
    once in namespace ns, within ALLOWED_AXIOMS; no other name of ns is reported; the log carries no BAD_LOG
    token. An empty log or an unset namespace fails."""
    if not ns or not isinstance(log, str) or not log.strip():
        return [('log', False, 'no log or namespace')]
    log = untimestamped(log)
    pat = re.compile(r"'%s\.([\w']+)' (?:depends on axioms: \[([^\]]*)\]|does not depend on any axioms)" % re.escape(ns))
    seen = {}
    for m in pat.finditer(log):
        seen.setdefault(m.group(1), []).append({a.strip() for a in (m.group(2) or '').split(',') if a.strip()})
    out = []
    for n in CORE_PRINTS + INST_PRINTS:
        reps = seen.get(n, [])
        extra = sorted(set().union(*reps) - ALLOWED_AXIOMS) if reps else []
        out.append((n, len(reps) == 1 and not extra, '%d report(s)%s' % (len(reps), ', extra ' + ', '.join(extra)
                                                                          if extra else '')))
    other = sorted(set(seen) - set(CORE_PRINTS + INST_PRINTS))
    out.append(('no other report', not other, ', '.join(other)))
    bad = [b for b in BAD_LOG if b in log]
    # the label names no forbidden token: this output lands in the bridge log, which verdict reads whole
    out.append(('no forbidden log token', not bad, '%d found' % len(bad) if bad else ''))
    return out


def candidate(X):
    """The controls that need no F, on the candidate execution tree of commit X, against the preregistration at X:
    C2 (the frozen blobs and the ninth path's named content), S1, S2, S3, S4 for the module headers (the result
    note comes at E), W, I, J, A, and G with no receipt. Evidence for the executor before F and E: not an input
    of verdict, not a stage of check, and not run by the workflow, whose self-test every later commit inherits.
    Returns {code: passed}."""
    outcomes = {}

    def record(code, name, ok, detail=''):
        ok = ok is True
        report('candidate ' + code + ' ' + name, ok, detail)
        outcomes[code] = outcomes.get(code, True) and ok
    pf = show(X, PREREG) or ''
    fb = frozen_blobs(pf)
    pend = sorted(p for p, b in (fb or {}).items() if b is None)
    bad = sorted(p for p in FROZEN_PATHS if fb and fb.get(p) and blob(X, p) != fb[p])
    nprobs = ninth_problems(pf, PROBE_SPEC, show(X, NINTH), True)
    record('C2', 'the frozen execution blobs and the ninth path\'s named content at X',
           fb is not None and set(fb) == FROZEN_PATHS and not pend and not bad and not nprobs,
           ('pending %s ' % pend if pend else '') + ('differ %s ' % bad if bad else '') + '; '.join(nprobs))
    core, inst = show(X, CORE), show(X, INST)
    probs = s1(core, inst, frozen_surface(pf), NS)
    record('S1', 'surface: the two modules equal the frozen blocks', not probs, '; '.join(probs))
    probs = s2(X, pf)
    record('S2', 'the landed objects and cited spans on their pinned lines; the prose citations pinned', not probs,
           '; '.join(probs))
    probs = s3(core, inst)
    record('S3', 'the statement-level design invariants', not probs, '; '.join(probs))
    hits = s4([('core header', header_of(core)), ('instances header', header_of(inst))])
    record('S4', 'both module headers present, with no excluded phrase',
           bool(header_of(core).strip()) and bool(header_of(inst).strip()) and not hits, str(hits) if hits else '')
    wd, wx = workflow(show(D, WORKFLOW), SPLICES), show(X, WORKFLOW)
    record('W', 'the workflow at X is D\'s with the frozen splices, installing the SymPy pin',
           wd is not None and wx is not None and wx == wd and pin_ok(SPLICES, PROBE_SPEC))
    rd, rx = root_expected(show(D, ROOT)), show(X, ROOT)
    record('I', 'the two import lines after D\'s last import', rd is not None and rx is not None and rx == rd)
    record('J', 'the census at X is D\'s with the frozen families', registry_ok(show(D, REGISTRY), show(X, REGISTRY),
                                                                                   FAMILIES))
    aprobs, bound = archive_citations(lambda q: show(X, q), lambda run: names_run(X, run))
    record('A', "the archive's pending citations of this record stand as the archive records them", not aprobs,
           '; '.join(aprobs) if aprobs else '%d run(s) cited on their recorded lines only' % len(bound))
    diff = [x for x in git('diff', '--no-renames', '--name-status', D, X).splitlines() if x.strip()]
    gp = governed(pf)
    badg = g(diff, gp or [])
    record('G', 'every change from D lies in the governed paths; no receipt; the legacy manifest untouched',
           gp == GOVERNED and bool(diff) and not badg and blob(X, RECEIPT) is None
           and blob(D, LEGACY) is not None and blob(D, LEGACY) == blob(X, LEGACY),
           str(badg) if badg else '%d paths' % len(diff))
    return outcomes


CANDIDATE = ['C2', 'S1', 'S2', 'S3', 'S4', 'W', 'I', 'J', 'A', 'G']


# ---------------------------------------------------------------- self-test fixture (synthetic, never compiled)

FIX_NS = 'OIBridge.PreservationInductionFixture'
FIX_CORE = '''import OIBridge.ImplementationLocality

/-!
Synthetic self-test fixture of controls.py: never compiled, not the adopted module.
-/

namespace {NS}

open Matrix InterventionLocality OperationalAssembly ReferenceExtension MonoidalCompletion SpectatorBridge

abbrev CarrierConeFamily :=
  ∀ (S : Type) [Fintype S] [DecidableEq S], Set (Matrix S S ℂ)

structure AdditiveClosure (C : CarrierConeFamily) : Prop where
  zero_mem : ∀ (S : Type) [Fintype S] [DecidableEq S], (0 : Matrix S S ℂ) ∈ C S
  add_mem : ∀ (S : Type) [Fintype S] [DecidableEq S] (X Y : Matrix S S ℂ),
    X ∈ C S → Y ∈ C S → X + Y ∈ C S

def PreservesCarrier (C : CarrierConeFamily) (S : Type) [Fintype S] [DecidableEq S]
    (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) : Prop :=
  ∀ X, X ∈ C S → Φ X ∈ C S

structure PrimitivePreservation (𝓘 : ImplementationClass) (C : CarrierConeFamily) : Prop where
  op : ∀ (S : Type) [Fintype S] [DecidableEq S] (K : Matrix S S ℂ),
    𝓘 S K → Kᴴ * K = 1 → PreservesCarrier C S (conjChannel K)
  readout : ∀ (S T : Type) [Fintype S] [DecidableEq S] [Fintype T] [DecidableEq T]
    (m : ℕ) (e : T × Fin m ≃ S),
    (∀ k, 𝓘 S (Matrix.reindex e e (readProj T m k))) →
    ∀ k, PreservesCarrier C S (conjChannel (Matrix.reindex e e (readProj T m k)))

def UniformAttachPreservation (C : CarrierConeFamily) : Prop :=
  ∀ (S : Type) [Fintype S] [DecidableEq S] (m : ℕ), 0 < m →
    ∀ X, X ∈ C S → uniformAttach m X ∈ C (S × Fin m)

def AncillaDiscardPreservation (C : CarrierConeFamily) : Prop :=
  ∀ (S : Type) [Fintype S] [DecidableEq S] (m : ℕ), 0 < m →
    ∀ X, X ∈ C (S × Fin m) → ptraceAnc m X ∈ C S

theorem finite_sum_mem (C : CarrierConeFamily) (hC : AdditiveClosure C)
    {S : Type} [Fintype S] [DecidableEq S] {ι : Type} (s : Finset ι)
    (X : ι → Matrix S S ℂ) (hX : ∀ i ∈ s, X i ∈ C S) :
    (∑ i ∈ s, X i) ∈ C S := by
  fixture_proof

theorem instAvail_preserves (C : CarrierConeFamily) (hC : AdditiveClosure C)
    {𝓘 : ImplementationClass} (hPrim : PrimitivePreservation 𝓘 C)
    (hAttach : UniformAttachPreservation C) (hDiscard : AncillaDiscardPreservation C)
    {S : Type} [Fintype S] [DecidableEq S] {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (h : InstAvail 𝓘 S O F) :
    ∀ a, PreservesCarrier C S (F a) := by
  classical
  induction h with
  | op K hK hiso => exact fixture_op
  | readout e hP => exact fixture_readout
  | coarse f _ ih => exact finite_sum_mem C hC _ _ fixture_coarse
  | bind _ _ ihF ihG => exact fixture_bind
  | discard hm _ ih => exact hDiscard _ _ hm _ (ih a _ (hAttach _ _ hm X hX))

theorem instAvail_sum_preserves (C : CarrierConeFamily) (hC : AdditiveClosure C)
    {𝓘 : ImplementationClass} (hPrim : PrimitivePreservation 𝓘 C)
    (hAttach : UniformAttachPreservation C) (hDiscard : AncillaDiscardPreservation C)
    {S : Type} [Fintype S] [DecidableEq S] {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (h : InstAvail 𝓘 S O F) :
    PreservesCarrier C S (∑ a, F a) := by
  exact finite_sum_mem C hC _ _ fun a _ => instAvail_preserves C hC hPrim hAttach hDiscard h a

theorem instAvail_spectator_preserves (C : CarrierConeFamily) (hC : AdditiveClosure C)
    {𝓘 : ImplementationClass} (hPrim : PrimitivePreservation 𝓘 C)
    (hAttach : UniformAttachPreservation C) (hDiscard : AncillaDiscardPreservation C)
    (hc : ContextStable 𝓘) (hl : LabelInvariant 𝓘)
    (R : Type) [Fintype R] [DecidableEq R]
    {S : Type} [Fintype S] [DecidableEq S] {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (h : InstAvail 𝓘 S O F) :
    ∀ a, PreservesCarrier C (R × S) (amplRefL R (F a)) :=
  instAvail_preserves C hC hPrim hAttach hDiscard (instAvail_spectator hc hl R h)

theorem instAvail_transport_preserves (C : CarrierConeFamily) (hC : AdditiveClosure C)
    {𝓘 : ImplementationClass} (hPrim : PrimitivePreservation 𝓘 C)
    (hAttach : UniformAttachPreservation C) (hDiscard : AncillaDiscardPreservation C)
    (hl : LabelInvariant 𝓘)
    {S : Type} [Fintype S] [DecidableEq S] {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (h : InstAvail 𝓘 S O F)
    (S' : Type) [Fintype S'] [DecidableEq S'] (e : S ≃ S') :
    ∀ a, PreservesCarrier C S' (transport e (F a)) :=
  instAvail_preserves C hC hPrim hAttach hDiscard (instAvail_transport hl h S' e)

#print axioms instAvail_preserves
#print axioms instAvail_sum_preserves
#print axioms instAvail_spectator_preserves
#print axioms instAvail_transport_preserves

end {NS}
'''
FIX_INST = '''import OIBridge.PreservationInduction
import OIBridge.StructuralClosure

/-!
Synthetic self-test fixture of controls.py: never compiled, not the adopted module.
-/

namespace {NS}

open Matrix InterventionLocality OperationalAssembly MonoidalCompletion
open scoped ComplexOrder

abbrev quantumCone : CarrierConeFamily := fun _ _ _ => {X | X.PosSemidef}

abbrev classicalCone : CarrierConeFamily := fun _ _ _ =>
  {X | X.PosSemidef ∧ ∃ d, X = Matrix.diagonal d}

abbrev classicalClass : ImplementationClass := substratumClass

theorem classicalCone_iff {S : Type} [Fintype S] [DecidableEq S] (X : Matrix S S ℂ) :
    X ∈ classicalCone S ↔ ∃ d, (∀ i, 0 ≤ d i) ∧ X = Matrix.diagonal d := by
  fixture_proof

theorem quantum_additive : AdditiveClosure quantumCone where
  zero_mem := fixture_zero
  add_mem := fixture_add

theorem quantum_conj {S : Type} [Fintype S] [DecidableEq S] (K : Matrix S S ℂ) :
    PreservesCarrier quantumCone S (conjChannel K) := by
  fixture_proof

theorem quantum_primitive (𝓘 : ImplementationClass) : PrimitivePreservation 𝓘 quantumCone where
  op := fixture_op
  readout := fixture_readout

def attachBlock {S : Type} [Fintype S] [DecidableEq S] (m : ℕ)
    (e : Fin m) (X : Matrix S S ℂ) : Matrix (S × Fin m) (S × Fin m) ℂ :=
  let P := Matrix.diagonal (fun p : S × Fin m => if p.2 = e then (1 : ℂ) else 0)
  P * X.submatrix Prod.fst Prod.fst * Pᴴ

theorem attachBlock_apply {S : Type} [Fintype S] [DecidableEq S] (m : ℕ) (e : Fin m)
    (X : Matrix S S ℂ) (p q : S × Fin m) :
    attachBlock m e X p q = if p.2 = e ∧ q.2 = e then X p.1 q.1 else 0 := by
  fixture_proof

theorem uniformAttach_eq_blocks {S : Type} [Fintype S] [DecidableEq S] (m : ℕ) (X : Matrix S S ℂ) :
    uniformAttach m X = (m : ℂ)⁻¹ • ∑ e : Fin m, attachBlock m e X := by
  fixture_proof

theorem quantum_attach : UniformAttachPreservation quantumCone := by
  fixture_proof

theorem ptraceAnc_eq_blocks {S : Type} [Fintype S] [DecidableEq S] (m : ℕ)
    (X : Matrix (S × Fin m) (S × Fin m) ℂ) :
    ptraceAnc m X = ∑ e : Fin m, X.submatrix (fun s => (s, e)) (fun s => (s, e)) := by
  fixture_proof

theorem quantum_discard : AncillaDiscardPreservation quantumCone := by
  fixture_proof

theorem quantum_instAvail {𝓘 : ImplementationClass}
    {S : Type} [Fintype S] [DecidableEq S] {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (h : InstAvail 𝓘 S O F) :
    ∀ a, PreservesCarrier quantumCone S (F a) :=
  instAvail_preserves quantumCone quantum_additive (quantum_primitive 𝓘) quantum_attach quantum_discard h

theorem quantum_fullClass {S : Type} [Fintype S] [DecidableEq S] {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (h : InstAvail fullClass S O F) :
    ∀ a, PreservesCarrier quantumCone S (F a) := quantum_instAvail h

theorem classical_additive : AdditiveClosure classicalCone where
  zero_mem := fixture_zero
  add_mem := fixture_add

theorem classical_conj {S : Type} [Fintype S] [DecidableEq S] (K : Matrix S S ℂ) (hK : classicalClass S K) :
    PreservesCarrier classicalCone S (conjChannel K) := by
  fixture_proof

theorem classical_primitive : PrimitivePreservation classicalClass classicalCone where
  op := fixture_op
  readout := fixture_readout

theorem classical_attach : UniformAttachPreservation classicalCone := by
  fixture_proof

theorem classical_discard : AncillaDiscardPreservation classicalCone := by
  fixture_proof

theorem classical_readProj {S T : Type} [Fintype S] [DecidableEq S] [Fintype T] [DecidableEq T]
    (m : ℕ) (e : T × Fin m ≃ S) (k : Fin m) :
    classicalClass S (Matrix.reindex e e (readProj T m k)) := by
  fixture_proof

theorem classical_instAvail {S : Type} [Fintype S] [DecidableEq S] {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (h : InstAvail classicalClass S O F) :
    ∀ a, PreservesCarrier classicalCone S (F a) :=
  instAvail_preserves classicalCone classical_additive classical_primitive classical_attach classical_discard h

theorem classical_native_readout {S T : Type} [Fintype S] [DecidableEq S] [Fintype T] [DecidableEq T]
    (m : ℕ) (e : T × Fin m ≃ S) :
    ∀ k, PreservesCarrier classicalCone S (conjChannel (Matrix.reindex e e (readProj T m k))) := by
  fixture_proof

example : ContextStable classicalClass := substratumClass_contextStable
example : LabelInvariant classicalClass := substratumClass_labelInvariant

#print axioms quantum_instAvail
#print axioms classical_instAvail
#print axioms quantum_attach
#print axioms quantum_discard
#print axioms classical_readProj
#print axioms classical_native_readout

end {NS}
'''
FIX_SPLICES = [('    needs: [probes_a]\n', '    needs: [probes_a, probes_preserveinduct1]\n'),
               ('jobs:\n', 'jobs:\n  probes_preserveinduct1:\n    runs-on: fixture\n'
                '    steps:\n      - run: python -m pip install sympy==1.14.0\n')]
FIX_FAMILIES = [{'name': 'fixture family (synthetic)', 'modules': ['PreservationInduction',
                                                                   'PreservationInductionInstances'],
                 'status': 'kernel-only', 'manuscript': [], 'note': 'synthetic'}]
FIX_MANIFEST = 'f' * 64
FIX_OUT = {'probe': 'SYMPY 1.14.0\nPASS FIX1 (3)\nPASS FIX2 (3)\nREJECTED m1: FIX1\n'
                    'mutations: 1 rejected, 0 survived, 0 undecided\n'
                    'SAMPLE-MANIFEST-SHA256 %s\nchecks: 6, failures: 0\nfixture_probe: OK -- 6 checks\n' % FIX_MANIFEST,
           'indep': 'PASS IND1 (1)\nSAMPLE-MANIFEST-SHA256 %s\nchecks: 1, failures: 0\nfixture_indep: OK -- 1 checks\n'
                    % FIX_MANIFEST}
_sha = lambda s: hashlib.sha256(s.encode('utf-8')).hexdigest()
FIX_SPEC = {'sympy': '1.14.0', 'manifest': FIX_MANIFEST, 'mutations': ['m1: FIX1'],
            'probe': {'codes': ['FIX1', 'FIX2'], 'n': 6, 'final': 'fixture_probe: OK -- 6 checks',
                      'stdout_sha256': _sha(FIX_OUT['probe'])},
            'indep': {'codes': ['IND1'], 'n': 1, 'final': 'fixture_indep: OK -- 1 checks',
                      'stdout_sha256': _sha(FIX_OUT['indep'])}}


FIX_ROADMAP = '\n'.join('synthetic ROADMAP fixture line %d' % i for i in range(1, 1141)) + '\n'
FIX_SPANS = [(p, a, b, span_digest(FIX_ROADMAP, a, b)) for p, a, b, _ in CITED_SPANS]


def fix_res(probe=None, indep=None, rc=(0, 0), err=('', '')):
    """A probe result in run_probe's shape from the fixture outputs, or the given ones."""
    return {'probe': (rc[0], FIX_OUT['probe'] if probe is None else probe, err[0]),
            'indep': (rc[1], FIX_OUT['indep'] if indep is None else indep, err[1])}


def git_blob_id(text):
    b = text.encode('utf-8')
    return hashlib.sha1(b'blob %d\0' % len(b) + b).hexdigest()


def fix_log(ns, names, axioms='propext, Classical.choice, Quot.sound'):
    return '\n'.join("info: x.lean:1:0: '%s.%s' depends on axioms: [%s]" % (ns, n, axioms) for n in names) + '\n'


FIX_E_SHA = '0e' * 20
FIX_TS = '2026-10-19T00:00:00.0000000Z '


def gate_text(step, ns=FIX_NS):
    """The axiom gate's output on `step`, as main prints it, and its final line; FAILED adds the runner's error."""
    lines = ['%s axioms: %s%s' % ('PASS' if ok else 'FAIL', n, ('  ' + d) if d else '') for n, ok, d in axioms_gate(step, ns)]
    good = all(ok for _, ok, _ in axioms_gate(step, ns))
    lines.append(GATE_OK if good else 'preserve_induct1 axioms: FAILED')
    lines.append('controls: %s' % ('OK (0 failure(s))' if good else 'FAILED (1 failure(s))'))
    return '\n'.join(lines) + '\n' + ('' if good else '##[error]Process completed with exit code 1.\n')


def fix_bridge(step=None, sha=FIX_E_SHA, gate='auto', build=None, extra_after='', checkout=None, ns=FIX_NS,
               tail=''):
    """A served bridge-job log in GitHub's layout, every line timestamped (synthetic): the checkout naming `checkout`
    (default sha), the Build step's own copies of the reports (`build`, default the ten clean), the release gate's
    summary with the untruncated 'no sorryAx' text, then the final step: its echoed script, its marker naming
    `sha`, the step's reports (`step`, default the ten clean), the gate's output ('auto' renders the real gate on
    those reports; 'ok' or 'failed' forces the final line; 'none' omits it; any other string is used as is),
    `extra_after`, the job's cleanup, then `tail`."""
    names = CORE_PRINTS + INST_PRINTS
    step = fix_log(ns, names).replace('info: x.lean:1:0: ', '') if step is None else step
    build = fix_log(ns, names) if build is None else build
    if gate == 'auto':
        g = gate_text(step, ns)
    elif gate == 'ok':
        g = GATE_OK + '\ncontrols: OK (0 failure(s))\n'
    elif gate == 'failed':
        g = 'preserve_induct1 axioms: FAILED\n##[error]Process completed with exit code 1.\n'
    elif gate == 'none':
        g = ''
    else:
        g = gate
    body = ('##[group]Run actions/checkout@v4\n##[endgroup]\n[command]/usr/bin/git log -1 --format=%%H\n%s\n'
            '##[group]Run lean --version\n%s'
            '##[group]Run python3 tools/release_gate.py\n'
            '  PASS  lean-axioms      lean_axiom_check: OK (5989 named result(s) reported, no sorryAx, every axiom '
            'within {propext, Classical.choice, Quot.sound}; self-test passed)\n'
            '##[group]Run set -euo pipefail\n\x1b[36;1mset -euo pipefail\x1b[0m\n'
            '\x1b[36;1mhead=$(git rev-parse HEAD)\x1b[0m\n'
            '\x1b[36;1mecho "preserve_induct1 axioms: step at ${head}"\x1b[0m\n'
            '\x1b[36;1mpython3 -I -B ../programmes/oi-qm/reconstruction/round-preserve-induct-1/controls.py axioms '
            '"$log"\x1b[0m\n##[endgroup]\n'
            'preserve_induct1 axioms: step at %s\n%s%s%sPost job cleanup.\n%s') % (
        checkout or sha, build, sha, step, g, extra_after, tail)
    return ''.join(FIX_TS + l + '\n' for l in body.split('\n')[:-1])


def set_row(prereg, label, file_cell, sha_cell):
    """Rewrite the retention row `label` with the given cells."""
    return re.sub(r'^\| `%s` \|[^\n]*$' % re.escape(label), lambda m: '| `%s` | %s | %s |' % (label, file_cell, sha_cell),
                  prereg, count=1, flags=re.M)


def fill_ninth(prereg, text, spec, blob_id):
    """The ninth-path table rewritten for a fixture file `text`, the probe spec `spec` and its pinned blob."""
    s = spec['indep']
    b = text.encode('utf-8')
    rows = {'path': '`%s`' % NINTH, 'governed entry': '`execution A %s`' % NINTH, 'blob': '`%s`' % blob_id,
            'sha256': '`%s`' % hashlib.sha256(b).hexdigest(), 'bytes': '`%d`' % len(b),
            'imports': ', '.join('`%s`' % m for m in py_imports(text)) or 'none',
            'codes': ', '.join('`%s`' % c for c in s['codes']), 'checks': '`%d`' % s['n'],
            'final line': '`%s`' % s['final'], 'stdout sha256': '`%s`' % s['stdout_sha256']}
    for k, v in rows.items():
        prereg = re.sub(r'^\| %s \|[^\n]*$' % re.escape(k), lambda m: '| %s | %s |' % (k, v), prereg, count=1,
                        flags=re.M)
    return prereg


def fill(prereg, title, values):
    """Replace the cell of each path of the pin table `title` (pending or pinned) by `values[path]`."""
    for path, v in values.items():
        prereg = re.sub(r'^(\| `%s` \| )[^|\n]*\|' % re.escape(path), lambda m: m.group(1) + '`%s` |' % v,
                        prereg, flags=re.M)
    return prereg


def fake_archive(prereg):
    """A synthetic evidence archive awaiting the preregistration's run citations as they stand: one research-build
    entry and one retained commit per run linked on a line of the preregistration, the head being the 40-digit
    word beside it. The run numbers come from the preregistration, so this source names none."""
    lines, files, entries, objs = prereg.split('\n'), {}, [], []
    for n, l in enumerate(lines, 1):
        for run in sorted(set(re.findall(r'/actions/runs/([0-9]+)', l))):
            win = ' '.join(lines[k - 1] for k in (n - 1, n, n + 1) if 1 <= k <= len(lines))
            head = (re.findall(r'(?<![0-9a-f])[0-9a-f]{40}(?![0-9a-f])', win) or ['0' * 40])[0]
            res = '{"synthetic": "archived fixture result, not run evidence", "line": %d}\n' % n
            files[ARCHIVE + 'ci/%s/run.json' % run] = json.dumps({'head_sha': head}) + '\n'
            files[ARCHIVE + 'ci/%s/results.json' % run] = res
            entries.append({'id': 'research-' + run, 'kind': 'derived', 'run_id': run,
                            'awaiting_citation': {'round': ROUND, 'record': PREREG, 'line': n, 'head': head,
                                                  'pull_request': 831},
                            'files': [{'path': 'ci/%s/results.json' % run, 'sha256': _sha(res)}]})
            objs.append({'oid': head, 'awaiting_citation': {'round': ROUND, 'record': PREREG, 'run': run,
                                                            'pull_request': 831}})
    files[ARCHIVE + 'manifest.json'] = json.dumps({'entries': entries}, indent=1) + '\n'
    files[ARCHIVE + 'objects/manifest.json'] = json.dumps({'objects': objs}, indent=1) + '\n'
    return files


def fake_repo(prereg, src):
    """An in-memory D, F, E: D holds synthetic shared files, F adds the preregistration with every pending pin
    filled and a statement-surface section built from the fixture modules, and E holds the fixture execution:
    the two modules, a stub probe, this source, evidence files, an f-run file and a result note. Every file is
    synthetic and labelled as such; none is run evidence."""
    core, inst = FIX_CORE.replace('{NS}', FIX_NS), FIX_INST.replace('{NS}', FIX_NS)
    landed = {}
    for path, line, name in LANDED:
        landed.setdefault(path, {})[line] = 'def %s : fixture' % name
    Dm = {p: '\n'.join(v.get(i, '-- synthetic filler') for i in range(1, max(v) + 2)) + '\n' for p, v in landed.items()}
    Dm[WORKFLOW] = 'jobs:\n  probes_a:\n    runs-on: fixture\n  aggregate:\n    needs: [probes_a]\n'
    Dm[ROOT] = 'import OIBridge.A\nimport OIBridge.B\n\nnamespace OIBridge\n'
    Dm[REGISTRY] = json.dumps({'families': [{'name': 'x', 'modules': ['A']}]}, indent=2) + '\n'
    Dm[LEGACY] = '{"synthetic": true}\n'
    Dm[ROADMAP] = FIX_ROADMAP
    E = dict(Dm)
    E[CORE], E[INST] = core, inst
    E[PROBE] = '# synthetic stub probe; the self-test never runs it\n'
    E[INDEP] = '# synthetic stub independent check; the self-test never runs it\nimport sys\n'
    E[CONTROLS] = src
    rows = {}
    for label in sorted(retention(prereg) or {}):
        p = 'evidence/%s.json' % label
        E[RDIR + p] = '{"synthetic": "controls self-test fixture, not run evidence", "row": "%s"}\n' % label
        rows[label] = (p, hashlib.sha256(E[RDIR + p].encode('utf-8')).hexdigest())
    E[RDIR + FRUN + 'f-run.json'] = '{"synthetic": "fixture"}\n'
    E[RESULT] = '# PRESERVE-INDUCT-1 result (synthetic self-test fixture)\n\nNo claim.\n'
    E[WORKFLOW] = workflow(Dm[WORKFLOW], FIX_SPLICES)
    E[ROOT] = root_expected(Dm[ROOT])
    reg = json.loads(Dm[REGISTRY]); reg['families'].extend(FIX_FAMILIES)
    E[REGISTRY] = json.dumps(reg, indent=2) + '\n'
    pf = fill(prereg, 'Frozen execution blobs.', {p: git_blob_id(E[p]) for p in FROZEN_PATHS})
    pf = fill_ninth(pf, E[INDEP], FIX_SPEC, git_blob_id(E[INDEP]))
    for label, (p, h) in rows.items():
        pf = set_row(pf, label, '`%s`' % p, '`%s`' % h)
    if '\n## The statement surface (frozen' in pf:
        pf = pf[:pf.index('\n## The statement surface (frozen')] + '\n'
    pf += '\n## The statement surface (frozen; synthetic fixture)\n\n```lean\n%s```\n\n```lean\n%s```\n' % (
        render_block(core), render_block(inst))
    arch = fake_archive(pf)
    Dm.update(arch)
    E.update(arch)
    Fm = dict(Dm); Fm[PREREG] = pf
    E[PREREG] = pf
    return {'D': Dm, 'F': Fm, 'E': E, 'flags': {'pre': 'F D', 'lin': 'E S1\nS1 F', 'anc': True}}


def install_fake(mod, repo):
    key = lambda c: 'D' if c == D else c
    mod.show = lambda c, p: repo[key(c)].get(p)
    mod.blob = lambda c, p: git_blob_id(repo[key(c)][p]) if repo[key(c)].get(p) is not None else None
    mod.is_ancestor = lambda a, b: repo['flags']['anc']

    def fgit(*args):
        if args[0] == 'ls-tree':
            return '\n'.join(sorted(p for p, t in repo[key(args[3])].items() if t is not None and p.startswith(args[5])))
        if args[:3] == ('diff', '--no-renames', '--name-status'):
            a, b = repo[key(args[3])], repo[key(args[4])]
            rows = [('A\t' if a.get(p) is None else 'M\t') + p for p in sorted(b) if b[p] is not None
                    and a.get(p) != b[p]]
            return '\n'.join(rows + ['D\t' + p for p in sorted(a) if a[p] is not None and b.get(p) is None])
        if args[:2] == ('diff', '--name-only'):
            a, b = repo[key(args[2])], repo[key(args[3])]
            return '\n'.join(p for p in sorted(set(a) | set(b)) if a.get(p) != b.get(p))
        if args[:2] == ('rev-list', '--parents'):
            return repo['flags']['pre' if args[2].endswith('..F') else 'lin']
        raise ValueError('fake git: unsupported ' + ' '.join(args))
    mod.git = fgit

    def fnames(c, run):
        rx = re.compile(r'(?<![0-9])%s(?![0-9])' % re.escape(run))
        return {p for p, txt in repo[key(c)].items() if txt is not None and not p.startswith(ARCHIVE) and rx.search(txt)}
    mod.names_run = fnames


def load(src, name, params=True, **override):
    """The module built from src, with the fixture's parameters (params True) or every PENDING one unset."""
    mod = types.ModuleType(name)
    mod.__file__ = __file__
    exec(compile(src, name, 'exec'), mod.__dict__)
    if params:
        mod.NS, mod.SPLICES, mod.FAMILIES, mod.PROBE_SPEC = FIX_NS, FIX_SPLICES, FIX_FAMILIES, FIX_SPEC
    else:
        mod.NS = mod.SPLICES = mod.FAMILIES = mod.PROBE_SPEC = None
    mod.CITED_SPANS = FIX_SPANS
    mod.full_sha = lambda c: FIX_E_SHA if c in ('E', FIX_E_SHA) else None
    for k, v in override.items():
        setattr(mod, k, v)
    return mod


def end_to_end(src, repo, axlog, params=True, **override):
    """check() then verdict() of the module built from src, on the fake repo; (ok, output, probe calls)."""
    mod = load(src, 'controls_e2e', params, **override)
    install_fake(mod, repo)
    calls = []

    def probe(E, *a):
        calls.append(E)
        return fix_res()
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        ok = mod.verdict('E', 'F', axlog, probe_fn=probe)
    return ok, buf.getvalue(), len(calls)


def drop_record(src, code):
    """Source mutation: remove the record call of `code` inside check(), whole statement, replaced by `pass`."""
    start = src.index('def check(E, F')
    i = src.index("record('%s'," % code, start)
    depth, j = 0, i + len('record')
    while True:
        ch = src[j]
        depth += ch == '('
        depth -= ch == ')'
        j += 1
        if depth == 0:
            break
    return src[:i] + 'pass' + src[j:]


def failed_named(out, codes):
    m = re.search(r'^STATIC CONTROLS FAILED: (.*)$', out, re.M)
    return m is not None and all(c in m.group(1).split(', ') for c in codes)


def leaked(out):
    return [t for t in POSITIVE if has_token(out, t)]


def e2e_cases(prereg):
    """The real check() through verdict(): unmutated; each control's record call removed; each control's inputs
    absent; the shipped (pending) parameters; main()'s exits and stage handling. Returns (problems, cases)."""
    src = open(__file__, encoding='utf-8').read()
    problems, n = [], 0
    repo = fake_repo(prereg, src)
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, 'bridge.log')
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(fix_bridge())
        n += 1
        ok, out, calls = end_to_end(src, repo, path)
        if not ok or calls != 1 or leaked(out) != POSITIVE or re.search(r'^FAIL ', out, re.M):
            problems.append('unmutated: result %s, probe calls %d, positive %s, failures %s' % (
                ok, calls, leaked(out), re.findall(r'^FAIL .*$', out, re.M)))
        for code in REQUIRED['E']:
            n += 1
            if src[src.index('def check(E, F'):src.index('def passed(')].count("record('%s'," % code) != 1:
                problems.append('%s: not exactly one record call in check()' % code); continue
            ok, out, calls = end_to_end(drop_record(src, code), repo, path)
            if ok or leaked(out) or not failed_named(out, [code]) or calls:
                problems.append('%s record removed: result %s, positive %s, named %s, probe calls %d'
                                % (code, ok, leaked(out), failed_named(out, [code]), calls))

        def variant(edit):
            r = {k: dict(v) for k, v in repo.items()}
            edit(r)
            return r

        def drop(*spec):
            def ed(r):
                for c, p in spec:
                    r[c][p] = None
            return ed

        def prereg_edit(f):
            def ed(r):
                r['F'][PREREG] = r['E'][PREREG] = f(r['F'][PREREG])
            return ed
        def gapped(r, labels, keep=False):
            for c in ('F', 'E'):
                for label in labels:
                    r[c][PREREG] = set_row(r[c][PREREG], label, 'none', 'gap: log not recoverable (fixture)')
            if not keep:
                for label in labels:
                    r['E'][RDIR + 'evidence/%s.json' % label] = None

        def archived(r, labels, at_d=True):
            for label in labels:
                a = 'verification/audits/evidence-retention/fixture/%s.json' % label
                body = '{"synthetic": "archived fixture, not run evidence", "row": "%s"}\n' % label
                r['E'][a] = body
                if at_d:
                    r['D'][a] = r['F'][a] = body
                r['E'][RDIR + 'evidence/%s.json' % label] = None
                for c in ('F', 'E'):
                    r[c][PREREG] = set_row(r[c][PREREG], label, '`%s`' % a,
                                           '`%s`' % hashlib.sha256(body.encode('utf-8')).hexdigest())
        def awaited(r):
            """{line: (run, results path)} of the fixture archive's entries."""
            man = json.loads(r['E'][ARCHIVE + 'manifest.json'])
            return {e['awaiting_citation']['line']: (e['run_id'], ARCHIVE + e['files'][0]['path']) for e in man['entries']}

        def in_archive(r, labels, good=True):
            for label in labels:
                run, res = awaited(r)[HIST_LINES[label]]
                h = hashlib.sha256(r['E'][res].encode('utf-8')).hexdigest() if good else '0' * 64
                r['E'][RDIR + 'evidence/%s.json' % label] = None
                for c in ('F', 'E'):
                    r[c][PREREG] = set_row(r[c][PREREG], label, 'archive', '`%s`' % h)

        def run_on_line(t, n, extra):
            L = t.split('\n')
            L[n - 1] += extra
            return '\n'.join(L)

        def retarget_commit(r):
            for c in ('D', 'F', 'E'):
                om = json.loads(r[c][ARCHIVE + 'objects/manifest.json'])
                om['objects'][0]['oid'] = '1' * 40
                r[c][ARCHIVE + 'objects/manifest.json'] = json.dumps(om)
        first_run = awaited(repo)[sorted(HIST_LINES.values())[0]][0]
        ev = sorted(p for p in repo['E'] if p.startswith(RDIR + 'evidence/') and not p.startswith(RDIR + FRUN))[:1]
        frun = [p for p in repo['E'] if p.startswith(RDIR + FRUN)]
        strip_hdr = lambda t: re.sub(r'/-!.*?-/\n', '', t, count=1, flags=re.S)
        cut = lambda title: (lambda t: re.sub(r'\*\*%s\*\*.*?\n\n(?:\|.*\n)+' % re.escape(title), '', t, count=1,
                                              flags=re.S))
        absences = [
            ('the preregistration absent at F and E', ['C1'], drop(('F', PREREG), ('E', PREREG))),
            ('the frozen-blob table absent', ['C2'], prereg_edit(cut('Frozen execution blobs.'))),
            ('the retained-evidence table absent', ['P', 'R'], prereg_edit(cut('Retained evidence (§A.42).'))),
            ('the statement-surface section absent', ['S1'],
             prereg_edit(lambda t: t[:t.index('\n## The statement surface (frozen')] + '\n')),
            ('the governed-path block absent', ['G'],
             prereg_edit(lambda t: re.sub(r'```v3-governed-paths\n.*?```\n', '', t, count=1, flags=re.S))),
            ('a landed file absent at D and E', ['S2'], drop(('D', LANDED[0][0]), ('E', LANDED[0][0]))),
            ('the core module absent at E', ['S1', 'S3'], drop(('E', CORE))),
            ('the instances header absent', ['S4'], lambda r: r['E'].__setitem__(INST, strip_hdr(r['E'][INST]))),
            ('the result note absent at E', ['S4', 'R'], drop(('E', RESULT))),
            ('the workflow absent at D and E', ['W'], drop(('D', WORKFLOW), ('E', WORKFLOW))),
            ('OIBridge.lean absent at D and E', ['I'], drop(('D', ROOT), ('E', ROOT))),
            ('the census absent at D and E', ['J'], drop(('D', REGISTRY), ('E', REGISTRY))),
            ('a pinned evidence file absent at E', ['P'], drop(*[('E', e) for e in ev])),
            ('evidence/f-run/ absent at E', ['R'], drop(*[('E', e) for e in frun])),
            ('E identical to D', ['G'], lambda r: r.__setitem__('E', dict(r['D']))),
            ('no execution commit after F', ['T'], lambda r: r['flags'].__setitem__('lin', '')),
            ('the legacy manifest absent at D and E', ['G'], drop(('D', LEGACY), ('E', LEGACY))),
            ('the predicted-tree row recorded as a gap', ['P'], lambda r: gapped(r, [REQUIRED_PIN])),
            ('a historical gap whose file stays in the record directory', ['R'],
             lambda r: gapped(r, sorted(HISTORICAL)[:1], keep=True)),
            ('a retention row dropped', ['P'], prereg_edit(lambda t: re.sub(
                r'^\| `%s` \|[^\n]*\n' % re.escape(REQUIRED_PIN), '', t, count=1, flags=re.M))),
            ('a historical row retained outside the record directory but absent at D', ['P'],
             lambda r: archived(r, sorted(HISTORICAL)[:1], at_d=False)),
            ('the #831 citation removed', ['C1'], prereg_edit(lambda t: t.replace(SUPERSEDED_CITE[1], '#831'))),
            ('an old #831 commit in the drafting chain', ['T'], lambda r: r['flags'].__setitem__(
                'pre', 'F %s\n%s D' % (sorted(OLD_CHAIN)[1], sorted(OLD_CHAIN)[1]))),
            ('the archive manifest absent at D, F and E', ['A'],
             drop(('D', ARCHIVE + 'manifest.json'), ('F', ARCHIVE + 'manifest.json'), ('E', ARCHIVE + 'manifest.json'))),
            ('a research run named in the result note', ['A'],
             lambda r: r['E'].__setitem__(RESULT, r['E'][RESULT] + 'The core build ran as %s.\n' % first_run)),
            ('the record citing its runs one line lower', ['A'], prereg_edit(lambda t: '\n' + t)),
            ('another head beside a run', ['A'],
             prereg_edit(lambda t: run_on_line(t, sorted(HIST_LINES.values())[0] + 1, ' (`abcdef1`)'))),
            ('a run named a second time in the record', ['A'],
             prereg_edit(lambda t: run_on_line(t, 3, ' (run %s)' % first_run))),
            ('a retained commit awaiting the round that heads no awaited run', ['A'], retarget_commit),
            ('an archived historical row whose digest the archive does not hold', ['P'],
             lambda r: in_archive(r, sorted(HISTORICAL), good=False)),
            ('a cited run line rewritten in place', ['A'],
             prereg_edit(lambda t: run_on_line(t, sorted(HIST_LINES.values())[1], ' '))),
            ('a prose citation off its pinned line', ['S2'], prereg_edit(lambda t: t.replace('(:359)', '(:358)', 1))),
            ('the cited ROADMAP span changed at D, F and E', ['S2'],
             lambda r: [r[c].__setitem__(ROADMAP, r[c][ROADMAP].replace('fixture line 1127\n', 'fixture line 1127 '
                                                                         'edited\n')) for c in ('D', 'F', 'E')]),
            ('the ROADMAP changed after D', ['S2', 'G'], lambda r: r['E'].__setitem__(ROADMAP, r['E'][ROADMAP] + 'x\n')),
            ("the ninth path's named byte count wrong", ['C2'],
             prereg_edit(lambda t: re.sub(r'^\| bytes \|[^\n]*$', '| bytes | `1` |', t, count=1, flags=re.M))),
            ("the ninth path's named imports wrong", ['C2'],
             prereg_edit(lambda t: re.sub(r'^\| imports \|[^\n]*$', '| imports | `json` |', t, count=1, flags=re.M))),
        ]
        for name, codes, edit in absences:
            n += 1
            ok, out, calls = end_to_end(src, variant(edit), path)
            if ok or calls or not failed_named(out, codes) or leaked(out):
                problems.append('%s: result %s, %s named %s, probe calls %d, positive %s'
                                % (name, ok, codes, failed_named(out, codes), calls, leaked(out)))
        # frozen splices that install SymPy unpinned, applied faithfully at E: W must still fail
        n += 1
        loose = [(o, nw.replace('sympy==1.14.0', 'sympy')) for o, nw in FIX_SPLICES]
        lrepo = variant(lambda r: r['E'].__setitem__(WORKFLOW, workflow(r['D'][WORKFLOW], loose)))
        ok, out, calls = end_to_end(src, lrepo, path, SPLICES=loose)
        if ok or calls or not failed_named(out, ['W']) or leaked(out):
            problems.append('unpinned SymPy splices: result %s, W named %s, probe calls %d' % (
                ok, failed_named(out, ['W']), calls))
        # historical rows recorded as gaps, or retained on main before D: passing states
        for label, edit in (('historical gaps', lambda r: gapped(r, sorted(HISTORICAL))),
                            ('historical rows retained on main at D', lambda r: archived(r, sorted(HISTORICAL))),
                            ('historical rows held by the archive', lambda r: in_archive(r, sorted(HISTORICAL)))):
            n += 1
            ok, out, calls = end_to_end(src, variant(edit), path)
            if not ok or calls != 1 or leaked(out) != POSITIVE:
                problems.append('%s: result %s, probe calls %d, positive %s, failures %s' % (
                    label, ok, calls, leaked(out), re.findall(r'^FAIL .*$', out, re.M)))
        # the pending state: the live preregistration as it stands, and every PENDING parameter unset
        n += 1
        shipped = variant(prereg_edit(lambda t: prereg))
        ok, out, calls = end_to_end(src, shipped, path, params=False)
        if ok or calls or not failed_named(out, ['C2', 'S1', 'W', 'J', 'P']) or leaked(out):
            problems.append('pending state: result %s, probe calls %d, positive %s' % (ok, calls, leaked(out)))
        # main(): exits, a record call removed, stage handling, unknown arguments
        mods = {'plain': load(src, 'controls_main'), 'dropped': load(drop_record(src, 'T'), 'controls_main_t'),
                'stage1': load(src, 'controls_main_s1')}
        for which, m in mods.items():
            install_fake(m, variant(drop(('E', RESULT))) if which == 'stage1' else repo)
        main_cases = [('plain', ['check', 'E', '--freeze', 'F'], 0),
                      ('stage1', ['check', 'E', '--freeze', 'F', '--stage', 'S1'], 0),
                      ('plain', ['check', 'E', '--freeze', 'F', '--stage', 'S1'], 1),
                      ('dropped', ['check', 'E', '--freeze', 'F'], 1),
                      ('plain', ['check', 'E', '--freeze', 'F', '--stage', 'e'], 2),
                      ('plain', ['check', 'E', '--freeze', 'F', '--stage'], 2),
                      ('plain', ['check', 'E', '--freeze', 'F', '--stgae', 'S1'], 2),
                      ('plain', ['verdict', 'E', '--freeze', 'F', '--axioms'], 2)]
        for which, argv, want in main_cases:
            n += 1
            m = mods[which]
            del m.FAIL[:]
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    got = m.main(argv)
            except Exception as e:  # a refusal must be an exit status, not an exception
                got = '%s: %s' % (type(e).__name__, e)
            if got != want:
                problems.append('main %s %s: exit %s, expected %s' % (which, ' '.join(argv), got, want))
        n += 1
        m = load(src, 'controls_stage')
        install_fake(m, repo)
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                m.check('E', 'F', 'e')
            problems.append("check() accepted the unknown stage 'e'")
        except ValueError:
            pass
    return problems, n


def verdict_regression():
    """Through verdict() itself, with injected static results: each required control failing alone, one left
    unreported, a non-bool value, and the all-clean case; then the cells' separation and the final bridge step's
    rules, on served bridge logs (fix_bridge), the Build step's copies of the reports clean throughout unless
    stated. Returns (problems, cases)."""
    problems, n = [], 0
    mod = load(open(__file__, encoding='utf-8').read(), 'controls_vr')
    with tempfile.TemporaryDirectory() as tmp:
        def put(text, name='bridge.log'):
            fp = os.path.join(tmp, name)
            with open(fp, 'w', encoding='utf-8') as fh:
                fh.write(text)
            return fp
        path = put(fix_bridge())

        def run(results, log=path, E='E', probe=None):
            buf, calls = io.StringIO(), []
            with contextlib.redirect_stdout(buf):
                ok = mod.verdict(E, 'F', log, check_fn=lambda E, F: dict(results),
                                 probe_fn=lambda E, *a: calls.append(E) or (probe or fix_res()))
            return ok, buf.getvalue(), len(calls)
        clean = {c: True for c in REQUIRED['E']}
        n += 1
        ok, out, calls = run(clean)
        if not ok or leaked(out) != POSITIVE or calls != 1 or 'earned reading: full (every cell positive)' not in out:
            problems.append('all-clean: result %s, positive %s, probe calls %d' % (ok, leaked(out), calls))
        cases = [(c, dict(clean, **{c: False})) for c in REQUIRED['E']]
        cases.append(('C2', {c: True for c in REQUIRED['E'] if c != 'C2'}))
        cases.append(('S3', dict(clean, S3=1)))
        for name, results in cases:
            n += 1
            ok, out, calls = run(results)
            if ok or leaked(out) or calls or not failed_named(out, [name]):
                problems.append('%s failing: result %s, positive %s, probe calls %d' % (name, ok, leaked(out), calls))
        names = CORE_PRINTS + INST_PRINTS
        step = lambda ns_names, ax='propext, Classical.choice, Quot.sound': fix_log(FIX_NS, ns_names, ax).replace(
            'info: x.lean:1:0: ', '')
        exact_only, all_pos = [CELLS[2][1], READ], POSITIVE
        lean_cases = [
            # (label, log, E, expected positive tokens)
            ('B1, the reviewer\'s log: clean Build copies, an extra report in the step, the gate FAILED and the '
             'runner\'s error', fix_bridge(step=step(names) + step(['finite_sum_mem'])), 'E', exact_only),
            ('B1 with the gate\'s FAILED line and the error forced over clean step reports',
             fix_bridge(gate='failed'), 'E', exact_only),
            ('no OK line of the gate (the step stopped)', fix_bridge(gate='none'), 'E', exact_only),
            ('two OK lines of the gate', fix_bridge(extra_after=GATE_OK + '\n'), 'E', exact_only),
            ('the OK line before the step\'s last report', fix_bridge(step=step(names[:-1]), gate='ok',
                                                                       extra_after=step(names[-1:])), 'E', exact_only),
            ('a FAILED line of the gate elsewhere in the log', fix_bridge(
                build=fix_log(FIX_NS, names) + 'preserve_induct1 axioms: FAILED\n'), 'E', exact_only),
            ('the step and the checkout at another commit', fix_bridge(sha='1f' * 20), 'E', exact_only),
            ('the step at another commit, the checkout naming E', fix_bridge(sha='1f' * 20, checkout=FIX_E_SHA), 'E',
             exact_only),
            ('the step at another commit, no checkout section', fix_bridge(sha='1f' * 20).replace(
                FIX_TS + '[command]/usr/bin/git log -1 --format=%%H\n%s%s\n' % (FIX_TS, '1f' * 20), ''), 'E', exact_only),
            ('the checkout naming another commit', fix_bridge(checkout='2a' * 20), 'E', exact_only),
            ('no step marker (only the Build step\'s copies)', ''.join(
                FIX_TS + l + '\n' for l in fix_log(FIX_NS, names).splitlines()), 'E', exact_only),
            ('two step markers', fix_bridge(extra_after='preserve_induct1 axioms: step at %s\n' % FIX_E_SHA), 'E',
             exact_only),
            ('an error line in the step', fix_bridge(extra_after='##[error]Process completed with exit code 1.\n'),
             'E', exact_only),
            ('a forbidden token in the step', fix_bridge(extra_after='warning: uses Lean.ofReduceBool\n'), 'E',
             exact_only),
            ('a report repeated in the step', fix_bridge(step=step(names) + step(names[:1]), gate='ok'), 'E',
             exact_only),
            ('E with no full SHA', fix_bridge(), 'X', exact_only),
            ('a dirty instance report in the step', fix_bridge(step=step([p for p in names if p != INST_PRINTS[0]])
                                                               + step(INST_PRINTS[:1], 'sorryAx')), 'E', exact_only),
            ('an instance report with an extra axiom, the OK line forced', fix_bridge(
                step=step([p for p in names if p != INST_PRINTS[0]]) + step(
                    INST_PRINTS[:1], 'propext, Classical.choice, Quot.sound, oops'), gate='ok'), 'E', exact_only),
            ('an instance report missing, the OK line forced', fix_bridge(
                step=step([p for p in names if p != INST_PRINTS[0]]), gate='ok'), 'E', exact_only),
            ('a dirty headline report, the OK line forced', fix_bridge(
                step=step(names[1:]) + step([HEADLINE], 'propext, oops'), gate='ok'), 'E', exact_only),
            ('a corollary report missing, the OK line forced', fix_bridge(
                step=step([p for p in names if p != COR_PRINTS[2]]), gate='ok'), 'E', [CELLS[0][1], CELLS[2][1], READ]),
            ('dirty Build-step copies, a clean step: only the step is read', fix_bridge(
                build=fix_log(FIX_NS, names, 'propext, sorryAx')), 'E', all_pos),
            ('a later step after the block with dirty reports', fix_bridge(
                extra_after='##[group]Run later\n' + step(names, 'propext, oops')), 'E', all_pos),
            ('reports after the job\'s cleanup', fix_bridge(tail=step(names, 'oops')), 'E', all_pos),
            ('the release gate\'s untruncated summary naming the token, outside the step', fix_bridge(), 'E', all_pos),
            ('no axiom log', None, 'E', exact_only),
        ]
        for label, log, E, want in lean_cases:
            n += 1
            ok, out, calls = run(clean, put(log, 'case.log') if log is not None else None, E)
            if not ok or leaked(out) != want or calls != 1:
                problems.append('%s: positive %s, expected %s' % (label, leaked(out), want))
        if 'preserve_induct1 axioms: FAILED' not in gate_text(step(names) + step(['finite_sum_mem'])):
            problems.append('the B1 fixture does not carry the gate\'s FAILED line')
        if '--format=%H' in fix_bridge(sha='1f' * 20).replace(
                FIX_TS + '[command]/usr/bin/git log -1 --format=%%H\n%s%s\n' % (FIX_TS, '1f' * 20), ''):
            problems.append('the no-checkout fixture still carries the checkout line')
        # a failing probe leaves the Lean cells positive and the earned reading not full
        n += 1
        ok, out, _ = run(clean, probe=fix_res(indep=FIX_OUT['indep'].replace('PASS IND1 (1)', 'FAIL IND1')))
        if not ok or leaked(out) != [CELLS[0][1], CELLS[1][1], READ] or 'earned reading: not full (Q-EXACT' not in out:
            problems.append('failing probe: positive %s' % leaked(out))
    return problems, n


def in_decl(text, name, old, new):
    """Replace old by new once, inside the declaration `name` only."""
    m = re.search(r'^(?:theorem|def|abbrev|structure) %s\b' % re.escape(name), text, re.M)
    if not m:
        return text
    rest = text[m.end():]
    k = re.search(r'^(?:(?:noncomputable )?(?:def|abbrev|theorem|structure)\s|example\b|#)', rest, re.M)
    end = m.end() + (k.start() if k else len(rest))
    return text[:m.start()] + text[m.start():end].replace(old, new, 1) + text[end:]


def candidate_cases(prereg):
    """candidate() on the fake repository: unmutated it passes; a module changed, an ungoverned path changed, the
    ninth path's named content wrong or the frozen-blob table pending each fail their control; main exits.
    Returns (problems, cases)."""
    src = open(__file__, encoding='utf-8').read()
    repo = fake_repo(prereg, src)
    problems, n = [], 0

    def run(edit=None):
        r = {k: dict(v) for k, v in repo.items()}
        if edit:
            edit(r)
        m = load(src, 'controls_candidate')
        install_fake(m, r)
        with contextlib.redirect_stdout(io.StringIO()):
            res = m.candidate('E')
        return {c for c in CANDIDATE if res.get(c) is not True}, set(res)
    n += 1
    bad, ran = run()
    if bad or ran != set(CANDIDATE):
        problems.append('unmutated: failed %s, ran %s' % (sorted(bad), sorted(ran)))

    def pe(f):
        return lambda r: [r[c].__setitem__(PREREG, f(r[c][PREREG])) for c in ('F', 'E')]
    cases = [('a premise dropped from the headline at X', {'S1', 'C2'},
              lambda r: r['E'].__setitem__(CORE, in_decl(r['E'][CORE], HEADLINE,
                  '(hAttach : UniformAttachPreservation C) (hDiscard : AncillaDiscardPreservation C)',
                  '(hAttach : UniformAttachPreservation C)'))),
             ('a path outside the governed set changed', {'G'},
              lambda r: r['E'].__setitem__('papers/GR.md', 'synthetic\n')),
             ("the ninth path's named sha256 wrong", {'C2'},
              pe(lambda t: re.sub(r'^\| sha256 \|[^\n]*$', '| sha256 | `%s` |' % ('0' * 64), t, count=1, flags=re.M))),
             ('a frozen blob pending', {'C2'},
              pe(lambda t: re.sub(r'^(\| `%s` \| )[^|\n]*\|' % re.escape(PROBE), lambda m: m.group(1) + 'pending |',
                                  t, count=1, flags=re.M))),
             ('the root import moved', {'I'}, lambda r: r['E'].__setitem__(ROOT, r['E'][ROOT] + '\n')),
             ('a run named in another file', {'A'},
              lambda r: r['E'].__setitem__('verification/x.md', 'run %s\n' % sorted(
                  e['run_id'] for e in json.loads(r['E'][ARCHIVE + 'manifest.json'])['entries'])[0]))]
    for name, want, edit in cases:
        n += 1
        bad, ran = run(edit)
        if not want <= bad or ran != set(CANDIDATE):
            problems.append('%s: failed %s, expected at least %s' % (name, sorted(bad), sorted(want)))
    for argv, want in ((['candidate', 'E'], 0), (['candidate'], 2), (['candidate', 'E', 'x'], 2)):
        n += 1
        m = load(src, 'controls_candidate_main')
        install_fake(m, repo)
        with contextlib.redirect_stdout(io.StringIO()):
            got = m.main(argv)
        if got != want:
            problems.append('main %s: exit %s, expected %s' % (' '.join(argv), got, want))
    return problems, n


def axioms_cases():
    """The bridge job's fail-closed step through axioms_gate() and main(): the clean report passes, also in the
    no-axiom form; a missing, repeated, unexpected or dirty report, a bad log token, an empty log, an unset
    namespace and an unreadable log each fail; main exits 0, 1 or 2. Returns (problems, cases)."""
    problems, n = [], 0
    names = CORE_PRINTS + INST_PRINTS
    clean = fix_log(FIX_NS, names)
    ok = lambda log, ns=FIX_NS: all(x[1] for x in axioms_gate(log, ns))
    good = [('clean', clean),
            ('one report without axioms', clean.replace(
                "'%s.%s' depends on axioms: [propext, Classical.choice, Quot.sound]" % (FIX_NS, names[0]),
                "'%s.%s' does not depend on any axioms" % (FIX_NS, names[0]))),
            ('a report Lean wrapped, in a timestamped job log', ''.join(
                '2026-10-16T05:46:35.6502678Z ' + l + '\n' for l in fix_log(FIX_NS, names[1:]).splitlines()) +
             "2026-10-16T05:46:35.6504636Z '%s.%s' depends on axioms: [propext,\n"
             "2026-10-16T05:46:35.6504891Z  Classical.choice,\n2026-10-16T05:46:35.6505011Z  Quot.sound]\n"
             % (FIX_NS, names[0]))]
    bad = [('a report missing', fix_log(FIX_NS, names[1:])),
           ('a report repeated', clean + fix_log(FIX_NS, names[:1])),
           ('an extra axiom', fix_log(FIX_NS, names[1:]) + fix_log(FIX_NS, names[:1], 'propext, sorryAx')),
           ('an unlisted axiom', fix_log(FIX_NS, names[1:]) + fix_log(FIX_NS, names[:1], 'propext, oops')),
           ('another name of the namespace reported', clean + fix_log(FIX_NS, ['finite_sum_mem'])),
           ('a bad token elsewhere in the log', clean + 'warning: uses Lean.ofReduceBool\n'),
           ('the reports of another namespace', fix_log('OIBridge.Other', names)),
           ('an empty log', ''),
           ('a wrapped report with a bad axiom on its continuation line', fix_log(FIX_NS, names[1:]) +
            "2026-10-16T05:46:35.6504636Z '%s.%s' depends on axioms: [propext,\n"
            "2026-10-16T05:46:35.6504891Z  Classical.choice,\n2026-10-16T05:46:35.6505011Z  oops]\n"
            % (FIX_NS, names[0]))]
    for label, log in good:
        n += 1
        if not ok(log) or set(axioms_from(log, FIX_NS)) != set(names) or not all(
                v <= ALLOWED_AXIOMS for v in axioms_from(log, FIX_NS).values()):
            problems.append('%s: rejected, or the verdict\'s reader disagrees' % label)
    for label, log in bad:
        n += 1
        if ok(log):
            problems.append('%s: accepted' % label)
    n += 1
    if ok(clean, None):
        problems.append('the namespace unset: accepted')
    src = open(__file__, encoding='utf-8').read()
    with tempfile.TemporaryDirectory() as tmp:
        for label, text, want in (('clean', clean, 0), ('dirty', bad[0][1], 1), ('absent', None, 1)):
            n += 1
            fp = os.path.join(tmp, label + '.log')
            if text is not None:
                with open(fp, 'w', encoding='utf-8') as fh:
                    fh.write(text)
            m = load(src, 'controls_axioms')
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    got = m.main(['axioms', fp])
            except Exception as e:  # a failure must be an exit status, not an exception
                got = '%s: %s' % (type(e).__name__, e)
            if got != want:
                problems.append('main axioms %s: exit %s, expected %s' % (label, got, want))
            # the gate's own output lands in the step block that verdict reads: it must keep the Lean cells
            # positive and carry no BAD_LOG token
            if label == 'clean':
                served = fix_bridge(step=clean.replace('info: x.lean:1:0: ', ''), gate=buf.getvalue())
                if any(b in buf.getvalue() for b in BAD_LOG) or lean_cells(served, FIX_E_SHA, FIX_NS)[:2] != (True, True):
                    problems.append('the gate\'s own output trips the verdict\'s step rule: %s'
                                    % lean_cells(served, FIX_E_SHA, FIX_NS)[2])
        for argv in (['axioms'], ['axioms', 'a', 'b']):
            n += 1
            m = load(src, 'controls_axioms_usage')
            with contextlib.redirect_stdout(io.StringIO()):
                got = m.main(argv)
            if got != 2:
                problems.append('main %s: exit %s, expected 2' % (' '.join(argv), got))
    return problems, n


def historical_archive(prereg):
    """Control A on this preregistration against the archive at D: the pending citations, the run heads and the
    files naming each run are D's, so no later change to the working tree or to main can alter them."""
    return archive_citations(lambda q: prereg if q == PREREG else show(D, q), lambda run: names_run(D, run))[0]


def self_test():
    global GIT_CWD
    here = os.path.dirname(os.path.abspath(__file__))
    GIT_CWD = here
    prereg = open(os.path.join(here, 'preregistration.md'), encoding='utf-8').read()
    report('self: D agrees with the preregistration', ('D: `%s`' % D) in prereg)
    report('self: the round declaration parses', round_block(prereg) == ROUND_BLOCK)
    report('self: the governed-path block equals the frozen nine entries', governed(prereg) == GOVERNED)
    fb = frozen_blobs(prereg)
    report('self: the frozen-blob table names the five execution files', fb is not None and set(fb) == FROZEN_PATHS,
           '%s rows, %d pending' % (len(fb or {}), sum(v is None for v in (fb or {}).values())))
    rows = retention(prereg)
    report('self: the retention table parses into the three frozen rows', rows is not None and set(rows) == EVIDENCE_ROWS,
           '%d rows, %d pending' % (len(rows or {}), sum(p is None or h is None for p, h in (rows or {}).values())))
    report('self: the drafting decision\'s citation of 65b85147 and link to #831 are present',
           all(c in prereg for c in SUPERSEDED_CITE))
    report("self: the preregistration's S2 table equals LANDED", landed_table(prereg) == LANDED)
    # the historical fixture: every cited object is read at D, never from the working tree
    atd = has_commit(D)
    report('self: D is in this repository\'s history, where the historical fixture is read', atd,
           '' if atd else 'D %s absent (a shallow or partial checkout fails closed)' % D[:12])
    live = []
    for path, line, name in LANDED:
        lines = (show(D, path) if atd else None) or ''
        l = (lines.splitlines() + [''] * line)[line - 1]
        if not re.match(r'(noncomputable )?(def|abbrev|theorem|structure|inductive) %s\b' % re.escape(name), l):
            live.append('%s:%d' % (path, line))
    report('self: every landed object resolves on its pinned line at D (%d)' % len(LANDED), atd and not live,
           ', '.join(live))
    sp = spans_problems(lambda q: show(D, q) if atd else None)
    report('self: every cited span has its pinned digest at D (%d)' % len(CITED_SPANS), atd and not sp, ', '.join(sp))
    report('self: the pinned-line table equals CITED_SPANS and the cited run lines\' digests',
           pinned_lines_table(prereg) == pinned_lines_expected(), str(pinned_lines_table(prereg)))
    cp = citation_problems(prereg)
    report('self: every line citation in the preregistration\'s prose is a pinned landed object or span',
           not cp, '; '.join(cp))
    live = historical_archive(prereg) if atd else ['D absent']
    report('self: control A holds on this file against the archive at D, each cited line with its pinned text',
           not live, '; '.join(live))
    np_ = ninth_problems(prereg, PROBE_SPEC)
    report('self: the ninth governed path\'s named content agrees with the frozen-blob pin and PROBE_SPEC',
           not np_, '; '.join(np_))
    report('self: every surface name, print and token is named in the preregistration',
           all(('`%s`' % n) in prereg for n in CORE_NAMES + INST_NAMES + CORE_PRINTS + INST_PRINTS + POSITIVE
               + [READ, NOT_READ] + [c[2] for c in CELLS] + list(PENDING) + sorted(EVIDENCE_ROWS)))
    unset = [p for p in PENDING if globals()[p] is None]
    report('self: every PENDING parameter is set, or a frozen blob is still pending here',
           not unset or any(v is None for v in (fb or {}).values()), 'unset: ' + ', '.join(unset) if unset else '')
    report('self: the probe spec names the eight frozen mutations and the mutation-rule code',
           len((PROBE_SPEC or {}).get('mutations') or []) == 8
           and 'MUTATION-RULE' in ((PROBE_SPEC or {}).get('probe') or {}).get('codes', []))
    core, inst = FIX_CORE.replace('{NS}', FIX_NS), FIX_INST.replace('{NS}', FIX_NS)
    surf = (render_block(core), render_block(inst))
    report('self: S1 accepts the fixture against its frozen blocks', s1(core, inst, surf, FIX_NS) == [])
    report('self: S1 fails closed with the surface or the namespace pending',
           bool(s1(core, inst, None, FIX_NS)) and bool(s1(core, inst, surf, None)))
    report('self: S3 accepts the fixture', s3(core, inst) == [])
    s1m = [
        ('hDiscard dropped from the headline', 'c', lambda t: in_decl(t, HEADLINE,
            '(hAttach : UniformAttachPreservation C) (hDiscard : AncillaDiscardPreservation C)',
            '(hAttach : UniformAttachPreservation C)')),
        ('0 < m dropped from UniformAttachPreservation', 'c', lambda t: in_decl(t, 'UniformAttachPreservation',
            '(m : ℕ), 0 < m →', '(m : ℕ),')),
        ('the transport conclusion moved to the source carrier', 'c', lambda t: in_decl(
            t, 'instAvail_transport_preserves', "PreservesCarrier C S' (transport", 'PreservesCarrier C S (transport')),
        ('the headline restricted to fullClass', 'c', lambda t: in_decl(t, HEADLINE, '{𝓘 : ImplementationClass} (hPrim',
                                                                        '(hPrim')),
        ('quantum_instAvail restricted to fullClass', 'i', lambda t: in_decl(t, 'quantum_instAvail',
            'InstAvail 𝓘 S O F', 'InstAvail fullClass S O F')),
        ('an extra print', 'c', lambda t: t.replace('#print axioms instAvail_preserves\n',
                                                    '#print axioms instAvail_preserves\n#print axioms finite_sum_mem\n', 1)),
        ('a second import', 'c', lambda t: t.replace('import OIBridge.ImplementationLocality\n',
                                                     'import OIBridge.ImplementationLocality\nimport OIBridge.X\n', 1)),
        ('an example dropped', 'i', lambda t: t.replace('example : LabelInvariant classicalClass := '
                                                        'substratumClass_labelInvariant\n', '', 1)),
        ('a sorry in a proof', 'c', lambda t: t.replace('  fixture_proof\n', '  sorry\n', 1)),
        ('an open line changed', 'i', lambda t: t.replace('open scoped ComplexOrder\n', '', 1)),
        ('the classical cone redefined', 'i', lambda t: t.replace('{X | X.PosSemidef ∧ ∃ d, X = Matrix.diagonal d}',
                                                                  '{X | ∃ d, X = Matrix.diagonal d}', 1)),
    ]
    for name, which, f in s1m:
        mc, mi = (f(core), inst) if which == 'c' else (core, f(inst))
        report('self: S1 rejects: ' + name, (mc, mi) != (core, inst) and bool(s1(mc, mi, surf, FIX_NS)))
    s3m = [
        ('PSD used in a core proof', 'c', lambda t: t.replace('  fixture_proof\n',
                                                              '  have _ := Matrix.PosSemidef.zero\n', 1)),
        ('the discard arm removed', 'c', lambda t: t.replace(
            '  | discard hm _ ih => exact hDiscard _ _ hm _ (ih a _ (hAttach _ _ hm X hX))\n', '', 1)),
        ('the coarse and bind arms swapped', 'c', lambda t: t.replace('  | coarse f _ ih => ', '  | coarseX ', 1)
         .replace('  | bind _ _ ihF ihG => ', '  | coarse f _ ih => ', 1).replace('  | coarseX ', '  | bind _ _ ihF ihG => ', 1)),
        ('the transport corollary not built from instAvail_transport', 'c', lambda t: t.replace(
            '(instAvail_transport hl h S\' e)', '(fixture_transport hl h S\' e)', 1)),
        ('the spectator corollary not built from the headline', 'c', lambda t: t.replace(
            '  instAvail_preserves C hC hPrim hAttach hDiscard (instAvail_spectator',
            '  fixture_headline C hC hPrim hAttach hDiscard (instAvail_spectator', 1)),
        ('a research namespace left in the instances', 'i', lambda t: t.replace(
            'open scoped ComplexOrder\n', 'open scoped ComplexOrder\nopen OIBridge.PreservationInductionDesign\n', 1)),
        ('a third AdditiveClosure field', 'c', lambda t: t.replace(
            '    X ∈ C S → Y ∈ C S → X + Y ∈ C S\n',
            '    X ∈ C S → Y ∈ C S → X + Y ∈ C S\n  smul_mem : ∀ (S : Type), True\n', 1)),
    ]
    for name, which, f in s3m:
        mc, mi = (f(core), inst) if which == 'c' else (core, f(inst))
        report('self: S3 rejects: ' + name, (mc, mi) != (core, inst) and bool(s3(mc, mi)))
    reach = inst.replace('abbrev classicalCone : CarrierConeFamily := fun _ _ _ =>',
                         'abbrev classicalCone : CarrierConeFamily := fun S _ _ => {X | InstAvail X} ∪', 1)
    report('self: S3 rejects a preparation family defined through availability', reach != inst and bool(s3(core, reach)))
    run, H = '987654321012', '0123456789abcdef0123456789abcdef01234567'
    link = '[%s](https://github.com/o/r/actions/runs/%s),' % (run, run)
    report('self: the run-citation rule: a link and its URL free, an identifier embedded, a longer number not the run; '
           'the full head beside, another head or no head refused, a 64-digit digest opaque',
           run_mentions(link, run) == 'free' and run_mentions('`core-build-%s`' % run, run) == 'embedded'
           and run_mentions('x1%s' % run, run) is None and run_mentions('%s5' % run, run) is None
           and head_beside(['at `%s`, run' % H, link, 'job 115478781754'], 2, H) == []
           and bool(head_beside(['at `%s`, run' % H, link, 'see `abcdef1`'], 2, H))
           and bool(head_beside(['at `%s`, run' % H[:12], link, ''], 2, H))
           and head_beside(['at `%s`' % H, link, '`%s`' % ('e' * 64)], 2, H) == [])
    para = ('The kernel `A` (`ImplementationLocality.lean:268`), `B` (:359) and `uniformAttach` is\n'
            '`OperationalAssembly.lean:492`, `ptraceAnc` :453; see (ROADMAP :1125\u20131129 at D).')
    c_, s_, p_ = prose_citations(para + '\n\nA bare :12 here.\n\n```lean\nX.lean:1\n```\n')
    report('self: the prose-citation reader takes a file:line, a bare :N against the paragraph\'s last file and a '
           'ROADMAP span, flags a bare :N with no file, and skips fenced code',
           c_ == [('ImplementationLocality.lean', 268), ('ImplementationLocality.lean', 359),
                  ('OperationalAssembly.lean', 492), ('OperationalAssembly.lean', 453)]
           and s_ == [(ROADMAP, 1125, 1129)] and len(p_) == 1
           and bool(citation_problems(prereg.replace('(:359)', '(:358)', 1))) and span_digest('a\nb\n', 1, 3) is None)
    report('self: S4 flags each excluded phrase and passes the fixture headers',
           all(s4([('x', 'Here ' + p + '.')]) for p in PHRASES) and not s4([('h', header_of(core)),
                                                                              ('h', header_of(inst))]))
    wbase = 'jobs:\n  probes_a:\n    runs-on: fixture\n  aggregate:\n    needs: [probes_a]\n'
    report('self: W applies the splices once each, and fails closed with none, an absent base or a lost anchor',
           workflow(wbase, FIX_SPLICES) is not None and workflow(wbase, None) is None and workflow(None, FIX_SPLICES)
           is None and workflow(wbase.replace('needs: [probes_a]', 'needs: []'), FIX_SPLICES) is None)
    gate_new = SPLICES[-1][1] if SPLICES else ''
    report('self: the frozen bridge-job step fails closed: pipefail, its marker naming the checked-out SHA, both '
           'modules teed to one log, then this file\'s axiom gate on that log',
           'set -euo pipefail\n' in gate_new and gate_new.count('2>&1 | tee') == 2
           and 'round-preserve-induct-1/controls.py axioms "$log"\n' in gate_new
           and 'head=$(git rev-parse HEAD)\n' in gate_new
           and 'echo "preserve_induct1 axioms: step at ${head}"\n' in gate_new
           and gate_new.index('set -euo') < gate_new.index('head=$(git rev-parse') < gate_new.index('step at ${head}')
           < gate_new.index('lake env lean') < gate_new.index('controls.py axioms'))
    rbase = 'import OIBridge.A\nimport OIBridge.B\n\nnamespace OIBridge\n'
    report('self: I inserts both lines after the last import, and refuses a base already carrying one',
           root_expected(rbase) == 'import OIBridge.A\nimport OIBridge.B\n' + '\n'.join(ROOT_LINES) +
           '\n\nnamespace OIBridge\n' and root_expected(rbase + ROOT_LINES[0] + '\n') is None
           and root_expected(None) is None)
    jb = json.dumps({'families': [{'name': 'x'}]})
    jh = json.dumps({'families': [{'name': 'x'}] + FIX_FAMILIES})
    report('self: J accepts the families and rejects a changed status, none, or an absent base',
           registry_ok(jb, jh, FIX_FAMILIES) and not registry_ok(jb, jh.replace('kernel-only', 'current'), FIX_FAMILIES)
           and not registry_ok(jb, jb, []) and not registry_ok(None, jh, FIX_FAMILIES))
    bad = g(['M\tpapers/GR.md', 'M\t' + LEGACY, 'M\tverification/ROADMAP.md', 'A\t' + CORE, 'A\t' + RDIR + 'x',
             'M\t' + CORE, 'D\t' + WORKFLOW, 'M\t' + LP + 'ImplementationLocality.lean'], GOVERNED)
    gwant = ['M\tpapers/GR.md', 'M\t' + LEGACY, 'M\tverification/ROADMAP.md', 'M\t' + CORE, 'D\t' + WORKFLOW,
             'M\t' + LP + 'ImplementationLocality.lean']
    report('self: G authorizes by status letter and longest prefix', bad == gwant, '' if bad == gwant else str(bad))
    dig = {l: ('evidence/%s.json' % l, '0' * 64) for l in EVIDENCE_ROWS}
    files = record_files(dig)
    names = [RDIR + n for n in ['preregistration.md', 'controls.py', 'result.md', FRUN + 'x'] + sorted(files)]
    gapd = dict(dig, **{h: (NONE, GAP) for h in HISTORICAL})
    arch = dict(dig, **{h: ('verification/audits/evidence-retention/x/%s.json' % h, '0' * 64) for h in HISTORICAL})
    hist_files = {'evidence/%s.json' % h for h in HISTORICAL}
    report('self: R requires the frozen files, the record-relative digest rows\' files, f-run and (at E) the result '
           'note, and nothing else; a gap row or a file retained on main names no record file',
           len(files) == 3 and record_ok(names, files, True) and not record_ok(names + [RDIR + 'extra.md'], files, True)
           and not record_ok([x for x in names if FRUN not in x], files, True)
           and not record_ok([x for x in names if not x.endswith('result.md')], files, True)
           and record_ok([x for x in names if not x.endswith('result.md')], files, False)
           and record_files(gapd) == record_files(arch) == {'evidence/%s.json' % REQUIRED_PIN}
           and record_ok([x for x in names if x[len(RDIR):] not in hist_files], record_files(gapd), True)
           and not record_ok(names, record_files(gapd), True))
    report('self: the probe rule accepts the frozen shape and fails closed with no spec, a code missing, stderr, a '
           'nonzero exit or a script absent',
           probe_ok(fix_res(), FIX_SPEC) and not probe_ok(fix_res(), None)
           and not probe_ok(fix_res(probe=FIX_OUT['probe'].replace('PASS FIX2', 'PASS FIX')), FIX_SPEC)
           and not probe_ok(fix_res(err=('', 'x')), FIX_SPEC) and not probe_ok(fix_res(rc=(1, 0)), FIX_SPEC)
           and not probe_ok({'probe': fix_res()['probe']}, FIX_SPEC) and not probe_ok(None, FIX_SPEC))
    bump = FIX_OUT['indep'] + ' '
    noind = FIX_OUT['indep'].replace('PASS IND1 (1)\n', '')
    other_manifest = FIX_OUT['indep'].replace(FIX_MANIFEST, 'e' * 64)
    spec_other = dict(FIX_SPEC, indep=dict(FIX_SPEC['indep'], stdout_sha256=_sha(other_manifest)))
    report('self: the probe rule requires the independent check\'s codes, both byte replays, the shared manifest '
           'digest, the SymPy line and every mutation rejected',
           not probe_ok(fix_res(), dict(FIX_SPEC, indep=dict(FIX_SPEC['indep'], codes=[])))
           and not probe_ok(fix_res(indep=bump), FIX_SPEC)
           and not probe_ok(fix_res(), dict(FIX_SPEC, probe=dict(FIX_SPEC['probe'], stdout_sha256=None)))
           and not probe_ok(fix_res(probe=FIX_OUT['probe'].replace('SYMPY 1.14.0', 'SYMPY 1.13.3')),
                            dict(FIX_SPEC, probe=dict(FIX_SPEC['probe'], stdout_sha256=_sha(
                                FIX_OUT['probe'].replace('SYMPY 1.14.0', 'SYMPY 1.13.3')))))
           and not probe_ok(fix_res(), dict(FIX_SPEC, sympy='1.13.3'))
           and not probe_ok(fix_res(indep=noind), dict(FIX_SPEC, indep=dict(FIX_SPEC['indep'],
                                                                              stdout_sha256=_sha(noind))))
           and not probe_ok(fix_res(indep=other_manifest), spec_other)
           and not probe_ok(fix_res(), dict(FIX_SPEC, mutations=['m1: FIX1', 'm2: FIX2'])))
    summary = 'REJECTED m1: FIX1\nmutations: 1 rejected, 0 survived, 0 undecided\n'
    runs = {'an undecided (crashed) run': 'UNDECIDED m1: FIX1 (faithful True, mutated None)\n'
                                          'mutations: 0 rejected, 0 survived, 1 undecided\n',
            'a surviving run': 'SURVIVED m1: FIX1 (faithful True, mutated True)\n'
                               'mutations: 0 rejected, 1 survived, 0 undecided\n',
            'a crash beside the rejected run': 'REJECTED m1: FIX1\nUNDECIDED m2: FIX2 (faithful True, mutated None)\n'
                                               'mutations: 1 rejected, 0 survived, 1 undecided\n',
            'a crash line under a clean summary': 'REJECTED m1: FIX1\nUNDECIDED m2: FIX2 (faithful None, mutated None)\n'
                                                  'mutations: 1 rejected, 0 survived, 0 undecided\n',
            'a rejected line repeated': 'REJECTED m1: FIX1\nREJECTED m1: FIX1\n'
                                        'mutations: 1 rejected, 0 survived, 0 undecided\n',
            'the older two-count summary': 'REJECTED m1: FIX1\nmutations: 1 rejected, 0 accepted\n'}
    caught = []
    for label, text in runs.items():
        out = FIX_OUT['probe'].replace(summary, text)
        if out == FIX_OUT['probe'] or probe_ok(fix_res(probe=out), dict(FIX_SPEC, probe=dict(
                FIX_SPEC['probe'], stdout_sha256=_sha(out)))):
            caught.append(label)
    report('self: a mutation run counts only as rejected: an undecided (crashed) or surviving run, a crash beside a '
           'clean summary and a repeated rejection each fail the probe rule (%d cases)' % len(runs), not caught,
           'accepted: ' + ', '.join(caught))
    loose = [(o, n.replace('sympy==1.14.0', 'sympy')) for o, n in FIX_SPLICES]
    other = [(o, n.replace('sympy==1.14.0', 'sympy>=1.14')) for o, n in FIX_SPLICES]
    report('self: W\'s pin rule requires exactly sympy==1.14.0 when the spec names SymPy, and fails with the spec pending',
           pin_ok(FIX_SPLICES, FIX_SPEC) and not pin_ok(loose, FIX_SPEC) and not pin_ok(other, FIX_SPEC)
           and not pin_ok(FIX_SPLICES, None) and not pin_ok(FIX_SPLICES, dict(FIX_SPEC, sympy=None))
           and pin_ok([FIX_SPLICES[0]], dict(FIX_SPEC, sympy=None)))
    h0 = sorted(HISTORICAL)[0]
    gtab = prereg
    for h in HISTORICAL:
        gtab = set_row(gtab, h, 'none', 'gap: log expired')
    gp_ = retention(gtab)
    atab = set_row(prereg, h0, '`verification/audits/evidence-retention/x/a.json`', '`%s`' % ('0' * 64))
    bad_rows = [set_row(prereg, h0, 'none', 'gap:'), set_row(prereg, h0, '`evidence/a.json`', 'gap: lost'),
                set_row(prereg, h0, 'none', '`%s`' % ('0' * 64)), set_row(prereg, h0, 'pending', '`%s`' % ('0' * 64)),
                set_row(prereg, h0, '`%sx.json`' % RDIR, '`%s`' % ('0' * 64)),
                set_row(prereg, h0, '`papers/x.md`', '`%s`' % ('0' * 64))]
    report('self: the retention table takes an expected-result digest, a file retained on main or a recorded gap on '
           'a historical row, and refuses the inconsistent forms',
           gp_ is not None and set(gp_) == EVIDENCE_ROWS and all(gp_[h] == (NONE, GAP) for h in HISTORICAL)
           and (retention(atab) or {}).get(h0) == ('verification/audits/evidence-retention/x/a.json', '0' * 64)
           and all(retention(t) is None for t in bad_rows))
    report('self: passed() rejects an empty, non-bool or partial map and an unknown stage',
           not passed({}) and not passed({c: 1 for c in REQUIRED['E']}) and passed({c: True for c in REQUIRED['E']})
           and passed({c: True for c in REQUIRED['S1']}, 'S1') and not passed({c: True for c in REQUIRED['S1']})
           and not passed({c: True for c in REQUIRED['E']}, 'x'))
    problems, n = axioms_cases()
    report('self: the bridge job\'s axiom gate passes the ten clean reports and fails closed on a missing, repeated, '
           'dirty or unexpected report, a bad token, an empty log or an unset namespace; main exits (%d cases)' % n,
           not problems, '; '.join(problems))
    problems, n = verdict_regression()
    report('self: verdict() prints no positive token when any required control fails, is unreported or non-bool; '
           'each cell reads only its own reports; the Lean cells read only the final step\'s block, bound to E, with '
           'one OK line after its last report and no FAILED line (%d cases)' % n, not problems, '; '.join(problems))
    problems, n = e2e_cases(prereg)
    report('self: the real check() through verdict() fails, names the control, prints no positive token and never '
           'runs the probe with any record call removed or any control\'s inputs absent; unmutated it passes; main '
           'exits and refuses unknown stages and arguments (%d cases)' % n, not problems, '; '.join(problems))
    problems, n = candidate_cases(prereg)
    report('self: candidate() on the fixture passes unmutated and fails the named control on a candidate tree with a '
           'premise dropped from a module, an ungoverned path, a wrong ninth-path row, a pending pin, a moved import or a run named '
           'elsewhere; main exits (%d cases)' % n, not problems, '; '.join(problems))
    selfs = len([r for r in RAN if r.startswith('self:')]) + 1
    report('self: %d self-checks ran, as frozen (%d)' % (selfs, SELF_CHECKS), selfs == SELF_CHECKS)
    return not FAIL


def main(argv):
    def opts(rest, allowed):
        out, i = {}, 0
        while i < len(rest):
            if rest[i] not in allowed or i + 1 >= len(rest) or rest[i + 1].startswith('--'):
                return None
            out[rest[i]] = rest[i + 1]; i += 2
        return out
    if argv == ['--self-test']:
        ok = self_test()
    elif argv[:1] == ['check'] and len(argv) >= 4 and argv[2] == '--freeze':
        o = opts(argv[4:], {'--stage'})
        if o is None or o.get('--stage', 'E') not in STAGES:
            print('check: unknown argument or stage %r (expected --stage one of %s)' % (argv[4:], ', '.join(STAGES)))
            return 2
        stage = o.get('--stage', 'E')
        ok = passed(check(argv[1], argv[3], stage), stage)
    elif argv[:1] == ['verdict'] and len(argv) >= 4 and argv[2] == '--freeze':
        o = opts(argv[4:], {'--axioms'})
        if o is None:
            print('verdict: unknown argument %r' % (argv[4:],))
            return 2
        ok = verdict(argv[1], argv[3], o.get('--axioms'))
    elif argv[:1] == ['candidate'] and len(argv) == 2:
        res = candidate(argv[1])
        ok = all(res.get(c) is True for c in CANDIDATE)
    elif argv[:1] == ['axioms'] and len(argv) == 2:
        try:
            log = open(argv[1], encoding='utf-8', errors='replace').read()
        except OSError as e:
            log = None
            report('axioms: the log is readable', False, str(e))
        for name, good, detail in (axioms_gate(log, NS) if log is not None else []):
            report('axioms: ' + name, good, detail)
        ok = log is not None and not FAIL
        print('preserve_induct1 axioms: %s' % ('OK -- %d reports' % len(CORE_PRINTS + INST_PRINTS) if ok else 'FAILED'))
    else:
        print(__doc__)
        return 2
    print('controls: %s (%d failure(s))' % ('OK' if ok else 'FAILED', len(FAIL)))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
