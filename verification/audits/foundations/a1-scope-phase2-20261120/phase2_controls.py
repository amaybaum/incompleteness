#!/usr/bin/env python3
"""A1-SCOPE Phase 2: regression controls and decision-rule predicates for the companion edit.

Fixed before any manuscript edit (PREREG.md sections 5 and 6). Standard library only. Reuses the Phase 0
control functions (../a1-scope-phase0-20261120/phase0_controls.py) for CTL-1 to CTL-13 and adds CTL-14 to CTL-16.

    python3 -I phase2_controls.py --root <checkout> [--base <sha>] [--json <out>]
    python3 -I phase2_controls.py --root <checkout> --dry-run     # base + phase2_ledger.json, in memory
    python3 -I phase2_controls.py --root <checkout> --self-test   # countercontrols on the real base texts

The base is read with `git show <base>:<path>`. The head is the working tree at --root or, with --dry-run, the
base with every splice of phase2_ledger.json applied in memory (nothing is written). Exit status: 0 iff no control
FAILs (run) or every countercontrol behaves as required (self-test). The decision-rule predicates DR-* are
reported separately: unmet at the base, met by the ledger in the dry run, required on the final head.
"""
import argparse, glob, hashlib, importlib.util, json, os, re, subprocess, sys

BASE = 'b9168ef0408b5f55b935a4df17cb0841877e221a'
HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(HERE, 'phase2_ledger.json')
DISPOSITIONS = os.path.join(HERE, 'dispositions.json')
P0_PATH = os.path.join(HERE, '..', 'a1-scope-phase0-20261120', 'phase0_controls.py')
SITES = os.path.join(HERE, '..', 'a1-scope-phase0-20261120', 'sites.json')

_spec = importlib.util.spec_from_file_location('phase0_controls', P0_PATH)
P0 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(P0)

MAIN = P0.MAIN
FULL = P0.FULL
SCOPE_PAPERS = ['papers/SM.md', 'papers/Substratum.md', 'papers/GR.md', 'papers/Structure.md']
SCOPE_BOOK = ['book/ch02-substratum.md', 'book/ch03-structural-realism.md', 'book/ch04-methodology.md',
              'book/ch05-gauge-structure.md', 'book/ch07-gravity.md', 'book/ch09-universality.md', 'book/glossary.md']
SCOPE_FILES = SCOPE_PAPERS + SCOPE_BOOK + [FULL]

# CTL-14: a sentence on an in-scope site line that asserts finiteness of the substratum or total carrier must carry
# a condition token, or be listed in the ledger's keep list with its reason.
FIN = re.compile(r"(?<![A-Za-z-])(finite (\$S\$|\$\\mathcal\{S\}\$|set|configuration space|phase space|state space|"
                 r"bijection|substratum|total|carrier|hidden|universe|representative|reversible|bijective|OI|lattice|"
                 r"periodic|product|recurrence|return|order)|\$S\$ (is |be )?(a )?finite|\|S\| ?<|finite cardinality|"
                 r"finitely many (total )?(configurations|states)|total finiteness|[Tt]otal-finiteness|finite \$\|S\|\$)")
COND = re.compile(r"\bA1\b|\bA4\b|posit|hypothes|assum|\bif\b|\bLet\b|condition|sufficient|\(NR\)|representative|"
                  r"model|realiz|counterexample|instance|on a finite|for a finite|for finite|suppose|finite under",
                  re.I)

