#!/usr/bin/env python3
"""Runs the checks that read the edited files on the simulated post-deletion tree. Planning tooling: it writes
only a temporary copy of the tree, outside the repository, and never a manuscript.

Usage (from the repository root):
  python3 -I -B verification/audits/foundations/a1exit-deletion-20261121/guards_check.py [--rev REV] [--mutants] [--keep DIR]

The tree of REV (default: the drafting base of edits.json) is written to a temporary directory from the object
store (`git cat-file --batch`, every tracked file, including the paths `.gitattributes` marks export-ignore), the
edit list is applied to it, and each check of CHECKS runs there with its own working directory. The run passes when
every check exits 0 on the simulated tree and every countercontrol fails as named:

  CC-1  the guard-pin edit D302 omitted, its target edit applied: the R7 guard fails (a pin left at the old text);
  CC-2  every edit applied, then the literal D302 pins removed from its target verification/README.md: the R7
        guard fails (an updated pin missing from its simulated target);
  CC-3  the glossary edit D220 omitted, its pin D306 applied: the R7 guard fails (a target edit missing);
  CC-4  the guard-pin edit D301 omitted: bohr_frequency_probe.py fails (guard F71).

--mutants  additionally runs, for every retained A1 string literal of the two guards (PINS), a mutation of its
           named target: a positive pin's literal is removed from the target, a negative pin's literal is inserted
           into it. The pin passes its test against that target when the guard passes on the simulated tree and
           fails under the mutation. The failing check tags are printed as the evidence.
"""
import argparse, importlib.util, os, re, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
_spec = importlib.util.spec_from_file_location('edits_check', os.path.join(HERE, 'edits_check.py'))
ec = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ec)

R7 = 'verification/lean/edge_rigidity_probe.py'
F71 = 'verification/lean/bohr_frequency_probe.py'
# (name, working directory, argv): the two guards that pin edited text, and the bounded checks that read an
# edited file and run without a Lean toolchain or repository history.
CHECKS = [
    ('R7 guard', 'verification/lean', ['edge_rigidity_probe.py']),
    ('F71 guard', 'verification/lean', ['bohr_frequency_probe.py']),
    ('repertoire_lie', 'verification/lean', ['repertoire_lie_probe.py']),
    ('wave_period', 'verification/lean', ['wave_period_probe.py']),
    ('gap_correspondence', 'verification/lean', ['gap_correspondence_probe.py']),
    ('stinespring_scope', 'verification/lean', ['stinespring_scope_probe.py']),
    ('canonical_measure', 'verification/lean', ['canonical_measure_probe.py']),
    ('structural_chain', 'verification/lean', ['structural_chain_probe.py']),
    ('structural_core', 'verification/lean', ['structural_core_probe.py']),
    ('cubic_isotropy', 'verification/lean', ['cubic_isotropy_probe.py']),
    ('lean-manuscript census', '.', ['tools/lean_manuscript_census.py']),
    ('mirror', '.', ['papers/oi_lattice_code/mirror_check.py']),
    ('citation', '.', ['papers/oi_lattice_code/citation_check.py']),
    ('dependency-label', '.', ['tools/dependency_label_check.py', '--strict']),
]

