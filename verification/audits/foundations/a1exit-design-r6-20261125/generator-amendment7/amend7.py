"""Generator of amendment 7 to design r6: applies the adopted wording and cases of AMENDMENT-7.md (adopted at r4,
fbfeac8a, with every-configuration binding for an unresolvable configuration; owner decision, amaybaum,
2026-11-27T03:17:51Z, #1169 comment 7208869709) to DESIGN-r6.md, EXPECTATIONS.json and REQUIREMENTS.json, as
generator-amendment1 to generator-amendment6 did for their amendments.

Usage: python3 -I -B amend7.py DIR OUT

Amendment 7 was adopted before amendment 8, but its generator runs after generator-amendment8 and
generator-amendment9. DIR therefore holds DESIGN-r6.md and REQUIREMENTS.json as generator-amendment8 leaves them,
EXPECTATIONS.json as generator-amendment9 leaves it, and AMENDMENT-7.md as landed on `main` by PR #1618 (each checked
against its sha256 below). The script writes the three amended files into OUT. The chain from `main` at 69d4d1c2 is
amend8.py, then amend9.py, then this script; the earlier generators' pins are unchanged.

What it applies, every text read from AMENDMENT-7.md:
- DESIGN-r6.md: the four replacements of sec. 2 and sec. 3 (R6.RECON.26 body, Form of a finding (iv) and (v);
  R6.RECON.27 Keys), each located once with its line breaks ignored, the unchanged words kept as they stand; the
  Sources lines of R6.RECON.26 and R6.RECON.27 name amendment 7; sec. 0.9 quotes the decision.
- EXPECTATIONS.json (sec. 4): the cases of the two control tables, appended in table order to FINDING-FORM (sec. 2:
  1 to 10, 8b, C1 to C3), FINDING-KEYS, FINDING-LINEAGE and REASSESS-KEYS (sec. 3, by its Row column), each named
  "amendment 7, sec. N, case K: <case>"; the case texts of FINDING-KEYS case 3, FINDING-LINEAGE case 5 and
  FINDING-LINEAGE countercase 8 as sec. 3's table of effects states. No outcome of an existing case changes, and no
  row is added or removed.
- REQUIREMENTS.json: an owner_decision entry for amendment 7 on R6.RECON.26 and R6.RECON.27; no control changes.

The new cases correspond to local controls the tool already carries (obl29_controls.py: A7-I-*, A7-II-*,
N-PREPEND, SECOND-KIND-REVIEWED-MISSING; custody_controls.py: A7-KEYS-*); registering a runner for the rows is not
part of this change.

Self-checks: the input sha256 pins; 14 cases in sec. 2 and 12 in sec. 3, each outcome one of the stated forms; every
anchor occurs exactly once; every row other than the four is byte-identical in its JSON form; in the four, the
existing cases keep their order and every field but the three stated case texts; case names are unique within a
row; only the two requirements change, and their controls do not. Standard library only; deterministic.
"""
import copy
import hashlib
import json
import os
import re
import sys

BASE_SHA256 = {
    'DESIGN-r6.md': '06f5639f9b456f2b21277b2f1da591b0022f90bb6e80cbd8ebbead28b6bac3d3',
    'EXPECTATIONS.json': '0c6f3fed91b888ae4343539142488a55301adc1f462f0a6b7a07b6a1038adc81',
    'REQUIREMENTS.json': '4c0b0a69ef040c81dd2f942b4f4b3bb8e7920e7e2dfe68aad2561570ade3fdc5',
    'AMENDMENT-7.md': '5fa4be0a63b997967f5ed268bc91449b3162b6a856294f16cd1cd148029f7b9d',
}
ROWS = ('FINDING-FORM', 'FINDING-KEYS', 'FINDING-LINEAGE', 'REASSESS-KEYS')
REQS = ('R6.RECON.26', 'R6.RECON.27')

