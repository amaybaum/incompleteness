#!/usr/bin/env python3
"""A1-EXIT regression comparison (#1468): frozen collection, replay classification and verdict.

Standard library only; run with `python3 -I -B`. The procedure and decision rules are PREREG.md and
amendments/A1-replay.md in this directory. Modes:

  compile --units <U,...> --commit <rev> --out <file>
      Compile the edit lists of the named units from their allowlisted source records at <rev>
      (structural parsing of Markdown Old/New pairs; JSON records read as objects).
  check-edits --edits <file> --units <U,...> --commit <rev>
      Recompile those units at <rev> and require byte-identical agreement with <file>.
  collect --head <H> --out <DIR>
      <DIR> must not exist or be empty. Runs the controls (C0 frozen inputs, C1 baseline check,
      C2 baseline self-test, C3 baseline against itself, C4 this tool's self-test, C6 check-edits of
      the frozen S2 list, C6-DEL compile of the deletion list at <H>), the comparison
      `baseline.py --compare <H> --json <DIR>/compare.json`, and the injected-value countercontrol C5.
      Writes <DIR>/controls.json and <DIR>/edits-del.json.
  verdict --dir <DIR> [--classify <file>]
      Replays the frozen S2 edits and <DIR>/edits-del.json on the pinned corpus, classifies every
      reported change (J / R / U), runs the bad-citation countercontrol C7, and writes
      <DIR>/verdict.json. Exit 0 PASS, 1 FAIL, 3 PENDING, 4 VOID.
  self-test
      Controls of this tool on synthetic data built from the pinned corpus (no after-state is read).
  digests
      Print the frozen digests (the content of FROZEN.json).

Schemas (JSON, UTF-8):
  edits      a1exit-compare-edits/2: {"schema", "units", "commit", "edits": [{"key", "unit", "pr", "id",
             "seq", "kind" ("replace" | "replace-each" | "resolve"), "targets": [{"file", "chapter",
             "count"}], "old", "new", "amends", "rows", "source_path", "method"}]}
  classify   a1exit-compare-classify/2: {"schema", "head", "items": {<item key>: {"class": "R",
             "reason", "resolution": null | {"outcome": "justified" | "unjustified", "review": <URL of
             a recorded review comment>, "reviewer": <login>, "author": <login>}}}}
  controls   a1exit-compare-controls/2: {"schema", "head", "out_was_fresh", "controls": {<name>:
             {"exit", "pass"}}, "injection": {...}}
  verdict    a1exit-compare-verdict/2: {"schema", "head", "verdict", "counts", "items", "controls",
             "countercontrols", "inputs_sha256", "text"}
"""
import difflib
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
RECORD = os.path.dirname(HERE)
ROOT = os.path.abspath(os.path.join(RECORD, '..', '..', '..', '..'))
sys.path.insert(0, RECORD)
import baseline as B  # noqa: E402

FULL = B.FULL
SOURCE_COMMIT = '7f28886f4cc96fbfa7407af1fdc37de2f0e562e5'   # main with S2-A..S2-E landed
LEDGER_ROWS = 'verification/audits/foundations/a1exit-ledger-20261120/rows.json'
LEDGER_COMMIT = SOURCE_COMMIT                                  # the ledger state J9 reads (frozen)
S2_EDITS = os.path.join(HERE, 'edits', 'S2.json')
M = 'verification/audits/manuscript/'
UNITS = {
    'S2-A': (1470, [M + 'a1exit-s2a-20261121/checks/s2a_edits.json']),
    'S2-B': (1473, [M + 'a1exit-s2b-20261121/PREREG.md', M + 'a1exit-s2b-20261121/amendments/A1-round1.md',
                    M + 'a1exit-s2b-20261121/amendments/A2-return-form.md',
                    M + 'a1exit-s2b-20261121/amendments/A3-cptp-register.md']),
    'S2-C': (1474, [M + 'a1exit-s2c-20261121/PREREG.md', M + 'a1exit-s2c-20261121/amendments/A1.md',
                    M + 'a1exit-s2c-20261121/RESULT.md']),
    'S2-D': (1472, [M + 'a1exit-s2d-20261121/PREREG.md', M + 'a1exit-s2d-20261121/amendments/A1.md']),
    'S2-E': (1475, [M + 'a1exit-s2e-20261121/checks/s2e_edits.json',
                    M + 'a1exit-s2e-20261121/checks/s2e_amend1.json']),
    'DEL': (None, ['verification/audits/foundations/a1exit-deletion-20261121/edits.json']),
}
UNIT_ORDER = ['S2-A', 'S2-B', 'S2-C', 'S2-D', 'S2-E', 'DEL']   # landing order; DEL last
SCI_CATEGORIES = {'C-TAB', 'C-PROSE', 'C-FINL', 'C-CDO', 'C-CAL', 'C-OBS', 'C-OPEN'}
OPEN_TERMS = re.compile(r'\b(open|conditional(?:ly)?|hypothes[ie]s|assumed|posit(?:ed)?|not established|'
                        r'not derived|conjectur\w*|unverified)\b', re.I)
FINITE_TERMS = re.compile(r'\bfinite\b', re.I)
POW10 = re.compile(r'10\s*\^\s*\{?\s*[-−]?\d+|\\times\s*10|×\s*10')
REVIEW_URL = re.compile(r'^https://github\.com/amaybaum/incompleteness/(?:pull|issues)/\d+'
                        r'#(?:issuecomment-\d+|pullrequestreview-\d+|discussion_r\d+)$')


def norm(s):
    return ' '.join(s.split())


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha256_file(p):
    with open(p, 'rb') as fh:
        return sha256_bytes(fh.read())


# --------------------------------------------------------------------------- compile (parsers)

def amap_full():
    m = B.abbrev_map(B.PIN_CORPUS())
    m['Main'] = 'papers/Main.md'
    return m


SITE_TOK = re.compile(r'`([\w./-]+\.md):(\d+)`|(?<![\w`/])([A-Za-z][A-Za-z0-9]*):(\d+)|(?<=[ ,(]):(\d+)')
ROWS_RE = re.compile(r'X-\d\d')


def sites_in(text, amap):
    """[(file, line)] from backticked paths, abbreviations and bare ':n' continuations."""
    out, prefix = [], None
    for m in SITE_TOK.finditer(text):
        if m.group(1):
            prefix = m.group(1)
            out.append((m.group(1), int(m.group(2))))
        elif m.group(3):
            if m.group(3) in amap:
                prefix = amap[m.group(3)]
                out.append((prefix, int(m.group(4))))
            else:
                prefix = None
        elif m.group(5) and prefix:
            out.append((prefix, int(m.group(5))))
    return out


