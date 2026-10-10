#!/usr/bin/env python3
"""controls.py -- round KT4-PREM-1's own contracts, frozen with the preregistration beside it.

Imports nothing from the repository and changes nothing in it. Reads D and the commit under check through git, and
embeds every frozen text it compares against: the probe blob, the workflow edit, the landed texts the round cites at
D, the cell rules, the earned reading, the non-inference rule and the phrase list.

  controls.py check <commit> [--freeze F]   the execution at <commit> against D (and, with F, the preregistration
                                            unchanged from F, and F = D plus the preregistration alone)
  controls.py verdict <commit>              run the probe of <commit>'s tree and print one outcome per cell
  controls.py --self-test                   every mutation control must fail with its named code; the positive
                                            controls must pass

Exit 1 on any failure.
"""
import os
import re
import subprocess
import sys
import tempfile
import textwrap

D = 'bcbc516fe78eb7aa303a41e7bc9cc106dd63bd58'
RDIR = 'verification/programmes/oi-qm/reconstruction/round-kt4-prem-1-premise-audit/'
PREREG = RDIR + 'preregistration.md'
CONTROLS = RDIR + 'controls.py'
RESULT = RDIR + 'result.md'
RECEIPT = 'verification/receipts/KT4-PREM-1.json'
PROBE = 'verification/lean/kt4_prem1_probe.py'
PROBE_BLOB = '5609d96a9886d5d8548c0322e084849e700ba72b'
WORKFLOW = '.github/workflows/verify.yml'
LEAN = 'verification/lean-mathlib/OIBridge/'
PROBE_SOURCES = (LEAN + 'CompositeDimension.lean', LEAN + 'K2Guard.lean')
PROBE_SUMMARY = 'kt4_prem1_probe: OK -- 79 checks'

# ---------------------------------------------------------------------------------------------------- the cells
S0 = ['S0.sgn', 'S0.pc', 'S0.pt', 'S0.phiW', 'S0.idW', 'S0.chainW', 'S0.reflY']
DICT = ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7']
CARRIER = ['H%d' % i for i in range(1, 11)]
CC = ['X1', 'X2', 'X3', 'X4']
CELLS = [
    ('Q1-CL', 'CLOSEDNESS-FOIL-VERIFIED',
     S0 + DICT + CARRIER + ['F0', 'F1', 'F2', 'F3', 'F2v', 'F2s', 'M_cl.1', 'M_cl.5', 'M_cl.6', 'M_cl.7', 'M_cl.8',
                            'M_cl.9', 'M_cl.10', 'M_cl.11', 'M_cl.12'] + CC),
    ('Q1-MAX', 'MAXCONE-MODEL-VERIFIED',
     S0 + DICT + CARRIER + ['F4', 'F5', 'F6', 'M_max.2', 'M_max.3', 'M_max.4', 'M_max.6', 'X6'] + CC),
    ('Q1-MAP', 'COUNTERMODEL-MATRIX-VERIFIED',
     S0 + DICT + CARRIER + ['F7', 'F8', 'F9', 'F10', 'M_D.1', 'M_D.2', 'M_refl.1', 'M_id.1', 'M_class.1', 'M_class.2',
                            'M_class.3', 'M_class.4', 'M_mix.1', 'M_int.1', 'M_int.2', 'T1', 'T2', 'T3', 'T4', 'X5']
     + CC),
    ('Q1-NEC', 'CLASSIFICATION-STEPS-VERIFIED',
     S0 + ['D1', 'D7', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'M_max.4'] + CC),
    ('Q2', 'PAIR-ROUTE-GAP-VERIFIED', S0 + ['I1', 'I2', 'M_cl.7', 'M_cl.8', 'M_cl.9', 'M_max.3', 'M_max.4'] + CC),
    ('Q3', 'SOURCE-MAP-CITATIONS-VERIFIED', None),
]


def negative(token):
    return token.rsplit('-', 1)[0] + '-NOT-ESTABLISHED'


ALL_TOKENS = [t for _, t, _ in CELLS] + [negative(t) for _, t, _ in CELLS]

# ---------------------------------------------------------------------------------------------- landed at D
SCOPE_SENTENCE = ('The stage-level product of two `DirectedStages` and the bridge from completed product towers to '
                  'this interface are not part of this module.')
