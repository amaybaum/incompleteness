#!/usr/bin/env python3
"""A1-EXIT regression audit (#1468): read-only baseline extractor.

Standard library only; run with `python3 -I -B`. The inventory rule is PREREG.md.

  build                   write snapshot.json from the pinned tree (Git objects at PIN)
  check                   regenerate the snapshot from PIN and compare bytes with snapshot.json
  self-test               controls and countercontrols of the compare mode on in-memory edits
  --compare <commit>      report each baseline entry at <commit> (unchanged / text / value / label
                          changed / removed) and new entries
  --compare-tree <dir>    the same against a directory holding papers/ and book/
  --json                  with --compare*, print the report as JSON
"""
import difflib
import hashlib
import json
import os
import re
import subprocess
import sys

PIN = '1c7eedc402eafd2bac654484fa790874a33f444d'
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
LEDGER_DIR = 'verification/audits/foundations/a1exit-ledger-20261120'
SNAPSHOT = os.path.join(HERE, 'snapshot.json')
FULL = 'book/The-Incompleteness-of-Observation-FULL.md'

# --------------------------------------------------------------------------- inventory constants

CATEGORIES = [
    ('C-CDO', ['X-48']),
    ('C-FINL', ['X-47']),
    ('C-CAL', ['X-70', 'X-71', 'X-72']),
    ('C-OBS', ['X-63']),
    ('C-OPEN', ['X-11', 'X-71']),
    ('C-LEDGER', ['X-00', 'X-01', 'X-02', 'X-12', 'X-20', 'X-23', 'X-25', 'X-40', 'X-41', 'X-42',
                  'X-43', 'X-44', 'X-45', 'X-46', 'X-74']),
]

ABBREV_FIXED = {
    'M': 'papers/Main.md', 'SM': 'papers/SM.md', 'GR': 'papers/GR.md',
    'Sub': 'papers/Substratum.md', 'Str': 'papers/Structure.md', 'Meth': 'papers/Methodology.md',
    'Comp': 'papers/Computation.md', 'Cx': 'papers/Complexity.md', 'Intro': 'papers/Introduction.md',
    'Med': 'papers/Medicine.md', 'appA': 'book/appendix-a-prediction-status.md',
    'appa': 'book/appendix-a-prediction-status.md', 'appB': 'book/appendix-b-derivations.md',
    'appb': 'book/appendix-b-derivations.md', 'appC': 'book/appendix-c-objections.md',
    'appc': 'book/appendix-c-objections.md', 'README': 'book/README.md', 'gloss': 'book/glossary.md', 'FULL': FULL,
}
SITE_RE = re.compile(r'(?<![A-Za-z0-9.])(?:([A-Za-z][A-Za-z0-9]*)?):(\d+)(?:\s*[–-]\s*(\d+))?')

X4_RE = re.compile(r'classical-dimension|N < \\infty|fixed finite carrier')  # ledger_check.py 'X4'
FINL_RE = re.compile(r'[Ee]xtrapolat|[NL] *\\to *\\infty|[NL] *→ *∞|finite-[LN]\b|finite lattice')
TABLE_DELIM = re.compile(r'^\|[\s:|-]+\|\s*$')
CLASS_PRED = re.compile(r'Predict|Observ|Match|Empirical|Measure|Deviation|Discrepanc|σ|\\sigma|'
                        r'Residual|Testab|Value|value|Leading')
CLASS_STATUS = re.compile(r'Status|Class|Tier|Emerges|Transports|Layer')
ROLES = [
    ('label', re.compile(r'Class|Status|Tier|Layer|Cat\b|Input|Testab|Emerges|Transports|role')),
    ('match', re.compile(r'Match|match|Deviation|Discrepanc|Residual|σ|\\sigma')),
    ('observed', re.compile(r'Observ|Measure|Data|PDG|Experiment')),
    ('predicted', re.compile(r'Predict|Formula|Value|value|Leading|Quantitative|Required|Estimated')),
]