BLOCKED = {'outcome': 'FAIL', 'classes_include': ['retirement-blocked']}
BLOCKED_INV = {'outcome': 'FAIL', 'classes_include': ['retirement-blocked', 'record-invalid']}
NOT_BLOCKED = {'outcome': 'ANY', 'invariants': [{'not_class': ['retirement-blocked']}]}
# each outcome cell of the two tables: (expectation, the part of the cell the expectation's fields do not carry,
# appended to the case name in parentheses)
OUTCOMES = {
    'FAIL, `retirement-blocked` and `record-invalid`': (BLOCKED_INV, None),
    'FAIL, `retirement-blocked`': (BLOCKED, None),
    'FAIL, run-level `retirement-blocked`; no ERROR': (BLOCKED, 'run-level retirement-blocked; no ERROR'),
    'FAIL, run-level `retirement-blocked` and `record-invalid`; no ERROR':
        (BLOCKED_INV, 'run-level retirement-blocked; no ERROR'),
    'ANY, not `retirement-blocked`': (NOT_BLOCKED, None),
    'FAIL, `base-drift`, RC1 failing; not `retirement-blocked`, not `record-invalid` (RECON-FIELDS countercase 2, '
    'unchanged)': ({'outcome': 'FAIL', 'classes_include': ['base-drift'],
                    'invariants': [{'failed_conditions_include': 'RC1'},
                                   {'not_class': ['retirement-blocked', 'record-invalid']}]},
                   'RECON-FIELDS countercase 2, unchanged'),
    'FAIL, run-level `retirement-blocked` naming the finding, and `record-invalid`':
        (BLOCKED_INV, 'run-level retirement-blocked naming the finding'),
    'FAIL, run-level `retirement-blocked`': (BLOCKED, 'run-level retirement-blocked'),
    'FAIL; `category3.blocked` holds an entry for `E1` and a run-level entry with `edit` null for the finding':
        ({'outcome': 'FAIL'}, 'category3.blocked holds an entry for E1 and a run-level entry with edit null for the '
                              'finding'),
    'FAIL, run-level `retirement-blocked` and `record-invalid`': (BLOCKED_INV, 'run-level retirement-blocked'),
    'FAIL, run-level `retirement-blocked` (the target match does not keep it below run level)':
        (BLOCKED, 'run-level retirement-blocked; the target match does not keep it below run level'),
    'FAIL, `retirement-blocked` on `E1`': (BLOCKED, 'retirement-blocked on E1'),
    'FAIL, run-level `retirement-blocked` (an edit reassessment does not lift the run-level binding); the expected '
    'classes omit `record-invalid` by design, since under the amended Keys a non-null `edit` for an edit of the citing '
    'configuration is well formed and the reassessment applies, lifting nothing':
        (BLOCKED, 'run-level retirement-blocked; an edit reassessment does not lift the run-level binding'),
}
# sec. 3, "Effect on existing controls, gap (ii)": (row, the case as it stands, the case as amended)
TEXTS = [
    ('FINDING-KEYS',
     'an element whose id is absent from the named configuration\'s ledger: the fallback binds every configuration '
     'carrying the id, a migrated id or the target',
     'an element whose id is absent from the named configuration\'s ledger: the fallback binds every configuration '
     'carrying the id, a migrated id or the target, and binds the lineage at run level'),
    ('FINDING-LINEAGE',
     'a finding naming no configuration, or one that cannot be read: it binds every configuration whose ledger carries '
     'the edit by id, a migrated id or the target, the other retirement\'s id collision included',
     'a finding naming no configuration, or one that cannot be read: it binds every configuration whose ledger carries '
     'the edit by id, a migrated id or the target, the other retirement\'s id collision included, and every '
     'configuration at run level'),
    ('FINDING-LINEAGE',
     'countercase: the other retirement bound only by the fallback\'s id collision, frozen anew with the colliding id '
     'renamed under a recorded migration, its target different (positive)',
     'countercase: the other retirement bound only by the fallback\'s id collision, the finding naming a readable '
     'configuration with which an element differs, frozen anew with the colliding id renamed under a recorded '
     'migration, its target different (positive)'),
]
DECISION = ('owner decision of 2026-11-27 (amaybaum, coordinating session; #1169 comment 7208869709): amendment 7 '
            'adopted at fbfeac8ae3a7914255e07d9a0351eff4bd1d1474, with every-configuration binding')