COMPLETION_TEXTS = [
    (LEAN + 'StageCompletion.lean',
     'def body : Set (CSpace D) :=\n  closure (convexHull ℝ (Set.range (prepVec D)))'),
    (LEAN + 'CompletionAction.lean', 'theorem body_isClosed : IsClosed (body D) := isClosed_closure'),
    (LEAN + 'CompletionAction.lean',
     'structure OpDatum (D : DirectedStages) where\n  τ : Prep D → CSpace D\n  mem_body : ∀ x, τ x ∈ body D'),
    (LEAN + 'CompletionAction.lean',
     'def Undoes (S T : OpDatum D) (hS : AffineRespect S) : Prop :=\n  ∀ x, (after C S T hS).τ x = prepVec D x'),
    (LEAN + 'CompletionAction.lean',
     'theorem preservesBody_inducedEquiv {S T : OpDatum D} (hS : AffineRespect S)\n'
     '    (hT : AffineRespect T) (hST : Undoes C S T hS) (hTS : Undoes C T S hT) :\n'
     '    PreservesBody (chartBody C) {inducedEquiv C hS hT hST hTS} := by'),
]
DIRECTED_SYSTEMS = {'badD', 'bitTower', 'midD'}
CITATIONS = [
    ('CompositeDimension.lean', ['cnot', 'phiW', 'prodState', 'pairVal', 'prodEffVal', 'maxCone', 'actT', 'actC',
                                 'IsNot', 'NativeGate', 'nativeGate_cnot', 'cnot_prodState_xplus_z3']),
    ('K2Guard.lean', ['CandidateCone', 'idW', 'chainW', 'cnot_idW', 'chain_eq', 'chain_value',
                      'no_candidateCone_cnot_reflY', 'prodState_mem_maxCone', 'actT_reflY_phiW']),
    ('CompositeInterface.lean', ['ProductData', 'PreComposite', 'Composite', 'LocallyTomographic', 'minBody',
                                 'maxBody', 'subset_maxBody', 'JointReversible', 'modelData_ext',
                                 'prodEff_eq_of_eff_eq', 'minComposite', 'maxComposite', 'ball3MinComposite',
                                 'ball3MaxComposite']),
    ('StageCompletion.lean', ['body']),
    ('CompletionAction.lean', ['OpDatum', 'AffineRespect', 'Undoes', 'body_isClosed', 'induced_mem',
                               'preservesBody_inducedEquiv']),
    ('RelcSelectBlock.lean', ['CtrlGate', 'dim_of_ctrlGate', 'three_of_ctrlGate']),
]

# ---------------------------------------------------------------------------------------------- the workflow edit
SHARD = '''  probes_kt4prem1:
    name: Numerical probes / KT4-PREM-1 premise audit
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install the exact-algebra dependency
        run: pip install sympy==1.14.0

      - name: KT4-PREM-1 premise audit probe
        working-directory: verification/lean
        run: |
          echo "=== kt4_prem1_probe.py ==="
          python3 kt4_prem1_probe.py

'''
SHARD_ANCHOR = '          python3 kinf2_foundations_probe.py\n\n'
EDITS = [
    ('probes_nb1, probes_kinf2, probes_a42_witness', 'probes_nb1, probes_kinf2, probes_kt4prem1, probes_a42_witness'),
    ('          KINF2_RESULT: ${{ needs.probes_kinf2.result }}\n',
     '          KINF2_RESULT: ${{ needs.probes_kinf2.result }}\n'
     '          KT4PREM1_RESULT: ${{ needs.probes_kt4prem1.result }}\n'),
    ('          echo "kinf2=${KINF2_RESULT}"\n',
     '          echo "kinf2=${KINF2_RESULT}"\n          echo "kt4prem1=${KT4PREM1_RESULT}"\n'),
    ('          test "${KINF2_RESULT}" = success\n',
     '          test "${KINF2_RESULT}" = success\n          test "${KT4PREM1_RESULT}" = success\n'),
]

