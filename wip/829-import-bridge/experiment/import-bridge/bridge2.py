"""Import-redundancy bridge for #829: is `import OIBridge.EqvK2MaxCone` redundant for the design?

  python3 -I -B bridge2.py generate <design-dir> <out-dir>   # pure Python; checks the edit ledger
  python3 -I -B bridge2.py selftest                           # pure Python; comparator mutations
  lake env python3 -I -B bridge2.py run <out-dir>             # from verification/lean-mathlib

Regimes (each a directory of design modules with the pinned module names):
  pinned  the design sources at a4277540, byte for byte;
  remove  FinitePauli.lean line 1 `import OIBridge.EqvK2Schema` -> `import OIBridge.EqvK2Generation`;
  keep    FinitePauli.lean line 1 -> `import OIBridge.EqvK2MaxCone`, and FiniteReachTable.lean
          lines 1386-1393 (the environment-absence #eval and its comment) deleted;
  keep_i  keep's oleans, with the pinned FiniteReachTable.lean compiled against them.
Every other design byte is the pinned one. `remove` and `keep` differ exactly by the modules in
closure(EqvK2MaxCone) minus closure(EqvK2Generation) (EXTRA), for every design module.
The decision rule is frozen in VERDICT_RULE below; the verdict text is generated from the
measurements. Nothing here has been executed with Lean.
DEPCHECK's template is the one in agent-829/bridge (credited); WALK, DUMP, ABSENT, SPELL and
STMT-IDENTITY are new here.
"""
import difflib
import hashlib
import os
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TPL = HERE / 'tpl'
PINS = {  # design sources at a4277540
    'FinitePauli.lean': '4af38e2e151390edf8ca23cdec94be06b7b4b1f9c72c57292a5374b7ca195b8e',
    'FiniteWalsh.lean': 'd4815ec809fa37fefabe786886efb860f1da02788cea4f7e048e34726da8a5f0',
    'FiniteReach.lean': '5112671f1317d60e23b2fcb4a20953f38771e9c1f2f03b2c553f1360947985b4',
    'FiniteReachTable.lean': 'a71fcb33477cfce4200643f967c2fd4382dc942749fe304b08135748af294f08',
}
CHAIN = ['FinitePauli', 'FiniteWalsh', 'FiniteReach', 'FiniteReachTable']  # compile order
OLEAN = {'FinitePauli', 'FiniteReach', 'FiniteReachTable'}
PAULI_L1 = 'import OIBridge.EqvK2Schema\n'
EVAL_SPAN = (1386, 1393)  # 1-based, inclusive, in FiniteReachTable.lean
EVAL_FIRST = "/- The two-token generator theorem of the adopted `EqvK2MaxCone` module is not in this\n"
EVAL_LAST = '  logInfo "OIBridge.EqvK2MaxCone.pairCone_eq_Q3_of_drive_maxCone is not in the environment"\n'
REC = 'FiniteReconstructionDesign.pairCone_eq_Q3_of_kToken'
PAIR = '`OIBridge.EqvK2MaxCone.pairCone_eq_Q3_of_drive_maxCone'
SIBLINGS = ['OIBridge.EqvK2Generation.blockInvariant_of_drive',
            'OIBridge.EqvK2Generation.pairCone_eq_Q3_of_drive_exact',
            'OIBridge.EqvK2Generation.pairCone_eq_Q3_iff_drive_exact',
            'OIBridge.EqvK2Block.pairCone_eq_Q3_of_block',
            'OIBridge.EqvK2Block.pairCone_eq_Q3_iff_block',
            'OIBridge.EqvK2Schema.pairCone_eq_Q3_of_drive',
            'OIBridge.EqvK2Schema.subset_Q3_of_pure_dual',
            'OIBridge.EqvK2Schema.Q3_subset_of_pure',
            'OIBridge.EqvK2Converse.pairCone_eq_Q3_iff_drive']
DEP_REQUIRED = ['FiniteReconstructionDesign.kCone_eq_QK_of_drive_maxCone',
                'OIBridge.EqvK2Generation.su_euler']       # crosses into the adopted library
WALK_REQUIRED = ['OIBridge.EqvK2Generation.su_euler', 'OIBridge.CompositeDimension.cnot',
                 'Matrix.PosSemidef']
