#!/usr/bin/env python3
"""Round BG-3 -- the round's own static controls (stage 1).

It reads the repository only through git, at the commits it is given and at D, and never the working
tree's modules, so a later round that edits them does not make it fail. It certifies nothing on its
own: the Lean kernel and the release gate establish the mathematics, and the V3 verifier the protocol.
What it checks is that the execution is exactly the frozen edit ledger applied to D, that no statement
of a landed declaration changes, that the reduction is the design-compiled lemma stated once, that no
excluded phrase survives, and that nothing outside the governed paths changes.

    python3 -I controls.py --self-test                 mutation controls on the ledger's output and on
                                                       synthetic inputs; constants against the
                                                       preregistration and the ledger beside this file
    python3 -I controls.py check <E> --freeze <F>      C1, C2, L, P, R, S and G against the tree at E
    python3 -I controls.py verdict <E> --freeze <F> --log LOG
                                                       the four cell tokens: Q-RED, Q-PRES and Q-DOC
                                                       from the static controls, Q-KER from the saved
                                                       tail of E's Mathlib bridge log

Exit 1 on any failure; `verdict` also exits 1 unless all four tokens are positive.
"""
import hashlib
import json
import os
import re
import subprocess
import sys

D = 'e3ad5d7a71910ce5413ef6dacd25bf5a63d5a1e0'
RDIR = 'verification/programmes/oi-qm/reconstruction/round-bg-3-scope-transfer-correction/'
PREREG = RDIR + 'preregistration.md'
LEDGER = RDIR + 'edit-ledger.json'
RESULT = RDIR + 'result.md'
LEDGER_SHA256 = '7ad8dbef706b6deafd868100f43fa846f67a0236c8b57013180a6b2641527352'
TST = 'verification/lean-mathlib/OIBridge/TurnpikeScopeTransfer.lean'
CR = 'verification/lean-mathlib/OIBridge/CongruentReconstruction.lean'
RM = 'verification/ROADMAP.md'
DESIGN = 'verification/programmes/oi-qm/reconstruction/bekir-golomb-orientation-design/SignedRepairDesign.lean'
LEMMA = 'real_to_integer_surrogate'
TRANSFER = 'integer_realization_of_real_realization'
REFUTE = 'OIBridge.PremiseOrientation.not_BGIntegerClassification'
NS = 'OIBridge.ScopeTransfer'
GATE_COUNT = 5989
ALLOWED_AXIOMS = {'propext', 'Classical.choice', 'Quot.sound'}
UNTOUCHED = ['verification/programmes/oi-qm/reconstruction/round-bg-2-premise-orientation/',
             'verification/programmes/oi-qm/reconstruction/bekir-golomb-orientation-design/',
             'verification/infrastructure/legacy-records.json', 'verification/lean-manuscript-census.json',
             'verification/lean/', '.github/', 'papers/', 'book/', 'verification/coverage/']
EXCLUDED = ['only unproved', 'Bekir–Golomb 2007, in the spectral form', 'the 2007 classification for INTEGER',
            'THE EXTERNAL INTEGER PREMISE', 'THE REAL SPECTRAL CLASSIFICATION, derived',
            'CONDITIONAL ON THE INTEGER CLASSIFICATION ALONE', 'INTEGER Bekir–Golomb classification',
            'will eventually supply', 'can actually feed', 'turnpike classification supplies',
            'Bekir–Golomb is refuted', 'the classification is false', 'the two-branch theorem is false',
            'the premise is discharged', 'H-BG is proved']
EARNED = ('EARNED READING: TurnpikeScopeTransfer.lean states the real-to-integer reduction once, as '
          'real_to_integer_surrogate, and spectral_classification_of_BG factors through it. Its docstrings '
          'describe BGIntegerClassification as an unsigned integer premise refuted by '
          'OIBridge.PremiseOrientation.not_BGIntegerClassification, and its two consumers as implications '
          'from it. CongruentReconstruction.lean\'s docstrings describe hclass as a hypothesis about the '
          'given pair whose derivation from the published classification is not established, and which '
          'omits the reversed exceptional branch. No statement of either module changes.')

FAIL = []


def report(name, ok, detail=''):
    print(('PASS ' if ok else 'FAIL ') + name + (('  ' + detail) if detail else ''))
    if not ok:
        FAIL.append(name)
    return bool(ok)


