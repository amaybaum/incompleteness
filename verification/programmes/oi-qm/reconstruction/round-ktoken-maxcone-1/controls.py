#!/usr/bin/env python3
"""Round KTOKEN-MAXCONE-1 -- the round's own static controls (stage 1).

It reads nothing but the repository, through git, and certifies nothing on its own: the Lean kernel,
the axiom audit and the release gate establish the mathematics, check A3 (checks/run_checks.py, run
by the Mathlib bridge job) the k = 2 independence at the level of kernel terms, and the V3 verifier
the protocol. What it checks is that the execution carries the frozen statement surface and print
list, the frozen proof shape of the equivalence and of the k = 2 recovery, the frozen execution
blobs and workflow, registry and import edits, the retained evidence the preregistration pins,
none of the excluded phrases, and no change outside the governed paths.

    python3 -I controls.py --self-test                    mutation controls on the module text and on
                                                          synthetic inputs; constants against the
                                                          preregistration beside this file
    python3 -I controls.py check <E> --freeze <F>         C1, C2, S1-S4, W, I, J, R, P, G, T against E
    python3 -I controls.py verdict <E> --freeze <F> [--axioms LOG]
                                                          the four cell tokens from the measurements at
                                                          E: the static controls, the probe blob at E
                                                          run with python3 -I, and the axiom reports and
                                                          the A3 line of E's exact-head bridge log

Exit 1 on any failure.
"""
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

D = 'b96662e6be4f537502c772db369ea32a35b213a8'
RDIR = 'verification/programmes/oi-qm/reconstruction/round-ktoken-maxcone-1/'
PREREG = RDIR + 'preregistration.md'
RESULT = RDIR + 'result.md'
CONTROLS = RDIR + 'controls.py'
CHECKFILE = RDIR + 'checks/KTokenPairCheck.lean'
RUNNER = RDIR + 'checks/run_checks.py'
MODULE = 'verification/lean-mathlib/OIBridge/KTokenMaxCone.lean'
PAIR = 'verification/lean-mathlib/OIBridge/EqvK2MaxCone.lean'
PROBE = 'verification/lean/ktoken_maxcone1_probe.py'
ROOT = 'verification/lean-mathlib/OIBridge.lean'
REGISTRY = 'verification/lean-manuscript-census.json'
WORKFLOW = '.github/workflows/verify.yml'
LEGACY = 'verification/infrastructure/legacy-records.json'
NS = 'OIBridge.KTokenMaxCone'

IMPORTS = ['import OIBridge.EqvK2Generation']
OPEN_NS, END_NS, BLOCKS = 'namespace OIBridge.KTokenMaxCone', 'end OIBridge.KTokenMaxCone', 3
SCOPED = ['scoped instance carrierDecidableEq (d n : ℕ) : DecidableEq (Carrier d n) :=',
          'attribute [scoped instance high] bitsDecEq']
EVAL = ('open Lean Meta in\n'
        '#eval show MetaM Unit from do\n'
        '  if (← getEnv).contains `OIBridge.EqvK2MaxCone.pairCone_eq_Q3_of_drive_maxCone then\n'
        '    throwError "OIBridge.EqvK2MaxCone.pairCone_eq_Q3_of_drive_maxCone is in the environment"\n'
        '  logInfo "OIBridge.EqvK2MaxCone.pairCone_eq_Q3_of_drive_maxCone is not in the environment"\n')
EVAL_LOG = 'OIBridge.EqvK2MaxCone.pairCone_eq_Q3_of_drive_maxCone is not in the environment'
A3_LOG = 'A3-CHECK-NONVACUOUS: 13 cases as expected'
NAMES = ['WK', 'prodStateK', 'maxConeK', 'dictK', 'QK', 'cnotK', 'actK',
         'subset_QK_of_maxCone_drive', 'QK_subset_of_products_cone_drive', 'kCone_eq_QK_of_drive_maxCone',
         'driveInvariantK_of_eq_QK', 'kCone_eq_QK_iff_drive_maxCone', 'pairCarrierEquiv',
         'pairCone_eq_Q3_of_kToken']
PRINTS = '''tensor_conjugation pauliWord_orthogonal pauliWord_complete coordinates_dictionary
dictionary_coordinates dictionary_hermitian coordinates_dictionary_real dictionary_coordinates_real
blockFam_mul isWord_conjTranspose isWord_lift sign_induction isWord_rzFam isWord_suFam reach_prod
reach_norm subset_psd_of_maxCone_drive psd_subset_of_products_cone_drive kCone_eq_psd_of_drive_maxCone
driveInvariant_of_eq_psd kCone_eq_psd_iff_drive_maxCone dictionary_prodTab trace_dictionary_mul
tokMat_blochH lor_blochH quad_dictionary_prodVec psd_subset_of_pure_cone_drive
tableCone_eq_psd_of_drive_maxCone lorPair_nonneg_of_maxConeTab tableCone_eq_psd_of_drive_maxConeTab
tableDrive_of_eq_psd tableCone_eq_psd_iff_drive_maxConeTab pauliWord_apply dictionary_tabOf mem_QK_iff
tupOf_prodTab sum_prodTab_tupOf cnotM_apply pauli_cnot_pair dictK_cflip tabAct_cnotM tabAct_cnotM_eq
localM_conj_dictionary tabAct_localM tabAct_localM_eq tabAct_rotK tabAct_cycK
tableCone_subset_psd_of_maxCone_drive psd_subset_tableCone_of_products_cone_drive
subset_QK_of_maxCone_drive QK_subset_of_products_cone_drive kCone_eq_QK_of_drive_maxCone
driveInvariantK_of_eq_QK kCone_eq_QK_iff_drive_maxCone pairCarrierEquiv_prodState
pairCarrierEquiv_maxCone maxCone_of_pairCarrierEquiv mem_Q3_iff_pairCarrier pairCarrierEquiv_cnot
pairCarrierEquiv_actT pairCone_eq_Q3_of_kToken blochH_real lor_blochH_decomp lorTests_of_blochTests
maxConeTab_of_blochTests maxConeTab_of_prodVec_nonneg prodVec_nonneg_of_maxConeTab
maxConeTab_iff_prodVec_nonneg'''.split()
INCL = ['subset_QK_of_maxCone_drive', 'QK_subset_of_products_cone_drive']
EQ = ['kCone_eq_QK_of_drive_maxCone', 'driveInvariantK_of_eq_QK', 'kCone_eq_QK_iff_drive_maxCone']
PAIRSET = ['pairCarrierEquiv_prodState', 'pairCarrierEquiv_maxCone', 'maxCone_of_pairCarrierEquiv',
           'mem_Q3_iff_pairCarrier', 'pairCarrierEquiv_cnot', 'pairCarrierEquiv_actT', 'pairCone_eq_Q3_of_kToken']