# CTL-15: companion statements preserved byte for byte (paragraph openings), and required text.
PRESERVED = {
    'papers/GR.md': ['**The classical horizon temperature as a counting derivative, under H-count.**',
                     '**Lemma (Boundary-only dependence).**',
                     '**H-BD** (deep-sector influence bound; posited).',
                     'Let $\\mathcal{C}_V$, $\\mathcal{C}_B$, $\\mathcal{C}_D$ be finite configuration spaces'],
    'papers/SM.md': ['**Theorem 1a (equivariant finite projection preserves spatial symmetry).**',
                     '*Proof.* The $P/Q$ decomposition gives',
                     '**Theorem 19** (Reciprocity of visible transition counts).',
                     '**Proposition 4b (symmetric-point custodial scalarity',
                     '**Corollary** (conditional $d = 3$ selection under A4',
                     '**Linearity and coefficient selection: revised scope.**'],
    'papers/Substratum.md': ['(A4) **Center independence.**', '**Lemma 23.0** (Local-sector uniqueness preservation).',
                             '**Theorem 23** (Layered local reconstruction with Bell compatibility).',
                             '**Theorem 24** (Generators of the substratum gauge group).'],
    'papers/Structure.md': ['**Proposition 9.5** (OI gauge generators (i) and (iii) as observational sub-equivalence).'],
}
REQUIRED = {
    'papers/GR.md': ['Under A1, restrict the finite total system to a conserved energy shell',
                     'Under the hidden-sector condition **H-count** — that the total system is finite (A1)'],
    'papers/Substratum.md': ['(A1) **Finiteness.** The configuration space $S$ is finite.'],
    'papers/SM.md': ['and let the hidden prior be the counting measure'],
}

# DR-3: change rows; every token must occur in sentences of the file that are absent from the base.
DR3 = {
    'M4 (NR) propagation, SM:44': ('papers/SM.md', ['(NR)', 'not adopted', 'weaker sufficient condition']),
    'M4 (NR) propagation, GR:138 and GR:589': ('papers/GR.md', ['(NR)', 'not adopted', 'near-return corollary']),
    'A1 status and (NR), Substratum (A1)': ('papers/Substratum.md',
                                           ['open hypothesis, not adopted', 'one sufficient condition', '(NR)']),
    'A1 status, ch02 mirror': ('book/ch02-substratum.md', ['one sufficient condition']),
    'O-A4 SM:222 carrier': ('papers/SM.md', ['finite periodic', 'quotient of $\\Lambda$']),
    'O-A4 SM:539 parity': ('papers/SM.md', ['even coordinate sum', 'odd side']),
    'O-A4 Lemma 1c(ii) scope': ('papers/SM.md', ['On a finite carrier', 'Fourier fibre', 'not established']),
    'INFLOW Substratum:56': ('papers/Substratum.md', ['Without A1 this replacement is open']),
}


def sents(t):
    return [s for s in re.split(r'(?<=[.;:])\s+(?=[A-Z*(\[$])', t) if s.strip()]


def sha(s):
    return hashlib.sha256(s.encode()).hexdigest()


def load_sites():
    d = json.load(open(SITES, encoding='utf-8'))
    out = [s for s in d['sites'] if s['phase'] in ('P2', 'OA4') and s['file'] in SCOPE_PAPERS + SCOPE_BOOK]
    mirrors = [s for s in d['sites'] if s['file'] == FULL and s['phase'] in ('P2', 'OA4') and s.get('mirror_of')
               and s['mirror_of'].rsplit(':', 1)[0] in SCOPE_BOOK]
    return out, mirrors


def chapter_id(m):
    """sites.json mirror_of, e.g. 'book/ch02-substratum.md:158' -> ('book/ch02-substratum.md', 158)."""
    f, n = m['mirror_of'].rsplit(':', 1)
    return f, int(n)


def unconditioned(line):
    return [x for x in sents(line) if FIN.search(x) and not COND.search(x)]


def site_lines(texts, sites, mirrors):
    """(key, line text) for every in-scope site; FULL mirrors are located by their chapter line's text."""
    out = []
    for s in sites:
        lines = texts[s['file']].split('\n')
        out.append(('%s:%d' % (s['file'], s['line']), lines[s['line'] - 1] if s['line'] <= len(lines) else ''))
    full = texts[FULL].split('\n')
    for m in mirrors:
        f, n = chapter_id(m)
        if f not in texts:
            continue
        ch = texts[f].split('\n')[n - 1]
        hits = [l for l in full if l == ch]
        out.append(('FULL<-%s:%d' % (f, n), hits[0] if hits else ''))
    return out


