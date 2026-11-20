#!/usr/bin/env python3
"""A1-SCOPE Phase 0: regression controls and decision-rule predicates for the Phase 1 edit.

Fixed before any manuscript edit (PREREG.md section 4). Standard library only.

    python3 -I phase0_controls.py --root <checkout> [--base <sha>] [--json <out>]
    python3 -I phase0_controls.py --self-test

The base tree is read with `git show <base>:<path>`; the head tree is the working tree at --root.
Each control prints PASS or FAIL and the run writes a JSON record (control id -> status, detail).
Exit status: 0 when every regression control passes, 1 otherwise. The decision-rule predicates
DR-* are reported separately and do not affect the exit status: they are expected to fail at the
base (no edit yet) and to pass after Phase 1.
"""
import argparse, hashlib, json, os, re, subprocess, sys

BASE = 'd5735bedb3958394e3e095a4513d9fb5996d079d'
MAIN = 'papers/Main.md'

# CTL-1, CTL-2, CTL-3, CTL-4, CTL-5: paragraphs of Main frozen byte for byte, by opening text.
FROZEN = {
    'CTL-1': [  # S <=> D <=> Q_fb
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
# CTL-7: no added sentence may present a probability law, typicality, recurrence or inflow as derived.
NEW_LABELS = ['(NR)', '(IL)', '(ED)', '(IN)', '(RET)', '(REV)']
STATUS_TOKENS = re.compile(r'\b(posit|posited|hypothes[ie]s|open|supplied|declared|assumed|assume[sd]?|'
                           r'condition|conditions|sufficient)\b', re.I)
DERIVE = re.compile(r'\b(derive[sd]?|derivation|forces?|selects?|determines?|guarantees?|implies|yields?|'
                    r'entails?)\b[^.;]{0,90}\b(probability law|invariant (law|measure|probability)|the measure|'
                    r'canonical measure|typicality|typical|recurrence|recurs|return|inflow|boundary supply)\b',
                    re.I)
DERIVE2 = re.compile(r'\b(probability law|invariant (law|measure|probability)|the measure|canonical measure|'
                     r'typicality|recurrence|return|inflow|boundary supply)\b[^.;]{0,60}\b(is|are|was|were|being)\s+'
                     r'(derived|forced|selected|determined|guaranteed|excluded|established)\b', re.I)
SCOPE_TOKENS = re.compile(r'(finite representative|finite model|finite carrier|under A1|\bA1\b|\(NR\)|\(IL\)|'
                          r'\(ED\)|\(RET\)|\(REV\)|\(IN\)|hypothes|posit|supplied|declared|assum|conditional|'
                          r'open|if\b|whenever|given)', re.I)
INFLOW_OPEN = re.compile(r'\(IN\)[^.]*\bopen\b|\bopen\b[^.]*\(IN\)', re.I)
# CTL-8: register (AGENTS.md sections A.32 and A.33) on added sentences in papers/.
HISTORY = re.compile(r'\b(no longer|is now|are now|now settled|in its current form|the corrected form|'
                     r'as redefined|formerly|previously stated|earlier revision)\b', re.I)
META = re.compile(r'\b(should not be read as|the reader should note|the discipline maintained|'
                  r'stated in that register)\b', re.I)
CAPS_OK = {'CPTP', 'BQP', 'QCD', 'LQG', 'BFSS', 'CHSH', 'ETH', 'ENNReal', 'FULL', 'TV'}
CAPS = re.compile(r'(?<![\w`$\\(-])([A-Z]{4,})(?![\w`$-])')
# CTL-6: no Lean edits; no new kernel identifier cited in Main; registry dispositions unchanged.
LEAN_DIRS = ('verification/lean-mathlib/', 'verification/lean/')
REGISTRY = 'verification/lean-manuscript-census.json'
IDENT = re.compile(r'`([A-Za-z_][A-Za-z0-9_\'.]*)`')


def git_show(root, rev, path):
    try:
        return subprocess.run(['git', '-C', root, 'show', '%s:%s' % (rev, path)], check=True,
                              capture_output=True, text=True).stdout
    except subprocess.CalledProcessError:
        return None


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
    """pairs: list of (path, base_text, head_text). Returns CTL-7 and CTL-8 failures."""
    c7, c8 = [], []
    for path, b, h in pairs:
        for s in added_sentences(b or '', h or ''):
            plain = strip_code_math(s)
            if (DERIVE.search(plain) or DERIVE2.search(plain)) and not SCOPE_TOKENS.search(s):
                c7.append('%s: derivation wording without scope: %s' % (path, s[:160]))
            if any(l in s for l in NEW_LABELS) and not STATUS_TOKENS.search(s):
                c7.append('%s: new label without status: %s' % (path, s[:160]))
            if '(IN)' in s and not INFLOW_OPEN.search(s):
                c7.append('%s: (IN) not marked open: %s' % (path, s[:160]))
            if path.startswith('papers/'):
                if HISTORY.search(plain) or META.search(plain):
                    c8.append('%s: history/meta phrase: %s' % (path, s[:160]))
                for m in CAPS.finditer(plain):
                    if m.group(1) not in CAPS_OK:
                        c8.append('%s: caps emphasis %s: %s' % (path, m.group(1), s[:120]))
    return c7, c8


def ledger(text):
    p = find(paragraphs(text), '**The posit ledger.**')
    return p[0] if len(p) == 1 else ''


def status_remark(text):
    p = find(paragraphs(text), '*Remark (status of the early commitments).*')
    return p[0] if len(p) == 1 else ''


def item_ii(led):
    m = re.search(r'\(ii\)(.*?)(?=; \(iii\))', led, re.S)
    return m.group(1) if m else ''


def section(text, start, end):
    i = text.find(start)
    j = text.find(end, i + 1) if i >= 0 else -1
    return text[i:j] if i >= 0 and j > i else ''


# DR-3: per-consumer sufficient conditions that Phase 1 must leave explicit in Main. Each row lists
# alternatives; a row is met when every token of at least one alternative occurs inside the named
# section. Fixed in advance (PREREG.md section 6); the reviewer checks the semantics.
DR3 = {
    'M4 one-step theorem: (NR) corollary': ('### 2.3', '### 2.4', [['(NR)', 'Corollary (near-return)']]),
    'M7(i) index-free form under (NR)': ('### 2.3', '### 2.4', [['(NR)', 'index-free']]),
    'M5/M7(ii) index L on the finite representative': ('### 2.3', '### 2.4', [['finite representative', '$L$']]),
    'M3 doubly stochastic corner: (IL) or finite carrier': ('### 3.2', '### 3.3', [['(IL)', 'doubly stochastic']]),
    'M11 bijectivity: (REV)': ('### 4.5', '### 4.6', [['(REV)']]),
    'M1/M2 selection: (ED) or finite representative': ('### 4.5', '### 4.6', [['(ED)'], ['(iv)', 'finite representative']]),
    'M18/M20 operator step: (IL) or finiteness of S': ('### 4.6', '## 5.', [['(IL)'], ['finiteness of $S$']]),
    'M19 typicality: finite representative': ('### 4.6', '## 5.', [['finiteness of $S$', 'canonical-typicality']]),
    'inflow: (IN) open': ('### 4.5', '### 4.6', [['(IN)', 'open']]),
}


def decision_rule(head_main):
    led = ledger(head_main)
    ii = item_ii(led)
    dr = {}
    dr['DR-1 ledger item (ii) is a sufficient condition'] = bool(ii) and 'sufficient' in ii
    concl = [s for s in re.split(r'(?<=\.)\s+', led) if 'conditional on the full list' in s]
    dr['DR-2 closing sentence qualifies item (ii)'] = (not concl) or all(
        '(ii)' in s and 'sufficient' in s for s in concl)
    dr['DR-2b status Remark states sufficiency'] = 'sufficient' in status_remark(head_main)
    for name, (a, b, alts) in DR3.items():
        sec = section(head_main, a, b)
        dr['DR-3 ' + name] = bool(sec) and any(all(t in sec for t in alt) for alt in alts)
    return dr


def registry_status(text):
    r = json.loads(text)
    fams = r.get('families', r)
    return {f.get('name', f.get('family', '?')): f.get('status') for f in fams}


def run(root, base):
    out = {'base': base, 'controls': {}, 'decision_rule': {}}
    bm, hm = git_show(root, base, MAIN), open(os.path.join(root, MAIN), encoding='utf-8').read()
    if bm is None:
        print('cannot read base %s' % base)
        return 2, out
    for ctl, bad in check_frozen(bm, hm).items():
        out['controls'][ctl] = {'status': 'FAIL' if bad else 'PASS', 'detail': bad}
    changed = subprocess.run(['git', '-C', root, 'diff', '--name-only', base, '--', 'papers', 'book',
                              'verification'], capture_output=True, text=True).stdout.split()
    changed += subprocess.run(['git', '-C', root, 'ls-files', '--others', '--exclude-standard',
                               'papers', 'book', 'verification'], capture_output=True, text=True).stdout.split()
    pairs = []
    for p in sorted(set(changed)):
        if p.endswith('.md') and (p.startswith('papers/') or p.startswith('book/')):
            hp = os.path.join(root, p)
            pairs.append((p, git_show(root, base, p) or '',
                          open(hp, encoding='utf-8').read() if os.path.exists(hp) else ''))
    c7, c8 = check_added(pairs)
    out['controls']['CTL-7'] = {'status': 'FAIL' if c7 else 'PASS', 'detail': c7}
    out['controls']['CTL-8'] = {'status': 'FAIL' if c8 else 'PASS', 'detail': c8}
    bad6 = [p for p in changed if p.startswith(LEAN_DIRS) or p == REGISTRY]
    bid = set(IDENT.findall(bm))
    new_ids = sorted(set(IDENT.findall(hm)) - bid)
    if new_ids:
        bad6.append('new backticked identifiers in Main: %s' % ', '.join(new_ids[:20]))
    reg_b = git_show(root, base, REGISTRY)
    reg_h = open(os.path.join(root, REGISTRY), encoding='utf-8').read()
    if registry_status(reg_b) != registry_status(reg_h):
        bad6.append('registry family dispositions differ from base')
    cen = subprocess.run([sys.executable, '-I', os.path.join(root, 'tools/lean_manuscript_census.py'),
                          '--root', root], capture_output=True, text=True)
    if cen.returncode != 0:
        bad6.append('lean_manuscript_census exit %d' % cen.returncode)
    out['controls']['CTL-6'] = {'status': 'FAIL' if bad6 else 'PASS', 'detail': bad6}
    st = subprocess.run([sys.executable, '-I', os.path.join(root, 'tools/staleness_check.py'), '--root', root],
                        capture_output=True, text=True)
    out['controls']['CTL-9'] = {'status': 'PASS' if st.returncode == 0 else 'FAIL',
                                'detail': [] if st.returncode == 0 else st.stdout.splitlines()[-5:]}
    led = ledger(hm)
    bad10 = []
    if 'Fourteen items' not in led:
        bad10.append('ledger count sentence "Fourteen items" missing')
    for i in ['(i)', '(ii)', '(iii)', '(iv)', '(v)', '(vi)', '(vii)', '(viii)', '(ix)', '(x)', '(xi)',
              '(xii)', '(xiii)', '(xiv)']:
        if i not in led:
            bad10.append('ledger item %s missing' % i)
    out['controls']['CTL-10'] = {'status': 'FAIL' if bad10 else 'PASS', 'detail': bad10}
    out['decision_rule'] = decision_rule(hm)
    ok = all(v['status'] == 'PASS' for v in out['controls'].values())
    return (0 if ok else 1), out


def self_test():
    """Each control must fail on a violating edit and pass on the identity edit."""
    fails = []
    main = ('**The posit ledger.** Items (i) x; (ii) total finiteness; (iii) y. Fourteen items. '
            'The claims are conditional on the full list.\n\n'
            '**Definition.** An *observation* is a triple (S, phi, V).\n\n'
            '**Lemma 1** (Finiteness). Finite C_V.\n\n'
            'only finite visible resolution is a theorem.\n')
    FROZEN_SAVE = dict(FROZEN)
    FROZEN.clear()
    FROZEN['CTL-5'] = ['**Definition.** An *observation* is a triple', '**Lemma 1** (Finiteness).']
    if any(check_frozen(main, main).values()):
        fails.append('CTL-5 identity edit failed')
    if not check_frozen(main, main.replace('Finite C_V.', 'Finite C_V and S.'))['CTL-5']:
        fails.append('CTL-5 did not detect a changed Lemma 1')
    if not check_frozen(main, main.replace('only finite visible resolution is a theorem', 'x'))['CTL-5']:
        fails.append('CTL-5 did not detect the removed reading')
    FROZEN.clear()
    FROZEN.update(FROZEN_SAVE)
    viol = [
        ('papers/Main.md', 'The invariant measure is derived from the dynamics alone.', 'CTL-7'),
        ('papers/Main.md', 'The law (IL) holds for nature.', 'CTL-7'),
        ('papers/Main.md', 'Inflow is excluded by (IN) at spatial infinity.', 'CTL-7'),
        ('papers/Main.md', 'This bound is now settled.', 'CTL-8'),
        ('papers/Main.md', 'The bound holds for EVERY carrier.', 'CTL-8'),
    ]
    for path, s, ctl in viol:
        c7, c8 = check_added([(path, 'Old text.', 'Old text.\n\n' + s)])
        got = c7 if ctl == 'CTL-7' else c8
        if not got:
            fails.append('%s missed: %s' % (ctl, s))
    ok_add = ('A later common near-return (NR) is a posited sufficient condition. '
              'On a finite representative the exact return supplies it. '
              'The condition (IN) on incoming supply is open.')
    c7, c8 = check_added([('papers/Main.md', 'Old text.', 'Old text.\n\n' + ok_add)])
    if c7 or c8:
        fails.append('false positive on compliant text: %s %s' % (c7, c8))
    if any(decision_rule(main).get(k) for k in ('DR-1 ledger item (ii) is a sufficient condition',
                                                 'DR-2b status Remark states sufficiency')):
        fails.append('DR passed on the unedited ledger')
    good = main.replace('(ii) total finiteness;', '(ii) total finiteness, one sufficient condition;')
    if not decision_rule(good)['DR-1 ledger item (ii) is a sufficient condition']:
        fails.append('DR-1 failed on a compliant ledger')
    print('self-test:', 'PASS' if not fails else 'FAIL')
    for f in fails:
        print('  ', f)
    return 0 if not fails else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default='.')
    ap.add_argument('--base', default=BASE)
    ap.add_argument('--json')
    ap.add_argument('--self-test', action='store_true')
    a = ap.parse_args()
    if a.self_test:
        sys.exit(self_test())
    code, out = run(os.path.abspath(a.root), a.base)
    for k, v in out['controls'].items():
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
