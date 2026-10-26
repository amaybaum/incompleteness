"""Build the statements / kernel sections of the proof inventory (audit step 1).

Run from the worktree root with python3 -I. Reads only; writes JSON to argv[1].
"""
import json, re, os, sys, difflib, glob
from collections import defaultdict

W = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1]
CORE = ['Main', 'GR', 'SM', 'Substratum', 'Structure', 'Methodology', 'Juno']

census = json.load(open(os.path.join(W, '..', 'census.json')))
ledger = json.load(open('verification/coverage/LEDGER.json'))
L = {e['id']: e for e in ledger['entries']}
reg = json.load(open('verification/lean-manuscript-census.json'))
li = json.load(open(os.path.join(W, 'lean_index.json')))
axrec = json.load(open(os.path.join(W, 'axrec.json')))

texts = {p: open('papers/%s.md' % p, encoding='utf-8').read().split('\n') for p in CORE}

# ---------------------------------------------------------------- lean index helpers
by_short = defaultdict(list)
by_full = {}
for d in li['decls']:
    by_short[d['name'].split('.')[-1]].append(d)
    by_full[d['full']] = d
    by_full.setdefault(d['name'], d)
root_imports = set(re.findall(r'^import OIBridge\.(\w+)', open('verification/lean-mathlib/OIBridge.lean').read(), re.M))

# #print axioms index: resolve target relative to namespace
printed = defaultdict(list)
for p in li['prints']:
    t = p['target']
    cands = [t]
    if p['ns']:
        parts = p['ns'].split('.')
        for i in range(len(parts), 0, -1):
            cands.append('.'.join(parts[:i]) + '.' + t)
    for c in cands:
        if c in by_full:
            printed[by_full[c]['full']].append('%s:%d' % (p['path'], p['line']))
            break
    else:
        # fall back on suffix match
        for d in by_short.get(t.split('.')[-1], []):
            if d['full'].endswith(t):
                printed[d['full']].append('%s:%d' % (p['path'], p['line']))


def resolve(ident, module_hint=None, theorem_only=False):
    ident = ident.strip('`')
    out = []
    if ident in by_full:
        out = [by_full[ident]]
    else:
        short = ident.split('.')[-1]
        out = [d for d in by_short.get(short, []) if d['full'].endswith(ident)]
    if module_hint:
        hinted = [d for d in out if d['module'] == module_hint]
        if hinted:
            out = hinted
    if theorem_only:
        out = [d for d in out if d['kind'] in ('theorem', 'lemma')]
    return out


def axioms_for(d):
    rec = axrec.get(d['full']) or axrec.get('OIBridge.' + d['full']) or []
    if not rec:
        for k, v in axrec.items():
            if k.endswith('.' + d['full']) or k == d['name']:
                rec = v
                break
    return rec


def decl_record(d):
    gated = (d['tree'] == 'OIBridge' and d['module'] in root_imports) or d['tree'] == 'lean'
    pr = printed.get(d['full'], [])
    rec = axioms_for(d)
    if rec:
        status = 'recorded: ' + '; '.join('[%s] in %s' % (', '.join(r['axioms']) or 'none', r['source']) for r in rec)
    elif pr:
        status = ('printed in source (%s); output not retained in repo; CI gate tools/lean_axiom_check.py '
                  'fails the build on any axiom outside {propext, Classical.choice, Quot.sound} or sorryAx' % ', '.join(pr[:3]))
        if d['tree'] == 'lean':
            status = 'printed in source (%s); zero-import core file, output not retained in repo' % ', '.join(pr[:3])
    else:
        status = 'no #print axioms found for this declaration; not recorded'
    return {
        'decl': d['full'], 'kind': d['kind'], 'tree': d['tree'],
        'location': '%s:%d' % (d['path'], d['line']), 'module': d['module'],
        'gated_by_root_import': gated, 'print_axioms': status,
    }

