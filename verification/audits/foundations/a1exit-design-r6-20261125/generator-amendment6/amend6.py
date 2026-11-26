"""Generator of amendment 6 to design r6: four schema ambiguities of category 3 and one expectation conflict, raised by
the tool writer while implementing amendment 4 (owner direction of 2026-11-26, #1169 comment 7187418279, item 4).

Usage: python3 -I -B amend6.py BASE OUT

BASE holds DESIGN-r6.md, EXPECTATIONS.json, REQUIREMENTS.json and LANDING-MANIFEST.md as amendment 5 leaves them
(each checked against its sha256 below). The script reads owner-decisions-amendment6.json beside itself and writes
into OUT the amended DESIGN-r6.md, EXPECTATIONS.json and REQUIREMENTS.json, the change record AMENDMENT-6.md and the
updated LANDING-MANIFEST.md. Every recommendation is a proposal for the owner's decision at adoption.

Self-checks: no existing row changes except RECON-BLOCK, whose cases keep their outcomes and gain one; no requirement
loses a control or changes a field other than its controls and pending entries; every new row records both
directions; correspondence; the closed invariant vocabulary; the amendment-6 mark on every touched requirement.
Standard library only; deterministic.
"""
import copy
import hashlib
import json
import os
import re
import sys

BASE_SHA256 = {
    'DESIGN-r6.md': 'b643294b0ff8b82c511d5fcb77d00b72cd690e5d2d9b08480cfaa7da875a8c5b',
    'EXPECTATIONS.json': 'eb187360fa61ee30be94c2d66e0b1144463dc3f6b7d3cfbab91b10299436284c',
    'REQUIREMENTS.json': 'd59a2f514ffa95b6da363356190406939e5b105d268ae6e00f96f75462e59597',
    'LANDING-MANIFEST.md': 'a8890c2860b3a25d79fda60b733d9cc78d55c600f0ea48fb67b31a9614dc12bf',
}
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = 'r6 amendment 6 (owner direction of 2026-11-26, #1169 comment 7187418279, item 4; tool writer\'s points 1 to 5)'
FLAG = 'added by amendment 6 (a proposal); no runner records it before the tool revision implements it'
MARK = '(amendment 6, sec. 0.7: proposal, pending independent review and the owner\'s decision)'
PENDING = ('amendment 6 (category-3 schema resolutions): a proposal under the owner\'s direction of 2026-11-26 (#1169 '
           'comment 7187418279, item 4); needs independent review and the owner\'s decision at adoption')
BLOCKED = {'outcome': 'FAIL', 'classes_include': ['retirement-blocked']}
BLOCKED_INV = {'outcome': 'FAIL', 'classes_include': ['retirement-blocked', 'record-invalid']}
NOT_BLOCKED = {'outcome': 'ANY', 'invariants': [{'not_class': ['retirement-blocked']}]}


def sha(b):
    return hashlib.sha256(b).hexdigest()


def once(text, old, new, what):
    c = text.count(old)
    if c != 1:
        raise SystemExit('anchor for %s occurs %d times' % (what, c))
    return text.replace(old, new)


def dumpj(doc):
    return (json.dumps(doc, indent=1, ensure_ascii=False) + '\n').encode('utf-8')


def c(case, base):
    return dict(case=case, **copy.deepcopy(base))


def row(rid, req, cases, case):
    r = {'id': rid, 'requirements': req, 'runner': None, 'operations': ['execution'], 'direction': 'both',
         'expect': {'cases': cases}, 'source': SRC, 'flags': [FLAG]}
    return r, case


