#!/usr/bin/env python3
"""A1-EXIT regression comparison (#1468): frozen collection, classification check and verdict.

Standard library only; run with `python3 -I -B`. The procedure and decision rules are PREREG.md in
this directory. Modes:

  collect --head <sha> --out <dir>
      Controls C1-C3 (baseline check, self-test, self-compare) as exit statuses; the comparison
      `baseline.py --compare <sha> --json <dir>/compare.json`; and the countercontrol C5 (the corpus of
      <sha> copied to a temporary directory, one unjustified value change injected, compared with
      --compare-tree into <dir>/injected-compare.json). Writes <dir>/controls.json.
  verdict --dir <dir> --edits <edits.json> --classify <classify.json>
      Validates every classification against the decision rules, applies the countercontrol, and
      writes <dir>/verdict.json and the verdict text. Exit 0 on PASS, 1 on FAIL, 3 on PENDING,
      4 on VOID.
  check-edits --edits <edits.json> [--commit <rev>]
      Checks that every compiled edit occurs in its cited source record at <rev> (default HEAD).
  self-test
      Controls of this tool on synthetic data built from the pinned corpus (no after-state is read).
  digests
      Print the SHA-256 of baseline.py, snapshot.json and this file (the content of FROZEN.json).

Schemas (all JSON, UTF-8):
  edits.json      a1exit-compare-edits/1: {"schema", "edits": [{"key", "unit", "pr", "id", "file",
                  "files", "old", "new", "rows", "source_path"}]}; key = "<unit>:<id>".
  classify.json   a1exit-compare-classify/1: {"schema", "head", "items": {<item key>: {"class": "J"|"R",
                  "edits": [<edit key>...], "ledger_row": <row or null>, "reason": <text>,
                  "resolution": null | {"outcome": "justified"|"unjustified", "review": <reference>}}}}
                  Item keys: an entry id ("M:780"); "U:<file>:<line>" for an unaccounted line;
                  "D:<file>:<line>" for a deleted line (lines as in compare.json). An item not listed
                  is unclassified and counts as U.
  controls.json   a1exit-compare-controls/1: {"schema", "head", "controls": {<name>: {"exit": int,
                  "pass": bool}}, "injection": {"key", "file", "line", "old_token", "new_token"}}
  verdict.json    a1exit-compare-verdict/1: {"schema", "head", "verdict", "counts", "items", "controls",
                  "countercontrol", "text"}
"""
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
JUSTIFYING_PRS = {1470, 1473, 1474, 1472, 1475}   # Step-2 units S2-A, S2-B, S2-C, S2-D, S2-E
DELETION_UNIT = 'DEL'                              # the executed A1 deletion edit (#1477 plan)
SCI_CATEGORIES = {'C-TAB', 'C-PROSE', 'C-FINL', 'C-CDO', 'C-CAL', 'C-OBS', 'C-OPEN'}
OPEN_TERMS = re.compile(r'\b(open|conditional(?:ly)?|hypothes[ie]s|assumed|posit(?:ed)?|not established|'
                        r'not derived|conjectur\w*)\b', re.I)
FINITE_TERMS = re.compile(r'\bfinite\b|for a finite|finite[- ]only|finite representative|finite substrat',
                          re.I)


def norm(s):
    return ' '.join(s.split())


def run(argv):
    r = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True)
    return r.returncode


# --------------------------------------------------------------------------- collect

FROZEN_FILES = {'baseline.py': os.path.join(RECORD, 'baseline.py'),
                'snapshot.json': os.path.join(RECORD, 'snapshot.json'),
                'compare/verdict.py': os.path.abspath(__file__)}


def digests():
    import hashlib
    out = {}
    for k, p in sorted(FROZEN_FILES.items()):
        with open(p, 'rb') as fh:
            out[k] = hashlib.sha256(fh.read()).hexdigest()
    return out