def git(*args):
    return subprocess.run(['git'] + list(args), capture_output=True, text=True, check=True).stdout


def show(commit, path):
    r = subprocess.run(['git', 'show', '%s:%s' % (commit, path)], capture_output=True)
    return r.stdout.decode('utf-8') if r.returncode == 0 else None


def blob(commit, path):
    r = subprocess.run(['git', 'rev-parse', '%s:%s' % (commit, path)], capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else None


def sha(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()


def flat(s):
    return ' '.join(s.split())


# ---------------------------------------------------------------- Lean text, comments blanked

def code_only(text):
    """The text with every comment (nested /- -/, docstrings, module docs, --) replaced by spaces,
    newlines kept, so line numbers and column 0 survive. String literals are skipped as code."""
    out, i, depth, n = [], 0, 0, len(text)
    while i < n:
        two = text[i:i + 2]
        if depth == 0 and two == '--':
            j = text.find('\n', i)
            j = n if j < 0 else j
            out.append(' ' * (j - i))
            i = j
        elif two == '/-':
            depth += 1
            out.append('  ')
            i += 2
        elif depth > 0 and two == '-/':
            depth -= 1
            out.append('  ')
            i += 2
        elif depth > 0:
            out.append('\n' if text[i] == '\n' else ' ')
            i += 1
        elif text[i] == '"':
            j = i + 1
            while j < n and text[j] != '"':
                j += 2 if text[j] == '\\' else 1
            out.append(text[i:j + 1])
            i = j + 1
        else:
            out.append(text[i])
            i += 1
    return ''.join(out)


DECL = re.compile(r"^(?:(?:private|protected|noncomputable)\s+)*"
                  r"(theorem|lemma|def|abbrev|structure|instance|inductive|class)\s+([A-Za-z_][\w.']*)", re.M)


def decls(text):
    """{name: (kind, statement, first line, last line)} from code only. A theorem's statement stops at
    its first ':='; any other declaration runs to the next column-0 code line."""
    code = code_only(text)
    lines = code.split('\n')
    out = {}
    for m in DECL.finditer(code):
        kind, name = m.group(1), m.group(2)
        start = code.count('\n', 0, m.start())
        end = start + 1
        while end < len(lines) and not (lines[end][:1].strip() and not lines[end].startswith(' ')):
            end += 1
        while end - 1 > start and not lines[end - 1].strip():
            end -= 1
        body = '\n'.join(lines[start:end])
        stmt = body.split(':=', 1)[0] if kind in ('theorem', 'lemma') else body
        out[name] = (kind, stmt.rstrip(), start + 1, end)
    return out


def prints(text):
    return sorted(ln.strip() for ln in code_only(text).split('\n') if ln.startswith('#print axioms'))


def raw_block(text, name):
    """The raw lines of a declaration, from its keyword line to its last line, as in `decls`."""
    d = decls(text).get(name)
    if not d:
        return None
    return '\n'.join(text.split('\n')[d[2] - 1:d[3]])


def docstring_before(text, name):
    """The `/-- ... -/` that ends immediately above the declaration (an `open ... in` line allowed)."""
    d = decls(text).get(name)
    if not d:
        return ''
    lines = text.split('\n')
    k = d[2] - 2
    if k >= 0 and lines[k].startswith('open ') and lines[k].rstrip().endswith(' in'):
        k -= 1
    if k < 0 or not lines[k].rstrip().endswith('-/'):
        return ''
    j = k
    while j >= 0 and not lines[j].startswith('/--'):
        j -= 1
    return '\n'.join(lines[j:k + 1]) if j >= 0 else ''


def header(text):
    m = re.match(r'/-(.*?)-/', text, re.S)
    return m.group(1) if m else ''


# ---------------------------------------------------------------- the ledger

def apply_splices(base, splices):
    """Rebuild a file from the base text and its splices; None if an old-text hash does not hold."""
    L = base.split('\n')
    out, cur = [], 1
    for s in splices:
        a, b = s['span']
        if a < cur or b < a - 1:
            return None
        if sha('\n'.join(L[a - 1:b])) != s['old_sha256'] or sha(s['new']) != s['new_sha256']:
            return None
        out += L[cur - 1:a - 1] + s['new'].split('\n')
        cur = b + 1
    return '\n'.join(out + L[cur - 1:])


def ledger_outputs(ledger, base_of):
    """{path: rebuilt text or None}, checking each base and result hash."""
    res = {}
    for f in ledger['files']:
        base = base_of(f['path'])
        if base is None or sha(base) != f['base_sha256']:
            res[f['path']] = None
            continue
        out = apply_splices(base, f['splices'])
        res[f['path']] = out if out is not None and sha(out) == f['result_sha256'] else None
    return res


# ---------------------------------------------------------------- the controls, on texts

def ctl_P(d_tst, e_tst, d_cr, e_cr):
    """No statement changes; the only new declaration is the lemma; prints D's plus the lemma's."""
    ok = True
    for d, e, new in ((d_tst, e_tst, {LEMMA}), (d_cr, e_cr, set())):
        dd, ed = decls(d), decls(e)
        ok &= set(ed) == set(dd) | new
        ok &= all(ed.get(k, (None, None))[:2] == v[:2] for k, v in dd.items())
        ok &= prints(e) == sorted(prints(d) + ['#print axioms ' + n for n in new])
        ok &= not re.search(r'\b(sorry|admit|native_decide)\b|^axiom\s', code_only(e), re.M)
    return bool(ok)


def ctl_R(e_tst, design):
    """The lemma is byte-identical to the design file's; the consumer applies it; the transfer is
    applied exactly once in code, inside the lemma."""
    lem = raw_block(e_tst, LEMMA)
    ok = lem is not None and lem == raw_block(design, LEMMA)
    ds = decls(e_tst)
    spec = ds.get('spectral_classification_of_BG')
    code = code_only(e_tst).split('\n')
    if spec:
        proof = '\n'.join(code[spec[2] - 1:spec[3]]).split(':=', 1)[-1]
        ok &= re.search(r'\b%s\b' % LEMMA, proof) is not None and TRANSFER not in proof
    else:
        ok = False
    uses = [i + 1 for i, ln in enumerate(code) if re.search(r'\b%s\b' % TRANSFER, ln)
            and not ln.startswith(('theorem ', '#print'))]
    lm = ds.get(LEMMA)
    ok &= len(uses) == 1 and lm is not None and lm[2] <= uses[0] <= lm[3]
    return bool(ok)


def ctl_S(e_tst, e_cr, note):
    """No excluded phrase (whitespace collapsed, case ignored); the refutation is named where the
    preregistration requires it."""
    hits = [(where, p) for where, t in (('TurnpikeScopeTransfer', e_tst), ('CongruentReconstruction', e_cr),
                                        ('result note', note)) if t
            for p in EXCLUDED if p.lower() in flat(t).lower()]
    need = [header(e_tst), docstring_before(e_tst, 'BGIntegerClassification'),
            docstring_before(e_tst, 'spectral_classification_of_BG'),
            docstring_before(e_tst, 'twoBranch_of_BGClassification')]
    named = all(REFUTE in flat(x) for x in need) and 'revMuForm_r1_r2refl' in header(e_cr)
    return not hits and named, hits


def ctl_G(diff_lines, governed_paths):
    bad = []
    for ln in diff_lines:
        if not ln.strip():
            continue
        status, path = ln.split('\t', 1)
        inside = any(path == p or (p.endswith('/') and path.startswith(p)) for p in governed_paths)
        if not inside or any(path == u or (u.endswith('/') and path.startswith(u)) for u in UNTOUCHED):
            bad.append(ln)
    return bad


def modified_exactly(diff_lines):
    """The three execution files are modified, and no other file is."""
    return sorted(ln.split('\t', 1)[1] for ln in diff_lines if ln.startswith('M\t')) == sorted([TST, CR, RM])


def ctl_K(log):
    """Q-KER over the saved log tail: the build completed, the gate passed with the expected count,
    and every print of TurnpikeScopeTransfer reported within the permitted axioms."""
    rep = {}
    for m in re.finditer(r"'%s\.([\w']+)' depends on axioms: \[([^\]]*)\]" % re.escape(NS), log):
        rep[m.group(1)] = {a.strip() for a in m.group(2).split(',') if a.strip()}
    for m in re.finditer(r"'%s\.([\w']+)' does not depend on any axioms" % re.escape(NS), log):
        rep[m.group(1)] = set()
    want = {'rational_point', 'rational_solutions', 'exists_int_scaling', TRANSFER, LEMMA,
            'spectral_classification_of_BG', 'gaps_eq_of_equal_probabilities', 'twoBranch_of_BGClassification'}
    gate = re.search(r'PASS\s+lean-axioms\s+lean_axiom_check: OK \((\d+) named result', log)
    ok = (set(rep) >= want and all(rep[n] <= ALLOWED_AXIOMS for n in want)
          and 'Build completed successfully' in log and 'release gate: PASS' in log
          and gate is not None and int(gate.group(1)) == GATE_COUNT
          and 'sorryAx' not in log and 'Lean.ofReduceBool' not in log)
    return bool(ok), sorted(rep)


# ---------------------------------------------------------------- commit-level checks

def governed(prereg):
    m = re.search(r'```v3-governed-paths\n(.*?)```', prereg, re.S)
    return [ln.split()[-1] for ln in m.group(1).strip().splitlines()] if m else []


def frozen_blobs(prereg):
    m = re.search(r'```bg3-frozen-blobs\n(.*?)```', prereg, re.S)
    return [tuple(ln.split()) for ln in m.group(1).strip().splitlines()] if m else []


def check(E, F):
    prereg_F = show(F, PREREG)
    report('C1 the preregistration at E is the one at F', prereg_F is not None and prereg_F == show(E, PREREG))
    fb = frozen_blobs(prereg_F or '')
    miss = [(p, b) for p, b in fb if blob(E, p) != b]
    report('C2 the frozen blobs at E', len(fb) == 5 and not miss, str(miss) if miss else '%d blobs' % len(fb))
    led_text = show(E, LEDGER)
    report('L0 the ledger at E is the frozen one', led_text is not None and sha(led_text) == LEDGER_SHA256)
    ledger = json.loads(led_text or '{"files": []}')
    outs = ledger_outputs(ledger, lambda p: show(D, p))
    report('L every governed file at E is the ledger applied to D, byte for byte',
           len(outs) == 3 and all(outs[p] is not None and outs[p] == show(E, p) for p in outs))
    d_tst, e_tst, d_cr, e_cr = show(D, TST), show(E, TST) or '', show(D, CR), show(E, CR) or ''
    report('P no statement changes; one new declaration; prints D\'s plus the lemma\'s',
           ctl_P(d_tst, e_tst, d_cr, e_cr))
    report('R the reduction is the design file\'s lemma, stated once and applied by the consumer',
           ctl_R(e_tst, show(D, DESIGN) or ''))
    ok, hits = ctl_S(e_tst, e_cr, show(E, RESULT))
    report('S no excluded phrase; the refutation named where required', ok, str(hits) if hits else '')
    diff = git('diff', '--no-renames', '--name-status', D, E).splitlines()
    bad = ctl_G(diff, governed(prereg_F or ''))
    report('G every change from D to E inside the governed paths; nothing untouched changes; exactly the '
           'three execution files modified', not bad and modified_exactly(diff),
           str(bad) if bad else '%d paths' % len([x for x in diff if x.strip()]))
    return not FAIL


def verdict(E, F, logfile):
    static = check(E, F)
    named = {n for n in FAIL}
    red = not ({'R', 'L0'} & {n.split()[0] for n in named})
    pres = not ({'L', 'L0', 'P'} & {n.split()[0] for n in named})
    doc = not ({'S'} & {n.split()[0] for n in named})
    ker, rep = ctl_K(open(logfile, encoding='utf-8').read()) if logfile else (False, [])
    print('reports read: %s' % (rep or 'none'))
    print('TOKEN Q-RED  %s' % ('BG-3-REDUCTION-FACTORED' if red else 'BG-3-REDUCTION-NOT-FACTORED'))
    print('TOKEN Q-PRES %s' % ('BG-3-STATEMENTS-PRESERVED' if pres else 'BG-3-STATEMENTS-CHANGED'))
    print('TOKEN Q-DOC  %s' % ('BG-3-DOCSTRINGS-CORRECTED' if doc else 'BG-3-DOCSTRINGS-NOT-CORRECTED'))
    print('TOKEN Q-KER  %s' % ('BG-3-KERNEL-CLEAN' if ker else 'BG-3-KERNEL-NOT-ESTABLISHED'))
    allpos = red and pres and doc and ker and static
    if allpos:
        print(EARNED)
    return allpos


# ---------------------------------------------------------------- self-test

def synthetic_log(reports, count=GATE_COUNT, gate='PASS', extra=''):
    lines = ["info: OIBridge/TurnpikeScopeTransfer.lean:%d:0: '%s.%s' depends on axioms: [%s]"
             % (880 + i, NS, n, ', '.join(ax)) for i, (n, ax) in enumerate(reports)]
    lines += [extra, 'Build completed successfully (3652 jobs).',
              '  PASS  lean-axioms      lean_axiom_check: OK (%d named result(s) reported, no sorr' % count,
              'release gate: %s  (note)' % gate]
    return '\n'.join(lines)


def self_test():
    here = os.path.dirname(os.path.abspath(__file__))
    prereg = open(os.path.join(here, 'preregistration.md'), encoding='utf-8').read()
    led_text = open(os.path.join(here, 'edit-ledger.json'), encoding='utf-8').read()
    ledger = json.loads(led_text)
    report('self: D agrees with the preregistration and the ledger',
           ('D: ' + D) in prereg and ledger.get('base') == D)
    report('self: the ledger beside this file is the frozen one', sha(led_text) == LEDGER_SHA256)
    gp = governed(prereg)
    report('self: governed paths parsed (5): the two modules, the ROADMAP, the record directory, the receipt',
           len(gp) == 5 and TST in gp and CR in gp and RM in gp and RDIR in gp)
    base = {p: show(D, p) for p in (TST, CR, RM, DESIGN)}
    outs = ledger_outputs(ledger, lambda p: base.get(p))
    report('self: the ledger applies to D\'s three files with every hash holding',
           len(outs) == 3 and all(v is not None for v in outs.values()))
    t, c = outs.get(TST) or '', outs.get(CR) or ''
    report('self: P accepts the ledger output', ctl_P(base[TST], t, base[CR], c))
    report('self: R accepts the ledger output', ctl_R(t, base[DESIGN]))
    report('self: S accepts the ledger output', ctl_S(t, c, '')[0])
    report('self: S is not vacuous: the first ten excluded phrases occur at D, the other five do not',
           [p.lower() in flat(base[TST] + ' ' + base[CR]).lower() for p in EXCLUDED] == [True] * 10 + [False] * 5)
    report('self: the parser skips a docstring line beginning "theorem" (CongruentReconstruction.lean:750 at D)',
           base[CR].split('\n')[749].startswith('theorem in the form') and 'in' not in decls(base[CR])
           and decls('/-- x\ntheorem fake : True -/\ntheorem real : True := trivial\n').keys() == {'real'})
    spec_d = raw_block(base[TST], 'spectral_classification_of_BG')
    spec_t = raw_block(t, 'spectral_classification_of_BG')
    muts = [
        ('P', 'a changed statement (3 ≤ m to 2 ≤ m in the two-branch theorem)',
         lambda: (t.replace('theorem twoBranch_of_BGClassification (hBG : BGIntegerClassification) {m : ℕ} (hm : 3 ≤ m)',
                            'theorem twoBranch_of_BGClassification (hBG : BGIntegerClassification) {m : ℕ} (hm : 2 ≤ m)', 1), c)),
        ('P', 'a changed definition body (the reflection clause of the premise)',
         lambda: (t.replace("    (¬ ∃ c : ℤ, ∀ i, F' i = c - F i.rev) →\n    ∃ eS eT",
                            "    (¬ ∃ c : ℤ, ∀ i, F' i = c + F i.rev) →\n    ∃ eS eT", 1), c)),
        ('P', 'the lemma\'s print dropped', lambda: (t.replace('#print axioms %s\n' % LEMMA, '', 1), c)),
        ('P', 'an extra print', lambda: (t.replace('#print axioms %s\n' % LEMMA,
                                                    '#print axioms %s\n#print axioms row\n' % LEMMA, 1), c)),
        ('P', 'an extra declaration', lambda: (t.replace('end ScopeTransfer', 'theorem extra : True := trivial\n\nend ScopeTransfer', 1), c)),
        ('P', 'a changed statement in CongruentReconstruction',
         lambda: (t, c.replace('theorem twoBranch_of_spectral_classification (hm : 3 ≤ m)',
                               'theorem twoBranch_of_spectral_classification (hm : 4 ≤ m)', 1))),
        ('R', 'the inline reduction restored in the consumer', lambda: (t.replace(spec_t, spec_d, 1), c)),
        ('R', 'a changed lemma statement', lambda: (t.replace(
            '        (∀ a b c d : Fin n, a ≠ b → F\' d - F\' c = F b - F a →',
            '        (∀ a b c d : Fin n, a < b → F\' d - F\' c = F b - F a →', 1), c)),
        ('S', 'an excluded phrase reinserted', lambda: (t.replace('WHY THIS FILE EXISTS.', 'WHY THIS FILE EXISTS. '
                                                                  'The premise is the ONLY unproved input.', 1), c)),
        ('S', 'an excluded phrase across a line break', lambda: (t, c.replace(
            'internal is kernel-proved.', 'internal is kernel-proved; the turnpike\n  classification supplies it.', 1))),
        ('S', 'the refutation dropped from the definition\'s docstring', lambda: (t.replace(
            'The proposition is false:\n`OIBridge.PremiseOrientation.not_BGIntegerClassification` refutes',
            'The proposition is false:\nBG-2 refutes', 1), c)),
    ]
    checks = {'P': lambda a, b: ctl_P(base[TST], a, base[CR], b), 'R': lambda a, b: ctl_R(a, base[DESIGN]),
              'S': lambda a, b: ctl_S(a, b, '')[0]}
    for which, name, f in muts:
        a, b = f()
        report('self: %s rejects the mutation: %s' % (which, name), (a, b) != (t, c) and not checks[which](a, b))
    edited = t.replace('  THE TRANSFER. All realization', '  THE TRANSFER.  All realization', 1)
    bad_led = json.loads(led_text)
    bad_led['files'][0]['splices'][0]['old_sha256'] = '0' * 64
    report('self: L rejects a byte outside the spans, which P, R and S accept',
           edited != t and edited != outs[TST] and ctl_P(base[TST], edited, base[CR], c)
           and ctl_R(edited, base[DESIGN]) and ctl_S(edited, c, '')[0])
    report('self: the ledger rejects a span whose old-text hash does not hold',
           ledger_outputs(bad_led, lambda p: base.get(p))[TST] is None)
    bad = ctl_G(['M\tpapers/GR.md', 'M\t' + DESIGN, 'A\tverification/lean/x.py', 'M\t' + TST, 'M\t' + CR, 'M\t' + RM,
                 'A\t' + RDIR + 'controls.py', 'M\tverification/lean-manuscript-census.json'], gp)
    report('self: G flags a manuscript, the design package, a probe and the census, and passes the governed files',
           len(bad) == 4 and not any(p in ' '.join(bad) for p in (TST, RDIR)))
    report('self: G requires exactly the three execution files modified',
           modified_exactly(['M\t' + TST, 'M\t' + CR, 'M\t' + RM, 'A\t' + RDIR + 'x'])
           and not modified_exactly(['M\t' + TST, 'M\t' + RM])
           and not modified_exactly(['M\t' + TST, 'M\t' + CR, 'M\t' + RM, 'M\tverification/README.md']))
    good = [(n, ['propext', 'Classical.choice', 'Quot.sound']) for n in
            ('rational_point', 'rational_solutions', 'exists_int_scaling', TRANSFER, LEMMA,
             'spectral_classification_of_BG', 'gaps_eq_of_equal_probabilities', 'twoBranch_of_BGClassification')]
    report('self: K accepts a clean log', ctl_K(synthetic_log(good))[0])
    kmuts = [('the lemma\'s report missing', synthetic_log([g for g in good if g[0] != LEMMA])),
             ('sorryAx in the lemma\'s report', synthetic_log([(n, ax + ['sorryAx'] if n == LEMMA else ax)
                                                                for n, ax in good])),
             ('a non-permitted axiom', synthetic_log([(n, ax + ['Lean.ofReduceBool'] if n == LEMMA else ax)
                                                      for n, ax in good])),
             ('the count at D (5988)', synthetic_log(good, count=5988)),
             ('a failed gate', synthetic_log(good, gate='FAIL'))]
    for name, log in kmuts:
        report('self: K rejects: ' + name, not ctl_K(log)[0])
    return not FAIL


def main(argv):
    if argv[:1] == ['--self-test']:
        ok = self_test()
    elif argv[:1] == ['check'] and len(argv) >= 4 and argv[2] == '--freeze':
        ok = check(argv[1], argv[3])
    elif argv[:1] == ['verdict'] and len(argv) >= 6 and argv[2] == '--freeze' and argv[4] == '--log':
        ok = verdict(argv[1], argv[3], argv[5])
    else:
        print(__doc__)
        return 2
    print('controls: %s (%d failure(s))' % ('OK' if ok else 'FAILED', len(FAIL)))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