# Every A1 string literal the two guards keep after the edits (decision 5, #1169 c.7059136165): line in the
# simulated R7 guard, literal ('*': the whole string constant that starts on that line), target the guard reads,
# polarity (+ must occur, - must not occur), purpose.
MAA = 'verification/programmes/substratum/manuscript-axiom-audit.md'
SIA = 'verification/programmes/substratum/interface-audit.md'
CEN = 'verification/audits/manuscript/lean-manuscript-census.md'
PINS = [
    ('P01', 3346, 'A1–A6 are not `DerivedOI`', 'verification/programmes/substratum/route-b-audit.md', '+',
     'R7-RB1: the Route B record keeps its outcome wording (frozen record)'),
    ('P02', 3410, '**(A1) Finiteness.** The configuration space $S$ is finite.', MAA, '+',
     'R7-MAX: the audit record quotes the six axioms verbatim (frozen record)'),
    ('P03', 3414, '| A1 finiteness | **yes**', MAA, '+', 'R7-MAX: the per-axiom preregistered verdict row (frozen record)'),
    ('P04', 3419, 'Status: pass complete, with a scope repair recorded at review. No manuscript-level A1–A6 conjunct is '
     'presently a faithful predicate of the bare theory', MAA, '+', 'R7-MAX: the record\'s status line (frozen record)'),
    ('P05', 3421, 'A1 and A2 are realized-core images, not faithful predicates of the manuscript substratum', MAA, '+',
     'R7-MAX: the scope repair recorded at review (frozen record)'),
    ('P06', 3425, '| A1 finiteness | realized-core image holds for the witness, and for every theory; manuscript-level A1 '
     'is a gap (no identification map) |', MAA, '+', 'R7-MAX: the outcome row (frozen record)'),
    ('P07', 3453, 'A1 and A2 hold for the witness', 'verification/lean-mathlib/OIBridge/ManuscriptAxioms.lean', '-',
     'R7-MAX: a superseded reading is absent from the module'),
    ('P08', 3453, 'A1 AND A2 HOLD FOR THE WITNESS', 'verification/lean-mathlib/OIBridge/ManuscriptAxioms.lean', '-',
     'R7-MAX: the same superseded reading, capitalized, is absent from the module'),
    ('P09', 3456, 'A1–A6 hold for the witness', MAA, '-', 'R7-MAX: an overclaim is not asserted in the record'),
    ('P10', 3457, 'satisfies A1–A6', MAA, '-', 'R7-MAX: an overclaim is not asserted in the record'),
    ('P11', 3461, 'A1 and A2 hold for the witness', MAA, '-', 'R7-MAX: a superseded reading is not asserted in the record'),
    ('P12', 3468, 'manuscript axioms A1-A6', 'verification/lean-manuscript-census.json', '+',
     'R7-MAX: the registry family name, kept by owner decision (#1169 c.7058783437)'),
    ('P13', 3475, '| manuscript axioms A1–A6 | 1 | kernel-only |', CEN, '+', 'R7-MAX: the rendered census row of that family'),
    ('P14', 3475, 'realized-core images of A1 and A2', CEN, '+', 'R7-MAX: the census record\'s wording (record)'),
    ('P15', 3641, 'def A1 : Prop := Finite 𝒮.Conf', 'verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean', '+',
     'R7-SUB: the kernel definition of the finiteness predicate, verbatim (renamed only by #1482)'),
    ('P16', 3703, 'Status: pass complete. Q1: A1, A2 and A5 are stated on the structure', SIA, '+',
     'R7-SUB: the interface-audit record\'s status line (frozen record)'),
    ('P17', 3711, 'satisfies A1–A6', SIA, '-', 'R7-SUB: an overclaim is not asserted in the record'),
    ('P18', 3711, "satisfies the manuscripts' A1–A6", SIA, '-', 'R7-SUB: an overclaim is not asserted in the record'),
    ('P19', 3736, 'A1–A6 as predicates of it', 'verification/README.md', '-',
     'R7-SUB: a superseded reading is absent from the README'),
    ('P20', 6267, 'A1', 'verification/lean-mathlib/OIBridge/FrozenSourcing.lean', '-',
     'R7-FSS: the module defines no predicate named A1 (the freeze)'),
    ('P21', 6432, 'A1', 'verification/lean-mathlib/OIBridge/StochasticInterface.lean', '-',
     'R7-SOI: the module defines no predicate named A1 (the freeze)'),
    ('P22', 9523, '**a rigorous reversible fluid witness in the A1–A4, ¬A5 class**',
     'verification/lean-mathlib/OIBridge/HexLatticeGas.lean', '+', 'R7-HYB Z17: the module docstring keeps the frozen H-B wording'),
    ('P23', 9536, 'H-B: one candidate executed in the A1–A4, ¬A5 class; OI-compatibility of the class open '
     '(`round-h-b-reversible-fluid-substratum/result.md`).', 'verification/programmes/hydrodynamics/PROGRAMME.md', '+',
     'R7-HYB Z18: section 8 carries exactly the frozen H-B sentence'),
    ('P24', 9590, 'H-B: one candidate executed in the A1–A4, ¬A5 class; OI-compatibility of the class open',
     'verification/programmes/hydrodynamics/PROGRAMME.md', '+',
     'R7-HYB mutation control m25: the strengthened one-line state is built from the frozen sentence'),
    ('P25', 9748, '*', 'verification/ROADMAP.md', '+',
     'R7-A6P: the whole ROADMAP row P1 - A6 (`A1`-`A5`, `A1`, the A1-A6 package), byte-identical (frozen ROADMAP)'),
    ('P26', 10672, '*', 'verification/ROADMAP.md', '+', 'R7-A6D A18: the same ROADMAP row (frozen ROADMAP)'),
    ('P27', 10980, '¬ (linkSubstratum (Fin d → ZMod L) (Fin 6 → ℂ) (nbrs d L) M (fun _ _ h => mem_nbrs_symm d L h)).A1',
     'verification/lean-mathlib/OIBridge/A6Instantiation.lean', '+',
     'R7-A6I I17: the kernel statement of cx3b_complex_not_A1 (renamed only by #1482)'),
    ('P28', 11031, '`A1` is not weakened to make it fit', 'verification/ROADMAP.md', '+',
     'R7-A6I I22: the ROADMAP section of the instantiation round (frozen ROADMAP)'),
    ('P29', 11050, '`A1` is not weakened', 'verification/README.md', '+',
     'R7-A6I I23: the README paragraph of the instantiation round, which names the predicate'),
    ('P30', 11348, 'H-B: one candidate executed in the A1–A4, ¬A5 class; OI-compatibility of the class open '
     '(`round-h-b-reversible-fluid-substratum/result.md`).', 'verification/programmes/hydrodynamics/PROGRAMME.md', '+',
     'R7-HYE W21: section 8 keeps H-B\'s sentence byte-identical beside H-E\'s'),
]
# Lean declaration names inside two check messages: machine-facing technical pins that #1482 must remove or update
# (owner ruling #1169 c.7059632884)
# (guard line, text, target declaring them, names). Their test: each name renamed in its target fails the guard.
DECL_NAMES = [(3485, 'A1Realized, A2Realized, A1A2Realized', 'verification/lean-mathlib/OIBridge/ManuscriptAxioms.lean',
               ['A1Realized', 'A1A2Realized']),
              (11265, 'cx3b_complex_not_A1', 'verification/lean-mathlib/OIBridge/A6Instantiation.lean', ['cx3b_complex_not_A1'])]


