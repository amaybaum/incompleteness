#!/usr/bin/env python3
"""Round BG-2 -- the round's own static controls (stage 1).

It reads nothing but the repository, through git, and certifies nothing on its own: the Lean kernel,
the axiom audit and the release gate establish the mathematics, and the V3 verifier the protocol.
What it checks is that the execution carries the frozen statement surface, the frozen proof shape of
the refutation, none of the excluded phrases, and no change outside the governed paths.

    python3 -I controls.py --self-test                    mutation controls on the module text and on
                                                          synthetic inputs; constants against the
                                                          preregistration beside this file
    python3 -I controls.py check <E> --freeze <F>         C1, S1, S2, S3, S4 and G against the tree at E
    python3 -I controls.py verdict <E> --freeze <F> [--axioms LOG]
                                                          the three cell tokens from the measurements at
                                                          E: the static controls, the probe blob at E run
                                                          with python3 -I, and the axiom reports of the
                                                          exact-head build log

Exit 1 on any failure.
"""
import os
import re
import subprocess
import sys
import tempfile

D = '3519213a47c2c63f7ece3f55a81acffc2a96a3af'
RDIR = 'verification/programmes/oi-qm/reconstruction/round-bg-2-premise-orientation/'
PREREG = RDIR + 'preregistration.md'
RESULT = RDIR + 'result.md'
MODULE = 'verification/lean-mathlib/OIBridge/TurnpikePremiseOrientation.lean'
PROBE = 'verification/lean/bg2_orientation_probe.py'
BG1_DIR = 'verification/programmes/oi-qm/reconstruction/round-bg-1-integer-classification/'
LEGACY = 'verification/infrastructure/legacy-records.json'
NS = 'OIBridge.PremiseOrientation'

PREAMBLE = ['import OIBridge.TurnpikeScopeTransfer', 'import OIBridge.PiccardBridge',
            'namespace OIBridge.PremiseOrientation', 'open ScopeTransfer HomometricSix',
            'set_option maxRecDepth 100000', 'set_option maxHeartbeats 0']
END = 'end OIBridge.PremiseOrientation'
NAMES = ['r2refl', 'hyps_r1_r2refl', 'source_difference_cases', 'reflected_difference_obstruction',
         'not_muForm_r1_r2refl', 'not_BGIntegerClassification', 'muForm_r1_r2', 'revMuForm_r1_r2refl']
PRINTS = NAMES[1:]
# landed objects at D: (file, line, declaration head)
LANDED = [
    ('verification/lean-mathlib/OIBridge/TurnpikeScopeTransfer.lean', 542, 'def BGIntegerClassification'),
    ('verification/lean-mathlib/OIBridge/TurnpikeScopeTransfer.lean', 309, 'AscPair'),
    ('verification/lean-mathlib/OIBridge/HomometricSix.lean', 51, 'def r1'),
    ('verification/lean-mathlib/OIBridge/HomometricSix.lean', 55, 'def r2'),
    ('verification/lean-mathlib/OIBridge/HomometricSix.lean', 59, 'def mu'),
    ('verification/lean-mathlib/OIBridge/HomometricSix.lean', 77, 'theorem golomb_r1'),
    ('verification/lean-mathlib/OIBridge/HomometricSix.lean', 81, 'theorem golomb_r2'),
    ('verification/lean-mathlib/OIBridge/HomometricSix.lean', 85, 'theorem mu_gap'),
    ('verification/lean-mathlib/OIBridge/PiccardBridge.lean', 50, 'def piccardX'),
    ('verification/lean-mathlib/OIBridge/PiccardBridge.lean', 56, 'def piccardY'),
]
PHRASES = ['the classification is false', 'Bekir–Golomb is refuted', 'Bekir-Golomb is refuted',
           'the two-branch theorem is false', 'the premise is removed', 'the premise is discharged',
           'kernel proof of']
ALLOWED_AXIOMS = {'propext', 'Classical.choice', 'Quot.sound'}

FAIL = []