ROWS = [
    row('FINDING-FORM', ['R6.RECON.26', 'R6.REC.2'], [
        c('a writer\'s verdict no-effect and a non-author review whose verdict on the item <path>:scientific_effect is '
          'invalidates with a well-formed invalidated list, the review passing review-record lint', BLOCKED),
        c('the same review: the reviewed entry fails its own chain lint and does not apply, and the review stays valid',
          {'outcome': 'FAIL', 'classes_include': ['retirement-blocked', 'base-drift'],
           'invariants': [{'none': 'items[class=record-invalid,subject=$review]'}]}),
        c('a review verdict invalidates with an empty invalidated list (blocks every edit the entry\'s conclusions '
          'name, or every edit of the path)', BLOCKED_INV),
        c('a review verdict accept carrying an invalidated list', BLOCKED_INV),
        c('countercase: a review verdict reject without invalidated on the scientific_effect item (the path is not '
          'reconciled and is not blocked)', {'outcome': 'FAIL', 'classes_include': ['base-drift'],
                                             'invariants': [{'not_class': ['retirement-blocked']}]})],
     'point 1: a review-record finding is the verdict invalidates with invalidated on the scientific_effect item; '
     'review-record lint is separate from the reviewed record\'s chain lint; a malformed finding blocks'),
    row('FINDING-LINEAGE', ['R6.RECON.26'], [
        c('a finding naming its configuration; a later configuration on that configuration\'s supersedes chain carries '
          'the edit', BLOCKED),
        c('countercase: a configuration of another retirement, outside the lineage, whose ledger reuses the edit id '
          '(positive)', NOT_BLOCKED),
        c('a finding naming no configuration, or one that cannot be read: it binds every configuration whose ledger '
          'carries the edit, the other retirement\'s included', BLOCKED_INV)],
     'point 2: the finding names its configuration; the lineage is computed from it; a finding without one binds '
     'every configuration carrying the edit'),
    row('FINDING-KEYS', ['R6.RECON.26', 'R6.RECON.25'], [
        c('an invalidated element {id, sha256, target: {path, start_H, old_sha256}} matching the ledger splice of that '
          'id at H', BLOCKED),
        c('an element whose target differs from the ledger splice of its id (form failure; the id still blocks)',
          BLOCKED_INV),
        c('an element {id, sha256} without target (form failure; the id still blocks)', BLOCKED_INV),
        c('countercase: a revised configuration keeping only an edit of the same path that no finding names, without a '
          'reassessment (positive)', NOT_BLOCKED)],
     'point 4: the key names of an invalidated element; a malformed element still blocks its id'),
    row('MIGRATION-RECORD', ['R6.RECON.28', 'R6.CFG.4'], [
        c('an edit renamed, its old bytes also rewritten, under a reviewed edit-id migration record that the '
          'configuration references with kind edit-id-migration', BLOCKED),
        c('the same migration record referenced only by an earlier configuration on the supersedes chain', BLOCKED),
        c('a migration record that fails record lint, the renamed edit\'s old bytes unchanged (the path-and-old-bytes '
          'match still applies)', BLOCKED_INV),
        c('countercase: a configuration that removes the renamed edit (neither its old id, its new id nor its old '
          'bytes remain) (positive)', NOT_BLOCKED)],
     'point 3: where a recorded migration lives; a migration never lifts a block'),
]
NEW_IDS = [r['id'] for r, _ in ROWS]
REQ_CONTROLS = {}
for _r, _ in ROWS:
    for _q in _r['requirements']:
        REQ_CONTROLS.setdefault(_q, []).append(_r['id'])
NEW_REQS = ['R6.RECON.28']
TOUCHED = ['R6.RECON.26', 'R6.RECON.25', 'R6.REC.2', 'R6.CFG.4']

RECON_BLOCK_OLD = ('countercase: the run under a revised plan, a new configuration whose ledger changes the invalidated '
                   'edit\'s edit-list entry (positive)')
RECON_BLOCK_NEW = ('countercase: the run under a revised plan, a new configuration whose ledger changes the invalidated '
                   'edit\'s edit-list entry and whose freeze cites an applying reassessment naming the finding '
                   '(R6.RECON.27) (positive)')
RECON_BLOCK_ADDED = {'case': 'a revised plan whose ledger changes the invalidated edit\'s edit-list entry (a wording '
                             'change, the same id and target) and cites no reassessment', 'outcome': 'FAIL',
                     'classes_include': ['retirement-blocked']}

FORM = '''

**Form of a finding** %(mark)s. (i) A finding of the second kind is a verdict entry, in a review
record, on the item `<path>:scientific_effect` whose verdict value is `invalidates` (a value that `oi-review-record/1`
permits on that item only, R6.REC.2) and which carries a non-empty `invalidated`. The review record that carries it must
pass review-record lint: the checks of R6.REC.6 that concern the review as a record (schema and fields; a `reviewer`
other than the reviewed record's `author`, and not a run, check or Issue; `reviewed` naming exactly one record blob,
present where the scan of this requirement finds the review; verdicts covering every item id of the reviewed record,
without duplicates). Its verdict `invalidates` makes the reviewed record fail its own chain lint (R6.REC.6) and not
apply; it does not make the review invalid. A verdict entry on a `scientific_effect` item that carries `invalidated`
with any other verdict value, or the verdict `invalidates` with an empty or malformed `invalidated`, is a form failure,
FAIL `record-invalid`, and counts as a finding over every edit the entry's `conclusions` name, or, if they name none,
over every edit of the path: a malformed finding blocks rather than lapses. (ii) Each element of `invalidated`, in an
entry's `scientific_effect` or in a review verdict, is `{id, sha256, target: {path, start_H, old_sha256}}`: `id` names a
splice of the ledger of the configuration named in (iii); `sha256` is the canonical sha256 of that edit's edit-list
entry; `target` copies that splice's file, start and `old_sha256` at `H`. An element that differs from the ledger, or
lacks a key, is a form failure, FAIL `record-invalid`, and still blocks the id it names. (iii) Every finding names
`configuration`, the `{path, blob_sha256}` of the configuration under which it was made: the entry's
`scientific_effect` carries it for the first kind, the review verdict entry for the second. The plan lineage of the
block is computed from it. A finding whose `configuration` is absent or cannot be read is a form failure, FAIL
`record-invalid`, and binds every configuration whose ledger carries one of its edits, whatever its retirement. (iv)
The migrations the edit-id match follows are those of R6.RECON.28.'''