A1PAT = re.compile(r'\bA1\b|[Tt]otal[- ]finiteness|[Ff]initeness posit|posit \(ii\)|\bA1\s*[–-]\s*A6\b')
DECL = re.compile(r'\b\w*[a-z_]A1(?![0-9])\w*|\bA1[A-Za-z_]\w*|\ba1_\w+')
MA = 'verification/lean-mathlib/OIBridge/ManuscriptAxioms.lean'
SIAL = 'verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean'
A6I = 'verification/lean-mathlib/OIBridge/A6Instantiation.lean'
# Kernel identifiers containing A1 in code literals of the R7 guard (not messages): checks of kernel declarations that
# #1482's renames must update. They are outside the owner's two-message ruling (#1169 c.7059632884) and are put to the
# owner as a question, not taken as an exception (PREREG §26). (guard line, name, target, polarity, literal tested)
KERNEL_IDS = [
    (3380, 'a1_every_theory', MA, '+', 'a1_every_theory'),
    (3380, 'substratumTheory_A1', MA, '+', 'substratumTheory_A1'),
    (3380, 'substratumTheory_A1A2', MA, '+', 'substratumTheory_A1A2'),
    (3389, 'A1Realized', MA, '+', 'A1Realized'),
    (3389, 'A1A2Realized', MA, '+', 'A1A2Realized'),
    (3392, 'A1Realized', MA, '+', 'def A1Realized'),
    (3467, 'A1Realized', 'papers/Main.md', '-', 'A1Realized'),
    (3476, 'A1Realized', 'verification/README.md', '+', 'A1Realized'),
    (3667, 'a1_of_finite', SIAL, '+', 'a1_of_finite'),
    (3667, 'waveSubstratum_A1', SIAL, '+', 'waveSubstratum_A1'),
    (10978, 'cx3b_complex_not_A1', A6I, '+', 'theorem cx3b_complex_not_A1 (d L : ℕ)'),
    (11216, 'cx3b_complex_not_A1', 'verification/programmes/substratum/a6-instantiation/result.md', '+',
     '| `cx3b_complex_not_A1` | `[propext, Classical.choice, Quot.sound]` |'),
]