SUPPORT = [p for p in PRINTS if p not in INCL + EQ + PAIRSET]
IFF_PROOF = '⟨driveInvariantK_of_eq_QK, fun h => kCone_eq_QK_of_drive_maxCone hH1 hadd hsmul hmax h.1 h.2⟩'
EQ_PROOF = ('Set.Subset.antisymm (subset_QK_of_maxCone_drive hmax hH2 hA) '
            '(QK_subset_of_products_cone_drive hH1 hadd hsmul hH2 hA)')
SIBLINGS = ['blockInvariant_of_drive', 'pairCone_eq_Q3_of_drive_exact', 'pairCone_eq_Q3_iff_drive_exact',
            'pairCone_eq_Q3_of_block', 'pairCone_eq_Q3_iff_block', 'pairCone_eq_Q3_of_drive',
            'subset_Q3_of_pure_dual', 'Q3_subset_of_pure', 'pairCone_eq_Q3_iff_drive']
# landed objects at D: (file, line, declaration head); their blobs are D's at E
LP = 'verification/lean-mathlib/OIBridge/'
LANDED = [
    (LP + 'CompositeDimension.lean', 97, 'abbrev W '), (LP + 'CompositeDimension.lean', 100, 'def hom '),
    (LP + 'CompositeDimension.lean', 112, 'def homMap '), (LP + 'CompositeDimension.lean', 161, 'def prodState '),
    (LP + 'CompositeDimension.lean', 167, 'noncomputable def ehom '),
    (LP + 'CompositeDimension.lean', 186, 'def maxCone '), (LP + 'CompositeDimension.lean', 198, 'def actT '),
    (LP + 'CompositeDimension.lean', 741, 'def sgn '), (LP + 'CompositeDimension.lean', 744, 'def pc '),
    (LP + 'CompositeDimension.lean', 751, 'def pt '), (LP + 'CompositeDimension.lean', 775, 'def cnot '),
    (LP + 'KInfFoundations.lean', 116, 'def IsEffectOn '),
    (LP + 'KInfFoundations.lean', 386, 'noncomputable def rotLin '),
    (LP + 'KInfFoundations.lean', 416, 'noncomputable def cycEquiv '),
    (LP + 'TransitiveBody.lean', 518, 'def eball '), (LP + 'EqvK2Schema.lean', 25, 'noncomputable def pauli '),
    (LP + 'EqvK2Schema.lean', 78, 'noncomputable def dict '), (LP + 'EqvK2Schema.lean', 239, 'def Q3 '),
    (LP + 'EqvK2Block.lean', 190, 'def bloch '), (LP + 'EqvK2Generation.lean', 204, 'theorem dict_cnot_block '),
    (LP + 'EqvK2Generation.lean', 280, 'theorem exists_unit_sqrt '),
    (LP + 'EqvK2Generation.lean', 323, 'theorem su_euler '), (LP + 'EqvK2Converse.lean', 87, 'theorem tokMat_rot '),
    (LP + 'EqvK2Converse.lean', 106, 'def cycMat '), (LP + 'EqvK2Converse.lean', 133, 'theorem tokMat_cyc '),
    (LP + 'EqvK2MaxCone.lean', 153, 'theorem pairCone_eq_Q3_of_drive_maxCone '),
]
PHRASES = ['OI supplies', 'sources the k-token', 'local tomography is derived', 'is invariant under every unitary',
           'Kn is discharged', 'Kn is closed', 'K2 is closed', 'OI implies QM', 'kernel proof of']
ALLOWED_AXIOMS = {'propext', 'Classical.choice', 'Quot.sound'}
PROBE_CODES = ['DICT3', 'PRODUCT3', 'REACH3', 'DEMUX3', 'ADJOINT3', 'QUANTUM3', 'ZERO3', 'SCALE3', 'ADD3',
               'SHIFT3', 'SEP3', 'ORBIT3', 'CUT3', 'SLICE3']
PROBE_N = 3196
PROBE_MUTATIONS = ['trace-factor: DICT3', 'adjoint: ADJOINT3', 'shift-sign: SHIFT3', 'group-below-168: ORBIT3',
                   'cut-direction: CUT3']
FAMILY = {"name": "conditional k-token cone theorem: products, cone closure, the k-fold maxCone bound and CNOT plus rotation/cyclic invariance give the PSD cone of the k-fold Pauli dictionary (round KTOKEN-MAXCONE-1, reconstruction)", "modules": ["KTokenMaxCone"], "status": "kernel-only", "manuscript": [], "note": "Conditional k-token infrastructure on WK k = (Fin k → Fin 4) → ℝ. subset_QK_of_maxCone_drive uses the k-fold maxCone bound, CNOT into later tokens and the rotation/cyclic actions off the first token for the upper inclusion; QK_subset_of_products_cone_drive uses products of eball 3 states, addition, nonnegative scaling and the same actions for the lower. kCone_eq_QK_of_drive_maxCone assembles equality; kCone_eq_QK_iff_drive_maxCone has the witnesses driveInvariantK_of_eq_QK and kCone_eq_QK_of_drive_maxCone. pairCone_eq_Q3_of_kToken proves the statement of EqvK2MaxCone.pairCone_eq_Q3_of_drive_maxCone from the k-token theorem; EqvK2MaxCone is not imported. This family is carried by no manuscript. The k-token carrier, products, test validity and the invariance remain explicit premises; arbitrary unitary invariance and Kn are not asserted. Record: verification/programmes/oi-qm/reconstruction/round-ktoken-maxcone-1/."}
ROOT_ANCHOR = 'import OIBridge.TurnpikePremiseOrientation\n'
ROOT_LINE = 'import OIBridge.KTokenMaxCone\n'
SHARD = """
  probes_ktokenmaxcone1:
    name: Numerical probes / KTOKEN-MAXCONE-1 k = 3 exact layer
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: k = 3 exact witnesses and probe mutations
        run: python3 -I -B verification/lean/ktoken_maxcone1_probe.py --self-test

      - name: Native control mutation tests
        run: python3 -I -B verification/programmes/oi-qm/reconstruction/round-ktoken-maxcone-1/controls.py --self-test
"""
A3_STEP = """
      - name: KTOKEN-MAXCONE-1 check A3 (k = 2 statement identity and dependency walk, with mutations)
        if: ${{ !cancelled() }}
        working-directory: verification/lean-mathlib
        run: lake env python3 -I -B ../programmes/oi-qm/reconstruction/round-ktoken-maxcone-1/checks/run_checks.py run
"""
GATE_STEP = '      - name: Release gate\n        run: python3 tools/release_gate.py\n'
BG2_LAST = ('      - name: BG-2 control mutation tests\n        run: python3 -I -B verification/programmes/oi-qm/'
            'reconstruction/round-bg-2-premise-orientation/controls.py --self-test\n')