STATUS_TERMS = re.compile(
    r'\b(theorems?|propositions?|lemmas?|corollar(?:y|ies)|proved|proven|proofs?|derived|derivations?|'
    r'derives?|conditional(?:ly)?|unconditional(?:ly)?|open|hypothes[ie]s|posit(?:ed|s)?|assumed|'
    r'assumptions?|conjectur(?:e|es|al)|retrodictions?|calibrat(?:ion|ions|ed|es)|imported|inputs?|'
    r'fit|fitted|empirical(?:ly)?|numerical(?:ly)?|estimates?|evidence|inconclusive|structural|'
    r'established|not established|exact(?:ly)?|approximate|bounds?|consistent|compatible|'
    r'falsif(?:y|ied|ication|iable)|predict(?:s|ed|ion|ions)?|untested|open problem|'
    r'not derived|unverified|verified|kernel-checked|requires?|depends?)\b', re.I)
CLASS_MARK = re.compile(r'\*\*([SCLRPME])\*\*|\b(Tier|Layer)\s+(\d[a-z()]*)')
SCOPE_TERMS = re.compile(
    r'(\bfinite(?:ly)?\b|\binfinite\b|\bcontinuum\b|\blattices?\b|\btor(?:us|i)\b|\bperiodic\b|'
    r'\bcarriers?\b|\bextrapolat\w*|\bconverg\w*|\bapproximat\w*|L\s*(?:→|\\to|\\rightarrow)\s*\\?infty|'
    r'L\s*→\s*∞|ℤ|\\mathbb\s*\{?Z\}?|N\s*<\s*\\infty|for a fixed finite)', re.I)

UNIT_RE = re.compile(
    r'\s*\$?\s*(?:\\,|\\;|~)?\s*'
    r'(\\%|%|\\sigma|σ|\\text\{\s*(?:GeV|MeV|keV|TeV|eV|meV)\s*\}|\\mathrm\{\s*(?:GeV|MeV|keV|TeV|eV)\s*\}|'
    r'GeV|MeV|keV|TeV|meV|eV|km/s/Mpc|km/s|m/s²|m/s\^2|m/s|Mpc|kpc|ppm|ppb|Gyr|Myr|yr|years?|days?|'
    r'hours?|kHz|MHz|GHz|Hz|nm|fm|cm|mm|kg|K\b|ms\b|ns\b|s\b|m\b|bits?\b|nats?\b|°|deg\b|rad\b|dB\b)')
NUM_RE = re.compile(r'(?<![_\\§\d.])(-|−)?(\d+(?:\.\d+)?)(\(\d+\))?')
IDENT_TAIL = re.compile(r'(\\?)[A-Za-z]+$')
PM_RE = re.compile(r'\s*(?:\\pm|±)\s*(\d+(?:\.\d+)?)')
ASYM_RE = re.compile(r'\s*\^\{\s*\+\s*(\d+(?:\.\d+)?)\s*\}\s*_\{\s*[-−]\s*(\d+(?:\.\d+)?)\s*\}')
POW_RE = re.compile(r'\^\{?\s*([-−]?\d+)\s*\}?')
TIMES_RE = re.compile(r'\s*\)?\s*(?:\\times|×)\s*10\s*\^\{?\s*([-−]?\d+)\s*\}?')
EXCL_PREFIX = re.compile(r'(§\s*|\bCh\.?\s+|\bChapter\s+|\bTheorem\s+|\bLemma\s+|\bProposition\s+|'
                         r'\bTable\s+|\bEq\.?\s+|\bSection\s+|\bStep\s+|\bPart\s+|\bAppendix\s+|'
                         r'\bComment\s+|\bc\.|#)$')
CITE_RE = re.compile(r'\[\d+(?:\s*[,–-]\s*\d+)*\]')


# --------------------------------------------------------------------------- sources

def git(*args):
    return subprocess.run(['git', '-C', ROOT] + list(args), capture_output=True, check=True).stdout


def corpus_at_commit(commit):
    names = git('ls-tree', '--name-only', commit, 'papers/', 'book/').decode().split('\n')
    files = sorted(n for n in names if n.endswith('.md') and n.count('/') == 1)
    return {f: git('show', '%s:%s' % (commit, f)).decode('utf-8') for f in files}


def corpus_at_dir(d):
    out = {}
    for sub in ('papers', 'book'):
        p = os.path.join(d, sub)
        for n in sorted(os.listdir(p)):
            if n.endswith('.md'):
                with open(os.path.join(p, n), encoding='utf-8') as fh:
                    out[sub + '/' + n] = fh.read()
    return out


