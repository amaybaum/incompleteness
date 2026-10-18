#!/usr/bin/env python3
"""controls.py -- round KN-DESC-1's own contracts, frozen with the preregistration beside it.

Imports nothing from the repository and changes nothing in it. Reads D and the commits under check through git, run
from the repository root, and embeds every frozen text it compares against: the module's surface, the landed
declarations it resolves to at D, the workflow edit, the import line, the census family, the cell rules, the earned
reading, the non-inference rule and the phrase list.

  controls.py check <commit> [--freeze F] [--axioms R]
        the tree at <commit> against D: P, W, I, C, S1-S4, R, G, and, at a commit carrying the result note, V. With
        --freeze, also the control plane at F (as check-freeze) and the linear chain F -> C1 -> S1 -> ... -> <commit>,
        with P, W, I and C measured at the stage-1 commit as well
  controls.py check-freeze <F>
        the control plane: D..F single-parent and control-plane-only, the two declaration blocks, every frozen object id
        named, the controls blob named, and the C0 commit named and passing check-c0
  controls.py check-c0 <commit>
        a candidate predicted execution tree less the result note: a single-parent child of D carrying exactly the
        record's two files and the five frozen execution blobs
  controls.py verdict <commit> [--axioms R]
        one token per cell, computed from the measurements at <commit>: the module's statements, the landed
        declarations at D, the probe run, and the axiom report R
  controls.py note-scaffold <commit> [--axioms R]
        a result-note scaffold carrying the computed tokens, the frozen texts the rules require and the probe's last
        two lines; a scaffold, not the note
  controls.py --self-test
        positive controls must pass; every mutation must fail with its named code, or read not-established in exactly
        the cells it touches

R is an expected-result file (schema `oi-evidence-result`) extracted from the Mathlib bridge job of an exact-head run.
Its run's commit must carry the same `verification/lean-mathlib` tree as the commit under verdict. Without R, Q-DESC and
Q-IFF read not-established: no kernel build has been measured.

Codes: P probe, W workflow, I import, C census, S1 surface, S2 resolution, S3 directional witnesses, S4 phrases,
V verdicts, R record, G governed paths, F freeze, T chain, L landed citations, X axiom report, K C0 shape, M mutation,
Z self-test fixture. Exit 1 on any failure.
"""
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile

# ------------------------------------------------------------------------------------------------------- objects
D = '5bfdaba61b535e2fff83d8ba68e73a1b9dbc5dc5'
ROUND = 'KN-DESC-1'
RDIR = 'verification/programmes/oi-qm/reconstruction/round-kn-desc-1-qubit-power-descent/'
PREREG = RDIR + 'preregistration.md'
CONTROLS = RDIR + 'controls.py'
RESULT = RDIR + 'result.md'
AMEND = RDIR + 'amendments/'
RECEIPT = 'verification/receipts/KN-DESC-1.json'
LEAN = 'verification/lean-mathlib/OIBridge/'
LEAN_TREE = 'verification/lean-mathlib'
MOD = LEAN + 'KnDescent.lean'
MOD_KEY = 'OIBridge/KnDescent.lean'
PROBE = 'verification/lean/kn_desc1_probe.py'
IMPORTS = 'verification/lean-mathlib/OIBridge.lean'
CENSUS = 'verification/lean-manuscript-census.json'
WORKFLOW = '.github/workflows/verify.yml'

BLOBS = {  # the frozen execution blobs
    MOD: 'd2c3ebbe47341e3ebc275427c34f05ad3a64db7d',
    PROBE: 'a8f1ef39b11179fbbf0aacf836d7dc8c1558f8be',
    IMPORTS: '9ffd8aa5d0a3c8521623ca946225da28e031dc9c',
    CENSUS: '444fedcd3d07d2a5eb7ef287c2d5c9304d5f428d',
    WORKFLOW: 'f40440987d16f8c63373e75f4e3ebf8fff3ed96c',
}
D_BLOBS = {  # the files the execution modifies, at D
    IMPORTS: '9c84d95ed3ff2fedab4d5682547875e27beabc94',
    CENSUS: 'c8e0e1844c0b27b83b587bb7fc9e3bf63f1393a1',
    WORKFLOW: '159936eb42560fd4f22f14cd81fce2ae35382ffe',
}
GOVERNED = {MOD: 'A', PROBE: 'A', IMPORTS: 'M', CENSUS: 'M', WORKFLOW: 'M'}
FROZEN_IDS = sorted(set(BLOBS.values()) | {D_BLOBS[WORKFLOW], D})  # every id the preregistration must name at F

V3_ROUND = ('round KN-DESC-1\n'
            'kind non-sealing\n'
            'record-directory verification/programmes/oi-qm/reconstruction/round-kn-desc-1-qubit-power-descent/')
V3_PATHS = ('record AM verification/programmes/oi-qm/reconstruction/round-kn-desc-1-qubit-power-descent/\n'
            'record AM verification/receipts/KN-DESC-1.json\n'
            'execution A verification/lean-mathlib/OIBridge/KnDescent.lean\n'
            'execution A verification/lean/kn_desc1_probe.py\n'
            'execution M verification/lean-mathlib/OIBridge.lean\n'
            'execution M verification/lean-manuscript-census.json\n'
            'execution M .github/workflows/verify.yml')
CONTROLS_NAMED = re.compile(r'`controls\.py`, Git blob `([0-9a-f]{40})`')
C0_NAMED = re.compile(r'`C0` commit `([0-9a-f]{40})`')

# ------------------------------------------------------------------------------------------- the module surface
PREAMBLE = (
    '/-\n'
    '  OIBridge/KnDescent.lean — drivability descends from qubit-power carriers inside the K3\n'
    '  architecture (KN-DESC-1).\n'
    '\n'
    '  (A) Compression. In an implementation class with `Architecture`, `ContextStable` and\n'
    '  `LabelInvariant`, an admissible operator on `T` compresses to an admissible operator on `S` along\n'
    '  any injection `S ↪ T` (`compress_mem`): adjoin `S` as a spectator (`ContextStable`), relabel\n'
    '  `S × T` onto `S × Fin |T|` so that `(s₀, ι s)` goes to `(s, k)` (`LabelInvariant`), and take the\n'
    '  `(k, k)` block (`Architecture.block`).\n'
    '\n'
    '  (B) The elementary generators compress to the elementary generators along an injection\n'
    '  (`transition_submatrix`, `flow_transition_submatrix`, `permMatrix_swap_submatrix`,\n'
    '  `phaseGate_submatrix`).\n'
    '\n'
    '  (C) Drivability at one carrier descends to every smaller nonempty carrier\n'
    '  (`drivesElementaryAt_of_embedding`); drivability at the carriers `Fin (2 ^ k)` gives\n'
    '  `DrivesElementary` (`drivesElementary_of_pow`); and `QuantumArchitecture` holds exactly when its\n'
    '  four closure clauses hold with drivability at the qubit-power carriers\n'
    '  (`quantumArchitecture_iff_pow`: the forward direction through `drivesElementaryAt_of_drives`, the\n'
    '  converse through `drivesElementary_of_pow`).\n'
    '\n'
    '  The statements live in the carrier-general matrix framework of `ImplementationClass`;\n'
    '  `Architecture`, the spectator closure `ContextStable`, `LabelInvariant` and drivability enter as\n'
    '  premises. Nothing here sources drivability, a closure clause, or a dictionary from a\n'
    '  field-neutral composite to the carriers `Fin (2 ^ k)`.\n'
    '-/\n'
    'import OIBridge.SubstratumSource\n'
    'import OIBridge.LiftAudit\n'
    '\n'
    'namespace OIBridge\n'
    'namespace KnDescent\n'
    '\n'
    'open InterventionLocality MonoidalCompletion AncillaClosure CoherentLift LieRankSource\n'
    'open MicroReversibility SubstratumSource\n'
    '\n'
    'open scoped Matrix.Norms.L2Operator\n'
    '\n'
    'noncomputable section\n')
HEADER_END = PREAMBLE.index('-/\n') + 3
DECLS = [('def', 'DrivesElementaryAt')] + [('theorem', n) for n in (
    'drivesElementaryAt_of_drives', 'compress_mem', 'transition_submatrix', 'flow_transition_self',
    'flow_transition_submatrix', 'permMatrix_swap_submatrix', 'phaseGate_submatrix', 'drivesElementaryAt_of_embedding',
    'le_two_pow', 'drivesElementary_of_pow', 'quantumArchitecture_iff_pow', 'drivesElementaryAt_fullClass')]