REQ_EFFECTS = {
    'R6.RECON.26': ('amendment 7, gaps (i) and (ii)',
                    'side_change_commits limit the runs a finding blocks only when every element passes the scope '
                    'test, otherwise the finding blocks every run in which it is found; an element whose id is no edit '
                    'of the named configuration, or an unresolvable configuration, also binds at run level',
                    ['AMENDMENT-7.md, sec. 2', 'AMENDMENT-7.md, sec. 3']),
    'R6.RECON.27': ('amendment 7, gap (ii)',
                    'edit is null only when the finding binds the citing configuration at run level; a null-edit '
                    'reassessment lifts that binding only',
                    ['AMENDMENT-7.md, sec. 3']),
}
SOURCES = [
    ('amendment 6 (#1169 comment 7187418279; PR #1593 comment 7189446310). Controls: RECON-BLOCK, BLOCK-KEY, '
     'FINDING-FORM, FINDING-LINEAGE, FINDING-KEYS.',
     'amendment 6 (#1169 comment 7187418279; PR #1593 comment 7189446310); amendment 7 (#1169 comment 7208869709). '
     'Controls: RECON-BLOCK, BLOCK-KEY, FINDING-FORM, FINDING-LINEAGE, FINDING-KEYS.'),
    ('Sources: amendment 4 (#1169 comment 7185562871). Controls: BLOCK-KEY, REASSESS-FORM, REASSESS-KEYS.',
     'Sources: amendment 4 (#1169 comment 7185562871); amendment 7 (#1169 comment 7208869709). Controls: BLOCK-KEY, '
     'REASSESS-FORM, REASSESS-KEYS.'),
]
SEC = '''### 0.9 Amendment 7 of 2026-11-27

Owner decision at #1169 comment 7208869709 (amaybaum, 2026-11-27T03:17:51Z, recorded by the coordinating session);
excerpt of its first item (each line prefixed by "> "; "[...]" marks text left out):

> Approved:
>
> * Adopt r9 Amendment 1 at `e79e7ca9`, the S11-2a supplement at `6de7efa4`, and r13 Amendment 7 at `fbfeac8a`, with every-configuration binding.
>
> [...]

Amendment 7 (AMENDMENT-7.md of this directory, adopted at fbfeac8ae3a7914255e07d9a0351eff4bd1d1474) closes two
cases in which a recorded category-3 finding bound nothing: an entry whose `side_change_commits` cannot limit the
runs the finding blocks (R6.RECON.26, body), and an `invalidated` element whose `id` is no edit of the named
configuration, or a `configuration` that cannot be resolved (R6.RECON.26, Form of a finding (iv) and (v); R6.RECON.27,
Keys). Its wording uses `R*` (R6.OBL29.3) and residual R-1 of the OBL-29 remedy r9 and its Amendment 1, adopted by
the same decision. Its cases are added to FINDING-FORM, FINDING-KEYS, FINDING-LINEAGE and REASSESS-KEYS. No outcome
of an existing case changes, no row is added or removed, and no requirement gains or loses a control.

'''


def sha(b):
    return hashlib.sha256(b).hexdigest()


def once(text, old, new, what):
    n = text.count(old)
    if n != 1:
        raise SystemExit('anchor for %s occurs %d times' % (what, n))
    return text.replace(old, new)


def dumpj(doc):
    return (json.dumps(doc, indent=1, ensure_ascii=False) + '\n').encode('utf-8')


