"""Generator of amendment 8 to design r6: applies the adopted wording of AMENDMENT-8.md (r2 at f10195d4, adopted at
DP-1, #1169 comment 7214186738) to DESIGN-r6.md, EXPECTATIONS.json and REQUIREMENTS.json, as generator-amendment1 to
generator-amendment6 did for their amendments.

Usage: python3 -I -B amend8.py DIR OUT

DIR holds DESIGN-r6.md, EXPECTATIONS.json and REQUIREMENTS.json as they are on `main` at 69d4d1c2 (each checked
against its sha256 below) and AMENDMENT-8.md as adopted (r2 at f10195d4, with its status paragraph corrected on
adoption; the generator reads only its appendix A). The script writes the three amended files into OUT.

What it applies:
- EXPECTATIONS.json: each of the 135 rows of appendix A's dropped list admits NOT RUN with the reason "outside the
  A1 path (amendment 8)" and the constant-false release check (R6.GATE.15; M8-3, M8-4). No row is removed, no other
  row changes, and no expected value changes.
- REQUIREMENTS.json: an owner_decision entry naming the M8 item on each requirement whose clause amendment 8
  changes (R6.STAT.1, R6.STAT.10, R6.GATE.10, R6.GATE.12, R6.GATE.15, R6.CTRL.3, R6.PLACE.8, R6.PLACE.11). No
  control is added or removed.
- DESIGN-r6.md: the title and R6.STAT.1 corrected (M8-15); sec. 0.8 quoting the decision; a sentence naming the M8
  item at each clause it changes; the trace-table cells of OBL-13, OBL-14, OBL-22, OBL-24 and OBL-26.

Self-checks: the dropped list read from appendix A has 135 ids, all rows, in the four stated categories with the
stated counts; no dropped row already carries not_run; every row outside the list is byte-identical in its JSON
form; every anchor occurs exactly once. Standard library only; deterministic.
"""
import collections
import hashlib
import json
import os
import re
import sys

BASE_SHA256 = {
    'DESIGN-r6.md': 'd6b4356d1e1cb419abfbf95c4c14f3f0ab8ff90a092ad3c4534256fddb556967',
    'EXPECTATIONS.json': 'b8d0522b56687be41f448742d129579a42f463a8a985a732c029ba95b1cc448f',
    'REQUIREMENTS.json': '735ee8488d86672896fd32b8c89b06892049f24a0c6cacaa8919c43573def2c1',
    'AMENDMENT-8.md': '4d17a2fdb88c9287d33a4c0c434096aeda888e884a59cf768ca70a52e73392a3',
}
REASON = 'outside the A1 path (amendment 8)'
# the gate's constant-false release check (control_gate.RC_FALSE), a fixed key of R6.GATE.15
RC_FALSE = 'false until an owner-approved expectation change replaces this entry'
RELEASE = ('an owner-approved expectation change reinstates the row, before a configuration other than A1 relies on '
           'the tool (amendment 8, M8-3)')
DECISION = ('owner decision DP-1 of 2026-11-27 (amaybaum, coordinating session; #1169 comment 7214186738): amendment 8 '
            'adopted at f10195d45b443fed1c8bcb8d5a5a2d9cb44ef14a')
COUNTS = {'mutant row': 107, 'gate self-test': 24, 'generality (SYN)': 3, 'purity (Z9)': 1}


def sha(b):
    return hashlib.sha256(b).hexdigest()


def once(text, old, new, what):
    n = text.count(old)
    if n != 1:
        raise SystemExit('anchor for %s occurs %d times' % (what, n))
    return text.replace(old, new)


def dumpj(doc):
    return (json.dumps(doc, indent=1, ensure_ascii=False) + '\n').encode('utf-8')


def dropped_list(amendment):
    """The dropped ids of appendix A, by category, read from the adopted text."""
    part = amendment.split('**Dropped rows (135)', 1)[1]
    out = collections.OrderedDict()
    for line in part.split('\n'):
        m = re.match(r'- (mutant row|gate self-test|generality \(SYN\)|purity \(Z9\)) \((\d+)\): (.*)$', line)
        if m:
            ids = re.findall(r'`([^`]+)`', m.group(3))
            if len(ids) != int(m.group(2)):
                raise SystemExit('%s: %d ids, stated %s' % (m.group(1), len(ids), m.group(2)))
            out[m.group(1)] = ids
    if {k: len(v) for k, v in out.items()} != COUNTS:
        raise SystemExit('dropped categories %r' % {k: len(v) for k, v in out.items()})
    return out