def report(name, ok, detail=''):
    print(('PASS ' if ok else 'FAIL ') + name + (('  ' + detail) if detail else ''))
    if not ok:
        FAIL.append(name)
    return ok


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


# ---------------------------------------------------------------- the frozen surface, from the preregistration

def frozen_block(prereg):
    m = re.search(r'## The proposed statement surface.*?```lean\n(.*?)```', prereg, re.S)
    return m.group(1) if m else ''


def split_decls(text):
    """[(kind, name, signature)] for each top-level def/theorem; the signature stops at the first ':=' for a
    theorem (its proof is not part of the surface) and runs to the end of the line for a def."""
    out = []
    for m in re.finditer(r'^(def|theorem|lemma|abbrev|instance|axiom|opaque)\s+([A-Za-z_][\w.\']*)(.*?)(?=^\S|\Z)',
                         text, re.M | re.S):
        kind, name, rest = m.group(1), m.group(2), m.group(3)
        if kind == 'def':
            sig = flat(rest.split('\n')[0])
        else:
            sig = flat(rest.split(':=')[0])
        out.append((kind, name, sig, rest))
    return out


def governed(prereg):
    m = re.search(r'```v3-governed-paths\n(.*?)```', prereg, re.S)
    return [ln.split()[-1] for ln in m.group(1).strip().splitlines()] if m else []


# ---------------------------------------------------------------- the controls

def s1(module, frozen):
    ok = True
    lines = [ln.strip() for ln in module.splitlines()]
    code = [ln for ln in lines if ln and not ln.startswith('--')]
    # preamble: in order, outside the module docstring
    body = re.sub(r'/-!.*?-/', '', module, flags=re.S)
    blines = [ln.strip() for ln in body.splitlines() if ln.strip()]
    ok &= blines[:2] == PREAMBLE[:2] and blines[2:6] == PREAMBLE[2:] and blines[-1] == END
    want = [(k, n, s) for k, n, s, _ in split_decls(frozen)]
    have = [(k, n, s) for k, n, s, _ in split_decls(body)]
    ok &= [n for _, n, _ in want] == NAMES and have == want
    prints = [ln for ln in blines if ln.startswith('#print')]
    ok &= prints == ['#print axioms ' + n for n in PRINTS]
    ok &= not any(t in body for t in ('sorry', 'native_decide', 'admit', 'axiom '))
    return bool(ok)


def s3(module):
    decls = {n: rest for _, n, _, rest in split_decls(re.sub(r'/-!.*?-/', '', module, flags=re.S))}
    proof = decls.get('not_BGIntegerClassification', '').split(':=', 1)
    proof = proof[1] if len(proof) == 2 else ''
    return 'hyps_r1_r2refl' in proof and 'not_muForm_r1_r2refl' in proof and 'BGIntegerClassification' in \
        decls.get('not_BGIntegerClassification', '')


def s4(texts):
    hits = [(name, p) for name, t in texts for p in PHRASES if t and p.lower() in t.lower()]
    return hits


def header_of(module):
    m = re.search(r'/-!(.*?)-/', module, re.S)
    return m.group(1) if m else ''


def g(diff_lines, paths):
    bad = []
    for ln in diff_lines:
        if not ln.strip():
            continue
        status, path = ln.split('\t', 1)
        inside = any(path == p or (p.endswith('/') and path.startswith(p)) for p in paths) or path == PREREG
        if not inside or path.startswith(BG1_DIR) or path == LEGACY:
            bad.append(ln)
    return bad


def s2(E):
    ok = True
    for path, line, head in LANDED:
        bd, be = blob(D, path), blob(E, path)
        text = show(E, path) or ''
        at = text.splitlines()[line - 1] if len(text.splitlines()) >= line else ''
        found = head in at
        ok &= bd is not None and bd == be and found
        if not (bd == be and found):
            print('      S2 miss: %s:%d %r (blob at D %s, at E %s)' % (path, line, head, bd, be))
    return bool(ok)


