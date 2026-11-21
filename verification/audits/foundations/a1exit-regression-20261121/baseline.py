#!/usr/bin/env python3
"""A1-EXIT regression audit (#1468): read-only baseline extractor.

Standard library only; run with `python3 -I -B`. The inventory rule is PREREG.md.

  build                   write snapshot.json from the pinned tree (Git objects at PIN)
  check                   regenerate the snapshot from PIN and compare bytes with snapshot.json
  self-test               controls and countercontrols of the compare mode on in-memory edits
  --compare <commit>      report each baseline entry at <commit> (unchanged / text / value / label
                          changed / removed, with moves), every unaccounted changed or inserted line and
                          every deleted non-entry line; exit 1 if anything changed, 0 if nothing did
  --compare-tree <dir>    the same against a directory holding papers/ and book/
  --json <path>           with --compare*, also write the report to <path> (schema
                          a1exit-regression-compare/1: schema, pin, other, any_change, summary,
                          entries[id,file,line,categories,status[],new_file,new_line,moved,new_text],
                          unaccounted[file,line,kind,flags[],text], deleted[file,line,flags[],text])
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
    'Med': 'papers/Medicine.md', 'Bio': 'papers/Bioinformatics.md', 'Juno': 'papers/Juno.md',
    'appA': 'book/appendix-a-prediction-status.md',
    'appa': 'book/appendix-a-prediction-status.md', 'appB': 'book/appendix-b-derivations.md',
    'appb': 'book/appendix-b-derivations.md', 'appC': 'book/appendix-c-objections.md',
    'appc': 'book/appendix-c-objections.md', 'README': 'book/README.md', 'gloss': 'book/glossary.md', 'FULL': FULL,
}
SITE_RE = re.compile(r'(?<![A-Za-z0-9.])(?:([A-Za-z][A-Za-z0-9]*)?):(\d+)(?:\s*[–-]\s*(\d+))?')

X4_RE = re.compile(r'classical-dimension|N < \\infty|fixed finite carrier')  # ledger_check.py 'X4'
PROSE_CMP_RE = re.compile(r'(\\pm|±|\\sigma|σ|\bPDG\b|CODATA|observed|measured|measurement|experimental)',
                          re.I)  # amendment A1, P1 (the 890-line rule; kept for its count)
PROSE_DEC_RE = re.compile(r'(?<![\w.])\d+\.\d+')  # amendment A1, P1
# amendment A1, P1w (review round 1): widened markers and number forms; this is the selection rule
PROSE_MARK_W = re.compile(r'\\pm|±|\\sigma|σ|\bPDG\b|CODATA|observed|measured|measurement|experimental|'
                          r'observation|match|agree|coincid|%|discrepanc|predict', re.I)
PROSE_NUM_W = re.compile(r'(?<![\w.])\d+\.\d+|10\s*\^\s*\{?\s*[-−]?\d+|(?<![\w./])\d+\s*/\s*\d+(?![\w/.])|'
                         r'\\[dt]?frac\s*\{\s*\d+\s*\}\s*\{\s*\d+\s*\}|\d+(?:\.\d+)?\s*\\?%')
PROSE_MARK_FLAG = PROSE_MARK_W  # also used to flag unaccounted lines in compare mode
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

NEG_TERMS = re.compile(r"\b(not|no|never|cannot|can't|none|neither|nor|without|fails?|failed)\b", re.I)
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


def in_math(t, pos):
    """True when position pos lies inside inline math: an odd number of unescaped $ before it."""
    n, i = 0, 0
    while i < pos:
        if t[i] == '\\':
            i += 2
            continue
        if t[i] == '$':
            n += 1
        i += 1
    return n % 2 == 1


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
        # amendment A1, R3: a hyphen after a letter is part of an identifier (X-48, G-2, spin-0)
        # amendment A1, R5: ... except a subtraction: a Unicode minus (d−1, N−1), or an ASCII hyphen
        # inside inline math (2/(d-1)); the digit is kept, unsigned
        subtraction = False
        if m.group(1) and m.start() > 0 and t[m.start() - 1].isalpha():
            hit = IDENT_TAIL.search(t[max(0, m.start() - 40):m.start()])
            if not (hit and hit.group(1)):
                if m.group(1) == '−' or in_math(t, m.start()):
                    subtraction = True
                else:
                    in_ident = True
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
        sign = '-' if m.group(1) and not subtraction else ''
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
    return [(n['tok'], n.get('paren_unc'), tuple(n.get('unc', ())), n.get('exp10'), n.get('unit'))
            for n in nums]


def strip_numbers(text):
    return ' '.join(NUM_RE.sub(' ', text).split())


def labels_of(text):
    st = [m.group(0).lower() for m in STATUS_TERMS.finditer(text)]
    marks = []
    for m in CLASS_MARK.finditer(text):
        marks.append(m.group(1) if m.group(1) else '%s %s' % (m.group(2), m.group(3)))
    sc = [' '.join(m.group(0).lower().split()) for m in SCOPE_TERMS.finditer(text)]
    neg = [m.group(0).lower() for m in NEG_TERMS.finditer(text)]
    return {'status_terms': st, 'class_marks': marks, 'scope_terms': sc, 'negations': neg}


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
            tuple(lab.get('negations', ())), tuple(tuple(x) for x in lab.get('label_cells', ())))


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
    # amendment A1, P5: M:566 belongs to the X-48 argument (review round 1)
    add('papers/Main.md', 566, 'C-CDO', 'X-48', 'explicit-A1-P5')
    # amendment A1, P2 (was D1): C-CDO also takes every line matching the ledger's extended pattern X4
    for f in sorted(corpus):
        for i, t in enumerate(cache[f]):
            if X4_RE.search(t):
                add(f, i + 1, 'C-CDO', None, 'lexical-X4')
            # amendment A1, P3 (was D2): C-FINL also takes every line matching FINL_RE
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
    # amendment A1, P1: prose comparison lines; added after the mirror closure, so no mirror search
    # and no propagation of this category
    for f in sorted(corpus):
        for i, t in enumerate(cache[f]):
            if not t.startswith('|') and PROSE_MARK_W.search(t) and PROSE_NUM_W.search(t):
                add(f, i + 1, 'C-PROSE', None, 'prose-comparison')
    # amendment A1, P4: every site of the ledger's site map (all rows, FP and FREE included); added
    # after the mirror closure (the map lists its own FULL sites)
    for s in sitemap['sites']:
        row = s['row'] if s['row'] and s['row'] != '-' else None
        add(s['file'], s['line'], 'C-SITEMAP', row, 'sitemap-all')
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
    for cat, _ in [('C-TAB', None)] + CATEGORIES + [('C-PROSE', None), ('C-SITEMAP', None)]:
        counts[cat] = sum(1 for x in entries if cat in x['categories'])
    counts['C-PROSE-narrow-rule'] = sum(
        1 for x in entries if 'C-PROSE' in x['categories'] and PROSE_CMP_RE.search(x['text'])
        and PROSE_DEC_RE.search(x['text']))
    counts['C-PROSE-only'] = sum(1 for x in entries if x['categories'] == ['C-PROSE'])
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
#
# Amendment A1, R1 (review round 1). Lines are paired by content, not by position:
#   stage 0  lines inside difflib `equal` blocks of the same file keep their pairing;
#   stage 1  a baseline entry whose line is outside an equal block takes an unclaimed after-state line
#            with identical text (same file first, nearest line; then any file, so moves across files
#            are paired);
#   stage 2  remaining entries take the most similar unclaimed changed line, greedily by ratio
#            (threshold 0.6 in the same file, 0.8 across files);
# an entry with no partner is `removed`. Every changed or inserted after-state line that is not the
# image of an entry is reported as `unaccounted`, in every file including new ones, and every deleted
# pin line that is not an entry is reported as `deleted`; both are flagged for numbers, comparison
# markers, status/scope/negation terms and table rows.

COMPARE_SCHEMA = 'a1exit-regression-compare/1'
SAME_FILE_RATIO = 0.6
CROSS_FILE_RATIO = 0.8


def line_flags(f, text, new_file=False):
    lab = labels_of(text)
    flags = []
    if parse_numbers(text):
        flags.append('numbers')
    if PROSE_MARK_FLAG.search(text):
        flags.append('marker')
    if lab['status_terms'] or lab['class_marks'] or lab['scope_terms'] or lab['negations']:
        flags.append('terms')
    if text.startswith('|'):
        flags.append('table')
    if new_file:
        flags.append('new-file')
    return flags


def compare(snap, other):
    pin = PIN_CORPUS()
    ent_at = {(e['file'], e['line'] - 1): e for e in snap['entries']}
    files = sorted(set(pin) | set(other))
    old = {f: lines_of(pin[f]) if f in pin else [] for f in files}
    new = {f: lines_of(other[f]) if f in other else [] for f in files}
    eqmap, changed_new, changed_old = {}, {}, {}
    for f in files:
        sm = difflib.SequenceMatcher(None, old[f], new[f], autojunk=False)
        cn, co = set(range(len(new[f]))), set(range(len(old[f])))
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag == 'equal':
                for k in range(i2 - i1):
                    eqmap[(f, i1 + k)] = j1 + k
                    cn.discard(j1 + k)
                    co.discard(i1 + k)
        changed_new[f], changed_old[f] = cn, co
    image, claimed = {}, set()
    for key in sorted(ent_at):                                   # stage 0
        if key in eqmap:
            image[key] = (key[0], eqmap[key])
            claimed.add(image[key])
    by_text = {}
    for f in files:
        for j in sorted(changed_new[f]):
            by_text.setdefault(new[f][j], []).append((f, j))
    for key in sorted(k for k in ent_at if k not in image):     # stage 1
        cands = [c for c in by_text.get(ent_at[key]['text'], []) if c not in claimed]
        if cands:
            same = [c for c in cands if c[0] == key[0]]
            pick = min(same, key=lambda c: (abs(c[1] - key[1]), c[1])) if same else cands[0]
            image[key] = pick
            claimed.add(pick)
    rem = [k for k in sorted(ent_at) if k not in image]          # stage 2
    pool = [(f, j) for f in files for j in sorted(changed_new[f])
            if (f, j) not in claimed and new[f][j].strip()]
    pairs = []
    for k in rem:
        t = ent_at[k]['text']
        for c in pool:
            thr = SAME_FILE_RATIO if c[0] == k[0] else CROSS_FILE_RATIO
            sm = difflib.SequenceMatcher(None, t, new[c[0]][c[1]], autojunk=False)
            if sm.real_quick_ratio() < thr or sm.quick_ratio() < thr:
                continue
            r = sm.ratio()
            if r >= thr:
                pairs.append((-r, 0 if c[0] == k[0] else 1, k, c))
    pairs.sort()
    for _, _, k, c in pairs:
        if k not in image and c not in claimed:
            image[k] = c
            claimed.add(c)
    tidx = {f: tables_index(new[f]) for f in files}
    entries = []
    for key in sorted(ent_at):
        e = ent_at[key]
        r = {'id': e['id'], 'file': e['file'], 'line': e['line'], 'categories': e['categories']}
        if key not in image:
            r['status'] = ['removed']
            entries.append(r)
            continue
        f2, j = image[key]
        ne = describe_line(new[f2], j, tidx[f2])
        r['new_file'], r['new_line'] = f2, j + 1
        r['moved'] = (f2, j + 1) != (e['file'], e['line'])
        if f2 != e['file']:
            # amendment A1, R4: a move across files is a change; flagged when it leaves Main
            r['relocated'] = True
            if e['file'] == 'papers/Main.md':
                r['relocated_from_main'] = True
        if ne['text'] == e['text']:
            r['status'] = ['unchanged']
        else:
            st = []
            if number_key(all_numbers(ne)) != number_key(all_numbers(e)):
                st.append('value changed')
            if label_key(ne) != label_key(e):
                st.append('label changed')
            r['status'] = st or ['text changed']
            r['new_text'] = ne['text']
        entries.append(r)
    unaccounted, deleted = [], []
    pin_texts = {t for f in pin for t in old[f]}
    claimed_texts = {new[f][j] for (f, j) in claimed}
    for f in files:
        for j in sorted(changed_new[f]):
            t = new[f][j]
            if (f, j) in claimed or not t.strip():
                continue
            unaccounted.append({'file': f, 'line': j + 1, 'text': t,
                                'kind': 'identical-to-a-pin-line' if t in pin_texts else 'new-or-changed',
                                'flags': line_flags(f, t, f not in pin)})
        new_texts = {new[f2][j] for f2 in files for j in changed_new[f2]}
        for i in sorted(changed_old[f]):
            t = old[f][i]
            if (f, i) in ent_at or not t.strip() or t in new_texts or t in claimed_texts:
                continue
            deleted.append({'file': f, 'line': i + 1, 'text': t, 'flags': line_flags(f, t)})
    summary = {}
    for r in entries:
        k = '+'.join(r['status'])
        summary[k] = summary.get(k, 0) + 1
    summary['moved'] = sum(1 for r in entries if r.get('moved'))
    summary['relocated'] = sum(1 for r in entries if r.get('relocated'))
    summary['relocated_from_main'] = sum(1 for r in entries if r.get('relocated_from_main'))
    summary['unaccounted'] = len(unaccounted)
    summary['unaccounted_flagged'] = sum(1 for u in unaccounted if u['flags'])
    summary['deleted'] = len(deleted)
    summary['deleted_flagged'] = sum(1 for d in deleted if d['flags'])
    changed = (any(r['status'] != ['unchanged'] for r in entries) or bool(unaccounted) or bool(deleted)
               or summary['relocated'] > 0)
    return {'schema': COMPARE_SCHEMA, 'pin': PIN, 'any_change': changed, 'summary': summary,
            'entries': entries, 'unaccounted': unaccounted, 'deleted': deleted}


_PIN_CORPUS = {}


def PIN_CORPUS():
    if not _PIN_CORPUS:
        _PIN_CORPUS.update(corpus_at_commit(PIN))
    return _PIN_CORPUS


def print_report(res):
    for r in res['entries']:
        if r['status'] != ['unchanged'] or r.get('moved'):
            where = '-' if 'new_line' not in r else '%s:%d' % (r['new_file'], r['new_line'])
            print('%-12s %-28s -> %s  %s' % (r['id'], ', '.join(r['status']) + (' (relocated from Main)' if r.get('relocated_from_main') else
                                             ' (relocated)' if r.get('relocated') else
                                             ' (moved)' if r.get('moved') else ''),
                                             where, ','.join(r['categories'])))
    for u in res['unaccounted']:
        print('UNACCOUNTED  %s:%d  %s [%s]  %s' % (u['file'], u['line'], u['kind'], ','.join(u['flags']),
                                                  u['text'][:100]))
    for d in res['deleted']:
        print('DELETED      %s:%d  [%s]  %s' % (d['file'], d['line'], ','.join(d['flags']), d['text'][:100]))
    print('summary: %s; any change: %s' % (json.dumps(res['summary'], sort_keys=True), res['any_change']))


# --------------------------------------------------------------------------- self-test

def self_test(snap):
    pin = dict(PIN_CORPUS())
    ok = True
    ids = {e['id']: e for e in snap['entries']}
    at = {(e['file'], e['line']): e for e in snap['entries']}

    def run(name, mutate, expect, n_unacc=0, n_del=0, check=None, flags=None, n_reloc=0):
        nonlocal ok
        c = dict(pin)
        mutate(c)
        res = compare(snap, c)
        got = {r['id']: tuple(r['status']) for r in res['entries'] if r['status'] != ['unchanged']}
        good = (got == expect and len(res['unaccounted']) == n_unacc and len(res['deleted']) == n_del
                and res['summary']['relocated'] == n_reloc
                and res['any_change'] == bool(expect or n_unacc or n_del or n_reloc))
        if flags is not None:
            good = good and all(set(flags) <= set(u['flags']) for u in res['unaccounted'])
        if check is not None:
            good = good and check(res)
        print('%-46s %s  (changed %s, unaccounted %d, deleted %d)' % (
            name, 'PASS' if good else 'FAIL', got, len(res['unaccounted']), len(res['deleted'])))
        ok = ok and good
        return res

    def setline(c, f, i, text):
        ls = lines_of(c[f])
        ls[i - 1] = text
        c[f] = '\n'.join(ls)

    def edit_line(c, f, needle, old, newstr):
        ls = lines_of(c[f])
        hits = [i for i, l in enumerate(ls) if needle in l]
        if len(hits) != 1 or old not in ls[hits[0]]:
            raise SystemExit('self-test target not unique: %s %r' % (f, needle))
        ls[hits[0]] = ls[hits[0]].replace(old, newstr, 1)
        c[f] = '\n'.join(ls)

    def moved(res, *wanted):
        m = {r['id'] for r in res['entries'] if r.get('moved') and r['status'] == ['unchanged']}
        return set(wanted) <= m

    appA = 'book/appendix-a-prediction-status.md'
    A = lines_of(pin[appA])
    row = {k: [i for i, l in enumerate(A) if l.startswith('| %s |' % k)][0] + 1 for k in ('3', '4', '16')}
    aid = {k: 'appA:%d' % v for k, v in row.items()}

    run('identity control', lambda c: None, {})
    run('shift control (2 lines inserted above)',
        lambda c: c.__setitem__(appA, 'Inserted paragraph.\n\nAnother.\n' + c[appA]), {}, n_unacc=2,
        check=lambda res: sum(1 for r in res['entries'] if r['file'] == appA and r.get('moved')
                              and r['new_line'] == r['line'] + 3) > 0)
    run('countercontrol: changed value',
        lambda c: edit_line(c, appA, '| 16 |', '2.361', '2.362'), {aid['16']: ('value changed',)})
    run('countercontrol: changed label',
        lambda c: edit_line(c, appA, '| 16 |', '| L | 2(a) |', '| C | 2(a) |'), {aid['16']: ('label changed',)})

    def rm(c):
        ls = lines_of(c[appA])
        del ls[row['3'] - 1]
        c[appA] = '\n'.join(ls)
    run('countercontrol: removed row', rm, {aid['3']: ('removed',)})

    def addrow(c):
        ls = lines_of(c[appA])
        ls.insert(row['3'], '| 3b | synthetic row | 1.00 | C | 0 | none | Ch 6 |')
        c[appA] = '\n'.join(ls)
    run('countercontrol: added row', addrow, {}, n_unacc=1, flags=['table', 'numbers'])

    def swap(c):
        ls = lines_of(c[appA])
        ls[row['3'] - 1], ls[row['4'] - 1] = ls[row['4'] - 1], ls[row['3'] - 1]
        c[appA] = '\n'.join(ls)
    run('countercontrol: row swap (both moved, unchanged)', swap, {},
        check=lambda res: moved(res, aid['3'], aid['4']))

    def move_edit(c):
        ls = lines_of(c[appA])
        r3 = ls[row['3'] - 1]
        ls[row['4'] - 1] = ls[row['4'] - 1].replace('29.57', '29.58', 1)
        ls.insert(row['16'], r3)
        del ls[row['3'] - 1]
        c[appA] = '\n'.join(ls)
    run('countercontrol: move plus adjacent edit', move_edit, {aid['4']: ('value changed',)},
        check=lambda res: moved(res, aid['3']))

    intro = 'papers/Introduction.md'
    t135 = lines_of(pin[intro])[134]
    w = [x for x in re.findall(r'\b[a-z]{5,}\b', t135)
         if not STATUS_TERMS.fullmatch(x) and not SCOPE_TERMS.fullmatch(x) and not NEG_TERMS.fullmatch(x)][0]

    def wording(c):
        setline(c, intro, 135, t135.replace(w, w + 'x', 1))
    run('countercontrol: prose wording only', wording, {'Intro:135': ('text changed',)})
    run('countercontrol: prose scope qualifier',
        lambda c: setline(c, intro, 135, t135 + ' This holds for a fixed finite carrier.'),
        {'Intro:135': ('label changed',)})

    def rewrite_insert(c):
        ls = lines_of(c[intro])
        ls[134] = t135.replace(w, w + 'x', 1)
        ls.insert(135, 'The predicted value is 1.234 MeV against an observed 1.230 MeV.')
        c[intro] = '\n'.join(ls)
    run('countercontrol: insertion inside a rewritten block', rewrite_insert,
        {'Intro:135': ('text changed',)}, n_unacc=1, flags=['numbers', 'marker'])

    mev = [e for e in snap['entries'] if e['kind'] == 'table' and e['file'].startswith('papers/')
           and any(n.get('unit') == 'MeV' for n in all_numbers(e)) and e['text'].count('MeV') >= 1][0]
    run('countercontrol: unit change (MeV -> GeV)',
        lambda c: setline(c, mev['file'], mev['line'], mev['text'].replace('MeV', 'GeV', 1)),
        {mev['id']: ('value changed',)})

    neg = [e for e in snap['entries'] if 'C-CDO' in e['categories'] and ' is ' in e['text']][0]
    run('countercontrol: negation',
        lambda c: setline(c, neg['file'], neg['line'], neg['text'].replace(' is ', ' is not ', 1)),
        {neg['id']: ('label changed',)})

    comp = 'papers/Computation.md'
    run('countercontrol: new paragraph away from entries',
        lambda c: c.__setitem__(comp, 'Synthetic: the mass is predicted at 1.234 MeV against an observed '
                                      '1.230 MeV.\n\n' + c[comp]),
        {}, n_unacc=1, flags=['numbers', 'marker'])
    run('countercontrol: new file',
        lambda c: c.__setitem__('papers/Synthetic.md', '# Synthetic\n\nPredicted 2.5 \\pm 0.1 GeV.\n'),
        {}, n_unacc=2, flags=['new-file'])

    non = None
    for f in sorted(pin):
        if not f.startswith('papers/'):
            continue
        for i, t in enumerate(lines_of(pin[f])):
            if (f, i + 1) in at or t.startswith('|') or not t.strip():
                continue
            m = PROSE_DEC_RE.search(t)
            if m and any(n['tok'] == m.group(0) for n in parse_numbers(t)):
                non = (f, i + 1, t, m)
                break
        if non:
            break
    if non is None:
        print('non-entry value countercontrol target         FAIL  (none found)')
        ok = False
    else:
        nf, nl, nt, nm = non
        d = nt[nm.end() - 1]
        run('countercontrol: value change on a non-entry line',
            lambda c: setline(c, nf, nl, nt[:nm.end() - 1] + str((int(d) + 1) % 10) + nt[nm.end():]),
            {}, n_unacc=1, n_del=1, flags=['numbers'])

    # amendment A1: countercontrols on one prose-comparison line
    pe, pm = None, None
    for e in snap['entries']:
        if not (e['file'].startswith('papers/') and e['categories'] == ['C-PROSE']
                and e['labels']['status_terms']):
            continue
        toks = {n['tok'].lstrip('-') for n in e['numbers']}
        pm = next((m for m in PROSE_DEC_RE.finditer(e['text']) if m.group(0) in toks), None)
        if pm:
            pe = e
            break
    if pe is None:
        print('prose-comparison countercontrol target        FAIL  (none found)')
        ok = False
    else:
        pf, pl, pid, pt = pe['file'], pe['line'], pe['id'], pe['text']
        print('%-46s %s' % ('prose-comparison target', pid))
        dd = pt[pm.end() - 1]
        run('countercontrol: prose-comparison value',
            lambda c: setline(c, pf, pl, pt[:pm.end() - 1] + str((int(dd) + 1) % 10) + pt[pm.end():]),
            {pid: ('value changed',)})
        run('countercontrol: prose-comparison label',
            lambda c: setline(c, pf, pl, pt + ' This estimate is conditional.'), {pid: ('label changed',)})

        def premove(c):
            ls = lines_of(c[pf])
            del ls[pl - 1]
            c[pf] = '\n'.join(ls)
        run('countercontrol: prose-comparison removed', premove, {pid: ('removed',)})

    # amendment A1, R4: a passage moved out of Main into a downstream paper
    mainf, subf = 'papers/Main.md', 'papers/Substratum.md'
    m780 = ids['M:780']

    def move_out(c):
        ls = lines_of(c[mainf])
        assert ls[779] == m780['text']
        del ls[779]
        c[mainf] = '\n'.join(ls)
        c[subf] = c[subf] + '\n' + m780['text'] + '\n'
    run('countercontrol: passage moved out of Main', move_out, {}, n_reloc=1,
        check=lambda res: res['summary']['relocated_from_main'] == 1 and any(
            r['id'] == 'M:780' and r.get('relocated_from_main') and r['new_file'] == subf
            for r in res['entries']))

    # amendment A1, R5: a subtraction keeps its digit
    sub = [e for e in snap['entries'] if 'd−1' in e['text'] and e['kind'] == 'prose'][0]
    run('countercontrol: d−1 -> d−2 is a value change',
        lambda c: setline(c, sub['file'], sub['line'], sub['text'].replace('d−1', 'd−2', 1)),
        {sub['id']: ('value changed',)})
    tok = [n['tok'] for n in parse_numbers('d−1 and N−1 and $2/(d-1)$')]
    good = tok == ['1', '1', '2', '1']
    print('%-46s %s  (%s)' % ('subtraction digits are kept', 'PASS' if good else 'FAIL', tok))
    ok = ok and good
    tok = [n['tok'] for n in parse_numbers('X-48, G-2, spin-0 and 10-20 with -0.5')]
    good = tok == ['10', '20', '-0.5']
    print('%-46s %s  (%s)' % ('identifier digits are not numbers', 'PASS' if good else 'FAIL', tok))
    ok = ok and good
    s2 = build_snapshot()
    good = dump(s2) == dump(snap)
    print('%-46s %s' % ('determinism (two builds identical)', 'PASS' if good else 'FAIL'))
    ok = ok and good
    print('self-test ' + ('PASS' if ok else 'FAIL'))
    return ok


# --------------------------------------------------------------------------- main

def main(argv):
    json_path = None
    if '--json' in argv:
        k = argv.index('--json')
        if k + 1 >= len(argv):
            print(__doc__)
            return 2
        json_path = argv[k + 1]
        argv = argv[:k] + argv[k + 2:]
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
        res = compare(snap, other)
        # amendment A1, R6: a tree is recorded by its basename only, never a local path
        res['other'] = argv[1] if argv[0] == '--compare' else 'tree:' + os.path.basename(
            os.path.normpath(argv[1]))
        print_report(res)
        if json_path:
            with open(json_path, 'w', encoding='utf-8', newline='\n') as fh:
                fh.write(json.dumps(res, ensure_ascii=False, indent=1, sort_keys=True) + '\n')
        return 1 if res['any_change'] else 0
    print(__doc__)
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