MARKS = [
    ('**R6.STAT.10**', 'M8-8', 'the implementation certification of OBL-26 is not a precondition of the tool\'s use '
     'in the A1 retirement and gates none of it.'),
    ('**R6.GATE.10**', 'M8-4', 'no mutation re-establishment gates the tool\'s landing; the `MUT:` rows admit NOT RUN '
     'with the reason "%s" (R6.GATE.15). The seven known survivors stay recorded as limitations.' % REASON),
    ('**R6.GATE.12**', 'M8-3', 'the landing gate covers the A1 path: the rows of appendix A of AMENDMENT-8.md that it '
     'drops admit NOT RUN with the reason "%s", and stay rows, so the correspondence in both directions is unchanged. '
     'A testable requirement without a control outside the kept rows is verified by review.' % REASON),
    ('**R6.GATE.15**', 'M8-3', 'the 135 rows of appendix A of AMENDMENT-8.md also admit NOT RUN, with the reason "%s" '
     'and the constant-false release check; where no runner records such a row, the gate records it NOT RUN with '
     'that reason. A record a runner makes for it is evaluated as for any row.' % REASON),
    ('**R6.CTRL.3**', 'M8-3', 'the both-directions scope is the kept rows of appendix A of AMENDMENT-8.md; each kept '
     'row keeps both its directions, the pair RT-T / RT-T0 included.'),
    ('**R6.PLACE.8**', 'M8-11', 'the landing paths also cover '
     '`verification/audits/foundations/a1exit-staging-amendment-20261126/` and '
     '`verification/audits/foundations/a1exit-adjudication-design-20261126/`.'),
    ('**R6.PLACE.11**', 'M8-4, M8-12', 'the local suite includes no mutation run and no mutation evidence is '
     're-established; the implementation review is a focused delta review of what changed since the last accepted '
     'head.'),
    ('**OBL-2**', 'M8-9', 'narrowed to "measured during design, not retained"; OBL-1\'s retained script and its seeded '
     'counts are the evidence.'),
    ('**OBL-6**', 'M8-9', 'discharged by OBL-3.'),
    ('**OBL-7**', 'M8-9', 'discharged by OBL-15.'),
    ('**OBL-10**', 'M8-14', 'the sentence "The amendment refers to no authority record, freeze ledger, comment form '
     'or automated authorization check." is removed; the pins and execution-identity sentences stay.'),
    ('**OBL-12**', 'M8-9', 'ESC-1 to ESC-4 are discharged by records re-derived on `main` at the final `H`: the allow '
     'root (ESC-1), the OBL-1 script (ESC-2), the configuration\'s scope record (ESC-3) and the hit classifications '
     'of OBL-15 (ESC-4); ESC-6 goes with the tool revision\'s README.'),
    ('**OBL-13**', 'M8-2', 'RT-L2 is recorded NOT RUN at the tool\'s landing and does not gate it. The drift check '
     'runs once, at the A1 retirement landing, on the real `M`, with the reconciliation records at `M` and RT-L. '
     'Gates: the A1 retirement landing.'),
    ('**OBL-14**', 'M8-2', 'RT-O9-L2 is recorded NOT RUN at the tool\'s landing and does not gate it; it is decided '
     'with RT-L2 at the A1 retirement landing. Gates: the A1 retirement landing.'),
    ('**OBL-20**', 'M8-3', 'the scope is the kept rows of appendix A of AMENDMENT-8.md.'),
    ('**OBL-22**', 'M8-7', 'the migration is not applied; identifiers stay as implemented, and MIGRATION.json stays as '
     'the index. Gates: none.'),
    ('**OBL-23**', 'M8-9', 'discharged by the representative-snapshot runs.'),
    ('**OBL-24**', 'M8-4', 'no mutation re-establishment gates the landing; the `MUT:` rows admit NOT RUN (R6.GATE.15) '
     'and the seven known survivors stay recorded as limitations. Gates: none.'),
    ('**OBL-25**', 'M8-3', 'the rows in scope are the kept rows of appendix A of AMENDMENT-8.md.'),
    ('**OBL-26**', 'M8-8', 'gates no part of the A1 retirement. Gates: none.'),
    ('**OBL-28**', 'M8-3, M8-4, M8-5, M8-6', 'C-1, C-3 and C-26 cover the kept rows of appendix A of AMENDMENT-8.md; '
     'C-28 is removed; C-7, C-11, C-12, C-14, C-15, C-22, C-23, C-24, RE-13, RE-18, RE-27 and RE-29 do not gate the '
     'landing; C-5 stays for every kept row; C-29 does not gate the landing (M8-2).'),
]