# ---------------------------------------------------------------- statement extraction
HEAD = re.compile(r'^\*\*(Theorem|Lemma|Corollary|Proposition|Claim|Definition|Axiom)\b')
ITHEAD = re.compile(r'^\*(Theorem|Lemma|Corollary|Proposition|Rounding Lemma)\b')
REFS = re.compile(r'\[(?:Main|GR|SM|Substratum|Structure|Methodology|Juno|Complexity|Computation)[^\]]{0,40}\]|'
                  r'(?:§|Appendix |Theorem |Lemma |Corollary |Proposition )[A-Z]?[0-9][0-9.]*[a-z]?|'
                  r'companion [a-z ]{0,30}paper|book[ \']s? [A-Za-z ]{0,20}appendix')
KCIT = re.compile(r'\(kernel:([^)]*)\)')
IDENT = re.compile(r'`([A-Za-z_][A-Za-z0-9_\'₀₁₂.]*)`')
PATHC = re.compile(r'`?(OIBridge/[A-Za-z0-9_]+\.lean)`?')

HYP_TOKENS = ["H-slope", "H-Bell", "H-link", "H-cust", "H-scramble", "H-decouple", "H-χ'", "H-spin'",
              "H-BG", "H-det", "H-top", "H-blind", "H-observer-bundle", "H-Y-vertex", "H-balance",
              "H-spectrum", "H-Hawking", "H-frame", "H-state", "H-energy", "H-shell", "H-local-lift",
              "H-orientation", "(EM)", "(T)", "M1-T", "M1-B", "Cond 2", "Condition 2", "Condition 1",
              "mixing hypothesis", "conditional-mixing hypothesis", "Axiom 2", "Axiom 1"]
RANGED = {'C': ['(C1)', '(C2)', '(C3)', '(C4)'], 'A': ['A1', 'A2', 'A3', 'A4', 'A5', 'A6'],
          'E': ['E%d' % i for i in range(1, 8)], 'S': ['S1', 'S2', 'S3', 'S4'],
          'U': ['(U1)', '(U2)', '(U3)'], 'G': ['(G1)', '(G2)', '(G3)']}


def find_hyps(text):
    found = set()
    for t in HYP_TOKENS:
        if re.search(r'(?<![A-Za-z0-9])' + re.escape(t) + r"(?![A-Za-z0-9-])", text):
            found.add(t.replace('Condition 2', 'Cond 2'))
    # ranges like (C1)–(C4), C1–C4, A1–A6, E1–E7, S1–S4, (U1)–(U3)
    for m in re.finditer(r"\(?([CAESUG])([1-9])'?\)?\s*[–-]\s*\(?([CAESUG])?([1-9])'?\)?", text):
        k, a, k2, b = m.group(1), int(m.group(2)), m.group(3), int(m.group(4))
        if k2 and k2 != k:
            continue
        if k in RANGED and a < b <= len(RANGED[k]) + 0:
            for i in range(a, b + 1):
                tok = RANGED[k][i - 1]
                found.add(tok if not tok.startswith('(') else tok)
    for m in re.finditer(r"(?<![A-Za-z0-9-])\(?(C[1-4])\)?(?![0-9'])", text):
        found.add('(%s)' % m.group(1))
    for m in re.finditer(r"(?<![A-Za-z0-9-])(A[1-6]|E[1-7]|S[1-4])(?![0-9A-Za-z])", text):
        found.add(m.group(1))
    for m in re.finditer(r"\((U[1-3]|G[1-3]|EM|T)\)", text):
        found.add('(%s)' % m.group(1))
    if 'H-χ' in text and "H-χ'" not in found:
        found.add("H-χ'")
    if 'H-spin' in text and "H-spin'" not in found:
        found.add("H-spin'")
    return sorted(found)


CUE = re.compile(r"(?:^|(?<=[.*;:] )|(?<=\*))((?:Let|Assume|Suppose|Under|If|Given|Fix|For (?:every|any|each|all)|Model|Decompose|Write|Consider|Within)\b[^.;]{3,400}[.;])")