def fenced_after(lines, i):
    """The content of the first fenced block starting at or after line i; (text, index after)."""
    j = i
    while j < len(lines) and not lines[j].startswith('```'):
        j += 1
    k = j + 1
    while k < len(lines) and not lines[k].startswith('```'):
        k += 1
    return '\n'.join(lines[j + 1:k]), k + 1


def parse_md_heading(text, amap):
    """### <ID> — ... blocks with Site(s): lines (or a backticked site in the heading), and
    Old / New fenced blocks, or 'Old and new strings: identical to <ID>'."""
    lines = text.split('\n')
    recs, i, in_fence = [], 0, False
    starts = []
    for n, l in enumerate(lines):
        if l.startswith('```'):
            in_fence = not in_fence
        elif not in_fence and l.startswith('### '):
            starts.append(n)
    starts.append(len(lines))
    by_id = {}
    for a, b in zip(starts, starts[1:]):
        head = lines[a][4:]
        rid = head.split(' — ')[0].strip().strip('`')
        block = lines[a + 1:b]
        sites = [(m.group(1), int(m.group(2))) for m in re.finditer(r'`([\w./-]+\.md):(\d+)`', head)]
        rows = ROWS_RE.findall(head)
        old = new = None
        k = 0
        while k < len(block):
            l = block[k]
            if re.match(r'^Sites?\b', l):
                sites += sites_in(l, amap)
            m = re.match(r'^Old and new strings: identical to (\S+?)[ .(]', l + ' ')
            if m and m.group(1) in by_id:
                old, new = by_id[m.group(1)]['old'], by_id[m.group(1)]['new']
            if re.match(r'^Old\b', l) and old is None:
                old, k = fenced_after(block, k + 1)
                continue
            if re.match(r'^New\b', l) and new is None:
                new, k = fenced_after(block, k + 1)
                continue
            if l.startswith('Finding') or l.startswith('Sites'):
                rows += ROWS_RE.findall(l) if l.startswith('Sites') else []
            k += 1
        if old is None or new is None or not sites:
            continue
        r = {'id': rid, 'sites': sites, 'old': old, 'new': new, 'rows': sorted(set(rows)), 'method': 'md-heading'}
        by_id[rid] = r
        recs.append(r)
    return recs


def strip_ticks(c):
    c = c.strip()
    if len(c) >= 2 and c[0] == '`' and c[-1] == '`':
        return c[1:-1]
    return c


def parse_md_table(text, amap):
    """Tables whose header has 'Old' and 'New' columns: one record per row."""
    lines = text.split('\n')
    recs = []
    i = 0
    while i < len(lines):
        if lines[i].startswith('|') and i + 1 < len(lines) and B.TABLE_DELIM.match(lines[i + 1]):
            cols = B.split_cells(lines[i])
            io = next((k for k, c in enumerate(cols) if c.startswith('Old')), None)
            inew = next((k for k, c in enumerate(cols) if c.startswith('New')), None)
            isite = next((k for k, c in enumerate(cols) if c.startswith('Site')), None)
            irow = next((k for k, c in enumerate(cols) if c.startswith('Row')), None)
            j = i + 2
            while j < len(lines) and lines[j].startswith('|'):
                if io is not None and inew is not None and isite is not None:
                    cells = B.split_cells(lines[j])
                    if len(cells) == len(cols):
                        rows = ROWS_RE.findall(cells[irow]) if irow is not None else []
                        recs.append({'id': strip_ticks(cells[0]), 'sites': sites_in(cells[isite], amap),
                                     'old': strip_ticks(cells[io]).replace('\\|', '|'),
                                     'new': strip_ticks(cells[inew]).replace('\\|', '|'),
                                     'rows': sorted(set(rows)), 'method': 'md-table'})
                j += 1
            i = j
        else:
            i += 1
    return recs


def quoted(lines, k, tag):
    """'- old: "..."' possibly wrapped over indented lines; returns (text, next index)."""
    s = lines[k].split(tag, 1)[1].strip()
    k += 1
    while k < len(lines) and lines[k].startswith('  ') and not lines[k].lstrip().startswith('- '):
        s += ' ' + lines[k].strip()
        k += 1
    if s.startswith('"') and s.endswith('"'):
        s = s[1:-1]
    return s, k


def parse_md_bullet(text, amap):
    """**<ID> (...)** paragraphs with '- old: "..."' / '- new: "..."' bullets; sites in the paragraph.
    A sentence 'The splices are applied in the order A, B, C.' fixes the order."""
    lines = text.split('\n')
    recs, k = [], 0
    while k < len(lines):
        m = re.match(r'^\*\*([A-Z][\w.-]*-\d+)\b', lines[k])
        if not m:
            k += 1
            continue
        rid, para, k = m.group(1), [lines[k]], k + 1
        while k < len(lines) and not lines[k].startswith('- old:'):
            para.append(lines[k])
            k += 1
        if k >= len(lines):
            break
        old, k = quoted(lines, k, '- old:')
        if k < len(lines) and lines[k].startswith('- new:'):
            new, k = quoted(lines, k, '- new:')
            ptxt = ' '.join(para)
            recs.append({'id': rid, 'sites': sites_in(ptxt, amap), 'old': old, 'new': new,
                         'rows': sorted(set(ROWS_RE.findall(ptxt))), 'method': 'md-bullet'})
    om = re.search(r'applied in the order ([A-Z0-9, -]+?)\.', text)
    if om:
        order = [x.strip() for x in om.group(1).split(',')]
        recs.sort(key=lambda r: order.index(r['id']) if r['id'] in order else len(order))
    return recs


def parse_md_resolved(text, amap):
    """'Resolved line `file:n`, in full:' followed by a '> ' line: the line as resolved at a catch-up."""
    lines = text.split('\n')
    recs = []
    for k, l in enumerate(lines):
        m = re.match(r'^Resolved line `([\w./-]+\.md):(\d+)`, in full:', l)
        if not m:
            continue
        j = k + 1
        while j < len(lines) and not lines[j].startswith('> '):
            j += 1
        recs.append({'id': 'resolved-%s:%s' % (m.group(1), m.group(2)), 'sites': [(m.group(1), int(m.group(2)))],
                     'old': None, 'new': lines[j][2:], 'rows': [], 'method': 'md-resolved', 'kind': 'resolve'})
    return recs


def chapter_spans(full_text, corpus):
    """[(start, end, chapter file)] of FULL by each book file's first heading line."""
    fl = full_text.split('\n')
    pos = []
    for f in sorted(corpus):
        if not f.startswith('book/') or f in (FULL, 'book/README.md'):
            continue
        h = next((l for l in corpus[f].split('\n') if l.startswith('#')), None)
        if h is None:
            continue
        idx = [i for i, l in enumerate(fl) if l == h]
        if len(idx) == 1:
            pos.append((idx[0], f))
    pos.sort()
    return [(s, pos[n + 1][0] if n + 1 < len(pos) else len(fl), f) for n, (s, f) in enumerate(pos)]