def corpus_digest(corpus):
    h = hashlib.sha256()
    for f in sorted(corpus):
        h.update(f.encode() + b'\0' + corpus[f].encode('utf-8') + b'\0')
    return h.hexdigest()


def lines_of(text):
    return text.split('\n')


def abbrev_map(corpus):
    m = dict(ABBREV_FIXED)
    for f in corpus:
        g = re.match(r'book/(ch\d\d)-', f)
        if g:
            m[g.group(1)] = f
    return m


def short(f, amap):
    for k in sorted(amap):
        if amap[k] == f and k not in ('appa', 'appb', 'appc'):
            return k
    return f


# --------------------------------------------------------------------------- parsing

def split_cells(line):
    s = line.strip()
    if s.startswith('|'):
        s = s[1:]
    if s.endswith('|'):
        s = s[:-1]
    cells, cur, i = [], '', 0
    while i < len(s):
        c = s[i]
        if c == '\\' and i + 1 < len(s) and s[i + 1] == '|':
            cur += '\\|'
            i += 2
            continue
        if c == '|':
            cells.append(cur.strip())
            cur = ''
        else:
            cur += c
        i += 1
    cells.append(cur.strip())
    return cells


def find_tables(lines):
    """Return list of tables: dict(start, header_line, rows=[line indices], heading)."""
    tabs, i = [], 0
    while i < len(lines):
        if lines[i].startswith('|') and i + 1 < len(lines) and TABLE_DELIM.match(lines[i + 1]):
            j = i + 2
            while j < len(lines) and lines[j].startswith('|'):
                j += 1
            heading = ''
            for k in range(i, -1, -1):
                if lines[k].startswith('#'):
                    heading = lines[k].strip()
                    break
            tabs.append({'start': i, 'rows': list(range(i + 2, j)), 'heading': heading,
                         'columns': split_cells(lines[i])})
            i = j
        else:
            i += 1
    return tabs


def table_class(header_text):
    if CLASS_PRED.search(header_text):
        return 'prediction'
    if CLASS_STATUS.search(header_text):
        return 'status'
    return 'other'


def role_of(col):
    for name, rx in ROLES:
        if rx.search(col):
            return name
    return 'other'


def parse_numbers(text):
    t = CITE_RE.sub(lambda m: ' ' * len(m.group(0)), text)
    out, pos = [], 0
    while True:
        m = NUM_RE.search(t, pos)
        if not m:
            break
        pre = t[max(0, m.start() - 14):m.start()]
        end = m.end()
        it = IDENT_TAIL.search(t[max(0, m.start() - 40):m.start()]) if not m.group(1) else None
        in_ident = bool(it) and not it.group(1)
        if in_ident or EXCL_PREFIX.search(pre) or (m.start() > 0 and t[m.start() - 1] in '-' and
                                                   re.search(r'[A-Za-z]-$', pre)):
            pos = end
            # skip dotted section numbers like 6.4.2
            while end < len(t) and t[end] == '.' and end + 1 < len(t) and t[end + 1].isdigit():
                end += 1
                while end < len(t) and t[end].isdigit():
                    end += 1
            pos = end
            continue
        sign = '-' if m.group(1) else ''
        tok = sign + m.group(2)
        rec = {'tok': tok}
        if m.group(3):
            rec['paren_unc'] = m.group(3)[1:-1]
        dec = len(m.group(2).split('.')[1]) if '.' in m.group(2) else 0
        rec['decimals'] = dec
        pw = POW_RE.match(t, end)
        if m.group(2) == '10' and pw:
            rec['tok'] = sign + '10^' + pw.group(1).replace('−', '-')
            end = pw.end()
        unc = []
        while True:
            pm = PM_RE.match(t, end)
            if not pm:
                break
            unc.append(pm.group(1))
            end = pm.end()
        am = ASYM_RE.match(t, end)
        if am:
            unc.append('+' + am.group(1) + '/-' + am.group(2))
            end = am.end()
        if unc:
            rec['unc'] = unc
        tm = TIMES_RE.match(t, end)
        if tm:
            rec['exp10'] = tm.group(1).replace('−', '-')
            end = tm.end()
        um = UNIT_RE.match(t, end)
        if um:
            u = re.sub(r'\\(?:text|mathrm)\{\s*(\S+?)\s*\}', r'\1', um.group(1))
            rec['unit'] = {'\\%': '%', '\\sigma': 'σ', 'm/s^2': 'm/s²'}.get(u, u)
            end = um.end()
        out.append(rec)
        pos = max(end, m.end())
    return out