def resolve(dest):
    """PINS with every '*' literal replaced by the string constant of the simulated R7 guard that starts on its line."""
    import ast, warnings
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        tree = ast.parse(open(os.path.join(dest, R7), encoding='utf-8').read())
    starts = {}
    for n in ast.walk(tree):
        if isinstance(n, ast.Constant) and isinstance(n.value, str):
            starts.setdefault(n.lineno, n.value)
    return [(p[0], p[1], starts.get(p[1], '') if p[2] == '*' else p[2]) + p[3:] for p in PINS]


def inventory(dest):
    """Every A1 string of the two simulated guards is a listed pin or a listed declaration name; no comment keeps one."""
    import ast, io, tokenize, warnings
    out = []
    for g in (R7, F71):
        src = open(os.path.join(dest, g), encoding='utf-8').read()
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            tree = ast.parse(src)
        for n in ast.walk(tree):
            if not (isinstance(n, ast.Constant) and isinstance(n.value, str) and (A1PAT.search(n.value) or DECL.search(n.value))):
                continue
            pinned = [p for p in resolve(dest) if g == R7 and n.lineno - 2 <= p[1] <= n.end_lineno + 2 and p[2] in n.value]
            rest = n.value
            for p in pinned:
                rest = rest.replace(p[2], ' ')
            if any(g == R7 and n.lineno - 2 <= x[0] <= n.end_lineno + 2 for x in DECL_NAMES):
                rest = DECL.sub(' ', rest)
            for k in KERNEL_IDS:
                if g == R7 and n.lineno - 1 <= k[0] <= n.end_lineno + 1:
                    rest = re.sub(r'\b%s\b' % k[1], ' ', rest)
            if A1PAT.search(rest) or DECL.search(rest):
                out.append('%s:%d: A1 string neither a listed pin nor a listed declaration name: %r' % (g, n.lineno, rest[:90]))
        for t in tokenize.generate_tokens(io.StringIO(src).readline):
            if t.type == tokenize.COMMENT and A1PAT.search(t.string):
                out.append('%s:%d: comment keeps an A1 string: %r' % (g, t.start[0], t.string[:90]))
    return out