def hyp_clauses(stmt):
    s = re.sub(r'\$[^$]*\$', lambda m: m.group(0), stmt)
    out = [m.group(1).strip() for m in CUE.finditer(s)]
    for m in re.finditer(r'([^.;]{0,80}\b(?:conditional on|under|assuming|given|provided)\b[^.;]{3,200})', s):
        c = m.group(1).strip()
        if c not in out and len(out) < 6:
            out.append(c)
    return [c[:400] for c in out[:6]]


def span(paper, line, nxt):
    lines = texts[paper]
    end = min(nxt - 1 if nxt else len(lines), line - 1 + 60)
    out = []
    for i in range(line - 1, end):
        if i > line - 1 and lines[i].startswith('#'):
            break
        out.append((i + 1, lines[i]))
    return out


def proof_location(paper, sp, stmt_text):
    inline = None
    for ln, l in sp:
        m = re.search(r'\*(Proof[^*]{0,60}|Conditional proof|Proof sketch)\.?\*', l)
        if m and ln != sp[0][0]:
            inline = ln
            break
        if m and ln == sp[0][0] and l.index(m.group(0)) > len(l) * 0.05:
            inline = ln
            break
    refs = []
    body = ' '.join(l for _, l in sp[:6])
    for m in REFS.finditer(body):
        r = m.group(0)
        if r not in refs:
            refs.append(r)
    if inline:
        loc = 'inline proof at %s:%d' % ('papers/%s.md' % paper, inline)
    else:
        delegated = [r for r in refs if r.startswith('[') or 'companion' in r or 'Appendix' in r or 'appendix' in r]
        loc = 'no inline proof block; ' + ('delegated/cited: ' + '; '.join(delegated[:6]) if delegated else 'see references and kernel citations')
    return {'summary': loc, 'inline_proof_line': inline, 'references_in_statement_and_following_paragraph': refs[:15]}


def kernel_from_span(sp):
    found = []
    for ln, l in sp:
        for m in KCIT.finditer(l):
            grp = m.group(1)
            mods = PATHC.findall(grp)
            hint = os.path.basename(mods[0])[:-5] if len(mods) == 1 else None
            for ident in IDENT.findall(grp):
                if ident.endswith('.lean'):
                    continue
                ds = resolve(ident, hint)
                if ds:
                    for d in ds[:3]:
                        found.append({'cited_as': ident, 'line': ln, 'resolved': '%s:%s' % (d['module'], d['full']),
                                      'kind': d['kind']})
                else:
                    found.append({'cited_as': ident, 'line': ln, 'resolved': None})
    return found


def family_anchors(sp, paper):
    flat = re.sub(r'\s+', ' ', ' '.join(l for _, l in sp))
    fams = []
    for fam in reg['families']:
        for a in fam.get('manuscript', []):
            if a['file'] == 'papers/%s.md' % paper and a['anchor'] in flat:
                fams.append({'family': fam['name'], 'status': fam['status'], 'modules': fam['modules'],
                             'anchor': a['anchor']})
                break
    return fams


def ledger_kernel(e):
    out = []
    for ch in e['checks']:
        if ch['kind'] != 'lean':
            continue
        mod = os.path.basename(ch['path'])[:-5]
        names = ch.get('names') or ([ch['evidence']] if ch.get('evidence') else [])
        for n in names:
            ds = resolve(n, mod)
            if ds:
                d = ds[0]
                out.append({'module_decl': '%s:%s' % (mod, d['full']), 'location': '%s:%d' % (d['path'], d['line']),
                            'kind': d['kind'], 'basis': ch.get('basis')})
            else:
                out.append({'module_decl': '%s:%s' % (mod, n), 'location': None, 'kind': None,
                            'basis': ch.get('basis'), 'unresolved': True})
    return out