def all_numbers(rec):
    if rec['kind'] == 'table':
        return [n for c in rec['cells'] for n in c['numbers']]
    return rec['numbers']


def number_key(nums):
    return [(n['tok'], n.get('paren_unc'), tuple(n.get('unc', ())), n.get('exp10')) for n in nums]


def strip_numbers(text):
    return ' '.join(NUM_RE.sub(' ', text).split())


def labels_of(text):
    st = [m.group(0).lower() for m in STATUS_TERMS.finditer(text)]
    marks = []
    for m in CLASS_MARK.finditer(text):
        marks.append(m.group(1) if m.group(1) else '%s %s' % (m.group(2), m.group(3)))
    sc = [' '.join(m.group(0).lower().split()) for m in SCOPE_TERMS.finditer(text)]
    return {'status_terms': st, 'class_marks': marks, 'scope_terms': sc}


def describe_line(lines, idx, tables_by_row):
    """Extract the record for line index idx (0-based)."""
    text = lines[idx]
    rec = {'text': text}
    tab = tables_by_row.get(idx)
    if tab is not None:
        ordinal, t = tab
        cells = split_cells(text)
        cols = t['columns']
        cl = []
        for k, c in enumerate(cells):
            col = cols[k] if k < len(cols) else ''
            cl.append({'col': col, 'role': role_of(col), 'text': c, 'numbers': parse_numbers(c)})
        rec['kind'] = 'table'
        rec['table'] = {'ordinal': ordinal, 'class': table_class(' | '.join(cols)),
                        'heading': t['heading'], 'columns': cols}
        rec['cells'] = cl
        lab = labels_of(text)
        lab['label_cells'] = [[c['col'], c['text'] if c['role'] == 'label' else strip_numbers(c['text'])]
                              for c in cl if c['role'] in ('label', 'match')]
        rec['labels'] = lab
    else:
        rec['kind'] = 'prose'
        rec['numbers'] = parse_numbers(text)
        rec['labels'] = labels_of(text)
    return rec


def label_key(rec):
    lab = rec['labels']
    return (tuple(lab['status_terms']), tuple(lab['class_marks']), tuple(lab['scope_terms']),
            tuple(tuple(x) for x in lab.get('label_cells', ())))


def tables_index(lines):
    idx = {}
    for o, t in enumerate(find_tables(lines)):
        for r in t['rows']:
            idx[r] = (o, t)
    return idx


# --------------------------------------------------------------------------- ledger inputs

def ledger_inputs():
    """Read the ledger files at PIN (Git objects) and return (sitemap, table rows, blob ids)."""
    blobs = {}
    data = {}
    for n in ('LEDGER.md', 'sitemap.json', 'rows.json'):
        p = LEDGER_DIR + '/' + n
        blobs[p] = git('rev-parse', '%s:%s' % (PIN, p)).decode().strip()
        data[n] = git('show', '%s:%s' % (PIN, p)).decode('utf-8')
    sitemap = json.loads(data['sitemap.json'])
    led = data['LEDGER.md']
    a, b = led.index('<!-- TABLE:BEGIN -->'), led.index('<!-- TABLE:END -->')
    rows = {}
    for line in led[a:b].split('\n'):
        if not line.startswith('| X-'):
            continue
        cells = split_cells(line)
        rows[cells[0]] = {'home': cells[1], 'sites': cells[9]}
    return sitemap, rows, blobs


def parse_site_cell(cell, amap):
    out, prefix = [], None
    for m in SITE_RE.finditer(cell):
        p, a, b = m.group(1), int(m.group(2)), m.group(3)
        if p is None:
            if prefix is None:
                continue
        else:
            if p not in amap:
                if re.match(r'^(S0|OA4|CK\d)$', p):
                    prefix = None
                    continue
                raise SystemExit('unrecognized site prefix %r in ledger cell: %s' % (p, cell[:120]))
            prefix = p
        lo, hi = a, int(b) if b else a
        for n in range(lo, hi + 1):
            out.append((amap[prefix], n))
    return out