def frozen_ok():
    """C0: the tools and baseline in use are byte-identical to those frozen in FROZEN.json."""
    with open(os.path.join(HERE, 'FROZEN.json'), encoding='utf-8') as fh:
        want = json.load(fh)['sha256']
    got = digests()
    for k in sorted(want):
        if got.get(k) != want[k]:
            print('FROZEN MISMATCH  %s' % k)
    return got == want


def pick_injection(compare, corpus):
    """The first C-TAB prediction-table entry reported unchanged, with a decimal token."""
    snap = load_snapshot()
    by_id = {e['id']: e for e in snap['entries']}
    for r in compare['entries']:
        e = by_id[r['id']]
        if r['status'] != ['unchanged'] or e['kind'] != 'table' or e['table']['class'] != 'prediction':
            continue
        f, ln = r['new_file'], r['new_line']
        text = B.lines_of(corpus[f])[ln - 1]
        toks = {n['tok'] for c in e['cells'] for n in c['numbers']}
        m = next((m for m in B.PROSE_DEC_RE.finditer(text) if m.group(0) in toks), None)
        if m:
            d = text[m.end() - 1]
            new_tok = m.group(0)[:-1] + str((int(d) + 1) % 10)
            return {'key': r['id'], 'file': f, 'line': ln, 'old_token': m.group(0), 'new_token': new_tok,
                    'span': [m.start(), m.end()]}
    return None