def chapter_of_full_line(line):
    pin = B.PIN_CORPUS()
    for s, e, f in chapter_spans(pin[FULL], pin):
        if s < line <= e:
            return f
    return None


def targets_for(sites, multi):
    """Group sites into targets, one per file (and FULL chapter); a FULL target carries the chapter whose
    FULL span contains its stated line. count = number of listed sites in that file when the record is a
    multi-site splice (md-bullet), else 1 (the records state each old string is unique in its file)."""
    out = {}
    for f, ln in sites:
        ch = chapter_of_full_line(ln) if f == FULL else None
        key = (f, ch)
        out[key] = out.get(key, 0) + 1 if multi else 1
    return [{'file': f, 'chapter': ch, 'count': n} for (f, ch), n in sorted(out.items(), key=lambda x: (x[0][0], x[0][1] or ''))]


def compile_unit(unit, commit):
    pr, paths = UNITS[unit]
    amap = amap_full()
    recs = []
    for p in paths:
        src = B.git('show', '%s:%s' % (commit, p)).decode('utf-8')
        if p.endswith('.json'):
            data = json.loads(src)
            objs = data['edits'] if isinstance(data, dict) else data
            for o in objs:
                sites = [(o['file'], int(o.get('line') or 0))]
                if unit == 'DEL' and o.get('site'):
                    sf, sl = o['site'].rsplit(':', 1)
                    sites = [(sf, int(sl))]
                mir = o.get('mirror')
                if isinstance(mir, list):
                    sites.append((mir[0], int(mir[1])))
                if o.get('full_mirror'):
                    sites.append((FULL, None))
                rows = ROWS_RE.findall(str(o.get('row') or ''))
                recs.append({'id': o['id'], 'sites': sites, 'old': o['old'], 'new': o['new'],
                             'amends': o.get('amends'), 'rows': sorted(set(rows)), 'method': 'json',
                             'source_path': p, 'chapter_hint': o['file'] if o.get('full_mirror') else None})
        else:
            got = parse_md_heading(src, amap) + parse_md_table(src, amap) + parse_md_bullet(src, amap)
            got += parse_md_resolved(src, amap)
            for r in got:
                r['source_path'] = p
            recs += got
    edits = []
    for n, r in enumerate(recs):
        tg = []
        for t in targets_for([(f, ln) for f, ln in r['sites'] if ln is not None], r['method'] == 'md-bullet'):
            tg.append(t)
        if any(f == FULL and ln is None for f, ln in r['sites']):
            tg.append({'file': FULL, 'chapter': r.get('chapter_hint'), 'count': 1})
        kind = r.get('kind') or ('replace-each' if any(t['count'] > 1 for t in tg) else 'replace')
        edits.append({'key': '%s:%s' % (unit, r['id']), 'unit': unit, 'pr': pr, 'id': r['id'],
                      'seq': UNIT_ORDER.index(unit) * 10000 + n, 'kind': kind, 'targets': tg,
                      'old': r['old'], 'new': r['new'], 'amends': r.get('amends'), 'rows': r['rows'],
                      'source_path': r['source_path'], 'method': r['method']})
    return edits


def compile_units(units, commit):
    edits = []
    for u in units:
        edits += compile_unit(u, commit)
    return {'schema': 'a1exit-compare-edits/2', 'units': units, 'commit': commit, 'edits': edits}


def dump_json(obj):
    return json.dumps(obj, ensure_ascii=False, indent=1, sort_keys=True) + '\n'


def check_edits(path, units, commit):
    with open(path, encoding='utf-8') as fh:
        have = fh.read()
    try:
        compiled = compile_units(units, commit)
    except subprocess.CalledProcessError:
        print('check-edits: FAIL (a source record of %s is missing at %s)' % (','.join(units), commit[:8]))
        return 1
    if not compiled['edits']:
        print('check-edits: FAIL (no edits compiled for %s at %s)' % (','.join(units), commit[:8]))
        return 1
    want = dump_json(compiled)
    bad = []
    for e in json.loads(want)['edits']:
        if e['old'] is None and e['kind'] != 'resolve' or not e['targets']:
            bad.append(e['key'])
    ok = have == want and not bad
    print('check-edits: %s (%d edits; %s)' % ('PASS' if ok else 'FAIL', len(json.loads(want)['edits']),
                                              'identical to recompilation at %s' % commit[:8] if have == want
                                              else 'differs from recompilation'))
    for k in bad:
        print('  incomplete edit record: %s' % k)
    return 0 if ok else 1


# --------------------------------------------------------------------------- replay

def ws_pattern(s):
    return re.compile(r'\s+'.join(re.escape(t) for t in s.split()))


def replay(corpus, edits):
    """Apply edits in seq order; returns (corpus', log)."""
    c = dict(corpus)
    log = []
    for e in sorted(edits, key=lambda x: x['seq']):
        if e['kind'] == 'resolve':
            t = e['targets'][0]
            ls = c.get(t['file'], '').split('\n')
            best, br = None, 0.0
            for i, l in enumerate(ls):
                r = difflib.SequenceMatcher(None, norm(l), norm(e['new']), autojunk=False).ratio()
                if r > br:
                    best, br = i, r
            if best is not None and br >= 0.5:
                ls[best] = e['new']
                c[t['file']] = '\n'.join(ls)
                log.append((e['key'], 'applied'))
            else:
                log.append((e['key'], 'unapplied: no line to resolve'))
            continue
        if not e['old'] or not norm(e['old']):
            log.append((e['key'], 'unapplied: empty old string'))
            continue
        pat = ws_pattern(e['old'])
        status = 'applied'
        for t in e['targets']:
            text = c.get(t['file'])
            if text is None:
                status = 'unapplied: no file %s' % t['file']
                continue
            a, b = 0, len(text)
            if t['file'] == FULL:
                if not t.get('chapter'):
                    status = 'unapplied: FULL target without chapter'
                    continue
                spans = {f: (s, en) for s, en, f in chapter_spans(text, c)}
                if t['chapter'] not in spans:
                    status = 'unapplied: chapter span not found'
                    continue
                s, en = spans[t['chapter']]
                fl = text.split('\n')
                a = len('\n'.join(fl[:s])) + (1 if s else 0)
                b = len('\n'.join(fl[:en]))
            region = text[a:b]
            hits = list(pat.finditer(region))
            # replace: exactly one occurrence; replace-each: between 1 and the number of listed sites
            # (an earlier splice of the same record set may already have rewritten a listed site)
            okn = len(hits) == 1 if e['kind'] == 'replace' else 1 <= len(hits) <= t['count']
            if not okn:
                status = 'unapplied: %d occurrence(s) of old in %s, expected %d' % (len(hits), t['file'], t['count'])
                continue
            region = pat.sub(lambda m: e['new'], region)
            c[t['file']] = text[:a] + region + text[b:]
        log.append((e['key'], status))
    return c, log