# ---------------------------------------------------------------------------------------------- the frozen texts
EARNED = (
    'The hypothesis hcl cannot be dropped from the Pauli-free four-copy theorem: the closedness foil satisfies hcls, '
    'hadm, hgate and H and fails IE1. The hypothesis hgate is not necessary relative to hcls, hadm, hcl, H and the '
    'conclusion: the maximal-cone model satisfies all of them and fails hgate; this does not show that hgate can be '
    'removed, and the D-gate model refutes the implication without it. Each of hcls, hadm, hgate and the token clauses '
    'cannot be dropped, and each of hcls, hadm and the token clauses of the given data is not necessary, by the models '
    'of the matrix. Under hadm, H is equivalent to the cone-level interface FCC, one direction by Lemma B1 of the '
    'design modules and the other by an explicit carrier. Certified main supplies neither closedness nor gate '
    'preservation for a composite of two balls; a pair-level completion supplies closedness only from a new premise, '
    'and gate preservation only from a premise that states it on preparations.')
NONINF = (
    'This round adopts no premise, sources none of the five hypotheses, and makes no manuscript claim and no ROADMAP '
    'claim. Its countermodels are models of the hypothesis sets they are stated for and of nothing more; none is a '
    'physical theory. The necessity of hcl relative to hcls, hadm, hgate and the conclusion rests on a written argument '
    'with one standard input from Lie theory and is not kernel-checked; the probe checks its finite steps only. The '
    'audited theorem is kernel-checked in a design run and is not certified. Nothing here says that the observational '
    'axioms force quantum cones: the classification of a pair cone as Q3 or its twin holds relative to N-CLASS gates, '
    'admissible cones, gate preservation and IE1, none of which is sourced.')
PHRASES = ['observational axioms force', 'oi forces', 'forces quantum', 'is sourced', 'are sourced', 'adopt',
           'hgate can be dropped', 'hgate can be removed', 'hgate is redundant', 'hgate is unnecessary',
           'without hgate the theorem', 'hcl is redundant', 'proves that hcl is necessary',
           'kernel-checked necessity', 'certified theorem', 'physical theory']


# ------------------------------------------------------------------------------------------------------- helpers
def norm(s):
    return ' '.join(s.replace('`', '').split()).lower()


def unquote(note):
    """The note with its blockquote markers removed, so a frozen text quoted across lines reads as one passage."""
    return '\n'.join(re.sub(r'^\s*>\s?', '', line) for line in note.split('\n'))


def git(*args, data=None):
    r = subprocess.run(['git', *args], capture_output=True, input=data)
    if r.returncode != 0:
        raise RuntimeError('git %s: %s' % (' '.join(args), r.stderr.decode('utf-8', 'replace').strip()))
    return r.stdout.decode('utf-8')


def show(commit, path):
    r = subprocess.run(['git', 'show', '%s:%s' % (commit, path)], capture_output=True)
    return r.stdout.decode('utf-8') if r.returncode == 0 else None


def blob(commit, path):
    r = subprocess.run(['git', 'rev-parse', '%s:%s' % (commit, path)], capture_output=True)
    return r.stdout.decode('utf-8').strip() if r.returncode == 0 else None


def blob_text(blob_id):
    r = subprocess.run(['git', 'cat-file', 'blob', blob_id], capture_output=True)
    return r.stdout.decode('utf-8') if r.returncode == 0 else None


def hash_text(text):
    return git('hash-object', '--stdin', data=text.encode('utf-8')).strip()


def ls(commit, prefix):
    out = git('ls-tree', '-r', '--name-only', commit, '--', prefix)
    return sorted(l for l in out.split('\n') if l)


def changed(base, head):
    out = git('diff', '--name-only', base, head)
    return sorted(l for l in out.split('\n') if l)


class Fail(Exception):
    def __init__(self, code, msg):
        super().__init__('%s: %s' % (code, msg))
        self.code = code


def need(cond, code, msg):
    if not cond:
        raise Fail(code, msg)