DESIGN_MODULES = ['FinitePauli', 'FiniteReach', 'FiniteReachTable']
EXPECTED_THEOREMS = {'FinitePauli': 14, 'FiniteReach': 77, 'FiniteReachTable': 136}
EXPECTED_AXIOM_LINES = {'FinitePauli': 8, 'FiniteWalsh': 3, 'FiniteReach': 13, 'FiniteReachTable': 47}

VERDICT_RULE = """\
VOID unless every control case has its expected outcome and codes, the path guard holds and the
comparator self-test passes.  Otherwise:
IMPORT-REDUNDANT-IN-DESIGN  iff  pinned, remove and keep build with no error; keep_i has exactly one
  error, the #eval's 'is in the environment'; the axiom lines of remove and keep are identical
  (and keep_i's equal keep's for FiniteReachTable); the DUMP STMT lines of remove and keep are
  identical; WALK PASS in all three regimes; DEPCHECK PASS in remove (absent mode, and present mode
  in the remove control file) and in keep (present mode); STMT-IDENTITY ok in remove and keep.
IMPORT-USED  if WALK in keep reports a design constant reaching a constant of an EXTRA module.
IMPORT-NOT-TRANSPARENT  if the builds are clean and WALK passes but axiom lines or STMT lines of
  remove and keep differ.
IMPORT-BRIDGE-INCONCLUSIVE  otherwise.
Reported, not decisive: remove vs pinned (axioms, STMT lines); VALUEHASH agreement of remove/keep.
"""

# --- source parsing (theorem names, for DUMP's vacuity control) ---------------------------------
DECL = re.compile(r'^\s*(?:@\[[^\]]*\]\s*)?(?:(?:private|protected|noncomputable|nonrec|partial)\s+)*'
                  r'(theorem|lemma)\s+([^\s:({\[]+)')


def strip_comments(text):
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
            j = text.find('\n', i)
            i = n if j < 0 else j
            continue
        out.append(text[i]); i += 1
    return ''.join(out)


def theorems(text, namespace='FiniteReconstructionDesign'):
    names = []
    for line in strip_comments(text).splitlines():
        m = DECL.match(line)
        if m:
            names.append(namespace + '.' + m.group(2))
    return names


def lean_names(xs):
    return '#[' + ', '.join('`' + x for x in xs) + ']'


def fill(name, **kw):
    t = (TPL / name).read_text(encoding='utf-8')
    for k, v in kw.items():
        t = t.replace('@@' + k + '@@', v)
    assert '@@' not in t, (name, re.findall(r'@@\w+@@', t))
    return t


def depcheck(target, present, siblings=SIBLINGS, modules='#[`OIBridge.EqvK2MaxCone]',
             required=DEP_REQUIRED):
    return fill('depcheck.lean.in', TARGET='`' + target, PAIR=PAIR,
                PAIR_PRESENT='true' if present else 'false', MODULES=modules,
                SIBLINGS=lean_names(siblings), REQUIRED=lean_names(required), WATCH='`OIBridge')


def walk_dump(present, thms, required=WALK_REQUIRED, modules=DESIGN_MODULES, roots=()):
    return fill('walk_dump.lean.in', PRESENT='true' if present else 'false',
                DESIGN_MODULES=lean_names(modules), WALK_REQUIRED=lean_names(required),
                THEOREMS=lean_names(thms), EXTRA_ROOTS=lean_names(roots))


def stmt(recovered=REC):
    return fill('stmt.lean.in', RECOVERED=recovered)


def absent(module):
    return fill('absent.lean.in', MODULE='`' + module)