def replacements(amendment):
    """The (current, replacement) pairs of the adopted wording, in order: each is the blockquote after a line starting
    'Current' and the blockquote after the next line starting 'Replacement'."""
    lines = amendment.split('\n')
    pairs, cur = [], None
    for k, ln in enumerate(lines):
        if ln.startswith('Current') or ln.startswith('Replacement'):
            j = k + 1
            while lines[j] == '':
                j += 1
            quote = []
            while j < len(lines) and lines[j].startswith('> '):
                quote.append(lines[j][2:])
                j += 1
            if len(quote) != 1:
                raise SystemExit('the quote after %r is not one line' % ln)
            if ln.startswith('Current'):
                if cur is not None:
                    raise SystemExit('two Current quotes without a Replacement')
                cur = quote[0]
            else:
                if cur is None:
                    raise SystemExit('a Replacement quote without a Current')
                pairs.append((cur, quote[0]))
                cur = None
    if len(pairs) != 4 or cur is not None:
        raise SystemExit('%d replacement pairs, expected 4' % len(pairs))
    return pairs


def apply_wording(text, cur, rep):
    """Replace `cur`, found once in `text` with its whitespace ignored, by `rep`: the words common to the start and the
    end of both stay as they stand in `text` (line breaks included); only the differing words change."""
    words = cur.split()
    hits = list(re.finditer(r'\s+'.join(re.escape(w) for w in words), text))
    if len(hits) != 1:
        raise SystemExit('the current wording %r... occurs %d times' % (cur[:60], len(hits)))
    m = hits[0]
    toks = [(m.start() + t.start(), m.start() + t.end()) for t in re.finditer(r'\S+', m.group(0))]
    new = rep.split()
    if len(toks) != len(words):
        raise SystemExit('tokenization')
    p = 0
    while p < min(len(words), len(new)) and words[p] == new[p]:
        p += 1
    s = 0
    while s < min(len(words), len(new)) - p and words[-1 - s] == new[-1 - s]:
        s += 1
    mid_old, mid_new = words[p:len(words) - s], new[p:len(new) - s]
    if not mid_new:
        raise SystemExit('a replacement that only removes words')
    ins = ' '.join(mid_new)
    if mid_old:
        a, b = toks[p][0], toks[len(words) - s - 1][1]
        return text[:a] + ins + text[b:]
    if p:
        a = toks[p - 1][1]
        return text[:a] + ' ' + ins + text[a:]
    a = toks[0][0]
    return text[:a] + ins + ' ' + text[a:]


def tables(amendment):
    """The control tables: sec. 2 (# | Case | Outcome) to FINDING-FORM, sec. 3 (# | Row | Case | Outcome)."""
    out = []
    sec = None
    for ln in amendment.split('\n'):
        if ln.startswith('## 2.'):
            sec = 2
        elif ln.startswith('## 3.'):
            sec = 3
        elif ln.startswith('## '):
            sec = None
        if sec is None or not ln.startswith('| '):
            continue
        cells = [x.strip() for x in ln.strip().strip('|').split(' | ')]
        if not re.fullmatch(r'[0-9]+b?|C[0-9]+', cells[0]):
            continue
        if sec == 2 and len(cells) == 3:
            out.append((2, cells[0], 'FINDING-FORM', cells[1], cells[2]))
        elif sec == 3 and len(cells) == 4 and cells[1] in ROWS:
            out.append((3, cells[0], cells[1], cells[2], cells[3]))
    n2 = [c for c in out if c[0] == 2]
    n3 = [c for c in out if c[0] == 3]
    if len(n2) != 14 or len(n3) != 12:
        raise SystemExit('cases: %d in sec. 2, %d in sec. 3' % (len(n2), len(n3)))
    return out


def new_case(sec, num, case, outcome):
    if outcome not in OUTCOMES:
        raise SystemExit('outcome %r of case %s is not a stated form' % (outcome, num))
    exp, note = OUTCOMES[outcome]
    name = 'amendment 7, sec. %d, case %s: %s' % (sec, num, case.replace('`', ''))
    if note:
        name += ' (%s)' % note
    return dict(case=name, **copy.deepcopy(exp))