def collect(head, out):
    os.makedirs(out, exist_ok=True)
    base = os.path.join(RECORD, 'baseline.py')
    py = [sys.executable, '-I', '-B', base]
    ctl = {}
    ctl['C0-frozen-tools'] = 0 if frozen_ok() else 1
    ctl['C4-verdict-self-test'] = run([sys.executable, '-I', '-B', os.path.abspath(__file__), 'self-test'])
    ctl['C1-check'] = run(py + ['check'])
    ctl['C2-self-test'] = run(py + ['self-test'])
    ctl['C3-self-compare'] = run(py + ['--compare', B.PIN, '--json', os.path.join(out, 'self-compare.json')])
    code = run(py + ['--compare', head, '--json', os.path.join(out, 'compare.json')])
    ctl['compare-ran'] = code
    with open(os.path.join(out, 'compare.json'), encoding='utf-8') as fh:
        compare = json.load(fh)
    corpus = B.corpus_at_commit(head)
    inj = pick_injection(compare, corpus)
    tmp = tempfile.mkdtemp(prefix='a1exit-cc-')
    try:
        for f, text in corpus.items():
            if inj and f == inj['file']:
                ls = B.lines_of(text)
                t = ls[inj['line'] - 1]
                a, b = inj['span']
                ls[inj['line'] - 1] = t[:a] + inj['new_token'] + t[b:]
                text = '\n'.join(ls)
            os.makedirs(os.path.join(tmp, os.path.dirname(f)), exist_ok=True)
            with open(os.path.join(tmp, f), 'w', encoding='utf-8', newline='') as fh:
                fh.write(text)
        ctl['C5-injected-compare-ran'] = run(py + ['--compare-tree', tmp, '--json',
                                                   os.path.join(out, 'injected-compare.json')])
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    expect = {'C0-frozen-tools': 0, 'C4-verdict-self-test': 0, 'C1-check': 0, 'C2-self-test': 0, 'C3-self-compare': 0, 'compare-ran': (0, 1),
              'C5-injected-compare-ran': 1}
    controls = {k: {'exit': v, 'pass': (v in expect[k]) if isinstance(expect[k], tuple) else v == expect[k]}
                for k, v in ctl.items()}
    rec = {'schema': 'a1exit-compare-controls/1', 'head': head, 'controls': controls,
           'injection': {k: inj[k] for k in ('key', 'file', 'line', 'old_token', 'new_token')} if inj else None}
    with open(os.path.join(out, 'controls.json'), 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(json.dumps(rec, ensure_ascii=False, indent=1, sort_keys=True) + '\n')
    print(json.dumps(rec, ensure_ascii=False, sort_keys=True))
    return 0 if all(c['pass'] for c in controls.values()) and inj else 4


# --------------------------------------------------------------------------- classification rules

def load_snapshot():
    with open(os.path.join(RECORD, 'snapshot.json'), encoding='utf-8') as fh:
        return json.load(fh)


def items_of(compare):
    """Every reported change, keyed; each with kind, before text, after text and flags."""
    snap = {e['id']: e for e in load_snapshot()['entries']}
    out = {}
    for r in compare['entries']:
        e = snap[r['id']]
        st = r['status']
        if st == ['unchanged'] and not r.get('relocated'):
            continue
        kinds = [] if st == ['unchanged'] else list(st)
        if r.get('relocated'):
            kinds.append('relocated_from_main' if r.get('relocated_from_main') else 'relocated')
        out[r['id']] = {'kinds': kinds, 'file': e['file'], 'new_file': r.get('new_file'),
                        'before': e['text'], 'after': r.get('new_text', e['text'] if 'new_file' in r else None),
                        'categories': e['categories'],
                        'table_class': e['table']['class'] if e['kind'] == 'table' else None,
                        'before_numbers': B.number_key(B.all_numbers(e))}
    for u in compare['unaccounted']:
        out['U:%s:%d' % (u['file'], u['line'])] = {'kinds': ['unaccounted'], 'file': u['file'],
                                                   'before': None, 'after': u['text'], 'flags': u['flags']}
    for d in compare['deleted']:
        out['D:%s:%d' % (d['file'], d['line'])] = {'kinds': ['deleted'], 'file': d['file'],
                                                   'before': d['text'], 'after': None, 'flags': d['flags']}
    return out


def file_ok(e, f):
    files = set(e.get('files') or []) | {e['file']}
    return f in files or (f == FULL and any(x.startswith('book/') for x in files))


def sci_flag(item):
    if item.get('categories') and set(item['categories']) & SCI_CATEGORIES:
        if 'C-TAB' in item['categories'] and len(item['categories']) == 1 and item.get('table_class') == 'other':
            return False
        return True
    fl = item.get('flags') or []
    return 'numbers' in fl or 'marker' in fl


def changed_tokens(before, after):
    bt = [n['tok'] for n in B.parse_numbers(before)] if before else []
    at = [n['tok'] for n in B.parse_numbers(after)] if after else []
    rem, add = list(bt), []
    for t in at:
        if t in rem:
            rem.remove(t)
        else:
            add.append(t)
    return rem, add


def edit_covers(item, kind, e):
    """Rule J1-J8 of PREREG §3: does edit e account for this item's change of this kind?"""
    old, new = norm(e['old']), norm(e['new'])
    before = norm(item['before']) if item['before'] is not None else None
    after = norm(item['after']) if item['after'] is not None else None
    if kind in ('text changed', 'value changed', 'label changed'):
        if not (file_ok(e, item['file']) and old and old in before and new in after):
            return False
        if kind == 'value changed':
            rem, add = changed_tokens(item['before'], item['after'])
            ot = [n['tok'] for n in B.parse_numbers(e['old'])]
            nt = [n['tok'] for n in B.parse_numbers(e['new'])]
            return all(t in ot for t in rem) and all(t in nt for t in add)
        return True
    if kind == 'removed':
        return file_ok(e, item['file']) and (before in old or (old and old in before))
    if kind in ('relocated', 'relocated_from_main'):
        return (file_ok(e, item['file']) and before in old) or (file_ok(e, item['new_file']) and before in new)
    if kind == 'unaccounted':
        return file_ok(e, item['file']) and bool(new) and (after in new or new in after)
    if kind == 'deleted':
        return file_ok(e, item['file']) and bool(old) and (before in old or old in before)
    return False


def disposition_ok(item, row, rows):
    """Rule J9: a label change matches an accepted ledger disposition of the cited row."""
    r = rows.get(row)
    if r is None:
        return False
    disp = r['disposition']
    after = item['after'] or ''
    if disp == 'F':
        return bool(FINITE_TERMS.search(after))
    if disp == 'O':
        return bool(OPEN_TERMS.search(after))
    if disp == 'J':
        # no silent promotion: an open/conditional term present before must survive
        return not (OPEN_TERMS.search(item['before'] or '') and not OPEN_TERMS.search(after))
    return False


def classify(compare, edits, cls, rows):
    E = {e['key']: e for e in edits['edits']}
    res = {}
    for key, item in sorted(items_of(compare).items()):
        c = cls.get('items', {}).get(key)
        notes, klass = [], 'U'
        if c is None:
            notes.append('unclassified')
        else:
            cited = [E[k] for k in c.get('edits', []) if k in E]
            missing = [k for k in c.get('edits', []) if k not in E]
            if missing:
                notes.append('cited edits not in the compiled list: %s' % ', '.join(missing))
            bad_src = [e['key'] for e in cited if not (e['pr'] in JUSTIFYING_PRS or e['unit'] == DELETION_UNIT)]
            if bad_src:
                notes.append('cited edits outside the justification sources: %s' % ', '.join(bad_src))
                cited = [e for e in cited if e['key'] not in bad_src]
            covered = all(any(edit_covers(item, k, e) for e in cited) for k in item['kinds']) and bool(cited)
            label_ok = True
            if 'label changed' in item['kinds']:
                row = c.get('ledger_row')
                rows_ok = row is not None and any(row in (e.get('rows') or []) for e in cited)
                label_ok = rows_ok and disposition_ok(item, row, rows)
                if not label_ok:
                    notes.append('label change does not match the cited row\'s accepted disposition')
            needs_review = 'relocated_from_main' in item['kinds']
            if c.get('class') == 'J' and covered and label_ok and not needs_review:
                klass = 'J'
            elif c.get('class') in ('J', 'R') and covered:
                klass = 'R'
                if needs_review:
                    notes.append('relocation out of Main: review of Main independence required')
            elif c.get('class') == 'R':
                klass = 'R'
                notes.append('no covering edit; R requires review')
            else:
                notes.append('no cited edit accounts for the change')
            if klass == 'R':
                resn = c.get('resolution')
                if resn and resn.get('review') and resn.get('outcome') in ('justified', 'unjustified'):
                    klass = 'R-justified' if resn['outcome'] == 'justified' else 'U'
                    notes.append('resolved by review: %s' % resn['review'])
        res[key] = {'kinds': item['kinds'], 'class': klass, 'scientific_evaluation': sci_flag(item),
                    'notes': notes}
    return res


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
            '%d flagged for scientific evaluation; controls %s; countercontrol %s.'
            % (v, counts['items'], counts['J'], counts['R-justified'], counts['R-unresolved'], counts['U'],
               counts['scientific_evaluation'], 'pass' if controls_ok else 'FAIL', 'pass' if cc_ok else 'FAIL'))
    return v, text