# --------------------------------------------------------------------------- classification

def load_snapshot():
    with open(os.path.join(RECORD, 'snapshot.json'), encoding='utf-8') as fh:
        return json.load(fh)


def load_rows():
    raw = B.git('show', '%s:%s' % (LEDGER_COMMIT, LEDGER_ROWS))
    return {r['id']: r for r in json.loads(raw.decode('utf-8'))['rows']}, sha256_bytes(raw)


def residue(r_corpus, h_corpus):
    """Per file: H line indices and R line indices outside equal blocks of the normalized diff;
    and the R lines with no H counterpart."""
    res_h, res_r_only = {}, {}
    for f in sorted(set(r_corpus) | set(h_corpus)):
        a = [norm(x) for x in r_corpus.get(f, '').split('\n')] if f in r_corpus else []
        b = [norm(x) for x in h_corpus.get(f, '').split('\n')] if f in h_corpus else []
        sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
        rh, ro = set(), []
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag == 'equal':
                continue
            rh |= set(range(j1, j2))
            extra = (i2 - i1) - (j2 - j1)
            if extra > 0:
                ro += [i for i in range(i2 - extra, i2) if a[i]]
        res_h[f], res_r_only[f] = rh, ro
    return res_h, res_r_only


def sci_text(t):
    if not t:
        return False
    if B.PROSE_DEC_RE.search(t) or POW10.search(t) or B.PROSE_MARK_W.search(t):
        return True
    return any(n.get('unit') for n in B.parse_numbers(t))


def items_of(compare, snap_by_id):
    out = {}
    for r in compare['entries']:
        e = snap_by_id[r['id']]
        st = r['status']
        if st == ['unchanged'] and not r.get('relocated'):
            continue
        kinds = [] if st == ['unchanged'] else list(st)
        if r.get('relocated'):
            kinds.append('relocated_from_main' if r.get('relocated_from_main') else 'relocated')
        after = r.get('new_text', e['text']) if 'new_line' in r else None
        out[r['id']] = {'kinds': kinds, 'file': e['file'], 'new_file': r.get('new_file'), 'new_line': r.get('new_line'),
                        'before': e['text'], 'after': after, 'categories': e['categories'],
                        'ledger_rows': e['ledger_rows'],
                        'table_class': e['table']['class'] if e['kind'] == 'table' else None}
    for u in compare['unaccounted']:
        out['U:%s:%d' % (u['file'], u['line'])] = {'kinds': ['unaccounted'], 'file': u['file'], 'new_file': u['file'],
                                                   'new_line': u['line'], 'before': None, 'after': u['text'],
                                                   'flags': u['flags'], 'ledger_rows': []}
    for d in compare['deleted']:
        out['D:%s:%d' % (d['file'], d['line'])] = {'kinds': ['deleted'], 'file': d['file'], 'before': d['text'],
                                                   'after': None, 'flags': d['flags'], 'ledger_rows': []}
    return out


def sci_flag(item):
    if 'value changed' in item['kinds']:
        return True
    cats = set(item.get('categories') or [])
    if cats & SCI_CATEGORIES and not (cats == {'C-TAB'} and item.get('table_class') == 'other'):
        return True
    return sci_text(item.get('before')) or sci_text(item.get('after'))


def j9(item, rows):
    """For a label change: every one of the entry's own ledger rows is checked against its accepted
    disposition. Returns (ok, notes)."""
    notes = []
    before, after = item['before'] or '', item['after'] or ''
    ob = {m.group(0).lower() for m in OPEN_TERMS.finditer(before)}
    oa = {m.group(0).lower() for m in OPEN_TERMS.finditer(after)}
    promoted = bool(ob - oa)
    for row in item.get('ledger_rows') or []:
        r = rows.get(row)
        if r is None:
            continue
        d = r['disposition']
        if d == 'F':
            if len(FINITE_TERMS.findall(after)) < len(FINITE_TERMS.findall(before)):
                notes.append('%s (F): a finite term of the baseline line is lost' % row)
            if promoted:
                notes.append('%s (F): an open/conditional term is lost' % row)
        elif d == 'O':
            if not oa:
                notes.append('%s (O): no open/conditional/hypothesis term in the after text' % row)
        elif d == 'J':
            if promoted:
                notes.append('%s (J): an open/conditional term is lost' % row)
    return not notes, notes


def resolution_ok(res):
    return (isinstance(res, dict) and res.get('outcome') in ('justified', 'unjustified')
            and bool(REVIEW_URL.match(res.get('review') or '')) and res.get('reviewer')
            and res.get('author') and res['reviewer'] != res['author'])


def classify(snap, h_corpus, r_corpus, compare_h, compare_r, cls, rows):
    by_id = {e['id']: e for e in snap['entries']}
    items_h = items_of(compare_h, by_id)
    items_r = items_of(compare_r, by_id)
    res_h, res_r_only = residue(r_corpus, h_corpus)
    r_deleted = {(i['file'], norm(i['before'])) for k, i in items_r.items() if k.startswith('D:')}
    covered_h = set()
    out = {}
    for key, it in sorted(items_h.items()):
        notes, cand = [], False
        if it.get('new_line') is not None:
            covered_h.add((it['new_file'], it['new_line'] - 1))
        if key.startswith('D:'):
            cand = (it['file'], norm(it['before'])) in r_deleted
        elif 'removed' in it['kinds']:
            ri = items_r.get(key)
            cand = bool(ri) and 'removed' in ri['kinds']
        else:
            cand = (it['new_line'] - 1) not in res_h.get(it['new_file'], set())
            if cand and any(k.startswith('relocated') for k in it['kinds']):
                ri = items_r.get(key)
                cand = bool(ri) and ri.get('new_file') == it['new_file']
        if not cand:
            klass = 'U'
            notes.append('not reproduced by the replay of the compiled edits')
        else:
            klass = 'J'
            if 'label changed' in it['kinds']:
                ok, n9 = j9(it, rows)
                if not ok:
                    klass = 'R'
                    notes += n9
            if 'relocated_from_main' in it['kinds']:
                klass = 'R'
                notes.append('relocation out of Main: review of Main independence required')
            c = (cls or {}).get('items', {}).get(key)
            if c and c.get('class') == 'R' and klass == 'J':
                klass = 'R'
                notes.append('marked for review: %s' % c.get('reason', ''))
        if klass == 'R':
            c = (cls or {}).get('items', {}).get(key) or {}
            resn = c.get('resolution')
            if resn is not None:
                if resolution_ok(resn):
                    klass = 'R-justified' if resn['outcome'] == 'justified' else 'U'
                    notes.append('resolved by review %s' % resn['review'])
                else:
                    notes.append('resolution ignored: needs a recorded review URL and a reviewer distinct from the author')
        out[key] = {'kinds': it['kinds'], 'class': klass, 'scientific_evaluation': sci_flag(it), 'notes': notes}
    # replay-missing: residue lines of H that no item covers (H kept the baseline line where the replay
    # changed it), and replay lines with no H counterpart
    for f in sorted(res_h):
        for j in sorted(res_h[f]):
            if (f, j) in covered_h:
                continue
            line = h_corpus.get(f, '').split('\n')[j] if f in h_corpus else ''
            if not line.strip():
                continue
            out['M:%s:%d' % (f, j + 1)] = {'kinds': ['replay-missing'], 'class': 'U', 'notes':
                                           ['the replay changes this line and the after-state does not'],
                                           'scientific_evaluation': sci_text(line)}
        for i in res_r_only.get(f, []):
            line = r_corpus[f].split('\n')[i]
            out['MR:%s:%d' % (f, i + 1)] = {'kinds': ['replay-missing'], 'class': 'U', 'notes':
                                            ['a replayed line is absent from the after-state'],
                                            'scientific_evaluation': sci_text(line)}
    return out


