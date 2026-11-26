"""Generator of amendment 6 (r3) to design r6: the category-3 schema ambiguities raised by the tool writer (points 1 to
5); the answers to the reviews of its drafts (PR #1593 comments 7189446310, 7190255132 and 7190234470); two further
ambiguities found by the tool writer (RC14 (b) and the R6.RECON.24 resolution schema); the schema contract of the
reconciliation record kinds from the owner's completeness audit (PR #1593 comment 7189621405); and the amendment 5
nits routed here, under the owner's directions of 2026-11-26 (#1169 comments 7187418279, item 4; 7188752730, item 2;
7189470338, items 1, 3 and 4; 7189915409).

Usage: python3 -I -B amend6.py BASE OUT

BASE holds DESIGN-r6.md, EXPECTATIONS.json, REQUIREMENTS.json and LANDING-MANIFEST.md as amendment 5 leaves them
(each checked against its sha256 below). The script reads owner-decisions-amendment6.json beside itself and writes
into OUT the amended DESIGN-r6.md, EXPECTATIONS.json and REQUIREMENTS.json, the change record AMENDMENT-6.md and the
updated LANDING-MANIFEST.md. Every recommendation is a proposal for the owner's decision at adoption.

Self-checks: every difference from a row amendment 5 left is a declared change in its declared form, a classes_exact
only narrows unless declared, and amendment 5 r2's strengthenings are pinned; no requirement loses a control or gains
an undeclared control or pending entry; every new row has a countercase and a positive case; correspondence; the
closed invariant vocabulary; the amendment-6 mark on every touched requirement; one key table per record kind,
rendered from one definition; every case removed from r2 names the case that covers it; every review finding, audit
row, nit and item B is mapped in the change record. Standard library only; deterministic.
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
MARK = '(amendment 6, sec. 0.7: proposal, pending independent review and the owner\'s decision)'
PENDING = ('amendment 6 (category-3 schema resolutions and the reconciliation schema contract): a proposal under the '
           'owner\'s directions of 2026-11-26 (#1169 comments 7187418279, item 4; 7188752730, item 2; 7189470338, items '
           '1, 3 and 4); needs independent review and the owner\'s decision at adoption')


def sha(b):
    return hashlib.sha256(b).hexdigest()


def once(text, old, new, what):
    n = text.count(old)
    if n != 1:
        raise SystemExit('anchor for %s occurs %d times' % (what, n))
    return text.replace(old, new)


def dumpj(doc):
    return (json.dumps(doc, indent=1, ensure_ascii=False) + '\n').encode('utf-8')

# ---- the record specifications: one definition per kind, rendered as its key tables (R6.RECON.29 to R6.RECON.34)
# and expanded into the conformance mutants (CONFORMANCE-MUTANTS.json). Each part: (table id, title, rows); each row:
# (key, type as written, required, source and binding, acceptance, machine type). Machine types: ('lit', v),
# ('enum', (v, ...)), ('str',), ('nstr',), ('commit',), ('blob',), ('sha256',), ('offset',), ('int',), ('path',),
# ('ident',), ('time',), ('b64',), ('null',), ('obj', table id), ('arr', element type, minimum length),
# ('or', type, type, ...), ('any',).
REF = 'reference'
T_REF = ('obj', 'reference')
T_REF_OR_NULL = ('or', T_REF, ('null',))
S = ('nstr',)
SPEC = {
    'recon': [
        ('reference', 'reference (R6.RECON.29)', [
            ('path', 'path', 'yes', 'the record\'s path', '', ('path',)),
            ('blob_sha256', 'sha256', 'yes', 'the sha256 of the blob\'s bytes', '', ('sha256',)),
        ]),
        ('recon.record', '`oi-reconciliation/2` record', [
            ('schema', '`"oi-reconciliation/2"`', 'yes', '', 'a record of schema `oi-reconciliation/1` that a run '
             'reads is FAIL `record-invalid` and never applies; detection (R6.RECON.35) reads `/1` files too',
             ('lit', 'oi-reconciliation/2')),
            ('record_id', 'non-empty string', 'yes', 'the record\'s lineage (R6.REC.7)', '', S),
            ('supersedes', REF + ' or null', 'yes', 'R6.REC.7', '', T_REF_OR_NULL),
            ('author', 'identity string', 'yes', 'the writer (R6.REC.2)', '', ('ident',)),
            ('M', 'commit id', 'yes', 'the run\'s `M`', 'equal, as a string, to the run\'s full id', ('commit',)),
            ('X', 'commit id', 'yes', 'the run\'s `X`', 'equal, as a string, to the run\'s full id', ('commit',)),
            ('ledger_base', 'commit id', 'yes', '`roles.scientific_base`', 'equals `H` (RC13, R6.RECON.5)',
             ('commit',)),
            ('changes_decisions_on_X', 'array', 'yes', 'R6.RECON.3', 'RC12 holds only for `[]`',
             ('arr', ('any',), 0)),
            ('paths', 'non-empty array of entries', 'yes', 'the paths the record covers',
             'each entry\'s `path` occurs once', ('arr', ('obj', 'recon.entry'), 1)),
        ]),
        ('recon.entry', 'entry (element of `paths`)', [
            ('path', 'path', 'yes', 'a ledgered or corpus path that differs between `H` and `M`', '', ('path',)),
            ('ledger_binding', 'object (below)', 'yes', 'read through the ledger interface (R6.ADAPT.2)',
             'RC13 (R6.RECON.5)', ('obj', 'recon.ledger_binding')),
            ('side_change_commits', 'array of commit ids', 'yes', 'the commits on `M`\'s first-parent chain after `H` '
             'that change the path, oldest first', 'RC1', ('arr', ('commit',), 0)),
            ('scientific_effect', 'object (below)', 'yes', 'R6.RECON.25', '', ('obj', 'recon.scientific_effect')),
            ('m', 'blob id', 'yes', 'the path\'s blob at `M`', 'RC2', ('blob',)),
            ('m_sha256', 'sha256', 'yes', 'the same blob', 'RC2', ('sha256',)),
            ('l', 'blob id', 'yes', 'the composed blob (R6.TREE.12, R6.RECON.19)', 'RC7', ('blob',)),
            ('l_sha256', 'sha256', 'yes', 'the same blob', 'RC7', ('sha256',)),
            ('x', 'blob id', 'yes', 'the path\'s blob at `X`', 'RC8', ('blob',)),
            ('x_sha256', 'sha256', 'yes', 'the same blob', 'RC8', ('sha256',)),
            ('splices', 'array of splices (below)', 'yes', 'one element for each splice of the path in the ledger, '
             'in ledger order', 'the list of `id` values equals the ledger\'s splice ids for the path, in order',
             ('arr', ('obj', 'recon.splice'), 0)),
            ('protected', 'array of protected ranges (below)', 'yes', 'the protected ranges at `M`', 'RC9',
             ('arr', ('obj', 'recon.protected'), 0)),
            ('resolutions', 'array of resolutions (below)', 'no; absent means `[]`', 'the explicit resolutions',
             'R6.RECON.24', ('arr', ('obj', 'recon.resolution'), 0)),
        ]),
        ('recon.ledger_binding', '`ledger_binding`', [
            ('files_entry_sha256', 'sha256 or null', 'yes', 'the canonical sha256 of the path\'s raw `files` entry',
             'null for a corpus path the ledger does not list', ('or', ('sha256',), ('null',))),
            ('splices_sha256', 'sha256 or null', 'yes', 'the canonical sha256 of the list of the path\'s raw splices, '
             'in ledger order', 'likewise', ('or', ('sha256',), ('null',))),
            ('edit_records_sha256', 'sha256 or null', 'yes', 'the canonical sha256 of the list of the raw edit-list '
             'entries whose `file` is the path, in edit-list order', 'likewise', ('or', ('sha256',), ('null',))),
        ]),
        ('recon.scientific_effect', '`scientific_effect`', [
            ('conclusions', '`"none"` or a non-empty array of distinct edit ids', 'yes', 'R6.RECON.25',
             'edit ids of the edit list of the configuration `configuration` names, not the run\'s',
             ('or', ('lit', 'none'), ('arr', S, 1))),
            ('assessment', 'non-empty string', 'yes', 'R6.RECON.25', 'rests on the review', S),
            ('method', 'non-empty string', 'yes', 'R6.RECON.25', 'the executed-path rule below', S),
            ('verdict', '`"no-effect"` or `"invalidates"`', 'yes', 'R6.RECON.25', '',
             ('enum', ('no-effect', 'invalidates'))),
            ('configuration', REF, 'yes', 'the configuration under which the entry was assessed (R6.RECON.26, Form of '
             'a finding (iii))', 'resolved as R6.RECON.33 states', T_REF),
            ('invalidated', 'non-empty array of `invalidated` elements (below)',
             'exactly when `verdict` is `"invalidates"`', 'R6.RECON.26', 'checked against the configuration '
             '`configuration` names', ('arr', ('obj', 'invalidated'), 1)),
        ]),
        ('invalidated', '`invalidated` element (R6.RECON.26, Form of a finding (ii))', [
            ('id', 'non-empty string', 'yes', 'an edit id of the named configuration\'s edit list', '', S),
            ('sha256', 'sha256', 'yes', 'the canonical sha256 of that edit-list entry', '', ('sha256',)),
            ('target', 'object (below)', 'yes', 'the edit at the named configuration\'s `H`', '',
             ('obj', 'invalidated.target')),
        ]),
        ('invalidated.target', '`target`', [
            ('path', 'path', 'yes', 'the edit\'s file', '', ('path',)),
            ('start_H', 'offset', 'yes', 'the edit\'s start at that `H`', '', ('offset',)),
            ('old_sha256', 'sha256', 'yes', 'the sha256 of the edit\'s old bytes (a retained edit\'s `text`)', '',
             ('sha256',)),
        ]),
        ('recon.splice', 'splice (element of `splices`)', [
            ('id', 'non-empty string', 'yes', 'the ledger\'s splice id', '', S),
            ('start_H', 'offset', 'yes', 'the splice\'s start at `H`', 'equals the ledger\'s', ('offset',)),
            ('end_H', 'offset', 'yes', 'the splice\'s end at `H`', 'equals the ledger\'s', ('offset',)),
            ('start_M', 'offset', 'yes', 'the splice\'s translated start at `M`', 'RC4', ('offset',)),
            ('end_M', 'offset', 'yes', '`start_M + end_H - start_H`', 'equal to that sum', ('offset',)),
            ('new_sha256', 'sha256', 'yes', 'the sha256 of the splice\'s new bytes', 'RC6', ('sha256',)),
            ('translation', '`"identity"` or an integer', 'yes', 'R6.RECON.10', 'RC5',
             ('or', ('lit', 'identity'), ('int',))),
        ]),
        ('recon.protected', 'protected range (element of `protected`)', [
            ('start_M', 'offset', 'yes', 'R6.RECON.1', 'RC9', ('offset',)),
            ('end_M', 'offset', 'yes', 'R6.RECON.1', 'RC9', ('offset',)),
            ('sha256', 'sha256', 'yes', 'the bytes `m[start_M:end_M]`', 'RC9', ('sha256',)),
        ]),
        ('recon.resolution', 'resolution (element of `resolutions`)', [
            ('splice', 'non-empty string', 'yes', 'R6.RECON.24, resolution schema', '', S),
            ('start_M', 'offset', 'yes', 'R6.RECON.24', '', ('offset',)),
            ('end_M', 'offset', 'yes', 'R6.RECON.24', '', ('offset',)),
            ('sha256', 'sha256', 'yes', 'R6.RECON.24', '', ('sha256',)),
            ('resolved', 'canonical base64 string', 'yes', 'R6.RECON.24', '', ('b64',)),
            ('resolved_sha256', 'sha256', 'yes', 'R6.RECON.24', '', ('sha256',)),
        ]),
    ],
    'review': [
        ('review.record', '`oi-review-record/1` record', [
            ('schema', '`"oi-review-record/1"`', 'yes', '', '', ('lit', 'oi-review-record/1')),
            ('kind', '`"review"` or `"widening"`', 'no; absent means `"review"`', '', '',
             ('enum', ('review', 'widening'))),
            ('reviewer', 'identity string', 'yes', 'the reviewer (R6.REC.2)', 'not equal to the reviewed record\'s '
             '`author`; for a widening review, also not equal to the reviewer of the superseding record\'s own review '
             '(R6.REC.13)', ('ident',)),
            ('reviewed', REF, 'yes', 'the reviewed record', 'its `path` and `blob_sha256` both equal those of the '
             'reviewed record, in record lint, in the post-freeze route and in detection alike', T_REF),
            ('replaces', REF, 'exactly when `kind` is `"widening"`', 'the superseded record (R6.REC.13)', '', T_REF),
            ('method', 'non-empty string', 'yes', 'how each item was re-derived (R6.REC.2)',
             'contains at least one full 40-character object id that the reviewer read', S),
            ('verdicts', 'array of verdict entries (below)', 'yes', 'R6.REC.2',
             'one entry for each item id of the reviewed record (the item-id table below), no duplicate',
             ('arr', ('obj', 'review.verdict'), 1)),
            ('dissent', 'string', 'no', 'R6.REC.2', '', ('str',)),
        ]),
        ('review.verdict', 'verdict entry (element of `verdicts`)', [
            ('item', 'non-empty string', 'yes', 'an item id of the reviewed record', '', S),
            ('verdict', '`"accept"`, `"reject"`, `"dissent"` or `"invalidates"`', 'yes', 'R6.REC.2, R6.RECON.26',
             '`invalidates` only on `<path>:scientific_effect`',
             ('enum', ('accept', 'reject', 'dissent', 'invalidates'))),
            ('reason', 'string', 'yes', 'R6.REC.2', 'non-empty for a verdict other than `accept`', ('str',)),
            ('invalidated', 'non-empty array of `invalidated` elements (R6.RECON.30)', 'with `invalidates` only',
             'R6.RECON.26', '', ('arr', ('obj', 'invalidated'), 1)),
            ('configuration', REF, 'with `invalidates` only', 'R6.RECON.26 (iii)', '', T_REF),
            ('confirms', 'object (below)', 'on a resolution item only, and there required', 'R6.RECON.24',
             'equal to the resolution\'s values', ('obj', 'review.confirms')),
        ]),
        ('review.confirms', '`confirms`', [
            ('start_M', 'offset', 'yes', 'the resolution\'s `start_M`', 'equal', ('offset',)),
            ('end_M', 'offset', 'yes', 'the resolution\'s `end_M`', 'equal', ('offset',)),
            ('sha256', 'sha256', 'yes', 'the resolution\'s `sha256`', 'equal', ('sha256',)),
            ('resolved_sha256', 'sha256', 'yes', 'the resolution\'s `resolved_sha256`', 'equal', ('sha256',)),
        ]),
    ],
    'reassess': [
        ('reassess.record', '`oi-reassessment/1` record', [
            ('schema', '`"oi-reassessment/1"`', 'yes', '', '', ('lit', 'oi-reassessment/1')),
            ('record_id', 'non-empty string', 'yes', 'R6.REC.7', '', S),
            ('supersedes', REF + ' or null', 'yes', 'R6.REC.7', '', T_REF_OR_NULL),
            ('author', 'identity string', 'yes', 'R6.REC.2', '', ('ident',)),
            ('finding', 'object (below)', 'yes', 'R6.RECON.27, Keys', '', ('obj', 'reassess.finding')),
            ('repair', 'object (below), or null', 'yes', 'R6.RECON.27, Keys', 'null only where Keys admits it',
             ('or', ('obj', 'reassess.repair'), ('null',))),
            ('edit', 'object (below), or null', 'yes', 'R6.RECON.27, Keys',
             'null exactly for a finding bound at run level', ('or', ('obj', 'reassess.edit'), ('null',))),
            ('rederivation', 'non-empty string', 'yes', 'the edit\'s justification re-derived at the run\'s `M`, '
             'stating what was re-run', 'that the re-run happened rests on the review', S),
            ('verdict', '`"no-effect"`', 'yes', 'R6.RECON.27', '', ('lit', 'no-effect')),
        ]),
        ('reassess.finding', '`finding`', [
            ('path', 'path', 'yes', 'the path of the file carrying the finding', '', ('path',)),
            ('blob_sha256', 'sha256', 'yes', 'the sha256 of that file', '', ('sha256',)),
            ('item', 'non-empty string, or null', 'yes', 'R6.RECON.27, Keys',
             'null exactly for a finding read from a malformed file (R6.RECON.35 classes (b) and (c))',
             ('or', S, ('null',))),
        ]),
        ('reassess.repair', '`repair`', [
            ('commits', 'non-empty array of distinct commit ids', 'yes', 'the repairing change',
             'each on `M`\'s first-parent chain', ('arr', ('commit',), 1)),
            ('entry', 'object (below)', 'yes', 'the reconciliation record entry recording the repair', '',
             ('obj', 'reassess.repair.entry')),
        ]),
        ('reassess.repair.entry', '`repair.entry`', [
            ('path', 'path', 'yes', 'the reconciliation record\'s path', '', ('path',)),
            ('blob_sha256', 'sha256', 'yes', 'its sha256', '', ('sha256',)),
            ('entry_path', 'path', 'yes', 'the path of its entry for the repairing change', '', ('path',)),
        ]),
        ('reassess.edit', '`edit`', [
            ('id', 'non-empty string', 'yes', 'an edit id of the citing configuration\'s edit list', '', S),
            ('sha256', 'sha256', 'yes', 'the canonical sha256 of that edit-list entry', '', ('sha256',)),
        ]),
        ('migration.record', '`oi-edit-id-migration/1` record', [
            ('schema', '`"oi-edit-id-migration/1"`', 'yes', '', '', ('lit', 'oi-edit-id-migration/1')),
            ('record_id', 'non-empty string', 'yes', 'R6.REC.7', '', S),
            ('supersedes', REF + ' or null', 'yes', 'R6.REC.7', '', T_REF_OR_NULL),
            ('author', 'identity string', 'yes', 'R6.REC.2', '', ('ident',)),
            ('migrations', 'non-empty array of migrations (below)', 'yes', 'R6.RECON.28', 'the lint of R6.RECON.28',
             ('arr', ('obj', 'migration.element'), 1)),
            ('approval', 'object (below)', 'yes', 'the owner\'s recorded approval (AGENTS.md sec. A.48 item 3)',
             'form only (R6.REC.3)', ('obj', 'migration.approval')),
        ]),
        ('migration.element', 'migration (element of `migrations`)', [
            ('old', 'non-empty string', 'yes', 'the renamed edit id', '', S),
            ('new', 'non-empty string', 'yes', 'its successor', '', S),
        ]),
        ('migration.approval', '`approval`', [
            ('quote', 'non-empty string', 'yes', 'the owner\'s words', '', S),
            ('author', 'identity string', 'yes', 'the owner\'s login', '', ('ident',)),
            ('time', 'time', 'yes', 'the time of the owner\'s record', '', ('time',)),
        ]),
    ],
    'class': [
        ('class.record', '`oi-side-change-classes/1` record', [
            ('schema', '`"oi-side-change-classes/1"`', 'yes', '', '', ('lit', 'oi-side-change-classes/1')),
            ('record_id', 'non-empty string', 'yes', 'R6.REC.7', '', S),
            ('supersedes', REF + ' or null', 'yes', 'R6.REC.7', '', T_REF_OR_NULL),
            ('author', 'identity string', 'yes', 'R6.REC.2', '', ('ident',)),
            ('classes', 'non-empty array of classes (below)', 'yes', 'R6.TREE.5', 'each class id defined once',
             ('arr', ('obj', 'class.class'), 1)),
        ]),
        ('class.class', 'class (element of `classes`)', [
            ('id', 'non-empty string', 'yes', 'R6.TREE.5', '', S),
            ('prefixes', 'array of paths', 'yes', 'where the class\'s paths may lie (R6.TREE.5)',
             'a path lies under a prefix when it begins with the prefix followed by `/`', ('arr', ('path',), 0)),
            ('pins', 'array of pins (below)', 'yes', 'the pinned blobs (R6.TREE.5)', '',
             ('arr', ('obj', 'class.pin'), 0)),
        ]),
        ('class.pin', 'pin (element of `pins`)', [
            ('path', 'path', 'yes', 'the pinned path', '', ('path',)),
            ('blob_sha256', 'sha256', 'yes', 'the sha256 of its blob at `M`', 'the pin', ('sha256',)),
        ]),
    ],
}
PARTS = {pid: (kind, title, rows) for kind, parts in SPEC.items() for pid, title, rows in parts}


def spec_tables(kind):
    out = []
    for pid, title, rows in SPEC[kind]:
        out += ['*%s* (table `%s`)' % (title, pid), '',
                '| Key | Type | Required | Source and binding | Acceptance |', '|---|---|---|---|---|']
        for key, typ, req, src, acc, _m in rows:
            out.append('| `%s` | %s | %s | %s | %s |' % (key, typ, req, src or '', acc or ''))
        out.append('')
    return '\n'.join(out).rstrip('\n')


JSON_TYPES = ('null', 'boolean', 'number', 'string', 'array', 'object')
STRINGISH = ('lit', 'enum', 'str', 'nstr', 'commit', 'blob', 'sha256', 'path', 'ident', 'time', 'b64')
# the near-miss variants of each encoding, all of the correct JSON type (R6.RECON.29)
NEAR = {
    'commit': ['upper-case', 'thirty-nine-characters', 'trailing-newline'],
    'blob': ['upper-case', 'thirty-nine-characters', 'trailing-newline'],
    'sha256': ['upper-case', 'sixty-three-characters', 'trailing-newline'],
    'offset': ['fraction-5.0', 'negative'],
    'int': ['fraction-5.0'],
    'path': ['leading-slash', 'trailing-slash', 'empty-component', 'dot-component', 'dot-dot-component'],
    'ident': ['url'],
    'time': ['no-zone', 'space-separator'],
    'b64': ['unpadded', 'line-break'],
    'nstr': ['empty'],
    'lit': ['trailing-space', 'other-case'],
    'enum': ['unlisted-value'],
}


def admitted(t):
    k = t[0]
    if k in STRINGISH:
        return {'string'}
    if k in ('offset', 'int'):
        return {'number'}
    if k == 'null':
        return {'null'}
    if k == 'obj':
        return {'object'}
    if k == 'arr':
        return {'array'}
    if k == 'any':
        return set(JSON_TYPES)
    if k == 'or':
        out = set()
        for x in t[1:]:
            out |= admitted(x)
        return out
    raise SystemExit('machine type %r' % (t,))


def near_misses(t, path):
    k = t[0]
    out = []
    if k == 'or':
        for x in t[1:]:
            out += near_misses(x, path)
    elif k == 'arr':
        if t[2] >= 1:
            out.append((path, 'empty-array'))
        if t[1][0] not in ('obj', 'any'):
            out += near_misses(t[1], path + '[0]')
    elif k in NEAR:
        out += [(path, v) for v in NEAR[k]]
    return out


def mutants():
    """The conformance mutants, by the fixed rule of R6.RECON.29: (table, key path, violation)."""
    out = []
    for pid, (kind, title, rows) in sorted(PARTS.items()):
        for key, typ, req, src, acc, m in rows:
            if req == 'yes':
                out.append((pid, key, 'required-key-removed'))
            for jt in JSON_TYPES:
                if jt not in admitted(m):
                    out.append((pid, key, 'type-' + jt))
            out += [(pid, p, v) for p, v in near_misses(m, key)]
        out.append((pid, '+unlisted', 'unlisted-key-added'))
    return out


def mutants_doc():
    ms = mutants()
    return {'schema': 'oi-conformance-mutants/1',
            'rule': 'R6.RECON.29: for each key table, each required key removed, one unlisted key added, one value of '
                    'each other JSON type for each key, and each near-miss variant of each encoding with the correct '
                    'JSON type; a nested table is mutated at one occurrence in its kind\'s positive record',
            'tables': sorted(PARTS),
            'mutants': [{'table': a, 'key_path': b, 'violation': c} for a, b, c in ms]}


MUTANTS_SHA = sha(dumpj(mutants_doc()))

SRC = ('r6 amendment 6 (owner directions of 2026-11-26, #1169 comments 7187418279, item 4, 7188752730, item 2, and '
       '7189470338, items 1, 3 and 4; reviews on PR #1593: 7189446310, 7189621405, 7190234470 and 7190255132)')
FLAG = 'added by amendment 6 (a proposal); no runner records it before the tool revision implements it'

BLOCKED = {'outcome': 'FAIL', 'classes_include': ['retirement-blocked']}
BLOCKED_INV = {'outcome': 'FAIL', 'classes_include': ['retirement-blocked', 'record-invalid']}
NOT_BLOCKED = {'outcome': 'ANY', 'invariants': [{'not_class': ['retirement-blocked']}]}
INVALID = {'outcome': 'FAIL', 'classes_include': ['record-invalid']}
INVALID_DRIFT = {'outcome': 'FAIL', 'classes_include': ['record-invalid', 'base-drift']}
INVALID_NOT_BLOCKED = {'outcome': 'FAIL', 'classes_include': ['record-invalid'],
                       'invariants': [{'not_class': ['retirement-blocked']}]}
CLEAN = {'outcome': 'ANY', 'invariants': [{'not_class': ['base-drift', 'record-invalid']}]}
CLEAN_SCAN = {'outcome': 'ANY', 'invariants': [{'not_class': ['record-invalid', 'retirement-blocked']}]}
RESOLVED = {'outcome': 'ANY', 'invariants': [{'not_class': ['base-drift', 'record-invalid']},
                                             {'equals': 'the path\'s disposition is reconciled-resolved, category 2'}]}
RECONCILED = {'outcome': 'ANY', 'invariants': [{'not_class': ['base-drift', 'record-invalid']},
                                               {'equals': 'the path\'s disposition is reconciled, category 1'}]}
CONFIG_ERR = {'outcome': 'ERROR', 'stop_class': 'CONFIG_INVALID'}
CONFIG_OK = {'outcome': 'ANY', 'invariants': [{'no_stop': True}]}


def rc(cond):
    return {'outcome': 'FAIL', 'classes_include': ['base-drift'], 'invariants': [{'failed_conditions_include': cond}]}


def c(case, base):
    return dict(case=case, **copy.deepcopy(base))


def row(rid, req, cases, summary, ops=('execution',)):
    r = {'id': rid, 'requirements': req, 'runner': None, 'operations': list(ops), 'direction': 'both',
         'expect': {'cases': cases}, 'source': SRC, 'flags': [FLAG]}
    return r, summary


GENERIC_CASE = ('countercase (conformance mutants): each mutant of CONFORMANCE-MUTANTS.json (sha256 %s), applied '
                '(R6.RECON.29) to the positive record of its kind, run separately and recorded with its id (table, '
                'key path, violation); the recorded ids equal the list' % MUTANTS_SHA)

ROWS = [
    row('FINDING-FORM', ['R6.RECON.26', 'R6.REC.2', 'R6.REC.6'], [
        c('a writer\'s verdict no-effect and a non-author review whose verdict on the item <path>:scientific_effect is '
          'invalidates with a well-formed invalidated list and configuration, the review passing review-record lint',
          BLOCKED),
        c('the same review: the reviewed entry fails its own chain lint and does not apply, and the review stays valid',
          {'outcome': 'FAIL', 'classes_include': ['retirement-blocked'],
           'invariants': [{'none': 'items[class=record-invalid,subject=$review]'}]}),
        c('a review verdict invalidates with an empty invalidated list (blocks every edit the entry\'s conclusions '
          'name, or every edit of the path)', BLOCKED_INV),
        c('a review verdict accept carrying an invalidated list', BLOCKED_INV),
        c('a non-author review with a well-formed invalidates verdict whose verdicts omit an unrelated item of the '
          'reviewed record (review-record lint fails elsewhere; detection precedes lint)', BLOCKED_INV),
        c('the same, the verdicts duplicating an unrelated item', BLOCKED_INV),
        c('the same, the review without method', BLOCKED_INV),
        c('a well-formed invalidates verdict and invalidated list placed on an item other than <path>:scientific_effect '
          '(for example <path>:resolution:<splice>)', BLOCKED_INV),
        c('a review verdict invalidates with an empty invalidated list on an entry with conclusions none for an '
          'unledgered corpus path (the fallback set is empty): a run-level retirement-blocked item binds the lineage',
          BLOCKED_INV),
        c('countercase: the same finding, the configuration frozen anew citing an applying reassessment that names the '
          'finding with edit null (positive)', NOT_BLOCKED),
        c('countercase: a review verdict reject without invalidated on the scientific_effect item (the path is not '
          'reconciled and is not blocked)', {'outcome': 'FAIL', 'classes_include': ['base-drift'],
                                             'invariants': [{'not_class': ['retirement-blocked']}]}),
        c('countercase: a review with a well-formed invalidates verdict whose reviewer equals the reviewed record\'s '
          'author after trimming and case-folding (an independence failure: not a finding; the record fails lint)',
          INVALID_NOT_BLOCKED),
        c('countercase: an accepting non-author review and a second non-author review of the same blob whose verdict on '
          'another item is reject (every review naming the blob counts; the record fails lint and is not blocked)',
          INVALID_NOT_BLOCKED)],
        'detection before lint; only an independence failure disqualifies; an empty fallback binds at run level; every '
        'review naming the blob counts'),
    row('FINDING-LINEAGE', ['R6.RECON.26', 'R6.RECON.33'], [
        c('a fork outside the lineage (supersedes null, a new config_id, a new retirement name and Issue) carrying the '
          'invalidated edit under the same id and target with reworded new text, citing no reassessment', BLOCKED),
        c('the same fork carrying the invalidated edit\'s target (the same path and old bytes) under another id',
          BLOCKED),
        c('a fork frozen on a new H after a repair changed the old bytes of the edit\'s span, carrying the edit under '
          'the same id on the same path (the id-and-path match)', BLOCKED),
        c('countercase: a configuration of another retirement, outside the lineage, whose ledger reuses the edit id on '
          'another path, and holds no edit of the target path with the recorded old bytes (positive)', NOT_BLOCKED),
        c('a finding naming no configuration, or one that cannot be read: it binds every configuration whose ledger '
          'carries the edit by id, a migrated id or the target, the other retirement\'s id collision included',
          BLOCKED_INV),
        c('a finding naming no configuration; a superseding configuration renames the edit id, keeps its old bytes and '
          'records no migration', BLOCKED_INV),
        c('a finding naming a readable configuration of another lineage whose ledger holds the same id and target: the '
          'retirement\'s own configuration carrying the target is still blocked', BLOCKED),
        c('countercase: the other retirement bound only by the fallback\'s id collision, frozen anew with the colliding '
          'id renamed under a recorded migration, its target different (positive)', NOT_BLOCKED)],
        'the global match by path and old bytes, or by id and path; the fallback; the rename remedy'),
    row('FINDING-KEYS', ['R6.RECON.26', 'R6.RECON.25'], [
        c('an invalidated element {id, sha256, target: {path, start_H, old_sha256}} matching the ledger edit of that id '
          'at the named configuration\'s H', BLOCKED),
        c('an element whose target differs from the ledger edit of its id (form failure; the element blocks through the '
          'fallback)', BLOCKED_INV),
        c('an element whose id is absent from the named configuration\'s ledger: the fallback binds every configuration '
          'carrying the id, a migrated id or the target', BLOCKED_INV),
        c('an element {id, sha256} without target (form failure; the id still blocks)', BLOCKED_INV),
        c('an element whose start_H and old_sha256 are those of a commit other than the named configuration\'s H',
          BLOCKED_INV),
        c('an element naming a retained edit (no splice), its target the occurrence of the retained text at H, matched in '
          'a later configuration whose retained edit has the same text', BLOCKED),
        c('countercase: a revised configuration keeping only an edit of the same path that no finding names, under '
          'another id, whose old bytes\' sha256 differs from every recorded old_sha256, without a reassessment '
          '(positive)', NOT_BLOCKED)],
        'the invalidated element, read against the named configuration; a retained edit\'s old bytes are its text'),
    row('MIGRATION-RECORD', ['R6.RECON.28', 'R6.CFG.4', 'R6.RECON.32'], [
        c('an edit renamed, its old bytes also rewritten, under a reviewed edit-id migration record that the '
          'configuration references with kind edit-id-migration', BLOCKED),
        c('the same migration record referenced only by an earlier configuration on the supersedes chain', BLOCKED),
        c('two referenced migration records chaining A to B and B to C (transitive closure)', BLOCKED),
        c('a migration record that fails record lint, the renamed edit\'s old bytes unchanged (the path-and-old-bytes '
          'match still applies)', BLOCKED_INV),
        c('a migration record whose new is an id in use (a configuration on the supersedes chain holds both the old and '
          'the new id), or that repeats an old: record lint fails and it maps nothing; the renamed edit\'s old bytes '
          'unchanged', BLOCKED_INV),
        c('countercase: a configuration that removes the renamed edit (neither its old id, its new id nor its old '
          'bytes remain) (positive)', NOT_BLOCKED),
        c('countercase: a lint-passing migration record found at M that neither the configuration nor its supersedes '
          'chain references, mapping the invalidated id to an id of this configuration whose edit has another target '
          'and another path (the mapping is not applied) (positive)', NOT_BLOCKED)],
        'where a recorded migration lives; lint against reuse; only referenced records apply'),
    row('REASSESS-KEYS', ['R6.RECON.27', 'R6.RECON.32'], [
        c('one record carrying findings on two entries (paths p and q) against the same edit; the revised configuration '
          'cites one reassessment whose finding names the record with item p only', BLOCKED),
        c('a reassessment whose finding lacks item', BLOCKED_INV),
        c('a reassessment whose repair.commits holds an abbreviated commit id', BLOCKED_INV),
        c('a reassessment whose repair.entry names an entry_path that the named reconciliation record has no entry for',
          BLOCKED_INV),
        c('a reassessment whose edit.sha256 is computed over a non-canonical serialization of the edit-list entry (it '
          'differs from the canonical sha256)', BLOCKED_INV),
        c('a reassessment with edit null for a finding bound to an edit (not at run level)', BLOCKED_INV),
        c('a reassessment whose rederivation is not a string, or which carries a key outside its table', BLOCKED_INV),
        c('a reassessment with repair null for a well-formed finding of the second kind', BLOCKED_INV),
        c('a reassessment with repair null for a second-kind finding by an independent reviewer that is malformed '
          '(its review lacks method, or omits an unrelated verdict)', BLOCKED_INV),
        c('a reassessment with repair null for a first-kind finding whose entry has no review', BLOCKED_INV),
        c('a reassessment with item null for a finding read from a well-formed record (class (a) of R6.RECON.35)',
          BLOCKED_INV),
        c('countercase: a reassessment with repair null for a first-kind finding whose entry\'s non-author review '
          'rejects <path>:scientific_effect, with a non-empty rederivation at M, an accepting non-author review and a '
          'new freeze citing it (positive)', NOT_BLOCKED),
        c('countercase: a reassessment with item null and repair null for a malformed file of class (c) of '
          'R6.RECON.35, the finding being the whole file, with its rederivation, review and new freeze (positive)',
          NOT_BLOCKED),
        c('countercase: two reassessments, one for each finding, each naming its record and item, with repair and edit '
          'as defined (positive)', NOT_BLOCKED)],
        'the reassessment keys; per-finding lifting; repair null only for a form failure or an unaccepted first-kind '
        'finding'),
    row('RECON-RETAINED', ['R6.RECON.24', 'R6.ADAPT.2'], [
        c('M changes a byte of the line holding a retained edit\'s text at H', rc('RC14')),
        c('M adds a second copy of a retained site\'s line elsewhere in the file', rc('RC14')),
        c('a retained edit whose text spans two lines; M changes a byte of the second line', rc('RC14')),
        c('a retained site that moved between E and H (its site-map pin_line differs from its line at H), M not '
          'touching its line: the line at H is found from the retained text, with no E..H walk (positive)', CLEAN),
        c('countercase: M changes bytes outside every context window and every retained site\'s line (positive)',
          CLEAN)],
        'RC14 (b) finds the retained site\'s line at H from the retained text'),
    row('RESOLUTION-SCHEMA', ['R6.RECON.24', 'R6.REC.2'], [
        c('a resolution {splice, start_M, end_M, sha256, resolved, resolved_sha256}: 0-based byte offsets into the '
          'entry\'s m blob, end exclusive; sha256 of m[start_M:end_M]; resolved the canonical base64 of the replacement '
          'bytes; resolved_sha256 their sha256; l equal to the composition; the review\'s verdict on '
          '<path>:resolution:<splice> accept with confirms equal to the window and resolved_sha256 (positive)',
          RESOLVED),
        c('a deletion splice (empty new) resolved by replacement bytes that do not contain the splice\'s old bytes, '
          'confirmed by the review (positive)', RESOLVED),
        c('countercase (replacement content): a deletion splice whose replacement bytes still contain its old bytes',
          rc('RC14')),
        c('countercase (window): end_M greater than the length of the m blob', INVALID_DRIFT),
        c('countercase (window): start_M equal to end_M', INVALID_DRIFT),
        c('countercase (window): start_M inside a multi-byte UTF-8 character', INVALID_DRIFT),
        c('countercase (window): an m blob that is not valid UTF-8', INVALID_DRIFT),
        c('countercase (window): a window one byte wider than H\'s context window, which still occurs exactly once at '
          'M, its sha256 that of the wider bytes', rc('RC14')),
        c('countercase (hash): sha256 not the hash of m[start_M:end_M]', INVALID_DRIFT),
        c('countercase (hash): resolved_sha256 not the hash of the decoded resolved bytes', INVALID_DRIFT),
        c('countercase (encoding): resolved base64 with a line break, without padding, or with a character outside the '
          'standard alphabet', INVALID_DRIFT),
        c('countercase (replacement content): decoded resolved bytes carrying the splice\'s new bytes twice',
          rc('RC14')),
        c('countercase (replacement content): the hashes consistent, l composed from other replacement bytes than the '
          'decoded resolved bytes', rc('RC7')),
        c('countercase (splice identity): splice naming an id absent from the ledger, or a splice of another path',
          INVALID_DRIFT),
        c('countercase (splice identity): two resolutions naming one splice', INVALID_DRIFT),
        c('countercase (splice identity): a resolution naming a splice for which RC14 (a) holds and whose old bytes '
          'occur once at M', INVALID_DRIFT),
        c('countercase (windows): two resolution windows of the entry that overlap, or a window overlapping an '
          'unresolved splice\'s translated span', INVALID_DRIFT),
        c('countercase (review): the verdict accept on <path>:resolution:<splice> without confirms', INVALID_DRIFT),
        c('countercase (review): confirms whose resolved_sha256, start_M, end_M or sha256 differs from the '
          'resolution\'s', INVALID_DRIFT),
        c('countercase (review): no verdict on <path>:resolution:<splice>', INVALID_DRIFT)],
        'the resolution schema (owner decision 7189470338, item 1), its mechanical checks, deletion splices and the '
        'bound review confirmation'),
    row('RECON-SCHEMA', ['R6.RECON.29', 'R6.RECON.30', 'R6.RECON.10', 'R6.RECON.31', 'R6.RECON.32', 'R6.RECON.34'], [
        c('a record that conforms to every key table of R6.RECON.30 and to the conditions stated beside them (positive)',
          CLEAN),
        c('a review record, a reassessment, an edit-id migration record and a side-change class record, each '
          'conforming to its key tables of R6.RECON.31, R6.RECON.32 and R6.RECON.34 (positive, one record per kind)',
          {'outcome': 'ANY', 'invariants': [{'not_class': ['record-invalid']}]}),
        c(GENERIC_CASE, {'outcome': 'FAIL', 'classes_include': ['record-invalid'],
                         'invariants': [{'items_include': [{'class': 'record-invalid', 'subject': '$mutant_record',
                                                            'key_path': '$key_path'}]},
                                        {'none': 'items[subject=$mutant_record,failed_conditions_nonempty]'}]}),
        c('countercase: changes_decisions_on_X missing, null, {} or ""', INVALID_DRIFT),
        c('countercase: an offset written 5.0, or true, in a splice, a protected range or a resolution', INVALID_DRIFT),
        c('countercase: a splice translation "shift"', INVALID_DRIFT),
        c('countercase: a record of schema oi-reconciliation/1 read by the run', INVALID_DRIFT),
        c('countercase: two entries with one path', INVALID_DRIFT),
        c('countercase: an entry whose splices list holds an element for a splice the ledger does not have for the '
          'path', INVALID_DRIFT),
        c('countercase: an entry whose splices list holds the path\'s splices in another order than the ledger\'s',
          INVALID_DRIFT),
        c('countercase: a splice translation given as an integer other than start_M - start_H', rc('RC5')),
        c('an equal-length change on M before a splice, the splice\'s translation 0 (positive)', RECONCILED),
        c('countercase: the same change with translation "identity" (the prefix agreement fails)', rc('RC5'))],
        'conformance to the key tables, a malformed field record-invalid before any condition, the named tool '
        'divergences, splice-list completeness and RC5'),
    row('RECON-FIELDS', ['R6.RECON.30', 'R6.RECON.21'], [
        c('a mode-only change of a ledgered path on M (100644 to 100755), the commit listed in side_change_commits and '
          'every other condition holding (positive)', RECONCILED),
        c('countercase: the same mode-only change with side_change_commits empty', rc('RC1')),
        c('countercase: a ledgered path deleted at M', rc('RC2')),
        c('countercase: x naming the path\'s blob at C where C differs from X', rc('RC8')),
        c('a no-effect entry whose conclusions name an edit removed by a revised plan, read against the configuration '
          'it names (positive: no form failure)', {'outcome': 'ANY',
                                                   'invariants': [{'not_class': ['record-invalid']}]}),
        c('countercase: an entry for a path with a suffix of the configuration\'s executed_suffixes whose method does '
          'not contain the l blob id', INVALID_DRIFT),
        c('countercase: an entry for a path a delegation class covers whose method does not contain the l blob id',
          INVALID_DRIFT),
        c('an entry for an executed path outside the suffix floor (an extensionless script a workflow runs) whose '
          'method names the check re-run at l, accepted by the review (positive)', CLEAN)],
        'mode-only drift, deletion, x at X, conclusions against the named configuration, the executed-path floor'),
    row('CANON-JSON', ['R6.RECON.29', 'R6.ADAPT.2'], [
        c('a ledger_binding computed from the raw files entry, the path\'s raw splices in ledger order and the path\'s '
          'raw edit-list entries in edit-list order, canonical JSON with non-ASCII text written as UTF-8 (positive)',
          CLEAN),
        c('countercase: edit_records_sha256 computed with non-ASCII characters escaped as \\u sequences', rc('RC13')),
        c('countercase: splices_sha256 computed over the splices in another order', rc('RC13')),
        c('countercase: a ledger adapter that returns no raw edit-list entries (the interface is incomplete)',
          {'outcome': 'ERROR', 'stop_class': 'LEDGER_INTEGRITY'}),
        c('countercase: an edit list with a duplicate key in an entry, or a non-integer number in a hashed value',
          {'outcome': 'ERROR', 'stop_class': 'LEDGER_INTEGRITY'})],
        'the canonical JSON, strict parsing of the ledger and edit list, and the raw entries in the ledger interface'),
    row('REVIEW-SCHEMA', ['R6.RECON.31', 'R6.REC.2', 'R6.CTX.7', 'R6.HIT.4'], [
        c('a review record with reviewer, reviewed {path, blob_sha256} matching the record, method naming a full object '
          'id, and verdicts {item, verdict, reason} covering the item ids of the table, for each reviewed kind of the '
          'table (an HP record by sites[].site_id; a context or hit-classification record by each element\'s id) '
          '(positive)', CLEAN),
        c('countercase: a verdict entry without reason, or with a key outside the table', INVALID_DRIFT),
        c('countercase: reviewed naming the record\'s blob under another path', INVALID_DRIFT),
        c('countercase: method naming no full object id', INVALID_DRIFT),
        c('countercase: verdicts whose item strings are not the item ids of the table (for example "entry 1", or an HP '
          'review keyed by entries)', INVALID_DRIFT),
        c('countercase: a reconciliation record without a review in its own directory, its only review lying in '
          'another directory', INVALID_DRIFT),
        c('a widening review of kind widening with replaces naming the superseded blob and one verdict for each item id '
          'of the difference rule, all accept (positive)', CLEAN),
        c('countercase: a widening review without kind widening, or without replaces', INVALID),
        c('countercase: a widening review that omits the item field:<key> of a changed top-level key', INVALID),
        c('countercase: a configuration carrying a widening_review key', CONFIG_ERR)],
        'the review record\'s keys, identity, method, the item-id table and the widening items'),
    row('CONFIG-REFS', ['R6.RECON.33', 'R6.CFG.4'], [
        c('a configuration whose records entries each carry a kind of the enumeration with a record of the mapped '
          'schema, roles.side_change_classes also listed in records with the same blob, retirement {name, issue}, '
          'executed_suffixes holding the design floor and .js added (positive)', CONFIG_OK),
        c('countercase: executed_suffixes lacking .py, or set to [".none"] (it must contain the design floor)',
          CONFIG_ERR),
        c('countercase: a records entry of a kind outside the enumeration', CONFIG_ERR),
        c('countercase: a records entry whose record has a schema other than its kind\'s', CONFIG_ERR),
        c('countercase: roles.side_change_classes not listed in records, or listed with another blob', CONFIG_ERR),
        c('countercase: retirement.issue a string, or retirement without name', CONFIG_ERR),
        c('countercase: a check carrying default_for (a key outside R6.CFG.4)', CONFIG_ERR),
        c('countercase: a configuration with a top-level notes or sites key', CONFIG_ERR),
        c('countercase: an op B or op D run without --check', {'outcome': 'USAGE'})],
        'the kind enumeration and schema map, the class role, retirement keys, unknown keys, no default check',
        ops=('execution', 'coverage', 'terms')),
    row('SUPERSEDES-RESOLVE', ['R6.RECON.33', 'R6.REC.7', 'R6.REC.17'], [
        c('a configuration version 2 whose supersedes names version 1, which is no longer at its path at F: version 1 '
          'resolves at the newest commit on F\'s first-parent chain whose tree holds that path with that blob '
          '(positive)', CONFIG_OK),
        c('a finding made under version 1 binds version 2, resolved in that way, which carries the edit', BLOCKED),
        c('a harness run (RT-L2) whose record\'s scientific_effect.configuration names the control-supplied draft '
          'configuration: it resolves to that configuration (positive)', CLEAN),
        c('countercase: a harness run whose record names a configuration that is neither the draft configuration nor '
          'held on REV\'s first-parent chain', INVALID_DRIFT),
        c('countercase: a configuration supersedes blob that no commit on F\'s first-parent chain holds at that path',
          CONFIG_ERR),
        c('countercase: a record\'s supersedes naming a record blob that no commit on the chain holds at that path',
          INVALID)],
        'the resolution of a reference in each admission mode, the whole-chain walk, the lineage direction'),
    row('CLASS-SCHEMA', ['R6.RECON.34', 'R6.TREE.5'], [
        c('a class record whose classes carry id, prefixes and pins [{path, blob_sha256}] (positive)', CLEAN),
        c('countercase: a pin carrying git_blob (a key outside the table)', INVALID),
        c('countercase: a class carrying the class-level paths form', INVALID),
        c('countercase: a superseding class record that adds a pin without a widening review', INVALID)],
        'side-change class record keys and widening'),
    row('SCAN-PARSE', ['R6.RECON.35', 'R6.RECON.2'], [
        c('a review record carrying a finding, stored without a .json suffix in a reconciliation directory', BLOCKED),
        c('a file under verification/audits/ that begins with { and fails strict parsing (a duplicate key, NaN), whose '
          'text contains oi-review-record/1 and invalidates: a malformed finding, run level', BLOCKED_INV),
        c('a file that parses and whose schema is a near miss ("oi-review-record/1 ", "Oi-review-record/1" or '
          '"oi-review-record/2") with a verdict invalidates: a malformed finding, run level', BLOCKED_INV),
        c('a review carrying a finding stored as a JSON array holding the review object', BLOCKED_INV),
        c('a malformed file encoded in UTF-16 with a byte-order mark, or writing the schema id with \\u escapes, whose '
          'text contains oi-review-record/1 and invalidates', BLOCKED_INV),
        c('a review carrying a well-formed finding that lies in the plan\'s record directory', BLOCKED),
        c('a file beginning with { that holds one invalid UTF-8 byte, whose lossy text contains oi-review-record/1 and '
          'invalidates: selected by its leading bytes, a malformed finding, run level', BLOCKED_INV),
        c('a parsed object with no schema key but a review\'s shape (a reviewed key and a verdicts entry carrying '
          'invalidates)', BLOCKED_INV),
        c('a file that fails strict parsing and contains oi-reconciliation/2 but neither invalidates nor invalidated: a '
          'malformed record, not a finding', INVALID_NOT_BLOCKED),
        c('two byte-identical reconciliation records at different paths covering one path: two records',
          INVALID_DRIFT),
        c('a review carrying a finding that lies in a reconciliation directory other than its record\'s', BLOCKED_INV),
        c('countercase: a Markdown document under verification/audits/ that quotes oi-review-record/1 and invalidates '
          '(it does not begin a JSON value, so it is not a record) (positive)', CLEAN_SCAN),
        c('countercase: a JSON file under verification/audits/ that parses, whose objects carry no schema beginning '
          'oi-review-record/ or oi-reconciliation/, and whose text contains invalidates (positive)', CLEAN_SCAN)],
        'detection over every JSON-shaped file, D_rec included; near-miss schemas; strict parsing; record identity'),
]

NEW_IDS = [r['id'] for r, _ in ROWS]
# existing rows that amendment 6 makes control a requirement (by a declared change below)
EXTRA_CONTROLS = {'R6.RECON.36': ['RECON-ENUM'], 'R6.OUT.18': ['RECON-ENUM']}
REQ_CONTROLS = {}
for _r, _ in ROWS:
    for _q in _r['requirements']:
        REQ_CONTROLS.setdefault(_q, []).append(_r['id'])
for _q, _ids in EXTRA_CONTROLS.items():
    REQ_CONTROLS.setdefault(_q, []).extend(_ids)
NEW_REQS = ['R6.RECON.28', 'R6.RECON.29', 'R6.RECON.30', 'R6.RECON.31', 'R6.RECON.32', 'R6.RECON.33', 'R6.RECON.34',
            'R6.RECON.35', 'R6.RECON.36', 'R6.GATE.17']
TOUCHED = ['R6.RECON.26', 'R6.RECON.25', 'R6.RECON.24', 'R6.RECON.27', 'R6.RECON.21', 'R6.RECON.2', 'R6.RECON.10',
           'R6.REC.2', 'R6.REC.6', 'R6.REC.7', 'R6.REC.17', 'R6.CFG.4', 'R6.ADAPT.2', 'R6.TREE.5', 'R6.OUT.18',
           'R6.CTX.7', 'R6.HIT.4', 'R6.RECON.23', 'R6.GATE.3']
# touched requirements whose existing rows control them (no new control is added to their Controls lines)
EXISTING_CONTROLLED = {'R6.RECON.23': 'RECON-TRIAL', 'R6.GATE.3': 'L2, RT-D, RT-DR, RT-DR3W (the corrected count keys)'}
CONTROLS_ANCHOR = {
    'R6.RECON.26': 'Controls: RECON-BLOCK, BLOCK-KEY.',
    'R6.RECON.25': 'Controls: RECON-SCI, RECON-BLOCK, BLOCK-KEY.',
    'R6.RECON.24': 'Controls: RECON-CONFLICT, RECON-CATEGORY, RECON-OVERLAP.',
    'R6.RECON.27': 'Controls: BLOCK-KEY, REASSESS-FORM.',
    'R6.RECON.21': 'RTL2-BIND, RECON-TRIAL, RECORD-BASE.',
    'R6.RECON.2': 'RB-C10, RB-C11.',
    'R6.RECON.10': 'Sources: E-1347. Controls: N13.',
    'R6.REC.2': 'Sources: E-136, V2-056, RV-019. Controls: O1, O2, O3, O5, O7, I2-5.',
    'R6.REC.6': 'Controls: O1, O2, O3, O5, R3-F2, R4-B3, R4-B3-DUP, R5-N6, GV6.',
    'R6.REC.7': 'LN7, LN8, LN10, R6-G6, POSTF-4.',
    'R6.REC.17': 'GV-CACHE-IMMUTABLE, GV-CACHE-KEY, K1-GRAPH.',
    'R6.CFG.4': 'CONFIG-LINT, Z8, BLOCK-KEY.',
    'R6.ADAPT.2': 'E-1428. Controls: U10, U11, M3, M4, M5, Z9h.',
    'R6.TREE.5': 'Controls: R18, R18-engine, R19, R19-engine, Z11, TT13, RDIR-24.',
    'R6.OUT.18': 'S7-schema-and-checker, B4-MEANING, U2, U9, U10.',
    'R6.CTX.7': 'Sources: E-082, RV-013. Controls: K10.',
    'R6.HIT.4': 'Sources: E-1060, E-1061. Controls: I2-7, I2-4, I2-6.',
}

RECON_BLOCK_OLD = ('countercase: the run under a revised plan, a new configuration whose ledger changes the invalidated '
                   'edit\'s edit-list entry (positive)')
RECON_BLOCK_NEW = ('countercase: the run under a revised plan, a new configuration whose ledger changes the invalidated '
                   'edit\'s edit-list entry and whose freeze cites an applying reassessment naming the finding '
                   '(R6.RECON.27) (positive)')



FORM = '''

**Form of a finding** %(mark)s. (i) *Detection precedes lint.* A finding is read from every file
that the detection of R6.RECON.35 selects, before and whatever the outcome of the file's schema check and record
lint. A review record counts as a finding of the second kind when an entry of its `verdicts`, on any item of a
reconciliation record entry, has the verdict value `invalidates` or carries the key `invalidated`, unless its
independence fails: its `reviewer` equals the `author` of the record its `reviewed` names (R6.RECON.29), or is a run,
check or Issue (R6.REC.6). Only such an independence failure disqualifies it; a review whose `reviewed` names no
record the scan finds, so that its independence cannot be established, counts, as a form failure. Every other failure
of such a review (its schema or fields, R6.RECON.31; a missing `method`; verdicts that omit or duplicate an item;
`invalidates` on an item other than `<path>:scientific_effect`; `invalidated` with a verdict value other than
`invalidates`; an empty or malformed `invalidated`; a missing or unreadable `configuration`) is a form failure, FAIL
`record-invalid`, and the finding still blocks. A finding of the first kind is a reconciliation record entry whose
`scientific_effect` has the verdict `invalidates` or carries `invalidated`, read likewise before the record's schema
and lint; it counts whatever the entry's review says, and a failure of the record's form is a form failure that still
blocks. A well-formed finding of the second kind is the verdict `invalidates` on `<path>:scientific_effect` with a
non-empty `invalidated` of the form (ii) and a `configuration` (iii); `oi-review-record/1` permits `invalidates` on that
item only (R6.REC.2). The verdict `invalidates` makes the reviewed record fail its own chain lint (R6.REC.6) and not
apply; it does not make the review invalid. A file that R6.RECON.35 classes as a malformed finding binds at run level
under (iv). (ii) *The invalidated element.* Each element of `invalidated`, in an entry's `scientific_effect` or in a
review verdict, is `{id, sha256, target: {path, start_H, old_sha256}}`, read against the configuration named in (iii):
`id` is an edit id of that configuration's edit list (R6.ADAPT.2 `edits`), a retained edit included; `sha256` is the
canonical sha256 (R6.RECON.29) of that edit-list entry; `target` gives, at that configuration's `H`
(`roles.scientific_base`), the edit's file, its start and the sha256 of its old bytes: for an edit with a splice, the
splice's `file`, `start` and `old_sha256`; for a retained edit, the start of its `text` (R6.ADAPT.2 `retained`) at `H`
and the sha256 of that text. In every match of this requirement, a retained edit's old bytes are its `text`. An
element that lacks a key, or any of whose values differs from that configuration's ledger, is a form failure, FAIL
`record-invalid`, and blocks through the fallback of (iii). (iii) *Configuration.* Every finding names
`configuration`, the reference of the configuration under which it was made: the entry's `scientific_effect` carries
it for the first kind, the review verdict entry for the second. It is resolved, and the plan lineage is computed from
it, as R6.RECON.33 states. A finding whose `configuration` is absent or cannot be resolved, or one of whose
`invalidated` elements differs from the named configuration's ledger, is a form failure, FAIL `record-invalid`, and
binds, besides the lineage where one is readable, every configuration whose ledger carries one of its edits, whatever
its lineage or retirement; here a ledger carries an edit when it holds the edit's id, an id the edit was renamed to
under R6.RECON.28, or an edit of the target's path whose old bytes hash to the target's `old_sha256`. (iv) *The edits a
finding binds.* A finding binds the edits its `invalidated` elements name, by id and, where an element carries one, by
target. Where `invalidated` is absent, empty or unreadable, or the verdict lies on an item other than
`<path>:scientific_effect`, it binds every edit the entry's `conclusions` name, or, if they name none, every edit of
the entry's path. Where that set is empty (for example `conclusions: "none"` on a corpus path the ledger does not
list), or the finding names no entry the scan finds, it binds at run level every configuration of its lineage, and
every configuration when its `configuration` cannot be resolved: each such run has a run-level item FAIL
`retirement-blocked` naming the finding, as amendment 3 provides for a path that does not differ. That binding is
lifted only by a new freeze that cites an applying reassessment naming the finding, with `edit` null (R6.RECON.27).
(v) *Scope of the matches.* The id match and the migration match are scoped to the plan lineage. Two matches apply to
every configuration, whatever its lineage: an edit of the target's path whose old bytes hash to the target's
`old_sha256`, whatever its id and offset; and an edit with the invalidated edit's id on the target's path, whatever its
old bytes. A fork (a configuration with `supersedes: null`, a new `config_id` and a new retirement name and Issue) that
carries the invalidated edit's target, or its id on the same file after a repair changed the old bytes on a new `H`,
is therefore blocked. A configuration bound only by an id collision (through the fallback of (iii), its edit of that
id lying on another path) proceeds by a new freeze that renames the colliding id, through an AGENTS.md sec. A.48 item
3 migration where records cite it; a configuration bound by a global match proceeds, as any blocked plan does, by
removing the edit or by an applying reassessment. No later record narrows a finding's binding. The one residual is a
rename that also rewrites the old bytes and records no migration (R6.RECON.28). (vi) The migrations the edit-id match
follows are those of R6.RECON.28.'''

KEYS27 = '''

**Keys** %(mark)s. `finding` is `{path, blob_sha256, item}`: the reference of the record or review
record carrying the finding, and `item`, which of its findings is meant: for a finding of the first kind, the entry's
path; for one of the second kind, the item id of the verdict entry carrying it (for example
`<path>:scientific_effect`); null exactly for a finding read from a malformed file of class (b) or (c) of R6.RECON.35,
the finding then being the whole file. A reassessment lifts only the finding it names; a record or review that carries several
findings needs one reassessment for each. Where duplicated verdict entries give two findings with one `item`, a
reassessment naming that `item` lifts each of them for its `edit` only, and only where that finding binds the `edit`.
`repair` is `{commits, entry}`: `commits`, a non-empty array of distinct commit ids (R6.RECON.29), each on `M`'s
first-parent chain; `entry`, `{path, blob_sha256, entry_path}`, the reference of the reconciliation record that records
the repair and the path of its entry for the repairing change. `repair` is null only where no independent reviewer asserts the
invalidation: (a) a finding of the first kind whose entry has a non-author review that rejects or dissents on
`<path>:scientific_effect` (such a review must exist; an entry with no review does not qualify); (b) a review whose
`reviewed` names no record the scan finds, so that its independence cannot be established; or (c) a malformed file of
class (b) or (c) of R6.RECON.35. A finding of the second kind by an independent reviewer needs a repair however it is
malformed. Where `repair` is null, every other condition of this requirement still holds (an applying review, the
re-derivation at `M`, the verdict, and a new freeze that cites the reassessment), and only the conditions on the
repair's commits and entry are not evaluated. `edit` is `{id, sha256}`: `id`, an edit id of the citing configuration's
edit list; `sha256`, the canonical sha256 (R6.RECON.29) of that id's edit-list entry in the citing configuration, so
that a later rewording of the edit needs a new reassessment. `edit` is null exactly when the named finding is bound at
run level (R6.RECON.26, Form of a finding (iv)). The finding and the repair's entry are resolved from the scans of
R6.RECON.35 at the run's `M`, not by the search of R6.RECON.33. A key that is missing, of another type, or outside the
table of R6.RECON.32 is a form failure: the reassessment does not apply, FAIL `record-invalid`, and the block stands.'''

NEW_REQ28 = '''
**R6.RECON.28** **Edit-id migration record** %(mark)s. A rename of a ledger edit id under AGENTS.md
sec. A.48 item 3 is recorded for the tool in a reviewed, immutable record of schema `oi-edit-id-migration/1`, under the
ownership chain of sec. 11, with the fields of R6.RECON.32: `migrations`, a list of `{old, new}` edit ids, and
`approval`, the owner's recorded approval quoted with its author and time. A configuration that carries a renamed edit
references the record in `records` with kind `edit-id-migration` (R6.CFG.4). For R6.RECON.26 the tool maps a finding's
edit id through every such record that the configuration, or a configuration on its `supersedes` chain, references,
taking the transitive closure. A record that fails record lint is FAIL `record-invalid` and maps nothing. A migration
record never lifts a block: the global matches of R6.RECON.26 apply whether or not a migration is recorded, and a
mapping only adds edits the block binds. The tool checks `approval` for form only (R6.RECON.32); it neither reads nor
checks the owner's approval (R6.REC.3). Record lint also rejects a record in which an `old` or a `new` repeats or an
`old` equals its `new`, and a record referenced by a configuration on whose `supersedes` chain (itself included) some
configuration's ledger holds both an `old` and its `new`: the `new` id would then be an id in use, which AGENTS.md
sec. A.48 item 3 forbids. An `old` mapped to two different `new` ids, or a cycle, over the records applied, fails each
record involved. Only referenced records apply: a migration record that no configuration on the chain references is
not used (R6.REC.4, R6.REC.5), even where the scan finds it, so a record written for another plan cannot map this
plan's ids, and every mapping a run applies is pinned at the freeze by its blob sha256. A rename that also rewrites the
edit's old bytes and moves it to another path, or rewrites them with no recorded, referenced migration, is the residual
of R6.RECON.26 (v); it rests on the review of the new freeze.
Sources: amendment 6 (#1169 comment 7187418279; PR #1593 comment 7189446310, finding 7). Controls: MIGRATION-RECORD.
'''

RC14B_OLD = ('(b) the line of each retained site of the path (the ledger interface\'s `retained`, resolved at `H`\n'
             'through the site map) occurs exactly once at `M`, with the same bytes.')
RC14B_NEW = ('(b) the line of each retained site of the path occurs exactly once at `M`, with the same bytes. The\n'
             'line at `H` is found from the retained edit\'s own text, not through the site map %s: the ledger\n'
             'interface\'s `retained` entry carries `text`, the bytes of the pair that P\'s selection picks for that edit at\n'
             '`H` (R6.PROF.8; for a retained edit `old` equals `new`), whose occurrence at `H` is unique by R6.PROF.8 and\n'
             'whose site text is the same at `H` and `X` by R6.PIPE.15; the line is the bytes from the start of the first\n'
             'line that overlaps that occurrence to the end of the last such line; `site_ref` identifies the site only.\n'
             'Op C reads no `E..H` walk for it.' % MARK)

RC5_OLD = ('**R6.RECON.10** RC5 (translation): each splice\'s translation is the one the record states. For an\n'
           '`identity` translation, `H` and `M` agree byte for byte up to the splice\'s end and `start_M` equals the\n'
           'splice\'s start; otherwise the offset of the unique occurrence at `M` minus the splice\'s start equals\n'
           'the record\'s `start_M` minus the splice\'s start.')
RC5_NEW = ('**R6.RECON.10** RC5 (translation): each splice\'s `translation` agrees with its offsets and with `H` and\n'
           '`M` %s. The value `"identity"` requires `start_M` to equal the splice\'s start and `H` and `M` to agree byte\n'
           'for byte from the start of the file up to the splice\'s end (prefix agreement). An integer requires\n'
           '`start_M` minus the splice\'s start to equal it; 0 is allowed and makes no claim about the bytes before the\n'
           'splice, so an equal-length change on `M` before the splice is recorded with 0. In both cases RC4 places the\n'
           'splice\'s old bytes at `start_M`. A `translation` of another type is a schema failure (R6.RECON.29); a value\n'
           'of the right type that disagrees fails RC5.' % MARK)

RESOLUTION = '''
**Resolution schema** %(mark)s. Each element of `resolutions` is `{splice, start_M, end_M,
sha256, resolved, resolved_sha256}` (owner decision of 2026-11-26, #1169 comment 7189470338, item 1; key table in
R6.RECON.30), with no other key:
- `splice`: the id of the conflicting retirement edit's splice in the configuration's ledger (R6.ADAPT.2
  `splices[].id`, unique there), whose `file` is the entry's path, and for which RC14 (a) fails or whose old bytes do
  not occur exactly once at `M`. An entry has at most one resolution per splice.
- `start_M`, `end_M`: the window, as offsets (R6.RECON.29) into the entry's `m` blob, the path's blob in `M`'s tree:
  0-based byte offsets, `start_M` included and `end_M` excluded, the convention of the ledger's byte spans, with
  `0 <= start_M < end_M <=` the blob's length, each at a UTF-8 character boundary of the blob. An `m` blob that is not
  valid UTF-8 has no character boundaries: its resolutions fail (FAIL `record-invalid`), and the path stays
  `base-drift`; a ledgered path is valid UTF-8 at `H` (R6.PROF.8).
- `sha256`: the sha256 of the bytes `m[start_M:end_M]`.
- `resolved`: the replacement bytes, in base64 (RFC 4648 sec. 4: the standard alphabet, `=` padding, no line break or
  other character), and canonical: re-encoding the decoded bytes gives the same string. Base64 is lossless for every
  byte, carriage returns, invisible characters and invalid UTF-8 included, and no text normalization on the way can
  alter it without breaking the decoding or `resolved_sha256`.
- `resolved_sha256`: the sha256 of the decoded replacement bytes.

The tool verifies mechanically from git objects: the keys and types; splice identity (the id is a splice of the
ledger at the entry's path, conflicting as above, and not resolved twice); the window boundaries; that `sha256` is the
sha256 of the window's bytes; that the window's bytes occur exactly once in `m`, every byte position counted
(overlapping occurrences included), and, where `H`'s context window still occurs exactly once at `M`, that the window
is that occurrence; that the decoded `resolved` hashes to `resolved_sha256`; containment, that the splice's approved
new bytes (the ledger's `new`, hashing to `new_sha256`) occur exactly once in the decoded bytes, every position
counted, or, for a splice whose new bytes are empty (a deletion), that the decoded bytes do not contain the splice's
old bytes, every position counted; that the windows of an entry are pairwise disjoint and disjoint from the translated
span of every unresolved splice of the path; and the composed content, that the entry's `l` is `m` with each window
replaced by its decoded bytes and every unresolved splice applied at its translated offset (R6.TREE.12, R6.TREE.13). A
failure of the keys, types, encoding, a hash, the boundaries, disjointness or splice identity is FAIL
`record-invalid`; a failure of the occurrence or of containment fails RC14; a composition that differs fails RC7; in
each case the resolution does not apply and the path stays `base-drift`. **Review confirmation.** Each resolution is
the item `<path>:resolution:<splice>` of the record (R6.RECON.30). The review's verdict entry on it carries `confirms`,
`{start_M, end_M, sha256, resolved_sha256}`, equal to the resolution's, and its verdict `accept` confirms that window
and those replacement bytes: that the window covers every byte `M` changed in the splice's context, and that each byte
`M` changed inside the window is kept in the replacement bytes or that dropping it is justified. A verdict entry
without `confirms`, a `confirms` that differs from the resolution, or no verdict on the item is FAIL `record-invalid`,
and the resolution does not apply.'''

ADAPT2_OLD = ('`splices [{id, file, start, end, old_sha256,\nnew_sha256, new}]` (byte spans at `base`); `files {path: '
              '{base_sha256, expected_sha256}}`;\n`retained [{id, site_ref}]`;')
ADAPT2_NEW = ('`splices [{id, file, start, end, old_sha256,\nnew_sha256, new, raw}]` (byte spans at `base`); `files {path: '
              '{base_sha256, expected_sha256, raw}}`;\n`edits [{id, file, raw}]`, every entry of the edit list in '
              'edit-list order, retained edits included; `retained [{id, site_ref, text}]`, with `text` the bytes of the '
              'retained edit\'s pair selected at `base` (R6.RECON.24 (b)); each `raw` is the ledger\'s or edit list\'s own '
              'entry, unchanged, which R6.RECON.30\'s `ledger_binding` and R6.RECON.26\'s edit-list hashes read, so that '
              'the engine reads nothing outside the interface (R6.CORE.4); the ledger and the edit list are parsed '
              'strictly (R6.RECON.29), and a parse failure, or a number other than an integer in a value the engine '
              'hashes, is ERROR `LEDGER_INTEGRITY` %s;' % MARK)

R29 = '''
### 23.1 Schema contract of the reconciliation record kinds

**R6.RECON.29** **Common encodings and malformed input** %(mark)s. This requirement and R6.RECON.30
to R6.RECON.36 state, for the record kinds of the reconciliation route (reconciliation, review, reassessment, edit-id
migration and side-change class records), for the configuration's references to them and for the result fields of the
route, the field names, types, encodings, data sources, identity bindings, item ids, review requirements and
mechanical acceptance conditions that the requirements they cite state by meaning (owner decision of 2026-11-26, #1169
comment 7189470338, item 4). Each kind is specified once, by its key tables, each with a table id; the tables are
normative. Each definition below is stated once and cited elsewhere.

| Term | Encoding |
|---|---|
| commit id | a JSON string of 40 lowercase hexadecimal characters, the full git object id of a commit |
| blob id | a JSON string of 40 lowercase hexadecimal characters, the git object id of a blob |
| sha256 | a JSON string of 64 lowercase hexadecimal characters, the SHA-256 of the raw bytes named |
| offset | a JSON number written as an integer, with no fraction or exponent (not `5.0`, a boolean or a string), at least 0, counting bytes from 0; a span `[start, end)` excludes `end`, as the ledger's byte spans do (R6.ADAPT.2) |
| path | a JSON string giving the exact git tree path: relative to the repository root, `/`-separated, with no leading or trailing `/` and no empty, `.` or `..` component; compared byte for byte, without case folding or Unicode normalization |
| reference | `{path, blob_sha256}`: a path and the sha256 of the blob's raw bytes. A record's identity is its reference in every rule: two byte-identical copies at two paths are two records |
| identity string | `author` and `reviewer`: a GitHub login, not a run, check, Issue or URL (R6.REC.6). Two identity strings are equal when they are equal after removing leading and trailing whitespace and Unicode case folding |
| time | `YYYY-MM-DDTHH:MMZ` or `YYYY-MM-DDTHH:MM:SSZ`, in UTC |
| canonical base64 | RFC 4648 sec. 4, standard alphabet, `=` padding, no other character, and equal to the re-encoding of its decoded bytes |
| canonical JSON | the bytes that Python's `json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False)` produces, encoded as UTF-8: keys sorted by code point, no whitespace, non-ASCII characters written as themselves; a hashed value holds no number other than an integer. The canonical sha256 of a value is the sha256 of these bytes (R6.RECON.5, R6.RECON.25, R6.RECON.26, R6.RECON.27) |
| strict parse | the bytes are UTF-8 without a byte-order mark and hold one JSON value, an object; a duplicate key in any object, or `NaN`, `Infinity` or `-Infinity`, is a parse failure |

Every encoding is a match of the whole string: no leading or trailing character, a trailing newline included (a full
match, not a search ending at `$`). The types of the key tables are these encodings, `string`, `non-empty string`,
`integer`, `array`, `object`, a quoted literal, and their combinations as written. A record fails its schema when a
required key is missing, a value has another type or encoding, a key appears that its table does not list, or it fails
strict parsing. A schema failure of a record a run reads is FAIL `record-invalid`, decided before any condition
RC1-RC14 is evaluated, and the record does not apply: a malformed field is never reported only as a failed condition,
and the path the record would cover stays `base-drift` (R6.TREE.7). A schema failure never loses a finding
(R6.RECON.26, Form of a finding (i)).

**Conformance mutants.** From the same single definition of the key tables, the generator of this design writes the
list `CONFORMANCE-MUTANTS.json` by a fixed rule: for each table, each required key removed and one unlisted key added;
for each key, one value of each JSON type the key does not admit; and for each encoding of the table above, its named
near-miss variants with the correct JSON type (upper case, one character short and a trailing newline for the
hexadecimal ids; `5.0` and a negative value for an offset; a leading or trailing `/`, an empty, `.` or `..`
component for a path; a URL for an identity string; no zone or a space for a time; unpadded or broken base64; the empty
string for a non-empty string; a trailing space or another case for a literal; an unlisted value for an enumeration;
an empty array where one element is required). A nested table is mutated at one occurrence in its kind's positive
record. Each mutant has the id `(table, key path, violation)`. For every mutant the tool's result carries a
`record-invalid` item naming that key path and reports no condition RC1-RC14 for the mutant record; the gate checks
that the mutant ids its records carry equal the list. The list is also the check that any machine schema the tool
carries agrees with the tables: no other comparison is made.
Sources: PR #1593 comments 7189621405, 7190234470 and 7190609504. Controls: RECON-SCHEMA, CANON-JSON.

**R6.RECON.30** **`oi-reconciliation/2`: fields, item ids and acceptance** %(mark)s. The fields that
R6.RECON.1 names by meaning:

%(t_recon)s

Beside the tables the tool checks: that each entry's `path` occurs once; that each entry's `splices` lists exactly the
ledger's splices of the path, in ledger order (an extra, missing or reordered element is FAIL `record-invalid`);
`end_M`; the `translation` value (RC5, R6.RECON.10); the edit ids against the configuration `configuration` names, not
the run's, so that a revised plan that removes an edit does not turn an earlier entry into a form failure; and the
executed-path floor. **Executed paths.** A path is executed by a check, for the mechanical floor, when its name ends
in one of the configuration's `executed_suffixes` (R6.CFG.4), which contain at least `.py`, `.lean`, `.yml`,
`.yaml` and `.sh`, or a delegation class of the configuration covers it (sec.
13); for such an entry `method` contains the entry's `l` blob id in full, or the record fails its schema. Any other
path that a check executes (an extensionless script, a file type outside the list) carries the same obligation under
R6.RECON.25, and the review's `accept` on `<path>:scientific_effect` confirms that `method` names the check re-run at
`l`; that the check was re-run, and its result, rest on the review in both cases.

"Changes the path" means, for RC1 and for drift alike (R6.RECON.22), that the path's tree entry (mode and object id,
absence counted as an entry) in the commit differs from that in its first parent; a change of mode alone is therefore a
drift, and its commit is listed. A path absent at `M` or at `X` has no blob there: RC2 or RC8 fails, and the path stays
`base-drift`. `x` is read at `X`; R6.RECON.21's binding reads it at `X`, which is `C` in RT-L2.

The record's item ids are, for each entry, `<path>`, `<path>:scientific_effect` and, for each resolution,
`<path>:resolution:<splice id>`. The verdict `accept` on `<path>` confirms that the reviewer re-derived from the object
store the entry's `side_change_commits`, `ledger_binding`, blob ids and sha256 values, splice offsets and translations
and protected ranges, and the record's `M`, `X`, `ledger_base` and `changes_decisions_on_X` as they bear on the path;
on `<path>:scientific_effect` it confirms what R6.RECON.25 states, and on a resolution item what R6.RECON.24 states.
Sources: PR #1593 comments 7189621405 and 7190234470. Controls: RECON-SCHEMA, RECON-FIELDS.

**R6.RECON.31** **`oi-review-record/1`: fields, item ids and widening** %(mark)s.

%(t_review)s

The key set of a verdict entry is closed: a future verdict datum needs a change of this design, which is accepted
knowingly. A reserved prefix for unread keys is not provided, because an unreviewed key could carry meaning; moving to
a new schema id would not hide a finding from an older pinned tool, whose detection reads any schema beginning
`oi-review-record/` (R6.RECON.35). `reason` is required in every verdict entry, and `method` must name a full object
id; existing review fixtures that lack them are rewritten (no expectation value changes).

Item ids, by the kind of the reviewed record:

| Reviewed kind | Item ids |
|---|---|
| `oi-reconciliation/2` | as R6.RECON.30 states |
| `oi-reassessment/1` | `finding`, `repair`, `edit`, `rederivation`, `verdict` |
| `oi-edit-id-migration/1` | `migration:<old>` for each element of `migrations`, and `approval` |
| `oi-side-change-classes/1` | the `id` of each element of `classes` |
| `oi-term-rules/2` | the `id` of each element of `rules` |
| `oi-hp-adjudication/1` | the `site_id` of each element of `sites` (R6.HP.4) |
| `oi-context-adjudication/1` | the `id` of each element of `entries` (R6.CTX.7) |
| `oi-hit-classification/1` | the `id` of each element of `classifications` (R6.HIT.4) |
| a kind without an item list (`oi-scope/1`, `oi-delegation/1`) and the configuration | the single item `record_id`, for the configuration `config_id` |

A review whose `item` values are not exactly these ids fails record lint (R6.REC.6). A widening review covers the items
of the difference between the superseding record (`reviewed`) and the superseded one (`replaces`): for a kind with an
item list, the id of each element added, removed or changed (elements matched by id), and `field:<key>` for each other
top-level key whose value differs, `supersedes`, `version` and the item list excluded; for the configuration,
`field:<key>` for each top-level key whose value differs. The configuration's widening review is a review record of
kind `"widening"` listed in `records` with kind `review` (R6.RECON.33); the configuration has no `widening_review` key,
and one is an unknown field (R6.VALID.2).
Sources: PR #1593 comments 7189621405 and 7190234470. Controls: REVIEW-SCHEMA, RECON-SCHEMA.

**R6.RECON.32** **`oi-reassessment/1` and `oi-edit-id-migration/1`: fields and location** %(mark)s.

%(t_reassess)s

Both kinds lie, with their review records, in the plan's record directory (`D_rec`, R6.RDIR.1) of the configuration
that references them, and are read by their reference; a referenced record outside it is FAIL `record-invalid`.
Sources: PR #1593 comment 7189621405 (C, G). Controls: REASSESS-KEYS, MIGRATION-RECORD, RECON-SCHEMA.

**R6.RECON.33** **Configuration references, resolution and lineage** %(mark)s. The kinds of `records`
(R6.CFG.4) and the schema each requires:

| Kind | Schema |
|---|---|
| `review` | `oi-review-record/1` |
| `hp-adjudication` | `oi-hp-adjudication/1` |
| `context-adjudications` | `oi-context-adjudication/1` |
| `hit-classifications` | `oi-hit-classification/1` |
| `scope` | `oi-scope/1` |
| `side-change-classes` | `oi-side-change-classes/1` |
| `reconciliation` | `oi-reconciliation/2` |
| `reassessment` | `oi-reassessment/1` |
| `edit-id-migration` | `oi-edit-id-migration/1` |

A kind outside this table, or a referenced record whose schema is not its kind's, is ERROR `CONFIG_INVALID` (R6.VALID.3:
an undefined record kind); no reference is skipped. `roles.side_change_classes` names a reference that also appears in
`records` with kind `side-change-classes` and the same blob, and RC11 and the tool-landing domain read that one record;
otherwise ERROR `CONFIG_INVALID`. `retirement` is `{name, issue}`: `name` a non-empty string, `issue` a positive integer,
the number of the accountable Issue. A key that R6.CFG.4 does not list, at the top level or inside a member whose keys
it lists, such as a check's `default_for` or a top-level `widening_review`, `notes` or `sites`, is an unknown field:
ERROR `CONFIG_INVALID` (R6.VALID.2). An op B or op D run without `--check` is USAGE (R6.OUT.6): no default check is
defined.

**Resolution of a reference.** A reference to a configuration or record that is not read at its path in the anchor
commit is resolved by walking the anchor's first-parent chain towards the root: it resolves at the newest commit whose
tree holds the path with a blob of that sha256 (R6.REC.17 states this walk). The anchor depends on the admission mode:
in a chain-admitted run it is `F`; a reconciliation record admitted by the post-freeze route, and its review, are read
at their paths in `REV`'s tree (R6.RECON.2 (d)), and the references they carry are resolved from `F`; in a
control-harness run, which has no `F` (RT-L2, R6.RECON.21), a reference equal to the control-supplied configuration's
reference resolves to that configuration, and any other is resolved from `REV`, or, when no `REV` is named, from the
commit the record is read from (R6.RECON.21). A reference that no commit on the
chain holds names no record: FAIL `record-invalid` for a record, ERROR `CONFIG_INVALID` for a configuration. The search
resolves the configurations named by `supersedes` (R6.REC.7, R6.CFG.3) and by R6.RECON.26 (iii), and the migration
records of R6.RECON.28; the finding and the repair entry of R6.RECON.27 are read from the scans at `M` instead.

**Lineage.** The plan lineage of a finding is every configuration on whose `supersedes` chain, itself included, the
finding's configuration lies, and every configuration that names the same retirement, by an equal `retirement.name`
or an equal `retirement.issue`. R6.RECON.26 and R6.RECON.28 use this definition.

**A revised plan on a new `H`.** The plan's record directory may hold no entry at `H` (Dir2, R6.RDIR.5), and the
admitted record directories are fixed by the tool (R6.A1CFG.1). A revised plan whose `H` follows the earlier plan's
landing therefore uses a new record directory, admitted by a tool revision that adds it to the tuple; its
configuration's `supersedes` names the earlier configuration at its own path, which the search above resolves. Dir2 is
unchanged.
Sources: PR #1593 comments 7189621405 and 7190234470. Controls: CONFIG-REFS, SUPERSEDES-RESOLVE, FINDING-LINEAGE.

**R6.RECON.34** **Side-change class records** %(mark)s.

%(t_class)s

A class-level `paths` list is not a form of this record, and a pin carries no `git_blob`: its integrity is its
`blob_sha256`, which a git object id would only restate. A superseding class record that adds a pin or a prefix, or
changes a pin's blob, widens the record it supersedes and needs a widening review (R6.REC.13), as a changed class widens
the configuration (R6.CFG.7).
Sources: PR #1593 comment 7189621405 (E). Controls: CLASS-SCHEMA, RECON-SCHEMA.

**R6.RECON.35** **Detection and the scanned set** %(mark)s. *Selection.* Detection (R6.RECON.26) reads every
regular file under `verification/audits/`, outside every prefix of the tool-landing class, the plan's record
directory included, whatever its name, whose raw leading bytes are an optional byte-order mark (UTF-8 or UTF-16),
then ASCII whitespace, then `{` or `[` (in UTF-16 after a UTF-16 byte-order mark). Its text is the file decoded as
UTF-8, or as UTF-16 after a UTF-16 byte-order mark, invalid bytes replaced by U+FFFD (a lossy decode, so that an
invalid byte does not take a file out of detection). A file that does not begin a JSON object or array is not a
record of any kind (R6.RECON.29), so prose that quotes a record is not read. *Classes of a selected file.* (a) A file that parses strictly as an object whose `schema` is exactly
`oi-reconciliation/1`, `oi-reconciliation/2` or `oi-review-record/1` is a record of that kind; its findings are read
under R6.RECON.26, Form of a finding (i). (b) Any other selected file in which some object, at any depth, has a
`schema` string that, after trimming and case folding, begins with `oi-review-record/` or `oi-reconciliation/`, or has
no `schema` key but a review's shape (a `reviewed` key and a `verdicts` entry carrying `invalidates` or `invalidated`),
the file parsed with duplicate keys and non-finite numbers admitted for this test only, is a malformed record: FAIL
`record-invalid`. (c) A selected file that does not parse even so, and whose lossy text, with JSON `\\uXXXX` escapes
resolved and case folded, contains `oi-review-record/` or `oi-reconciliation/`, is a malformed record likewise. A malformed
record whose text, with escapes resolved, also contains `invalidates` or `invalidated` is a malformed finding, which
binds at run level (R6.RECON.26, Form of a finding (iv)). *The scanned set* of R6.RECON.2 (d) and (e) is the records of
class (a) outside the plan's record directory. *Identity.* Record identity is the reference (R6.RECON.29): two
byte-identical files at two paths are two records, for R6.RECON.2 (e) and for findings alike. *Review location.* The
review records of a reconciliation record lie in its directory (R6.RECON.1, R6.RECON.2 (d)), and a review elsewhere is
not its review for record lint; detection reads review records wherever they lie among the selected files, and one
elsewhere that carries a finding counts, as a form failure. *Residuals.* Three changes to a landed finding record are
not caught by detection: its deletion from `main`; leading bytes that do not begin a JSON value added to it (a stray
character, a comment line, a NUL); and its storage under a prefix of the tool-landing class, where an unpinned file is
REVIEW_REQUIRED `side-change-unclassified` at the run, visible but not blocking. Each needs a landed change to `main`
under the owner's merge approval; they are tracked together in Issue #1598.
Sources: PR #1593 comments 7189621405, 7190234470, 7190255132 (D1) and 7190609504 (B). Controls: SCAN-PARSE.

**R6.RECON.36** **Result fields of the reconciliation route** %(mark)s. An op C result with `M` carries:
- `dispositions`: one entry for each drifted ledgered or corpus path (R6.RECON.22), `{path, disposition, category,
  record, failed, conflicts, why}`: `disposition` one of `reconciled`, `reconciled-resolved`, `base-drift` and
  `retirement-blocked`; `category` 1, 2 or 3 where R6.RECON.22 assigns one, otherwise null; `record` the reference of
  the record whose entry for the path applies, or null; `failed` an array with one element `{record, conditions}` for
  each admitted record that covers the path (its reference, and the names of the conditions it fails: `RC1` to
  `RC14`, `reconciled-state`), or the single element `{record: null, conditions: ["no-record"]}` when none covers it;
  `conflicts` an array of splice and site ids; `why` a string, a diagnostic;
- `category3`: `{findings, blocked, reassessments}`: `findings` `[{record, item}]`, with `record` a reference and
  `item` as R6.RECON.27's `finding.item`; `blocked` `[{record, item, edit}]`, `edit` null for a run-level binding;
  `reassessments` the references of the applying reassessments;
- `inputs.classify_records` `[{rev, path, sha256, review: {path, sha256}}]` and `inputs.record_base`, a commit id or
  null (R6.RECON.2 (c)).

R6.OUT.18 lists these fields, and the result's JSON Schema file carries them.
Sources: PR #1593 comments 7189621405 (A, H) and 7190234470 (S3). Controls: RECON-ENUM.
'''

RECON_ENUM_CASE = {'case': 'the same result: each dispositions entry carries path, disposition, category, record, '
                           'failed (one element per covering record, or no-record), conflicts and why; category3 carries '
                           'findings, blocked and reassessments; inputs.classify_records entries carry the review, and '
                           'inputs.record_base is present (R6.RECON.36) (positive)',
                   'outcome': 'PREDICATE', 'invariants': [{'schema_errors': []}]}
RECON_ENUM_COUNTER = {'case': 'countercase: the same result with a dispositions entry whose failed is a flat list of '
                              'condition names, or whose record is missing',
                      'outcome': 'PREDICATE', 'invariants': [{'schema_errors': ['dispositions entry not of the '
                                                                                'R6.RECON.36 form']}]}

RECON23_OLD = ('by fingerprint,\nthe tree field excluded, counting multiplicities: a fingerprint found k times at the landing and j times at '
               '`X` gives\nk - j new findings when k > j.')
RECON23_NEW = ('by a matching key %s, not by\nfingerprint (an item\'s fingerprint includes its subject\'s line number, so a line '
               'that `M`\'s changes move would\nappear new): for an item with a file and line, the key is its class, its file, its '
               '`rule_id` or, without one, its\nprofiles, and the sha256 of the text it matched on (its line, or for a '
               'sentence-level item its sentence),\nthe line number, the segment and the tree excluded; for an item without '
               'a line, the key is its class, its\nsubject and its fingerprint. Keys are counted with multiplicity: a key '
               'found k times at the landing and j\ntimes at `X` gives k - j new findings when k > j, so a line that `M` '
               'moves gives none and a second copy of\na line gives one; when several new findings share a key, each is '
               'reported, at the landing\'s positions of the\nlast k - j occurrences in file order.' % MARK)
GATE3_OLD = ('  - `<unit>[k=v,...]` with unit `items`, `lines`, `sentences`, `hits` or `findings`, counted over the\n    '
             'result. Filter keys are item fields (`obligation`, `class`, `decision`, `rule_id`, `profile`,\n    `file`, '
             '`subject`, `segment`, `state`, `path`, `literal`, `only_profile`). `|` separates\n    alternatives.')
GATE3_NEW = ('  - `<unit>[k=v,...]` with unit `items`, `findings`, `hits`, `sites`, `lines`, `fail_lines` or `sentences`,\n'
             '    counted over the result %s. A filter key is a field of the counted object: an item field for\n'
             '    `items`, `findings`, `lines`, `fail_lines` and `sentences` (for example `obligation`, `class`, `decision`,\n'
             '    `rule_id`, `alternatives`, `profile`, `file`, `line`, `subject`, `segment`, `state`, `path`, `literal`,\n'
             '    `only_profile`, `attribution`, `key_path`), a hit field for `hits`, a site field for `sites` (for\n'
             '    example `moved_in`). `k=v` holds when the field equals `v` or, for a list-valued field, contains `v`;\n'
             '    `|` separates alternative values; `k_nonempty` holds when the field is present and non-empty.\n'
             '    `items`, `findings`, `hits` and `sites` count objects. `lines` counts distinct `(file, line)` pairs,\n'
             '    an item\'s `line` being the line on which its match begins: a sentence-level item (one whose sentence\n'
             '    spans several lines) counts once, at that line, and several items on one line count once.\n'
             '    `fail_lines` is `lines` over the items whose decision is FAIL. `sentences` counts distinct sentences,\n'
             '    each identified by its file and its start line. The modifier `count_sentence_lines=true`, which is\n'
             '    not a field, makes `lines` and `fail_lines` count every line that the sentence of each sentence-level\n'
             '    item spans.' % MARK)

GATE17 = """
**R6.GATE.17** **Classifying a failing row** %s. When a gate run gives a row FAIL, or NOT RUN outside its
allowance, its cause is classified, in the review of that run and never in the expectation file, with one of four
statuses: `expectation-defect` (the expectation misstates what a governing requirement asks, for example a misnamed
count key or a value contradicting it); `implementation-defect` (the tool, a runner or the evidence it retains does not
do what the design requires); `verification-failure` (the tool correctly finds that the subject or its records do not
meet the design); or `unresolved`. A row is `unresolved` whenever the retained evidence does not settle which of the
other three applies, and its classification names the evidence that would settle it; no row is forced into one of
the other three. No classification changes an expected value or weakens an intended check: an expectation defect is
corrected only by an owner-approved expectation change that names the governing requirement, and an implementation
defect or a verification failure is never resolved by editing the expectation. A classification is review
information: it confers no status, and the row keeps the status the gate computed (R6.GATE.9).
Sources: owner decision of 2026-11-26 (#1169 comment 7190776267, item 3).
""" % MARK
RECON_TRIAL_CASE = {'case': 'a finding at X on a line that M\'s changes move (lines inserted above it): matched at the '
                            'landing by its key, the line number excluded; no new finding (positive)',
                    'outcome': 'ANY', 'invariants': [{'not_class': ['base-drift', 'record-invalid']}]}


MISSING = '(absent)'
RT_DR_OLD = ('countercase: at H with the DR-1 alternative-a match at book/The-Incompleteness-of-Observation-FULL.md:6504 '
             'removed (one target missing): the target item is absent')
RT_DR_NEW = ('countercase: at H with the DR-1 alternative-a match at book/The-Incompleteness-of-Observation-FULL.md:6504 '
             'replaced by neutral text on the same line (the line is kept, so no later line is renumbered; one target '
             'missing): the target item is absent')
RTL2_OLD = ('countercase: the same reconciled drift with a planted non-delegated REVIEW item that touches no '
            'reconciliation (an unclassified review hit on an unledgered line): the drift stays reconciled and the '
            'positive predicate (REVIEW_REQUIRED only from delegated classes) fails')
RTL2_NEW = ('countercase: the same reconciled drift with a planted non-delegated REVIEW item that touches no '
            'reconciliation: a hit on a line unchanged across H, M and X, surfaced by a review profile present only in '
            'the countercase configuration, so that no path changes and no side change is added, and unclassified: the '
            'drift stays reconciled and the positive predicate (REVIEW_REQUIRED only from delegated classes) fails')
RT_D_WHY_OLD = 'no mutation, but a positive control asserting acceptance of the 11 W1/W2 lines by their allow rules'
RT_D_WHY_NEW = ('no mutation, but a positive control asserting acceptance of the 10 W1/W2 lines by their allow rules, '
                'with the superseding rule file that drops W1-a')
RT_D_FLAG = ('amendment 6 (amendment 5 delta review, PR #1592 comment 7189385508, nit 3): the count of 10 W1/W2 PASS '
             'lines and the SM:1394 site hold only with the superseding rule file that drops W1-a, under the owner\'s '
             'decision on the W1-a row (amaybaum, 2026-11-26T07:55:49Z, #1169 comment 7185991140); rule content is '
             'plan content (R6.DENY.1), and until that rule file is written and reviewed RT-D is not run against these '
             'figures')
# every change to a row that amendment 5 left: (row id, path, old value, new value); nothing else may differ
DECLARED_DIFFS = [
    ('RECON-BLOCK', ('expect', 'cases', 12, 'case'), RECON_BLOCK_OLD, RECON_BLOCK_NEW),
    ('RECON-ENUM', ('requirements', 1), MISSING, 'R6.RECON.36'),
    ('RECON-ENUM', ('requirements', 2), MISSING, 'R6.OUT.18'),
    ('RECON-ENUM', ('expect', 'cases', 3), MISSING, RECON_ENUM_CASE),
    ('RECON-ENUM', ('expect', 'cases', 4), MISSING, RECON_ENUM_COUNTER),
    ('L2', ('expect', 'invariants', 0, 'all'), 'lines[rule=W2]', 'lines[rule_id=W2]'),
    ('RECON-TRIAL', ('expect', 'cases', 7), MISSING, RECON_TRIAL_CASE),
    ('S11-2a', ('expect', 'sites', 0, 'added_relative_to_unmutated'), MISSING,
     {'items[class=unclassified,subject=$new_line]': 1}),
    ('RTL2-BIND', ('expect', 'cases', 6, 'case'), RTL2_OLD, RTL2_NEW),
    ('RT-D', ('direction', 'why'), RT_D_WHY_OLD, RT_D_WHY_NEW),
    ('RT-D', ('expect', 'sites', 1, 'classes_exact'), MISSING, ['unclassified']),
    ('RT-D', ('flags', 6), MISSING, RT_D_FLAG),
    ('RT-DR', ('expect', 'cases', 3, 'case'), RT_DR_OLD, RT_DR_NEW),
]
# order-preserving renames of count keys to the grammar of R6.GATE.3 (tool writer, 2026-11-26): (row, path of the
# dict, old key, new key); each is checked by the guard as a removed and an added leaf with the same value
DECLARED_KEY_RENAMES = [
    ('L2', ('expect', 'counts'), 'lines[rule=W2,state=PASS]', 'lines[rule_id=W2,state=PASS]'),
    ('RT-D', ('expect', 'counts'), 'lines[state=PASS,rule=W1|W2]', 'lines[state=PASS,rule_id=W1|W2]'),
    ('RT-DR', ('expect', 'cases', 0, 'counts'), 'lines[rule=DR-1]', 'lines[rule_id=DR-1]'),
    ('RT-DR', ('expect', 'cases', 0, 'counts'), 'lines[rule=DR-1,alternative=a]', 'lines[rule_id=DR-1,alternatives=a]'),
    ('RT-DR', ('expect', 'cases', 0, 'counts'), 'lines[rule=DR-1,alternative=b]', 'lines[rule_id=DR-1,alternatives=b]'),
    ('RT-DR', ('expect', 'cases', 0, 'counts'), 'lines[rule=DR-1,alternative=c]', 'lines[rule_id=DR-1,alternatives=c]'),
    ('RT-DR', ('expect', 'cases', 0, 'counts'), 'lines[rule=DR-3]', 'lines[rule_id=DR-3]'),
    ('RT-DR', ('expect', 'cases', 0, 'counts'), 'lines[rule=DR-4]', 'lines[rule_id=DR-4]'),
    ('RT-DR', ('expect', 'cases', 0, 'counts'), 'lines[rule=DR-5]', 'lines[rule_id=DR-5]'),
    ('RT-DR3W', ('expect', 'cases', 0, 'counts'), 'sentences[rule=DR-3]', 'sentences[rule_id=DR-3]'),
    ('RT-DR3W', ('expect', 'cases', 1, 'counts'), 'sentences[rule=DR-3]', 'sentences[rule_id=DR-3]'),
]
# amendment 5 r2's own strengthenings, pinned so that no later edit reverts them (delta review nit 4)
PINS = [
    ('L2', ('expect', 'counts', 'lines[rule_id=W2,state=PASS]'), 4),
    ('L2', ('expect', 'invariants', 0, 'all'), 'lines[rule_id=W2]'),
    ('V7a', ('expect', 'invariants', 0, 'items_include', 0, 'subject'), '$planted'),
    ('V23', ('expect', 'invariants', 1, 'items_include', 0, 'subject'), '$planted'),
    ('V24', ('expect', 'invariants', 1, 'items_include', 0, 'subject'), '$planted'),
    ('R18', ('expect', 'sites', 0, 'decision'), 'REVIEW_REQUIRED'),
    ('RT-D', ('expect', 'counts', 'lines[state=PASS,rule_id=W1|W2]'), 10),
    ('RT-D', ('expect', 'classes_exact'), ['unclassified']),
    ('RT-D', ('expect', 'sites', 1, 'subject'), 'papers/SM.md:1394'),
    ('RT-DR', ('expect', 'cases', 0, 'invariants', 0, 'items_include', 2, 'file'), 'book/ch09-universality.md'),
    ('RT-DR', ('expect', 'cases', 3, 'invariants', 0, 'none'),
     'items[rule_id=DR-1,file=book/The-Incompleteness-of-Observation-FULL.md,line=6504]'),
    ('RTL2-BIND', ('expect', 'cases', 6, 'invariants', 1, 'items_include', 0, 'subject'), '$planted'),
    ('S11-2a', ('expect', 'classes_include'), ['unclassified', 'deny-match']),
    ('U14', ('expect', 'cases', 1, 'sites', 0, 'classes_exact'), ['provenance-mismatch']),
]

# cases of the r2 draft (319e9bbf) that r3 removes or merges, each with the case that covers it (simplification;
# both reviews, PR #1593 comments 7190234470 and 7190255132)
REMOVED_R2 = [
    ('RECON-BLOCK', 'a revised plan whose ledger changes the invalidated edit\'s edit-list entry (a wording change, the same '
     'id and target) and cites no reassessment', 'BLOCK-KEY',
     'the edit\'s wording changed in a revised configuration (new bytes or reason; the same id and target), no '
     'reassessment cited'),
    ('FINDING-LINEAGE', 'a finding naming its configuration; a later configuration on that configuration\'s supersedes '
     'chain carries the edit', 'SUPERSEDES-RESOLVE',
     'a finding made under version 1 binds version 2, resolved in that way, which carries the edit'),
    ('FINDING-LINEAGE', 'a finding whose invalidated element differs from the named configuration\'s ledger (the id '
     'absent there, or another target): the fallback binds every configuration carrying the id, a migrated id or the '
     'target', 'FINDING-KEYS', 'an element whose id is absent from the named configuration\'s ledger: the fallback binds '
     'every configuration carrying the id, a migrated id or the target'),
    ('REASSESS-KEYS', 'a reassessment whose repair.commits holds an abbreviated commit id, or a commit not on M\'s '
     'first-parent chain', 'REASSESS-FORM', 'a reassessment whose repair names no commit on M\'s first-parent chain'),
    ('REASSESS-KEYS', 'a reassessment whose rederivation is not a non-empty string, or which carries a key outside the '
     'table', 'REASSESS-FORM', 'a reassessment with an empty re-derivation of the edit\'s justification'),
    ('MIGRATION-RECORD', 'a migration record whose approval lacks quote, author or time, or whose time is not of the '
     'stated form; the renamed edit\'s old bytes unchanged', 'RECON-SCHEMA',
     GENERIC_CASE),
    ('RESOLUTION-SCHEMA', 'countercase (window): a float (5.0), boolean or string offset', 'RECON-SCHEMA',
     'countercase: an offset written 5.0, or true, in a splice, a protected range or a resolution'),
    ('RESOLUTION-SCHEMA', 'countercase: a resolution carrying a key outside the six', 'RECON-SCHEMA',
     GENERIC_CASE),
    ('RECON-SCHEMA', 'countercase: changes_decisions_on_X null, {} or ""', 'RECON-SCHEMA',
     'countercase: changes_decisions_on_X missing, null, {} or ""'),
    ('RECON-SCHEMA', 'countercase: a splice without start_M', 'RECON-SCHEMA',
     GENERIC_CASE),
    ('RECON-SCHEMA', 'countercase: a protected range with a non-integer offset', 'RECON-SCHEMA',
     'countercase: an offset written 5.0, or true, in a splice, a protected range or a resolution'),
    ('RECON-SCHEMA', 'countercase: a key outside the table, at the top level or in an entry', 'RECON-SCHEMA',
     GENERIC_CASE),
    ('RECON-SCHEMA', 'countercase: an entry path with a leading /, a . or .. component, or a trailing /', 'RECON-SCHEMA',
     GENERIC_CASE),
    ('RECON-SCHEMA', 'countercase: M, X or ledger_base in upper case or abbreviated', 'RECON-SCHEMA',
     GENERIC_CASE),
    ('RECON-SCHEMA', 'countercase: a record without record_id', 'RECON-SCHEMA',
     GENERIC_CASE),
    ('RESULT-FIELDS', '(row merged)', 'RECON-ENUM', RECON_ENUM_CASE['case']),
    ('WIDENING-ITEMS', '(row merged)', 'REVIEW-SCHEMA',
     'a widening review of kind widening with replaces naming the superseded blob and one verdict for each item id of '
     'the difference rule, all accept (positive)'),
]

POINTS = [
    ('1. A review-record finding (R6.RECON.26, second kind)',
     ['(a) The verdict entry on `<path>:scientific_effect` counts as a finding whenever it carries a non-empty '
      '`invalidated`, whatever its verdict value. Safe against loss, but it makes an `accept` that also lists '
      '`invalidated` ambiguous.',
      '(b) A dedicated verdict value, `invalidates`, plus `invalidated`. Unambiguous. Using `reject` instead would overload '
      'a value that also means "wrong for other reasons", so a plain rejection could not be told from a finding.'],
     'Proposal: (b) with the value `invalidates`, permitted on `scientific_effect` items only, and detection before '
     'lint (r2, review finding 3): any non-author review carrying `invalidates` or `invalidated` on any item counts; '
     'every lint failure other than an independence failure is a form failure that still blocks. Reasoning: '
     'R6.RECON.26 already says the review "finds that the change invalidates", and R6.REC.6 makes every non-`accept` '
     'verdict a failure of the reviewed record, so a separate value fits both without changing R6.REC.6.',
     'FINDING-FORM'),
    ('2. Lineage scope',
     ['(a) Bind every configuration whose ledger carries the edit. Never loses a block, but over-blocks another '
      'retirement that reuses the edit id.',
      '(b) The finding names the configuration it was made under, `{path, blob_sha256}`; the lineage of amendment 4 is '
      'computed from it.'],
     'Proposal: (b) for the id and migration matches, with the path-and-old-bytes match applied to every configuration '
     'whatever its lineage (r2, review finding 1), and (a) by id, migrated id or target as the fail-closed fallback '
     '(review finding 2). Reasoning: amendment 4 defines the lineage from "the configuration the finding was made '
     'under", which only (b) makes readable from git objects; the global target match closes the fork escape; the '
     'fallback keeps the owner\'s rule that a finding cannot be lost.',
     'FINDING-LINEAGE'),
    ('3. Where a recorded migration lives',
     ['(a) No location: only the path-and-old-bytes match is implementable. The owner\'s row "Block follows the recorded '
      'migration" would then rest on the mechanical match alone, and a rename that also rewrites the old bytes would '
      'escape it.',
      '(b) A reviewed record `oi-edit-id-migration/1`, referenced by the configuration with kind `edit-id-migration`, '
      'followed through the `supersedes` chain.'],
     'Proposal: (b), with the mechanical match kept in addition, so a missing or invalid migration record can never '
     'lift a block; a mapping only adds edits. Under (b) a rename that also rewrites the old bytes is caught only when '
     'its migration is recorded and referenced; otherwise the residual of R6.RECON.26 remains (it rests on the review '
     'of the new freeze). Reasoning: AGENTS.md sec. A.48 item 3 requires the migration to be recorded and approved; '
     'reading it from the configuration\'s references keeps it pinned at the freeze.',
     'MIGRATION-RECORD'),
    ('4. Key names inside `invalidated`',
     ['(a) `{id, sha256}` as the amendment-3 code reads: loses the target that amendment 4 requires for the '
      'path-and-old-bytes match.',
      '(b) The writer\'s proposal `{id, sha256, target: {path, start_H, old_sha256}}`, the target copied from the ledger '
      'edit of the same id at the named configuration\'s `H`.'],
     'Proposal: (b), with `id` an edit id of the edit list (a retained edit included, its target the occurrence of its '
     'text at `H`; audit ranked item 2). A mismatch or a missing key is a form failure that blocks through the '
     'fallback.',
     'FINDING-KEYS'),
    ('5. RECON-BLOCK versus amendment 4',
     ['The RECON-BLOCK countercase expected no block for a revised plan that only changes the edit\'s entry; amendment 4 '
      'keeps the block for a wording change unless the freeze cites an applying reassessment.'],
     'Correction: the RECON-BLOCK countercase now requires the cited reassessment naming the finding, and a case is '
     'added in which a wording change without a reassessment stays blocked. This follows R6.RECON.26 as amended by '
     'amendment 4, which governs over Table 17.1.',
     'RECON-BLOCK'),
]

REVIEW_MAP = [
    ('1', 'Fork escape. R6.RECON.26: the amendment-4 sentence and Form (v) apply the path-and-old-bytes match to every '
          'configuration, whatever its lineage; the id and migration matches stay lineage-scoped. FINDING-LINEAGE '
          'gains the two fork cases, and its countercase now states another target.'),
    ('2', 'Fallback. Form (iii): "carries" means the id, a migrated id or the path-and-old-bytes match, with no lineage '
          'restriction, and any mismatch between an `invalidated` element and the named configuration\'s ledger '
          'triggers the fallback. FINDING-LINEAGE cases on a missing configuration with an unrecorded rename, a '
          'mismatching element and a readable wrong configuration.'),
    ('3', 'Detection before lint. Form (i): a non-author review carrying `invalidates` or `invalidated` on any item is '
          'a finding; every other lint failure is a form failure that still blocks; only an independence failure '
          'disqualifies. FINDING-FORM cases on an omitted item, a duplicated item, a missing `method` and '
          '`invalidates` on another item; the independence countercase.'),
    ('4', 'Empty fallback set. Form (iv): it binds the lineage at run level, every configuration when the '
          'configuration cannot be resolved; remedy: a new freeze citing an applying reassessment that names the '
          'finding, with `edit` null. FINDING-FORM case and countercase.'),
    ('5', 'Reassessment keys (owner, #1169 comment 7188752730, item 2). R6.RECON.27 Keys: `finding` `{path, '
          'blob_sha256, item}`; `repair` `{commits, entry: {path, blob_sha256, entry_path}}`; `edit` `{id, sha256}` with '
          'the canonical sha256 of the citing configuration\'s entry; Form (ii): `start_H` and `old_sha256` at the named '
          'configuration\'s `H`. REASSESS-KEYS (new); FINDING-KEYS case on another commit\'s target.'),
    ('6', 'Over-blocking remedy. Form (v): a new freeze renaming the colliding id, through an AGENTS.md sec. A.48 item 3 '
          'migration where records cite it. The optional narrowing superseding finding is not adopted: it would let a '
          'later record reduce a finding\'s binding, which R6.RECON.26 excludes; the global target match and the '
          'rename remedy bound the over-blocking without it. FINDING-LINEAGE rename countercase.'),
    ('7', 'R6.RECON.28: (a) `approval` checked for form only (R6.REC.3); (b) lint against a repeated `old` or `new`, an '
          '`old` equal to its `new`, and a `new` in use on the `supersedes` chain; (c) the reviewer\'s option is '
          'declined: only referenced records apply, because R6.REC.4 and R6.REC.5 already forbid a run to use a record '
          'the configuration does not reference, and applying every record the scan finds would let a record written '
          'for another plan map this plan\'s ids, while the global target match already gives the fail-closed '
          'coverage; the residual is stated in R6.RECON.28 and in point 3 above. MIGRATION-RECORD cases on a chained '
          'closure, reuse, approval form and the unreferenced-record countercase.'),
    ('8', 'R6.REC.6: every review naming the record\'s blob counts. FINDING-FORM case 2 requires `retirement-blocked` '
          'only; the FINDING-KEYS countercase states that the kept edit\'s old bytes differ from every recorded '
          '`old_sha256`. FINDING-FORM countercase on a second, rejecting review.'),
    ('9', 'Not addressed, as directed (outside the amendment\'s scope); the coordinator raises it with the owner as an '
          'Issue.'),
    ('10', 'Nit: in R6.CFG.4 and R6.RECON.25 the amendment-6 parenthetical follows the amendment-4 one, and the stray '
           'comma is removed.'),
]

B_MAP = [
    ('B1', 'RC14 (b), retained-site line at `H`',
     ['(a) op C takes op B\'s `E..H` inputs: reuses a walk op C does not run, and makes the reconciliation depend on '
      'the provenance walk and its failure modes;',
      '(b) the line at `H` is found from the retained edit\'s own text (its pair selected at `H`), whose uniqueness at '
      '`H` R6.PROF.8 and whose identity at `H` and `X` R6.PIPE.15 already check; the site map identifies the site '
      'only;',
      '(c) a schema addition giving each retained site\'s line at `H`: a second statement of a fact the edit list '
      'already fixes, which needs its own consistency check.'],
     'Proposal: (b). Safety: the line is fixed by exact bytes that are unique at `H`; any change on `M` to those lines, '
     'or a second copy, fails RC14; no walk is added. The ledger interface\'s `retained` entry carries the text '
     '(R6.ADAPT.2). Controls: RECON-RETAINED (both directions).'),
    ('B2', 'R6.RECON.24 explicit-resolution schema',
     ['keys: the tool writer\'s `{splice, start_M, end_M, sha256, resolved, resolved_sha256}`, which the owner accepted '
      'with the meanings quoted in sec. 0.7;',
      'source of the resolved bytes: inline, in a lossless encoding (chosen), or read from `l` through an offset map '
      '(rejected: it makes the bytes the review confirms depend on a second mapping);',
      'confirmation: the review item `<path>:resolution:<splice>`, its verdict carrying `confirms` equal to the window '
      'and `resolved_sha256`.'],
     'Proposal: 0-based byte offsets into the entry\'s `m` blob, end exclusive, at UTF-8 character boundaries; base64 '
     '(RFC 4648 sec. 4, canonical) for `resolved`, chosen over UTF-8 text because no normalization on the way can alter '
     'it silently; the review confirmation bound to the window and `resolved_sha256`. Safety: every hash, boundary, '
     'containment, splice identity and the composed content are checked mechanically; a malformed resolution never '
     'applies. Controls: RESOLUTION-SCHEMA (both directions), with countercontrols for windows, hashes, encoding, '
     'replacement content, splice identity and review confirmation.'),
]

AUDIT_MAP = [
    ('A.1', 'top-level keys `schema`, `record_id`, `supersedes`, `author`', 'R6.RECON.30 table; `record_id` required (owner choice); RECON-SCHEMA'),
    ('A.2', 'commits `M`, `X`; `x` at `X` or `C`', 'R6.RECON.29 commit id, R6.RECON.30; `x` read at `X`, R6.RECON.21 corrected to `X` (= `C` in RT-L2); RECON-FIELDS'),
    ('A.3', 'path list and entry `path`', 'R6.RECON.29 path encoding; R6.RECON.30 `paths`, unique `path`; RECON-SCHEMA'),
    ('A.4', '`ledger_base`', 'R6.RECON.30: commit id equal to `H`'),
    ('A.5', '`changes_decisions_on_X`', 'R6.RECON.30: required array, RC12 only for `[]`; tool behaviour (missing key passes) contradicts the design; RECON-SCHEMA countercases'),
    ('A.6', '`ledger_binding`', 'R6.RECON.30 keys and values; R6.RECON.29 canonical JSON; R6.ADAPT.2 raw entries; CANON-JSON'),
    ('A.7', '`m`, `l`, `x` and their sha256; deletion at `M`', 'R6.RECON.29 blob id; R6.RECON.30: a path absent at `M` or `X` stays `base-drift`; RECON-FIELDS'),
    ('A.8', '`side_change_commits` and "changes the path"', 'R6.RECON.30: oldest first; tree entry (mode, object id), one definition for RC1 and drift; RECON-FIELDS'),
    ('A.9', '`splices[]`', 'R6.RECON.30: keys, `end_M`, list completeness; RC5 rewritten (R6.RECON.10: `"identity"` with prefix agreement, or an integer, 0 allowed); R6.RECON.29 offsets; RECON-SCHEMA'),
    ('A.10', 'protected ranges', 'R6.RECON.30 `protected`; malformed is `record-invalid`; RECON-SCHEMA'),
    ('A.11', '`scientific_effect.conclusions`', 'R6.RECON.30: `"none"` or an array, checked against the configuration in (iii); RECON-FIELDS'),
    ('A.12', '`assessment`, `method`, `verdict`; executed paths', 'R6.RECON.30: types; executed-path predicate and `method` contains `l` (owner choice); RECON-FIELDS'),
    ('A.13', '`scientific_effect.configuration`', 'R6.RECON.30; resolved by R6.RECON.33\'s search from the anchor of the admission mode'),
    ('A.14', 'record item ids', 'R6.RECON.30 item ids and what `accept` on `<path>` confirms; REVIEW-SCHEMA'),
    ('A.15', 'field malformation in general', 'R6.RECON.29: schema failure is `record-invalid` before any RC; one key table per kind, normative; RECON-SCHEMA (generic conformance)'),
    ('A.16', 'schema `oi-reconciliation/1`', 'R6.RECON.30: retired, `record-invalid` when read, still scanned; RECON-SCHEMA'),
    ('A.17', 'dispositions in the result', 'R6.RECON.36 (`failed` per record), R6.OUT.18; RECON-ENUM'),
    ('B.1', '`verdicts[]` entry keys', 'R6.RECON.31: `{item, verdict, reason}` plus the admitted keys; REVIEW-SCHEMA'),
    ('B.2', '`reviewed`', 'R6.RECON.31: path and blob both match, one rule everywhere; REVIEW-SCHEMA'),
    ('B.3', '`reviewer` / `author`', 'R6.RECON.29 identity string (trim, case-fold); FINDING-FORM independence countercase'),
    ('B.4', '`method`', 'R6.RECON.31: contains a full object id (owner choice); REVIEW-SCHEMA'),
    ('B.5', 'widening review', 'R6.RECON.31: `kind`, `replaces`, `field:<key>` and element-id items; `widening_review` is an unknown configuration field; REVIEW-SCHEMA'),
    ('B.6', 'item ids of every kind', 'R6.RECON.31 item-id table (HP by `sites[].site_id`; `id` in R6.CTX.7 and R6.HIT.4); REVIEW-SCHEMA'),
    ('C.1', '`rederivation`', 'R6.RECON.32: a non-empty string (owner choice); REASSESS-KEYS'),
    ('C.2', 'reassessment item ids', 'R6.RECON.31: `finding`, `repair`, `edit`, `rederivation`, `verdict`'),
    ('C.3', 'reassessment location', 'R6.RECON.32: the plan\'s record directory of the citing configuration (owner choice)'),
    ('D.1', '`records[].kind`', 'R6.RECON.33 enumeration and schema map; unknown or mismatched kind is ERROR `CONFIG_INVALID`; tool behaviour (skipping) contradicts R6.VALID.3; CONFIG-REFS'),
    ('D.2', '`roles.side_change_classes` and `records`', 'R6.RECON.33: also listed in `records` with the same blob; CONFIG-REFS'),
    ('D.3', '`retirement`', 'R6.RECON.33: `{name, issue}`, matched by equal name or issue; CONFIG-REFS'),
    ('D.4', 'supersedes resolution at or before `F`', 'R6.RECON.33: the anchor per admission mode, the walk to the root stated in R6.REC.17, a revised plan on a new `H` in a new record directory; SUPERSEDES-RESOLVE'),
    ('D.5', 'direction of "reachable through `supersedes`"', 'R6.RECON.33 and R6.RECON.26 (iii): the finding\'s configuration lies on the run configuration\'s chain'),
    ('D.6', '`checks[].default_for`', 'R6.RECON.33: an unknown field (R6.VALID.2), no default check; CONFIG-REFS'),
    ('E.1', 'class record keys', 'R6.RECON.34: `classes[{id, prefixes, pins[{path, git_blob, blob_sha256}]}]`, both hashes required, no `paths` form; CLASS-SCHEMA'),
    ('E.2', 'class record widening', 'R6.RECON.34: an added pin or prefix or changed blob needs a widening review (owner choice); CLASS-SCHEMA'),
    ('F.1', 'file selection', 'R6.RECON.35: no suffix filter; tool behaviour (`.json` filter) contradicts the design; SCAN-PARSE'),
    ('F.2', 'parse failure', 'R6.RECON.35: every JSON-shaped file, UTF-8 or UTF-16, escapes resolved, near-miss schemas; a malformed finding blocks at run level; SCAN-PARSE'),
    ('F.3', 'record identity across copies', 'R6.RECON.29 and R6.RECON.35: identity is the reference; SCAN-PARSE'),
    ('F.4', 'first-kind finding review location', 'R6.RECON.35: same directory for lint; anywhere for detection; SCAN-PARSE, REVIEW-SCHEMA'),
    ('G.1', '`migrations[]` and chaining', 'R6.RECON.32 and R6.RECON.28: `{old, new}` strings, transitive closure; MIGRATION-RECORD'),
    ('G.2', '`approval`', 'R6.RECON.32: `{quote, author, time}`, time as R6.RECON.29, form only; MIGRATION-RECORD'),
    ('G.3', 'migration item ids and location', 'R6.RECON.31 (`migration:<old>`, `approval`) and R6.RECON.32 (plan\'s record directory)'),
    ('G.4', 'R6.CORE.5 allowlist', 'Tool change listed below: `oi-reassessment/1` and `oi-edit-id-migration/1` join the schema list; R6.CORE.5\'s list is illustrative ("among them"), so the text is not edited'),
    ('H.1', '`inputs.classify_records`', 'R6.OUT.18 and R6.RECON.36: `review: {path, sha256}`; RECON-ENUM'),
    ('H.2', '`inputs.record_base` and `category3`', 'R6.OUT.18 and R6.RECON.36; RECON-ENUM'),
]
AUDIT_LABELS = (['A.%d' % i for i in range(1, 18)] + ['B.%d' % i for i in range(1, 7)] + ['C.1', 'C.2', 'C.3']
                + ['D.%d' % i for i in range(1, 7)] + ['E.1', 'E.2'] + ['F.%d' % i for i in range(1, 5)]
                + ['G.%d' % i for i in range(1, 5)] + ['H.1', 'H.2'])
RANKED_MAP = [
    ('1', 'D.4, D.5'), ('2', 'A.6, FINDING-KEYS retained-edit case, R6.ADAPT.2 `edits`'), ('3', 'A.5, A.9, A.15'),
    ('4', 'A.11'), ('5', 'A.14, B.5, B.6'), ('6', 'F.1 to F.3'), ('7', 'D.1, D.2'), ('8', 'A.2'), ('9', 'A.7, A.8'),
    ('10', 'A.9, A.10, A.12'), ('11', 'B.3, D.3, C.1, C.3, G.3, H.1, H.2, D.6, E.1, G.4'),
]

DELTA_MAP = [
    ('D1', 'R6.RECON.35: detection selects every JSON-shaped file (object or array), UTF-8 or UTF-16, the plan\'s record '
           'directory included; near-miss schema strings and escaped ids are malformed findings at run level when the '
           'text holds `invalidates` or `invalidated`; prose files are not records (stated, so that design documents '
           'that quote these words do not block every run). SCAN-PARSE case 2 now contains `invalidates`, with a '
           'separate case for a malformed record that is not a finding.'),
    ('D2', 'R6.RECON.26 (v) and the body sentence: the global matches are (path and `old_sha256`) or (id and path). '
           'FINDING-LINEAGE fork-after-repair case.'),
    ('D3', 'Owner choice, as proposed: `repair` null exactly for a form failure or an unaccepted first-kind finding; all '
           'other conditions stand (R6.RECON.27 Keys). REASSESS-KEYS cases in both directions. AMENDMENT-6 notes the '
           'dependence of the interim remedy on the deletion-gap Issue (review finding 9).'),
    ('D4', 'R6.RECON.24: for a deletion splice (empty new bytes), containment means the replacement bytes do not contain '
           'the splice\'s old bytes. Chosen over "wait for a revised plan": both fail closed and neither forces '
           'another amendment, but this one keeps the same protections as any resolution (the bytes the plan removes '
           'are mechanically absent, the review confirms the window, the renewed scientific review and the trial run) '
           'without a new freeze for every neighbouring change; a resolution that keeps the old bytes is refused. '
           'RESOLUTION-SCHEMA cases in both directions.'),
    ('D5', 'R6.RECON.30: the configuration\'s `executed_suffixes` (R6.CFG.4; for A1 the five suffixes) plus delegation '
           'coverage is a mechanical floor; every other executed path keeps R6.RECON.25\'s obligation, confirmed by the '
           'review. RECON-FIELDS cases.'),
    ('D6', 'One definition each: a finding (R6.RECON.26 Form (i); the body cites it), the lineage (R6.RECON.33; R6.RECON.26 '
           'cites it), the reassessment parts (R6.RECON.27 Keys; the body names the parts only).'),
    ('D7', 'R6.RECON.27 Keys: a duplicated item is lifted per finding for its `edit`; R6.RECON.24: a non-UTF-8 `m` blob has '
           'no resolution (`record-invalid`), a ledgered path being UTF-8 at `H` (R6.PROF.8).'),
]

FOLLOWUP_MAP = [
    ('1', 'R6.RECON.33: the anchor per admission mode (chain `F`; post-freeze route: the record at `REV`, its references '
          'from `F`; harness: the control-supplied configuration, otherwise `REV`). SUPERSEDES-RESOLVE harness cases.'),
    ('2', 'R6.RECON.10 rewritten (RC5): `"identity"` with prefix agreement, or an integer equal to `start_M - start_H`, 0 '
          'allowed; a wrong type is a schema failure, a wrong value fails RC5. RECON-SCHEMA positive case (translation 0) '
          'and countercase.'),
    ('3', 'R6.RECON.31: HP items are `sites[].site_id`; R6.CTX.7 and R6.HIT.4 now give each element an `id`.'),
    ('4', 'R6.REC.17 states the walk to the root; the finding and `repair.entry` are read from the scans at `M` '
          '(R6.RECON.27 Keys, R6.RECON.33).'),
    ('5', 'R6.RECON.33: a revised plan on a new `H` uses a new record directory admitted by a tool revision (R6.A1CFG.1); '
          'Dir2 is unchanged (fail-closed; owner choice).'),
    ('6', 'R6.RECON.30: the splice list equals the ledger\'s splices of the path, in order; RECON-SCHEMA countercases for '
          'an extra element and a reordered list.'),
    ('7', 'R6.RECON.26 body cites R6.RECON.33 for the lineage and Form (i) for a finding; R6.RECON.27 body names the parts '
          'and cites Keys.'),
    ('8', 'R6.RECON.26 Form (ii): a retained edit\'s old bytes are its `text` in every match.'),
    ('9', 'R6.RECON.35: every JSON-shaped file is selected, decoded as UTF-8 or UTF-16, escapes resolved (merged with '
          'D1); a non-JSON file is not a record (stated boundary).'),
    ('10', 'R6.ADAPT.2: the ledger and edit list parsed strictly, a non-integer number in a hashed value '
           '`LEDGER_INTEGRITY`; CANON-JSON names one class.'),
    ('11', 'CONFIG-REFS: `notes` and `sites` unknown fields; op B or D without `--check` is USAGE (R6.RECON.33); '
           'SUPERSEDES-RESOLVE names `CONFIG_INVALID` and adds the record case (`record-invalid`). Tool change: the EI4 '
           'fixture drops `notes`.'),
    ('12', 'R6.RECON.31: `reason` is a required key; the fixture rewrite is listed among the tool changes. Disagreement '
           'recorded (sec. 5).'),
    ('13', 'R6.RECON.29: every encoding is a full match of the whole string (no trailing newline).'),
    ('S1.1', 'One key table per kind, rendered from one definition in the generator; the hand-written JSON Schema is '
             'removed, and any machine schema is derived from the tables (R6.RECON.29).'),
    ('S1.2', 'RECON-SCHEMA: one generic conformance case; named cases kept only for the known tool divergences.'),
    ('S1.3', 'RESULT-FIELDS merged into RECON-ENUM.'),
    ('S1.4', 'REVIEW-SCHEMA and WIDENING-ITEMS merged.'),
    ('S1.5', 'Kept (the delta reviewer lists `git_blob` as necessary); disagreement recorded (sec. 5).'),
    ('S1.6', 'Kept (`method` floor and `reason`); disagreement recorded (sec. 5).'),
    ('S1.7', 'The time grammar is kept; its check is form only (R6.REC.3) and costs nothing; the migration approval case '
             'is covered by the generic conformance case.'),
    ('S2', 'Every listed safeguard is kept.'),
    ('S3.1', 'Finding 2.'), ('S3.2', 'Finding 1.'), ('S3.3', 'Finding 3.'), ('S3.4', 'Finding 5.'),
    ('S3.5', 'D5: `executed_suffixes` carried by the configuration, the meaning-based obligation kept.'),
    ('S3.6', 'R6.RECON.31: the closed verdict key set is accepted knowingly, with the reason; detection of '
             '`oi-review-record/` prefixes keeps a future schema from hiding a finding.'),
    ('S3.7', 'R6.RECON.36: `failed` is per record.'),
    ('S3.8', 'Each expectation names one stop class.'),
]

OWNER_CHOICES = [
    'Points 1 to 4 as proposed, with the D1 and D2 fixes.',
    'No narrowing superseding finding; the remedy for an id collision is a rename.',
    'Only referenced migration records apply.',
    'Item B1: reading (b), with `text` in the ledger interface\'s `retained` entry.',
    'Item B2: 0-based, end-exclusive byte offsets at UTF-8 character boundaries; base64; `confirms`; a resolution of a '
    'splice without a conflict is `record-invalid`; `resolutions` optional; the deletion-splice rule (D4).',
    '`record_id` required on reconciliation, reassessment, migration and class records.',
    'Canonical JSON as Python\'s `json.dumps(..., sort_keys=True, separators=(\',\', \':\'), ensure_ascii=False)`.',
    'Identity strings compared after trimming and Unicode case folding.',
    'A review\'s `method` names a full object id, and `reason` is required in every verdict entry (the reviewers '
    'disagree: the auditor would drop both, returning `method` to non-empty and `reason` to optional on `accept`; the '
    'delta reviewer recommends the `method` floor; implemented as required).',
    'The executed-path floor carried by the configuration (`executed_suffixes`, which must contain the design floor '
    '`.py`, `.lean`, `.yml`, `.yaml`, `.sh` and may only add to it), with the meaning-based obligation for other '
    'executed paths.',
    '`x` read at `X`; R6.RECON.21 reads `X`, which is `C` in RT-L2.',
    '"Changes the path" by tree entry; a mode-only change drifts; a deletion stays `base-drift`.',
    '`oi-reconciliation/1` retired: `record-invalid` when read, still read by detection.',
    'Review-record `kind` optional; widening items `field:<key>` and element ids.',
    '`rederivation` a non-empty string.',
    'Reassessment and migration records in the citing configuration\'s record directory.',
    'The names of the `records` kinds.',
    'Supersedes resolution along the anchor\'s whole first-parent chain, and the anchors per admission mode.',
    '`retirement` as `{name, issue}` with an integer issue.',
    '`default_for`, `widening_review`, `notes` and `sites` treated as unknown fields; no default check (USAGE without '
    '`--check`).',
    'Widening review for a class record that adds a pin or prefix or changes a blob; and `git_blob` dropped from class '
    'pins, the pin being its `blob_sha256` (both reviewers now agree that `git_blob` adds no protection; the alternative '
    'is both keys required and cross-checked; an optional `git_blob` is the form both reject).',
    'Detection selection: every JSON-shaped file (object or array), the plan\'s record directory included; prose files '
    'are not records.',
    'The `dispositions` (per-record `failed`) and `category3` keys; `category` null where R6.RECON.22 assigns none.',
    'D3 as narrowed by the final review (F1): `repair` null only where no independent reviewer asserts the '
    'invalidation: a first-kind finding whose entry\'s non-author review rejects or dissents; a review whose `reviewed` '
    'names no record the scan finds; a malformed file of class (b) or (c); with `finding.item` null for the last (F2).',
    'A revised plan on a new `H` uses a new record directory admitted by a tool revision; Dir2 unchanged (the '
    'alternative, Dir2 relative to the superseded plan\'s files, is not taken because it would weaken Dir2).',
    'The verdict key set closed, accepted knowingly.',
]

NITS_MAP = [
    ('1', 'S11-2a (reading A adopted): the `$new_line` site item gains `added_relative_to_unmutated` '
          '(`items[class=unclassified,subject=$new_line]`: 1), so the control states its dependence on the mutation.'),
    ('2', 'RTL2-BIND countercase: the planting is stated (a hit on a line unchanged across `H`, `M` and `X`, surfaced by '
          'a review profile present only in the countercase configuration; no path changes, no side change).'),
    ('3', 'RT-D: a flag states that the 10 and the SM:1394 site hold only with the superseding rule file that drops '
          'W1-a, citing the owner\'s W1-a row (amaybaum, 2026-11-26T07:55:49Z, #1169 comment 7185991140); '
          '`direction.why` and the sec. 31 figure say 10; the SM:1394 site gains `classes_exact: [unclassified]`.'),
    ('4', 'The declared-change guard of this generator: every difference from a row amendment 5 left must be a declared '
          'change in its declared form; a `classes_exact` may only narrow unless declared; amendment 5 r2\'s '
          'strengthenings are pinned; requirement control and pending additions must equal the declared ones.'),
    ('5', 'RT-DR countercase: the matched text is replaced by neutral text on the same line, so no later line is '
          'renumbered.'),
]

R4_MAP = [
    ('F1', 'R6.RECON.27 Keys: `repair` null only for (a) a first-kind finding whose entry has a non-author review that '
           'rejects or dissents on `scientific_effect` (the review must exist), (b) a review whose `reviewed` names no '
           'record the scan finds, (c) a malformed file of class (b) or (c); an independent second-kind finding needs a '
           'repair however malformed. REASSESS-KEYS: positive countercase now (a); blocked cases for the reviewer\'s '
           'sequence and for an entry with no review.'),
    ('F2', 'R6.RECON.27 Keys and the `reassess.finding` table: `item` null exactly for a finding read from a class (b) or '
           '(c) file, the finding being the whole file. REASSESS-KEYS positive and blocked cases.'),
    ('F3 / A1', 'R6.RECON.29 conformance mutants: generated by a fixed rule from the single table definition into '
                'CONFORMANCE-MUTANTS.json (a generated output); ids `(table, key path, violation)`; per mutant a '
                '`record-invalid` item naming the key path and no RC condition; the gate compares the recorded ids with '
                'the list. RECON-SCHEMA: one positive record per kind, R6.RECON.31, R6.RECON.32 and R6.RECON.34 added to '
                'its requirements. The removed approval case is now covered by the migration tables\' mutants.'),
    ('F4', 'R6.CFG.4 and R6.RECON.30: `executed_suffixes` contains the design floor and may only add; CONFIG-REFS '
           'countercase.'),
    ('A2', 'R6.RECON.29: the sec. 16 claim is dropped; the mutant list is the check of any machine schema.'),
    ('A3', 'Key tables for the `invalidated` element and `target`, `confirms`, `finding`, `repair`, `repair.entry`, '
           '`edit`, `approval`, a migration, a pin, `ledger_binding` and the reference; all closed key sets.'),
    ('A4', 'Every ERROR case names its class in `stop_class`: `CONFIG_INVALID` (CONFIG-REFS, REVIEW-SCHEMA, '
           'SUPERSEDES-RESOLVE), `LEDGER_INTEGRITY` (CANON-JSON, missing raw edit-list entries included).'),
    ('A5', 'R6.RECON.33: a harness run that names no `REV` resolves from the commit the record is read from '
           '(R6.RECON.21).'),
    ('B1', 'R6.RECON.35: selection on raw leading bytes; test (c) on a lossy decode. SCAN-PARSE invalid-byte case.'),
    ('B2 / B3', 'R6.RECON.35 Residuals: leading non-JSON bytes on a corrupted record, and storage under a tool-landing '
                'prefix (REVIEW_REQUIRED, not blocking), joined to the deletion residual and Issue #1598.'),
    ('22', 'R6.RECON.35 class (b): a parsed object with no `schema` key but a review\'s shape. SCAN-PARSE case.'),
    ('21', 'Owner choice: `git_blob` dropped from class pins (R6.TREE.5, R6.RECON.34); CLASS-SCHEMA countercase is a pin '
           'carrying `git_blob`; the alternative (both required and cross-checked) recorded in sec. 5.'),
    ('T1', 'Tool writer: R6.RECON.23 matches findings by an explicit key (class, file, `rule_id` or profiles, the sha256 '
           'of the matched line or sentence; the line number, segment and tree excluded; for an item without a line, '
           'class, subject and fingerprint), counted with multiplicity. RECON-TRIAL moved-line case (declared).'),
    ('O', 'Owner (#1169 comment 7190776267, item 3): R6.GATE.17 (new) classifies a failing row\'s cause as '
          '`expectation-defect`, `implementation-defect`, `verification-failure` or `unresolved`, with the evidence that '
          'would settle an unresolved row; no classification changes an expected value or weakens a check.'),
    ('T2', 'Tool writer: R6.GATE.3\'s count grammar is stated for the keys the adopted rows use (units `sites` and '
           '`fail_lines`; any field of the counted object; list membership; `_nonempty`; the `count_sentence_lines` '
           'modifier; how sentence-level items count), and the misnamed keys `rule` and `alternative` in L2, RT-D, RT-DR '
           'and RT-DR3W are corrected to `rule_id` and `alternatives` (declared, values unchanged).'),
]


def note(owner):
    out = ['', '### 0.7 Amendment 6 of 2026-11-26', '']
    for d in owner['decisions']:
        out += ['Owner direction at %s (%s, %s, relayed by the %s); excerpt of %s (each line prefixed by "> "; "[...]" '
                'marks text left out):' % (d['record'], d['author'], d['time'], d['relayed_by'], d['item']), '']
        blocks = []
        for x in d['quotes']:
            blocks.append('> [...]' if x is None else '\n'.join('> ' + y for y in x.split('\n')))
        out += ['\n>\n'.join(blocks), '']
    out += ['Amendment 6 resolves the schema ambiguities of category 3 that the tool writer raised while implementing '
            'amendment 4 and one expectation conflict; answers the independent review of its first draft (PR #1593 '
            'comment 7189446310); resolves two further ambiguities, the retained-site line of RC14 (b) and the '
            'resolution schema of R6.RECON.24; and states the schema contract of the reconciliation record kinds that '
            'the owner\'s completeness audit (PR #1593 comment 7189621405) found stated by meaning only (sec. 23.1, '
            'R6.RECON.29 to R6.RECON.36, one key table per kind); it then answers the reviews of its second draft (PR '
            '#1593 comments 7190255132 and 7190234470), states each definition once, and removes cases and text that '
            'both reviewers found to add no protection; and it makes the corrections of the two final checks (PR #1593 '
            'comments 7190624085 and 7190609504), states the matching key of R6.RECON.23 and the count grammar of '
            'R6.GATE.3, and adds R6.GATE.17, under which a failing row may stay unresolved. Each resolution is a proposal for the owner\'s decision at adoption '
            '(AMENDMENT-6.md gives the options and lists the owner choices). None lets a finding be lost or lifted by '
            'rewording: a finding is detected before lint, every form failure blocks rather than lapses, the '
            'path-and-old-bytes match binds every configuration, and a migration only adds edits. Where the tool '
            'accepts input the design refuses (a missing `changes_decisions_on_X`, non-integer offsets, a suffix filter '
            'on the scanned set, skipped parse failures, ignored record kinds), the design rule is stated and a '
            'countercontrol row is added; no requirement is weakened to match the tool.', '']
    return '\n'.join(out)


def add_controls(t, req, ids):
    anchor = CONTROLS_ANCHOR[req]
    if not anchor.endswith('.'):
        raise SystemExit('controls anchor %s' % req)
    a = t.index('**%s**' % req)
    nxt = re.compile(r'\n(?:\*\*R6\.|\*\*\*|#)').search(t, a + 1)
    b = nxt.start() if nxt else len(t)
    block = t[a:b]
    if block.count(anchor) != 1:
        raise SystemExit('controls anchor for %s occurs %d times in its block' % (req, block.count(anchor)))
    block = block.replace(anchor, anchor[:-1] + ', ' + ', '.join(ids) + '.')
    return t[:a] + block + t[b:]


def amend_design(t, owner):
    # R6.REC.2: the verdict values and keys
    t = once(t, "of the reviewed record (`accept`, `reject` or `dissent`, with the reason); and `dissent`, if any. A",
             "of the reviewed record (`accept`, `reject` or `dissent`, with the reason, and, on the item\n"
             "`<path>:scientific_effect` of a reconciliation record entry only, `invalidates` with `invalidated`,\n"
             "R6.RECON.26; on a resolution item, `confirms`, R6.RECON.24; the keys are those of R6.RECON.31 %s);\n"
             "and `dissent`, if any. A" % MARK, 'R6.REC.2')
    # R6.REC.6: every review naming the blob counts
    t = once(t, "path that is not a regular file (R6.REC.17); a record not read from the git object store.\n",
             "path that is not a regular file (R6.REC.17); a record not read from the git object store. Every review\n"
             "record that names the record's reference, among the records the run reads and the scanned sets of\n"
             "R6.RECON.35, is a review of it and is checked here: a second review whose verdict on any item is not\n"
             "`accept`, `invalidates` included, fails the record %s.\n" % MARK, 'R6.REC.6')
    # R6.REC.7: the resolution of a reference
    t = once(t, "a first record has `supersedes: null`.",
             "a first record has `supersedes: null`. A reference \"at or before `F`\" is resolved by the search of\n"
             "R6.RECON.33 %s." % MARK, 'R6.REC.7')
    # R6.REC.17: the one unbounded walk
    t = once(t, "- **Bounded walks, no fetch.** Every walk runs between explicit commits.",
             "- **Bounded walks, no fetch.** Every walk runs between explicit commits, except the resolution of a\n"
             "  reference by R6.RECON.33, which walks from its anchor towards the root and stops at the first commit\n"
             "  that resolves it %s." % MARK, 'R6.REC.17')
    # R6.RECON.26: one definition of a finding (Form (i)) and of the lineage (R6.RECON.33); the global matches
    t = once(t, "retirement. A finding is either a reconciliation record entry whose review accepts a `scientific_effect` "
                "with verdict\n`invalidates`, or a non-author review record (passing record lint) whose verdict on an "
                "entry's `scientific_effect` finds\nthat the change invalidates the basis of a planned edit, whatever the "
                "writer's verdict; such a review verdict names\n`invalidated`, each an edit id with the canonical sha256 "
                "of its edit-list entry and its target (the path, `start_H` and `old_sha256` of the edit at `H`).",
             "retirement. A finding is of one of the two kinds that Form of a finding (i) below defines: a reconciliation\n"
             "record entry whose `scientific_effect` has the verdict `invalidates` (the first kind), or a non-author review\n"
             "record whose verdict finds that the change invalidates the basis of a planned edit, whatever the writer's\n"
             "verdict (the second kind); its `invalidated` elements have the form of (ii).", 'R6.RECON.26 definition')
    t = once(t, "one in the plan lineage of\nthe configuration the finding was made under (every configuration reachable "
                "from it through `supersedes`,\nand every configuration whose `retirement` names the same retirement, by "
                "name or by accountable Issue),\nwhose ledger holds",
             "one in the plan lineage of\nthe finding (R6.RECON.33), whose ledger holds", 'R6.RECON.26 lineage')
    t = once(t, "for findings, by the scan of R6.RECON.2 (d), whether or",
             "for findings, by the detection of R6.RECON.35, whether or", 'R6.RECON.26 detection')
    t = once(t, "whose ledger holds the edit's id, an id the edit was renamed to under a migration recorded under AGENTS.md\n"
                "sec. A.48 item 3, or an edit of the same path whose old bytes hash to the recorded `old_sha256`, "
                "whatever its\noffset (so a renumbering on a new `H` is still matched).",
             "whose ledger holds the edit's id or an id the edit was renamed to under a migration recorded under AGENTS.md\n"
             "sec. A.48 item 3; and any configuration, whatever its lineage or retirement (Form of a finding (v) "
             "below), whose ledger holds an edit of the same path whose old bytes hash to the recorded `old_sha256`, "
             "whatever its\noffset (so a renumbering on a new `H` is still matched), or an edit with the same id on the "
             "same path, whatever its old bytes.", 'R6.RECON.26 match scope')
    t = once(t, "The block is scoped to the plan lineage: it binds every\nconfiguration that carries an invalidated edit",
             "The block, with the scope just stated, binds every\nconfiguration that carries an invalidated edit",
             'R6.RECON.26 scope sentence')
    a = t.index('**R6.RECON.26** **Category 3: the blocking state**')
    b = t.index('\nSources: amendment 3 (#1169 comments 7184569981, 7184626125, 7184808247 and 7185092393); amendment 4',
                a)
    t = t[:b] + FORM % {'mark': MARK} + t[b:]
    t = once(t, "Sources: amendment 3 (#1169 comments 7184569981, 7184626125, 7184808247 and 7185092393); amendment 4 "
                "(#1169 comment 7185562871). Controls: RECON-BLOCK, BLOCK-KEY.",
             "Sources: amendment 3 (#1169 comments 7184569981, 7184626125, 7184808247 and 7185092393); amendment 4 "
             "(#1169 comment 7185562871); amendment 6 (#1169 comment 7187418279; PR #1593 comment 7189446310). "
             "Controls: RECON-BLOCK, BLOCK-KEY.", 'R6.RECON.26 sources')
    # R6.RECON.25: the form of invalidated (amendment-6 parenthetical after the amendment-4 one)
    t = once(t, "`old_sha256` of the edit at `H`) (amendment 4, sec. 0.5: pending independent review and the owner's "
                "acceptance). For an entry",
             "`old_sha256` of the edit at `H`) (amendment 4, sec. 0.5: pending independent review and the owner's "
             "acceptance), in the form and with the `configuration` of R6.RECON.26, Form of a finding (ii) and (iii) %s. "
             "For an entry" % MARK, 'R6.RECON.25 invalidated')
    # R6.RECON.24: RC14 (b) and the resolution schema
    t = once(t, RC14B_OLD, RC14B_NEW, 'RC14 (b)')
    t = once(t, "A conflict is resolved only by an entry's `resolutions`, one for each\nconflicting splice: the window at "
                "`M` (`start_M`, `end_M`, `sha256`) and the resolved bytes' sha256.",
             "A conflict is resolved only by an entry's `resolutions`, one for each\nconflicting splice: the window at "
             "`M` (`start_M`, `end_M`, `sha256`) and the resolved bytes and their sha256 (`resolved`,\n"
             "`resolved_sha256`), in the resolution schema below.", 'R6.RECON.24 resolutions')
    t = once(t, "the tool checks only that the window\noccurs once at `M` and that the review covers and accepts that item.",
             "the tool checks that the window\noccurs once at `M` and that the review covers and accepts that item with "
             "the confirmation of the resolution schema below.", 'R6.RECON.24 review item')
    a = t.index('**R6.RECON.24** **Conflict detection: RC14**')
    b = t.index('\nSources: amendment 3 (#1169 comments 7184569981, 7184626125 and 7184808247). Controls: RECON-CONFLICT',
                a)
    t = t[:b] + '\n' + RESOLUTION % {'mark': MARK} + t[b:]
    # R6.RECON.27: the keys; edit null for a run-level binding
    t = once(t, "`no-effect`; and `edit` names", "`no-effect`; and, unless it is null for a finding bound at run level "
                                                 "(Keys, below), `edit` names", 'R6.RECON.27 edit')
    t = once(t, "and names: `finding`, the\n`{path, blob_sha256}` of the record or review record carrying the category-3 "
                "finding (R6.RECON.26); `repair`, the\ncommits of the repairing change on `main` and the `{path, "
                "blob_sha256}` of the reconciliation record entry that records\nit; `edit`, the edit id and the canonical "
                "sha256 of its edit-list entry as worded in the configuration that cites the\nreassessment;",
             "and names, each as Keys below defines: `finding`, the\ncategory-3 finding it reassesses (R6.RECON.26); "
             "`repair`, the repairing change on `main` and the reconciliation record entry that records\nit; `edit`, "
             "the reassessed edit as worded in the configuration that cites the\nreassessment;", 'R6.RECON.27 body')
    t = once(t, "finds at the run's `M`; the\nrepair's commits lie on",
             "finds at the run's `M`; unless `repair` is null (Keys, below), the\nrepair's commits lie on",
             'R6.RECON.27 repair null')
    a = t.index('**R6.RECON.27** **Reassessment of an invalidated edit**')
    b = t.index('\nSources: amendment 4 (#1169 comment 7185562871). Controls: BLOCK-KEY, REASSESS-FORM.', a)
    t = t[:b] + KEYS27 % {'mark': MARK} + t[b:]
    # R6.RECON.10: RC5
    t = once(t, RC5_OLD, RC5_NEW, 'R6.RECON.10')
    # R6.CTX.7, R6.HIT.4: the id of each element
    t = once(t, "resolves a context FAIL;",
             "resolves a context FAIL (each adjudication an element of the record's `entries`, carrying `id`, a\n"
             "non-empty string unique in the record, from which its review item is taken, R6.RECON.31 %s);" % MARK,
             'R6.CTX.7')
    t = once(t, "It reaches the run through the `--classify` route of sec. 22.",
             "Each classification carries `id`, a non-empty string unique in the record, from which its review\n"
             "item is taken (R6.RECON.31) %s. It reaches the run through the `--classify` route of sec. 22." % MARK,
             'R6.HIT.4')
    # R6.CFG.4: the executed-path floor
    t = once(t, "- `rules`: `[{path, blob_sha256}]`, rule files of schema `oi-term-rules/2`;",
             "- `executed_suffixes`: a non-empty array of file-name suffixes, the mechanical floor of the executed-path\n"
             "  rule of R6.RECON.30; it contains `.py`, `.lean`, `.yml`, `.yaml` and `.sh`, the floor this design fixes,\n"
             "  and may add suffixes, and a list lacking one of them is ERROR `CONFIG_INVALID` %s;\n"
             "- `rules`: `[{path, blob_sha256}]`, rule files of schema `oi-term-rules/2`;" % MARK, 'R6.CFG.4 suffixes')
    # R6.RECON.21: x read at X
    t = once(t, "blob ids for each path equal the path's blobs at the run's `M` and\n  `C`;",
             "blob ids for each path equal the path's blobs at the run's `M` and\n  `X`, which is `C` here (R6.RECON.30 "
             "%s);" % MARK, 'R6.RECON.21 x')
    # R6.RECON.2 (d): the scanned set
    t = once(t, "(the scanned set; review records are found the same way, with schema",
             "(the scanned set, selected and parsed as R6.RECON.35 states %s; review records are found the same way, "
             "with schema" % MARK, 'R6.RECON.2 (d)')
    # R6.CFG.4: kinds (amendment-6 parenthetical after the amendment-4 one)
    t = once(t, "  record that the freeze cites (R6.RECON.27) is listed with kind `reassessment` (amendment 4, sec. 0.5: "
                "pending independent review and the owner's acceptance);",
             "  record that the freeze cites (R6.RECON.27) is listed with kind `reassessment` (amendment 4, sec. 0.5: "
             "pending independent review and the owner's acceptance), and an edit-id migration\n  record (R6.RECON.28) "
             "with kind `edit-id-migration`; the kinds and the schema each requires are those of R6.RECON.33 %s;"
             % MARK, 'R6.CFG.4 kind')
    t = once(t, "- `retirement`: name and accountable Issue;",
             "- `retirement`: name and accountable Issue, `{name, issue}` (R6.RECON.33);", 'R6.CFG.4 retirement')
    # R6.ADAPT.2: raw entries, edits and the retained text
    t = once(t, ADAPT2_OLD, ADAPT2_NEW, 'R6.ADAPT.2')
    # R6.TREE.5: the pin is the blob's sha256 (owner choice: git_blob dropped)
    t = once(t, "pinned blob (`git_blob` and\n`blob_sha256`).", "pinned blob (its `blob_sha256`; R6.RECON.34).",
             'R6.TREE.5 pin')
    # R6.RECON.23: the matching key; R6.GATE.3: the count grammar
    t = once(t, RECON23_OLD, RECON23_NEW, 'R6.RECON.23')
    t = once(t, GATE3_OLD, GATE3_NEW, 'R6.GATE.3')
    # R6.TREE.5: class record keys
    t = once(t, "directory the rule of sec. 21 also applies.",
             "directory the rule of sec. 21 also applies. The keys of a class record are those of R6.RECON.34 %s."
             % MARK, 'R6.TREE.5')
    # R6.OUT.18: result fields
    t = once(t, "`hp_records` and `classify_records` `[{rev, path, sha256}]`;",
             "`hp_records` `[{rev, path, sha256}]`; `classify_records` `[{rev, path, sha256, review: {path, sha256}}]`; "
             "`record_base`, a commit id or null (R6.RECON.36 %s);" % MARK, 'R6.OUT.18 inputs')
    m = [x for x in re.finditer(r'^\| `pins` \| N \| [^\n]*$', t, re.M)]
    if len(m) != 1:
        raise SystemExit('R6.OUT.18 pins row')
    t = (t[:m[0].end()] + '\n| `dispositions` | N | op C with `M`: one entry per drifted ledgered or corpus path, '
         '`[{path, disposition, category, record, failed, conflicts, why}]` (R6.RECON.22, R6.RECON.36) |'
         '\n| `category3` | N | op C with `M`: `{findings, blocked, reassessments}` (R6.RECON.26, R6.RECON.36) |'
         + t[m[0].end():])
    # sec. 31 evidence figure for RT-D (amendment 5 r2 set the count to 10)
    t = once(t, "| `resid`: 45 REVIEW lines, 17 hit by no other profile; 11 W1/W2 lines PASS | RT-D |",
             "| `resid`: 45 REVIEW lines, 17 hit by no other profile; 10 W1/W2 lines PASS, with the superseding rule file "
             "that drops W1-a (amendment 6) | RT-D |", 'sec. 31 RT-D figure')
    # Controls lines of the touched requirements
    for req in TOUCHED:
        ids = [r for r in REQ_CONTROLS.get(req, [])]
        if ids:
            t = add_controls(t, req, ids)
    # R6.GATE.17: four statuses for a failing row's cause, unresolved among them
    t = once(t, "Sources: OD-18, Q2. Controls: RT-L2, GATE-13, GATE-14, GATE-15, GATE-19, RTL2-BIND, RECORD-BASE.\n",
             "Sources: OD-18, Q2. Controls: RT-L2, GATE-13, GATE-14, GATE-15, GATE-19, RTL2-BIND, RECORD-BASE.\n"
             + GATE17, 'R6.GATE.17')
    # the new requirements
    t = once(t, "\n***\n\n## 24. Engine, purity scope (Z9), generality",
             NEW_REQ28 % {'mark': MARK}
             + R29 % {'mark': MARK, 't_recon': spec_tables('recon'), 't_review': spec_tables('review'),
                      't_reassess': spec_tables('reassess'), 't_class': spec_tables('class')}
             + "\n***\n\n## 24. Engine, purity scope (Z9), generality", 'R6.RECON.28 to R6.RECON.36')
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


def get_path(x, path):
    for k in path:
        if isinstance(x, dict):
            if k not in x:
                return MISSING
            x = x[k]
        elif isinstance(x, list):
            if not isinstance(k, int) or k >= len(x):
                return MISSING
            x = x[k]
        else:
            return MISSING
    return x


def set_path(x, path, value):
    for k in path[:-1]:
        x = x[k]
    k = path[-1]
    if isinstance(x, list) and k == len(x):
        x.append(copy.deepcopy(value))
    else:
        x[k] = copy.deepcopy(value)


def amend_expectations(E):
    E = copy.deepcopy(E)
    by = {r['id']: r for r in E['rows']}
    for rid, path, old, new in DECLARED_KEY_RENAMES:
        d = get_path(by[rid], path)
        if old not in d or new in d:
            raise SystemExit('declared rename %s %s' % (rid, old))
        items = [(new if k == old else k, v) for k, v in d.items()]
        d.clear()
        d.update(items)
    for rid, path, old, new in DECLARED_DIFFS:
        if get_path(by[rid], path) != old:
            raise SystemExit('declared change %s %s: the base value differs' % (rid, path))
        set_path(by[rid], path, new)
    for r, _ in ROWS:
        if r['id'] in by:
            raise SystemExit('id %s already a row' % r['id'])
        E['rows'].append(r)
    return E


def leaves(x, p=()):
    if isinstance(x, dict):
        for k, v in x.items():
            yield from leaves(v, p + (k,))
    elif isinstance(x, list):
        for i, v in enumerate(x):
            yield from leaves(v, p + (i,))
    else:
        yield p, x


def row_diffs(a, b):
    """The leaf paths at which two rows differ."""
    la, lb = dict(leaves(a)), dict(leaves(b))
    return sorted({p for p in set(la) | set(lb) if la.get(p, MISSING) != lb.get(p, MISSING)}, key=repr)


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
    sources = {'R6.RECON.28': ['#1169 comment 7187418279', 'PR #1593 comment 7189446310']}
    new = []
    for rid in NEW_REQS:
        if rid == 'R6.GATE.17':
            continue
        new.append({'id': rid, 'section': 'RECON', 'section_number': 23, 'kind': 'testable',
                    'sources': sources.get(rid, ['#1169 comment 7189470338', 'PR #1593 comment 7189621405']),
                    'controls': list(REQ_CONTROLS[rid]), 'verification': ['controls', 'review'], 'open': [],
                    'pending_owner_confirmation': [PENDING], 'owner_decision': []})
    R = R[:i + 1] + new + R[i + 1:]
    j = [k for k, q in enumerate(R) if q['id'] == 'R6.GATE.16'][0]
    g17 = {'id': 'R6.GATE.17', 'section': 'GATE', 'section_number': 16, 'kind': 'governance',
           'sources': ['#1169 comment 7190776267'], 'controls': [], 'verification': ['review'], 'open': [],
           'pending_owner_confirmation': [PENDING], 'owner_decision': []}
    return R[:j + 1] + [g17] + R[j + 1:]


def vocabulary(t):
    a = t.index('### 16.10 Annex: invariant vocabulary')
    b = t.index('***', a)
    return set(re.findall(r'`([A-Za-z_0-9]+)`', t[t.index('\n\n', t.index('A key outside it', a)):b]))


def block_of(t, rid):
    start = t.index('**%s**' % rid)
    nxt = re.compile(r'\n(?:\*\*R6\.|\*\*\*|#)').search(t, start + 1)
    return t[start:nxt.start() if nxt else len(t)]


def self_checks(E0, E, R0, R, t, base_texts):
    problems = []
    r0 = {r['id']: r for r in E0['rows']}
    r1 = {r['id']: r for r in E['rows']}
    reqs = {q['id']: q for q in R}
    declared = {}
    for rid, path, old, new in DECLARED_DIFFS:
        declared.setdefault(rid, []).append((path, old, new))
    for rid, path, old, new in DECLARED_KEY_RENAMES:
        v = get_path(r0[rid], path + (old,))
        declared.setdefault(rid, []).append((path + (old,), v, MISSING))
        declared.setdefault(rid, []).append((path + (new,), MISSING, v))
    for rid, r in r0.items():
        out = r1.get(rid)
        if out is None:
            problems.append('existing row %s removed' % rid)
            continue
        for p in row_diffs(r, out):
            cover = [d for d in declared.get(rid, []) if p[:len(d[0])] == d[0]]
            if not cover:
                problems.append('existing row %s: undeclared change at %s' % (rid, '/'.join(map(str, p))))
        for path, old, new in declared.get(rid, []):
            if get_path(r, path) != old or get_path(out, path) != new:
                problems.append('existing row %s: declared change at %s not in its declared form' % (rid, path))
        # a classes_exact may only narrow unless the change declares it (delta review nit 4)
        def exacts(x, p=()):
            if isinstance(x, dict):
                for k, v in x.items():
                    if k == 'classes_exact':
                        yield p + (k,), v
                    else:
                        yield from exacts(v, p + (k,))
            elif isinstance(x, list):
                for i, v in enumerate(x):
                    yield from exacts(v, p + (i,))
        old_ex = dict(exacts(r))
        for p, v in exacts(out):
            o = old_ex.get(p, MISSING)
            if o is not MISSING and not set(v) <= set(o) and not any(d[0] == p for d in declared.get(rid, [])):
                problems.append('existing row %s: classes_exact widened at %s' % (rid, p))
    for rid, path, value in PINS:
        if get_path(r1[rid], path) != value:
            problems.append('pinned amendment-5 strengthening %s %s changed' % (rid, path))
    for rid in NEW_IDS + NEW_REQS + ['oi-edit-id-migration/1', 'edit-id-migration', 'resolved_sha256']:
        for name, b in base_texts.items():
            if re.search(r'(?<![A-Za-z0-9.-])%s(?![A-Za-z0-9-])' % re.escape(rid), b):
                problems.append('%s already occurs in base %s' % (rid, name))
    if len(set(NEW_IDS)) != len(NEW_IDS):
        problems.append('duplicate new row id')
    for r, _ in ROWS:
        cases = r['expect']['cases']
        if not any('countercase' in x['case'] for x in cases):
            problems.append('%s: no countercase' % r['id'])
        if not any(x['outcome'] in ('ANY', 'PASS') for x in cases) and not any(
                'positive' in x['case'] for x in cases):
            problems.append('%s: no positive case' % r['id'])
        if len({x['case'] for x in cases}) != len(cases):
            problems.append('%s: repeated case text' % r['id'])
        for q in r['requirements']:
            if q not in reqs:
                problems.append('%s lists unknown requirement %s' % (r['id'], q))
            elif r['id'] not in reqs[q]['controls']:
                problems.append('%s lists %s, which does not name it' % (r['id'], q))
    for q, ctl in REQ_CONTROLS.items():
        cl = block_of(t, q).split('Controls:')[-1]
        for cc in ctl:
            if not re.search(r'(?<![A-Za-z0-9-])%s(?![A-Za-z0-9-])' % re.escape(cc), cl):
                problems.append('%s: DESIGN Controls line does not name %s' % (q, cc))
    for rid in TOUCHED + NEW_REQS:
        if MARK not in block_of(t, rid):
            problems.append('%s does not carry the amendment-6 mark' % rid)
    for rid in TOUCHED:
        if rid not in REQ_CONTROLS and rid not in EXISTING_CONTROLLED:
            problems.append('%s touched but no row controls it' % rid)
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
        if q1['controls'][len(q['controls']):] != REQ_CONTROLS.get(rid, []):
            problems.append('requirement %s: undeclared control additions' % rid)
        added = q1['pending_owner_confirmation'][len(q['pending_owner_confirmation']):]
        if q1['pending_owner_confirmation'][:len(q['pending_owner_confirmation'])] != q['pending_owner_confirmation'] \
                or added != ([PENDING] if rid in TOUCHED else []):
            problems.append('requirement %s: undeclared pending change' % rid)
    if sorted(q['id'] for q in R if q['id'] not in {x['id'] for x in R0}) != sorted(NEW_REQS):
        problems.append('new requirements differ from NEW_REQS')
    # one definition per kind: unique keys per part, every table rendered in its requirement
    for kind, parts in SPEC.items():
        for pid, title, rows in parts:
            keys = [x[0] for x in rows]
            if len(set(keys)) != len(keys):
                problems.append('SPEC %s %s: repeated key' % (kind, title))
    for rid, kind in (('R6.RECON.30', 'recon'), ('R6.RECON.31', 'review'), ('R6.RECON.32', 'reassess'),
                      ('R6.RECON.34', 'class')):
        if spec_tables(kind) not in block_of(t, rid):
            problems.append('%s does not carry the key tables of %s' % (rid, kind))
    res = [x[0] for x in PARTS['recon.resolution'][2]]
    if res != ['splice', 'start_M', 'end_M', 'sha256', 'resolved', 'resolved_sha256']:
        problems.append('resolution keys')
    if 'json' + chr(10) + '{' in t[t.index('### 23.1'):]:
        problems.append('a hand-written JSON Schema remains in sec. 23.1')
    # every case r3 removes from r2 names a case of E that covers it, and is gone
    for rid, old, cov_row, cov_case in REMOVED_R2:
        cases = r1.get(cov_row, {}).get('expect', {}).get('cases', [])
        if not any(x.get('case') == cov_case for x in cases):
            problems.append('removed case of %s: covering case not found in %s' % (rid, cov_row))
        if rid in r1 and old != '(row merged)' and any(x.get('case') == old for x in r1[rid]['expect'].get('cases', [])):
            problems.append('removed case of %s still present' % rid)
        if old == '(row merged)' and rid in r1:
            problems.append('merged row %s still present' % rid)
    r24 = block_of(t, 'R6.RECON.24')
    for k in ('splice', 'start_M', 'end_M', 'sha256', 'resolved', 'resolved_sha256', 'confirms'):
        if '`%s`' % k not in r24:
            problems.append('R6.RECON.24 does not define %s' % k)
    r27 = block_of(t, 'R6.RECON.27')
    for k in ('finding', 'repair', 'edit', 'item', 'commits', 'entry_path'):
        if not re.search(r'(?<![A-Za-z_])%s(?![A-Za-z_])' % k, r27):
            problems.append('R6.RECON.27 does not define %s' % k)
    # every review finding, audit row, ranked item and item B is mapped
    if [x[0] for x in REVIEW_MAP] != [str(i) for i in range(1, 11)]:
        problems.append('review map incomplete')
    if [x[0] for x in AUDIT_MAP] != AUDIT_LABELS:
        problems.append('audit map incomplete')
    if [x[0] for x in RANKED_MAP] != [str(i) for i in range(1, 12)]:
        problems.append('ranked map incomplete')
    if [x[0] for x in DELTA_MAP] != ['D%d' % i for i in range(1, 8)]:
        problems.append('delta review map incomplete')
    if [x[0] for x in FOLLOWUP_MAP] != ([str(i) for i in range(1, 14)] + ['S1.%d' % i for i in range(1, 8)] + ['S2']
                                         + ['S3.%d' % i for i in range(1, 9)]):
        problems.append('audit follow-up map incomplete')
    if [x[0] for x in R4_MAP] != ['F1', 'F2', 'F3 / A1', 'F4', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2 / B3', '22', '21', 'T1',
                                  'O', 'T2']:
        problems.append('final-check map incomplete')
    for r, _ in ROWS:
        for x in r['expect']['cases']:
            if x['outcome'] == 'ERROR' and not x.get('stop_class'):
                problems.append('%s: an ERROR case without stop_class' % r['id'])
    if [x[0] for x in NITS_MAP] != ['1', '2', '3', '4', '5']:
        problems.append('amendment 5 nit map incomplete')
    if [x[0] for x in B_MAP] != ['B1', 'B2']:
        problems.append('item B map incomplete')
    return problems


def counts():
    n_cases = sum(len(r['expect']['cases']) for r, _ in ROWS)
    return len(ROWS), n_cases


def change_record(owner, outs, gen_sha, owner_sha, totals):
    nr, nc = counts()
    lines = ['# r6 amendment 6: change record', '',
             'Owner directions, quoted in DESIGN-r6.md sec. 0.7: %s. Generated by generator-amendment6/amend6.py '
             '(sha256 %s) from the amendment-5 outputs (amendment 5 r2, e0706a4b, adopted) and '
             'generator-amendment6/owner-decisions-amendment6.json (sha256 %s). This is r4. r3, the last general revision, '
             'it answers the delta review of r2 (PR #1593 comment 7190255132, D1 to D7) and the completeness-audit '
             'follow-up (PR #1593 comment 7190234470, findings 1 to 13 and section S), and removes complexity that '
             'both reviewers agree gives no protection. It keeps the answers of r2 to the first review (PR #1593 '
             'comment 7189446310), items B1 and B2, the completeness audit (PR #1593 comment 7189621405) and the '
             'amendment 5 nits. r4 makes only the corrections of the two final checks of r3 (PR #1593 comments 7190624085 '
             'and 7190609504), the owner choice on `git_blob`, and the tool writer\'s two defects (R6.RECON.23 '
             'matching; R6.GATE.3 count grammar). Every resolution is a proposal; the choice is the owner\'s at adoption.'
             % ('; '.join('%s, %s (%s), %s' % (d['author'], d['time'], d['record'], d['item'])
                          for d in owner['decisions']), gen_sha, owner_sha), '',
             'Safety rule for every point: no reading may let a category-3 finding be lost or lifted by rewording, and '
             'no rule is weakened to match the tool. The owner\'s lifecycle holds: the block persists for the frozen '
             'plan, a repair does not validate, and a revised plan may proceed (by removing the edit, or by citing an '
             'applying reassessment for each finding).', '',
             '## 0. Counts', '',
             '| | Rows (whole file) | Rows added by amendment 6 | Their cases | Requirements (whole index) | Added |',
             '|---|---|---|---|---|---|',
             '| amendment 5 r2 (base) | %d | | | %d | |' % (totals['base_rows'], totals['base_reqs']),
             '| amendment 6 r2 (319e9bbf) | 621 | 17 | 123 | 443 | 9 |',
             '| amendment 6 r3 (c6df73dd) | 619 | 15 | 134 | 443 | 9 |',
             '| amendment 6 r4 | %d | %d | %d | %d | %d |' % (totals['rows'], nr, nc, totals['reqs'], len(NEW_REQS)), '',
             'r4 generates %d conformance mutants into CONFORMANCE-MUTANTS.json, each an identifiable case of the '
             'RECON-SCHEMA mutant countercase.' % len(mutants()), '',
             'r3 merges RESULT-FIELDS into RECON-ENUM (two cases added there) and WIDENING-ITEMS into REVIEW-SCHEMA, '
             'collapses the individual schema violations of RECON-SCHEMA into one generic conformance case, removes '
             'the hand-written JSON Schema (sec. 23.1 now renders one key table per kind from one definition), and '
             'adds the cases the new rules need. Sec. 6a lists every case removed, with the case that covers it.', '',
             '## 1. The tool writer\'s points 1 to 5', '']
    for title, opts, rec, ctl in POINTS:
        lines += ['### ' + title, '', 'Options:', ''] + ['- ' + o for o in opts] + ['', rec, '',
                                                                                      'Controls: %s.' % ctl, '']
    lines += ['## 2. First review (PR #1593 comment 7189446310)', '', '| Finding | Disposition |', '|---|---|']
    lines += ['| %s | %s |' % (k, v) for k, v in REVIEW_MAP] + ['']
    lines += ['Finding 9 (a deleted finding record is invisible to the scan) is held for a separate Issue. The interim '
              'remedy for a false-alarm finding without a repair, before D3 is adopted, is deleting the file under '
              'AGENTS.md sec. A.50 item 3; that remedy exists only because of that gap, so the Issue for finding 9 '
              'should note that closing it relies on D3.', '']
    lines += ['## 2a. Amendment 5 nits (delta review, PR #1592 comment 7189385508; routed here by the owner, #1169 '
              'comment 7189915409)', '', '| Nit | Disposition |', '|---|---|']
    lines += ['| %s | %s |' % (k, v) for k, v in NITS_MAP] + ['']
    lines += ['## 2b. Delta review of r2 (PR #1593 comment 7190255132)', '', '| Finding | Disposition |', '|---|---|']
    lines += ['| %s | %s |' % (k, v) for k, v in DELTA_MAP] + ['']
    lines += ['## 2c. Completeness-audit follow-up (PR #1593 comment 7190234470)', '', '| Item | Disposition |',
              '|---|---|']
    lines += ['| %s | %s |' % (k, v) for k, v in FOLLOWUP_MAP] + ['']
    lines += ['## 2d. Final checks of r3 (PR #1593 comments 7190624085 and 7190609504) and the tool writer\'s two '
              'defects', '', '| Item | Disposition |', '|---|---|']
    lines += ['| %s | %s |' % (k, v) for k, v in R4_MAP] + ['']
    lines += ['Grammar (T2), rows affected and keys corrected: L2 (`lines[rule=W2,state=PASS]`, `all: lines[rule=W2]`); '
              'RT-D (`lines[state=PASS,rule=W1|W2]`); RT-DR (`lines[rule=DR-1]` and its `alternative=a|b|c` forms, '
              '`lines[rule=DR-3]`, `DR-4`, `DR-5`); RT-DR3W (`sentences[rule=DR-3]`, two cases). Rows whose keys the '
              'stated grammar now admits unchanged: RT-I7A (`fail_lines`, `count_sentence_lines=true`), RT-T0 '
              '(`attribution`, `sites[moved_in=...]`, `sites[region_shared_with_nonempty]`), RT-DR (`line` in a `none` '
              'filter). The expected values are unchanged: RT-DR\'s and RT-I7A\'s 86 deny-match lines at `H` count each '
              'line once at the line where a match begins, and the 93 count every line a sentence spans; a runner whose '
              'items put a sentence-level match on its sentence\'s start line instead reports 87, which is a conformance '
              'difference of the items\' `line` field, not of the expectation.', '']
    lines += ['## 3. Items B (tool writer)', '']
    for k, title, opts, rec in B_MAP:
        lines += ['### %s. %s' % (k, title), '', 'Options:', ''] + ['- ' + o for o in opts] + ['', rec, '']
    lines += ['## 4. Schema completeness audit (PR #1593 comment 7189621405)', '',
              'Rows are labelled by the audit\'s section and their order in it.', '',
              '| Row | Field | Disposition |', '|---|---|---|']
    lines += ['| %s | %s | %s |' % x for x in AUDIT_MAP] + ['', 'Ranked gaps:', '', '| Rank | Covered by |', '|---|---|']
    lines += ['| %s | %s |' % x for x in RANKED_MAP] + ['']
    lines += ['Where the tool accepts input the design refuses, the design rule is stated and a countercontrol is '
              'kept: a missing or empty `changes_decisions_on_X`, float or boolean offsets, `"shift"`, an '
              '`oi-reconciliation/1` record, two entries with one path, splice-list completeness (RECON-SCHEMA); the '
              '`.json` suffix filter and skipped parse failures (SCAN-PARSE); skipped or unknown record kinds, '
              '`default_for`, `notes`, `sites` and a run without `--check` (CONFIG-REFS); an optional `git_blob` and '
              'the class-level `paths` form (CLASS-SCHEMA); `widening_review` (REVIEW-SCHEMA).', '']
    lines += ['## 5. Points for the owner\'s choice', '']
    lines += ['%d. %s' % (i + 1, x) for i, x in enumerate(OWNER_CHOICES)] + ['']
    lines += ['## 6. Changes', '', '| File | Place | Change |', '|---|---|---|',
              '| DESIGN-r6.md | R6.REC.2, R6.REC.6, R6.REC.7, R6.REC.17 | verdict values and keys; every review counts; '
              'reference resolution; the one unbounded walk |',
              '| DESIGN-r6.md | R6.RECON.10 | RC5 rewritten |',
              '| DESIGN-r6.md | R6.RECON.24 | RC14 (b) from the retained text; resolution schema, deletion splices, '
              'non-UTF-8 blobs, review confirmation |',
              '| DESIGN-r6.md | R6.RECON.25 | `invalidated` form |',
              '| DESIGN-r6.md | R6.RECON.26 | one definition of a finding; lineage cited; the global matches; Form of a '
              'finding (i) to (vi) |',
              '| DESIGN-r6.md | R6.RECON.27 | the body names the parts; Keys; `repair` and `edit` null |',
              '| DESIGN-r6.md | R6.RECON.21, R6.RECON.2 (d) | `x` at `X`; detection and scanned set per R6.RECON.35 |',
              '| DESIGN-r6.md | R6.CFG.4 | kinds; `retirement`; `executed_suffixes` |',
              '| DESIGN-r6.md | R6.ADAPT.2 | raw entries, `edits`, retained `text`, strict parsing |',
              '| DESIGN-r6.md | R6.TREE.5, R6.CTX.7, R6.HIT.4, R6.OUT.18 | class keys; element ids; result fields |',
              '| DESIGN-r6.md | R6.RECON.28 (new); sec. 23.1, R6.RECON.29 to R6.RECON.36 (new) | the migration record; '
              'the schema contract, one key table per kind |',
              '| DESIGN-r6.md | sec. 0.7, sec. 31, R6.CTRL.3, Table 17.1 | the note; the RT-D figure; %d rows counted and '
              'added |' % len(ROWS),
              '| EXPECTATIONS.json | %s (new) | both directions each |' % ', '.join(NEW_IDS),
              '| EXPECTATIONS.json | RECON-BLOCK | the revised-plan countercase requires a cited reassessment; no '
              'expectation value changes |',
              '| EXPECTATIONS.json | RECON-ENUM | the result fields of R6.RECON.36, both directions (merged from '
              'RESULT-FIELDS) |',
              '| EXPECTATIONS.json | S11-2a, RTL2-BIND, RT-D, RT-DR | the amendment 5 nits (sec. 2a), each a declared '
              'change |',
              '| REQUIREMENTS.json | %s (new); %s | controls appended; `pending_owner_confirmation` |'
              % (', '.join(NEW_REQS), ', '.join(TOUCHED)), '',
              '## 6a. Cases of r2 removed or merged, with the case that covers each', '',
              '| Row in r2 | Case removed | Covered by |', '|---|---|---|']
    lines += ['| %s | %s | %s: %s |' % x for x in REMOVED_R2] + ['']
    lines += ['## 7. Tool changes implied (not made here)', '',
              '- Finding detection over every JSON-shaped file before lint; form failures that still block; the '
              'global matches by path and old bytes or by id and path; the fallback; run-level binding (R6.RECON.26, '
              'R6.RECON.35).',
              '- The reassessment keys, per-finding lifting, `repair` and `edit` null (R6.RECON.27); migration lint '
              'and closure (R6.RECON.28).',
              '- RC5 as rewritten (R6.RECON.10); RC14 (b) from the retained text; the resolution checks, deletion '
              'splices and `confirms` (R6.RECON.24).',
              '- The schema contract: strict parsing, the key tables before any RC, full-match encodings, item ids, '
              'kinds, reference resolution per admission mode, class record keys, the result fields (R6.RECON.29 to '
              'R6.RECON.36).',
              '- The ledger adapter returns `raw`, `edits` and the retained `text`, and parses the ledger and edit '
              'list strictly (R6.ADAPT.2); configurations carry `executed_suffixes` (R6.CFG.4).',
              '- Fixtures: every control review record carries `reason` in each verdict and a full object id in '
              '`method`; the EI4 fixture drops `notes`; configuration fixtures add `executed_suffixes`. No '
              'expectation value changes.',
              '- Allowlist and schema list (R6.CORE.5): `oi-reassessment/1`, `oi-edit-id-migration/1`, and the new '
              'keys and values where the engine holds them as literals.',
              '- Runners for %s, and for the RECON-ENUM cases added.' % ', '.join(NEW_IDS), '',
              '## 8. Outputs', '', '| File | sha256 |', '|---|---|']
    for n in ('DESIGN-r6.md', 'EXPECTATIONS.json', 'REQUIREMENTS.json', 'CONFORMANCE-MUTANTS.json'):
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
    rows = ('| CONFORMANCE-MUTANTS.json | the conformance mutants of R6.RECON.29, generated from the key tables | '
            'amendment-6 output | %s |\n' % sha(outs['CONFORMANCE-MUTANTS.json'])
            + '| AMENDMENT-6.md | change record of amendment 6 | amendment-6 output | %s |\n'
            '| generator-amendment6/amend6.py | amendment-6 generator | amendment-6 generator | %s |\n'
            '| generator-amendment6/owner-decisions-amendment6.json | amendment-6 generator input (the owner directions '
            'quoted) | amendment-6 generator | %s |\n' % (sha(outs['AMENDMENT-6.md']), gen_sha, owner_sha))
    m = once(m, '| LANDING-MANIFEST.md | this manifest (A5) | amendment-5 output | (this file) |',
             rows + '| LANDING-MANIFEST.md | this manifest (A5) | amendment-6 output | (this file) |', 'manifest self')
    para = ('\nAmendment 6 (owner directions of 2026-11-26, amaybaum, #1169 comments 7187418279, item 4, 7188752730, '
            'item 2, and 7189470338, items 1, 3 and 4, quoted in DESIGN-r6.md sec. 0.7): DESIGN-r6.md, EXPECTATIONS.json '
            'and REQUIREMENTS.json are amended, and AMENDMENT-6.md records the options, the proposals and the points '
            'for the owner\'s choice. Recipe: run the amendment-5 recipe into `out5/` and run '
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
    outs = {'DESIGN-r6.md': t.encode('utf-8'), 'EXPECTATIONS.json': dumpj(E), 'REQUIREMENTS.json': dumpj(R),
            'CONFORMANCE-MUTANTS.json': dumpj(mutants_doc())}
    with open(os.path.join(HERE, 'amend6.py'), 'rb') as f:
        gen_sha = sha(f.read())
    totals = {'base_rows': len(E0['rows']), 'base_reqs': len(R0), 'rows': len(E['rows']), 'reqs': len(R)}
    outs['AMENDMENT-6.md'] = change_record(owner, outs, gen_sha, sha(owner_b), totals).encode('utf-8')
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