# --------------------------------------------------------------------------- mirror search

def mirror_of(f, text, corpus, cache):
    if len(text.strip()) < 40:
        return None
    if f == FULL:
        targets = [g for g in sorted(corpus) if g.startswith('book/') and g not in (FULL, 'book/README.md')]
    else:
        targets = [FULL]
    exact = []
    for g in targets:
        for i, l in enumerate(cache[g]):
            if l == text:
                exact.append((g, i + 1))
    if len(exact) == 1:
        return {'file': exact[0][0], 'line': exact[0][1], 'method': 'exact'}
    best, br = None, 0.0
    n = len(text)
    for g in targets:
        for i, l in enumerate(cache[g]):
            if not l or min(n, len(l)) / max(n, len(l)) < 0.90:
                continue
            sm = difflib.SequenceMatcher(None, text, l, autojunk=False)
            if sm.real_quick_ratio() < 0.90 or sm.quick_ratio() < 0.90:
                continue
            r = sm.ratio()
            if r > br:
                best, br = (g, i + 1), r
    if best and br >= 0.90:
        if exact and len(exact) > 1:
            return {'file': best[0], 'line': best[1], 'method': 'fuzzy:%.2f' % br, 'note': 'several exact'}
        return {'file': best[0], 'line': best[1], 'method': 'fuzzy:%.2f' % br}
    return None


# --------------------------------------------------------------------------- build

def build_snapshot():
    corpus = corpus_at_commit(PIN)
    amap = abbrev_map(corpus)
    cache = {f: lines_of(corpus[f]) for f in corpus}
    tidx = {f: tables_index(cache[f]) for f in corpus}
    sitemap, lrows, blobs = ledger_inputs()
    if sitemap.get('pin') != 'e837e3dbaa605efc867a213f3345cee14c36d8f5':
        raise SystemExit('unexpected sitemap pin')
    sel = {}   # (file, line) -> {'categories': set, 'rows': set, 'via': set}

    def add(f, n, cat, row, via):
        if f not in corpus or n < 1 or n > len(cache[f]):
            raise SystemExit('site out of range: %s:%d' % (f, n))
        e = sel.setdefault((f, n), {'categories': set(), 'rows': set(), 'via': set()})
        e['categories'].add(cat)
        if row:
            e['rows'].add(row)
        e['via'].add(via)

    for f in sorted(corpus):
        for r in sorted(tidx[f]):
            add(f, r + 1, 'C-TAB', None, 'table')
    site_row = {(s['file'], s['line']): s['row'] for s in sitemap['sites']}
    for cat, rows in CATEGORIES:
        for row in rows:
            for s in sitemap['sites']:
                if s['row'] == row:
                    add(s['file'], s['line'], cat, row, 'sitemap')
            cell = lrows[row]
            for part, via in ((cell['home'], 'ledger-home'), (cell['sites'], 'ledger-sites')):
                for f, n in parse_site_cell(part, amap):
                    t = cache[f][n - 1]
                    if not t.strip() or TABLE_DELIM.match(t):
                        continue
                    add(f, n, cat, row, via)
    # deviation D1 (RESULT): C-CDO also takes every line matching the ledger's extended pattern X4
    for f in sorted(corpus):
        for i, t in enumerate(cache[f]):
            if X4_RE.search(t):
                add(f, i + 1, 'C-CDO', None, 'lexical-X4')
            # deviation D2 (RESULT): C-FINL also takes every line matching FINL_RE
            if FINL_RE.search(t):
                add(f, i + 1, 'C-FINL', None, 'lexical-FINL')
    # mirrors of ledger-selected entries
    # (closure: a mirror added here gets its own mirror search; categories and rows propagate to a
    # fixed point)
    while True:
        changed = False
        for (f, n) in sorted(list(sel)):
            e = sel[(f, n)]
            if e['categories'] == {'C-TAB'}:
                continue
            if 'mirror' not in e:
                e['mirror'] = mirror_of(f, cache[f][n - 1], corpus, cache)
                changed = True
            mir = e['mirror']
            if mir and (mir['file'], mir['line']) != (f, n):
                key = (mir['file'], mir['line'])
                before = (frozenset(sel[key]['categories']), frozenset(sel[key]['rows'])) \
                    if key in sel else None
                for cat in sorted(e['categories'] - {'C-TAB'}):
                    add(mir['file'], mir['line'], cat, None, 'mirror')
                sel[key]['rows'] |= e['rows']
                if before != (frozenset(sel[key]['categories']), frozenset(sel[key]['rows'])):
                    changed = True
        if not changed:
            break
    entries = []
    for (f, n) in sorted(sel):
        e = sel[(f, n)]
        rec = {'id': '%s:%d' % (short(f, amap), n), 'file': f, 'line': n,
               'categories': sorted(e['categories']), 'via': sorted(e['via'])}
        rows = set(e['rows'])
        if (f, n) in site_row and site_row[(f, n)]:
            rows.add(site_row[(f, n)])
        rec['ledger_rows'] = sorted(rows)
        if 'mirror' in e:
            rec['mirror'] = e['mirror']
        rec.update(describe_line(cache[f], n - 1, tidx[f]))
        entries.append(rec)
    counts = {}
    for cat, _ in [('C-TAB', None)] + CATEGORIES:
        counts[cat] = sum(1 for x in entries if cat in x['categories'])
    counts['entries'] = len(entries)
    counts['table_rows_by_class'] = {}
    for x in entries:
        if x['kind'] == 'table':
            c = x['table']['class']
            counts['table_rows_by_class'][c] = counts['table_rows_by_class'].get(c, 0) + 1
    counts['tables'] = sum(len(find_tables(cache[f])) for f in corpus)
    counts['numbers'] = sum(len(all_numbers(x)) for x in entries)
    counts['entries_without_mirror_ledger'] = sum(
        1 for x in entries if x['categories'] != ['C-TAB'] and 'mirror' in x and x['mirror'] is None)
    snap = {
        'schema': 'a1exit-regression-baseline/1',
        'pin': PIN,
        'corpus_digest': corpus_digest(corpus),
        'corpus_files': sorted(corpus),
        'ledger_blobs': blobs,
        'counts': counts,
        'entries': entries,
    }
    return snap