THEOREMS = [n for k, n in DECLS if k == 'theorem']
STATEMENTS = {  # definitions whole; theorems up to the first ` :=`
    'DrivesElementaryAt':
        'def DrivesElementaryAt (𝓘 : ImplementationClass) (T : Type) [Fintype T] [DecidableEq T] : Prop :=\n'
        '  (∀ (a b : T) (t : ℝ), 𝓘 T (ReachabilitySeam.flow (transition a b) t))\n'
        '    ∧ (∀ a b : T, 𝓘 T (permMatrix (Equiv.swap a b)))\n'
        '    ∧ ∀ a : T, 𝓘 T (phaseGate a)',
    'drivesElementaryAt_of_drives':
        'theorem drivesElementaryAt_of_drives {𝓘 : ImplementationClass} (h : DrivesElementary 𝓘)\n'
        '    (T : Type) [Fintype T] [DecidableEq T] : DrivesElementaryAt 𝓘 T',
    'compress_mem':
        'theorem compress_mem {𝓘 : ImplementationClass} (arch : Architecture 𝓘) (hC : ContextStable 𝓘)\n'
        '    (hL : LabelInvariant 𝓘) {S T : Type} [Fintype S] [DecidableEq S] [Nonempty S] [Fintype T]\n'
        '    [DecidableEq T] (ι : S ↪ T) {K : Matrix T T ℂ} (hK : 𝓘 T K) : 𝓘 S (K.submatrix ι ι)',
    'transition_submatrix':
        'theorem transition_submatrix (ι : S ↪ T) (a b : S) :\n'
        '    (transition (ι a) (ι b)).submatrix ι ι = transition a b',
    'flow_transition_self':
        'theorem flow_transition_self (a : S) (t : ℝ) :\n'
        '    ReachabilitySeam.flow (transition a a) t\n'
        '      = 1 + (Complex.exp ((-(t : ℂ) * Complex.I) * 2) - 1) • Matrix.single a a (1 : ℂ)',
    'flow_transition_submatrix':
        'theorem flow_transition_submatrix (ι : S ↪ T) (a b : S) (t : ℝ) :\n'
        '    (ReachabilitySeam.flow (transition (ι a) (ι b)) t).submatrix ι ι\n'
        '      = ReachabilitySeam.flow (transition a b) t',
    'permMatrix_swap_submatrix':
        'theorem permMatrix_swap_submatrix (ι : S ↪ T) (a b : S) :\n'
        '    (permMatrix (Equiv.swap (ι a) (ι b))).submatrix ι ι = permMatrix (Equiv.swap a b)',
    'phaseGate_submatrix':
        'theorem phaseGate_submatrix (ι : S ↪ T) (a : S) :\n'
        '    (phaseGate (ι a)).submatrix ι ι = phaseGate a',
    'drivesElementaryAt_of_embedding':
        'theorem drivesElementaryAt_of_embedding {𝓘 : ImplementationClass} (arch : Architecture 𝓘)\n'
        '    (hC : ContextStable 𝓘) (hL : LabelInvariant 𝓘) {S T : Type} [Fintype S] [DecidableEq S]\n'
        '    [Nonempty S] [Fintype T] [DecidableEq T] (ι : S ↪ T) (hT : DrivesElementaryAt 𝓘 T) :\n'
        '    DrivesElementaryAt 𝓘 S',
    'le_two_pow': 'theorem le_two_pow (n : ℕ) : n ≤ 2 ^ n',
    'drivesElementary_of_pow':
        'theorem drivesElementary_of_pow {𝓘 : ImplementationClass} (arch : Architecture 𝓘)\n'
        '    (hC : ContextStable 𝓘) (hL : LabelInvariant 𝓘)\n'
        '    (hpow : ∀ k : ℕ, DrivesElementaryAt 𝓘 (Fin (2 ^ k))) : DrivesElementary 𝓘',
    'quantumArchitecture_iff_pow':
        'theorem quantumArchitecture_iff_pow (𝓘 : ImplementationClass) :\n'
        '    QuantumArchitecture 𝓘 ↔ Architecture 𝓘 ∧ ContextStable 𝓘 ∧ LabelInvariant 𝓘\n'
        '      ∧ DaggerStable 𝓘 ∧ ∀ k : ℕ, DrivesElementaryAt 𝓘 (Fin (2 ^ k))',
    'drivesElementaryAt_fullClass':
        'theorem drivesElementaryAt_fullClass (T : Type) [Fintype T] [DecidableEq T] :\n'
        '    DrivesElementaryAt fullClass T',
}
CONTEXT = ['section Generators',
           'variable {S T : Type} [Fintype S] [DecidableEq S] [Fintype T] [DecidableEq T]',
           'end Generators', 'end', 'end KnDescent', 'end OIBridge']
PREFIX = 'OIBridge.KnDescent.'
PRINTS = [PREFIX + n for n in THEOREMS]
IFF, FWD, BWD = 'quantumArchitecture_iff_pow', 'drivesElementaryAt_of_drives', 'drivesElementary_of_pow'
IFF_DECLS = ['DrivesElementaryAt', FWD, BWD, IFF]  # the statements Q-IFF reads
PERMITTED = {'propext', 'Classical.choice', 'Quot.sound'}

# ------------------------------------------------------------------- the landed declarations at D (S2, L)
OPENS = ['InterventionLocality', 'MonoidalCompletion', 'AncillaClosure', 'CoherentLift', 'LieRankSource',
         'MicroReversibility', 'SubstratumSource']
# name as the module writes it -> (file, line at D, fully qualified name, first line of the declaration at D,
#                                  SHA-256 of the declaration's text at D)
LANDED = {
    'ImplementationClass': ('ImplementationLocality.lean', 244, 'OIBridge.InterventionLocality.ImplementationClass',
                            'abbrev ImplementationClass :='),
    'ContextStable': ('ImplementationLocality.lean', 359, 'OIBridge.InterventionLocality.ContextStable',
                      'def ContextStable (𝓘 : ImplementationClass) : Prop :='),
    'LabelInvariant': ('ImplementationLocality.lean', 364, 'OIBridge.InterventionLocality.LabelInvariant',
                       'def LabelInvariant (𝓘 : ImplementationClass) : Prop :='),
    'fullClass': ('ImplementationLocality.lean', 374, 'OIBridge.InterventionLocality.fullClass',
                  'def fullClass : ImplementationClass := fun _ _ _ _ => True'),
    'Architecture': ('ImplementationLocality.lean', 506, 'OIBridge.InterventionLocality.Architecture',
                     'structure Architecture (𝓘 : ImplementationClass) : Prop where'),
    'DaggerStable': ('MicroscopicReversibility.lean', 216, 'OIBridge.MicroReversibility.DaggerStable',
                     'def DaggerStable (𝓘 : ImplementationClass) : Prop :='),
    'DrivesElementary': ('SubstratumSource.lean', 77, 'OIBridge.SubstratumSource.DrivesElementary',
                         'def DrivesElementary (𝓘 : ImplementationClass) : Prop :='),
    'QuantumArchitecture': ('SubstratumSource.lean', 86, 'OIBridge.SubstratumSource.QuantumArchitecture',
                            'structure QuantumArchitecture (𝓘 : ImplementationClass) : Prop where'),
    'ancBlock': ('AncillaClosure.lean', 457, 'OIBridge.AncillaClosure.ancBlock',
                 'def ancBlock {m : ℕ} (K : Matrix (S × Fin m) (S × Fin m) ℂ) (f e : Fin m) : Matrix S S ℂ :='),
    'tensorOf': ('MonoidalCompletion.lean', 193, 'OIBridge.MonoidalCompletion.tensorOf',
                 'def tensorOf (XA : Matrix A A ℂ) (XB : Matrix B B ℂ) : Matrix (A × B) (A × B) ℂ :='),
    'transition': ('LieRankSource.lean', 199, 'OIBridge.LieRankSource.transition',
                   'def transition (a b : S) : Matrix S S ℂ := Matrix.single a b 1 + Matrix.single b a 1'),
    'phaseGate': ('LieRankSource.lean', 209, 'OIBridge.LieRankSource.phaseGate',
                  'def phaseGate (a : S) : Matrix S S ℂ := Matrix.diagonal fun p => if a = p then Complex.I else 1'),
    'permMatrix': ('CoherentLift.lean', 92, 'OIBridge.CoherentLift.permMatrix',
                   'def permMatrix (g : S ≃ S) : Matrix S S ℂ :='),
    'ReachabilitySeam.flow': ('ReachabilitySeam.lean', 95, 'OIBridge.ReachabilitySeam.flow',
                              'noncomputable def flow (H : Matrix S S ℂ) (t : ℝ) : Matrix S S ℂ :='),
    'LiftAudit.pairProj': ('LiftAudit.lean', 252, 'OIBridge.LiftAudit.pairProj',
                           'def pairProj (a b : S) : Matrix S S ℂ := Matrix.single a a 1 + Matrix.single b b 1'),
}
LANDED_SHA = {}  # filled below: the frozen SHA-256 of each landed declaration's text at D
# further citations the preregistration makes at D: (path, line, the line's stripped text starts with)
CITED = [
    (LEAN + 'ImplementationLocality.lean', 514, 'block : ∀ (S : Type) [Fintype S] [DecidableEq S] (m : ℕ)'),
    (LEAN + 'ImplementationLocality.lean', 518, 'theorem fullClass_arch : Architecture fullClass where'),
    (LEAN + 'SubstratumSource.lean', 136, 'theorem genTheory_qm_of_quantumArchitecture'),
    (LEAN + 'LiftAudit.lean', 276, 'theorem flow_transition_closedForm {a b : S} (hab : a ≠ b)'),
    (LEAN + 'LiftAudit.lean', 219, 'theorem exp_smul_idempotent {P : Matrix S S ℂ} (hP : P * P = P)'),
    (LEAN + 'StructuralClosure.lean', 383, 'theorem substratum_residual :'),
    ('verification/ROADMAP.md', 1070, '- **Kₙ — elementary-to-arbitrary-carrier lift. OPEN.**'),
    ('verification/ROADMAP.md', 1081,
     '[`audits/foundations/kn-elementary-carrier-census.md`](audits/foundations/kn-elementary-carrier-census.md).'),
    ('verification/audits/foundations/kn-elementary-carrier-census.md', 1, ''),
]

# ------------------------------------------------------------------------------------------- the workflow edit
SHARD = '''  probes_kndesc1:
    name: Numerical probes / KN-DESC-1 qubit-power descent
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install the exact-algebra dependency
        run: pip install sympy==1.14.0

      - name: KN-DESC-1 compression-descent probe
        working-directory: verification/lean
        run: |
          echo "=== kn_desc1_probe.py ==="
          out=$(python3 -I -B kn_desc1_probe.py)
          printf '%s\\n' "$out"
          test "$(printf '%s\\n' "$out" | tail -n 1)" = "VERDICT COMPRESSION-DESCENT-EXACT"

'''
SHARD_ANCHOR = '\n  probes_oichannel1:\n'
AGG_EDITS = [
    ('probes_kt4prem1, probes_oichannel1', 'probes_kt4prem1, probes_kndesc1, probes_oichannel1'),
    ('          KT4PREM1_RESULT: ${{ needs.probes_kt4prem1.result }}\n',
     '          KT4PREM1_RESULT: ${{ needs.probes_kt4prem1.result }}\n'
     '          KNDESC1_RESULT: ${{ needs.probes_kndesc1.result }}\n'),
    ('          echo "kt4prem1=${KT4PREM1_RESULT}"\n',
     '          echo "kt4prem1=${KT4PREM1_RESULT}"\n          echo "kndesc1=${KNDESC1_RESULT}"\n'),
    ('          test "${KT4PREM1_RESULT}" = success\n',
     '          test "${KT4PREM1_RESULT}" = success\n          test "${KNDESC1_RESULT}" = success\n'),
]
IMPORT_ANCHOR = 'import OIBridge.EqvK2MaxCone\n'
IMPORT_LINE = 'import OIBridge.KnDescent\n'
PREV_FAMILY_MODULES = ['EqvK2Schema', 'EqvK2Converse', 'EqvK2Block', 'EqvK2Generation', 'BridgeDictionary',
                       'BridgeConverge', 'EqvK2MaxCone']