def check(E, F):
    prereg_F, prereg_E = show(F, PREREG), show(E, PREREG)
    module = show(E, MODULE) or ''
    report('C1 the preregistration at E is the one at F', prereg_F is not None and prereg_F == prereg_E)
    frozen = frozen_block(prereg_F or '')
    report('S1 surface: preamble, the eight frozen declarations in order, the seven prints', s1(module, frozen))
    report('S2 the landed objects resolve at D\'s blobs and lines', s2(E))
    report('S3 the refutation names the premise and its two lemmas', s3(module))
    hits = s4([('module header', header_of(module)), ('result note', show(E, RESULT))])
    report('S4 no excluded phrase in the module header or the result note', not hits, str(hits) if hits else '')
    diff = git('diff', '--no-renames', '--name-status', D, E).splitlines()
    bad = g(diff, governed(prereg_F or ''))
    report('G every change from D to E lies in the governed paths; BG-1 and the legacy manifest untouched',
           not bad, str(bad) if bad else '%d paths' % len([d for d in diff if d.strip()]))
    return not FAIL


def run_probe(E):
    with tempfile.TemporaryDirectory() as tmp:
        arch = subprocess.run(['git', 'archive', E, 'verification/lean/bg2_orientation_probe.py',
                               'verification/lean-mathlib/OIBridge/HomometricSix.lean',
                               'verification/lean-mathlib/OIBridge/PiccardBridge.lean'],
                              capture_output=True, check=True).stdout
        subprocess.run(['tar', '-x', '-C', tmp], input=arch, check=True)
        r = subprocess.run([sys.executable, '-I', os.path.join(tmp, PROBE)], capture_output=True, text=True)
        return r.stdout


def axioms_from(log):
    rep = {}
    for m in re.finditer(r"'%s\.([\w']+)' depends on axioms: \[([^\]]*)\]" % re.escape(NS), log):
        rep[m.group(1)] = {a.strip() for a in m.group(2).split(',') if a.strip()}
    for m in re.finditer(r"'%s\.([\w']+)' does not depend on any axioms" % re.escape(NS), log):
        rep[m.group(1)] = set()
    return rep


def verdict(E, F, axlog):
    static = check(E, F)
    out = run_probe(E)
    print(out.rstrip())
    exact = (all(('PASS %s ' % c) in out for c in ('O0', 'O1', 'O2', 'O3', 'O4', 'O5', 'K1', 'K2'))
             and 'FAIL' not in out and 'checks: 8, failures: 0' in out
             and 'VERDICT PREMISE-ORIENTATION-EXACT' in out)
    ax = axioms_from(open(axlog, encoding='utf-8').read()) if axlog else {}
    bad_tok = ('sorryAx', 'Lean.ofReduceBool')

    def clean(n):
        return n in ax and ax[n] <= ALLOWED_AXIOMS and not any(t in ax[n] for t in bad_tok)
    s_ok = 'S1' not in ''.join(FAIL) and 'S2' not in ''.join(FAIL)
    ref = s_ok and 'S3' not in ''.join(FAIL) and all(clean(n) for n in
                                                     ('hyps_r1_r2refl', 'not_muForm_r1_r2refl',
                                                      'not_BGIntegerClassification'))
    ctrl = s_ok and all(clean(n) for n in ('muForm_r1_r2', 'revMuForm_r1_r2refl'))
    print('axiom reports read: %s' % (sorted(ax) if ax else 'none (no --axioms log)'))
    print('TOKEN Q-REF   %s' % ('BG-2-PREMISE-REFUTED' if ref else 'BG-2-PREMISE-UNDECIDED'))
    print('TOKEN Q-CTRL  %s' % ('BG-2-CONTROLS-PROVED' if ctrl else 'BG-2-CONTROLS-NOT-ESTABLISHED'))
    print('TOKEN Q-EXACT %s' % ('BG-2-ORIENTATION-EXACT' if exact else 'BG-2-ORIENTATION-NOT-ESTABLISHED'))
    if ref and ctrl and exact and static:
        print('EARNED READING: BGIntegerClassification as stated at TurnpikeScopeTransfer.lean:542 is false: '
              'the six-mark integer rulers (0,1,4,10,12,17), (0,4,6,9,16,17) satisfy its hypotheses, no '
              'relabelings realize mu in the orientation its conclusion fixes, and the pair realizes mu '
              'reversed.')
    return static