def materialize(rev, dest):
    ls = subprocess.run(['git', '-C', ROOT, 'ls-tree', '-r', '-z', rev], capture_output=True, check=True).stdout
    ents = []
    for rec in ls.split(b'\0'):
        if not rec:
            continue
        meta, path = rec.split(b'\t', 1)
        mode, typ, oid = meta.split()
        if typ == b'blob':
            ents.append((mode, oid, path.decode('utf-8')))
    p = subprocess.Popen(['git', '-C', ROOT, 'cat-file', '--batch'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    for mode, oid, path in ents:
        p.stdin.write(oid + b'\n'); p.stdin.flush()
        hdr = p.stdout.readline().split()
        n = int(hdr[2]); data = p.stdout.read(n); p.stdout.read(1)
        fp = os.path.join(dest, path)
        os.makedirs(os.path.dirname(fp), exist_ok=True)
        if mode == b'120000':
            os.symlink(data.decode('utf-8'), fp)
        else:
            with open(fp, 'wb') as f:
                f.write(data)
    p.stdin.close(); p.wait()
    return len(ents)


def apply(data, dest, rev, omit=()):
    sub = {'edits': [e for e in data['edits'] if e['id'] not in omit]}
    out = ec.apply_edits(sub, lambda pth: ec.git_show(rev, pth))
    for f, t in out.items():
        with open(os.path.join(dest, f), 'w', encoding='utf-8') as fh:
            fh.write(t)
    return out


def run(dest, cwd, argv, timeout=900):
    r = subprocess.run([sys.executable, '-B'] + argv, cwd=os.path.join(dest, cwd), capture_output=True, text=True, timeout=timeout)
    fails = sorted(set(re.findall(r'^\s*FAIL\s+([A-Za-z0-9_.-]+)', r.stdout, re.M)))
    if r.returncode and not fails:
        at = re.findall(r'File "[^"]*%s", line (\d+)' % re.escape(argv[0]), r.stderr)
        if at:
            fails = ['abort@%s' % at[-1]]
    return r.returncode, fails, (r.stdout + r.stderr).strip().split('\n')[-1][:160]


def flex(lit):
    return re.compile(r'\s+'.join(re.escape(w) for w in lit.split()))


def mutate(dest, target, lit, pol):
    fp = os.path.join(dest, target)
    t = open(fp, encoding='utf-8').read()
    if pol == '+':
        m, n = flex(lit).subn(lambda x: x.group(0).replace('A1', 'A·1').replace('a1', 'a·1'), t)
        if n == 0:
            return None, 0
        return t, m
    if target.endswith('.lean'):
        extra = ('\ndef A1 : Prop := True\n' if lit == 'A1' else '\n-- ' + lit + '\n')
    else:
        extra = '\n\n' + lit + '.\n'
    return t, t + extra


def predict(data, rev, dest):
    """The predicted execution tree, less its result note, as a git worktree of the ledger base: the edits applied, the
    TeX of the edited sources rebuilt by build.sh's recipe, the seven stale coverage fingerprints re-affirmed from the
    census, the plan's record directory copied in, and the SC-42 result regenerated. PDFs are left to the CI build."""
    import hashlib, json as _json
    subprocess.run(['git', '-C', ROOT, 'worktree', 'add', '--detach', dest, rev], check=True, capture_output=True)
    after = apply(data, dest, rev)
    srcs = [f for f in after if re.match(r'^papers/[^/]+\.md$', f)] + [f for f in after if f == ec.FULL]
    for md in srcs:
        book = md == ec.FULL
        cmd = ['pandoc', md, '-s'] + (['--toc', '--metadata=toc:false'] if book else []) + \
              ['--pdf-engine=xelatex', '--include-in-header=tools/unicode-fix.tex', '-o', md[:-3] + '.tex']
        subprocess.run(cmd, cwd=dest, check=True, capture_output=True)
        with open(os.path.join(dest, md), 'rb') as f:
            stamp = '%% source-sha256: %s\n' % hashlib.sha256(f.read()).hexdigest()
        with open(os.path.join(dest, md[:-3] + '.tex'), 'a', encoding='utf-8') as f:
            f.write(stamp)
    cen = {c['id']: c['fingerprint'] for c in _json.loads(subprocess.run([sys.executable, '-I', '-B', 'tools/proof_census.py', '--json'],
                                                                          cwd=dest, capture_output=True, text=True, check=True).stdout)}
    cov = os.path.join(dest, 'verification/coverage/LEDGER.json')
    t = open(cov, encoding='utf-8').read()
    stale = ['MAIN:L-3', 'STRUCTURE:P-9.5', 'SUBSTRATUM:C-effective-finiteness-gauge-class-transfer', 'SUBSTRATUM:T-23',
             # amendment §31, nit 5 (D389-D391)
             'SM:L-1c-canonical-projection-resummed-kernel', 'SM:P-4b-symmetric-point-custodial-scalarity-component', 'SM:T-19']
    for i in stale:
        m = re.search(r'"id": "%s",.*?"fingerprint": "([0-9a-f]*)"' % re.escape(i), t, re.S)
        t = t[:m.start(1)] + cen[i] + t[m.end(1):]
    open(cov, 'w', encoding='utf-8').write(t)
    rec = os.path.relpath(HERE, ROOT)
    os.makedirs(os.path.join(dest, rec), exist_ok=True)
    for n in sorted(os.listdir(HERE)):
        if os.path.isfile(os.path.join(HERE, n)) and not n.startswith('.'):
            shutil.copy2(os.path.join(HERE, n), os.path.join(dest, rec, n))
    r = 'verification/audits/manuscript/bell-operational-reconciliation-20261029/'
    out = subprocess.run([sys.executable, '-I', '-B', r + 'check_sc42_integration.py', '--verbose'], cwd=dest, capture_output=True, check=True).stdout
    open(os.path.join(dest, r + 'sc42-integration-result.json'), 'wb').write(out)
    # verify.yml's SC-42 step, on the predicted tree
    runs = [subprocess.run([sys.executable, '-I'] + o + ['-B', r + 'check_sc42_integration.py'] + a, cwd=dest, capture_output=True)
            for a, o in ((['--verbose'], []), ([], ['-O']), (['--self-test'], []), (['--self-test'], ['-O']))]
    ctrl = open(os.path.join(dest, r + 'sc42-integration-controls.json'), 'rb').read()
    step = (all(x.returncode == 0 for x in runs) and runs[0].stdout == out == runs[1].stdout and runs[2].stdout == ctrl and runs[3].stdout == ctrl)
    print('predicted tree at %s: %d files edited, %d TeX rebuilt, %d fingerprints re-affirmed, record directory copied, '
          'SC-42 result regenerated; verify.yml SC-42 comparisons on it: %s' % (dest, len(after), len(srcs), len(stale),
                                                                                  'PASS' if step else 'FAIL'))
    return step


RESULTS = []


def record(name, ok, discrepancies=()):
    RESULTS.append({'name': name, 'status': 'pass' if ok else 'fail', 'discrepancies': list(discrepancies)})


def write_result(explicit, mode, meta):
    """The structured result (§A.44), to --result-json and, when RUNNER_TEMP/out exists, there as well."""
    import json as _json
    doc = dict(meta, schema='a1exit-checker-result-v1', checker='guards_check.py', mode=mode, checks=RESULTS,
               verdict='pass' if RESULTS and all(c['status'] == 'pass' for c in RESULTS) else 'fail')
    paths = [explicit] if explicit else []
    rt = os.environ.get('RUNNER_TEMP')
    if rt and os.path.isdir(os.path.join(rt, 'out')):
        paths.append(os.path.join(rt, 'out', 'guards_check-%s.json' % mode))
    for pth in paths:
        with open(pth, 'w', encoding='utf-8') as f:
            _json.dump(doc, f, indent=1, sort_keys=True, ensure_ascii=False)
            f.write('\n')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--rev')
    ap.add_argument('--mutants', action='store_true')
    ap.add_argument('--keep')
    ap.add_argument('--result-json', metavar='PATH', help='write the structured result here')
    ap.add_argument('--predict', help='write the predicted execution tree as a git worktree at this new path, and exit')
    a = ap.parse_args()
    data = ec.load()
    rev = a.rev or data['drafting_base']
    if a.predict:
        good = predict(data, rev, a.predict)
        record('predicted tree built; verify.yml SC-42 comparisons on it', good, [] if good else ['SC-42 comparisons failed'])
        write_result(a.result_json, 'predict', {'base': rev, 'tree': a.predict})
        sys.exit(0 if good else 1)
    dest = a.keep or tempfile.mkdtemp(prefix='a1exit-sim-')
    ok = True
    try:
        n = materialize(rev, dest)
        after = apply(data, dest, rev)
        print('simulated tree: %d tracked files of %s, %d edited by %d edits' % (n, rev[:12], len(after), len(data['edits'])))
        for name, cwd, argv in CHECKS:
            rc, fails, last = run(dest, cwd, argv)
            good = rc == 0 and not fails
            ok &= good
            record('%s on the simulated tree' % name, good, [] if good else ['exit %d %s' % (rc, ','.join(fails))])
            print('  %s %-24s exit %d%s  %s' % ('PASS' if good else 'FAIL', name, rc, (' FAIL ' + ','.join(fails)) if fails else '', last))
        print('countercontrols (each must fail):')
        ccs = [('CC-1 pin edit D302 omitted', ['D302'], None, R7),
               ('CC-2 D302 literal removed from its target', [], ('verification/README.md', 'whose substratum conditions are not `DerivedOI`'), R7),
               ('CC-3 glossary edit D220 omitted, pin D306 applied', ['D220', 'D221'], None, R7),
               ('CC-4 pin edit D301 omitted', ['D301'], None, F71)]
        for name, omit, strip, guard in ccs:
            apply(data, dest, rev, omit=omit)
            saved = None
            if strip:
                fp = os.path.join(dest, strip[0]); saved = open(fp, encoding='utf-8').read()
                new, k = flex(strip[1]).subn('', saved)
                assert k > 0, 'countercontrol literal not found'
                open(fp, 'w', encoding='utf-8').write(new)
            rc, fails, last = run(dest, 'verification/lean', [os.path.basename(guard)])
            caught = rc != 0
            ok &= caught
            record(name + ' must fail', caught, [] if caught else ['the countercontrol passed'])
            print('  %s %s: exit %d, failing checks %s' % ('ok ' if caught else 'BAD', name, rc, ','.join(fails) or '-'))
            if saved is not None:
                open(fp, 'w', encoding='utf-8').write(saved)
        apply(data, dest, rev)
        inv = inventory(dest)
        ok &= not inv
        record('guard A1-string inventory', not inv, inv)
        print('guard A1-string inventory: %d listed pins, %d messages naming declarations (pins pending #1482); %d unlisted strings or comments'
              % (len(PINS), len(DECL_NAMES), len(inv)))
        for x in inv:
            print('  BAD ' + x)
        if a.mutants:
            import ast, warnings
            with warnings.catch_warnings():
                warnings.simplefilter('ignore')
                gt = ast.parse(open(os.path.join(dest, R7), encoding='utf-8').read())
            consts = [(n.lineno, n.end_lineno, n.value) for n in ast.walk(gt) if isinstance(n, ast.Constant) and isinstance(n.value, str)]
            print('pin inventory: %d retained A1 string literals of the guards, each mutated in its target' % len(PINS))
            for pid, line, lit, target, pol, why in resolve(dest):
                if not any(a - 2 <= line <= b + 2 and lit in v for a, b, v in consts):
                    print('  BAD %s: literal not found near line %d of the simulated guard' % (pid, line)); ok = False; continue
                tgt = os.path.join(dest, target)
                before = open(tgt, encoding='utf-8').read()
                flat = ' '.join(before.split())
                present = (lit in flat) if pol == '+' else (not re.search(r'(?m)^(?:noncomputable )?def A1\b', before) if lit == 'A1' else True)
                orig, new = mutate(dest, target, lit, pol)
                if orig is None:
                    print('  BAD %s: positive pin absent from its simulated target %s' % (pid, target)); ok = False; continue
                open(tgt, 'w', encoding='utf-8').write(new)
                rc, fails, _ = run(dest, 'verification/lean', ['edge_rigidity_probe.py'])
                open(tgt, 'w', encoding='utf-8').write(orig)
                named = any(not f.startswith('abort@') or abs(int(f[6:]) - line) <= 5 for f in fails)
                good = present and rc != 0 and named
                ok &= good
                record('pin %s %s against %s' % (pid, pol, target), good, [] if good else ['mutation not detected or not named: %s' % (','.join(fails) or '-')])
                print('  %s %s %s %s -> %s: mutation fails %s' % ('ok ' if good else 'BAD', pid, pol, lit[:48], target,
                                                                  ','.join(fails) or 'nothing named (exit %d)' % rc))
            print('kernel identifiers in code literals (owner question, #1482 updates them), each tested against its target:')
            for line, nm, target, pol, lit in KERNEL_IDS:
                tgt = os.path.join(dest, target)
                orig, new = mutate(dest, target, lit, pol)
                if orig is None:
                    print('  BAD line %d %s: literal absent from %s' % (line, nm, target)); ok = False; continue
                open(tgt, 'w', encoding='utf-8').write(new)
                rc, fails, _ = run(dest, 'verification/lean', ['edge_rigidity_probe.py'])
                open(tgt, 'w', encoding='utf-8').write(orig)
                good = rc != 0 and bool(fails)
                ok &= good
                record('kernel identifier %s (line %d, %s) against %s' % (nm, line, pol, target), good, [] if good else ['not detected'])
                print('  %s line %d %s %s -> %s: mutation fails %s' % ('ok ' if good else 'BAD', line, pol, nm, target, ','.join(fails) or '-'))
            print('declaration names in check messages (technical pins pending #1482), each renamed in its target:')
            for line, text, target, names in DECL_NAMES:
                tgt = os.path.join(dest, target)
                before = open(tgt, encoding='utf-8').read()
                for nm in names:
                    present = re.search(r'\b%s\b' % nm, before) is not None
                    open(tgt, 'w', encoding='utf-8').write(re.sub(r'\b%s\b' % nm, nm.replace('A1', 'A·1'), before))
                    rc, fails, _ = run(dest, 'verification/lean', ['edge_rigidity_probe.py'])
                    open(tgt, 'w', encoding='utf-8').write(before)
                    good = present and rc != 0
                    ok &= good
                    record('message name %s renamed in %s fails the guard' % (nm, target), good, [] if good else ['not detected'])
                    print('  %s line %d %s -> %s: renaming fails %s' % ('ok ' if good else 'BAD', line, nm, target, ','.join(fails) or 'the guard (exit %d)' % rc))
    finally:
        if not a.keep:
            shutil.rmtree(dest, ignore_errors=True)
    if not ok and all(c['status'] == 'pass' for c in RESULTS):
        record('overall', False, ['a check failed without a recorded entry'])
    write_result(a.result_json, 'mutants' if a.mutants else 'checks', {'base': rev})
    print('RESULT ' + ('PASS' if ok else 'FAIL'))
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