# supplementary displayed statements the census regex does not recognise (bold head not at
# line start, lower-case "theorem", italic heads, Markdown headings, inline bold axioms)
SUPP = [
    ('Main', 38, 'Axiom', '1', 'inline bold mid-paragraph', r'\*\*Axiom 1\*\*'),
    ('Main', 38, 'Axiom', '2', 'inline bold mid-paragraph', r'\*\*Axiom 2\*\*'),
    ('Main', 360, 'Theorem', '(Bell ceiling for a screened local completion)', 'inline bold mid-paragraph', r'\*\*Theorem \(Bell ceiling'),
    ('Main', 466, 'Proposition', '(no uniform finite realization)', 'italic head', r'\*Proposition \(no uniform'),
    ('Main', 516, 'Theorem', 'Characterization theorem', 'bold head, lower-case "theorem" (census regex requires **Theorem)', r'\*\*Characterization theorem'),
    ('Main', 538, 'Proposition', '(finite-substratum operational obstruction — classical-dimension form)', 'italic head', r'\*Proposition \(finite-substratum'),
    ('Main', 556, 'Lemma', 'Rounding Lemma (instrument-level, fixed-point dyadic model)', 'italic head', r'\*Rounding Lemma'),
    ('Main', 556, 'Corollary', '(clipping and normalization)', 'italic head mid-paragraph', r'\*Corollary \(clipping'),
    ('Main', 560, 'Corollary', '(single controlled dynamics)', 'italic head', r'\*Corollary \(single'),
    ('Main', 574, 'Lemma', '(adaptive diamond telescoping)', 'italic head', r'\*Lemma \(adaptive'),
    ('Main', 578, 'Corollary', '(finite-test density of deterministic realizations in operational quantum theory)', 'italic head', r'\*Corollary \(finite-test'),
    ('GR', 677, 'Theorem', '(universality of the partition-geometry results)', 'italic head', r'\*Theorem \(universality'),
    ('SM', 1416, 'Proposition', '(determination by (C,T))', 'inline bold mid-paragraph', r'\*\*Proposition\.\*\*'),
    ('SM', 1588, 'Theorem', 'A.1 (Period formula)', 'Markdown heading', r'Theorem A\.1'),
    ('SM', 1596, 'Theorem', 'A.2 (Jordan-Chevalley decomposition)', 'Markdown heading', r'Theorem A\.2'),
    ('SM', 1604, 'Theorem', 'A.3 (q-independence of the Weil-Deligne conductor)', 'Markdown heading', r'Theorem A\.3'),
    ('SM', 1620, 'Theorem', 'A.4 (Additive decomposition over gauge irreps)', 'Markdown heading', r'Theorem A\.4'),
    ('Methodology', 226, 'Axiom', '1', 'list item bold', r'\*\*Axiom 1\.\*\*'),
    ('Methodology', 227, 'Axiom', '2', 'list item bold', r'\*\*Axiom 2\.\*\*'),
    ('Methodology', 235, 'Theorem', 'no-go (§5.5, the one rung that is not a lemma)', 'italic statement, no bold head', r'Given Axiom 1'),
]

# ---------------------------------------------------------------- build
core_rows = [r for r in census if os.path.splitext(os.path.basename(r['paper']))[0] in CORE]
heads_by_paper = defaultdict(list)
for r in core_rows:
    heads_by_paper[os.path.splitext(os.path.basename(r['paper']))[0]].append(r['line'])
for p, ln, *_ in SUPP:
    heads_by_paper[p].append(ln)
for p in heads_by_paper:
    heads_by_paper[p] = sorted(set(heads_by_paper[p]))


def next_head(paper, line):
    for h in heads_by_paper[paper]:
        if h > line:
            return h
    return None