NEW_REQ = '''
**R6.RECON.28** **Edit-id migration record** %(mark)s. A rename of a ledger edit id under AGENTS.md
sec. A.48 item 3 is recorded for the tool in a reviewed, immutable record of schema `oi-edit-id-migration/1`, under the
ownership chain of sec. 11: `migrations`, a list of `{old, new}` edit ids, and `approval`, the owner's recorded approval
quoted with its author and time. A configuration that carries a renamed edit references the record in `records` with
kind `edit-id-migration` (R6.CFG.4). For R6.RECON.26 the tool maps a finding's edit id through every such record that
the configuration, or a configuration on its `supersedes` chain, references, transitively. A record that fails record
lint is FAIL `record-invalid` and maps nothing. A migration record never lifts a block: the path-and-old-bytes match of
R6.RECON.26 applies whether or not a migration is recorded, and a mapping only adds edits the block binds.
Sources: %(src)s. Controls: MIGRATION-RECORD.
'''

POINTS = [
    ('1. A review-record finding (R6.RECON.26, second kind)',
     ['(a) The verdict entry on `<path>:scientific_effect` counts as a finding whenever it carries a non-empty '
      '`invalidated`, whatever its verdict value. Safe against loss, but it makes an `accept` that also lists '
      '`invalidated` ambiguous.',
      '(b) A dedicated verdict value, `invalidates`, plus `invalidated`. Unambiguous. Using `reject` instead would overload '
      'a value that also means "wrong for other reasons", so a plain rejection could not be told from a finding.'],
     'Proposal: (b) with the value `invalidates`, permitted on `scientific_effect` items only. Review-record lint (the '
     'review as a record) is separate from the reviewed record\'s chain lint: the finding makes the reviewed record not '
     'apply, while the review stays valid. Any `invalidated` with another value, or `invalidates` with an empty or '
     'malformed list, is a form failure that still blocks (over the edits the entry\'s conclusions name, or every edit '
     'of the path), so no form error can lose a finding. Reasoning: R6.RECON.26 already says the review "finds that the '
     'change invalidates", and R6.REC.6 makes every non-`accept` verdict a failure of the reviewed record, so a separate '
     'value fits both without changing R6.REC.6.',
     'FINDING-FORM'),
    ('2. Lineage scope',
     ['(a) Bind every configuration whose ledger carries the edit. Never loses a block, but over-blocks another '
      'retirement that reuses the edit id.',
      '(b) The finding names the configuration it was made under, `{path, blob_sha256}`; the lineage of amendment 4 is '
      'computed from it.'],
     'Proposal: (b), with (a) as the fail-closed fallback: a finding without a readable `configuration` is a form '
     'failure and binds every configuration carrying its edits. Reasoning: amendment 4 defines the lineage from "the '
     'configuration the finding was made under", which only (b) makes readable from git objects; the fallback keeps '
     'the owner\'s rule that a finding cannot be lost.',
     'FINDING-LINEAGE'),
    ('3. Where a recorded migration lives',
     ['(a) No location: only the path-and-old-bytes match is implementable. The owner\'s row "Block follows the recorded '
      'migration" would then rest on the mechanical match alone, and a rename that also rewrites the old bytes would '
      'escape it.',
      '(b) A reviewed record `oi-edit-id-migration/1`, referenced by the configuration with kind `edit-id-migration`, '
      'followed through the `supersedes` chain.'],
     'Proposal: (b), with the mechanical match kept in addition, so a missing or invalid migration record can never '
     'lift a block; a mapping only adds edits. Reasoning: AGENTS.md sec. A.48 item 3 requires the migration to be '
     'recorded and approved; reading it from the configuration\'s references keeps it pinned at the freeze.',
     'MIGRATION-RECORD'),
    ('4. Key names inside `invalidated`',
     ['(a) `{id, sha256}` as the amendment-3 code reads: loses the target that amendment 4 requires for the '
      'path-and-old-bytes match.',
      '(b) The writer\'s proposal `{id, sha256, target: {path, start_H, old_sha256}}`, the target copied from the ledger '
      'splice of the same id at `H`.'],
     'Proposal: (b). Each splice id of the retirement ledger is unique (399 splices, no repeated id), so one target per '
     'id suffices. A mismatch or a missing key is a form failure that still blocks the id.',
     'FINDING-KEYS'),
    ('5. RECON-BLOCK versus amendment 4',
     ['The RECON-BLOCK countercase expected no block for a revised plan that only changes the edit\'s entry; amendment 4 '
      'keeps the block for a wording change unless the freeze cites an applying reassessment.'],
     'Correction: the RECON-BLOCK countercase now requires the cited reassessment naming the finding, and a case is '
     'added in which a wording change without a reassessment stays blocked. This follows R6.RECON.26 as amended by '
     'amendment 4, which governs over Table 17.1.',
     'RECON-BLOCK'),
]