def counts_of(res):
    c = {'items': len(res), 'J': 0, 'R-justified': 0, 'R-unresolved': 0, 'U': 0, 'scientific_evaluation': 0}
    for v in res.values():
        c['R-unresolved' if v['class'] == 'R' else v['class']] += 1
        c['scientific_evaluation'] += 1 if v['scientific_evaluation'] else 0
    return c


def verdict_of(counts, controls_ok, cc_ok):
    if not controls_ok or not cc_ok:
        v = 'VOID'
    elif counts['U'] > 0:
        v = 'FAIL'
    elif counts['R-unresolved'] > 0:
        v = 'PENDING'
    else:
        v = 'PASS'
    text = ('VERDICT %s: %d reported changes; J %d, R resolved as justified %d, R unresolved %d, U %d; '
            '%d flagged for scientific evaluation; controls %s; countercontrols %s.'
            % (v, counts['items'], counts['J'], counts['R-justified'], counts['R-unresolved'], counts['U'],
               counts['scientific_evaluation'], 'pass' if controls_ok else 'FAIL', 'pass' if cc_ok else 'FAIL'))
    return v, text


# --------------------------------------------------------------------------- collect

FROZEN_FILES = {'baseline.py': os.path.join(RECORD, 'baseline.py'),
                'snapshot.json': os.path.join(RECORD, 'snapshot.json'),
                'compare/verdict.py': os.path.abspath(__file__),
                'compare/edits/S2.json': S2_EDITS}


def digests():
    out = {k: sha256_file(p) for k, p in sorted(FROZEN_FILES.items())}
    out['ledger rows.json at %s' % LEDGER_COMMIT[:8]] = load_rows()[1]
    return out


def frozen_ok():
    with open(os.path.join(HERE, 'FROZEN.json'), encoding='utf-8') as fh:
        want = json.load(fh)['sha256']
    got = digests()
    for k in sorted(set(want) | set(got)):
        if got.get(k) != want.get(k):
            print('FROZEN MISMATCH  %s' % k)
    return got == want


def run(argv):
    return subprocess.run(argv, cwd=ROOT, capture_output=True, text=True).returncode


def write_tree(corpus, mutate=None):
    tmp = tempfile.mkdtemp(prefix='a1exit-cc-')
    for f, text in corpus.items():
        if mutate:
            text = mutate(f, text)
        os.makedirs(os.path.join(tmp, os.path.dirname(f)), exist_ok=True)
        with open(os.path.join(tmp, f), 'w', encoding='utf-8', newline='') as fh:
            fh.write(text)
    return tmp


def pick_injection(compare, corpus, snap):
    by_id = {e['id']: e for e in snap['entries']}
    for r in compare['entries']:
        e = by_id[r['id']]
        if r['status'] != ['unchanged'] or e['kind'] != 'table' or e['table']['class'] != 'prediction':
            continue
        text = corpus[r['new_file']].split('\n')[r['new_line'] - 1]
        toks = {n['tok'] for c in e['cells'] for n in c['numbers']}
        m = next((m for m in B.PROSE_DEC_RE.finditer(text) if m.group(0) in toks), None)
        if m:
            d = text[m.end() - 1]
            return {'key': r['id'], 'file': r['new_file'], 'line': r['new_line'], 'old_token': m.group(0),
                    'new_token': m.group(0)[:-1] + str((int(d) + 1) % 10), 'span': [m.start(), m.end()]}
    return None