statements = []
for r in core_rows:
    paper = os.path.splitext(os.path.basename(r['paper']))[0]
    e = L[r['id']]
    sp = span(paper, r['line'], next_head(paper, r['line']))
    stmt = r['statement']
    hyps = sorted(set(find_hyps(stmt)) | set(find_hyps(e.get('assumptions', ''))))
    statements.append({
        'id': r['id'], 'source': 'proof_census', 'paper': r['paper'], 'line': r['line'], 'kind': r['kind'],
        'label': r['label'], 'fingerprint': r['fingerprint'],
        'statement_300': stmt[:300],
        'hypotheses_as_stated': hyp_clauses(stmt),
        'named_hypotheses': hyps,
        'ledger': {'id': e['id'], 'line_recorded': e['line'], 'line_moved': e['line'] != r['line'],
                   'area': e['area'], 'level': e['kernel'], 'assumptions': e['assumptions'],
                   'checks': e['checks'], 'delta': e['delta'], 'note': e['note'][:600]},
        'kernel_anchors': {'ledger_lean_checks': ledger_kernel(e), 'manuscript_kernel_citations': kernel_from_span(sp),
                           'census_registry_families': family_anchors(sp, paper)},
        'proof_location': proof_location(paper, sp, stmt),
    })

for paper, ln, kind, label, why, pat in SUPP:
    lines = texts[paper]
    l = lines[ln - 1]
    m = re.search(pat, l)
    assert m, (paper, ln, pat)
    body = l[m.start():]
    # extend to following non-blank lines (statement block)
    j = ln
    while j < len(lines) and lines[j].strip() and not HEAD.match(lines[j]) and not lines[j].startswith('#'):
        body += '\n' + lines[j]
        j += 1
        if len(body) > 4000:
            break
    if lines[ln - 1].startswith('#'):
        # heading: statement is the following paragraph
        k = ln
        while k < len(lines) and not lines[k].strip():
            k += 1
        body = lines[ln - 1].lstrip('# ') + ' ' + lines[k]
    sp = span(paper, ln, next_head(paper, ln))
    statements.append({
        'id': None, 'source': 'supplementary (not recognised by tools/proof_census.py: %s)' % why,
        'paper': 'papers/%s.md' % paper, 'line': ln, 'kind': kind, 'label': label, 'fingerprint': None,
        'statement_300': body[:300], 'hypotheses_as_stated': hyp_clauses(body[:2500]),
        'named_hypotheses': find_hyps(body[:2500]),
        'ledger': None,
        'kernel_anchors': {'ledger_lean_checks': [], 'manuscript_kernel_citations': kernel_from_span(sp),
                           'census_registry_families': family_anchors(sp, paper)},
        'proof_location': proof_location(paper, sp, body),
    })

statements.sort(key=lambda s: (CORE.index(os.path.splitext(os.path.basename(s['paper']))[0]), s['line']))

# ---------------------------------------------------------------- appendix B statements and their paper twins
appb = open('book/appendix-b-derivations.md', encoding='utf-8').read().split('\n')
ABH = re.compile(r'^\*\*(Theorem|Lemma|Corollary|Proposition|Definition)([^*]*)\*\*')
appb_rows = []
norm = lambda s: re.sub(r'\s+', ' ', re.sub(r'^\*\*[^*]*\*\*\s*', '', s)).strip()
cands = [s for s in statements]
for i, l in enumerate(appb):
    m = ABH.match(l)
    if not m:
        continue
    body = l
    j = i + 1
    while j < len(appb) and appb[j].strip():
        body += '\n' + appb[j]
        j += 1
    nb = norm(body)
    best, bestr = None, 0.0
    for s in cands:
        st = s['statement_300'] if s['source'] != 'proof_census' else next(r['statement'] for r in census if r['id'] == s['id'])
        r_ = difflib.SequenceMatcher(None, nb[:1500], norm(st)[:1500]).ratio()
        if r_ > bestr:
            best, bestr = s, r_
    appb_rows.append({'line': i + 1, 'kind': m.group(1), 'label': (m.group(1) + m.group(2)).strip(' .'),
                      'statement_300': body[:300],
                      'closest_paper_statement': {'id': best['id'], 'paper': best['paper'], 'line': best['line'],
                                                  'label': best['label'], 'kind': best['kind'],
                                                  'text_similarity': round(bestr, 3)} if best else None,
                      'named_hypotheses': find_hyps(body)})