def note(owner):
    d = owner['decisions'][0]
    out = ['', '### 0.7 Amendment 6 of 2026-11-26', '',
           'Owner direction at %s (%s, %s, relayed by the %s); excerpt of item 4 (each line prefixed by "> "; "[...]" '
           'marks text left out):' % (d['record'], d['author'], d['time'], d['relayed_by']), '',
           '\n>\n'.join('> ' + (x if x is not None else '[...]') for x in d['quotes']), '',
           'Amendment 6 resolves four schema ambiguities of category 3 and one expectation conflict that the tool writer '
           'raised while implementing amendment 4. Each resolution is a proposal for the owner\'s decision at adoption '
           '(AMENDMENT-6.md gives the options). None lets a finding be lost or lifted by rewording: every form failure '
           'blocks rather than lapses, and a migration only adds edits. Proposed: a review-record finding is the verdict '
           '`invalidates` with `invalidated` (R6.REC.2, R6.RECON.26); a finding names its configuration, with the '
           'fail-closed fallback of binding every configuration carrying the edit; migrations live in a reviewed '
           '`oi-edit-id-migration/1` record the configuration references (R6.RECON.28, R6.CFG.4); an `invalidated` '
           'element is `{id, sha256, target: {path, start_H, old_sha256}}`; RECON-BLOCK agrees with amendment 4.', '']
    return '\n'.join(out)