def dump(snap):
    """Top-level keys one per line; each entry as one compact JSON line (diffable, small)."""
    def c(v):
        return json.dumps(v, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
    parts = []
    for k in sorted(snap):
        if k == 'entries':
            parts.append(' "entries": [\n' + ',\n'.join('  ' + c(e) for e in snap[k]) + '\n ]')
        else:
            parts.append(' %s: %s' % (c(k), c(snap[k])))
    return '{\n' + ',\n'.join(parts) + '\n}\n'


# --------------------------------------------------------------------------- compare

def line_map(old, new):
    """Map old line index -> new index or None; and the set of unpaired new indices with the
    old indices they are adjacent to."""
    sm = difflib.SequenceMatcher(None, old, new, autojunk=False)
    mp, unpaired = {}, []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal':
            for k in range(i2 - i1):
                mp[i1 + k] = j1 + k
        elif tag == 'replace':
            m = min(i2 - i1, j2 - j1)
            for k in range(m):
                mp[i1 + k] = j1 + k
            for k in range(m, i2 - i1):
                mp[i1 + k] = None
            for k in range(m, j2 - j1):
                unpaired.append((j1 + k, list(range(max(0, i1 - 1), i2 + 1))))
        elif tag == 'delete':
            for k in range(i1, i2):
                mp[k] = None
        elif tag == 'insert':
            for k in range(j1, j2):
                unpaired.append((k, [i1 - 1, i1]))
    return mp, unpaired


def compare(snap, other):
    base_corpus_files = snap['corpus_files']
    by_file = {}
    for e in snap['entries']:
        by_file.setdefault(e['file'], []).append(e)
    # reconstruct pin texts from Git only for files with entries
    report, new = [], []
    pin_cache = {}
    for f in sorted(set(base_corpus_files) | set(other)):
        old = pin_cache[f] = lines_of(PIN_CORPUS()[f]) if f in base_corpus_files else []
        newl = lines_of(other[f]) if f in other else []
        tidx_new = tables_index(newl)
        mp, unpaired = line_map(old, newl) if f in other else ({}, [])
        images = set()
        ent_lines = set()
        for e in by_file.get(f, []):
            i = e['line'] - 1
            ent_lines.add(i)
            j = mp.get(i) if f in other else None
            r = {'id': e['id'], 'file': f, 'line': e['line'], 'categories': e['categories']}
            if j is None:
                r['status'] = ['removed']
                report.append(r)
                continue
            images.add(j)
            ne = describe_line(newl, j, tidx_new)
            r['new_line'] = j + 1
            if ne['text'] == e['text']:
                r['status'] = ['unchanged']
            else:
                st = []
                if number_key(all_numbers(ne)) != number_key(all_numbers(e)):
                    st.append('value changed')
                if label_key(ne) != label_key(e):
                    st.append('label changed')
                if not st:
                    st.append('text changed')
                r['status'] = st
                r['new_text'] = ne['text']
            report.append(r)
        prose_lines = {e['line'] - 1 for e in by_file.get(f, []) if e['kind'] == 'prose'}
        for j in sorted(tidx_new):
            if j not in images:
                new.append({'file': f, 'new_line': j + 1, 'kind': 'table', 'text': newl[j]})
        for j, adj in unpaired:
            if j in tidx_new or not newl[j].strip():
                continue
            if any(a in prose_lines for a in adj):
                new.append({'file': f, 'new_line': j + 1, 'kind': 'prose-adjacent', 'text': newl[j]})
    return report, new


_PIN_CORPUS = {}


def PIN_CORPUS():
    if not _PIN_CORPUS:
        _PIN_CORPUS.update(corpus_at_commit(PIN))
    return _PIN_CORPUS


def summarize(report, new):
    out = {}
    for r in report:
        k = '+'.join(r['status'])
        out[k] = out.get(k, 0) + 1
    return out, len(new)


def print_report(report, new, as_json):
    summ, nnew = summarize(report, new)
    if as_json:
        print(json.dumps({'summary': summ, 'new': new,
                          'changed': [r for r in report if r['status'] != ['unchanged']]},
                         ensure_ascii=False, indent=1, sort_keys=True))
        return
    for r in report:
        if r['status'] != ['unchanged'] or r.get('new_line', r['line']) != r['line']:
            print('%-12s %s -> %s  %s' % (r['id'], ', '.join(r['status']),
                                          r.get('new_line', '-'), ','.join(r['categories'])))
    for n in new:
        print('NEW          %s:%d  %s  %s' % (n['file'], n['new_line'], n['kind'], n['text'][:100]))
    print('summary: %s; new entries: %d' % (json.dumps(summ, sort_keys=True), nnew))


# --------------------------------------------------------------------------- self-test

def self_test(snap):
    pin = dict(PIN_CORPUS())
    ok = True

    def run(name, mutate, expect, expect_new):
        nonlocal ok
        c = dict(pin)
        mutate(c)
        rep, new = compare(snap, c)
        got = {r['id']: tuple(r['status']) for r in rep if r['status'] != ['unchanged']}
        good = got == expect and len(new) == expect_new
        print('%-44s %s  (changed %s, new %d)' % (name, 'PASS' if good else 'FAIL', got, len(new)))
        ok = ok and good
        return rep

    def edit_line(c, f, needle, old, newstr):
        ls = lines_of(c[f])
        hits = [i for i, l in enumerate(ls) if needle in l]
        if len(hits) != 1 or old not in ls[hits[0]]:
            raise SystemExit('self-test target not unique: %s %r' % (f, needle))
        ls[hits[0]] = ls[hits[0]].replace(old, newstr, 1)
        c[f] = '\n'.join(ls)
        return hits[0] + 1

    appA = 'book/appendix-a-prediction-status.md'
    line16 = [i for i, l in enumerate(lines_of(pin[appA])) if l.startswith('| 16 |')][0] + 1
    line3 = [i for i, l in enumerate(lines_of(pin[appA])) if l.startswith('| 3 |')][0] + 1
    id16, id3 = 'appA:%d' % line16, 'appA:%d' % line3

    run('identity control', lambda c: None, {}, 0)
    rep = run('shift control (lines inserted above)',
              lambda c: c.__setitem__(appA, 'Inserted paragraph.\n\nAnother.\n' + c[appA]), {}, 0)
    moved = [r for r in rep if r['file'] == appA and r.get('new_line') != r['line']]
    good = len(moved) > 0 and all(r['new_line'] == r['line'] + 3 for r in moved)
    print('%-44s %s  (%d moved by 3)' % ('shift control moves entries', 'PASS' if good else 'FAIL', len(moved)))
    ok = ok and good
    run('countercontrol: changed value',
        lambda c: edit_line(c, appA, '| 16 |', '2.361', '2.362'), {id16: ('value changed',)}, 0)
    run('countercontrol: changed label',
        lambda c: edit_line(c, appA, '| 16 |', '| L | 2(a) |', '| C | 2(a) |'), {id16: ('label changed',)}, 0)

    def rm(c):
        ls = lines_of(c[appA])
        del ls[line3 - 1]
        c[appA] = '\n'.join(ls)
    run('countercontrol: removed row', rm, {id3: ('removed',)}, 0)

    def addrow(c):
        ls = lines_of(c[appA])
        ls.insert(line3, '| 3b | synthetic row | 1.00 | C | 0 | none | Ch 6 |')
        c[appA] = '\n'.join(ls)
    run('countercontrol: added row', addrow, {}, 1)

    intro = 'papers/Introduction.md'
    ln = 135
    t = lines_of(pin[intro])[ln - 1]
    w = [x for x in re.findall(r'\b[a-z]{5,}\b', t)
         if not STATUS_TERMS.fullmatch(x) and not SCOPE_TERMS.fullmatch(x)][0]

    def wording(c):
        ls = lines_of(c[intro])
        ls[ln - 1] = ls[ln - 1].replace(w, w + 'x', 1)
        c[intro] = '\n'.join(ls)
    run('countercontrol: prose wording only', wording, {'Intro:135': ('text changed',)}, 0)

    def scope(c):
        ls = lines_of(c[intro])
        ls[ln - 1] = ls[ln - 1] + ' This holds for a fixed finite carrier.'
        c[intro] = '\n'.join(ls)
    run('countercontrol: prose scope qualifier', scope, {'Intro:135': ('label changed',)}, 0)
    s2 = build_snapshot()
    good = dump(s2) == dump(snap)
    print('%-44s %s' % ('determinism (two builds identical)', 'PASS' if good else 'FAIL'))
    ok = ok and good
    print('self-test ' + ('PASS' if ok else 'FAIL'))
    return ok


# --------------------------------------------------------------------------- main

def main(argv):
    as_json = '--json' in argv
    argv = [a for a in argv if a != '--json']
    if not argv:
        print(__doc__)
        return 2
    if argv[0] == 'build':
        s = build_snapshot()
        with open(SNAPSHOT, 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(dump(s))
        print('wrote %s: %s' % (os.path.relpath(SNAPSHOT, ROOT), json.dumps(s['counts'], sort_keys=True)))
        return 0
    if argv[0] == 'check':
        s = build_snapshot()
        with open(SNAPSHOT, encoding='utf-8') as fh:
            have = fh.read()
        if dump(s) != have:
            print('check FAIL: regenerated snapshot differs from snapshot.json')
            return 1
        print('check PASS: snapshot.json regenerates byte for byte from %s (sha256 %s)'
              % (PIN, hashlib.sha256(have.encode('utf-8')).hexdigest()))
        return 0
    if argv[0] == 'self-test':
        with open(SNAPSHOT, encoding='utf-8') as fh:
            snap = json.load(fh)
        return 0 if self_test(snap) else 1
    if argv[0] in ('--compare', '--compare-tree') and len(argv) == 2:
        with open(SNAPSHOT, encoding='utf-8') as fh:
            snap = json.load(fh)
        other = corpus_at_commit(argv[1]) if argv[0] == '--compare' else corpus_at_dir(argv[1])
        rep, new = compare(snap, other)
        print_report(rep, new, as_json)
        return 0
    print(__doc__)
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
