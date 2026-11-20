#!/usr/bin/env python3
"""A1-SCOPE Phase 0: regression controls and decision-rule predicates for the Phase 1 edit.

Fixed before any manuscript edit (PREREG.md sections 5 and 7). Standard library only.

    python3 -I phase0_controls.py --root <checkout> [--base <sha>] [--json <out>]
    python3 -I phase0_controls.py --root <checkout> --dry-run     # base + phase1_ledger.json, in memory
    python3 -I phase0_controls.py --self-test

The base tree is read with `git show <base>:<path>`. The head is the working tree at --root, or, with
--dry-run, the base with every splice of phase1_ledger.json applied in memory (nothing is written).
Each control prints PASS, FAIL or N/A and the run can write a JSON record. Exit status: 0 iff no
control FAILs. The decision-rule predicates DR-* are reported separately: unmet at the base, met by
the ledger in the dry run, and required on Phase 1's final head.
"""
import argparse, glob, hashlib, json, os, re, subprocess, sys

BASE = 'd5735bedb3958394e3e095a4513d9fb5996d079d'
MAIN = 'papers/Main.md'
FULL = 'book/The-Incompleteness-of-Observation-FULL.md'
HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(HERE, 'phase1_ledger.json')

# CTL-1 ... CTL-5: paragraphs of Main frozen byte for byte, by opening text.
FROZEN = {
    'CTL-1': [  # S <=> D <=> Q_fb; the (S) paragraph also carries (D) and (Q_fb)
        '**Theorem (finite-horizon stochastic–reversible–unitary equivalence).**',
        '*(S) the finite stochastic laws;*',
        '*Proof.* (S $\\Rightarrow$ D)',
    ],
    'CTL-2': [  # finite-horizon equivalence: dilation and the characterization theorem
        '**Theorem (finite-horizon process dilation).**',
        '*Extension (arbitrary kernels — the response-table form).*',
        '*Proof (constructive).* Let $D$ be a common denominator',
        '**Characterization theorem.**',
        '*(i) $\\mathcal{S}$ is mathematically equivalent',
        '*(ii) $\\mathcal{S}$ is non-Markovian on accessible timescales',
        '*(iii) For some accessible order $k$',
    ],
    'CTL-3': [  # C4r / overlap-and-return route to P-indivisibility
        '**Theorem (overlap and return).**',
        '*Proof.* Distinct rows of $\\Gamma_n = I$',
    ],
    'CTL-4': [  # finite-carrier theorem statements, unchanged as finite-model statements
        '**Lemma 3** (Determinism, reversibility, and the selected measure).',
        '**Theorem.** *Let $\\mathcal{C}_V$ and $\\mathcal{C}_H$ be finite sets with',
        '*Step 1 (Recurrence).*',
        '**Theorem (history readback + finite recurrence implies indivisibility).**',
        '*Proof.* Because $\\varphi$ is a permutation of a finite set',
        '**Lemma (Reverse direction, scoped).**',
        '**Lemma (non-permutation witness).**',
        '**Theorem (CP-indivisibility, framework scope).**',
        '*Proposition (no uniform finite realization).*',
        '**Theorem (C3 necessity).**',
        '**Theorem (physical memory: C2, process form).**',
        '**Coupling-graph causal cone.**',
    ],
    'CTL-5': [  # observer-relative finiteness reading
        '**Definition.** An *observation* is a triple',
        '**Lemma 1** (Finiteness).',
    ],
}
REQUIRED_TEXT = {
    'CTL-3': ['`pIndivisible_of_identity_return_of_overlap`'],
    'CTL-5': ['only finite visible resolution is a theorem'],
}
# CTL-7: no added sentence presents a law, typicality, recurrence or inflow as derived or physical.
NEW_LABELS = ['(NR)', '(IL)', '(IP)', '(RET)', '(REV)', '(FS)', '(ED)', '(IN)']
STATUS = re.compile(r'(not adopted|\bassumed\b|\bhypothes[ie]s\b|\bcondition\b|\bsufficient\b|\bpostulate\b|'
                    r'\balternative\b|\bopen\b|full support)', re.I)
VERB = (r'(derive[sd]?|derivation|forces?|selects?|determines?|guarantees?|implies|yields?|entails?|follows|'
        r'fix(es)?|establish(es|ed)?|ensures?)')
TARGET = (r'(probability law|invariant (law|measure|probability)|the measure|typicality|typical|recurrence|recurs|'
          r'inflow|boundary supply|the universe)')