# --- mutations ---------------------------------------------------------------------------------
MUT_HEAD = '''import FiniteReachTable

namespace FiniteReconstructionDesign.Mutation

open Matrix
open OIBridge.MonoidalCompletion OIBridge.EqvK2Schema OIBridge.EqvK2Converse
  OIBridge.EqvK2Block OIBridge.EqvK2Generation OIBridge.CompositeDimension
open scoped ComplexOrder

set_option linter.unusedVariables false in
theorem pairCone_eq_Q3_of_kToken @@BINDER@@
    (hH1 : ∀ x ∈ OIBridge.TransitiveBody.eball 3, ∀ y ∈ OIBridge.TransitiveBody.eball 3,
      prodState x y ∈ K)
    (hadd : ∀ ω ∈ K, ∀ η ∈ K, ω + η ∈ K)
    (hsmul : ∀ c : ℝ, 0 ≤ c → ∀ ω ∈ K, c • ω ∈ K)
    (hmax : K ⊆ maxCone (OIBridge.TransitiveBody.eball 3))
    (hH2 : ∀ ω ∈ K, cnot ω ∈ K)
    (hA : ∀ t : ℝ, ∀ ω ∈ K, actT (OIBridge.KInfFoundations.rotLin t) ω ∈ K ∧
      actT (OIBridge.KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ K)@@EXTRA@@ :
    K = Q3 :=
@@PROOF@@

end FiniteReconstructionDesign.Mutation

'''
MUT = 'FiniteReconstructionDesign.Mutation.pairCone_eq_Q3_of_kToken'
EFFECT_ROOTS = ['FiniteReconstructionDesign.Mutation.sharpCone', 'FiniteReconstructionDesign.Mutation.sharpCone_subset']
MEASUREMENTS = ('Probe_pinned', 'Probe_remove', 'Control_remove', 'Probe_keep')
ARGS = 'hH1 hadd hsmul hmax hH2 hA'
REAL = f'  FiniteReconstructionDesign.pairCone_eq_Q3_of_kToken {ARGS}'
EFFECT_USE = '''import FiniteReachTable

namespace FiniteReconstructionDesign.Mutation

/-- A definition-level use of the import's closure: the sharp-test cone of `EffectSpace`. -/
def sharpCone : Set (OIBridge.CompositeDimension.W 3) :=
  OIBridge.EffectSpace.maxConeOf (OIBridge.EffectSpace.sharpFamily 3)

theorem sharpCone_subset : sharpCone ⊆ OIBridge.CompositeDimension.maxCone (OIBridge.TransitiveBody.eball 3) :=
  fun _ h => OIBridge.EffectSpace.maxConeOf_sharp_subset_maxCone (by norm_num) h

end FiniteReconstructionDesign.Mutation

'''


def mut(proof, check, extra='', binder='{K : Set (W 3)}'):
    return MUT_HEAD.replace('@@BINDER@@', binder).replace('@@EXTRA@@', extra).replace('@@PROOF@@', proof) + check