SPLICES = [
    (GATE_STEP, GATE_STEP + A3_STEP),
    (BG2_LAST, BG2_LAST + SHARD),
    ('probes_bg2, probes_a42_witness', 'probes_bg2, probes_ktokenmaxcone1, probes_a42_witness'),
    ('          BG2_RESULT: ${{ needs.probes_bg2.result }}\n',
     '          BG2_RESULT: ${{ needs.probes_bg2.result }}\n'
     '          KTOKENMAXCONE1_RESULT: ${{ needs.probes_ktokenmaxcone1.result }}\n'),
    ('          echo "bg2=${BG2_RESULT}"\n',
     '          echo "bg2=${BG2_RESULT}"\n          echo "ktokenmaxcone1=${KTOKENMAXCONE1_RESULT}"\n'),
    ('          test "${BG2_RESULT}" = success\n',
     '          test "${BG2_RESULT}" = success\n          test "${KTOKENMAXCONE1_RESULT}" = success\n'),
]
REQUIRED = ['C1', 'C2', 'S1', 'S2', 'S3', 'S4', 'W', 'I', 'J', 'P', 'R', 'G', 'T']
POSITIVE = ['KTOKEN-MAXCONE-INCLUSIONS-PROVED', 'KTOKEN-MAXCONE-EQ-PROVED', 'KTOKEN-MAXCONE-PAIR-RECOVERED',
            'KTOKEN-MAXCONE-K3-EXACT', 'KTOKEN-MAXCONE-1-READ']
STAGES = ('E', 'S1')
SELF_CHECKS = 38  # set to the number of self-checks; a dropped self-check fails the count
FIXED_RECORD = {'preregistration.md', 'controls.py', 'checks/KTokenPairCheck.lean', 'checks/run_checks.py'}

FAIL = []
RAN = []


def report(name, ok, detail=''):
    print(('PASS ' if ok else 'FAIL ') + name + (('  ' + detail) if detail else ''))
    RAN.append(name)
    if not ok:
        FAIL.append(name)
    return bool(ok)


def git(*args):
    return subprocess.run(['git'] + list(args), capture_output=True, text=True, check=True).stdout