def check_conditioned(texts, sites, mirrors, keep):
    """CTL-14. keep: {(site key or chapter key, sentence sha)}; FULL mirrors use their chapter key."""
    bad = []
    for key, line in site_lines(texts, sites, mirrors):
        k = key[6:] if key.startswith('FULL<-') else key
        for x in unconditioned(line):
            if (k, sha(x)) not in keep:
                bad.append('%s: unconditioned finiteness not in keep list: %s' % (key, x[:140]))
    return bad


def check_keep_integrity(base_texts, sites, mirrors, keep):
    have = set()
    for key, line in site_lines(base_texts, sites, mirrors):
        k = key[6:] if key.startswith('FULL<-') else key
        for x in unconditioned(line):
            have.add((k, sha(x)))
    return ['keep entry %s %s is not an unconditioned base sentence' % e for e in sorted(keep - have)]


def check_preserved(base_texts, head_texts):
    bad = []
    for f, prefixes in PRESERVED.items():
        bp, hp = P0.paragraphs(base_texts[f]), P0.paragraphs(head_texts.get(f, ''))
        for pre in prefixes:
            b, h = P0.find(bp, pre), P0.find(hp, pre)
            if len(b) != 1:
                bad.append('%s: base has %d paragraphs opening %r' % (f, len(b), pre[:50]))
            elif len(h) != 1 or b[0] != h[0]:
                bad.append('%s: changed or missing: %r' % (f, pre[:50]))
    for f, toks in REQUIRED.items():
        for t in toks:
            if t not in head_texts.get(f, ''):
                bad.append('%s: missing required text %r' % (f, t[:60]))
    return bad


def check_lines(base_texts, head_texts):
    return ['%s: line count %d != base %d' % (f, head_texts.get(f, '').count('\n'), base_texts[f].count('\n'))
            for f in SCOPE_FILES if head_texts.get(f, '').count('\n') != base_texts[f].count('\n')]


def check_status(base_texts, head_texts):
    bad = []
    for p in SCOPE_FILES + [MAIN]:
        b, h = base_texts.get(p, ''), head_texts.get(p, '')
        for name, fn in P0.STATUS_COUNTS.items():
            if fn(h) < fn(b):
                bad.append('%s: "%s" count %d < base %d' % (p, name, fn(h), fn(b)))
    return bad


def decision_rule(base_texts, head_texts, ledger, disp, sites, mirrors, keep):
    dr = {}
    # DR-1: disposition completeness and consistency with the ledger
    keys = {'%s:%d' % (s['file'], s['line']) for s in sites} | {
        'FULL<-%s:%d' % chapter_id(m) for m in mirrors}
    dkeys = {d['site'] for d in disp['dispositions']}
    units = {s['unit'] for s in ledger['splices']}
    used = {u for d in disp['dispositions'] for u in d.get('units', [])}
    lines_ok = True
    for d in disp['dispositions']:
        for u in d.get('units', []):
            sp = [s for s in ledger['splices'] if s['unit'] == u]
            if not sp:
                lines_ok = False
                continue
            if d['site'].startswith('FULL<-'):
                continue
            f, n = d['site'].rsplit(':', 1)
            line = base_texts[f].split('\n')[int(n) - 1]
            if sp[0]['old'] not in line:
                lines_ok = False
    companion = {s['unit'] for s in ledger['splices'] if s.get('companion_of')}
    dr['DR-1 every in-scope site has one disposition'] = keys == dkeys and len(dkeys) == len(disp['dispositions'])
    dr['DR-1 every edit disposition names ledger units whose old text lies on that site line'] = lines_ok
    dr['DR-1 every ledger unit is used by a disposition or is a declared companion splice'] = (
        units == used | companion)
    # DR-2: CTL-14 at the head, with a keep list that is exactly the base residue not edited
    dr['DR-2 no unconditioned finiteness on in-scope site lines outside the keep list'] = not check_conditioned(
        head_texts, sites, mirrors, keep)
    dr['DR-2 keep list entries are base sentences'] = not check_keep_integrity(base_texts, sites, mirrors, keep)
    # DR-3: diff-based change rows
    for name, (f, toks) in DR3.items():
        added = ' '.join(P0.added_sentences(base_texts.get(f, ''), head_texts.get(f, '')))
        dr['DR-3 ' + name] = all(t in added for t in toks)
    # DR-4: R1 stays conditional (GR:58), preserved statements
    dr['DR-4 GR:58 counting stays conditional on A1 and H-count; preserved statements unchanged'] = not check_preserved(
        base_texts, head_texts)
    return dr