# ---------------------------------------------------------------- self-test

def self_test():
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.abspath(os.path.join(here, '..', '..', '..', '..', '..'))
    prereg = open(os.path.join(here, 'preregistration.md'), encoding='utf-8').read()
    module = open(os.path.join(root, MODULE), encoding='utf-8').read()
    frozen = frozen_block(prereg)
    report('self: D agrees with the preregistration', ('D: ' + D) in prereg)
    gp = governed(prereg)
    report('self: governed paths parsed (7) and include the module, the probe and the record directory',
           len(gp) == 7 and MODULE in gp and PROBE in gp and RDIR in gp)
    report('self: the frozen block declares the eight names in order',
           [n for _, n, _, _ in split_decls(frozen)] == NAMES)
    report('self: S1 accepts the module', s1(module, frozen))
    report('self: S3 accepts the module', s3(module))
    report('self: S4 finds nothing in the module header', not s4([('header', header_of(module))]))
    muts = [
        ('r2 for r2refl in not_muForm_r1_r2refl',
         lambda t: t.replace('theorem not_muForm_r1_r2refl : ¬ ∃ eS eT : Fin 6 ≃ Fin 6, ∀ a b : Fin 6, a < b →\n'
                             '    r2refl (eT (mu a b).2) - r2refl (eT (mu a b).1)',
                             'theorem not_muForm_r1_r2refl : ¬ ∃ eS eT : Fin 6 ≃ Fin 6, ∀ a b : Fin 6, a < b →\n'
                             '    r2 (eT (mu a b).2) - r2 (eT (mu a b).1)', 1)),
        ('the reflection clause dropped from hyps_r1_r2refl',
         lambda t: t.replace(' ∧ (¬ ∃ c : ℤ, ∀ i, r2refl i = c - r1 i.rev) := by', ' := by', 1)),
        ('the unreversed sign in revMuForm_r1_r2refl',
         lambda t: t.replace('= r1 (eS a) - r1 (eS b) := by', '= r1 (eS b) - r1 (eS a) := by', 1)),
        ('the premise restated by hand in not_BGIntegerClassification',
         lambda t: t.replace('theorem not_BGIntegerClassification : ¬ BGIntegerClassification := by',
                             'theorem not_BGIntegerClassification : ¬ ∀ n : ℕ, n = n := by', 1)),
        ('an eighth print',
         lambda t: t.replace('#print axioms revMuForm_r1_r2refl\n',
                             '#print axioms revMuForm_r1_r2refl\n#print axioms r2refl\n', 1)),
    ]
    for name, f in muts:
        mt = f(module)
        report('self: S1 rejects the mutation: ' + name, mt != module and not s1(mt, frozen))
    m3 = module.replace('  obtain ⟨hmono, hmono\', hgap, hgap\', hsets, htr, hrf⟩ := hyps_r1_r2refl\n'
                        '  exact not_muForm_r1_r2refl (hBG 6 r1 r2refl hmono hmono\' hgap hgap\' hsets htr hrf)',
                        '  exact absurd hBG (by sorry)', 1)
    report('self: S3 rejects a refutation naming neither lemma', m3 != module and not s3(m3))
    report('self: S4 flags each excluded phrase',
           all(s4([('x', 'Here ' + p + ' at six marks.')]) for p in PHRASES))
    bad = g(['M\tpapers/GR.md', 'A\t' + BG1_DIR + 'x.md', 'M\t' + LEGACY, 'A\t' + MODULE], gp)
    report('self: G flags a manuscript, a BG-1 file and the legacy manifest, and passes the module',
           len(bad) == 3 and not any(MODULE in b for b in bad))
    return not FAIL


def main(argv):
    if argv[:1] == ['--self-test']:
        ok = self_test()
    elif argv[:1] == ['check'] and len(argv) >= 4 and argv[2] == '--freeze':
        ok = check(argv[1], argv[3])
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