DERIVE = re.compile(r'\b' + VERB + r'\b[^.;]{0,90}\b' + TARGET + r'\b|\b' + TARGET + r'\b[^.;]{0,90}\b' + VERB + r'\b',
                    re.I)
HARD = re.compile(r'\b(holds? in nature|in nature|physically real|is derived|are derived|derived from|'
                  r'follows from the dynamics)\b', re.I)
NEGATION = re.compile(r'\b(not|no|neither|nor|never|without)\b', re.I)
CONDITIONAL = re.compile(r'\b(if|whenever|unless|assumed|assuming)\b', re.I)
# CTL-8: register (AGENTS.md sections A.32 and A.33) on added sentences in papers/.
HISTORY = re.compile(r'\b(no longer|is now|are now|now settled|in its current form|the corrected form|'
                     r'as redefined|formerly|previously stated|earlier revision)\b', re.I)
META = re.compile(r'\b(should not be read as|the reader should note|the discipline maintained|'
                  r'stated in that register)\b', re.I)
CAPS_OK = {'CPTP', 'BQP', 'QCD', 'LQG', 'BFSS', 'CHSH', 'ETH', 'FULL'}
CAPS = re.compile(r'(?<![\w`$\\(-])([A-Z]{4,})(?![\w`$-])')
# CTL-6: no Lean edits; no new kernel identifier cited in Main; registry dispositions unchanged.
LEAN_DIRS = ('verification/lean-mathlib/', 'verification/lean/')
REGISTRY = 'verification/lean-manuscript-census.json'
IDENT = re.compile(r'`([A-Za-z_][A-Za-z0-9_\'.]*)`')
# CTL-10: the fourteen ledger items, each exactly once.
ITEMS = ['(i) Axiom 2', '(ii) total finiteness', '(iii) the record-preservation', '(iv) the measure selection',
         '(v) the hidden-sector mixing', '(vi) spatial isotropy', '(vii) linearity', '(viii) site factorization',
         '(ix) bounded coupling', '(x) the nearest-neighbour', '(xi) center independence',
         '(xii) background independence', '(xiii) the second-order form', '(xiv) measurement independence']
# CTL-12: status wording that may not decrease, per file in Phase 1 scope.
STATUS_COUNTS = {'not adopted': lambda t: t.count('not adopted'),
                 'open': lambda t: len(re.findall(r'\bopen\b', t)),
                 'sentences pairing A1 or item (ii) with posit or hypothesis': lambda t: sum(
                     1 for x in sentences(t) if re.search(r'\bA1\b|\(ii\)|[Tt]otal[- ]finiteness', x)
                     and re.search(r'\b(posit|hypothesis)\b', x))}
PHASE1_FILES = [MAIN, FULL, 'book/ch00-introduction.md', 'book/ch01-observation.md', 'book/ch19-open-problems.md',
                'book/appendix-b-derivations.md', 'book/appendix-c-objections.md', 'book/glossary.md',
                'book/preface.md']