def load_base(root, base):
    paths = sorted(set(P0.git_ls(root, base, 'papers/') + P0.git_ls(root, base, 'book/')))
    return {p: P0.git_show(root, base, p) for p in paths}


def keep_set(ledger):
    return {(k['site'], k['sentence_sha256']) for k in ledger['keep']}


def controls(root, base, base_texts, head_texts, ledger, dry):
    out = {}
    sites, mirrors = load_sites()

    def put(ctl, bad, na=False):
        out[ctl] = {'status': 'N/A' if na else ('FAIL' if bad else 'PASS'), 'detail': bad}
    for ctl, bad in P0.check_frozen(base_texts[MAIN], head_texts[MAIN]).items():
        put(ctl, bad)
    pairs = [(p, base_texts.get(p, ''), head_texts.get(p, '')) for p in sorted(set(base_texts) | set(head_texts))
             if base_texts.get(p) != head_texts.get(p)]
    c7, c8 = P0.check_added(pairs)
    put('CTL-7', c7)
    put('CTL-8', c8)
    bad6 = []
    for p, b, h in pairs:
        new_ids = sorted(set(P0.IDENT.findall(h)) - set(P0.IDENT.findall(b)))
        if new_ids:
            bad6.append('%s: new backticked identifiers %s' % (p, ', '.join(new_ids[:10])))
    if root and not dry:
        changed = subprocess.run(['git', '-C', root, 'diff', '--name-only', base, '--', 'verification'],
                                 capture_output=True, text=True).stdout.split()
        bad6 += [p for p in changed if p.startswith(P0.LEAN_DIRS) or p == P0.REGISTRY]
        reg_b = P0.git_show(root, base, P0.REGISTRY)
        reg_h = open(os.path.join(root, P0.REGISTRY), encoding='utf-8').read()
        if P0.registry_status(reg_b) != P0.registry_status(reg_h):
            bad6.append('registry family dispositions differ from base')
        cen = subprocess.run([sys.executable, '-I', os.path.join(root, 'tools/lean_manuscript_census.py'),
                              '--root', root], capture_output=True, text=True)
        if cen.returncode != 0:
            bad6.append('lean_manuscript_census exit %d' % cen.returncode)
    put('CTL-6', bad6)
    if dry or not root:
        put('CTL-9', ['requires a rebuild of the working tree'], na=True)
    else:
        st = subprocess.run([sys.executable, '-I', os.path.join(root, 'tools/staleness_check.py'), '--root', root],
                            capture_output=True, text=True)
        put('CTL-9', [] if st.returncode == 0 else st.stdout.splitlines()[-3:])
    led = P0.ledger_para(head_texts[MAIN])
    bad10 = [] if led.count('Fourteen items') == 1 else ['"Fourteen items" not present exactly once']
    bad10 += ['ledger item %r occurs %d times' % (i, led.count(i)) for i in P0.ITEMS if led.count(i) != 1]
    put('CTL-10', bad10)
    if dry:
        put('CTL-11', [], na=True)
    elif not pairs:
        put('CTL-11', [])  # no manuscript change yet: vacuous, as in Phase 0
    else:
        put('CTL-11', P0.check_ledger_exact(base_texts, head_texts, ledger))
    put('CTL-12', check_status(base_texts, head_texts))
    put('CTL-13', P0.check_full_parity(base_texts, head_texts))
    put('CTL-14', check_conditioned(head_texts, sites, mirrors, keep_set(ledger)) +
        check_keep_integrity(base_texts, sites, mirrors, keep_set(ledger)))
    put('CTL-15', check_preserved(base_texts, head_texts))
    put('CTL-16', check_lines(base_texts, head_texts))
    return out