def cases(thms):
    """(name, regime, olean?, expectation, codes). expectation: pass | fail | one-error."""
    vac_sib = [s if s != 'OIBridge.EqvK2Schema.Q3_subset_of_pure' else s + 'e' for s in SIBLINGS]
    assert vac_sib != SIBLINGS
    files = {
        'Probe_pinned': ('pinned', 'import FiniteReachTable\n\n' + depcheck(REC, False) + '\n' + walk_dump(False, thms)),
        'Probe_remove': ('remove', 'import FiniteReachTable\n\n' + depcheck(REC, False) + '\n' + walk_dump(False, thms)),
        'Control_remove': ('remove', 'import FiniteReachTable\nimport OIBridge.EqvK2MaxCone\n\n' + absent('FiniteReachTable')
                           + '\n' + stmt() + '\n' + depcheck(REC, True)),
        'Probe_keep': ('keep', 'import FiniteReachTable\n\n' + depcheck(REC, True) + '\n' + walk_dump(True, thms) + '\n' + stmt()),
        'M_direct': ('keep', mut(f'  OIBridge.EqvK2MaxCone.pairCone_eq_Q3_of_drive_maxCone {ARGS}', depcheck(MUT, True))),
        'M_iff': ('keep', mut('  (OIBridge.EqvK2MaxCone.pairCone_eq_Q3_iff_drive_maxCone hH1 hadd hsmul hmax).2 ⟨hH2, hA⟩', depcheck(MUT, True))),
        'M_inline': ('keep', mut('  OIBridge.EqvK2MaxCone.pairCone_eq_Q3_of_block_maxCone hH1 hadd hsmul hmax\n'
                                 '    (OIBridge.EqvK2Generation.blockInvariant_of_drive hH2 hA)', depcheck(MUT, True))),
        'M_deadref': ('keep', mut(f'  by\n    have _x := OIBridge.EqvK2MaxCone.pairCone_eq_Q3_of_drive_maxCone {ARGS}\n'
                                  f'    exact FiniteReconstructionDesign.pairCone_eq_Q3_of_kToken {ARGS}', depcheck(MUT, True))),
        'M_sibling': ('keep', mut('  by\n    have _x := OIBridge.EqvK2Generation.blockInvariant_of_drive hH2 hA\n'
                                  f'    exact FiniteReconstructionDesign.pairCone_eq_Q3_of_kToken {ARGS}', depcheck(MUT, True))),
        'M_real': ('keep', mut(REAL, depcheck(MUT, True))),
        'M_required': ('keep', mut(REAL, depcheck('FiniteReconstructionDesign.mem_Q3_iff_pairCarrier', True))),
        'M_vac_target': ('keep', mut(REAL, depcheck(MUT + 'X', True))),
        'M_vac_sibling': ('keep', mut(REAL, depcheck(MUT, True, siblings=vac_sib))),
        'M_vac_module': ('keep', mut(REAL, depcheck(MUT, True, modules='#[`OIBridge.EqvK2MaxCon]'))),
        'M_walk_effect': ('keep', EFFECT_USE + walk_dump(True, thms, roots=EFFECT_ROOTS)),
        'M_walk_required': ('keep', 'import FiniteReachTable\n\n' + walk_dump(True, thms, required=['OIBridge.EqvK2Generation.su_eulerX'])),
        'M_stmt_binder': ('keep', mut(f'  @FiniteReconstructionDesign.pairCone_eq_Q3_of_kToken K {ARGS}',
                                      stmt(MUT), binder='(K : Set (W 3))')),
        'M_stmt_hyp': ('keep', mut(REAL, stmt(MUT), extra='\n    (hextra : True)')),
        'M_absent_sibling': ('remove', mut('  by\n    have _x := OIBridge.EqvK2Generation.blockInvariant_of_drive hH2 hA\n'
                                           f'    exact FiniteReconstructionDesign.pairCone_eq_Q3_of_kToken {ARGS}', depcheck(MUT, False))),
        'M_absent_on_keep': ('keep', 'import FiniteReachTable\nimport OIBridge.EqvK2MaxCone\n\n' + absent('FiniteReachTable')),
    }
    expect = [
        ('Probe_pinned', 'pass', ['DEPCHECK-ABSENT ok', 'DEPCHECK PASS', 'WALK PASS', 'DUMP-BEGIN']),
        ('Probe_remove', 'pass', ['DEPCHECK-ABSENT ok', 'DEPCHECK PASS', 'WALK PASS', 'DUMP-BEGIN']),
        ('Control_remove', 'pass', ['ABSENT ok', 'SPELL ok', 'STMT-IDENTITY ok', 'DEPCHECK PASS']),
        ('Probe_keep', 'pass', ['DEPCHECK PASS', 'WALK PASS', 'WALK EXTRA-MODULES', 'DUMP-BEGIN', 'STMT-IDENTITY ok']),
        ('M_direct', 'fail', ['DEPCHECK-PAIR', 'DEPCHECK-MODULE', 'DEPCHECK-SIBLING', 'DEPCHECK-REQUIRED']),
        ('M_iff', 'fail', ['DEPCHECK-PAIR', 'DEPCHECK-PROVED-FROM OIBridge.EqvK2MaxCone.pairCone_eq_Q3_iff_drive_maxCone', 'DEPCHECK-MODULE']),
        ('M_inline', 'fail', ['DEPCHECK-MODULE', 'DEPCHECK-SIBLING', 'DEPCHECK-REQUIRED']),
        ('M_deadref', 'fail', ['DEPCHECK-PAIR', 'DEPCHECK-MODULE']),
        ('M_sibling', 'fail', ['DEPCHECK-SIBLING']),
        ('M_real', 'pass', ['DEPCHECK PASS']),
        ('M_required', 'fail', ['DEPCHECK-REQUIRED']),
        ('M_vac_target', 'fail', ['DEPCHECK-VACUOUS']),
        ('M_vac_sibling', 'fail', ['DEPCHECK-VACUOUS']),
        ('M_vac_module', 'fail', ['DEPCHECK-VACUOUS']),
        ('M_walk_effect', 'fail', ['WALK-EXTRA OIBridge.EffectSpace.', '<- FiniteReconstructionDesign.Mutation.sharpCone']),
        ('M_walk_required', 'fail', ['WALK-REQUIRED']),
        ('M_stmt_binder', 'fail', ['STMT-IDENTITY binder annotations differ']),
        ('M_stmt_hyp', 'fail', ['STMT-IDENTITY the statements are not alpha-equivalent']),
        ('M_absent_sibling', 'fail', ['DEPCHECK-ABSENT ok', 'DEPCHECK-SIBLING']),
        ('M_absent_on_keep', 'fail', ['ABSENT FAIL FiniteReachTable imports']),
    ]
    return files, expect