def amend_design(t, owner):
    t = once(t, "of the reviewed record (`accept`, `reject` or `dissent`, with the reason); and `dissent`, if any. A",
             "of the reviewed record (`accept`, `reject` or `dissent`, with the reason, and, on the item\n"
             "`<path>:scientific_effect` of a reconciliation record entry only, `invalidates` with `invalidated`,\n"
             "R6.RECON.26 %s); and `dissent`, if any. A" % MARK, 'R6.REC.2')
    a = t.index('**R6.RECON.26** **Category 3: the blocking state**')
    b = t.index('\nSources: amendment 3 (#1169 comments 7184569981, 7184626125, 7184808247 and 7185092393); amendment 4',
                a)
    t = t[:b] + FORM % {'mark': MARK} + t[b:]
    t = once(t, "Sources: amendment 3 (#1169 comments 7184569981, 7184626125, 7184808247 and 7185092393); amendment 4 "
                "(#1169 comment 7185562871). Controls: RECON-BLOCK, BLOCK-KEY.",
             "Sources: amendment 3 (#1169 comments 7184569981, 7184626125, 7184808247 and 7185092393); amendment 4 "
             "(#1169 comment 7185562871); amendment 6 (#1169 comment 7187418279). Controls: RECON-BLOCK, BLOCK-KEY, "
             "FINDING-FORM, FINDING-LINEAGE, FINDING-KEYS.", 'R6.RECON.26 controls')
    t = once(t, "the latter with `invalidated`, each an edit id with the\ncanonical sha256 of its edit-list entry and its "
                "target (the path, `start_H` and `old_sha256` of the edit at `H`)",
             "the latter with `invalidated`, each an edit id with the\ncanonical sha256 of its edit-list entry and its "
             "target (the path, `start_H` and `old_sha256` of the edit at `H`), in the form and with the `configuration` "
             "of R6.RECON.26 (iii) %s" % MARK, 'R6.RECON.25 invalidated')
    t = once(t, "Controls: RECON-SCI, RECON-BLOCK, \nBLOCK-KEY.", "Controls: RECON-SCI, RECON-BLOCK, \nBLOCK-KEY, FINDING-KEYS.",
             'R6.RECON.25 controls') if "Controls: RECON-SCI, RECON-BLOCK, \nBLOCK-KEY." in t else once(
        t, "Controls: RECON-SCI, RECON-BLOCK, BLOCK-KEY.", "Controls: RECON-SCI, RECON-BLOCK, BLOCK-KEY, FINDING-KEYS.",
        'R6.RECON.25 controls')
    t = once(t, "  record that the freeze cites (R6.RECON.27) is listed with kind `reassessment`",
             "  record that the freeze cites (R6.RECON.27) is listed with kind `reassessment`, and an edit-id migration\n"
             "  record (R6.RECON.28) with kind `edit-id-migration` %s," % MARK, 'R6.CFG.4 kind')
    t = once(t, "CONFIG-LINT, Z8, BLOCK-KEY.", "CONFIG-LINT, Z8, BLOCK-KEY, MIGRATION-RECORD.", 'R6.CFG.4 controls')
    t = once(t, "Sources: E-136, V2-056, RV-019. Controls: O1, O2, O3, O5, O7, I2-5.",
             "Sources: E-136, V2-056, RV-019. Controls: O1, O2, O3, O5, O7, I2-5, FINDING-FORM.", 'R6.REC.2 controls')
    t = once(t, "\n***\n\n## 24. Engine, purity scope (Z9), generality",
             NEW_REQ % {'mark': MARK, 'src': 'amendment 6 (#1169 comment 7187418279)'}
             + "\n***\n\n## 24. Engine, purity scope (Z9), generality", 'R6.RECON.28')
    t = once(t, "adds 9 rows (sec. 0.4), amendment 4 adds 3 rows (sec. 0.5), and amendment 5 adds 14 rows (sec. 0.6),\n"
                "each with one. Counted",
             "adds 9 rows (sec. 0.4), amendment 4 adds 3 rows (sec. 0.5), amendment 5 adds 14 rows (sec. 0.6), and\n"
             "amendment 6 adds %d rows (sec. 0.7), each with one. Counted" % len(ROWS), 'R6.CTRL.3 rows')
    m = re.search(r"\(\d+ rows, \d+ of them recording `scope: \"outside\"`; \d+ carry a `restored` expectation, \d+ "
                  r"declare direction `both`, \d+ name `paired_with`, \d+ are exempt as observations\)", t)
    if not m or t.count(m.group(0)) != 1:
        raise SystemExit('R6.CTRL.3 counts')
    t = t.replace(m.group(0), '(%s)' % COUNTS)
    anchor = [x for x in re.finditer(r'^\| LINE-PATCH-RC8 \| [^\n]*$', t, re.M)]
    if len(anchor) != 1:
        raise SystemExit('LINE-PATCH-RC8 table row')
    t = t[:anchor[0].end()] + '\n' + '\n'.join(
        '| %s | %s | to be implemented (tool revision) | decl | both | %s (amendment 6) |'
        % (r['id'], ', '.join(r['requirements']), cs) for r, cs in ROWS) + t[anchor[0].end():]
    a = t.index('### 0.6 Amendment 5 of 2026-11-26')
    b = t.index('\n***\n\n## 1. Notation and symbols', a)
    t = t[:b] + '\n' + note(owner) + t[b:]
    return t


COUNTS = ''


def counts_text(E):
    rows = [r for r in E['rows'] if not r['id'].startswith(('MUT:', 'GATE-'))]

    def dof(r):
        d = r.get('direction', 'adversarial')
        return d.get('of') if isinstance(d, dict) else d
    n_out = sum(1 for r in rows if isinstance(r.get('direction'), dict) and 'scope' in r['direction'])
    n_ex = sum(1 for r in rows if isinstance(r.get('direction'), dict) and r['direction'].get('exempt') == 'observation')
    return ('%d rows, %d of them recording `scope: "outside"`; %d carry a `restored` expectation, %d declare '
            'direction `both`, %d name `paired_with`, %d are exempt as observations'
            % (len(rows), n_out, sum(1 for r in rows if r.get('restored') is not None),
               sum(1 for r in rows if dof(r) == 'both'), sum(1 for r in rows if r.get('paired_with')), n_ex))