def show(commit, path):
    r = subprocess.run(['git', 'show', '%s:%s' % (commit, path)], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def blob(commit, path):
    r = subprocess.run(['git', 'rev-parse', '%s:%s' % (commit, path)], capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else None


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


# ---------------------------------------------------------------- the frozen surface, from the preregistration

def frozen_block(prereg):
    m = re.search(r'## The statement surface.*?```lean\n(.*?)```', prereg, re.S)
    return m.group(1) if m else ''


DECL = re.compile(r"^(?:noncomputable )?(def|abbrev|theorem)\s+([A-Za-z_][\w.']*)", re.M)


def decls(text):
    """{name: (kind, surface, body)}: a theorem's surface stops at its first ':='; a def's or an abbrev's
    surface is its whole text up to the next blank line, docstring or declaration."""
    out, lines = {}, text.split('\n')
    starts = [(i, m) for i, l in enumerate(lines) for m in [DECL.match(l)] if m]
    for k, (i, m) in enumerate(starts):
        end = starts[k + 1][0] if k + 1 < len(starts) else len(lines)
        chunk = lines[i:end]
        kind, name = m.group(1), m.group(2)
        if kind == 'theorem':
            whole = '\n'.join(chunk)
            surface, _, body = whole.partition(':=')
        else:
            buf = []
            for l in chunk:
                if l.strip() == '' or (buf and (l.startswith('/--') or l.startswith('#'))):
                    break
                buf.append(l)
            surface, body = '\n'.join(buf), ''
        if name in out:
            out[name] = ('dup', '', '')
        else:
            out[name] = (kind, flat(surface), body)
    return out


def order(text, names):
    pos = {m.group(2): m.start() for m in DECL.finditer(text)}
    return all(n in pos for n in names) and [pos[n] for n in names] == sorted(pos[n] for n in names)


def governed(prereg):
    m = re.search(r'```v3-governed-paths\n(.*?)```', prereg, re.S)
    return [ln.split()[-1] for ln in m.group(1).strip().splitlines()] if m else []


def frozen_blobs(prereg):
    m = re.search(r'\*\*Frozen execution blobs\.\*\*.*?\n\n(\|.*?)\n\n', prereg, re.S)
    rows = re.findall(r'^\| `([^`]+)` \| `([0-9a-f]{40})` \|$', m.group(1), re.M) if m else []
    return dict(rows)


def evidence_pins(prereg):
    """{record-relative path: sha256 or None (pending)} from the retained-evidence table."""
    m = re.search(r'\*\*Retained evidence \(§A\.42\)\.\*\*.*?\n\n(\|.*?)\n\n', prereg, re.S)
    rows = re.findall(r'^\| `(evidence/[^`]+)` \| (`[0-9a-f]{64}`|pending[^|]*) \|', m.group(1), re.M) if m else []
    return {p: (h.strip('`') if h.startswith('`') else None) for p, h in rows}


# ---------------------------------------------------------------- the controls

def s1(module, frozen):
    code = uncomment(module)
    lines = [l.strip() for l in code.splitlines() if l.strip()]
    ok = [l for l in lines if l.startswith('import ')] == IMPORTS and lines[0] == IMPORTS[0]
    ok &= lines.count(OPEN_NS) == BLOCKS and lines.count(END_NS) == BLOCKS and lines[-1] == END_NS
    ok &= all(lines.count(s) == 1 for s in SCOPED)
    want, have = decls(frozen), decls(code)
    ok &= list(want) == NAMES
    ok &= all(n in have and have[n][:2] == want[n][:2] for n in NAMES) and order(code, NAMES)
    ok &= [l for l in lines if l.startswith('#print')] == ['#print axioms ' + n for n in PRINTS]
    ok &= not any(re.search(r'\b%s\b' % t, code) for t in ('sorry', 'admit', 'native_decide', 'axiom',
                                                             'implemented_by', 'extern'))
    return bool(ok)


def pair_identity(module, pair):
    """The recovery's statement equals the landed pair theorem's (EqvK2MaxCone.lean:153-160) but for its name,
    after the qualification `OIBridge.` is dropped; the kernel-level identity is check A3's."""
    have = decls(uncomment(module)).get('pairCone_eq_Q3_of_kToken', ('', '', ''))[1]
    want = decls(uncomment(pair)).get('pairCone_eq_Q3_of_drive_maxCone', ('', '', ''))[1]
    norm = lambda s: s.replace('OIBridge.', '').split(None, 2)[2] if s.count(' ') >= 2 else ''
    return bool(have) and bool(want) and norm(have) == norm(want)


def s3(module):
    code = uncomment(module)
    d = decls(code)
    iff, eq, rec = (flat(d.get(n, ('', '', ''))[2]) for n in
                    ('kCone_eq_QK_iff_drive_maxCone', 'kCone_eq_QK_of_drive_maxCone', 'pairCone_eq_Q3_of_kToken'))
    ok = iff == IFF_PROOF and EQ_PROOF in eq
    rec_body = rec.split('#eval')[0]
    ok &= 'kCone_eq_QK_of_drive_maxCone' in rec_body and 'EqvK2MaxCone' not in rec_body
    ok &= not any(re.search(r'\b%s\b' % s, rec_body) for s in SIBLINGS)
    ok &= module.count(EVAL) == 1
    ok &= code.replace(uncomment(EVAL), '').count('EqvK2MaxCone') == 0
    return bool(ok)


def s4(texts):
    return [(name, p) for name, t in texts for p in PHRASES if t and p.lower() in t.lower()]


def header_of(module):
    m = re.match(r'\s*/-(.*?)-/', module, re.S)
    return m.group(1) if m else ''


def workflow(base):
    text = base
    for old, new in SPLICES:
        if text.count(old) != 1:
            return None
        text = text.replace(old, new)
    return text


def root_expected(base):
    return base.replace(ROOT_ANCHOR, ROOT_ANCHOR + ROOT_LINE) if base.count(ROOT_ANCHOR) == 1 else None


def registry_ok(base, head):
    try:
        want = json.loads(base)
        want['families'].append(FAMILY)
        return json.loads(head) == want
    except (ValueError, KeyError, TypeError):
        return False


def g(diff_lines, paths):
    bad = []
    for ln in diff_lines:
        if not ln.strip():
            continue
        status, path = ln.split('\t', 1)
        inside = any(path == p or (p.endswith('/') and path.startswith(p)) for p in paths)
        if not inside or path == LEGACY:
            bad.append(ln)
    return bad


def record_ok(names, pins, required):
    rel = {n[len(RDIR):] for n in names if n.startswith(RDIR)}
    want = FIXED_RECORD | set(pins) | ({'result.md'} if required else set())
    extra = {r for r in rel - want if not r.startswith('amendments/') and not r.startswith('evidence/f-run/')}
    return not (want - rel) and not extra


def s2(E):
    ok = True
    for path, line, head in LANDED:
        bd, be = blob(D, path), blob(E, path)
        text = (show(E, path) or '').splitlines()
        found = len(text) >= line and text[line - 1].startswith(head)
        ok &= bd is not None and bd == be and found
        if not (bd == be and found):
            print('      S2 miss: %s:%d %r (blob at D %s, at E %s)' % (path, line, head, bd, be))
    return bool(ok)


def check(E, F, stage='E'):
    """Runs and prints every static control. Each control records its own outcome when it runs; the result maps
    exactly the codes that recorded one ({code: passed}). A code that never ran is absent, and verdict and main
    treat an absent code as failed. stage 'E' requires the result note; stage 'S1' does not."""
    if stage not in STAGES:
        raise ValueError('check: unknown stage %r (expected one of %s)' % (stage, ', '.join(STAGES)))
    outcomes = {}

    def record(code, name, ok, detail=''):
        ok = bool(ok)
        report(code + ' ' + name, ok, detail)
        outcomes[code] = outcomes.get(code, True) and ok

    at_e = stage == 'E'
    prereg_F, prereg_E = show(F, PREREG), show(E, PREREG)
    module = show(E, MODULE) or ''
    result = show(E, RESULT)
    record('C1', 'the preregistration at E is the one at F', prereg_F is not None and prereg_F == prereg_E)
    fb = frozen_blobs(prereg_F or '')
    bad = [p for p, b in fb.items() if blob(E, p) != b]
    record('C2', 'the frozen execution blobs at E', len(fb) == 5 and not bad, str(bad) if bad else '')
    frozen = frozen_block(prereg_F or '')
    record('S1', 'surface: preamble, the frozen declarations in order, the %d prints' % len(PRINTS),
           s1(module, frozen) and pair_identity(module, show(E, PAIR) or ''))
    record('S2', 'the landed objects resolve at D\'s blobs and lines', s2(E))
    record('S3', 'the witnesses of the equivalence, the recovery\'s proof, the absence check', s3(module))
    hits = s4([('module header', header_of(module)), ('result note', result)])
    present = bool(header_of(module).strip()) and (result is not None or not at_e)
    record('S4', 'the module header (and, at E, the result note) present, with no excluded phrase',
           present and not hits, str(hits) if hits else ('' if present else 'header or result note absent'))
    wd, we = workflow(show(D, WORKFLOW) or ''), show(E, WORKFLOW)
    record('W', 'the workflow at E is D\'s with the frozen splices', wd is not None and we is not None and we == wd)
    rd, re_ = root_expected(show(D, ROOT) or ''), show(E, ROOT)
    record('I', 'one import line', rd is not None and re_ is not None and re_ == rd)
    record('J', 'one census family', registry_ok(show(D, REGISTRY), show(E, REGISTRY)))
    pins = evidence_pins(prereg_F or '')
    pend = [p for p, h in pins.items() if h is None]
    badpin = [p for p, h in pins.items()
              if h and (show(E, RDIR + p) is None or hashlib.sha256(show(E, RDIR + p).encode()).hexdigest() != h)]
    record('P', 'retained evidence pinned at F is present at E with its digest', bool(pins) and not pend and not badpin,
           str(pend + badpin) if pend or badpin else '%d pins' % len(pins))
    names = git('ls-tree', '-r', '--name-only', E, '--', RDIR).splitlines()
    record('R', 'the record directory holds exactly the frozen files', record_ok(names, pins, at_e))
    diff = [x for x in git('diff', '--no-renames', '--name-status', D, E).splitlines() if x.strip()]
    gp = governed(prereg_F or '')
    badg = g(diff, gp)
    record('G', 'every change from D to E lies in the governed paths; the legacy manifest untouched',
           len(gp) == 7 and diff and not badg, str(badg) if badg else '%d paths' % len(diff))
    fdelta = [x for x in git('diff', '--name-only', D, F).splitlines() if x.strip()]
    lin = git('rev-list', '--parents', F + '..' + E).splitlines()
    record('T', 'delta(D, F) is the control plane; the execution is linear after F',
           all(p == PREREG or p.startswith(RDIR + 'amendments/') for p in fdelta) and PREREG in fdelta
           and lin and all(len(x.split()) == 2 for x in lin))
    return outcomes


def passed(results):
    """True only when every REQUIRED code recorded an explicit True; absent or non-bool means failed."""
    return isinstance(results, dict) and all(results.get(c) is True for c in REQUIRED)


def run_probe(E, *args):
    with tempfile.TemporaryDirectory() as tmp:
        arch = subprocess.run(['git', 'archive', E, PROBE], capture_output=True, check=True).stdout
        subprocess.run(['tar', '-x', '-C', tmp], input=arch, check=True)
        r = subprocess.run([sys.executable, '-I', '-B', os.path.join(tmp, PROBE)] + list(args),
                           capture_output=True, text=True)
        return r.returncode, r.stdout, r.stderr


def probe_ok(rc, out, err, selftest):
    ok = rc == 0 and not err and 'FAIL' not in out
    ok &= all(re.search(r'^PASS %s \(\d+\)$' % c, out, re.M) for c in PROBE_CODES)
    ok &= 'checks: %d, failures: 0' % PROBE_N in out and out.rstrip().endswith('VERDICT KTOKEN-K3-EXACT')
    if selftest:
        ok &= all(('REJECTED ' + m) in out for m in PROBE_MUTATIONS) and 'mutations: 5 rejected, 0 accepted' in out
    return bool(ok)


def axioms_from(log):
    rep = {}
    for m in re.finditer(r"'%s\.([\w']+)' depends on axioms: \[([^\]]*)\]" % re.escape(NS), log):
        rep[m.group(1)] = {a.strip() for a in m.group(2).split(',') if a.strip()}
    for m in re.finditer(r"'%s\.([\w']+)' does not depend on any axioms" % re.escape(NS), log):
        rep[m.group(1)] = set()
    return rep


def cells(static_s1, static_s2, static_s3, ax, log, exact):
    clean = lambda n: n in ax and ax[n] <= ALLOWED_AXIOMS
    nosorry = 'sorryAx' not in log and 'Lean.ofReduceBool' not in log
    base = static_s1 and static_s2 and nosorry and all(clean(n) for n in SUPPORT)
    incl = base and all(clean(n) for n in INCL)
    eq = base and static_s3 and all(clean(n) for n in INCL + EQ)
    pair = base and static_s3 and all(clean(n) for n in PAIRSET + ['kCone_eq_QK_of_drive_maxCone']) \
        and A3_LOG in log and EVAL_LOG in log
    return incl, eq, pair, exact


def verdict(E, F, axlog, check_fn=None, probe_fn=None):
    """Every positive token is gated on every required static control: if any control in REQUIRED fails or is
    not reported, the failed controls are printed, the probe is not run, every cell prints NOT-ESTABLISHED,
    the round prints NOT-READ and the result is False. check_fn and probe_fn default to check and run_probe."""
    results = (check_fn or check)(E, F)
    results = results if isinstance(results, dict) else {}
    failed = [c for c in REQUIRED if results.get(c) is not True]
    if failed:
        print('STATIC CONTROLS FAILED: ' + ', '.join(failed))
        print('probe not run and axiom reports not read: a required static control failed')
        incl = eq = pair = exact = False
    else:
        rc, out, err = (probe_fn or run_probe)(E, '--self-test')
        print(out.rstrip())
        log = open(axlog, encoding='utf-8', errors='replace').read() if axlog else ''
        ax = axioms_from(log)
        incl, eq, pair, exact = cells(True, True, True, ax, log, probe_ok(rc, out, err, True))
        print('axiom reports read: %d of %d prints' % (len([p for p in PRINTS if p in ax]), len(PRINTS)))
    print('TOKEN Q-INCL  %s' % ('KTOKEN-MAXCONE-INCLUSIONS-PROVED' if incl else 'KTOKEN-MAXCONE-INCLUSIONS-NOT-ESTABLISHED'))
    print('TOKEN Q-EQ    %s' % ('KTOKEN-MAXCONE-EQ-PROVED' if eq else 'KTOKEN-MAXCONE-EQ-NOT-ESTABLISHED'))
    print('TOKEN Q-PAIR  %s' % ('KTOKEN-MAXCONE-PAIR-RECOVERED' if pair else 'KTOKEN-MAXCONE-PAIR-NOT-ESTABLISHED'))
    print('TOKEN Q-EXACT %s' % ('KTOKEN-MAXCONE-K3-EXACT' if exact else 'KTOKEN-MAXCONE-K3-NOT-ESTABLISHED'))
    print('KTOKEN-MAXCONE-1-NOT-READ (static controls failed: %s)' % ', '.join(failed) if failed
          else 'KTOKEN-MAXCONE-1-READ')
    return not failed


def verdict_regression():
    """Through verdict() itself: each required static control failing alone, a control left unreported, and
    the all-clean case. Returns a list of problems."""
    log = '\n'.join("'%s.%s' depends on axioms: [propext, Classical.choice, Quot.sound]" % (NS, p) for p in PRINTS)
    log += '\n' + EVAL_LOG + '\n' + A3_LOG + '\n'
    pout = '\n'.join('PASS %s (1)' % c for c in PROBE_CODES) + '\nchecks: %d, failures: 0\n' % PROBE_N + \
        '\n'.join('REJECTED ' + m for m in PROBE_MUTATIONS) + '\nmutations: 5 rejected, 0 accepted\n' \
        'VERDICT KTOKEN-K3-EXACT\n'
    probe = lambda E, *a: (0, pout, '')
    problems = []
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, 'bridge.log')
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(log)

        def run(results):
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                ok = verdict('E', 'F', path, check_fn=lambda E, F: dict(results), probe_fn=probe)
            return ok, buf.getvalue()
        clean = {c: True for c in REQUIRED}
        ok, out = run(clean)
        if not ok or not all(t in out for t in POSITIVE):
            problems.append('all-clean case: result %s, positive tokens %s' % (ok, [t for t in POSITIVE if t in out]))
        cases = [(c, dict(clean, **{c: False})) for c in REQUIRED]
        cases.append(('C2 unreported', {c: True for c in REQUIRED if c != 'C2'}))
        for name, results in cases:
            ok, out = run(results)
            leaked = [t for t in POSITIVE if t in out]
            if ok or leaked or 'STATIC CONTROLS FAILED: ' + name.split()[0] not in out:
                problems.append('%s alone failing: result %s, positive tokens printed %s' % (name, ok, leaked))
    return problems, len(REQUIRED) + 2


# ---------------------------------------------------------------- self-test

def git_blob_id(text):
    b = text.encode('utf-8')
    return hashlib.sha1(b'blob %d\0' % len(b) + b).hexdigest()


def fake_repo(root):
    """An in-memory D, F, E built from the live round files, for the end-to-end controls test (no git history
    needed): E holds the live execution files, a filled copy of the preregistration's evidence pins, two
    synthetic evidence files and a synthetic result note; D is E with the frozen splices undone; F is D plus the
    preregistration. Synthetic content is labelled as such and is not run evidence."""
    rd = lambda p: open(os.path.join(root, p), encoding='utf-8').read()
    E = {p: rd(p) for p in {MODULE, PAIR, PROBE, CHECKFILE, RUNNER, CONTROLS, WORKFLOW, ROOT, REGISTRY}
         | {path for path, _, _ in LANDED}}
    prereg = rd(PREREG)
    for path in evidence_pins(prereg):
        # Synthetic evidence only: the fixture never reads a retained evidence file. Each pin, pending or filled in
        # the live preregistration, is replaced in the fixture's own copy by the digest of a labelled synthetic file.
        body = '{"synthetic": "controls self-test fixture, not run evidence", "path": "%s"}\n' % path
        E[RDIR + path] = body
        prereg, n = re.subn(r'(\| `%s` \| )(?:pending[^|]*|`[0-9a-f]{64}` )\|' % re.escape(path),
                            lambda m: m.group(1) + '`%s` |' % hashlib.sha256(body.encode()).hexdigest(), prereg)
        if n != 1:
            return None
    E[PREREG] = prereg
    E[RESULT] = '# KTOKEN-MAXCONE-1 result (self-test fixture)\n\nNo claim.\n'
    Dm = {p: E[p] for p in {PAIR} | {path for path, _, _ in LANDED}}
    w = E[WORKFLOW]
    for old, new in reversed(SPLICES):
        if w.count(new) != 1:
            return None
        w = w.replace(new, old)
    Dm[WORKFLOW] = w
    if E[ROOT].count(ROOT_ANCHOR + ROOT_LINE) != 1:
        return None
    Dm[ROOT] = E[ROOT].replace(ROOT_ANCHOR + ROOT_LINE, ROOT_ANCHOR)
    reg = json.loads(E[REGISTRY])
    if reg['families'][-1] != FAMILY:
        return None
    reg['families'].pop()
    Dm[REGISTRY] = json.dumps(reg, indent=2, ensure_ascii=False) + '\n'
    Fm = dict(Dm)
    Fm[PREREG] = E[PREREG]
    return {'D': Dm, 'F': Fm, 'E': E}


def install_fake(mod, repo):
    key = lambda c: 'D' if c == D else c
    mod.show = lambda c, p: repo[key(c)].get(p)
    mod.blob = lambda c, p: git_blob_id(repo[key(c)][p]) if p in repo[key(c)] else None

    def fgit(*args):
        if args[0] == 'ls-tree':
            return '\n'.join(sorted(p for p in repo[key(args[3])] if p.startswith(args[5])))
        if args[:3] == ('diff', '--no-renames', '--name-status'):
            a, b = repo[key(args[3])], repo[key(args[4])]
            return '\n'.join(('A\t' if p not in a else 'M\t') + p for p in sorted(b) if a.get(p) != b[p])
        if args[:2] == ('diff', '--name-only'):
            a, b = repo[key(args[2])], repo[key(args[3])]
            return '\n'.join(p for p in sorted(b) if a.get(p) != b[p])
        if args[0] == 'rev-list':
            return 'E S1\nS1 C1\nC1 F\n'
        raise ValueError('fake git: unsupported ' + ' '.join(args))
    mod.git = fgit


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


def end_to_end(src, repo, axlog):
    """check() then verdict() of the module built from src, on the fake repo; returns (ok, output, probe_calls)."""
    mod = types.ModuleType('controls_e2e')
    mod.__file__ = __file__
    exec(compile(src, 'controls_e2e', 'exec'), mod.__dict__)
    install_fake(mod, repo)
    pout = '\n'.join('PASS %s (1)' % c for c in PROBE_CODES) + '\nchecks: %d, failures: 0\n' % PROBE_N + \
        '\n'.join('REJECTED ' + m for m in PROBE_MUTATIONS) + '\nmutations: 5 rejected, 0 accepted\n' \
        'VERDICT KTOKEN-K3-EXACT\n'
    calls = []

    def probe(E, *a):
        calls.append(E)
        return 0, pout, ''
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        ok = mod.verdict('E', 'F', axlog, probe_fn=probe)
    return ok, buf.getvalue(), len(calls)


def e2e_mutations(root):
    """The real check(), unmutated and with each REQUIRED code's record call removed, run through verdict()."""
    src = open(__file__, encoding='utf-8').read()
    repo = fake_repo(root)
    if repo is None:
        return ['fake repo: the live workflow, root or registry lacks the frozen splices'], 0
    problems = []
    log = '\n'.join("'%s.%s' depends on axioms: [propext, Classical.choice, Quot.sound]" % (NS, p) for p in PRINTS)
    log += '\n' + EVAL_LOG + '\n' + A3_LOG + '\n'
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, 'bridge.log')
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(log)
        ok, out, calls = end_to_end(src, repo, path)
        if not ok or calls != 1 or not all(t in out for t in POSITIVE) or 'FAIL ' in out:
            problems.append('unmutated: result %s, probe calls %d, positive %s, failures %s' % (
                ok, calls, [t for t in POSITIVE if t in out], re.findall(r'^FAIL .*$', out, re.M)))
        for code in REQUIRED:
            ok, out, calls = end_to_end(drop_record(src, code), repo, path)
            leaked = [t for t in POSITIVE if t in out]
            m = re.search(r'^STATIC CONTROLS FAILED: (.*)$', out, re.M)
            named = m is not None and code in m.group(1).split(', ')
            if ok or leaked or not named or calls:
                problems.append('%s record removed: result %s, positive printed %s, named failed %s, probe calls %d'
                                % (code, ok, leaked, named, calls))
        # absence cases on the unmutated check(): a control must fail when its inputs are absent
        def without(spec):
            r = {k: dict(v) for k, v in repo.items()}
            for c, pth in spec:
                r[c].pop(pth, None)
            return r
        ev = sorted(x for x in repo['E'] if x.startswith(RDIR + 'evidence/'))[:1]

        def pinned(value):
            # F's and E's preregistration with the first pin set to `value`: a pending pin, or a digest that is not
            # the evidence file's. The production check must reject both.
            r = {k: dict(v) for k, v in repo.items()}
            if not ev:
                return r
            rel = ev[0][len(RDIR):]
            for c in ('F', 'E'):
                r[c][PREREG] = re.sub(r'(\| `%s` \| )`[0-9a-f]{64}` \|' % re.escape(rel),
                                      lambda m: m.group(1) + value + ' |', r[c][PREREG], count=1)
            return r
        headerless = {k: dict(v) for k, v in repo.items()}
        headerless['E'][MODULE] = re.sub(r'\A\s*/-.*?-/\n', '', repo['E'][MODULE], count=1, flags=re.S)
        absences = [('workflow absent at D and E', ['W'], without([('D', WORKFLOW), ('E', WORKFLOW)])),
                    ('OIBridge.lean absent at D and E', ['I'], without([('D', ROOT), ('E', ROOT)])),
                    ('result note absent at E', ['S4', 'R'], without([('E', RESULT)])),
                    ('a pinned evidence file absent at E', ['P'], without([('E', e) for e in ev])),
                    ('a pin left pending at F', ['P'], pinned('pending (self-test)')),
                    ('a pin whose digest is not the file\'s', ['P'], pinned('`%s`' % hashlib.sha256(b'other').hexdigest())),
                    ('module header absent', ['S4'], headerless)]
        for name, codes, r in absences:
            ok, out, calls = end_to_end(src, r, path)
            m = re.search(r'^STATIC CONTROLS FAILED: (.*)$', out, re.M)
            named = m is not None and all(c in m.group(1).split(', ') for c in codes)
            if ok or calls or not named or any(t in out for t in POSITIVE):
                problems.append('%s: result %s, %s named %s, probe calls %d' % (name, ok, codes, named, calls))
    if passed({}) or passed({c: 1 for c in REQUIRED}) or not passed({c: True for c in REQUIRED}):
        problems.append('passed() accepts an empty or non-bool map, or rejects the all-True map')
    # an unknown stage is refused, not read as the laxer stage 1
    mod = types.ModuleType('controls_stage')
    mod.__file__ = __file__
    exec(compile(src, 'controls_stage', 'exec'), mod.__dict__)
    install_fake(mod, repo)
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            mod.check('E', 'F', 'e')
        problems.append('check() accepted the unknown stage \'e\'')
    except ValueError:
        pass
    return problems, len(REQUIRED) + 1 + 7 + 1 + 1