def git_show(root, rev, path):
    r = subprocess.run(['git', '-C', root, 'show', '%s:%s' % (rev, path)], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def git_ls(root, rev, pattern):
    r = subprocess.run(['git', '-C', root, 'ls-tree', '--name-only', rev, pattern], capture_output=True, text=True)
    return [p for p in r.stdout.split() if p.endswith('.md')]


def paragraphs(text):
    return [p.strip('\n') for p in re.split(r'\n\s*\n', text) if p.strip()]


def find(paras, prefix):
    return [p for p in paras if p.lstrip().startswith(prefix)]


def sentences(text):
    out = []
    for p in paragraphs(text):
        out += [s.strip() for s in re.split(r'(?<=[.;:])\s+(?=[A-Z*(\[$])', p) if s.strip()]
    return out


def added_sentences(base, head):
    bs = set(sentences(base))
    return [s for s in sentences(head) if s not in bs]


def strip_code_math(s):
    s = re.sub(r'`[^`]*`', ' ', s)
    s = re.sub(r'\$\$.*?\$\$', ' ', s)
    return re.sub(r'\$[^$]*\$', ' ', s)


def section(text, start, end):
    i = text.find(start)
    j = text.find(end, i + 1) if i >= 0 else -1
    return text[i:j] if i >= 0 and j > i else ''


def apply_ledger(base_texts, ledger):
    out = dict(base_texts)
    for s in ledger['splices']:
        t = out[s['file']]
        if t.count(s['old']) != 1 or hashlib.sha256(s['old'].encode()).hexdigest() != s['old_sha256']:
            raise ValueError('ledger splice %s does not apply' % s['unit'])
        out[s['file']] = t.replace(s['old'], s['new'], 1)
    return out


def check_frozen(base_main, head_main):
    res = {}
    bp, hp = paragraphs(base_main), paragraphs(head_main)
    for ctl, prefixes in FROZEN.items():
        bad = []
        for pre in prefixes:
            b, h = find(bp, pre), find(hp, pre)
            if len(b) != 1:
                bad.append('base has %d paragraphs opening %r' % (len(b), pre[:50]))
            elif len(h) != 1:
                bad.append('head has %d paragraphs opening %r' % (len(h), pre[:50]))
            elif b[0] != h[0]:
                bad.append('changed: %r' % pre[:50])
        for t in REQUIRED_TEXT.get(ctl, []):
            if t not in head_main:
                bad.append('missing text %r' % t)
        res[ctl] = bad
    return res


def check_added(pairs):
    """pairs: (path, base_text, head_text). Returns CTL-7 and CTL-8 failures."""
    c7, c8 = [], []
    for path, b, h in pairs:
        for s in added_sentences(b or '', h or ''):
            plain = strip_code_math(s)
            if HARD.search(plain) and not NEGATION.search(plain):
                c7.append('%s: derived/physical wording: %s' % (path, s[:160]))
            elif DERIVE.search(plain) and not (NEGATION.search(plain) or CONDITIONAL.search(plain)):
                c7.append('%s: derivation wording, neither negated nor conditional: %s' % (path, s[:160]))
            if any(l in s for l in NEW_LABELS) and not STATUS.search(s):
                c7.append('%s: new label without status: %s' % (path, s[:160]))
            if path.startswith('papers/'):
                if HISTORY.search(plain) or META.search(plain):
                    c8.append('%s: history/meta phrase: %s' % (path, s[:160]))
                for m in CAPS.finditer(plain):
                    if m.group(1) not in CAPS_OK:
                        c8.append('%s: caps emphasis %s: %s' % (path, m.group(1), s[:120]))
    return c7, c8


def check_ledger_exact(base_texts, head_texts, ledger):
    bad = []
    try:
        expect = apply_ledger(base_texts, ledger)
    except ValueError as e:
        return [str(e)]
    for p in sorted(set(base_texts) | set(head_texts)):
        if head_texts.get(p) != expect.get(p):
            bad.append('%s differs from base + ledger' % p)
    return bad


def check_status(base_texts, head_texts):
    bad = []
    for p in PHASE1_FILES:
        b, h = base_texts.get(p, ''), head_texts.get(p, '')
        for name, fn in STATUS_COUNTS.items():
            nb, nh = fn(b), fn(h)
            if nh < nb:
                bad.append('%s: "%s" count %d < base %d' % (p, name, nh, nb))
    return bad


def check_full_parity(base_texts, head_texts):
    bad = []
    chapters = [p for p in head_texts if p.startswith('book/') and p not in (FULL, 'book/README.md')]
    full_h = set(head_texts.get(FULL, '').split('\n'))
    chap_lines = set()
    for p in chapters:
        for line in head_texts[p].split('\n'):
            if line.strip():
                chap_lines.add(line)
                if line not in full_h:
                    bad.append('%s line absent from FULL: %s' % (p, line[:80]))
    def only_full(texts):
        cl = set()
        for p in texts:
            if p.startswith('book/') and p not in (FULL, 'book/README.md'):
                cl |= {l for l in texts[p].split('\n') if l.strip()}
        return {l for l in texts.get(FULL, '').split('\n') if l.strip() and l not in cl}
    if only_full(head_texts) != only_full(base_texts):
        bad.append('FULL-only lines differ from base')
    return bad[:20]


def ledger_para(text):
    p = find(paragraphs(text), '**The posit ledger.**')
    return p[0] if len(p) == 1 else ''


def status_remark(text):
    p = find(paragraphs(text), '*Remark (status of the early commitments).*')
    return p[0] if len(p) == 1 else ''


def item_ii(led):
    m = re.search(r'\(ii\) total finiteness(.*?)(?=; \(iii\))', led, re.S)
    return m.group(1) if m else ''


# DR-3. Change rows: every token must occur in sentences of the section that are absent from the base.
# Standing rows: finite-model scope phrases present at the base must remain at the head.
DR3_CHANGE = {
    'M4 corollary (NR)': ('### 2.3', '### 2.4', ['(NR)', 'not adopted']),
    'M7(i) index-free form with (FS) and the direct divisor': ('### 2.3', '### 2.4',
                                                              ['index-free', '(FS)', 'Q_s \\cdots Q_{t-1}']),
    'M5/M7(ii) index L on the finite representative': ('### 2.3', '### 2.4', ['finite representative', '$L$']),
    'M3 corner (IP)': ('### 3.2', '### 3.3', ['(IP)', '\\sum_a \\Gamma_t(a, b)']),
    'M11 bijectivity (REV)': ('### 4.5', '### 4.6', ['(REV)']),
    'M18/M20 decay estimate (IL), narrowed': ('### 4.6', '## 5.', ['(IL)', 'L^2(\\mu)', 'canonical-typicality clause']),
}
DR3_STANDING = {
    'M1/M2 selection on the finite representative': ['As for the measure on a finite representative',
                                                     'the counting measure is selected among invariant measures'],
    'M9 CP-indivisibility on the permutation-dilation family': ['For the permutation-dilation family'],
    'M13 orbit capacity': ['an orbit of period $p$ makes at most $p$ states dynamically accessible'],
    'M16 physical memory in the uniform-prior model': ['the uniform hidden prior of the model above'],
    'M19 typicality with finiteness of S': ['finiteness of $S$, the canonical-typicality result [31]'],
}


def decision_rule(base_main, head_main):
    led = ledger_para(head_main)
    ii = item_ii(led)
    dr = {}
    dr['DR-1 ledger item (ii) is a sufficient condition'] = bool(ii) and 'sufficient' in ii
    concl = [s for s in re.split(r'(?<=\.)\s+', led) if 'conditional on the full list' in s]
    dr['DR-2 closing sentence present and qualifies item (ii)'] = bool(concl) and all(
        '(ii)' in s and 'sufficient' in s for s in concl)
    dr['DR-2b status Remark states sufficiency'] = 'sufficient' in status_remark(head_main)
    for name, (a, b, toks) in DR3_CHANGE.items():
        added = ' '.join(added_sentences(section(base_main, a, b), section(head_main, a, b)))
        dr['DR-3 ' + name] = all(t in added for t in toks)
    cor = find(paragraphs(head_main), '*Corollary (near-return).*')
    dr['DR-3 corollary paragraph carries its proof'] = (len(cor) == 1 and '*Proof.*' in cor[0]
                                                         and '$\\square$' in cor[0])
    for name, phrases in DR3_STANDING.items():
        dr['DR-3 standing: ' + name] = all(p in base_main and p in head_main for p in phrases)
    return dr


def registry_status(text):
    r = json.loads(text)
    return {f.get('name', f.get('family', '?')): f.get('status') for f in r.get('families', r)}


def run(root, base, dry):
    out = {'base': base, 'mode': 'dry-run' if dry else 'working-tree', 'controls': {}, 'decision_rule': {}}
    ledger = json.load(open(LEDGER, encoding='utf-8'))
    paths = sorted(set(git_ls(root, base, 'papers/') + git_ls(root, base, 'book/')))
    base_texts = {p: git_show(root, base, p) for p in paths}
    if any(v is None for v in base_texts.values()):
        print('cannot read base %s' % base)
        return 2, out
    if dry:
        head_texts = apply_ledger(base_texts, ledger)
    else:
        head_paths = sorted(glob.glob(os.path.join(root, 'papers', '*.md')) + glob.glob(os.path.join(root, 'book', '*.md')))
        head_texts = {os.path.relpath(p, root): open(p, encoding='utf-8').read() for p in head_paths}
    bm, hm = base_texts[MAIN], head_texts[MAIN]
    def put(ctl, bad, na=False):
        out['controls'][ctl] = {'status': 'N/A' if na else ('FAIL' if bad else 'PASS'), 'detail': bad}
    for ctl, bad in check_frozen(bm, hm).items():
        put(ctl, bad)
    pairs = [(p, base_texts.get(p, ''), head_texts.get(p, '')) for p in sorted(set(base_texts) | set(head_texts))
             if base_texts.get(p) != head_texts.get(p)]
    c7, c8 = check_added(pairs)
    put('CTL-7', c7)
    put('CTL-8', c8)
    changed = [] if dry else subprocess.run(['git', '-C', root, 'diff', '--name-only', base, '--', 'verification'],
                                            capture_output=True, text=True).stdout.split()
    bad6 = [p for p in changed if p.startswith(LEAN_DIRS) or p == REGISTRY]
    new_ids = sorted(set(IDENT.findall(hm)) - set(IDENT.findall(bm)))
    if new_ids:
        bad6.append('new backticked identifiers in Main: %s' % ', '.join(new_ids[:20]))
    reg_b = git_show(root, base, REGISTRY)
    reg_h = reg_b if dry else open(os.path.join(root, REGISTRY), encoding='utf-8').read()
    if registry_status(reg_b) != registry_status(reg_h):
        bad6.append('registry family dispositions differ from base')
    if not dry:
        cen = subprocess.run([sys.executable, '-I', os.path.join(root, 'tools/lean_manuscript_census.py'),
                              '--root', root], capture_output=True, text=True)
        if cen.returncode != 0:
            bad6.append('lean_manuscript_census exit %d' % cen.returncode)
    put('CTL-6', bad6)
    if dry:
        put('CTL-9', ['requires a rebuild of the working tree'], na=True)
    else:
        st = subprocess.run([sys.executable, '-I', os.path.join(root, 'tools/staleness_check.py'), '--root', root],
                            capture_output=True, text=True)
        put('CTL-9', [] if st.returncode == 0 else st.stdout.splitlines()[-3:])
    led = ledger_para(hm)
    bad10 = [] if led.count('Fourteen items') == 1 else ['"Fourteen items" not present exactly once']
    bad10 += ['ledger item %r occurs %d times' % (i, led.count(i)) for i in ITEMS if led.count(i) != 1]
    put('CTL-10', bad10)
    if dry:
        put('CTL-11', [], na=True)
    else:
        put('CTL-11', check_ledger_exact(base_texts, head_texts, ledger) if hm != bm or any(
            base_texts.get(p) != head_texts.get(p) for p in head_texts) else [])
    put('CTL-12', check_status(base_texts, head_texts))
    put('CTL-13', check_full_parity(base_texts, head_texts))
    out['decision_rule'] = decision_rule(bm, hm)
    ok = all(v['status'] != 'FAIL' for v in out['controls'].values())
    return (0 if ok else 1), out


def self_test():
    """Each control must fail on a violating edit and pass on a compliant one."""
    fails = []
    def expect(cond, msg):
        if not cond:
            fails.append(msg)
    main = ('**The posit ledger.** Items (i) Axiom 2; (ii) total finiteness of S (an open hypothesis, not adopted); '
            '(iii) the record-preservation y. Fourteen items. The claims are conditional on the full list.\n\n'
            '**Definition.** An *observation* is a triple (S, phi, V).\n\n**Lemma 1** (Finiteness). Finite C_V.\n\n'
            'only finite visible resolution is a theorem. A1 is an open hypothesis, not adopted.\n')
    saved = dict(FROZEN)
    FROZEN.clear()
    FROZEN['CTL-5'] = ['**Definition.** An *observation* is a triple', '**Lemma 1** (Finiteness).']
    expect(not any(check_frozen(main, main).values()), 'CTL-5 identity edit failed')
    expect(check_frozen(main, main.replace('Finite C_V.', 'Finite C_V and S.'))['CTL-5'], 'CTL-5 missed Lemma 1 edit')
    expect(check_frozen(main, main.replace('only finite visible resolution is a theorem', 'x'))['CTL-5'],
           'CTL-5 missed the removed reading')
    FROZEN.clear()
    FROZEN.update(saved)
    # CTL-7 and CTL-8, including the review's adversarial sentences (#1442 review 7031480016)
    viol7 = ['The condition (NR) holds in nature, so physical recurrence is derived.',
             'The invariant law is derived from the dynamics alone, given the condition (IL).',
             'Recurrence of the universe follows from the dynamics.',
             'The invariant measure is derived from the dynamics alone.',
             'The law (IL) holds for nature.']
    for s in viol7:
        c7, _ = check_added([('papers/Main.md', 'Old text.', 'Old text.\n\n' + s)])
        expect(c7, 'CTL-7 missed: ' + s)
    for s in ['This bound is now settled.', 'The bound holds for EVERY carrier.']:
        _, c8 = check_added([('papers/Main.md', 'Old text.', 'Old text.\n\n' + s)])
        expect(c8, 'CTL-8 missed: ' + s)
    ok_add = ('Assume, as a hypothesis of this result and not adopted, the near-return condition (NR). '
              'On a finite representative Step 1 supplies the condition (NR) at every multiple of $N$ exceeding $s$. '
              'The recurrence is not derived from the dynamics.')
    c7, c8 = check_added([('papers/Main.md', 'Old text.', 'Old text.\n\n' + ok_add)])
    expect(not c7 and not c8, 'false positive on compliant text: %s %s' % (c7, c8))
    # CTL-12: deleting "not adopted"
    b = {MAIN: main}
    expect(check_status(b, {MAIN: main.replace(', not adopted', '')}), 'CTL-12 missed deleted "not adopted"')
    expect(not check_status(b, {MAIN: main}), 'CTL-12 identity failed')
    # CTL-11: a token-only insertion is not the ledger
    led = {'splices': [{'unit': 'X', 'file': MAIN, 'old': 'Fourteen items.',
                        'old_sha256': hashlib.sha256(b'Fourteen items.').hexdigest(),
                        'new': 'Fourteen items; (ii) is one sufficient condition.'}]}
    good = main.replace('Fourteen items.', 'Fourteen items; (ii) is one sufficient condition.')
    expect(not check_ledger_exact(b, {MAIN: good}, led), 'CTL-11 rejected the ledger edit')
    expect(check_ledger_exact(b, {MAIN: good + '\n(NR) Corollary (near-return) index-free (FS).\n'}, led),
           'CTL-11 accepted a token-only insertion')
    # CTL-10: exact item labels
    full_led = '**The posit ledger.** ' + '; '.join(ITEMS) + '. Fourteen items.'
    expect(all(full_led.count(i) == 1 for i in ITEMS), 'CTL-10 item list not unique in a complete ledger')
    expect(full_led.replace('(x) the nearest-neighbour', '(x) the').count('(x) the nearest-neighbour') == 0,
           'CTL-10 missed a deleted item')
    # CTL-13: FULL parity
    bt = {FULL: 'Title\nA line.\nB line.\n', 'book/ch01.md': 'A line.\n', 'book/ch02.md': 'B line.\n'}
    expect(not check_full_parity(bt, bt), 'CTL-13 identity failed')
    ht = dict(bt)
    ht['book/ch01.md'] = 'A line, edited.\n'
    expect(check_full_parity(bt, ht), 'CTL-13 missed an unmirrored chapter edit')
    # DR: unedited ledger unmet; deleting the closing sentence leaves DR-2 unmet; diff-based DR-3
    expect(not decision_rule(main, main)['DR-1 ledger item (ii) is a sufficient condition'], 'DR-1 met at base')
    nolast = main.replace(' The claims are conditional on the full list.', '')
    expect(not decision_rule(main, nolast)['DR-2 closing sentence present and qualifies item (ii)'],
           'DR-2 met with the closing sentence deleted')
    sec = '### 2.3\n\nOld (NR) not adopted.\n\n### 2.4\n'
    expect(not decision_rule(sec, sec)['DR-3 M4 corollary (NR)'], 'DR-3 change row met by base text')
    sec2 = sec.replace('### 2.4', 'New (NR), assumed and not adopted.\n\n### 2.4')
    expect(decision_rule(sec, sec2)['DR-3 M4 corollary (NR)'], 'DR-3 change row missed an added sentence')
    print('self-test:', 'PASS' if not fails else 'FAIL')
    for f in fails:
        print('  ', f)
    return 0 if not fails else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default='.')
    ap.add_argument('--base', default=BASE)
    ap.add_argument('--json')
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--self-test', action='store_true')
    a = ap.parse_args()
    if a.self_test:
        sys.exit(self_test())
    code, out = run(os.path.abspath(a.root), a.base, a.dry_run)
    for k in sorted(out['controls'], key=lambda x: int(x.split('-')[1])):
        v = out['controls'][k]
        print('%-7s %s' % (k, v['status']))
        for d in v['detail'][:10]:
            print('        ', d)
    for k, v in out['decision_rule'].items():
        print('%-5s %s' % ('MET' if v else 'unmet', k))
    if a.json:
        json.dump(out, open(a.json, 'w'), indent=1, sort_keys=True)
    sys.exit(code)


if __name__ == '__main__':
    main()