def load_rows():
    with open(os.path.join(ROOT, 'verification/audits/foundations/a1exit-ledger-20261120/rows.json'),
              encoding='utf-8') as fh:
        return {r['id']: r for r in json.load(fh)['rows']}


def verdict(d, edits_path, cls_path):
    rd = lambda n: json.load(open(os.path.join(d, n), encoding='utf-8'))  # noqa: E731
    compare, inj, ctl = rd('compare.json'), rd('injected-compare.json'), rd('controls.json')
    edits = json.load(open(edits_path, encoding='utf-8'))
    cls = json.load(open(cls_path, encoding='utf-8'))
    rows = load_rows()
    res = classify(compare, edits, cls, rows)
    counts = counts_of(res)
    controls_ok = all(c['pass'] for c in ctl['controls'].values()) and ctl.get('injection') is not None
    ires = classify(inj, edits, cls, rows)
    ic = counts_of(ires)
    k = ctl['injection']['key'] if ctl.get('injection') else None
    cc_ok = bool(k) and ires.get(k, {}).get('class') == 'U' and ic['U'] == counts['U'] + 1
    v, text = verdict_of(counts, controls_ok, cc_ok)
    out = {'schema': 'a1exit-compare-verdict/1', 'head': ctl['head'], 'verdict': v, 'counts': counts,
           'items': res, 'controls': ctl['controls'],
           'countercontrol': {'key': k, 'class': ires.get(k, {}).get('class'), 'U_base': counts['U'],
                              'U_injected': ic['U'], 'pass': cc_ok}, 'text': text}
    with open(os.path.join(d, 'verdict.json'), 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(json.dumps(out, ensure_ascii=False, indent=1, sort_keys=True) + '\n')
    print(text)
    return {'PASS': 0, 'FAIL': 1, 'PENDING': 3, 'VOID': 4}[v]


def check_edits(edits_path, commit='HEAD'):
    edits = json.load(open(edits_path, encoding='utf-8'))
    bad = 0
    cache = {}
    for e in edits['edits']:
        p = e['source_path']
        if p not in cache:
            cache[p] = B.git('show', '%s:%s' % (commit, p)).decode('utf-8')
        src = cache[p]
        if p.endswith('.json'):
            data = json.loads(src)
            objs = data if isinstance(data, list) else data.get('edits', [])
            ok = any(isinstance(o, dict) and o.get('old') == e['old'] and o.get('new') == e['new'] for o in objs)
        else:
            ok = e['old'] in src and e['new'] in src
        if not ok:
            bad += 1
            print('EDIT NOT IN SOURCE  %s  (%s)' % (e['key'], p))
    print('check-edits: %d edits, %d not found in their source' % (len(edits['edits']), bad))
    return 1 if bad else 0


# --------------------------------------------------------------------------- self-test

def self_test():
    snap = load_snapshot()
    pin = dict(B.PIN_CORPUS())
    rows = load_rows()
    ok = True

    def cmp_of(mut):
        c = dict(pin)
        mut(c)
        return B.compare(snap, c)

    def setline(c, f, ln, t):
        ls = B.lines_of(c[f])
        ls[ln - 1] = t
        c[f] = '\n'.join(ls)

    def report(name, good, detail=''):
        nonlocal ok
        print('%-56s %s  %s' % (name, 'PASS' if good else 'FAIL', detail))
        ok = ok and good

    empty_edits = {'schema': 'a1exit-compare-edits/1', 'edits': []}
    empty_cls = {'schema': 'a1exit-compare-classify/1', 'head': 'synthetic', 'items': {}}
    # T1 the baseline against itself: no reported change, verdict PASS
    r0 = B.compare(snap, pin)
    c0 = counts_of(classify(r0, empty_edits, empty_cls, rows))
    v0, _ = verdict_of(c0, True, True)
    report('T1 baseline vs itself: no change, PASS', c0['items'] == 0 and v0 == 'PASS', str(c0))
    # T2 an unjustified value change in a prediction-table row is U, verdict FAIL
    e85 = [e for e in snap['entries'] if e['id'] == 'appA:85'][0]
    r1 = cmp_of(lambda c: setline(c, e85['file'], e85['line'], e85['text'].replace('2.361', '2.362', 1)))
    res1 = classify(r1, empty_edits, empty_cls, rows)
    c1 = counts_of(res1)
    report('T2 injected unjustified value change -> U, FAIL',
           res1.get('appA:85', {}).get('class') == 'U' and c1['U'] == 1 and verdict_of(c1, True, True)[0] == 'FAIL'
           and res1['appA:85']['scientific_evaluation'], str(c1))
    # T3 the same change, justified by a cited edit of a justifying PR whose strings cover it: J
    ed = {'schema': 'a1exit-compare-edits/1', 'edits': [
        {'key': 'S2X:E1', 'unit': 'S2X', 'pr': 1475, 'id': 'E1', 'file': e85['file'], 'files': [e85['file']],
         'old': '$4.28/Z_S(\\lambda g_0^2) = 2.361$', 'new': '$4.28/Z_S(\\lambda g_0^2) = 2.362$',
         'rows': ['X-47'], 'source_path': 'synthetic'}]}
    cj = {'schema': 'a1exit-compare-classify/1', 'head': 'synthetic',
          'items': {'appA:85': {'class': 'J', 'edits': ['S2X:E1'], 'ledger_row': 'X-47', 'reason': 'synthetic',
                                'resolution': None}}}
    res3 = classify(r1, ed, cj, rows)
    report('T3 covered value change cited to a landed edit -> J, flagged',
           res3['appA:85']['class'] == 'J' and res3['appA:85']['scientific_evaluation'],
           str(res3['appA:85']))
    # T4 a citation whose new string is not in the after text is rejected -> U
    ed4 = json.loads(json.dumps(ed))
    ed4['edits'][0]['new'] = '$4.28/Z_S(\\lambda g_0^2) = 2.363$'
    res4 = classify(r1, ed4, cj, rows)
    report('T4 citation that does not cover the change -> U', res4['appA:85']['class'] == 'U', str(res4['appA:85']))
    # T5 a citation to a PR outside the justification sources -> U
    ed5 = json.loads(json.dumps(ed))
    ed5['edits'][0]['pr'] = 9999
    res5 = classify(r1, ed5, cj, rows)
    report('T5 citation outside the justification sources -> U', res5['appA:85']['class'] == 'U')
    # T6 value change outside the edit's span (edit covers a different number) -> U
    ed6 = json.loads(json.dumps(ed))
    ed6['edits'][0]['old'], ed6['edits'][0]['new'] = '| L | 2(a) |', '| L | 2(a) |'
    res6 = classify(r1, ed6, cj, rows)
    report('T6 value change outside the cited edit\'s span -> U', res6['appA:85']['class'] == 'U')
    # T7 R unresolved -> PENDING; resolved justified -> PASS; resolved unjustified -> FAIL
    cr = json.loads(json.dumps(cj))
    cr['items']['appA:85']['class'] = 'R'
    c7 = counts_of(classify(r1, ed, cr, rows))
    cr['items']['appA:85']['resolution'] = {'outcome': 'justified', 'review': 'synthetic review'}
    c7b = counts_of(classify(r1, ed, cr, rows))
    cr['items']['appA:85']['resolution'] = {'outcome': 'unjustified', 'review': 'synthetic review'}
    c7c = counts_of(classify(r1, ed, cr, rows))
    report('T7 R: unresolved PENDING, justified PASS, unjustified FAIL',
           verdict_of(c7, True, True)[0] == 'PENDING' and verdict_of(c7b, True, True)[0] == 'PASS'
           and verdict_of(c7c, True, True)[0] == 'FAIL')
    # T8 relocation out of Main is never plain J
    m780 = [e for e in snap['entries'] if e['id'] == 'M:780'][0]

    def mv(c):
        ls = B.lines_of(c['papers/Main.md'])
        del ls[779]
        c['papers/Main.md'] = '\n'.join(ls)
        c['papers/Substratum.md'] = c['papers/Substratum.md'] + '\n' + m780['text'] + '\n'
    r8 = cmp_of(mv)
    ed8 = {'schema': 'a1exit-compare-edits/1', 'edits': [
        {'key': 'DEL:X1', 'unit': 'DEL', 'pr': None, 'id': 'X1', 'file': 'papers/Substratum.md',
         'files': ['papers/Substratum.md'], 'old': '', 'new': m780['text'], 'rows': ['X-48'],
         'source_path': 'synthetic'}]}
    c8 = {'schema': 'a1exit-compare-classify/1', 'head': 'synthetic',
          'items': {'M:780': {'class': 'J', 'edits': ['DEL:X1'], 'ledger_row': 'X-48', 'reason': 'synthetic',
                              'resolution': None}}}
    res8 = classify(r8, ed8, c8, rows)
    report('T8 relocation out of Main cited as J -> R (Main independence)', res8.get('M:780', {}).get('class') == 'R',
           str(res8.get('M:780')))
    # T9 a label change needs the cited row's accepted disposition (F row requires a finite scope term)
    i135 = [e for e in snap['entries'] if e['id'] == 'Intro:135'][0]
    r9 = cmp_of(lambda c: setline(c, i135['file'], i135['line'], i135['text'] + ' This is conditional.'))
    ed9 = {'schema': 'a1exit-compare-edits/1', 'edits': [
        {'key': 'S2X:E9', 'unit': 'S2X', 'pr': 1475, 'id': 'E9', 'file': i135['file'], 'files': [i135['file']],
         'old': i135['text'][-30:], 'new': i135['text'][-30:] + ' This is conditional.', 'rows': ['X-48', 'X-11'],
         'source_path': 'synthetic'}]}
    c9 = {'schema': 'a1exit-compare-classify/1', 'head': 'synthetic',
          'items': {'Intro:135': {'class': 'J', 'edits': ['S2X:E9'], 'ledger_row': 'X-11', 'reason': 'synthetic',
                                  'resolution': None}}}
    res9 = classify(r9, ed9, c9, rows)
    c9b = json.loads(json.dumps(c9))
    c9b['items']['Intro:135']['ledger_row'] = 'X-44'
    res9b = classify(r9, ed9, c9b, rows)
    report('T9 label change: O row with open term -> J; row not on the edit -> R',
           res9['Intro:135']['class'] == 'J' and res9b['Intro:135']['class'] == 'R',
           '%s / %s' % (res9['Intro:135']['class'], res9b['Intro:135']['class']))
    # T10 an unaccounted new line is U unless an edit's new string contains it
    r10 = cmp_of(lambda c: c.__setitem__('papers/Computation.md', 'Predicted 1.234 MeV, observed 1.230 MeV.\n\n'
                                         + c['papers/Computation.md']))
    k10 = [k for k in items_of(r10) if k.startswith('U:')]
    res10 = classify(r10, empty_edits, empty_cls, rows)
    report('T10 unaccounted new prediction line -> U, flagged',
           len(k10) == 1 and res10[k10[0]]['class'] == 'U' and res10[k10[0]]['scientific_evaluation'])
    # T11 VOID when a control fails, regardless of counts
    report('T11 failed control -> VOID', verdict_of(c0, False, True)[0] == 'VOID'
           and verdict_of(c0, True, False)[0] == 'VOID')
    print('self-test ' + ('PASS' if ok else 'FAIL'))
    return 0 if ok else 1


def main(argv):
    def opt(name):
        return argv[argv.index(name) + 1] if name in argv else None
    if not argv:
        print(__doc__)
        return 2
    if argv[0] == 'self-test':
        return self_test()
    if argv[0] == 'digests':
        print(json.dumps({'schema': 'a1exit-compare-frozen/1', 'pin': B.PIN, 'sha256': digests()},
                         indent=1, sort_keys=True))
        return 0
    if argv[0] == 'collect' and opt('--head') and opt('--out'):
        return collect(opt('--head'), opt('--out'))
    if argv[0] == 'verdict' and opt('--dir') and opt('--edits') and opt('--classify'):
        return verdict(opt('--dir'), opt('--edits'), opt('--classify'))
    if argv[0] == 'check-edits' and opt('--edits'):
        return check_edits(opt('--edits'), opt('--commit') or 'HEAD')
    print(__doc__)
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