def in_decl(text, name, old, new):
    """Replace old by new once, inside the declaration `name` only."""
    m = re.search(r'^theorem %s\b' % re.escape(name), text, re.M)
    if not m:
        return text
    nxt = DECL.search(text, m.end())
    end = nxt.start() if nxt else len(text)
    chunk = text[m.start():end]
    return text[:m.start()] + chunk.replace(old, new, 1) + text[end:]


def self_test():
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.abspath(os.path.join(here, '..', '..', '..', '..', '..'))
    rd = lambda p: open(os.path.join(root, p), encoding='utf-8').read()
    prereg = open(os.path.join(here, 'preregistration.md'), encoding='utf-8').read()
    module, pairsrc = rd(MODULE), rd(PAIR)
    frozen = frozen_block(prereg)
    report('self: D agrees with the preregistration', ('D: ' + D) in prereg)
    gp = governed(prereg)
    report('self: governed paths parsed (7) and include the module, the probe and the record directory',
           len(gp) == 7 and MODULE in gp and PROBE in gp and RDIR in gp)
    report('self: the frozen block declares the %d names in order' % len(NAMES), list(decls(frozen)) == NAMES)
    report('self: the frozen-blob table names five paths', set(frozen_blobs(prereg)) ==
           {CONTROLS, MODULE, PROBE, CHECKFILE, RUNNER})
    pins = evidence_pins(prereg)
    report('self: the retained-evidence table parses', len(pins) >= 2,
           '%d rows, %d pending' % (len(pins), sum(h is None for h in pins.values())))
    report('self: %d prints, %d supporting' % (len(PRINTS), len(SUPPORT)), len(PRINTS) == 68 and len(set(PRINTS)) == 68)
    report('self: S1 accepts the module', s1(module, frozen))
    report('self: the recovery states the landed pair theorem', pair_identity(module, pairsrc))
    report('self: S3 accepts the module', s3(module))
    report('self: S4 finds nothing in the module header', not s4([('header', header_of(module))]))
    hA = '(hA : ∀ j : Fin k, (j : ℕ) ≠ 0 → ∀ t : ℝ, ∀ ω ∈ K,'
    muts = [
        ('hmax dropped from the upper inclusion', lambda t: in_decl(t, 'subset_QK_of_maxCone_drive',
            '    (hmax : K ⊆ maxConeK (OIBridge.TransitiveBody.eball 3))\n', '')),
        ('hadd dropped from the lower inclusion', lambda t: in_decl(t, 'QK_subset_of_products_cone_drive',
            '    (hadd : ∀ ω ∈ K, ∀ η ∈ K, ω + η ∈ K)\n', '')),
        ('the guard (j : ℕ) ≠ 0 removed', lambda t: in_decl(t, 'kCone_eq_QK_of_drive_maxCone',
            hA, '(hA : ∀ j : Fin k, ∀ t : ℝ, ∀ ω ∈ K,')),
        ('i < j replaced by i ≠ j', lambda t: in_decl(t, 'subset_QK_of_maxCone_drive',
            'i < j → ∀ ω ∈ K, cnotK', 'i ≠ j → ∀ ω ∈ K, cnotK')),
        ('K = QK k weakened to K ⊆ QK k', lambda t: in_decl(t, 'kCone_eq_QK_of_drive_maxCone',
            '    K = QK k :=', '    K ⊆ QK k :=')),
        ('an extra print', lambda t: t.replace('#print axioms pauliWord_apply\n',
                                               '#print axioms pauliWord_apply\n#print axioms pauliWord_apply\n', 1)),
        ('the classical instance made global', lambda t: t.replace('scoped instance carrierDecidableEq', 'instance carrierDecidableEq', 1)),
        ('a second import', lambda t: t.replace('import OIBridge.EqvK2Generation\n',
                                                'import OIBridge.EqvK2Generation\nimport OIBridge.EqvK2MaxCone\n', 1)),
    ]
    for name, f in muts:
        mt = f(module)
        report('self: S1 rejects the mutation: ' + name, mt != module and not s1(mt, frozen))
    rec_mut = module.replace('    K = Q3 := by\n  have hmem', '    K ⊆ Q3 := by\n  have hmem', 1)
    report('self: the pair identity rejects a recovery off EqvK2MaxCone.lean:153-160',
           rec_mut != module and not pair_identity(rec_mut, pairsrc))
    cite = module.replace('  ext ω\n  rw [← hmem, hK, ← mem_Q3_iff_pairCarrier]',
                          '  exact OIBridge.EqvK2MaxCone.pairCone_eq_Q3_of_drive_maxCone hH1 hadd hsmul hmax hH2 hA', 1)
    report('self: S3 rejects a recovery citing the pair theorem, and S1 does not', cite != module and not s3(cite)
           and s1(cite, frozen))
    sib = module.replace('  ext ω\n  rw [← hmem, hK, ← mem_Q3_iff_pairCarrier]',
                         '  have _x := blockInvariant_of_drive hH2 hA\n  ext ω\n  rw [← hmem, hK, ← mem_Q3_iff_pairCarrier]', 1)
    report('self: S3 rejects a recovery naming a sibling', sib != module and not s3(sib))
    swap = module.replace(IFF_PROOF, '⟨fun h => (driveInvariantK_of_eq_QK h), fun h => by exact absurd h (by simp)⟩', 1)
    report('self: S3 rejects an equivalence not built from its two witnesses', swap != module and not s3(swap))
    noeval = module.replace(EVAL, '', 1)
    report('self: S3 rejects the module without the absence check', noeval != module and not s3(noeval))
    report('self: S4 flags each excluded phrase', all(s4([('x', 'Here ' + p + ' at k tokens.')]) for p in PHRASES))
    # W, I, J on synthetic bases (the live shared files change after this round)
    wbase = 'jobs:\n' + GATE_STEP + '\n' + BG2_LAST + '\n' + \
        '    needs: [probes_bg2, probes_a42_witness]\n' + \
        '          BG2_RESULT: ${{ needs.probes_bg2.result }}\n' + \
        '          echo "bg2=${BG2_RESULT}"\n' + '          test "${BG2_RESULT}" = success\n'
    w = workflow(wbase)
    report('self: W applies its six splices once each', w is not None and w.count('probes_ktokenmaxcone1') == 3 and w.count('KTOKENMAXCONE1_RESULT') == 3
           and 'controls.py --self-test' in w and 'run_checks.py run' in w)
    report('self: W rejects a base lacking an anchor', workflow(wbase.replace('probes_bg2, probes_a42', 'x', 1)) is None)
    rbase = 'import OIBridge.EqvK2MaxCone\n' + ROOT_ANCHOR + '\nnamespace OIBridge\n'
    report('self: I adds exactly one line after the anchor', root_expected(rbase) == rbase.replace(
        ROOT_ANCHOR, ROOT_ANCHOR + ROOT_LINE) and root_expected(rbase + ROOT_ANCHOR) is None)
    jb = json.dumps({'families': [{'name': 'x'}]})
    jh = json.dumps({'families': [{'name': 'x'}, FAMILY]})
    report('self: J accepts the family and rejects a changed status', registry_ok(jb, jh) and not registry_ok(
        jb, jh.replace('kernel-only', 'current')))
    bad = g(['M\tpapers/GR.md', 'M\t' + LEGACY, 'M\tverification/ROADMAP.md', 'A\t' + MODULE, 'A\t' + RDIR + 'x'], gp)
    report('self: G flags a manuscript, the legacy manifest and the ROADMAP, and passes the module and the record',
           len(bad) == 3 and not any(MODULE in b or RDIR in b for b in bad))
    names = [RDIR + n for n in FIXED_RECORD | set(pins) | {'result.md'}]
    report('self: R accepts the frozen record and rejects an extra file', record_ok(names, pins, True)
           and not record_ok(names + [RDIR + 'extra.md'], pins, True) and not record_ok(names[1:], pins, True))
    log = '\n'.join("'%s.%s' depends on axioms: [propext, Classical.choice, Quot.sound]" % (NS, p) for p in PRINTS)
    log += '\n' + EVAL_LOG + '\n' + A3_LOG
    ax = axioms_from(log)
    report('self: the cells are positive on a clean synthetic log', all(cells(True, True, True, ax, log, True)))
    ax2 = dict(ax); ax2['pairCone_eq_Q3_of_kToken'] = ax['pairCone_eq_Q3_of_kToken'] | {'sorryAx'}
    c2 = cells(True, True, True, ax2, log, True)
    report('self: a sorryAx report on the recovery fails Q-PAIR alone', c2 == (True, True, False, True))
    c3 = cells(True, True, True, ax, log.replace(A3_LOG, ''), True)
    report('self: a missing A3 line fails Q-PAIR alone', c3 == (True, True, False, True))
    c4 = cells(True, True, True, {k: v for k, v in ax.items() if k != 'kCone_eq_QK_iff_drive_maxCone'}, log, True)
    report('self: a missing print fails Q-EQ', not c4[1])
    pout = '\n'.join('PASS %s (1)' % c for c in PROBE_CODES) + '\nchecks: %d, failures: 0\n' % PROBE_N + \
        '\n'.join('REJECTED ' + m for m in PROBE_MUTATIONS) + '\nmutations: 5 rejected, 0 accepted\nVERDICT KTOKEN-K3-EXACT\n'
    report('self: the probe rule accepts the frozen output shape and rejects N, a missing code and stderr',
           probe_ok(0, pout, '', True) and not probe_ok(0, pout.replace(str(PROBE_N), '3195'), '', True)
           and not probe_ok(0, pout.replace('PASS SLICE3', 'PASS SLICE'), '', True) and not probe_ok(0, pout, 'x', True))
    problems, n = verdict_regression()
    report('self: verdict() prints no positive token when any one of the %d required static controls fails or is '
           'unreported, and prints all of them when every control passes (%d cases)' % (len(REQUIRED), n),
           not problems, '; '.join(problems))
    problems, n = e2e_mutations(root)
    report('self: the real check() with any one control\'s record call removed, run through verdict(), fails, names '
           'that control, prints no positive token and never runs the probe; unmutated, it passes (%d cases)' % n,
           not problems, '; '.join(problems))
    selfs = len([r for r in RAN if r.startswith('self:')]) + 1
    report('self: %d self-checks ran, as frozen (%d)' % (selfs, SELF_CHECKS), selfs == SELF_CHECKS)
    return not FAIL


def main(argv):
    if argv[:1] == ['--self-test']:
        ok = self_test()
    elif argv[:1] == ['check'] and len(argv) >= 4 and argv[2] == '--freeze':
        stage = argv[argv.index('--stage') + 1] if '--stage' in argv else 'E'
        ok = passed(check(argv[1], argv[3], stage))
    elif argv[:1] == ['verdict'] and len(argv) >= 4 and argv[2] == '--freeze':
        ax = argv[argv.index('--axioms') + 1] if '--axioms' in argv else None
        ok = verdict(argv[1], argv[3], ax)
    else:
        print(__doc__)
        return 2
    print('controls: %s (%d failure(s))' % ('OK' if ok else 'FAILED', len(FAIL)))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