TABLE = [
    ('| OBL-13 | the tool\'s landing |', '| OBL-13 | the A1 retirement landing (amendment 8, M8-2) |'),
    ('| OBL-14 | the tool\'s landing |', '| OBL-14 | the A1 retirement landing (amendment 8, M8-2) |'),
    ('| OBL-22 | the tool\'s landing |', '| OBL-22 | none (amendment 8, M8-7) |'),
    ('| OBL-24 | the tool\'s landing |', '| OBL-24 | none (amendment 8, M8-4) |'),
    ('| OBL-26 | the implementation certification of the landed tool revision |',
     '| OBL-26 | none for the A1 retirement (amendment 8, M8-8) |'),
]

REQ_EFFECTS = {
    'R6.STAT.1': ('M8-15', 'r6 with amendments 1 to 7 confirmed as adopted; the status text corrected in place'),
    'R6.STAT.10': ('M8-8', 'the implementation certification (OBL-26) gates no part of the A1 retirement'),
    'R6.GATE.10': ('M8-4', 'no mutation re-establishment gates the landing; the MUT: rows admit NOT RUN'),
    'R6.GATE.12': ('M8-3', 'the landing gate covers the A1 path; dropped rows admit NOT RUN and stay rows'),
    'R6.GATE.15': ('M8-3', 'the 135 rows of appendix A admit NOT RUN with the reason "%s"' % REASON),
    'R6.CTRL.3': ('M8-3', 'the both-directions scope is the kept rows'),
    'R6.PLACE.8': ('M8-11', 'the landing paths also cover the staging amendment and adjudication design directories'),
    'R6.PLACE.11': ('M8-4, M8-12', 'no mutation run in the local suite; delta reviews replace full reviews'),
}

SEC = '''### 0.8 Amendment 8 of 2026-11-27

Owner decision DP-1 at #1169 comment 7214186738 (amaybaum, 2026-11-27T09:01:16Z, recorded by the coordinating
session); excerpt (each line prefixed by "> "; "[...]" marks text left out):

> Approved: DP-1 items 1–5.
>
> - Adopt Amendment 8 at f10195d45b443fed1c8bcb8d5a5a2d9cb44ef14a.
> - Confirm r6 with Amendments 1–7 as adopted and correct the stale status text.
>
> [...]

Amendment 8 (AMENDMENT-8.md of this directory) removes the obligations that do not gate A1 retirement, under the
owner's minimum-sufficient verification direction (#1169 comment 7213780573). Its items M8-1 to M8-15 are applied at
the clauses they name, each marked "Amendment 8 (sec. 0.8)". The landing gate covers the A1 path: of the 619 rows of
the expectation file it keeps 484, and the 135 rows of its appendix A (107 `MUT:` rows, 24 gate self-test rows, 3
R6.SYN rows and Z9e) admit NOT RUN with the reason "%s" under R6.GATE.15. No row is removed, no
expected value changes, and no requirement gains or loses a control. M8-1 (operational custody required only before
the first freeze of a discharge-bearing configuration) and M8-10 (the staging activation carried by the transition
descriptor that F's Record pins table pins) change the custody design and staging r2 as AMENDMENT-8.md states; the
tool's checks are unchanged by them. Retained rows fail closed as before.

''' % REASON