def collect(head, out):
    fresh = not os.path.exists(out) or (os.path.isdir(out) and not os.listdir(out))
    if not fresh:
        print('collect refused: %s exists and is not empty' % out)
        return 4
    os.makedirs(out, exist_ok=True)
    base = os.path.join(RECORD, 'baseline.py')
    py = [sys.executable, '-I', '-B', base]
    me = [sys.executable, '-I', '-B', os.path.abspath(__file__)]
    ctl = {'C0-frozen-inputs': 0 if frozen_ok() else 1,
           'C4-verdict-self-test': run(me + ['self-test']),
           'C1-check': run(py + ['check']),
           'C2-self-test': run(py + ['self-test']),
           'C3-self-compare': run(py + ['--compare', B.PIN, '--json', os.path.join(out, 'self-compare.json')]),
           'C6-check-edits-S2': run(me + ['check-edits', '--edits', S2_EDITS, '--units', 'S2-A,S2-B,S2-C,S2-D,S2-E',
                                          '--commit', SOURCE_COMMIT])}
    try:
        dl = compile_units(['DEL'], head)
    except subprocess.CalledProcessError:
        dl = {'schema': 'a1exit-compare-edits/2', 'units': ['DEL'], 'commit': head, 'edits': [],
              'error': 'deletion record not present at the head'}
    with open(os.path.join(out, 'edits-del.json'), 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(dump_json(dl))
    ctl['C6-check-edits-DEL'] = run(me + ['check-edits', '--edits', os.path.join(out, 'edits-del.json'),
                                          '--units', 'DEL', '--commit', head])
    ctl['compare-ran'] = run(py + ['--compare', head, '--json', os.path.join(out, 'compare.json')])
    with open(os.path.join(out, 'compare.json'), encoding='utf-8') as fh:
        compare = json.load(fh)
    corpus = B.corpus_at_commit(head)
    inj = pick_injection(compare, corpus, load_snapshot())

    def mut(f, text):
        if inj and f == inj['file']:
            ls = text.split('\n')
            t = ls[inj['line'] - 1]
            a, b = inj['span']
            ls[inj['line'] - 1] = t[:a] + inj['new_token'] + t[b:]
            return '\n'.join(ls)
        return text
    tmp = write_tree(corpus, mut)
    try:
        ctl['C5-injected-compare-ran'] = run(py + ['--compare-tree', tmp, '--json',
                                                   os.path.join(out, 'injected-compare.json')])
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    expect = {'compare-ran': (0, 1), 'C5-injected-compare-ran': (1,)}
    controls = {k: {'exit': v, 'pass': v in expect.get(k, (0,))} for k, v in ctl.items()}
    rec = {'schema': 'a1exit-compare-controls/2', 'head': head, 'out_was_fresh': fresh, 'controls': controls,
           'injection': {k: inj[k] for k in ('key', 'file', 'line', 'old_token', 'new_token', 'span')} if inj else None}
    with open(os.path.join(out, 'controls.json'), 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(dump_json(rec))
    print(json.dumps(rec, ensure_ascii=False, sort_keys=True))
    return 0 if all(c['pass'] for c in controls.values()) and inj else 4


# --------------------------------------------------------------------------- verdict

def verdict(d, cls_path):
    def rd(n):
        with open(os.path.join(d, n), encoding='utf-8') as fh:
            return json.load(fh)
    compare, inj_cmp, ctl = rd('compare.json'), rd('injected-compare.json'), rd('controls.json')
    head = ctl['head']
    fresh_ok = ctl.get('out_was_fresh') is True and compare.get('other') == head and compare.get('pin') == B.PIN
    cls = None
    if cls_path:
        with open(cls_path, encoding='utf-8') as fh:
            cls = json.load(fh)
    with open(S2_EDITS, encoding='utf-8') as fh:
        s2 = json.load(fh)
    dl = rd('edits-del.json')
    edits = s2['edits'] + dl['edits']
    snap = load_snapshot()
    rows, rows_sha = load_rows()
    pin = B.PIN_CORPUS()
    r_corpus, log = replay(pin, edits)
    h_corpus = B.corpus_at_commit(head)
    compare_r = B.compare(snap, r_corpus)
    res = classify(snap, h_corpus, r_corpus, compare, compare_r, cls, rows)
    counts = counts_of(res)
    controls_ok = all(c['pass'] for c in ctl['controls'].values()) and ctl.get('injection') is not None and fresh_ok
    # C5: injected unjustified value change
    inj = ctl['injection']
    ih = dict(h_corpus)
    ls = ih[inj['file']].split('\n')
    t = ls[inj['line'] - 1]
    ls[inj['line'] - 1] = t[:inj['span'][0]] + inj['new_token'] + t[inj['span'][1]:]
    ih[inj['file']] = '\n'.join(ls)
    ires = classify(snap, ih, r_corpus, inj_cmp, compare_r, cls, rows)
    ic = counts_of(ires)
    c5 = ires.get(inj['key'], {}).get('class') == 'U' and ic['U'] == counts['U'] + 1
    # C7: a J item perturbed beyond its edit must flip to U
    jk = next((k for k, v in sorted(res.items()) if v['class'] == 'J' and not k.startswith(('D:', 'M:', 'MR:'))
               and 'removed' not in v['kinds']), None)
    c7 = {'key': jk, 'pass': True, 'note': 'no J item with an after-state line; not applicable'}
    if jk:
        cmp_items = items_of(compare, {e['id']: e for e in snap['entries']})
        it = cmp_items[jk]
        ph = dict(h_corpus)
        pl = ph[it['new_file']].split('\n')
        pl[it['new_line'] - 1] = pl[it['new_line'] - 1] + ' [perturbed]'
        ph[it['new_file']] = '\n'.join(pl)
        pcmp = B.compare(snap, ph)
        pres = classify(snap, ph, r_corpus, pcmp, compare_r, cls, rows)
        pkey = jk if not jk.startswith('U:') else jk
        c7 = {'key': jk, 'class_after_perturbation': pres.get(pkey, {}).get('class'),
              'U_base': counts['U'], 'U_perturbed': counts_of(pres)['U']}
        c7['pass'] = c7['class_after_perturbation'] == 'U' and c7['U_perturbed'] == counts['U'] + 1
    cc_ok = c5 and c7['pass']
    v, text = verdict_of(counts, controls_ok, cc_ok)
    inputs = {n: sha256_file(os.path.join(d, n)) for n in ('compare.json', 'injected-compare.json', 'controls.json',
                                                           'edits-del.json')}
    inputs['compare/edits/S2.json'] = sha256_file(S2_EDITS)
    inputs['classify.json'] = sha256_file(cls_path) if cls_path else None
    inputs['ledger rows.json'] = rows_sha
    out = {'schema': 'a1exit-compare-verdict/2', 'head': head, 'verdict': v, 'counts': counts, 'items': res,
           'controls': ctl['controls'], 'fresh_output': fresh_ok, 'replay_log': log,
           'countercontrols': {'C5': {'key': inj['key'], 'class': ires.get(inj['key'], {}).get('class'),
                                      'U_base': counts['U'], 'U_injected': ic['U'], 'pass': c5}, 'C7': c7},
           'inputs_sha256': inputs, 'text': text}
    with open(os.path.join(d, 'verdict.json'), 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(dump_json(out))
    print(text)
    return {'PASS': 0, 'FAIL': 1, 'PENDING': 3, 'VOID': 4}[v]


# --------------------------------------------------------------------------- self-test

def self_test():
    snap = load_snapshot()
    pin = dict(B.PIN_CORPUS())
    rows, _ = load_rows()
    by_id = {e['id']: e for e in snap['entries']}
    ok = True

    def report(name, good, detail=''):
        nonlocal ok
        print('%-62s %s  %s' % (name, 'PASS' if good else 'FAIL', detail))
        ok = ok and good

    def setline(c, f, ln, t):
        ls = c[f].split('\n')
        ls[ln - 1] = t
        c[f] = '\n'.join(ls)

    def ed(key, f, old, new, rows_=(), count=1, chapter=None, kind='replace', seq=0):
        return {'key': key, 'unit': key.split(':')[0], 'pr': None, 'id': key, 'seq': seq, 'kind': kind,
                'targets': [{'file': f, 'chapter': chapter, 'count': count}], 'old': old, 'new': new,
                'amends': None, 'rows': list(rows_), 'source_path': 'synthetic', 'method': 'synthetic'}

    def run_case(edits, mutate_h, cls=None):
        h = dict(pin)
        mutate_h(h)
        r, log = replay(pin, edits)
        res = classify(snap, h, r, B.compare(snap, h), B.compare(snap, r), cls, rows)
        return res, counts_of(res), log

    e85, e72 = by_id['appA:85'], by_id['appA:72']
    s964 = by_id['SM:964']
    e_val = ed('S2-X:V', e85['file'], '= 2.361$', '= 2.362$', ['X-47'])

    # T1 baseline against itself
    res, c, _ = run_case([], lambda h: None)
    report('T1 baseline vs itself: no change, PASS', c['items'] == 0 and verdict_of(c, True, True)[0] == 'PASS', str(c))
    # T2 unjustified value change
    res, c, _ = run_case([], lambda h: setline(h, e85['file'], e85['line'], e85['text'].replace('2.361', '2.362')))
    report('T2 injected unjustified value change -> U, flagged, FAIL',
           res.get('appA:85', {}).get('class') == 'U' and res['appA:85']['scientific_evaluation'] and c['U'] == 1
           and verdict_of(c, True, True)[0] == 'FAIL', str(c))
    # T3 exact replay -> J, flagged
    res, c, log = run_case([e_val], lambda h: setline(h, e85['file'], e85['line'],
                                                       e85['text'].replace('2.361', '2.362')))
    report('T3 change reproduced by the replay -> J, flagged',
           res.get('appA:85', {}).get('class') == 'J' and res['appA:85']['scientific_evaluation'] and c['U'] == 0,
           '%s %s' % (c, log))
    # G1 whole row deleted, edit removes only a fragment
    res, c, _ = run_case([ed('S2-X:G1', e72['file'], '10.02', '10.0')],
                         lambda h: h.__setitem__(e72['file'], '\n'.join(
                             l for i, l in enumerate(h[e72['file']].split('\n')) if i != e72['line'] - 1)))
    report('G1 row deleted, cited fragment edit -> U', res.get('appA:72', {}).get('class') == 'U', str(c))
    # G2 new prediction sentence justified by a bare "conditional" insertion elsewhere
    comp = 'papers/Computation.md'
    cl = pin[comp].split('\n')
    tgt = next(i for i, l in enumerate(cl) if len(l) > 80 and 'conditional' not in l)
    w = cl[tgt].split()[-1]
    res, c, _ = run_case([ed('S2-X:G2', comp, w, w + ' conditional')],
                         lambda h: h.__setitem__(comp, 'Predicted 1.234 MeV (conditional).\n\n' + h[comp]))
    new_u = [k for k in res if k.startswith('U:') and res[k]['class'] == 'U']
    report('G2 new prediction sentence, unrelated cited insertion -> U', len(new_u) == 1 and c['U'] >= 2, str(c))
    # G3 reviewed word edit plus an unreviewed deletion on the same line
    i135 = by_id['Intro:135']
    words = i135['text'].split(' ')
    g3_after = ' '.join(words[:-6]).replace(words[3], words[3] + 'z', 1)
    res, c, _ = run_case([ed('S2-X:G3', i135['file'], ' '.join(words[2:5]),
                             ' '.join([words[2], words[3] + 'z', words[4]]))],
                         lambda h: setline(h, i135['file'], i135['line'], g3_after))
    report('G3 reviewed word edit hiding an unreviewed deletion -> U', res.get('Intro:135', {}).get('class') == 'U', str(c))
    # G4b unit change MeV -> GeV where the cited edit changes only the number
    res, c, _ = run_case([ed('S2-X:G4', s964['file'], '0.51098', '0.51099')],
                         lambda h: setline(h, s964['file'], s964['line'],
                                           s964['text'].replace('0.51098 MeV', '0.51099 GeV', 1)))
    report('G4b unit change hidden behind a number edit -> U', res.get('SM:964', {}).get('class') == 'U', str(c))
    # G5b predicted and observed swapped
    swapped = s964['text'].replace('0.51098 MeV', '@@').replace('0.51100 MeV', '0.51098 MeV').replace('@@', '0.51100 MeV')
    res, c, _ = run_case([ed('S2-X:G5', s964['file'], '0.003%', '0.003%')],
                         lambda h: setline(h, s964['file'], s964['line'], swapped))
    report('G5b predicted/observed swap -> U', res.get('SM:964', {}).get('class') == 'U', str(c))
    # G6 no-op edit cited for a real change
    res, c, _ = run_case([ed('S2-X:G6', e85['file'], '| L | 2(a) |', '| L | 2(a) |')],
                         lambda h: setline(h, e85['file'], e85['line'], e85['text'].replace('| L |', '| C |')))
    report('G6 no-op edit cited for a label change -> U', res.get('appA:85', {}).get('class') == 'U', str(c))
    # G7 F-row line promoted ("conditional" -> "established") while the edit changes something else
    def window(e):
        i = e['text'].find('conditional')
        return e['text'][max(0, i - 25):i + len('conditional')]
    frow = next(e for e in snap['entries'] if e['kind'] == 'prose' and e['file'].startswith('papers/')
                and 'conditional' in e['text']
                and any(rows.get(r, {}).get('disposition') == 'F' for r in e['ledger_rows'])
                and pin[e['file']].count(window(e)) == 1)
    fwin = window(frow)
    fw = frow['text'].split()
    res, c, _ = run_case([ed('S2-X:G7', frow['file'], fw[0] + ' ' + fw[1], fw[0] + ' ' + fw[1])],
                         lambda h: setline(h, frow['file'], frow['line'],
                                           frow['text'].replace('conditional', 'established', 1)))
    report('G7 F-row promotion beside an unrelated edit -> U (%s)' % frow['id'],
           res.get(frow['id'], {}).get('class') == 'U', str(c))
    # J9 the promotion itself reproduced by the replay -> R, never J
    promo = frow['text'].replace('conditional', 'established', 1)
    res, c, _ = run_case([ed('S2-X:P', frow['file'], fwin, fwin.replace('conditional', 'established'))],
                         lambda h: setline(h, frow['file'], frow['line'], promo))
    report('J9 reproduced promotion on an F row -> R', res.get(frow['id'], {}).get('class') == 'R',
           str(res.get(frow['id'])))
    # J9 an O-row label change keeping an open term -> J
    orow = next(e for e in snap['entries'] if e['kind'] == 'prose' and e['ledger_rows'] and
                all(rows.get(r, {}).get('disposition') == 'O' for r in e['ledger_rows'] if r in rows)
                and any(r in rows for r in e['ledger_rows']))
    ot = orow['text'] + ' This is conditional.'
    res, c, _ = run_case([ed('S2-X:O', orow['file'], orow['text'][-40:], orow['text'][-40:] + ' This is conditional.')],
                         lambda h: setline(h, orow['file'], orow['line'], ot))
    report('J9 O-row label change with an open term, reproduced -> J (%s)' % orow['id'],
           res.get(orow['id'], {}).get('class') == 'J', str(res.get(orow['id'])))
    # S1 a FULL edit scoped to the wrong chapter does not apply -> U
    f1642 = by_id['FULL:1642']
    res, c, log = run_case([ed('S2-X:S1', FULL, f1642['text'][:30], f1642['text'][:30] + 'Q', chapter='book/ch01-observation.md')],
                           lambda h: setline(h, FULL, 1642, f1642['text'].replace(f1642['text'][:30], f1642['text'][:30] + 'Q', 1)))
    report('S1 FULL edit outside its chapter span -> unapplied, U',
           res.get('FULL:1642', {}).get('class') == 'U' and 'unapplied' in log[0][1], str(log))
    res, c, log = run_case([ed('S2-X:S1b', FULL, f1642['text'][:30], f1642['text'][:30] + 'Q',
                               chapter='book/ch06-matter-content.md')],
                           lambda h: setline(h, FULL, 1642, f1642['text'].replace(f1642['text'][:30], f1642['text'][:30] + 'Q', 1)))
    report('S1b the same edit in its own chapter span -> J', res.get('FULL:1642', {}).get('class') == 'J', str(log))
    # M1 a reviewed edit missing from the after-state -> replay-missing U
    res, c, _ = run_case([e_val], lambda h: None)
    report('M1 reviewed edit not present in the after-state -> U (replay-missing)',
           c['U'] == 1 and any(v['kinds'] == ['replay-missing'] for v in res.values()), str(c))
    # R resolution must cite a recorded non-author review
    res0, c0, _ = run_case([ed('S2-X:P', frow['file'], fwin, fwin.replace('conditional', 'established'))],
                           lambda h: setline(h, frow['file'], frow['line'], promo))
    good_res = {'outcome': 'justified', 'review': 'https://github.com/amaybaum/incompleteness/pull/1483#issuecomment-1',
                'reviewer': 'reviewer-x', 'author': 'writer-y'}
    cases = {'valid': good_res, 'no URL': dict(good_res, review='looks fine'),
             'self-review': dict(good_res, reviewer='writer-y')}
    got = {}
    for name, rz in cases.items():
        cls = {'schema': 'a1exit-compare-classify/2', 'head': 'synthetic',
               'items': {frow['id']: {'class': 'R', 'reason': 'synthetic', 'resolution': rz}}}
        r2, _, _ = run_case([ed('S2-X:P', frow['file'], fwin, fwin.replace('conditional', 'established'))],
                            lambda h: setline(h, frow['file'], frow['line'], promo), cls)
        got[name] = r2[frow['id']]['class']
    report('R resolution: valid review -> R-justified; no URL or self-review -> stays R',
           got == {'valid': 'R-justified', 'no URL': 'R', 'self-review': 'R'}, str(got))
    # relocation out of Main reproduced -> R
    m780 = by_id['M:780']

    def mv(h):
        ls = h['papers/Main.md'].split('\n')
        del ls[779]
        h['papers/Main.md'] = '\n'.join(ls)
        h['papers/Substratum.md'] = h['papers/Substratum.md'] + '\n' + m780['text'] + '\n'
    rpin = dict(pin)
    mv(rpin)
    res = classify(snap, rpin, rpin, B.compare(snap, rpin), B.compare(snap, rpin), None, rows)
    report('Relocation out of Main reproduced by the replay -> R', res.get('M:780', {}).get('class') == 'R',
           str(res.get('M:780')))
    # C7 mechanism: a J item perturbed beyond its edit flips to U
    res, c, _ = run_case([e_val], lambda h: setline(h, e85['file'], e85['line'],
                                                     e85['text'].replace('2.361', '2.362') + ' [perturbed]'))
    report('C7 J item perturbed beyond its edit -> U', res.get('appA:85', {}).get('class') == 'U', str(c))
    # VOID when a control fails
    report('VOID on a failed control or countercontrol',
           verdict_of(counts_of({}), False, True)[0] == 'VOID' and verdict_of(counts_of({}), True, False)[0] == 'VOID')
    # parsers: heading / table / bullet / resolved on fixed samples
    amap = amap_full()
    sample_h = '### E1 — x; ledger X-50\n\nSites: `papers/Main.md:328`\n\nOld:\n\n```text\nA b\n```\n\nNew:\n\n```text\nA c\n```\n'
    sample_t = '| Id | Site | Old | New |\n|---|---|---|---|\n| R9 | Main:336 | `x y` | `x z` |\n'
    sample_b = ('**A1-1 (N1).** At M:131, :141 and `papers/SM.md:44`, replace\n\n- old: "a\n  b"\n- new: "c"\n')
    ph, pt, pb = parse_md_heading(sample_h, amap), parse_md_table(sample_t, amap), parse_md_bullet(sample_b, amap)
    good = (ph and ph[0]['old'] == 'A b' and ph[0]['new'] == 'A c' and ph[0]['sites'] == [('papers/Main.md', 328)]
            and pt and pt[0]['old'] == 'x y' and pt[0]['sites'] == [('papers/Main.md', 336)]
            and pb and pb[0]['old'] == 'a b' and pb[0]['sites'] == [('papers/Main.md', 131), ('papers/Main.md', 141),
                                                                  ('papers/SM.md', 44)])
    report('Markdown parsers (heading, table, bullet) on fixed samples', bool(good))
    print('self-test ' + ('PASS' if ok else 'FAIL'))
    return 0 if ok else 1


# --------------------------------------------------------------------------- main

def main(argv):
    def opt(name):
        return argv[argv.index(name) + 1] if name in argv and argv.index(name) + 1 < len(argv) else None
    if not argv:
        print(__doc__)
        return 2
    if argv[0] == 'self-test':
        return self_test()
    if argv[0] == 'digests':
        print(dump_json({'schema': 'a1exit-compare-frozen/2', 'pin': B.PIN, 'source_commit': SOURCE_COMMIT,
                         'ledger_commit': LEDGER_COMMIT, 'sha256': digests()}), end='')
        return 0
    if argv[0] == 'compile' and opt('--units') and opt('--commit') and opt('--out'):
        with open(opt('--out'), 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(dump_json(compile_units(opt('--units').split(','), opt('--commit'))))
        return 0
    if argv[0] == 'check-edits' and opt('--edits') and opt('--units') and opt('--commit'):
        return check_edits(opt('--edits'), opt('--units').split(','), opt('--commit'))
    if argv[0] == 'collect' and opt('--head') and opt('--out'):
        return collect(opt('--head'), opt('--out'))
    if argv[0] == 'verdict' and opt('--dir'):
        return verdict(opt('--dir'), opt('--classify'))
    print(__doc__)
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