# ------------------------------------------------------------------------------------------------- the controls
def landed_status(texts, lean_files):
    """texts: {path: text} at D for the cited files; lean_files: {path: text} for every OIBridge/*.lean at D.
    Returns {code: message or None}: L1 the COMP-1 scope sentence, L2 the completion-layer texts, L3 the directed
    systems, L4 the citations."""
    st = {}
    st['L1'] = None if norm(SCOPE_SENTENCE) in norm(texts.get(LEAN + 'CompositeInterface.lean', '')) else \
        'the COMP-1 scope sentence is not the frozen one at D'
    miss = [frag.split('\n')[0] for path, frag in COMPLETION_TEXTS if frag not in texts.get(path, '')]
    st['L2'] = None if not miss else 'frozen completion-layer texts missing at D: %s' % '; '.join(miss)
    systems = set()
    for text in lean_files.values():
        systems.update(re.findall(r'^(?:noncomputable )?def (\w+) : DirectedStages where$', text, re.M))
    st['L3'] = None if systems == DIRECTED_SYSTEMS else 'directed systems at D are %s' % sorted(systems)
    missing = []
    for fname, names in CITATIONS:
        text = texts.get(LEAN + fname, '')
        for nm in names:
            if not re.search(r'^(?:theorem|def|structure|abbrev|noncomputable def|lemma|class)\s+%s\b' % re.escape(nm),
                             text, re.M):
                missing.append('%s:%s' % (fname, nm))
    st['L4'] = None if not missing else 'unresolved citations: %s' % ', '.join(missing)
    return st


def control_L(texts, lean_files):
    for code, msg in sorted(landed_status(texts, lean_files).items()):
        need(msg is None, code, msg)


def apply_edit(workflow):
    need(workflow.count(SHARD_ANCHOR) == 1, 'W', 'the shard anchor is not unique in the workflow at D')
    out = workflow.replace(SHARD_ANCHOR, SHARD_ANCHOR + SHARD, 1)
    for old, new in EDITS:
        need(out.count(old) == 1, 'W', 'an aggregate anchor is not unique in the workflow at D')
        out = out.replace(old, new, 1)
    return out


def control_P(probe_text):
    need(probe_text is not None and hash_text(probe_text) == PROBE_BLOB, 'P', 'the probe is not the frozen blob')


def control_W(workflow_D, workflow_X):
    need(workflow_X == apply_edit(workflow_D), 'W', 'the workflow is not D\'s with exactly the frozen edit')


def parse_probe(stdout):
    passes, fails = set(), set()
    for line in stdout.split('\n'):
        m = re.match(r'^(PASS|FAIL) (\S+)  \[', line)
        if m:
            (passes if m.group(1) == 'PASS' else fails).add(m.group(2))
    return passes, fails


def cell_outcomes(passes, fails, landed_ok, citations_ok):
    out = []
    for cell, token, ids in CELLS:
        if ids is None:
            ok = citations_ok
        else:
            ok = all(i in passes and i not in fails for i in ids)
            if cell == 'Q2':
                ok = ok and landed_ok
        out.append((cell, token if ok else negative(token)))
    return out


def control_V(note, outcomes, summary_line):
    found = set(re.findall(r'\b[A-Z0-9]+(?:-[A-Z0-9]+)*-(?:VERIFIED|NOT-ESTABLISHED)\b', note))
    want = {t for _, t in outcomes}
    need(found == want, 'V1', 'the note carries %s, the cells give %s' % (sorted(found), sorted(want)))
    all_pos = all(not t.endswith('NOT-ESTABLISHED') for _, t in outcomes)
    has_earned = norm(EARNED) in norm(unquote(note))
    need(has_earned == all_pos, 'V2', 'the earned reading is %s but the cells are %s'
         % ('present' if has_earned else 'absent', 'all positive' if all_pos else 'not all positive'))
    need(norm(NONINF) in norm(unquote(note)), 'V3', 'the non-inference rule is not stated in its frozen words')
    need(summary_line in note, 'V4', 'the probe summary line from the run at E is not carried')


def control_S8(note):
    rest = norm(unquote(note)).replace(norm(EARNED), ' ').replace(norm(NONINF), ' ')
    hits = [p for p in PHRASES if p in rest]
    need(not hits, 'S8', 'frozen phrases in the result note: %s' % ', '.join(hits))


# -------------------------------------------------------------------------------------------- git-level drivers
def run_probe_text(probe_text, sources):
    """Run a probe text with python3 -I beside the given {path: text} sources; return (exit status, stdout)."""
    with tempfile.TemporaryDirectory() as td:
        for path, text in [(PROBE, probe_text)] + sorted(sources.items()):
            dest = os.path.join(td, path)
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with open(dest, 'w', encoding='utf-8') as f:
                f.write(text)
        r = subprocess.run([sys.executable, '-I', os.path.join(td, PROBE)], cwd=os.path.join(td, 'verification/lean'),
                           capture_output=True, timeout=3600)
        return r.returncode, r.stdout.decode('utf-8')