def main(base, out):
    raw = {}
    for name, digest in sorted(BASE_SHA256.items()):
        with open(os.path.join(base, name), 'rb') as f:
            raw[name] = f.read()
        if sha(raw[name]) != digest:
            raise SystemExit('%s: sha256 %s, expected %s' % (name, sha(raw[name]), digest))
    drop = dropped_list(raw['AMENDMENT-8.md'].decode('utf-8'))
    ids = [i for v in drop.values() for i in v]
    if len(set(ids)) != 135:
        raise SystemExit('dropped ids are not 135 distinct ids')

    exp = json.loads(raw['EXPECTATIONS.json'])
    before = {r['id']: json.dumps(r, sort_keys=True) for r in exp['rows']}
    if len(before) != 619 or not set(ids) <= set(before):
        raise SystemExit('dropped ids are not rows of the 619-row file')
    for r in exp['rows']:
        if r['id'] in set(ids):
            if 'not_run' in r:
                raise SystemExit('%s already carries not_run' % r['id'])
            allowed = list(r.get('status_allowed', ['PASS']))
            r['status_allowed'] = allowed + ['NOT RUN']
            r['not_run'] = {'reason': REASON, 'release_condition': RELEASE, 'release_check': RC_FALSE}
    for r in exp['rows']:
        if r['id'] not in set(ids) and json.dumps(r, sort_keys=True) != before[r['id']]:
            raise SystemExit('row %s changed' % r['id'])

    req = json.loads(raw['REQUIREMENTS.json'])
    byid = {q['id']: q for q in req}
    for rid, (item, effect) in sorted(REQ_EFFECTS.items()):
        byid[rid]['owner_decision'].append({'record': DECISION, 'decision': item, 'effect': effect,
                                            'decision_basis': ['AMENDMENT-8.md, %s' % item]})

    text = raw['DESIGN-r6.md'].decode('utf-8')
    text = once(text, '# Ledger coverage tool: design r6 (consolidated, self-contained; final draft for owner adoption, '
                'not adopted)', '# Ledger coverage tool: design r6 (consolidated, self-contained; adopted)', 'title')
    text = once(text, '**R6.STAT.1** Status: draft, not adopted. r6 is', '**R6.STAT.1** Status: adopted, with '
                'amendments 1 to 8 (owner decision DP-1 of 2026-11-27, #1169 comment 7214186738, sec. 0.8). r6 is',
                'R6.STAT.1 status')
    text = once(text, 'On its adoption by a recorded\nowner decision it supersedes design v6.0e and the amendments r4 '
                'and r5, which then become historical\nsources;', 'It supersedes design v6.0e and the amendments r4 '
                'and r5, which are historical\nsources;', 'R6.STAT.1 supersession')
    text = once(text, ' r6 adopts nothing before that decision, and changes no design, implementation,\ncontrol '
                'expectation or exception in force.\n', '\n', 'R6.STAT.1 tail')
    lines = text.split('\n')
    for anchor, item, body in MARKS:
        at = [k for k, l in enumerate(lines) if l.startswith(anchor)]
        if len(at) != 1:
            raise SystemExit('anchor %s occurs %d times' % (anchor, len(at)))
        j = at[0] + 1
        while not (lines[j].startswith('Sources') or lines[j].startswith('**') or lines[j].startswith('#')
                   or lines[j].startswith('Gates: the tool\'s landing. Discharged by: each row\'s control')):
            j += 1
        while j > at[0] + 1 and lines[j - 1] == '':
            j -= 1
        lines.insert(j, 'Amendment 8 (sec. 0.8), %s: %s' % (item, body))
    text = '\n'.join(lines)
    for old, new in TABLE:
        text = once(text, old, new, old)
    text = once(text, '***\n\n## 1. Notation and symbols', SEC + '***\n\n## 1. Notation and symbols', 'sec. 0.8')

    os.makedirs(out, exist_ok=True)
    for name, data in (('DESIGN-r6.md', text.encode('utf-8')), ('EXPECTATIONS.json', dumpj(exp)),
                       ('REQUIREMENTS.json', dumpj(req))):
        with open(os.path.join(out, name), 'wb') as f:
            f.write(data)
    print('dropped', {k: len(v) for k, v in drop.items()}, 'marks', len(MARKS), 'requirements', len(REQ_EFFECTS))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