def run(root, base, dry):
    ledger = json.load(open(LEDGER, encoding='utf-8'))
    disp = json.load(open(DISPOSITIONS, encoding='utf-8'))
    base_texts = load_base(root, base)
    if any(v is None for v in base_texts.values()):
        return 2, {'error': 'cannot read base %s' % base}
    if dry:
        head_texts = P0.apply_ledger(base_texts, ledger)
    else:
        hp = sorted(glob.glob(os.path.join(root, 'papers', '*.md')) + glob.glob(os.path.join(root, 'book', '*.md')))
        head_texts = {os.path.relpath(p, root): open(p, encoding='utf-8').read() for p in hp}
    out = {'base': base, 'mode': 'dry-run' if dry else 'working-tree'}
    out['controls'] = controls(root, base, base_texts, head_texts, ledger, dry)
    sites, mirrors = load_sites()
    out['decision_rule'] = decision_rule(base_texts, head_texts, ledger, disp, sites, mirrors, keep_set(ledger))
    ok = all(v['status'] != 'FAIL' for v in out['controls'].values())
    return (0 if ok else 1), out


def self_test(root, base):
    """Countercontrols on the real base texts: each mutation must make its control FAIL (or its DR unmet);
    the unmutated dry-run head must pass every control."""
    fails = []
    print('Phase 0 functions:', end=' ')
    if P0.self_test() != 0:
        fails.append('Phase 0 self-test failed')
    ledger = json.load(open(LEDGER, encoding='utf-8'))
    disp = json.load(open(DISPOSITIONS, encoding='utf-8'))
    bt = load_base(root, base)
    head = P0.apply_ledger(bt, ledger)
    sites, mirrors = load_sites()
    keep = keep_set(ledger)

    def status(h, led=ledger, dry=False):
        return controls(None, base, bt, h, led, dry)

    def expect_fail(name, h, ctl, led=ledger):
        st = status(h, led)[ctl]['status']
        if st != 'FAIL':
            fails.append('countercontrol %s: %s is %s, expected FAIL' % (name, ctl, st))

    def mutate(h, f, old, new, count=1):
        h = dict(h)
        if h[f].count(old) < 1:
            fails.append('mutation target missing in %s: %r' % (f, old[:60]))
            return h
        h[f] = h[f].replace(old, new, count)
        return h
    # compliant: the ledger applied exactly
    res = status(head, dry=False)
    for ctl, v in res.items():
        if v['status'] == 'FAIL':
            fails.append('compliant head fails %s: %s' % (ctl, v['detail'][:2]))
    dr = decision_rule(bt, head, ledger, disp, sites, mirrors, keep)
    for k, v in dr.items():
        if not v:
            fails.append('compliant head leaves %s unmet' % k)
    dr0 = decision_rule(bt, bt, ledger, disp, sites, mirrors, keep)
    if dr0['DR-2 no unconditioned finiteness on in-scope site lines outside the keep list']:
        fails.append('DR-2 met at the base (the keep list would excuse the edited sentences)')
    # M1: strip a stated condition from a site that carries it (Substratum:389)
    expect_fail('M1 strip "(finite under A1)" at Substratum:389',
                mutate(head, 'papers/Substratum.md', 'a set (finite under A1) with a deterministic bijection',
                       'a finite set with a deterministic bijection'), 'CTL-14')
    # M2: revert unit S3 at the head
    m2 = mutate(head, 'papers/SM.md', [s for s in ledger['splices'] if s['unit'] == 'S3'][0]['new'],
                [s for s in ledger['splices'] if s['unit'] == 'S3'][0]['old'])
    expect_fail('M2 revert S3', m2, 'CTL-14')
    expect_fail('M2 revert S3', m2, 'CTL-11')
    # M3: GR:58 loses its A1 condition
    expect_fail('M3 GR:58 without "Under A1"', mutate(head, 'papers/GR.md', 'Under A1, restrict the finite total',
                                                      'Restrict the finite total'), 'CTL-15')
    # M4: derived/physical wording added
    expect_fail('M4 "(NR) holds in nature"', mutate(head, 'papers/SM.md', 'is a weaker sufficient condition.',
                                                    'is a weaker sufficient condition. The condition (NR) holds in '
                                                    'nature, so recurrence is derived.'), 'CTL-7')
    # M5: a status word removed in a book mirror
    expect_fail('M5 delete "not adopted" in ch02:76',
                mutate(head, 'book/ch02-substratum.md', 'an open hypothesis, not adopted, and one sufficient',
                       'an open hypothesis, and one sufficient'), 'CTL-12')
    # M6: chapter edit without its FULL mirror
    m6 = dict(head)
    k1 = [s for s in ledger['splices'] if s['unit'] == 'K1-FULL'][0]
    m6[FULL] = m6[FULL].replace(k1['new'], k1['old'], 1)
    expect_fail('M6 K1 applied to the chapter only', m6, 'CTL-13')
    # M7: a new line in a scope file
    expect_fail('M7 inserted line', mutate(head, 'papers/SM.md', 'is a weaker sufficient condition.',
                                           'is a weaker sufficient condition.\n\nNew paragraph.'), 'CTL-16')
    # M8: a ledger whose S1 lacks (NR) leaves DR-3 unmet
    led8 = json.loads(json.dumps(ledger))
    s1 = [s for s in led8['splices'] if s['unit'] == 'S1'][0]
    s1['new'] = s1['new'].replace('the near-return condition (NR) of [Main §2.3]', 'a weaker condition')
    h8 = P0.apply_ledger(bt, led8)
    if decision_rule(bt, h8, led8, disp, sites, mirrors, keep)['DR-3 M4 (NR) propagation, SM:44']:
        fails.append('countercontrol M8: DR-3 SM:44 met without (NR)')
    # M9: a keep entry that is not a base sentence
    led9 = json.loads(json.dumps(ledger))
    led9['keep'].append({'site': 'papers/SM.md:44', 'sentence_sha256': '0' * 64, 'reason': 'x'})
    if not check_keep_integrity(bt, sites, mirrors, keep_set(led9)):
        fails.append('countercontrol M9: forged keep entry accepted')
    # M10: an unconditioned finiteness sentence inserted on a site line (GR:591)
    expect_fail('M10 inserted "The substratum is a finite set."',
                mutate(head, 'papers/GR.md', 'For systems other than the cosmological horizon,',
                       'The substratum is a finite set. For systems other than the cosmological horizon,'), 'CTL-14')
    # M11: a preserved theorem statement changed (Theorem 19 normalizer)
    expect_fail('M11 Theorem 19 prior changed', mutate(head, 'papers/SM.md',
                                                       'and let the hidden prior be the counting measure',
                                                       'and let the hidden prior be invariant'), 'CTL-15')
    print('Phase 2 self-test (11 countercontrols, compliant head, base residue):', 'PASS' if not fails else 'FAIL')
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
    root = os.path.abspath(a.root)
    if a.self_test:
        sys.exit(self_test(root, a.base))
    code, out = run(root, a.base, a.dry_run)
    if 'error' in out:
        print(out['error'])
        sys.exit(code)
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