def run_probe(commit):
    text = show(commit, PROBE)
    need(text is not None, 'P', '%s is absent at %s' % (PROBE, commit))
    sources = {}
    for path in PROBE_SOURCES:
        src = show(commit, path)
        need(src is not None, 'P', '%s is absent at %s' % (path, commit))
        sources[path] = src
    return run_probe_text(text, sources)


def landed_texts(commit):
    texts = {}
    for fname, _ in CITATIONS:
        texts[LEAN + fname] = show(commit, LEAN + fname) or ''
    lean_files = {}
    for path in ls(commit, LEAN):
        if path.endswith('.lean') and path.count('/') == LEAN.count('/'):
            lean_files[path] = show(commit, path) or ''
    return texts, lean_files


def verdict(commit):
    texts, lean_files = landed_texts(D)
    st = landed_status(texts, lean_files)
    landed_ok = st['L1'] is None and st['L2'] is None and st['L3'] is None
    citations_ok = st['L4'] is None
    rc, stdout = run_probe(commit)
    passes, fails = parse_probe(stdout)
    outcomes = cell_outcomes(passes, fails, landed_ok, citations_ok)
    summary = [l for l in stdout.split('\n') if l.startswith('kt4_prem1_probe:')]
    return outcomes, (summary[-1] if summary else '<no summary>'), rc


def check(commit, freeze):
    results = []

    def step(name, fn):
        fn()
        results.append(name)

    texts, lean_files = landed_texts(D)
    step('L landed texts at D', lambda: control_L(texts, lean_files))
    step('P probe blob', lambda: control_P(show(commit, PROBE)))
    step('W workflow edit', lambda: control_W(show(D, WORKFLOW), show(commit, WORKFLOW)))
    files = ls(commit, RDIR)
    allowed = {PREREG, CONTROLS, RESULT}
    step('R record directory', lambda: need(set(files) <= allowed and PREREG in files and CONTROLS in files, 'R',
                                            'the record directory holds %s' % files))
    with open(os.path.abspath(__file__), 'rb') as f:
        own = f.read().decode('utf-8')
    step('R controls blob', lambda: need(show(commit, CONTROLS) == own, 'R', 'controls.py at %s is not this file'
                                         % commit))
    gov = {PREREG, CONTROLS, RESULT, PROBE, WORKFLOW}
    step('G governed paths', lambda: need(set(changed(D, commit)) <= gov, 'G', 'delta(D, %s) leaves the governed paths'
                                          ': %s' % (commit, sorted(set(changed(D, commit)) - gov))))
    for path in PROBE_SOURCES:
        step('G probe source %s' % os.path.basename(path),
             lambda path=path: need(blob(commit, path) == blob(D, path), 'G', '%s changed' % path))
    if freeze:
        step('F parent', lambda: need(git('rev-parse', freeze + '^').strip() == D and
                                      git('rev-list', '--parents', '-n', '1', freeze).split()[1:] == [D], 'F',
                                      'F is not a single-parent child of D'))
        step('F delta', lambda: need(changed(D, freeze) == [PREREG], 'F', 'delta(D, F) is not the preregistration alone'))
        step('F preregistration unchanged', lambda: need(blob(commit, PREREG) == blob(freeze, PREREG), 'F',
                                                         'the preregistration changed after F'))
    note = show(commit, RESULT)
    if note is not None:
        outcomes, summary, _ = verdict(commit)
        step('V verdicts', lambda: control_V(note, outcomes, summary))
        step('S8 phrases', lambda: control_S8(note))
    return results