FAMILY = {
    'name': 'inside the K3 interfaces drivability descends from qubit-power carriers: in an implementation class with '
            'Architecture, ContextStable and LabelInvariant every admissible operator compresses along any injection '
            'of carriers, the elementary generators compress to themselves, and drivability at the carriers Fin (2^k) '
            'gives DrivesElementary (round KN-DESC-1, reconstruction)',
    'modules': ['KnDescent'],
    'status': 'kernel-only',
    'manuscript': [],
}

# --------------------------------------------------------------------------------------------- the cells and texts
PROBE_IDS = ['F0', 'G1', 'G2', 'G3', 'B1', 'K1', 'K2']
PROBE_SUMMARY = 'checks: 7, failures: 0'
PROBE_VERDICT = 'VERDICT COMPRESSION-DESCENT-EXACT'
CELLS = [('Q-DESC', 'KN-DESC-DESCENT-PROVED', 'KN-DESC-DESCENT-NOT-ESTABLISHED'),
         ('Q-IFF', 'KN-DESC-IFF-PROVED', 'KN-DESC-IFF-NOT-ESTABLISHED'),
         ('Q-EXACT', 'KN-DESC-INSTANCES-EXACT', 'KN-DESC-INSTANCES-NOT-ESTABLISHED')]
ALL_TOKENS = [t for _, p, n in CELLS for t in (p, n)]
TOKEN_LIKE = re.compile(r'(?<![\w-])KN-DESC-(?!1-)[A-Z]+(?:-[A-Z]+)*(?![\w-])')
EARNED = ('inside the K3 interfaces, an implementation class with Architecture, ContextStable and LabelInvariant that '
          'drives the elementary transitions on every carrier Fin (2^k) drives them on every finite carrier, and '
          'QuantumArchitecture is equivalent to its four closure clauses with drivability at the qubit-power carriers.')
NONINF = ('this round does not show that OI, K2 or any composite supplies drivability on any carrier, a dictionary from '
          'a field-neutral k-token composite to the carriers Fin (2^k), or any of the closure clauses Architecture, '
          'ContextStable, LabelInvariant, DaggerStable. The descent fixes the repertoire at carriers the formalism '
          'already has as types and uses ContextStable with spectators of odd size; it does not produce a three-level '
          'system from qubits. ContextStable is the matrix form of the spectator clause the composite action (b) '
          'needs; the reduction moves the carrier generality of Kn into it and does not discharge it. The '
          'load-bearing status of block and LabelInvariant rests on written arguments and is not part of this round. '
          'The probe is an exact computation, not a Lean kernel proof.')
PHRASES = ['OI supplies', 'K2 supplies', 'drivability is sourced', 'Kn is discharged', 'Kn is closed', 'Kₙ is closed',
           'F1 is established', 'establishes F1', 'the lift is supplied', 'produces a three-level system',
           'kernel proof of', 'design module', 'not for merge']


# ------------------------------------------------------------------------------------------------------- helpers
def norm(s):
    return ' '.join(s.replace('`', '').split()).lower()


def unquote(note):
    return '\n'.join(re.sub(r'^\s*>\s?', '', line) for line in note.split('\n'))