# --- generate ----------------------------------------------------------------------------------
def regime_sources(src):
    s = {f: (src / f).read_text(encoding='utf-8') for f in PINS}
    for f, h in PINS.items():
        got = hashlib.sha256((src / f).read_bytes()).hexdigest()
        if got != h:
            sys.exit(f'{f}: sha256 {got} is not the pinned {h}')
    assert s['FinitePauli.lean'].startswith(PAULI_L1)
    t = s['FiniteReachTable.lean'].splitlines(keepends=True)
    a, b = EVAL_SPAN
    assert t[a - 1] == EVAL_FIRST and t[b - 1] == EVAL_LAST, 'the #eval span moved'
    pinned = dict(s)
    remove = dict(s); remove['FinitePauli.lean'] = s['FinitePauli.lean'].replace(PAULI_L1, 'import OIBridge.EqvK2Generation\n', 1)
    keep = dict(s); keep['FinitePauli.lean'] = s['FinitePauli.lean'].replace(PAULI_L1, 'import OIBridge.EqvK2MaxCone\n', 1)
    keep['FiniteReachTable.lean'] = ''.join(t[:a - 1] + t[b:])
    return {'pinned': pinned, 'remove': remove, 'keep': keep}


def ledger(base, new):
    """The edit ledger of a regime against the pinned sources: (file, op, line, text) tuples."""
    out = []
    for f in sorted(base):
        a, b = base[f].splitlines(keepends=True), new[f].splitlines(keepends=True)
        for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(a=a, b=b, autojunk=False).get_opcodes():
            if tag != 'equal':
                out.append((f, tag, i1 + 1, i2, ''.join(a[i1:i2]), ''.join(b[j1:j2])))
    return out


FROZEN_LEDGER = {
    'pinned': [],
    'remove': [('FinitePauli.lean', 'replace', 1, 1, 'import OIBridge.EqvK2Schema\n', 'import OIBridge.EqvK2Generation\n')],
    'keep': [('FinitePauli.lean', 'replace', 1, 1, 'import OIBridge.EqvK2Schema\n', 'import OIBridge.EqvK2MaxCone\n'),
             ('FiniteReachTable.lean', 'delete', 1386, 1393, None, '')],
}


def generate(src, out):
    src, out = Path(src), Path(out)
    regs = regime_sources(src)
    for r, files in regs.items():
        got = ledger(regs['pinned'], files)
        want = FROZEN_LEDGER[r]
        ok = len(got) == len(want) and all(
            g[:4] == w[:4] and (w[4] is None or g[4] == w[4]) and g[5] == w[5] for g, w in zip(got, want))
        if not ok:
            sys.exit(f'LEDGER {r}: {got!r} is not the frozen {want!r}')
        d = out / r
        d.mkdir(parents=True, exist_ok=True)
        for f, text in files.items():
            (d / f).write_text(text, encoding='utf-8')
    (out / 'keep_i').mkdir(parents=True, exist_ok=True)
    (out / 'keep_i' / 'FiniteReachTableImportOnly.lean').write_text(regs['pinned']['FiniteReachTable.lean'], encoding='utf-8')
    thms = []
    for m in DESIGN_MODULES:
        names = theorems(regs['pinned'][m + '.lean'])
        if len(names) != EXPECTED_THEOREMS[m]:
            sys.exit(f'{m}: {len(names)} theorems parsed, expected {EXPECTED_THEOREMS[m]}')
        thms += names
    files, expect = cases(thms)
    texts = {}
    (out / 'cases').mkdir(parents=True, exist_ok=True)
    for name, (regime, text) in files.items():
        twins = [n for n, x in texts.items() if x == text and n.startswith('M_')]
        if name.startswith('M_') and twins:
            sys.exit(f'CASE {name} is byte-identical to {twins[0]}: a mutation that mutates nothing')
        texts[name] = text
        (out / 'cases' / f'{name}.lean').write_text(text, encoding='utf-8')
    assert [n for n, _, _ in expect] == list(files), 'expectations and cases differ'
    manifest = sorted(p for p in out.rglob('*.lean'))
    with open(out / 'GENERATED.SHA256SUMS', 'w', encoding='utf-8') as fh:
        for p in manifest:
            fh.write(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(out)}\n')
    for r in regs:
        print(f'LEDGER {r}: {len(FROZEN_LEDGER[r])} edit(s), as frozen')
    print(f'generated {len(manifest)} files in {out}: 3 regimes, keep_i, {len(files)} cases; {len(thms)} theorem names')