def amend_expectations(E):
    E = copy.deepcopy(E)
    by = {r['id']: r for r in E['rows']}
    rb = by['RECON-BLOCK']['expect']['cases']
    hits = [x for x in rb if x['case'] == RECON_BLOCK_OLD]
    if len(hits) != 1:
        raise SystemExit('RECON-BLOCK countercase not found once')
    hits[0]['case'] = RECON_BLOCK_NEW
    rb.append(copy.deepcopy(RECON_BLOCK_ADDED))
    for r, _ in ROWS:
        if r['id'] in by:
            raise SystemExit('id %s already a row' % r['id'])
        E['rows'].append(r)
    return E


def amend_requirements(R):
    R = copy.deepcopy(R)
    by = {q['id']: q for q in R}
    for rid, ctl in sorted(REQ_CONTROLS.items()):
        if rid in NEW_REQS:
            continue
        q = by[rid]
        if set(ctl) & set(q['controls']):
            raise SystemExit('%s: controls' % rid)
        q['controls'] = q['controls'] + ctl
    for rid in TOUCHED:
        by[rid]['pending_owner_confirmation'] = by[rid]['pending_owner_confirmation'] + [PENDING]
    i = [k for k, q in enumerate(R) if q['id'] == 'R6.RECON.27'][0]
    new = [{'id': 'R6.RECON.28', 'section': 'RECON', 'section_number': 23, 'kind': 'testable',
            'sources': ['#1169 comment 7187418279'], 'controls': list(REQ_CONTROLS['R6.RECON.28']),
            'verification': ['controls', 'review'], 'open': [], 'pending_owner_confirmation': [PENDING],
            'owner_decision': []}]
    return R[:i + 1] + new + R[i + 1:]


def vocabulary(t):
    a = t.index('### 16.10 Annex: invariant vocabulary')
    b = t.index('***', a)
    return set(re.findall(r'`([A-Za-z_0-9]+)`', t[t.index('\n\n', t.index('A key outside it', a)):b]))


def self_checks(E0, E, R0, R, t, base_texts):
    problems = []
    r0 = {r['id']: r for r in E0['rows']}
    r1 = {r['id']: r for r in E['rows']}
    reqs = {q['id']: q for q in R}
    for rid, r in r0.items():
        if rid == 'RECON-BLOCK':
            a, b = r, r1[rid]
            for f in a:
                if f != 'expect' and a[f] != b[f]:
                    problems.append('RECON-BLOCK field %s changed' % f)
            ca, cb = a['expect']['cases'], b['expect']['cases']
            if len(cb) != len(ca) + 1:
                problems.append('RECON-BLOCK: cases not exactly one added')
            for x, y in zip(ca, cb):
                if {k: v for k, v in x.items() if k != 'case'} != {k: v for k, v in y.items() if k != 'case'}:
                    problems.append('RECON-BLOCK: a case changed its expectation')
                if x['case'] != y['case'] and not (x['case'] == RECON_BLOCK_OLD and y['case'] == RECON_BLOCK_NEW):
                    problems.append('RECON-BLOCK: an unexpected case text change')
            continue
        if r1.get(rid) != r:
            problems.append('existing row %s changed' % rid)
    for rid in NEW_IDS + NEW_REQS + ['oi-edit-id-migration/1', 'edit-id-migration']:
        for name, b in base_texts.items():
            if re.search(r'(?<![A-Za-z0-9.-])%s(?![A-Za-z0-9-])' % re.escape(rid), b):
                problems.append('%s already occurs in base %s' % (rid, name))
    for r, _ in ROWS:
        cases = r['expect']['cases']
        if not any('countercase' in x['case'] for x in cases):
            problems.append('%s: no countercase' % r['id'])
        for q in r['requirements']:
            if r['id'] not in reqs[q]['controls']:
                problems.append('%s lists %s, which does not name it' % (r['id'], q))
    for q, ctl in REQ_CONTROLS.items():
        start = t.index('**%s**' % q)
        nxt = re.compile(r'\n(?:\*\*R6\.|\*\*\*|#)').search(t, start + 1)
        block = t[start:nxt.start()]
        cl = block.split('Controls:')[-1]
        for cc in ctl:
            if not re.search(r'(?<![A-Za-z0-9-])%s(?![A-Za-z0-9-])' % re.escape(cc), cl):
                problems.append('%s: DESIGN Controls line does not name %s' % (q, cc))
    for rid in TOUCHED + NEW_REQS:
        start = t.index('**%s**' % rid)
        nxt = re.compile(r'\n(?:\*\*R6\.|\*\*\*|#)').search(t, start + 1)
        if MARK not in t[start:nxt.start()]:
            problems.append('%s does not carry the amendment-6 mark' % rid)
    vocab = vocabulary(t)
    for r, _ in ROWS:
        for x in r['expect']['cases']:
            for inv in x.get('invariants', []):
                for k in inv:
                    if k not in vocab:
                        problems.append('%s: invariant key %s outside the vocabulary' % (r['id'], k))
    for rid, q in {q['id']: q for q in R0}.items():
        q1 = reqs[rid]
        if q1['controls'][:len(q['controls'])] != q['controls']:
            problems.append('requirement %s lost or reordered a control' % rid)
        for f in q:
            if f not in ('controls', 'pending_owner_confirmation') and q[f] != q1[f]:
                problems.append('requirement %s field %s changed' % (rid, f))
    return problems