def sha256(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def git_blob_id(text):
    data = text.encode('utf-8')
    return hashlib.sha1(b'blob %d\0' % len(data) + data).hexdigest()


def git(*args, ok=False):
    r = subprocess.run(['git', *args], capture_output=True)
    if r.returncode != 0:
        if ok:
            return None
        raise RuntimeError('git %s: %s' % (' '.join(args), r.stderr.decode('utf-8', 'replace').strip()))
    return r.stdout.decode('utf-8')


def show(commit, path):
    return git('show', '%s:%s' % (commit, path), ok=True)


def blob_of(commit, path):
    r = git('rev-parse', '--verify', '-q', '%s:%s' % (commit, path), ok=True)
    return r.strip() if r else None


def cat_blob(blob_id):
    return git('cat-file', 'blob', blob_id, ok=True)


def rev(commit):
    return git('rev-parse', '--verify', commit + '^{commit}').strip()


def parents(commit):
    return git('rev-list', '--parents', '-n', '1', commit).split()[1:]


def ls(commit, prefix):
    out = git('ls-tree', '-r', '-z', '--name-only', commit, '--', prefix)
    return sorted(p for p in out.split('\0') if p)


def delta(a, b):
    """[(status, path)] of git diff --no-renames --name-status a b, in git's order."""
    out = git('diff', '--no-renames', '--name-status', '-z', a, b)
    f = [x for x in out.split('\0') if x != '']
    return [(f[i], f[i + 1]) for i in range(0, len(f), 2)]


def batch_texts(commit, paths):
    """{path: text} for the given paths at commit, read through one git cat-file process."""
    if not paths:
        return {}
    req = ''.join('%s:%s\n' % (commit, p) for p in paths).encode('utf-8')
    r = subprocess.run(['git', 'cat-file', '--batch'], input=req, capture_output=True)
    data, out, i = r.stdout, {}, 0
    for p in paths:
        j = data.index(b'\n', i)
        head = data[i:j].decode('utf-8').split()
        i = j + 1
        if len(head) == 2 and head[1] == 'missing':
            continue
        size = int(head[2])
        out[p] = data[i:i + size].decode('utf-8')
        i += size + 1
    return out


FAILS, COUNT = [], [0]


def check(code, name, cond, detail=''):
    COUNT[0] += 1
    print(('  PASS  ' if cond else '  FAIL  ') + code + ' ' + name + (('  -- ' + detail) if detail and not cond else ''),
          flush=True)
    if not cond:
        FAILS.append(code)
    return cond


# --------------------------------------------------------------------------------------------- module parsing
DECL = re.compile(r'^[ \t]*(?:@\[[^\]\n]*\][ \t\n]*)?((?:(?:private|protected|noncomputable|unsafe|partial)[ \t]+)*'
                  r'(?:theorem|lemma|def|abbrev|instance|structure|class|inductive|opaque|axiom|example))\b[ \t]*'
                  r'(\S*)', re.M)
STOP = re.compile(r'^(?:/--|/-!|#|end\b|section\b|variable\b|namespace\b|open\b|@\[|theorem\b|lemma\b|def\b|abbrev\b|'
                  r'noncomputable\b|instance\b|structure\b|class\b|inductive\b|opaque\b|axiom\b|example\b|private\b|'
                  r'protected\b|attribute\b|set_option\b|universe\b|macro\b|syntax\b|notation\b|local\b|scoped\b|'
                  r'elab\b|macro_rules\b|initialize\b|omit\b|include\b|export\b|mutual\b)', re.M)
CTX = re.compile(r'^(?:section|end|variable|namespace|open|noncomputable section|set_option|attribute|universe|'
                 r'notation|local|scoped|macro|macro_rules|syntax|elab|initialize|export|include|omit)\b.*$', re.M)
FORBIDDEN = re.compile(r'\bsorry\b|\badmit\b|\bnative_decide\b|\bimplemented_by\b|@\[extern|\bunsafe\b|'
                       r'\bdecide\s*:=\s*true|\bofReduceBool\b|^\s*axiom\b', re.M)


def code_only(text):
    text = re.sub(r'/-.*?-/', ' ', text, flags=re.S)
    return re.sub(r'--[^\n]*', ' ', text)


def decls(text):
    return [(m.group(1).split()[-1], m.group(2)) for m in DECL.finditer(code_only_keep_lines(text))]


def code_only_keep_lines(text):
    """Comments blanked out, line structure and offsets kept."""
    def blank(m):
        s = m.group(0)
        keep = 3 if s.startswith(('/--', '/-!')) else 0
        return s[:keep] + re.sub(r'[^\n]', ' ', s[keep:])
    text = re.sub(r'/-.*?-/', blank, text, flags=re.S)
    return re.sub(r'(?<!/)--[^\n]*', blank, text)


def chunks(text):
    """name -> (kind, statement, proof): a definition's whole text as its statement; a theorem's text up to its first
    ` :=` as its statement and the rest as its proof."""
    clean = code_only_keep_lines(text)
    out = {}
    for m in DECL.finditer(clean):
        kind, name = m.group(1).split()[-1], m.group(2)
        s = m.start()
        while text[s] in ' \t\n':
            s += 1
        nxt = STOP.search(clean, m.end())
        whole = text[s:nxt.start() if nxt else len(text)].rstrip()
        if kind in ('theorem', 'lemma') and ' :=' in whole:
            j = whole.index(' :=')
            out[name] = (kind, whole[:j], whole[j:])
        else:
            out[name] = (kind, whole, '')
    return out


def context_lines(text, start):
    return [m.group(0) for m in CTX.finditer(code_only_keep_lines(text), start)]


def token_in(name, text):
    return re.search(r'(?<![\w.\'])%s(?![\w\'])' % re.escape(name), text) is not None


def s1_status(mod):
    """The surface: {'preamble', 'decls', 'context', 'prints', 'hygiene': bool, 'stmt': {name: bool}}."""
    st = {'stmt': {}}
    st['preamble'] = mod.startswith(PREAMBLE)
    st['decls'] = decls(mod) == DECLS
    st['context'] = context_lines(mod, len(PREAMBLE) if st['preamble'] else 0) == CONTEXT
    st['prints'] = re.findall(r'^[ \t]*#print\b.*$', mod, re.M) == ['#print axioms ' + p for p in PRINTS]
    st['hygiene'] = FORBIDDEN.search(code_only(mod)) is None
    ch = chunks(mod)
    for name in STATEMENTS:
        st['stmt'][name] = name in ch and ch[name][1] == STATEMENTS[name]
    return st


def s1_ok(st, names=None):
    names = list(STATEMENTS) if names is None else names
    return st['preamble'] and st['decls'] and st['context'] and st['prints'] and st['hygiene'] and \
        all(st['stmt'].get(n) for n in names)


def s1_ok_for(st, names):
    """Q-IFF's reading: the preamble, the context, the hygiene, the named statements and their prints."""
    return st['preamble'] and st['context'] and st['hygiene'] and all(st['stmt'].get(n) for n in names)


def s3_status(mod):
    """(ok, detail): the iff's proof is `by constructor` with two components; the forward names FWD and not BWD, the
    backward names BWD and not FWD."""
    ch = chunks(mod).get(IFF)
    if ch is None:
        return False, 'the iff is absent'
    proof = code_only(ch[2])
    m = re.match(r'\s*:=\s*by\s*\n\s*constructor\s*\n(.*)$', proof, re.S)
    if not m:
        return False, 'the proof is not `by constructor` followed by its components'
    comps = re.split(r'^\s*·', m.group(1), flags=re.M)
    if comps[0].strip() or len(comps) != 3:
        return False, 'the proof does not have exactly two components'
    fwd, bwd = comps[1], comps[2]
    ok = token_in(FWD, fwd) and not token_in(BWD, fwd) and token_in(BWD, bwd) and not token_in(FWD, bwd)
    return ok, '' if ok else 'forward names %s/%s, backward names %s/%s' % (
        token_in(FWD, fwd), token_in(BWD, fwd), token_in(BWD, bwd), token_in(FWD, bwd))


def phrase_hits(text):
    t = norm(text)
    return [p for p in PHRASES if norm(p) in t]


# ------------------------------------------------------------------------------------- the landed index at D
def namespace_decls(text):
    """[(fully qualified name, line number, stripped first line)] of every declaration in a module text."""
    out, stack = [], []
    clean = code_only_keep_lines(text)
    lines = clean.split('\n')
    raw = text.split('\n')
    for k, line in enumerate(lines):
        m = re.match(r'^(namespace)\s+(\S+)|^(noncomputable\s+section|section)\b\s*(\S*)|^end\b\s*(\S*)', line)
        if m:
            if m.group(1):
                stack.append(('ns', m.group(2)))
            elif m.group(3):
                stack.append(('sec', m.group(4)))
            elif stack:
                stack.pop()
            continue
        d = DECL.match(line)
        if d and d.group(2):
            kind = d.group(1).split()[-1]
            if kind == 'example':
                continue
            ns = '.'.join(n for t, n in stack if t == 'ns')
            name = d.group(2)
            if name.startswith('_root_.'):
                full = name[len('_root_.'):]
            else:
                full = (ns + '.' + name) if ns else name
            out.append((full, k + 1, raw[k].strip()))
    return out


def decl_text(text, line):
    """The text of the declaration that starts at the 1-based line, up to the next top-level item."""
    lines = text.split('\n')
    start = sum(len(l) + 1 for l in lines[:line - 1])
    clean = code_only_keep_lines(text)
    nxt = STOP.search(clean, start + len(lines[line - 1]))
    return text[start:nxt.start() if nxt else len(text)].rstrip()


def landed_index(files):
    """{fully qualified name: [(path, line, first line)]} over the given {path: text} of OIBridge modules."""
    idx = {}
    for path, text in sorted(files.items()):
        for full, line, first in namespace_decls(text):
            idx.setdefault(full, []).append((path, line, first))
    return idx


def d_lean_files():
    paths = [p for p in ls(D, LEAN) if p.endswith('.lean')]
    return batch_texts(D, paths)


def visible_candidates(written):
    return ['OIBridge.' + written, PREFIX + written] + ['OIBridge.%s.%s' % (o, written) for o in OPENS]


def s2_status(files, mod):
    """(ok, problems): every landed name resolves, among the declarations visible from the module, to exactly one
    landed declaration, which is the frozen one at its cited file and line with its frozen text at D, and the module
    declares none of these names."""
    idx = landed_index(files)
    probs = []
    local = {n for _, n in decls(mod)} if mod is not None else set()
    for written, (fname, line, full, first) in LANDED.items():
        path = LEAN + fname
        hits = [(c, e) for c in visible_candidates(written) for e in idx.get(c, [])]
        if len(hits) != 1:
            probs.append('%s resolves to %d visible declarations' % (written, len(hits)))
            continue
        c, (p, ln, fl) = hits[0]
        if c != full or p != path or ln != line or not fl.startswith(first):
            probs.append('%s resolves to %s at %s:%d' % (written, c, p, ln))
            continue
        if sha256(decl_text(files[path], line)) != LANDED_SHA.get(written):
            probs.append('the landed text of %s differs from the frozen one' % written)
        if written.split('.')[-1] in local:
            probs.append('the module declares %s' % written)
    return not probs, probs


def d_files_status(texts):
    """The three files the execution modifies are, at D, the blobs the preregistration names."""
    bad = [p for p, b in D_BLOBS.items() if texts.get(p) is None or git_blob_id(texts[p]) != b]
    return not bad, bad


def cited_status(texts):
    probs = []
    for path, line, start in CITED:
        t = texts.get(path)
        if t is None:
            probs.append('%s is absent at D' % path)
            continue
        ls_ = t.split('\n')
        if line > len(ls_) or not ls_[line - 1].strip().startswith(start):
            probs.append('%s:%d does not read as cited' % (path, line))
    return not probs, probs


# ------------------------------------------------------------------------- the workflow, the import, the census
def apply_workflow_edit(wd):
    if wd is None or wd.count(SHARD_ANCHOR) != 1:
        return None
    out = wd.replace(SHARD_ANCHOR, '\n' + SHARD + SHARD_ANCHOR[1:], 1)
    for old, new in AGG_EDITS:
        if out.count(old) != 1:
            return None
        out = out.replace(old, new, 1)
    return out


def workflow_ok(wd, wx):
    want = apply_workflow_edit(wd)
    return want is not None and wx == want and git_blob_id(wx) == BLOBS[WORKFLOW]


def imports_want(d_text):
    if d_text is None or d_text.count(IMPORT_ANCHOR) != 1:
        return None
    return d_text.replace(IMPORT_ANCHOR, IMPORT_ANCHOR + IMPORT_LINE, 1)


def imports_ok(d_text, x_text):
    want = imports_want(d_text)
    return want is not None and x_text == want and git_blob_id(x_text) == BLOBS[IMPORTS]


def census_want(d_text):
    try:
        reg = json.loads(d_text)
    except (TypeError, ValueError):
        return None
    fam = reg.get('families', [])
    if json.dumps(reg, indent=2, ensure_ascii=False) + '\n' != d_text or not fam \
            or fam[-1].get('modules') != PREV_FAMILY_MODULES or any('KnDescent' in f.get('modules', []) for f in fam):
        return None
    reg['families'] = fam + [dict(FAMILY)]
    return json.dumps(reg, indent=2, ensure_ascii=False) + '\n'


def census_ok(d_text, x_text):
    want = census_want(d_text)
    return want is not None and x_text == want and git_blob_id(x_text) == BLOBS[CENSUS]


def probe_ok(text):
    return text is not None and git_blob_id(text) == BLOBS[PROBE]


# ------------------------------------------------------------------------------------- the probe and the report
def run_probe_text(text):
    with tempfile.TemporaryDirectory() as td:
        dest = os.path.join(td, 'kn_desc1_probe.py')
        with open(dest, 'w', encoding='utf-8') as f:
            f.write(text)
        r = subprocess.run([sys.executable, '-I', '-B', dest], cwd=td, capture_output=True, timeout=3600)
    return r.returncode, r.stdout.decode('utf-8', 'replace')


def exact_status(stdout):
    """Q-EXACT's rule: PASS for each of the seven ids, no FAIL, the summary line and the verdict line."""
    lines = stdout.split('\n')
    passes = {m.group(1) for m in (re.match(r'^PASS (\S+)', l) for l in lines) if m}
    fails = [l for l in lines if l.startswith('FAIL')]
    return all(i in passes for i in PROBE_IDS) and not fails and PROBE_SUMMARY in lines and PROBE_VERDICT in lines


def last_two(stdout):
    lines = [l for l in stdout.split('\n') if l.strip()]
    return lines[-2:]


def report_status(report, same_tree):
    """{name: ok} for the twelve theorems from an oi-evidence-result report, and a list of problems. `same_tree(sha)`
    says whether the run's commit carries the same kernel tree as the commit under verdict."""
    probs = []
    ok_names = {n: False for n in THEOREMS}
    if report is None:
        return ok_names, ['no axiom report']
    try:
        run, exp = report['run'], report['expected']
        mod = exp['modules'][MOD_KEY]
        reports = mod['reports']
    except (KeyError, TypeError):
        return ok_names, ['the report is not an oi-evidence-result with a KnDescent module table']
    if report.get('schema') != 'oi-evidence-result':
        probs.append('schema')
    if run.get('workflow') != 'verify.yml' or run.get('job_name') != 'Mathlib bridge':
        probs.append('the report is not of the Mathlib bridge job of verify.yml')
    if not same_tree(run.get('head_sha', '')):
        probs.append('the run\'s commit does not carry the kernel tree under verdict')
    if exp.get('build_success') is not True:
        probs.append('the build did not succeed')
    if any(v != 0 for v in exp.get('markers', {'missing': 1}).values()):
        probs.append('a failure marker is nonzero')
    if mod.get('status') != 'complete':
        probs.append('the module table is not complete')
    names = [str(r.get('name')) if isinstance(r, dict) else '?' for r in reports]
    if sorted(names) != sorted(PRINTS) or len(set(names)) != len(names):
        probs.append('the reports are not exactly the twelve frozen prints')
    if probs:
        return ok_names, probs
    for r in reports:
        n = r['name'][len(PREFIX):]
        ok_names[n] = set(r.get('axioms', ['?'])) <= PERMITTED
    bad = [n for n, ok in ok_names.items() if not ok]
    return ok_names, (['axioms outside the three for %s' % ', '.join(bad)] if bad else [])


# ------------------------------------------------------------------------------------------------- the cells
def cells(st1, s2ok, s3ok, ax, exact):
    desc = s1_ok(st1) and s2ok and all(ax.get(n) for n in THEOREMS)
    iff = s1_ok_for(st1, IFF_DECLS) and s2ok and s3ok and all(ax.get(n) for n in (FWD, BWD, IFF))
    out = []
    for (cell, pos, neg), ok in zip(CELLS, (desc, iff, exact)):
        out.append((cell, pos if ok else neg))
    return out


def all_positive(outcomes):
    return all(t == pos for (c, t), (_, pos, _) in zip(outcomes, CELLS))


def control_V(note, outcomes, last_lines):
    probs = []
    found = set(TOKEN_LIKE.findall(note))
    want = {t for _, t in outcomes}
    if found != want:
        probs.append('V1 the note carries %s, the cells give %s' % (sorted(found), sorted(want)))
    has_earned = norm(EARNED) in norm(unquote(note))
    if has_earned != all_positive(outcomes):
        probs.append('V2 the earned reading is %s, the cells are %s' % (
            'present' if has_earned else 'absent', 'all positive' if all_positive(outcomes) else 'not all positive'))
    if norm(NONINF) not in norm(unquote(note)):
        probs.append('V3 the non-inference rule is not stated in its frozen words')
    lines = note.split('\n')
    missing = [l for l in last_lines if l not in lines]
    if missing or len(last_lines) != 2:
        probs.append('V4 the note does not carry the probe\'s last two lines %s' % missing)
    return probs


def control_G(rows, stage):
    """stage: 'c0', 's1' or 'e'. delta(D, commit) is exactly the record's files and the five governed paths."""
    want = {PREREG: 'A', CONTROLS: 'A'}
    if stage == 'e':
        want[RESULT] = 'A'
    want.update(GOVERNED)
    got = {}
    for s, p in rows:
        if p.startswith(AMEND) and s == 'A' and stage != 'c0':
            continue
        got[p] = s
    return got == want, sorted(set(got.items()) ^ set(want.items()))


def control_R(files, stage, f_record, at_blobs, f_blobs, own_blob, controls_blob):
    """files: the record directory at the commit; f_record: at F (None without F). The record holds exactly the
    preregistration, controls.py, the result note at E, and the amendments at F; each control-plane file has its blob
    at F; controls.py is this file."""
    want = {PREREG, CONTROLS} | ({RESULT} if stage == 'e' else set())
    if f_record is not None:
        want |= {p for p in f_record if p.startswith(AMEND)}
    probs = []
    if set(files) != want:
        probs.append('the record holds %s' % sorted(set(files) ^ want))
    if f_record is not None:
        for p in [PREREG] + [q for q in f_record if q.startswith(AMEND)]:
            if at_blobs.get(p) != f_blobs.get(p):
                probs.append('%s differs from F' % p)
    if controls_blob != own_blob:
        probs.append('controls.py at the commit is not this file')
    return not probs, probs


# --------------------------------------------------------------------------------------------- the git drivers
def own_text():
    with open(os.path.abspath(__file__), 'rb') as f:
        return f.read().decode('utf-8')


def axioms_arg(argv):
    if '--axioms' in argv:
        with open(argv[argv.index('--axioms') + 1], encoding='utf-8') as f:
            return json.load(f)
    return None


def same_tree_fn(commit):
    tree = blob_of(commit, LEAN_TREE)

    def same(sha):
        return bool(re.fullmatch(r'[0-9a-f]{40}', sha or '')) and blob_of(sha, LEAN_TREE) == tree
    return same


_DFILES = []


def d_files():
    if not _DFILES:
        _DFILES.append(d_lean_files())
    return _DFILES[0]


def measure(commit, report):
    mod = show(commit, MOD)
    st1 = s1_status(mod) if mod is not None else {'preamble': False, 'decls': False, 'context': False,
                                                  'prints': False, 'hygiene': False, 'stmt': {}}
    s2ok, s2p = s2_status(d_files(), mod) if mod is not None else (False, ['the module is absent'])
    s3ok, s3d = s3_status(mod) if mod is not None else (False, 'the module is absent')
    ax, axp = report_status(report, same_tree_fn(commit))
    probe = show(commit, PROBE)
    rc, out = run_probe_text(probe) if probe is not None else (None, '')
    exact = exact_status(out)
    outcomes = cells(st1, s2ok, s3ok, ax, exact)
    return {'mod': mod, 's1': st1, 's2': (s2ok, s2p), 's3': (s3ok, s3d), 'ax': (ax, axp), 'probe_out': out,
            'probe_rc': rc, 'exact': exact, 'outcomes': outcomes, 'last': last_two(out)}


def tree_checks(commit, stage, m, f_commit=None):
    """The checks of one commit's tree; stage 'c0', 's1' or 'e'."""
    tag = ' at %s' % commit[:12]
    check('P', 'the probe is the frozen blob' + tag, probe_ok(show(commit, PROBE)))
    check('W', 'the workflow is D\'s with exactly the frozen edit' + tag,
          workflow_ok(show(D, WORKFLOW), show(commit, WORKFLOW)))
    check('I', 'OIBridge.lean is D\'s with exactly the frozen import line' + tag,
          imports_ok(show(D, IMPORTS), show(commit, IMPORTS)))
    check('C', 'the census is D\'s with exactly the frozen family appended' + tag,
          census_ok(show(D, CENSUS), show(commit, CENSUS)))
    st = m['s1']
    check('S1', 'the preamble is the frozen one, byte for byte' + tag, st['preamble'])
    check('S1', 'the thirteen declarations, in order, with their kinds' + tag, st['decls'])
    bad = [n for n in STATEMENTS if not st['stmt'].get(n)]
    check('S1', 'every statement and definition is the frozen text' + tag, not bad, ', '.join(bad))
    check('S1', 'the context lines are the frozen ones, in order' + tag, st['context'])
    check('S1', 'exactly the twelve frozen #print axioms lines, in order' + tag, st['prints'])
    check('S1', 'no sorry, admit, axiom, native_decide or unsafe construct' + tag, st['hygiene'])
    check('S2', 'every landed name resolves to the frozen landed declaration at D' + tag, m['s2'][0],
          '; '.join(m['s2'][1][:4]))
    check('S3', 'the iff names drivesElementaryAt_of_drives forward and drivesElementary_of_pow backward' + tag,
          m['s3'][0], m['s3'][1])
    hdr =m['mod'][:m['mod'].index('-/\n') + 3] if m['mod'] is not None and '-/\n' in m['mod'] else ''
    hits = phrase_hits(hdr) if hdr else ['header absent']
    check('S4', 'the module header carries none of the frozen phrases' + tag, not hits, ', '.join(hits))
    rows = delta(D, commit)
    gok, gdiff = control_G(rows, stage)
    check('G', 'delta(D, commit) is exactly the record files and the five governed paths' + tag, gok, str(gdiff[:6]))
    files = ls(commit, RDIR)
    at_blobs = {p: blob_of(commit, p) for p in files}
    f_record = ls(f_commit, RDIR) if f_commit else None
    f_blobs = {p: blob_of(f_commit, p) for p in f_record} if f_commit else {}
    own = own_text()
    rok, rp = control_R(files, stage, f_record, at_blobs, f_blobs, git_blob_id(own), at_blobs.get(CONTROLS))
    check('R', 'the record directory' + tag, rok, '; '.join(rp))


def prereg_status(pre, amendments, own_blob):
    """The control plane's declarations at F (K1, K2, G10) and the ids it must name."""
    lines = pre.split('\n')

    def blocks(info):
        out = []
        for i, l in enumerate(lines):
            if l == '```' + info:
                j = next((k for k in range(i + 1, len(lines)) if lines[k] == '```'), None)
                out.append('\n'.join(lines[i + 1:j]) if j is not None else None)
        return out
    near_re = re.compile(r'^[ \t]*(`{3,}|~{3,})[ \t]*(v3-round|v3-governed-paths)([ \t\r].*)?$')
    near = [l for l in lines if near_re.match(l) and l not in ('```v3-round', '```v3-governed-paths')]
    am = [p for p, txt in amendments.items() if any(near_re.match(l) for l in txt.split('\n'))]
    named = CONTROLS_NAMED.findall(pre)
    return {'round': blocks('v3-round') == [V3_ROUND], 'paths': blocks('v3-governed-paths') == [V3_PATHS],
            'near': not near and not am, 'missing': [i for i in FROZEN_IDS if i not in pre],
            'controls': named == [own_blob], 'named': named, 'c0': C0_NAMED.findall(pre)}


def freeze_checks(f_commit, full=True):
    f = rev(f_commit)
    chain = git('rev-list', '--reverse', '--parents', '%s..%s' % (D, f)).split('\n')
    chain = [c.split() for c in chain if c]
    check('F', 'D is an ancestor of F', git('merge-base', '--is-ancestor', D, f, ok=True) is not None)
    lin = bool(chain) and chain[0][1:] == [D] and all(len(c) == 2 for c in chain) and \
        all(chain[i][1] == chain[i - 1][0] for i in range(1, len(chain))) and chain[-1][0] == f
    check('F', 'D..F is a linear chain of single-parent commits from D (%d commits)' % len(chain), lin)
    cp_only = all(all(p == PREREG or p.startswith(AMEND) for _, p in delta(c[1], c[0])) for c in chain)
    check('F', 'every commit of D..F changes only control-plane files', cp_only)
    pre = show(f, PREREG)
    check('F', 'the preregistration is present at F', pre is not None)
    pre = pre or ''
    amend = {p: show(f, p) or '' for p in ls(f, RDIR) if p.startswith(AMEND)}
    st = prereg_status(pre, amend, git_blob_id(own_text()))
    check('F', 'exactly one v3-round block, the frozen one', st['round'])
    check('F', 'exactly one v3-governed-paths block, the frozen one', st['paths'])
    check('F', 'no near-miss declaration line and no block in an amendment', st['near'])
    check('F', 'the preregistration names every frozen object id', not st['missing'], ', '.join(st['missing']))
    check('F', 'the preregistration names this controls.py by its Git blob, once', st['controls'],
          'named %s' % st['named'])
    if full:
        c0 = C0_NAMED.findall(pre)
        check('F', 'the preregistration names one C0 commit', len(c0) == 1, 'named %s' % c0)
        if len(c0) == 1:
            c0_checks(c0[0])


def c0_checks(commit):
    c = rev(commit)
    check('K', 'C0 is a single-parent child of D', parents(c) == [D])
    check('K', 'C0 carries no result note', show(c, RESULT) is None)
    m = measure(c, None)
    tree_checks(c, 'c0', m)
    check('K', 'the probe at C0, run, reads exact', m['exact'], ' / '.join(m['last']))


def chain_checks(f_commit, commit):
    """F -> C1 -> S1 -> repairs -> [E]. Returns the stage-1 commit."""
    f, e = rev(f_commit), rev(commit)
    check('T', 'F is an ancestor of the commit', git('merge-base', '--is-ancestor', f, e, ok=True) is not None)
    chain = [c.split() for c in git('rev-list', '--reverse', '--parents', '%s..%s' % (f, e)).split('\n') if c]
    lin = len(chain) >= 2 and chain[0][1:] == [f] and all(len(c) == 2 for c in chain) and \
        all(chain[i][1] == chain[i - 1][0] for i in range(1, len(chain))) and chain[-1][0] == e
    check('T', 'F..commit is a linear chain of single-parent commits (%d commits)' % len(chain), lin)
    if len(chain) < 2:
        return None
    c1, s1 = chain[0][0], chain[1][0]
    own = git_blob_id(own_text())
    check('T', 'C1 adds controls.py alone, this file', delta(f, c1) == [('A', CONTROLS)] and
          blob_of(c1, CONTROLS) == own)
    check('T', 'S1 adds the module and the probe and modifies the import, the census and the workflow',
          sorted(delta(c1, s1)) == sorted((s, p) for p, s in GOVERNED.items()))
    has_note = show(e, RESULT) is not None
    later = chain[2:-1] if has_note else chain[2:]
    rep = all(delta(c[1], c[0]) == [('M', MOD)] for c in later)
    check('T', 'every commit between S1 and the note changes the module alone (proof repairs)', rep)
    if has_note and len(chain) >= 3:
        check('T', 'the note commit adds the result note alone', delta(chain[-1][1], e) == [('A', RESULT)])
    elif has_note:
        check('T', 'the note commit follows S1', False)
    return s1


def run_check(commit, f_commit, report):
    c = rev(commit)
    stage = 'e' if show(c, RESULT) is not None else 's1'
    ok, probs = cited_status(batch_texts(D, sorted({p for p, _, _ in CITED})))
    check('L', 'the preregistration\'s citations at D read as cited', ok, '; '.join(probs))
    dok, dbad = d_files_status(batch_texts(D, sorted(D_BLOBS)))
    check('L', 'the three modified files at D are the blobs the preregistration names', dok, ', '.join(dbad))
    if f_commit:
        freeze_checks(f_commit, full=True)
        s1 = chain_checks(f_commit, c)
        if s1 and s1 != c:
            tree_checks(s1, 's1', measure(s1, None), rev(f_commit))
    m = measure(c, report)
    tree_checks(c, stage, m, rev(f_commit) if f_commit else None)
    note = show(c, RESULT)
    if note is not None:
        hits = phrase_hits(note)
        check('S4', 'the result note carries none of the frozen phrases', not hits, ', '.join(hits))
        probs = control_V(note, m['outcomes'], m['last'])
        check('V', 'the result note states exactly the computed tokens, the frozen texts and the probe lines',
              not probs, '; '.join(probs))
    report_line(m)


def report_line(m):
    for cell, token in m['outcomes']:
        print('  CELL  %-7s %s' % (cell, token))
    if m['ax'][1]:
        print('  NOTE  axiom report: %s' % '; '.join(m['ax'][1]))


def print_verdict(commit, report):
    c = rev(commit)
    m = measure(c, report)
    for cell, token in m['outcomes']:
        print('VERDICT  %-7s %s' % (cell, token))
    for line in m['last']:
        print(line)
    if m['ax'][1]:
        print('# axiom report: %s' % '; '.join(m['ax'][1]))
    if not m['s2'][0]:
        print('# S2: %s' % '; '.join(m['s2'][1]))
    check('V', 'exactly one token per cell', len(m['outcomes']) == 3 and
          all(t in (p, n) for (c_, t), (_, p, n) in zip(m['outcomes'], CELLS)))


def scaffold(commit, report):
    c = rev(commit)
    m = measure(c, report)
    out = ['# KN-DESC-1 — result (scaffold generated by controls.py from the measurements at %s)' % c, '']
    for cell, token in m['outcomes']:
        out.append('- %s: `%s`' % (cell, token))
    out.append('')
    if all_positive(m['outcomes']):
        out += ['> Earned reading: ' + EARNED, '']
    out += ['> Non-inference rule: ' + NONINF, '', 'The probe, run by `controls.py` at this commit, printed:', '']
    out += m['last'] + ['']
    print('\n'.join(out))


# ------------------------------------------------------------------------------------------------------ self-test
def self_test():
    n0 = COUNT[0]
    mod = cat_blob(BLOBS[MOD])
    check('Z', 'the frozen module blob is readable', mod is not None)
    probe = cat_blob(BLOBS[PROBE])
    check('Z', 'the frozen probe blob is readable', probe is not None)
    if mod is None or probe is None:
        return
    check('Z', 'the frozen module and probe are their blobs', git_blob_id(mod) == BLOBS[MOD] and probe_ok(probe))
    files = d_files()
    texts = batch_texts(D, sorted({p for p, _, _ in CITED}))
    ok, probs = cited_status(texts)
    check('L', 'the citations at D read as cited', ok, '; '.join(probs))
    t2 = dict(texts)
    t2[LEAN + 'StructuralClosure.lean'] = '\n' + t2[LEAN + 'StructuralClosure.lean']
    check('M', 'a citation moved by one line fails L', not cited_status(t2)[0])

    # positive controls on the frozen module
    st = s1_status(mod)
    check('S1', 'the frozen module passes the surface', s1_ok(st))
    s2ok, s2p = s2_status(files, mod)
    check('S2', 'the frozen module resolves to the landed declarations at D', s2ok, '; '.join(s2p))
    s3ok, s3d = s3_status(mod)
    check('S3', 'the frozen module names one witness per direction', s3ok, s3d)
    check('S4', 'the frozen header carries no frozen phrase', not phrase_hits(mod[:HEADER_END]))
    check('S4', 'the frozen earned reading and non-inference rule carry no frozen phrase',
          not phrase_hits(EARNED) and not phrase_hits(NONINF))
    rc, out = run_probe_text(probe)
    check('P', 'the frozen probe, run, reads exact', exact_status(out) and last_two(out) == [PROBE_SUMMARY,
                                                                                            PROBE_VERDICT])
    good_ax = {n: True for n in THEOREMS}
    pos = cells(st, s2ok, s3ok, good_ax, True)
    check('V', 'the frozen fixtures read three positive tokens', all_positive(pos))

    def rep(text, a, b):
        if text.count(a) != 1:
            raise SystemExit('self-test: the mutation anchor is not unique: %r' % a[:60])
        return text.replace(a, b, 1)

    def fails_s1(m2):
        return not s1_ok(s1_status(m2))

    # S1 mutations
    cm = STATEMENTS['compress_mem']
    m_hc = rep(mod, cm, cm.replace(' (hC : ContextStable 𝓘)', ''))
    check('M', 'S1: hC dropped from compress_mem fails S1', fails_s1(m_hc))
    m_ne = rep(mod, cm, cm.replace(' [Nonempty S]', ''))
    check('M', 'S1: [Nonempty S] dropped from compress_mem fails S1', fails_s1(m_ne))
    dp = STATEMENTS[BWD]
    m_hp = rep(mod, dp, dp.replace('(hpow : ∀ k : ℕ, DrivesElementaryAt', '(hpow : ∀ k : ℕ, 1 ≤ k → DrivesElementaryAt'))
    check('M', 'S1: hpow weakened to 1 ≤ k fails S1', fails_s1(m_hp))
    ip = STATEMENTS[IFF]
    m_dg = rep(mod, ip, ip.replace('\n      ∧ DaggerStable 𝓘 ∧ ∀ k', '\n      ∧ ∀ k'))
    check('M', 'S1: DaggerStable dropped from the iff fails S1', fails_s1(m_dg))
    m_f3 = rep(mod, dp, dp.replace(') : DrivesElementary 𝓘', ') : DrivesElementaryAt 𝓘 (Fin 3)'))
    check('M', 'S1: the descent\'s conclusion at Fin 3 fails S1', fails_s1(m_f3))
    m_pr = mod + '#print axioms OIBridge.KnDescent.le_two_pow\n'
    check('M', 'S1: a thirteenth print fails S1', fails_s1(m_pr))
    m_ctx = rep(mod, CONTEXT[1], CONTEXT[1].replace(' [Fintype T]', ''))
    check('M', 'S1: a changed section binder fails S1', fails_s1(m_ctx))
    m_ex = rep(mod, '\nend\n\nend KnDescent\n', '\ntheorem extra : True := trivial\n\nend\n\nend KnDescent\n')
    check('M', 'S1: an extra declaration fails S1', fails_s1(m_ex))
    m_ind = rep(mod, '\nend\n\nend KnDescent\n', '\n  axiom bad : False\n\nend\n\nend KnDescent\n')
    check('M', 'S1: an indented axiom fails S1', fails_s1(m_ind))
    m_so = rep(mod, '  exact h3\n', '  exact sorry\n')
    check('M', 'S1: a sorry in a proof fails S1', fails_s1(m_so))
    m_rp = rep(mod, '  exact h3\n', '  simpa using h3\n')
    check('M', 'S1: a proof repair passes S1', s1_ok(s1_status(m_rp)))

    # S2 mutations, on the landed side at D and on the module
    f2 = dict(files)
    f2[LEAN + 'LieRankSource.lean'] = rep(f2[LEAN + 'LieRankSource.lean'], 'def transition (a b : S)',
                                          'def transition\' (a b : S)')
    check('M', 'S2: a landed declaration renamed at D fails S2', not s2_status(f2, mod)[0])
    f3 = dict(files)
    f3[LEAN + 'ZZShadow.lean'] = 'namespace OIBridge\nnamespace CoherentLift\ndef transition : Nat := 0\nend ' \
                                 'CoherentLift\nend OIBridge\n'
    check('M', 'S2: a second visible declaration of transition fails S2', not s2_status(f3, mod)[0])
    f4 = dict(files)
    f4[LEAN + 'ImplementationLocality.lean'] = rep(
        f4[LEAN + 'ImplementationLocality.lean'], 'def ContextStable (𝓘 : ImplementationClass) : Prop :=\n',
        'def ContextStable (𝓘 : ImplementationClass) : Prop :=\n  True ∨\n')
    check('M', 'S2: a landed definition changed at D fails S2', not s2_status(f4, mod)[0])
    unwritten = [w for w in LANDED if not token_in(w, code_only(mod))]
    check('Z', 'the frozen module writes every landed name S2 resolves (the list is not vacuous)', not unwritten,
          ', '.join(unwritten))
    m_un = rep(mod, 'LiftAudit.pairProj, ', '')
    check('S2', 'a proof repair that drops a simp lemma still resolves', s2_status(files, m_un)[0])
    m_sh = rep(mod, '\nend\n\nend KnDescent\n', '\ndef transition : Nat := 0\n\nend\n\nend KnDescent\n')
    check('M', 'S2: a module declaration shadowing a landed name fails S2 (and S1)',
          not s2_status(files, m_sh)[0] and fails_s1(m_sh))
    dt = batch_texts(D, sorted(D_BLOBS))
    check('L', 'the three modified files at D are the blobs the preregistration names', d_files_status(dt)[0])
    dt2 = dict(dt)
    dt2[WORKFLOW] = dt2[WORKFLOW] + '\n'
    check('M', 'L: another workflow at D fails L', not d_files_status(dt2)[0])

    # S3 and the S4 header mutation
    fwd_old = '    exact ⟨h.arch, h.context, h.label, h.dagger, fun k => drivesElementaryAt_of_drives h.drives _⟩'
    fwd_new = ('    exact ⟨h.arch, h.context, h.label, h.dagger, fun k => ⟨fun a b t => h.drives.1 _ a b t,\n'
               '      fun a b => h.drives.2.1 _ a b, fun a => h.drives.2.2 _ a⟩⟩')
    m_s3 = rep(mod, fwd_old, fwd_new)
    st_s3 = s1_status(m_s3)
    check('M', 'S3: a forward component not naming drivesElementaryAt_of_drives fails S3 and nothing else',
          not s3_status(m_s3)[0] and s1_ok(st_s3) and s2_status(files, m_s3)[0] and not phrase_hits(m_s3[:HEADER_END]))
    m_s3b = rep(mod, '    exact ⟨harch, hC, hL, hD, drivesElementary_of_pow harch hC hL hpow⟩',
                '    exact ⟨harch, hC, hL, hD, drivesElementary_of_pow harch hC hL hpow⟩\n'
                '    have _x := @drivesElementaryAt_of_drives')
    check('M', 'S3: the backward component naming the forward witness fails S3', not s3_status(m_s3b)[0])
    src_header = ('/-\n  KnDescentDesign.lean — research-only rebuild of the design module of the research thread '
                  '`research/equivalence` (node E8,\n  draft S3). Not adopted, not certified, not a round.\n-/\n')
    m_hd = src_header + mod[HEADER_END:]
    check('M', 'S4: the source\'s header in place of the frozen one fails S1 and S4',
          fails_s1(m_hd) and bool(phrase_hits(m_hd[:m_hd.index('-/\n') + 3])))
    for p in ('Hence Kn is closed.', 'This establishes F1.', 'OI supplies the drivability.',
              'The kernel proof of the probe.'):
        check('M', 'S4: the phrase in "%s" is caught' % p, bool(phrase_hits(p)))

    # P
    check('M', 'P: a probe with one changed byte fails P', not probe_ok(probe.replace('t = 1', 't = 2', 1)))

    # W
    wd = show(D, WORKFLOW)
    good_w = apply_workflow_edit(wd)
    check('W', 'the frozen workflow edit reproduces its frozen blob', workflow_ok(wd, good_w))
    check('M', 'W: the unchanged workflow fails W', not workflow_ok(wd, wd))
    check('M', 'W: the aggregate without the KNDESC1 test fails W',
          not workflow_ok(wd, rep(good_w, '          test "${KNDESC1_RESULT}" = success\n', '')))
    check('M', 'W: the shard without its verdict test fails W', not workflow_ok(wd, rep(
        good_w, '          test "$(printf \'%s\\n\' "$out" | tail -n 1)" = "VERDICT COMPRESSION-DESCENT-EXACT"\n', '')))

    # I
    di = show(D, IMPORTS)
    gi = imports_want(di)
    check('I', 'the frozen import edit reproduces its frozen blob', imports_ok(di, gi))
    check('M', 'I: the unchanged file fails I', not imports_ok(di, di))
    moved = rep(di, 'import OIBridge.SubstratumSource\n', 'import OIBridge.SubstratumSource\n' + IMPORT_LINE)
    check('M', 'I: the line at another position fails I', moved != gi and not imports_ok(di, moved))
    check('M', 'I: a second added line fails I', not imports_ok(di, rep(gi, IMPORT_LINE, IMPORT_LINE +
                                                                         'import OIBridge.KnDescentExtra\n')))

    # C
    dc = show(D, CENSUS)
    gc = census_want(dc)
    check('C', 'the frozen census edit reproduces its frozen blob', census_ok(dc, gc))
    check('M', 'C: the unchanged file fails C', not census_ok(dc, dc))
    reg = json.loads(gc)
    reg['families'][-1]['status'] = 'carried'
    check('M', 'C: the family with another status fails C',
          not census_ok(dc, json.dumps(reg, indent=2, ensure_ascii=False) + '\n'))
    reg = json.loads(gc)
    reg['families'].insert(0, reg['families'].pop())
    check('M', 'C: the family at another position fails C',
          not census_ok(dc, json.dumps(reg, indent=2, ensure_ascii=False) + '\n'))
    check('M', 'C: a whitespace change fails C', not census_ok(dc, gc.replace('\n', '\n ', 1)))

    # V -- the decision rules, each mutation in its own cell
    o = dict(cells(s1_status(m_hc), s2_status(files, m_hc)[0], s3_status(m_hc)[0], good_ax, True))
    check('M', 'V: a changed signature of compress_mem reads DESCENT-NOT-ESTABLISHED alone',
          o == {'Q-DESC': CELLS[0][2], 'Q-IFF': CELLS[1][1], 'Q-EXACT': CELLS[2][1]})
    o = dict(cells(st_s3, s2_status(files, m_s3)[0], s3_status(m_s3)[0], good_ax, True))
    check('M', 'V: a forward component without its witness reads IFF-NOT-ESTABLISHED alone',
          o == {'Q-DESC': CELLS[0][1], 'Q-IFF': CELLS[1][2], 'Q-EXACT': CELLS[2][1]})
    p_w = rep(probe, 'flow_transition(nT, iota[0], 3, t)', 'flow_transition(nT, iota[0], 2, t)')
    rc_w, out_w = run_probe_text(p_w)
    o = dict(cells(st, s2ok, s3ok, good_ax, exact_status(out_w)))
    check('M', 'V: a probe with one changed witness value reads INSTANCES-NOT-ESTABLISHED alone',
          rc_w == 0 and 'FAIL K1' in out_w and
          o == {'Q-DESC': CELLS[0][1], 'Q-IFF': CELLS[1][1], 'Q-EXACT': CELLS[2][2]})
    o = dict(cells(st, False, s3ok, good_ax, True))
    check('M', 'V: an S2 failure reads DESCENT and IFF not established and leaves Q-EXACT',
          o == {'Q-DESC': CELLS[0][2], 'Q-IFF': CELLS[1][2], 'Q-EXACT': CELLS[2][1]})
    ax_c = dict(good_ax, compress_mem=False)
    o = dict(cells(st, s2ok, s3ok, ax_c, True))
    check('M', 'V: a non-standard axiom on compress_mem reads DESCENT-NOT-ESTABLISHED alone',
          o == {'Q-DESC': CELLS[0][2], 'Q-IFF': CELLS[1][1], 'Q-EXACT': CELLS[2][1]})
    o = dict(cells(st, s2ok, s3ok, {}, True))
    check('M', 'V: no axiom report reads DESCENT and IFF not established',
          o == {'Q-DESC': CELLS[0][2], 'Q-IFF': CELLS[1][2], 'Q-EXACT': CELLS[2][1]})

    # X -- the axiom report reader, on synthetic reports (fixtures, not evidence)
    def fixture(**kw):
        r = {'schema': 'oi-evidence-result',
             'run': {'workflow': 'verify.yml', 'job_name': 'Mathlib bridge', 'head_sha': 'a' * 40},
             'expected': {'build_success': True, 'markers': {'sorryAx': 0, "declaration uses 'sorry'": 0, 'error:': 0},
                          'modules': {MOD_KEY: {'status': 'complete', 'reports': [
                              {'name': p, 'axioms': ['propext', 'Classical.choice', 'Quot.sound']} for p in PRINTS]}}}}
        for k, v in kw.items():
            if k == 'reports':
                r['expected']['modules'][MOD_KEY]['reports'] = v(r['expected']['modules'][MOD_KEY]['reports'])
            elif k in ('build_success', 'markers'):
                r['expected'][k] = v
            else:
                r['run'][k] = v
        return r
    same = (lambda sha: sha == 'a' * 40)
    ax_ok, axp = report_status(fixture(), same)
    check('X', 'a standard report reads all twelve within the three axioms', all(ax_ok.values()) and not axp)
    for label, kw in [('a sorryAx report', {'reports': lambda rs: [dict(r, axioms=r['axioms'] + ['sorryAx'])
                                                                    if r['name'].endswith('compress_mem') else r
                                                                    for r in rs]}),
                      ('a missing print', {'reports': lambda rs: rs[1:]}),
                      ('an extra report', {'reports': lambda rs: rs + [{'name': PREFIX + 'extra', 'axioms': []}]}),
                      ('a failed build', {'build_success': False}),
                      ('a nonzero marker', {'markers': {'sorryAx': 1}}),
                      ('another kernel tree', {'head_sha': 'b' * 40}),
                      ('another job', {'job_name': 'Lean kernel check'})]:
        a2, p2 = report_status(fixture(**kw), same)
        check('M', 'X: %s does not read all twelve standard' % label, not all(a2.values()))
    check('M', 'X: no report reads none standard', not any(report_status(None, same)[0].values()))

    # the note
    last = [PROBE_SUMMARY, PROBE_VERDICT]
    toks = '\n'.join('- %s: `%s`' % c for c in pos)
    note = '%s\n\n> %s\n\n> %s\n\n%s\n%s\n' % (toks, EARNED, NONINF, last[0], last[1])
    check('V', 'a note with the computed tokens and the frozen texts passes V', not control_V(note, pos, last))
    check('S4', 'that note carries no frozen phrase', not phrase_hits(note))
    check('M', 'V: a note with an extra token fails V',
          bool(control_V(note + '\nAlso KN-DESC-IFF-NOT-ESTABLISHED.\n', pos, last)))
    neg = [(c, n if c == 'Q-EXACT' else t) for (c, t), (_, _, n) in zip(pos, CELLS)]
    note_neg = note.replace(CELLS[2][1], CELLS[2][2])
    check('M', 'V: a note stating the earned reading with a cell not positive fails V',
          bool(control_V(note_neg, neg, last)))
    check('V', 'the same note without the earned reading passes V',
          not control_V(note_neg.replace('> %s\n\n' % EARNED, ''), neg, last))
    check('M', 'V: a note without the non-inference rule fails V',
          bool(control_V(note.replace('> %s\n\n' % NONINF, ''), pos, last)))
    check('M', 'V: a note without the probe\'s summary line fails V',
          bool(control_V(note.replace(PROBE_SUMMARY + '\n', ''), pos, last)))
    check('M', 'V: a misspelled cell token fails V', bool(control_V(note + '\nKN-DESC-DESCENT-SHOWN\n', pos, last)))
    wrapped = note.replace('> ' + NONINF, '> ' + NONINF[:200] + '\n> ' + NONINF[200:])
    check('V', 'a frozen text quoted across lines passes V', not control_V(wrapped, pos, last))

    # F, on synthetic control-plane texts
    own = git_blob_id(own_text())
    pre_ok = ('```v3-round\n%s\n```\n\n```v3-governed-paths\n%s\n```\n\n%s\n\n`controls.py`, Git blob `%s`; '
              '`C0` commit `%s`.\n' % (V3_ROUND, V3_PATHS, ' '.join(FROZEN_IDS), own, 'c' * 40))
    s = prereg_status(pre_ok, {}, own)
    check('F', 'a control plane with the frozen blocks, ids and names passes F',
          s['round'] and s['paths'] and s['near'] and not s['missing'] and s['controls'] and s['c0'] == ['c' * 40])
    for label, txt, am, key in [
            ('a tilde fence', pre_ok.replace('```v3-round\n', '~~~v3-round\n', 1), {}, 'near'),
            ('a second round block', pre_ok + '```v3-round\n%s\n```\n' % V3_ROUND, {}, 'round'),
            ('a changed governed path', pre_ok.replace('execution A verification/lean/kn_desc1_probe.py',
                                                       'execution AM verification/lean/kn_desc1_probe.py'), {}, 'paths'),
            ('an opener with trailing text', pre_ok + '```v3-governed-paths extra\n', {}, 'near'),
            ('a block in an amendment', pre_ok, {AMEND + 'a1.md': '```v3-round\nround X\n```\n'}, 'near'),
            ('a missing frozen id', pre_ok.replace(BLOBS[CENSUS], 'x' * 40), {}, 'missing'),
            ('another controls blob', pre_ok.replace(own, 'd' * 40), {}, 'controls')]:
        s2 = prereg_status(txt, am, own)
        bad = bool(s2[key]) if key == 'missing' else not s2[key]
        check('M', 'F: %s fails F' % label, bad)

    # G and R, on synthetic rows and record listings
    rows_e = [('A', PREREG), ('A', CONTROLS), ('A', RESULT)] + [(s, p) for p, s in GOVERNED.items()]
    check('G', 'the frozen governed rows pass G at E', control_G(rows_e, 'e')[0])
    check('G', 'the frozen governed rows less the note pass G at S1', control_G(rows_e[:2] + rows_e[3:], 's1')[0])
    check('M', 'G: an extra path fails G', not control_G(rows_e + [('A', 'verification/lean/extra.py')], 'e')[0])
    check('M', 'G: a changed landed module fails G',
          not control_G(rows_e + [('M', LEAN + 'SubstratumSource.lean')], 'e')[0])
    check('M', 'G: a note at C0 fails G', not control_G(rows_e, 'c0')[0])
    rec = [PREREG, CONTROLS, RESULT]
    fb = {PREREG: 'f' * 40}
    check('R', 'the frozen record passes R', control_R(rec, 'e', [PREREG], {PREREG: 'f' * 40}, fb, own, own)[0])
    check('M', 'R: an extra file fails R',
          not control_R(rec + [RDIR + 'extra.md'], 'e', [PREREG], {PREREG: 'f' * 40}, fb, own, own)[0])
    check('M', 'R: a changed preregistration fails R',
          not control_R(rec, 'e', [PREREG], {PREREG: 'e' * 40}, fb, own, own)[0])
    check('M', 'R: another controls.py fails R', not control_R(rec, 'e', [PREREG], {PREREG: 'f' * 40}, fb, own,
                                                               'c' * 40)[0])
    print('  self-test: %d checks' % (COUNT[0] - n0))


def main(argv):
    try:
        if argv[1:] == ['--self-test']:
            self_test()
        elif len(argv) >= 3 and argv[1] == 'verdict':
            print_verdict(argv[2], axioms_arg(argv))
        elif len(argv) >= 3 and argv[1] == 'note-scaffold':
            scaffold(argv[2], axioms_arg(argv))
            return 0
        elif len(argv) == 3 and argv[1] == 'check-freeze':
            freeze_checks(argv[2])
        elif len(argv) == 3 and argv[1] == 'check-c0':
            c0_checks(argv[2])
        elif len(argv) >= 3 and argv[1] == 'check':
            f = argv[argv.index('--freeze') + 1] if '--freeze' in argv else None
            run_check(argv[2], f, axioms_arg(argv))
        else:
            print(__doc__)
            return 2
    except RuntimeError as e:
        print('controls: FAILED -- %s' % e)
        return 1
    if FAILS:
        print('controls: FAILED (%d of %d): %s' % (len(FAILS), COUNT[0], ' '.join(sorted(set(FAILS)))))
        return 1
    print('controls: OK -- %d checks' % COUNT[0])
    return 0


LANDED_SHA.update({  # SHA-256 of each landed declaration's text at D, as decl_text reads it
    'ImplementationClass': '06f1529ee87de1fb193e7ede25cabead9ace9b4f531224bdfa97b158362e3fe4',
    'ContextStable': '54760661bb067cd154c9f009c51c26521780c27d050b3c4c921a86e9043b0e45',
    'LabelInvariant': '054acc72a79ac38a02546b3e3471a7ec510edf18d6f86f4f8d92376bfcd75e43',
    'fullClass': '1e0fca7d4785049914900a4d2902cd325ee56c0ff1cf596967469870a1047c84',
    'Architecture': 'c3d991a57d908bcf340be574c1384affeb6ddb9b14fabf875eacc11b92f83b02',
    'DaggerStable': '339a16a79e8487b807f3263fe11c8affe9ce0bc72d67da70832070c3d4d7d6dd',
    'DrivesElementary': '11770f9d2a288b7b147fd04ef8563282af53e86a819668b6ab9a45d96e30b4cb',
    'QuantumArchitecture': 'ef926bb93bffd6cc453843cb85d96f3b2ffab92e567f589842f48fb91abbd271',
    'ancBlock': 'cedaf033d748eb98b9d7a8c1dec39c9dd13aaa04f17fb584d1ce4a8a5372055d',
    'tensorOf': '8372fd86e5a11e5afaf1bcedd92af554f095f510a49623403191f4f2314bdafb',
    'transition': '0cc5834341f40552682a2eafd1c1d8905043e9c1202ce2980e7e759221be9bdb',
    'phaseGate': '60a60645bf7fa8da2cb72a06f40f2039adf28ad225aa4a5fa62c85b66a28fc91',
    'permMatrix': '5f7b9dcabb5484e89597733dafa1cf0efc19a4ad882af09a8c1a5c8321c5587a',
    'ReachabilitySeam.flow': '51ebd98362f2a958bfa5284d6e6e6ba54e38b23354d0dfbe1b9336775fed5eea',
    'LiftAudit.pairProj': 'b3d619da15feeea65a98760148a78d899a7429856a751ba8c5fd8cc1c7786e1d',
})

if __name__ == '__main__':
    sys.exit(main(sys.argv))