# --- run ---------------------------------------------------------------------------------------
AX = re.compile(r"'([^']+)' (depends on axioms: \[[^\]]*\]|does not depend on any axioms)")
ERR = re.compile(r':\d+:\d+: error')


def path_guard(lean_path, regime_dir):
    hits = []
    for d in lean_path.split(':'):
        if not d or Path(d).resolve() == regime_dir.resolve():
            continue
        for m in OLEAN | {'FiniteWalsh'}:
            if (Path(d) / f'{m}.olean').exists():
                hits.append(f'{d}/{m}.olean')
    return hits


def lean(path, olean, env, log):
    cmd = ['lean'] + (['-o', str(path.with_suffix('.olean'))] if olean else []) + [str(path)]
    r = subprocess.run(cmd, capture_output=True, text=True, env=env)
    text = f'exit={r.returncode}\n' + r.stdout + r.stderr
    log.write_text(text, encoding='utf-8')
    return r.returncode, text


def axiom_lines(text):
    return [m.group(0) for m in AX.finditer(text)]


def stmt_lines(text):
    return sorted(l for l in text.splitlines() if l.startswith('STMT '))


def run(out):
    out = Path(out).resolve()
    base_path = os.environ.get('LEAN_PATH', '')
    results, bad = {}, []
    for regime in ('pinned', 'remove', 'keep'):
        d = out / regime
        hits = path_guard(base_path, d)
        if hits:
            bad.append(f'PATH-GUARD {regime}: {hits}')
        env = dict(os.environ, LEAN_PATH=base_path + ':' + str(d))
        for m in CHAIN:
            code, text = lean(d / f'{m}.lean', m in OLEAN, env, d / f'{m}.out')
            results[(regime, m)] = (code, text)
    env_k = dict(os.environ, LEAN_PATH=base_path + ':' + str(out / 'keep'))
    results[('keep_i', 'FiniteReachTable')] = lean(out / 'keep_i' / 'FiniteReachTableImportOnly.lean', False, env_k,
                                                   out / 'keep_i' / 'FiniteReachTableImportOnly.out')
    files, expect = cases([])  # names only; texts were generated
    for name, kind, codes in expect:
        regime = files[name][0]
        env = dict(os.environ, LEAN_PATH=base_path + ':' + str(out / regime))
        code, text = lean(out / 'cases' / f'{name}.lean', False, env, out / 'cases' / f'{name}.out')
        failed = code != 0 or bool(ERR.search(text))
        ok = (not failed) if kind == 'pass' else failed
        ok = ok and all(c in text for c in codes)
        results[('case', name)] = (code, text)
        print(f"{'OK ' if ok else 'BAD'} {name:20s} {regime:7s} expect={kind:4s} exit={code}")
        if not ok:
            bad.append(('MEASURE ' if name in MEASUREMENTS else 'CONTROL ') + name)
    # builds
    for regime in ('pinned', 'remove', 'keep'):
        for m in CHAIN:
            code, text = results[(regime, m)]
            n = len(ERR.findall(text))
            print(f'BUILD {regime:6s} {m:17s} exit={code} errors={n}')
            if code != 0 or n:
                bad.append(f'BUILD {regime} {m}')
    code, text = results[('keep_i', 'FiniteReachTable')]
    errs = ERR.findall(text)
    one = len(errs) == 1 and 'is in the environment' in text
    print(f'BUILD keep_i FiniteReachTable exit={code} errors={len(errs)} (expected exactly the #eval)')
    # comparisons
    cmp = {}
    for m in CHAIN:
        a = {r: axiom_lines(results[(r, m)][1]) for r in ('pinned', 'remove', 'keep')}
        for r, xs in a.items():
            if len(xs) != EXPECTED_AXIOM_LINES[m]:
                bad.append(f'AXIOM-COUNT {r} {m}: {len(xs)} lines, expected {EXPECTED_AXIOM_LINES[m]}')
        cmp[('ax', m, 'keep=remove')] = a['keep'] == a['remove']
        cmp[('ax', m, 'remove=pinned')] = a['remove'] == a['pinned']
    cmp[('ax', 'FiniteReachTable', 'keep_i=keep')] = axiom_lines(text) == axiom_lines(results[('keep', 'FiniteReachTable')][1])
    s = {r: stmt_lines(results[('case', f'Probe_{r}')][1]) for r in ('pinned', 'remove', 'keep')}
    cmp[('stmt', 'all', 'keep=remove')] = s['keep'] == s['remove'] and len(s['keep']) > 0
    cmp[('stmt', 'all', 'remove=pinned')] = s['remove'] == s['pinned'] and len(s['remove']) > 0
    for k, v in cmp.items():
        print(f"COMPARE {' '.join(k)}: {'identical' if v else 'DIFFERENT'}")
    walk_keep_extra = 'WALK-EXTRA' in results[('case', 'Probe_keep')][1]
    m = re.search(r'WALK EXTRA-MODULES \((\d+)\): (\[.*?\])', results[('case', 'Probe_keep')][1])
    print('EXTRA', m.group(0) if m else 'not printed')
    st = selftest(quiet=True)
    if not st:
        bad.append('SELFTEST')
    builds_clean = not any(b.startswith('BUILD') for b in bad) and one
    measured = not any(b.startswith('MEASURE') for b in bad)
    if [b for b in bad if b.startswith(('CONTROL', 'PATH-GUARD', 'AXIOM-COUNT', 'SELFTEST'))]:
        verdict = 'IMPORT-BRIDGE-VOID'
    elif walk_keep_extra:
        verdict = 'IMPORT-USED'
    elif builds_clean and measured and all(v for k, v in cmp.items() if k[2] in ('keep=remove', 'keep_i=keep')):
        verdict = 'IMPORT-REDUNDANT-IN-DESIGN'
    elif builds_clean:
        verdict = 'IMPORT-NOT-TRANSPARENT'
    else:
        verdict = 'IMPORT-BRIDGE-INCONCLUSIVE'
    print('\n'.join('UNEXPECTED ' + b for b in bad))
    print(f'IMPORT-BRIDGE cases: {len(expect)}, unexpected: {len(bad)}')
    print('VERDICT', verdict)
    sys.exit(0 if verdict == 'IMPORT-REDUNDANT-IN-DESIGN' else 1)