def change_record(owner, outs, gen_sha, owner_sha):
    d = owner['decisions'][0]
    lines = ['# r6 amendment 6: change record', '',
             'Owner direction: %s, %s (%s), item 4, quoted in DESIGN-r6.md sec. 0.7. Generated by '
             'generator-amendment6/amend6.py (sha256 %s) from the amendment-5 outputs and '
             'generator-amendment6/owner-decisions-amendment6.json (sha256 %s). Amendment 6 resolves the four ambiguities '
             'and the one expectation conflict that the tool writer raised while implementing amendment 4 (r6 as amended '
             'at 939a79c2). Every resolution is a proposal; the choice is the owner\'s at adoption. It is kept separate '
             'from amendment 5, whose review stands.' % (d['author'], d['time'], d['record'], gen_sha, owner_sha), '',
             'Safety rule for every point: no reading may let a category-3 finding be lost or lifted by rewording. The '
             'owner\'s lifecycle holds: the block persists for the frozen plan, a repair does not validate, and a revised '
             'plan may proceed (by removing the edit, or by citing an applying reassessment for each finding).', '']
    for title, opts, rec, ctl in POINTS:
        lines += ['## ' + title, '', 'Options:', ''] + ['- ' + o for o in opts] + ['', rec, '',
                                                                                     'Controls: %s.' % ctl, '']
    lines += ['## Changes', '', '| File | Place | Change |', '|---|---|---|',
              '| DESIGN-r6.md | R6.REC.2 | the verdict value `invalidates`, on `scientific_effect` items only |',
              '| DESIGN-r6.md | R6.RECON.26 | "Form of a finding" (i) to (iv) |',
              '| DESIGN-r6.md | R6.RECON.25 | `invalidated` in the form and with the `configuration` of R6.RECON.26 (iii) |',
              '| DESIGN-r6.md | R6.CFG.4 | record kind `edit-id-migration` |',
              '| DESIGN-r6.md | R6.RECON.28 (new) | the edit-id migration record |',
              '| DESIGN-r6.md | sec. 0.7, R6.CTRL.3, Table 17.1 | the note; %d rows counted and added |' % len(ROWS),
              '| EXPECTATIONS.json | %s (new) | both directions each |' % ', '.join(NEW_IDS),
              '| EXPECTATIONS.json | RECON-BLOCK | the revised-plan countercase requires a cited reassessment; a '
              'wording-change case is added (stays blocked); no expectation value changes |',
              '| REQUIREMENTS.json | R6.RECON.28 (new); %s | controls appended; `pending_owner_confirmation` |'
              % ', '.join(TOUCHED), '',
              '## Tool changes implied (not made here)', '',
              '- Review-record lint separate from chain lint; the verdict value `invalidates`; form failures that still '
              'block (R6.RECON.26 (i), (ii)).',
              '- `configuration` in `scientific_effect` and in review verdicts; the lineage computed from it; the '
              'fail-closed fallback (R6.RECON.26 (iii)).',
              '- `oi-edit-id-migration/1` records read through `records` and the `supersedes` chain (R6.RECON.28).',
              '- The `invalidated` element `{id, sha256, target}` checked against the ledger splice (R6.RECON.26 (ii)).',
              '- Allowlist and schema list: `oi-edit-id-migration/1`, `edit-id-migration`, `invalidates`, `configuration`, '
              '`target`, `migrations`, `approval` where the engine holds them as literals.',
              '- Runners for %s.' % ', '.join(NEW_IDS), '',
              '## Outputs', '', '| File | sha256 |', '|---|---|']
    for n in ('DESIGN-r6.md', 'EXPECTATIONS.json', 'REQUIREMENTS.json'):
        lines.append('| %s | %s |' % (n, sha(outs[n])))
    lines.append('')
    return '\n'.join(lines)