# ------------------------------------------------------------------------------------------------------ self-test
def self_test():
    n = [0]

    def expect_fail(code, fn):
        try:
            fn()
        except Fail as e:
            if e.code != code:
                raise SystemExit('self-test: expected %s, got %s' % (code, e.code))
            n[0] += 1
            return
        raise SystemExit('self-test: a mutation for %s passed' % code)

    def expect_pass(fn):
        fn()
        n[0] += 1

    texts, lean_files = landed_texts(D)
    expect_pass(lambda: control_L(texts, lean_files))
    t2 = dict(texts)
    t2[LEAN + 'CompositeInterface.lean'] = t2[LEAN + 'CompositeInterface.lean'].replace(
        'are not part of', 'are part of')
    expect_fail('L1', lambda: control_L(t2, lean_files))
    lf2 = dict(lean_files)
    lf2['extra.lean'] = 'noncomputable def pairTower : DirectedStages where\n'
    expect_fail('L3', lambda: control_L(texts, lf2))
    t3 = dict(texts)
    t3[LEAN + 'K2Guard.lean'] = t3[LEAN + 'K2Guard.lean'].replace('theorem chain_value', 'theorem chain_valueX')
    expect_fail('L4', lambda: control_L(t3, lean_files))
    t4 = dict(texts)
    t4[LEAN + 'CompletionAction.lean'] = t4[LEAN + 'CompletionAction.lean'].replace(
        'IsClosed (body D) := isClosed_closure', 'IsClosed (body D) := sorry')
    expect_fail('L2', lambda: control_L(t4, lean_files))

    wd = show(D, WORKFLOW)
    expect_pass(lambda: control_W(wd, apply_edit(wd)))
    expect_fail('W', lambda: control_W(wd, apply_edit(wd).replace('          test "${KT4PREM1_RESULT}" = success\n',
                                                                   '')))
    expect_fail('W', lambda: control_W(wd, wd))

    all_ids = set()
    for _, _, ids in CELLS:
        all_ids.update(ids or [])
    good = '\n'.join('PASS %s  [identity] x' % i for i in sorted(all_ids))
    p, f = parse_probe(good)
    pos = cell_outcomes(p, f, True, True)
    expect_pass(lambda: need(all(not t.endswith('NOT-ESTABLISHED') for _, t in pos), 'V0', 'positive control'))
    bad = good.replace('PASS M_cl.8  [', 'FAIL M_cl.8  [')
    p2, f2 = parse_probe(bad)
    o2 = dict(cell_outcomes(p2, f2, True, True))
    expect_pass(lambda: need(o2['Q1-CL'] == negative('CLOSEDNESS-FOIL-VERIFIED') and o2['Q1-MAX'].endswith('VERIFIED')
                             and not o2['Q1-MAX'].endswith('NOT-ESTABLISHED'), 'V0',
                             'a failing check reads not-established in its own cell alone'))
    renamed = good.replace('PASS M_max.4  [', 'PASS M_max.4x  [')
    p3, f3 = parse_probe(renamed)
    o3 = dict(cell_outcomes(p3, f3, True, True))
    expect_pass(lambda: need(o3['Q1-MAX'].endswith('NOT-ESTABLISHED') and o3['Q1-NEC'].endswith('NOT-ESTABLISHED')
                             and o3['Q2'].endswith('NOT-ESTABLISHED') and not o3['Q1-CL'].endswith('NOT-ESTABLISHED'),
                             'V0', 'a renamed check reads not-established in every cell that reads it'))
    o4 = dict(cell_outcomes(p, f, True, False))
    expect_pass(lambda: need([c for c, t in o4.items() if t.endswith('NOT-ESTABLISHED')] == ['Q3'], 'V0',
                             'an unresolved citation reads not-established in Q3 alone'))
    o5 = dict(cell_outcomes(p, f, False, True))
    expect_pass(lambda: need([c for c, t in o5.items() if t.endswith('NOT-ESTABLISHED')] == ['Q2'], 'V0',
                             'a landed completion text that differs reads not-established in Q2 alone'))

    probe = blob_text(PROBE_BLOB)
    need(probe is not None, 'T', 'the frozen probe blob %s is not in the object store' % PROBE_BLOB)
    expect_pass(lambda: control_P(probe))
    renamed_src = probe.replace("chk('M_max.4', ", "chk('M_max.4x', ", 1)
    expect_pass(lambda: need(renamed_src != probe, 'T', 'the rename anchor is absent'))
    expect_fail('P', lambda: control_P(renamed_src))
    mutated_src = probe.replace("chainW) == Q(-1, 2), 'witness')", "chainW) == Q(-1, 3), 'witness')", 1)
    expect_pass(lambda: need(mutated_src != probe, 'T', 'the witness anchor is absent'))
    expect_fail('P', lambda: control_P(mutated_src))
    rc_m, out_m = run_probe_text(mutated_src, {path: show(D, path) for path in PROBE_SOURCES})
    p_m, f_m = parse_probe(out_m)
    o_m = dict(cell_outcomes(p_m, f_m, True, True))
    expect_pass(lambda: need(rc_m == 1 and f_m == {'M_max.4'} and len(p_m) == 78
                             and sorted(c for c, t in o_m.items() if t.endswith('NOT-ESTABLISHED'))
                             == ['Q1-MAX', 'Q1-NEC', 'Q2'], 'V0',
                             'the probe with one witness value changed fails that check alone, and the cells that '
                             'read it alone read not-established'))

    tokens = ' '.join('`%s`' % t for _, t in pos)
    note = 'Outcome: %s.\n\n> %s\n\n> %s\n\n%s\n' % (tokens, EARNED, NONINF, PROBE_SUMMARY)
    expect_pass(lambda: control_V(note, pos, PROBE_SUMMARY))
    expect_pass(lambda: control_S8(note))
    expect_fail('V1', lambda: control_V(note + '\nAlso `MAXCONE-MODEL-NOT-ESTABLISHED`.\n', pos, PROBE_SUMMARY))
    expect_fail('V2', lambda: control_V(note.replace('cannot be dropped from', 'can be dropped from'), pos,
                                        PROBE_SUMMARY))
    expect_fail('V3', lambda: control_V(note.replace('none of which is sourced', 'all of which are sourced'), pos,
                                        PROBE_SUMMARY))
    expect_fail('V4', lambda: control_V(note.replace(PROBE_SUMMARY, ''), pos, PROBE_SUMMARY))
    expect_fail('S8', lambda: control_S8(note + '\nHence hgate can be dropped.\n'))
    expect_fail('S8', lambda: control_S8(note + '\nThe premise is sourced.\n'))
    def quoted(text):
        return '\n'.join('> ' + l for l in textwrap.wrap(text, 100, break_on_hyphens=False))
    wrapped = 'Outcome: %s.\n\n%s\n\nThe rule:\n\n%s\n\n%s\n' % (tokens, quoted(EARNED), quoted(NONINF), PROBE_SUMMARY)
    expect_pass(lambda: need(wrapped.count('\n> ') >= 8, 'T', 'the quotes do not span lines'))
    expect_pass(lambda: control_V(wrapped, pos, PROBE_SUMMARY))
    expect_pass(lambda: control_S8(wrapped))
    w_earned = wrapped.replace('and fails IE1.', 'and fails IE2.', 1)
    w_rule = wrapped.replace('none is a', 'each is a', 1)
    expect_pass(lambda: need(w_earned != wrapped and w_rule != wrapped, 'T', 'a quoted-text mutation is vacuous'))
    expect_fail('V2', lambda: control_V(w_earned, pos, PROBE_SUMMARY))
    expect_fail('V3', lambda: control_V(w_rule, pos, PROBE_SUMMARY))
    neg = [(c, negative(t) if c == 'Q1-MAX' else t) for c, t in pos]
    negtok = ' '.join('`%s`' % t for _, t in neg)
    note_neg = 'Outcome: %s.\n\n> %s\n\n%s\n' % (negtok, NONINF, PROBE_SUMMARY)
    expect_pass(lambda: control_V(note_neg, neg, PROBE_SUMMARY))
    expect_fail('V2', lambda: control_V(note_neg + '\n> %s\n' % EARNED, neg, PROBE_SUMMARY))
    return n[0]


def main(argv):
    if argv[1:] == ['--self-test']:
        k = self_test()
        print('controls: OK -- self-test %d checks' % k)
        return 0
    if len(argv) >= 3 and argv[1] == 'verdict':
        outcomes, summary, rc = verdict(argv[2])
        for cell, token in outcomes:
            print('%-7s %s' % (cell, token))
        print(summary)
        return 0
    if len(argv) >= 3 and argv[1] == 'check':
        freeze = argv[argv.index('--freeze') + 1] if '--freeze' in argv else None
        try:
            done = check(argv[2], freeze)
        except Fail as e:
            print('controls: FAILED %s' % e)
            return 1
        print('controls: OK -- %d checks' % len(done))
        return 0
    print(__doc__)
    return 1


if __name__ == '__main__':
    sys.exit(main(sys.argv))
