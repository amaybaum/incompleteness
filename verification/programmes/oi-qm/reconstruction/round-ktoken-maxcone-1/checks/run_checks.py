#!/usr/bin/env python3
"""KTOKEN-MAXCONE-1 check A3: the positive check file and its mutation cases, both directions.

  python3 -I -B run_checks.py generate <out-dir>   # pure Python: writes the case files
  python3 -I -B run_checks.py self-test            # pure Python: generation and the outcome rule
  lake env python3 -I -B <path>/run_checks.py run  # from verification/lean-mathlib, library built

The cases are generated from KTokenPairCheck.lean, beside this file; every substitution must apply
exactly once. `run` compiles each case with `lean` and exits 1 unless every case has its expected
outcome: the positive file and the harness control M_real compile with their markers and no
error; every mutation fails to compile and prints each of its expected codes. A missing `lean`, a
timeout or an unexpected outcome fails the run; nothing is skipped.
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
POSITIVE = HERE / 'KTokenPairCheck.lean'
REC = 'OIBridge.KTokenMaxCone.pairCone_eq_Q3_of_kToken'
MUT = 'KTokenMaxConeCheck.Mutation.pairCone_eq_Q3_of_kToken'
ARGS = 'hH1 hadd hsmul hmax hH2 hA'
REAL = f'  {REC} {ARGS}'
IMPORTS = 'import OIBridge.KTokenMaxCone\nimport OIBridge.EqvK2MaxCone\n\n'
ERROR = re.compile(r':\d+:\d+: error')
STMT_MARK = '/- Executable control STMT-IDENTITY'
DEP_MARK = '/- Executable control DEPCHECK'
TARGET_LINE = f'  let target : Lean.Name := `{REC}\n'
MUT_HEAD = '''namespace KTokenMaxConeCheck.Mutation

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

end KTokenMaxConeCheck.Mutation

'''


def sub(text, old, new):
    if text.count(old) != 1:
        raise SystemExit(f'GENERATE substitution does not apply exactly once: {old!r}')
    return text.replace(old, new)


def parts():
    text = POSITIVE.read_text(encoding='utf-8')
    head, sep, rest = text.partition(STMT_MARK)
    stmt, sep2, dep = rest.partition(DEP_MARK)
    if not sep or not sep2 or IMPORTS.strip() not in head:
        raise SystemExit('GENERATE the positive check file lacks its imports or sections')
    return STMT_MARK + stmt, DEP_MARK + dep


def mutant(proof, binder='{K : Set (W 3)}', extra=''):
    return IMPORTS + MUT_HEAD.replace('@@BINDER@@', binder).replace('@@EXTRA@@', extra) \
        .replace('@@PROOF@@', proof)


def dep_for(dep, target=MUT, siblings_typo=False, module_typo=False):
    d = sub(dep, TARGET_LINE, f'  let target : Lean.Name := `{target}\n')
    if siblings_typo:
        d = sub(d, '`OIBridge.EqvK2Schema.Q3_subset_of_pure,', '`OIBridge.EqvK2Schema.Q3_subset_of_puree,')
    if module_typo:
        d = sub(d, '#[`OIBridge.EqvK2MaxCone]', '#[`OIBridge.EqvK2MaxCon]')
    return d


def stmt_for(stmt):
    s = sub(stmt, f'type_of% @{REC} =', f'type_of% @{MUT} =')
    return sub(s, f'getConstInfo `{REC}\n', f'getConstInfo `{MUT}\n')


def cases():
    """name -> (source, expectation, codes); expectation is 'pass' or 'fail'."""
    stmt, dep = parts()
    pos = POSITIVE.read_text(encoding='utf-8')
    return {
        'Positive': (pos, 'pass', ['STMT-IDENTITY ok', f'DEPCHECK PASS {REC}']),
        'M_real': (mutant(REAL) + dep_for(dep), 'pass', [f'DEPCHECK PASS {MUT}']),
        'M_direct': (mutant(f'  OIBridge.EqvK2MaxCone.pairCone_eq_Q3_of_drive_maxCone {ARGS}') + dep_for(dep),
                     'fail', ['DEPCHECK-PAIR', 'DEPCHECK-MODULE', 'DEPCHECK-SIBLING', 'DEPCHECK-REQUIRED']),
        'M_iff': (mutant('  (OIBridge.EqvK2MaxCone.pairCone_eq_Q3_iff_drive_maxCone hH1 hadd hsmul hmax).2 ⟨hH2, hA⟩')
                  + dep_for(dep), 'fail',
                  ['DEPCHECK-PAIR', 'DEPCHECK-PROVED-FROM OIBridge.EqvK2MaxCone.pairCone_eq_Q3_iff_drive_maxCone',
                   'DEPCHECK-MODULE']),
        'M_inline': (mutant('  OIBridge.EqvK2MaxCone.pairCone_eq_Q3_of_block_maxCone hH1 hadd hsmul hmax\n'
                            '    (OIBridge.EqvK2Generation.blockInvariant_of_drive hH2 hA)') + dep_for(dep),
                     'fail', ['DEPCHECK-MODULE', 'DEPCHECK-SIBLING', 'DEPCHECK-REQUIRED']),
        'M_deadref': (mutant(f'  by\n    have _x := OIBridge.EqvK2MaxCone.pairCone_eq_Q3_of_drive_maxCone {ARGS}\n'
                             f'    exact {REC} {ARGS}') + dep_for(dep), 'fail', ['DEPCHECK-PAIR', 'DEPCHECK-MODULE']),
        'M_sibling': (mutant(f'  by\n    have _x := OIBridge.EqvK2Generation.blockInvariant_of_drive hH2 hA\n'
                             f'    exact {REC} {ARGS}') + dep_for(dep), 'fail', ['DEPCHECK-SIBLING']),
        'M_required': (mutant(REAL) + dep_for(dep, target='OIBridge.KTokenMaxCone.mem_Q3_iff_pairCarrier'),
                       'fail', ['DEPCHECK-REQUIRED']),
        'M_vac_target': (mutant(REAL) + dep_for(dep, target=MUT + 'X'), 'fail', ['DEPCHECK-VACUOUS']),
        'M_vac_sibling': (mutant(REAL) + dep_for(dep, siblings_typo=True), 'fail', ['DEPCHECK-VACUOUS']),
        'M_vac_module': (mutant(REAL) + dep_for(dep, module_typo=True), 'fail', ['DEPCHECK-VACUOUS']),
        'M_stmt_binder': (mutant(f'  @{REC} K {ARGS}', binder='(K : Set (W 3))') + stmt_for(stmt), 'fail',
                          ['STMT-IDENTITY binder annotations differ']),
        'M_stmt_hyp': (mutant(REAL, extra='\n    (hextra : True)') + stmt_for(stmt), 'fail',
                       ['STMT-IDENTITY the statements are not alpha-equivalent']),
    }


def judge(name, expectation, codes, returncode, output):
    """The frozen outcome rule; returns a list of problems (empty = as expected)."""
    bad = []
    if expectation == 'pass':
        if returncode != 0:
            bad.append(f'{name}: expected to compile, exit {returncode}')
        if ERROR.search(output):
            bad.append(f'{name}: error text in a clean compile')
    else:
        if returncode == 0:
            bad.append(f'{name}: mutation compiled (accepted)')
    for c in codes:
        if c not in output:
            bad.append(f'{name}: missing {c!r}')
    return bad


def generate(out):
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    cs = cases()
    for name, (src, _, _) in cs.items():
        (out / f'{name}.lean').write_text(src, encoding='utf-8')
    return cs


def self_test():
    cs = cases()
    probs = []
    names = [n for n in cs if n.startswith('M_')]
    if len(names) != 12 or sum(1 for n in cs if cs[n][1] == 'fail') != 11:
        probs.append('case inventory')
    for name, (src, exp, codes) in cs.items():
        if '@@' in src or IMPORTS not in src or not codes or (name.startswith('M_') and not src.startswith(IMPORTS)):
            probs.append(f'{name}: malformed')
        if name.startswith('M_') and src.count('#eval') != 1:
            probs.append(f'{name}: expected exactly one check section')
    # the outcome rule, against synthetic outcomes: each must be rejected
    synthetic = [('Positive', 'pass', ['STMT-IDENTITY ok'], 1, 'STMT-IDENTITY ok'),
                 ('Positive', 'pass', ['STMT-IDENTITY ok', 'DEPCHECK PASS'], 0, 'STMT-IDENTITY ok'),
                 ('M_direct', 'fail', ['DEPCHECK-PAIR'], 0, 'DEPCHECK-PAIR'),
                 ('M_direct', 'fail', ['DEPCHECK-PAIR'], 1, 'unknown identifier'),
                 ('M_real', 'pass', ['DEPCHECK PASS'], 0, 'M.lean:3:4: error: x\nDEPCHECK PASS')]
    for case in synthetic:
        if not judge(*case):
            probs.append(f'outcome rule accepted {case[:2]} rc={case[3]}')
    if judge('M_sibling', 'fail', ['DEPCHECK-SIBLING'], 1, 'error: DEPCHECK FAIL\nDEPCHECK-SIBLING x'):
        probs.append('outcome rule rejected a correct mutation outcome')
    if probs:
        print('\n'.join('SELF-TEST FAIL ' + p for p in probs))
        return 1
    print(f'SELF-TEST OK: {len(cs)} cases ({len(names)} mutation-harness cases), outcome rule rejects 5/5 '
          'synthetic defects and accepts the correct outcome')
    return 0


def run():
    lean = 'lean'
    with tempfile.TemporaryDirectory() as tmp:
        cs = generate(tmp)
        problems = []
        for name, (_, exp, codes) in cs.items():
            path = Path(tmp) / f'{name}.lean'
            try:
                r = subprocess.run([lean, str(path)], capture_output=True, text=True, timeout=1800)
            except FileNotFoundError:
                print('RUN FAIL: no lean on PATH (run under `lake env`)')
                return 1
            except subprocess.TimeoutExpired:
                problems.append(f'{name}: timeout')
                continue
            out = r.stdout + r.stderr
            print(f'::group::{name} (exit {r.returncode})')
            print(out)
            print('::endgroup::')
            bad = judge(name, exp, codes, r.returncode, out)
            problems += bad
            print(f"{'OK  ' if not bad else 'BAD '} {name} expected {exp}")
        if problems:
            print('\n'.join('A3 FAIL ' + p for p in problems))
            print('A3-CHECK-NOT-ESTABLISHED')
            return 1
        print(f'A3-CHECK-NONVACUOUS: {len(cs)} cases as expected')
        return 0


def main():
    if len(sys.argv) >= 2 and sys.argv[1] == 'self-test':
        sys.exit(self_test())
    if len(sys.argv) == 3 and sys.argv[1] == 'generate':
        generate(sys.argv[2]); print('generated', len(cases()), 'cases'); return
    if len(sys.argv) == 2 and sys.argv[1] == 'run':
        sys.exit(run())
    print(__doc__); sys.exit(2)


if __name__ == '__main__':
    main()