def manifest(m, outs, gen_sha, owner_sha):
    for n, label in (('DESIGN-r6.md', 'final r6 document (the design)'),
                     ('EXPECTATIONS.json', 'final r6 document (expectation file)'),
                     ('REQUIREMENTS.json', 'final r6 document (requirement index)')):
        mm = [x for x in re.finditer(r'^\| %s \| [^\n]*$' % re.escape(n), m, re.M)]
        if len(mm) != 1:
            raise SystemExit('manifest row %s' % n)
        m = m[:mm[0].start()] + '| %s | %s | amendment-6 output | %s |' % (n, label, sha(outs[n])) + m[mm[0].end():]
    rows = ('| AMENDMENT-6.md | change record of amendment 6 | amendment-6 output | %s |\n'
            '| generator-amendment6/amend6.py | amendment-6 generator | amendment-6 generator | %s |\n'
            '| generator-amendment6/owner-decisions-amendment6.json | amendment-6 generator input (the owner direction '
            'quoted) | amendment-6 generator | %s |\n' % (sha(outs['AMENDMENT-6.md']), gen_sha, owner_sha))
    m = once(m, '| LANDING-MANIFEST.md | this manifest (A5) | amendment-5 output | (this file) |',
             rows + '| LANDING-MANIFEST.md | this manifest (A5) | amendment-6 output | (this file) |', 'manifest self')
    para = ('\nAmendment 6 (owner direction of 2026-11-26, amaybaum, #1169 comment 7187418279, item 4, quoted in '
            'DESIGN-r6.md sec. 0.7): DESIGN-r6.md, EXPECTATIONS.json and REQUIREMENTS.json are amended, and '
            'AMENDMENT-6.md records the options and proposals. Recipe: run the amendment-5 recipe into `out5/` and run '
            '`python3 -I -B generator-amendment6/amend6.py out5 out6`. It checks the four files against their sha256, '
            'exits 0 and writes into `out6/` the files of sec. 1 marked "amendment-6 output" with the sha256 stated and '
            'this manifest.\n')
    m = once(m, '\n## 2. Files left to Git history', para + '\n## 2. Files left to Git history', 'manifest recipe')
    return m


def main():
    global COUNTS
    if len(sys.argv) != 3:
        sys.stderr.write('usage: amend6.py BASE OUT\n')
        return 64
    base, out = sys.argv[1], sys.argv[2]
    data = {}
    for n, h in BASE_SHA256.items():
        with open(os.path.join(base, n), 'rb') as f:
            data[n] = f.read()
        if sha(data[n]) != h:
            sys.stderr.write('%s: sha256 %s, expected %s\n' % (n, sha(data[n]), h))
            return 65
    with open(os.path.join(HERE, 'owner-decisions-amendment6.json'), 'rb') as f:
        owner_b = f.read()
    owner = json.loads(owner_b)
    E0 = json.loads(data['EXPECTATIONS.json'])
    R0 = json.loads(data['REQUIREMENTS.json'])
    E = amend_expectations(E0)
    R = amend_requirements(R0)
    COUNTS = counts_text(E)
    t = amend_design(data['DESIGN-r6.md'].decode('utf-8'), owner)
    problems = self_checks(E0, E, R0, R, t, {n: b.decode('utf-8') for n, b in data.items()})
    if problems:
        sys.stderr.write('self-check failures:\n' + '\n'.join(problems) + '\n')
        return 1
    outs = {'DESIGN-r6.md': t.encode('utf-8'), 'EXPECTATIONS.json': dumpj(E), 'REQUIREMENTS.json': dumpj(R)}
    with open(os.path.join(HERE, 'amend6.py'), 'rb') as f:
        gen_sha = sha(f.read())
    outs['AMENDMENT-6.md'] = change_record(owner, outs, gen_sha, sha(owner_b)).encode('utf-8')
    outs['LANDING-MANIFEST.md'] = manifest(data['LANDING-MANIFEST.md'].decode('utf-8'), outs, gen_sha,
                                           sha(owner_b)).encode('utf-8')
    os.makedirs(out, exist_ok=True)
    for n, b in sorted(outs.items()):
        with open(os.path.join(out, n), 'wb') as f:
            f.write(b)
        print('%s %s' % (sha(b), n))
    return 0


if __name__ == '__main__':
    sys.exit(main())