def main(base, out):
    raw = {}
    for name, digest in sorted(BASE_SHA256.items()):
        with open(os.path.join(base, name), 'rb') as f:
            raw[name] = f.read()
        if sha(raw[name]) != digest:
            raise SystemExit('%s: sha256 %s, expected %s' % (name, sha(raw[name]), digest))
    amendment = raw['AMENDMENT-7.md'].decode('utf-8')

    # EXPECTATIONS.json
    exp = json.loads(raw['EXPECTATIONS.json'])
    before = {r['id']: json.dumps(r, sort_keys=True) for r in exp['rows']}
    by = {r['id']: r for r in exp['rows']}
    old_cases = {rid: copy.deepcopy(by[rid]['expect']['cases']) for rid in ROWS}
    for rid, old, new in TEXTS:
        hits = [c for c in by[rid]['expect']['cases'] if c['case'] == old]
        if len(hits) != 1:
            raise SystemExit('%s: the case %r... occurs %d times' % (rid, old[:50], len(hits)))
        hits[0]['case'] = new
    added = {rid: 0 for rid in ROWS}
    for sec, num, rid, case, outcome in tables(amendment):
        by[rid]['expect']['cases'].append(new_case(sec, num, case, outcome))
        added[rid] += 1
    if added != {'FINDING-FORM': 14, 'FINDING-KEYS': 8, 'FINDING-LINEAGE': 1, 'REASSESS-KEYS': 3}:
        raise SystemExit('added cases %r' % added)
    renamed = {(rid, new) for rid, _old, new in TEXTS}
    for r in exp['rows']:
        if r['id'] not in ROWS:
            if json.dumps(r, sort_keys=True) != before[r['id']]:
                raise SystemExit('row %s changed' % r['id'])
            continue
        cases = r['expect']['cases']
        names = [c['case'] for c in cases]
        if len(set(names)) != len(names):
            raise SystemExit('%s: repeated case name' % r['id'])
        for o, n in zip(old_cases[r['id']], cases):
            if (r['id'], n['case']) not in renamed and o != n:
                raise SystemExit('%s: an existing case changed' % r['id'])
            if {k: v for k, v in o.items() if k != 'case'} != {k: v for k, v in n.items() if k != 'case'}:
                raise SystemExit('%s: an existing outcome changed' % r['id'])
        rest = copy.deepcopy(r)
        rest['expect'] = dict(rest['expect'], cases=None)
        orig = json.loads(before[r['id']])
        orig['expect'] = dict(orig['expect'], cases=None)
        if rest != orig:
            raise SystemExit('%s: a field other than its cases changed' % r['id'])

    # REQUIREMENTS.json
    req = json.loads(raw['REQUIREMENTS.json'])
    rbefore = {q['id']: json.dumps(q, sort_keys=True) for q in req}
    for q in req:
        if q['id'] in REQ_EFFECTS:
            item, effect, basis = REQ_EFFECTS[q['id']]
            q['owner_decision'].append({'record': DECISION, 'decision': item, 'effect': effect,
                                        'decision_basis': list(basis)})
    for q in req:
        old = json.loads(rbefore[q['id']])
        if q['id'] not in REQS and q != old:
            raise SystemExit('requirement %s changed' % q['id'])
        if q['controls'] != old['controls']:
            raise SystemExit('requirement %s: controls changed' % q['id'])

    # DESIGN-r6.md
    text = raw['DESIGN-r6.md'].decode('utf-8')
    for cur, rep in replacements(amendment):
        text = apply_wording(text, cur, rep)
    for old, new in SOURCES:
        text = once(text, old, new, old[:40])
    text = once(text, '***\n\n## 1. Notation and symbols', SEC + '***\n\n## 1. Notation and symbols', 'sec. 0.9')

    os.makedirs(out, exist_ok=True)
    for name, data in (('DESIGN-r6.md', text.encode('utf-8')), ('EXPECTATIONS.json', dumpj(exp)),
                       ('REQUIREMENTS.json', dumpj(req))):
        with open(os.path.join(out, name), 'wb') as f:
            f.write(data)
    print('cases added', added, 'case texts', len(TEXTS), 'requirements', len(REQ_EFFECTS))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