# --- comparator self-test (pure Python) -----------------------------------------------------------
def selftest(quiet=False):
    ax = "x.lean:1:0: info: 'A.b' depends on axioms: [propext, Classical.choice, Quot.sound]\n"
    ok = []
    ok.append(axiom_lines(ax) == ["'A.b' depends on axioms: [propext, Classical.choice, Quot.sound]"])
    ok.append(axiom_lines(ax) != axiom_lines(ax.replace('Quot.sound', 'Quot.sound, sorryAx')))
    ok.append(axiom_lines(ax) != axiom_lines(ax.replace("'A.b'", "'A.c'")))
    ok.append(axiom_lines(ax + ax) != axiom_lines(ax))
    d = 'DUMP-BEGIN\nSTMT M A.b theorem [] : ∀ {K : T}, P K\nVALUEHASH A.b 1\nDUMP-END\n'
    ok.append(stmt_lines(d) != stmt_lines(d.replace('{K : T}', '(K : T)')))
    ok.append(stmt_lines(d) == stmt_lines(d.replace('VALUEHASH A.b 1', 'VALUEHASH A.b 2')))
    ok.append(stmt_lines(d) != stmt_lines(d.replace('STMT M A.b', 'STMT M A.c')))
    ok.append(ERR.search('f.lean:3:4: error: x') is not None and ERR.search('f.lean:3:4: info: x') is None)
    res = all(ok)
    if not quiet:
        print(f"SELFTEST {'OK' if res else 'FAIL'} ({sum(ok)}/{len(ok)})")
    return res


if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'generate':
        generate(sys.argv[2], sys.argv[3])
    elif cmd == 'run':
        run(sys.argv[2])
    elif cmd == 'selftest':
        sys.exit(0 if selftest() else 1)
    elif cmd == 'rule':
        print(VERDICT_RULE)