# ---------------------------------------------------------------- kernel section
cited = defaultdict(lambda: {'sources': set()})


def cite(ident, src, hint=None):
    for d in resolve(ident, hint, theorem_only=True):
        c = cited[d['full']]
        c['decl'] = d
        c['sources'].add(src)


# manuscripts: every backticked identifier in papers/*.md and book/*.md
ms_files = sorted(glob.glob('papers/*.md')) + sorted(glob.glob('book/*.md'))
unresolved_kernel_cits = []
for f in ms_files:
    s = open(f, encoding='utf-8').read()
    for m in KCIT.finditer(s):
        grp = m.group(1)
        mods = PATHC.findall(grp)
        hint = os.path.basename(mods[0])[:-5] if len(mods) == 1 else None
        for ident in IDENT.findall(grp):
            if ident.endswith('.lean'):
                continue
            if not resolve(ident, hint):
                unresolved_kernel_cits.append({'file': f, 'ident': ident})
            cite(ident, 'manuscript kernel-citation: ' + f, hint)
    for ident in IDENT.findall(s):
        if len(ident) < 4:
            continue
        if resolve(ident, None, theorem_only=True):
            cite(ident, 'manuscript backtick: ' + f)
# registry: anchors and supersessions
unresolved_anchor_idents = []
for fam in reg['families']:
    for a in fam.get('manuscript', []):
        for ident in IDENT.findall(a['anchor']):
            ds = [d for d in resolve(ident) if d['module'] in fam['modules']] or resolve(ident)
            if not ds:
                unresolved_anchor_idents.append({'family': fam['name'], 'anchor': a['anchor'], 'file': a['file']})
            for d in ds:
                if d['kind'] in ('theorem', 'lemma'):
                    c = cited[d['full']]; c['decl'] = d; c['sources'].add('registry anchor: ' + fam['name'][:80])
for old, new in reg['supersessions'].items():
    for ident, role in ((old, 'superseded'), (new, 'successor')):
        ds = resolve(ident, None, theorem_only=True)
        for d in ds:
            c = cited[d['full']]; c['decl'] = d; c['sources'].add('registry supersession (%s)' % role)
# ledger checks
unresolved_ledger = []
for e in ledger['entries']:
    for k in ledger_kernel(e):
        if k.get('unresolved'):
            unresolved_ledger.append({'ledger_id': e['id'], 'module_decl': k['module_decl']})
    for ch in e['checks']:
        if ch['kind'] == 'lean':
            mod = os.path.basename(ch['path'])[:-5]
            for n in (ch.get('names') or [ch.get('evidence')]):
                if n:
                    for d in resolve(n, mod, theorem_only=True)[:1]:
                        c = cited[d['full']]; c['decl'] = d; c['sources'].add('ledger check: ' + e['id'])

kernel = []
for full, c in cited.items():
    rec = decl_record(c['decl'])
    rec['cited_by'] = sorted(c['sources'])
    kernel.append(rec)
kernel.sort(key=lambda r: (r['tree'], r['module'], r['location']))

json.dump({'statements': statements, 'appendix_b_statements': appb_rows, 'kernel': kernel,
           'diag': {'unresolved_kernel_citations': unresolved_kernel_cits,
                    'unresolved_registry_anchor_identifiers': unresolved_anchor_idents,
                    'unresolved_ledger_checks': unresolved_ledger,
                    'root_imports': len(root_imports)}},
          open(OUT, 'w'), ensure_ascii=False, indent=1)
print('statements', len(statements), 'appB', len(appb_rows), 'kernel', len(kernel))
print('unresolved kernel cits', len(unresolved_kernel_cits), unresolved_kernel_cits[:10])
print('unresolved anchors', unresolved_anchor_idents[:10])
print('unresolved ledger', unresolved_ledger[:10])
