"""Generator of amendment 6 (r2) to design r6: the category-3 schema ambiguities raised by the tool writer (points 1 to
5), the independent review of the first draft (PR #1593 comment 7189446310, findings 1 to 8 and 10), two further
ambiguities found by the tool writer (RC14 (b) and the R6.RECON.24 resolution schema), and the schema completeness
audit of the reconciliation record kinds (PR #1593 comment 7189621405), under the owner's directions of 2026-11-26
(#1169 comments 7187418279, item 4; 7188752730, item 2; 7189470338, items 1, 3 and 4).

Usage: python3 -I -B amend6.py BASE OUT

BASE holds DESIGN-r6.md, EXPECTATIONS.json, REQUIREMENTS.json and LANDING-MANIFEST.md as amendment 5 leaves them
(each checked against its sha256 below). The script reads owner-decisions-amendment6.json beside itself and writes
into OUT the amended DESIGN-r6.md, EXPECTATIONS.json and REQUIREMENTS.json, the change record AMENDMENT-6.md and the
updated LANDING-MANIFEST.md. Every recommendation is a proposal for the owner's decision at adoption.

Self-checks: no existing row changes except RECON-BLOCK, whose cases keep their outcomes and gain one; no requirement
loses a control or changes a field other than its controls and pending entries; every new row records both
directions and has a countercase; correspondence; the closed invariant vocabulary; the amendment-6 mark on every
touched requirement; the JSON Schema of R6.RECON.30 parses and names exactly the keys of its table; every review
finding, audit row and item B is mapped in the change record. Standard library only; deterministic.
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


SRC = 'r6 amendment 6 (owner direction of 2026-11-26, #1169 comment 7187418279, item 4; tool writer\'s points 1 to 5)'
SRC2 = ('r6 amendment 6 r2 (owner decisions of 2026-11-26, #1169 comments 7188752730, item 2, and 7189470338, items 1, '
        '3 and 4; independent review of ed9faa8a, PR #1593 comment 7189446310; schema completeness audit, PR #1593 '
        'comment 7189621405)')
FLAG = 'added by amendment 6 (a proposal); no runner records it before the tool revision implements it'

BLOCKED = {'outcome': 'FAIL', 'classes_include': ['retirement-blocked']}
BLOCKED_INV = {'outcome': 'FAIL', 'classes_include': ['retirement-blocked', 'record-invalid']}
NOT_BLOCKED = {'outcome': 'ANY', 'invariants': [{'not_class': ['retirement-blocked']}]}
INVALID = {'outcome': 'FAIL', 'classes_include': ['record-invalid']}
INVALID_DRIFT = {'outcome': 'FAIL', 'classes_include': ['record-invalid', 'base-drift']}
INVALID_NOT_BLOCKED = {'outcome': 'FAIL', 'classes_include': ['record-invalid'],
                       'invariants': [{'not_class': ['retirement-blocked']}]}
CLEAN = {'outcome': 'ANY', 'invariants': [{'not_class': ['base-drift', 'record-invalid']}]}
RESOLVED = {'outcome': 'ANY', 'invariants': [{'not_class': ['base-drift', 'record-invalid']},
                                             {'equals': 'the path\'s disposition is reconciled-resolved, category 2'}]}
RECONCILED = {'outcome': 'ANY', 'invariants': [{'not_class': ['base-drift', 'record-invalid']},
                                               {'equals': 'the path\'s disposition is reconciled, category 1'}]}
CONFIG_ERR = {'outcome': 'ERROR', 'invariants': [{'stop_class_in': ['CONFIG_INVALID', 'CONFIG_UNREVIEWED']}]}
CONFIG_OK = {'outcome': 'ANY', 'invariants': [{'no_stop': True}]}


def rc(cond):
    return {'outcome': 'FAIL', 'classes_include': ['base-drift'], 'invariants': [{'failed_conditions_include': cond}]}


def c(case, base):
    return dict(case=case, **copy.deepcopy(base))


def row(rid, req, cases, summary, src=SRC2):
    r = {'id': rid, 'requirements': req, 'runner': None, 'operations': ['execution'], 'direction': 'both',
         'expect': {'cases': cases}, 'source': src, 'flags': [FLAG]}
    return r, summary


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
        'point 1 and review findings 3, 4 and 8: detection before lint; only an independence failure disqualifies; an '
        'empty fallback binds at run level; every review naming the blob counts'),
    row('FINDING-LINEAGE', ['R6.RECON.26'], [
        c('a finding naming its configuration; a later configuration on that configuration\'s supersedes chain carries '
          'the edit', BLOCKED),
        c('a fork outside the lineage (supersedes null, a new config_id, a new retirement name and Issue) carrying the '
          'invalidated edit under the same id and target with reworded new text, citing no reassessment', BLOCKED),
        c('the same fork carrying the invalidated edit\'s target (the same path and old bytes) under another id',
          BLOCKED),
        c('countercase: a configuration of another retirement, outside the lineage, whose ledger reuses the edit id '
          'with another target (another path, or old bytes whose sha256 differs from the recorded old_sha256) '
          '(positive)', NOT_BLOCKED),
        c('a finding naming no configuration, or one that cannot be read: it binds every configuration whose ledger '
          'carries the edit by id, a migrated id or the target, the other retirement\'s id collision included',
          BLOCKED_INV),
        c('a finding naming no configuration; a superseding configuration renames the edit id, keeps its old bytes and '
          'records no migration', BLOCKED_INV),
        c('a finding whose invalidated element differs from the named configuration\'s ledger (the id absent there, or '
          'another target): the fallback binds every configuration carrying the id, a migrated id or the target',
          BLOCKED_INV),
        c('a finding naming a readable configuration of another lineage whose ledger holds the same id and target: the '
          'retirement\'s own configuration carrying the target is still blocked', BLOCKED),
        c('countercase: the other retirement bound only by the fallback\'s id collision, frozen anew with the colliding '
          'id renamed under a recorded migration, its target different (positive)', NOT_BLOCKED)],
        'point 2 and review findings 1, 2 and 6: the path-and-old-bytes match is global; the fallback matches by id, '
        'migrated id or target; the remedy for an id collision is a rename'),
    row('FINDING-KEYS', ['R6.RECON.26', 'R6.RECON.25'], [
        c('an invalidated element {id, sha256, target: {path, start_H, old_sha256}} matching the ledger edit of that id '
          'at the named configuration\'s H', BLOCKED),
        c('an element whose target differs from the ledger edit of its id (form failure; the element blocks through the '
          'fallback)', BLOCKED_INV),
        c('an element {id, sha256} without target (form failure; the id still blocks)', BLOCKED_INV),
        c('an element whose start_H and old_sha256 are those of a commit other than the named configuration\'s H',
          BLOCKED_INV),
        c('an element naming a retained edit (no splice), its target the occurrence of the retained text at H', BLOCKED),
        c('countercase: a revised configuration keeping only an edit of the same path that no finding names, whose old '
          'bytes\' sha256 differs from every recorded old_sha256, without a reassessment (positive)', NOT_BLOCKED)],
        'point 4, review finding 5 and audit ranked item 2: the invalidated element, read against the named '
        'configuration; a retained edit can be named'),
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
        c('a migration record whose approval lacks quote, author or time, or whose time is not of the stated form; the '
          'renamed edit\'s old bytes unchanged', BLOCKED_INV),
        c('countercase: a configuration that removes the renamed edit (neither its old id, its new id nor its old '
          'bytes remain) (positive)', NOT_BLOCKED),
        c('countercase: a lint-passing migration record found at M that neither the configuration nor its supersedes '
          'chain references, mapping the invalidated id to an id of this configuration whose edit has another target '
          '(the mapping is not applied) (positive)', NOT_BLOCKED)],
        'point 3, review finding 7 and audit G: where a recorded migration lives; lint against reuse; only referenced '
        'records apply; a migration never lifts a block'),
    row('REASSESS-KEYS', ['R6.RECON.27', 'R6.RECON.32'], [
        c('one record carrying findings on two entries (paths p and q) against the same edit; the revised configuration '
          'cites one reassessment whose finding names the record with item p only', BLOCKED),
        c('a reassessment whose finding lacks item', BLOCKED_INV),
        c('a reassessment whose repair.commits holds an abbreviated commit id, or a commit not on M\'s first-parent '
          'chain', BLOCKED_INV),
        c('a reassessment whose repair.entry names an entry_path that the named reconciliation record has no entry for',
          BLOCKED_INV),
        c('a reassessment whose edit.sha256 is computed over a non-canonical serialization of the edit-list entry (it '
          'differs from the canonical sha256)', BLOCKED_INV),
        c('a reassessment with edit null for a finding bound to an edit (not at run level)', BLOCKED_INV),
        c('a reassessment whose rederivation is not a non-empty string, or which carries a key outside the table',
          BLOCKED_INV),
        c('countercase: two reassessments, one for each finding, each naming its record and item, with repair and edit '
          'as defined (positive)', NOT_BLOCKED)],
        'review finding 5 and audit C: the reassessment keys; one reassessment lifts only the finding it names'),
    row('RECON-RETAINED', ['R6.RECON.24', 'R6.ADAPT.2'], [
        c('M changes a byte of the line holding a retained edit\'s text at H', rc('RC14')),
        c('M adds a second copy of a retained site\'s line elsewhere in the file', rc('RC14')),
        c('a retained edit whose text spans two lines; M changes a byte of the second line', rc('RC14')),
        c('a retained site that moved between E and H (its site-map pin_line differs from its line at H), M not '
          'touching its line: the line at H is found from the retained text, with no E..H walk (positive)', CLEAN),
        c('countercase: M changes bytes outside every context window and every retained site\'s line (positive)',
          CLEAN)],
        'item B1: RC14 (b) finds the retained site\'s line at H from the retained text; the site map identifies the '
        'site only'),
    row('RESOLUTION-SCHEMA', ['R6.RECON.24', 'R6.REC.2'], [
        c('a resolution {splice, start_M, end_M, sha256, resolved, resolved_sha256}: 0-based byte offsets into the '
          'entry\'s m blob, end exclusive; sha256 of m[start_M:end_M]; resolved the canonical base64 of the replacement '
          'bytes; resolved_sha256 their sha256; l equal to the composition; the review\'s verdict on '
          '<path>:resolution:<splice> accept with confirms equal to the window and resolved_sha256 (positive)',
          RESOLVED),
        c('countercase (window): end_M greater than the length of the m blob', INVALID_DRIFT),
        c('countercase (window): start_M equal to end_M', INVALID_DRIFT),
        c('countercase (window): start_M inside a multi-byte UTF-8 character', INVALID_DRIFT),
        c('countercase (window): a float (5.0), boolean or string offset', INVALID_DRIFT),
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
        c('countercase (review): no verdict on <path>:resolution:<splice>', INVALID_DRIFT),
        c('countercase: a resolution carrying a key outside the six', INVALID_DRIFT)],
        'item B2 (owner decision 7189470338, item 1): the resolution schema, its mechanical checks and the bound review '
        'confirmation'),
    row('RECON-SCHEMA', ['R6.RECON.29', 'R6.RECON.30'], [
        c('a record that passes the JSON Schema of R6.RECON.30 and every table rule, with record_id, supersedes null '
          'and author (positive)', CLEAN),
        c('countercase: changes_decisions_on_X missing', INVALID_DRIFT),
        c('countercase: changes_decisions_on_X null, {} or ""', INVALID_DRIFT),
        c('countercase: a splice offset written 5.0, or true', INVALID_DRIFT),
        c('countercase: a splice without start_M', INVALID_DRIFT),
        c('countercase: a splice translation "shift"', INVALID_DRIFT),
        c('countercase: a protected range with a non-integer offset', INVALID_DRIFT),
        c('countercase: a key outside the table, at the top level or in an entry', INVALID_DRIFT),
        c('countercase: two entries with one path', INVALID_DRIFT),
        c('countercase: an entry path with a leading /, a . or .. component, or a trailing /', INVALID_DRIFT),
        c('countercase: M, X or ledger_base in upper case or abbreviated', INVALID_DRIFT),
        c('countercase: a record without record_id', INVALID_DRIFT),
        c('countercase: a record of schema oi-reconciliation/1 read by the run', INVALID_DRIFT),
        c('countercase: a splice translation given as an integer other than start_M - start_H', rc('RC5'))],
        'audit A (ranked items 3 and 10): the field schema of oi-reconciliation/2; a malformed field is record-invalid '
        'before any condition; /1 retired'),
    row('RECON-FIELDS', ['R6.RECON.30', 'R6.RECON.21'], [
        c('a mode-only change of a ledgered path on M (100644 to 100755), the commit listed in side_change_commits and '
          'every other condition holding (positive)', RECONCILED),
        c('countercase: the same mode-only change with side_change_commits empty', rc('RC1')),
        c('countercase: a ledgered path deleted at M', rc('RC2')),
        c('countercase: x naming the path\'s blob at C where C differs from X', rc('RC8')),
        c('a no-effect entry whose conclusions name an edit removed by a revised plan, read against the configuration '
          'it names (positive: no form failure)', {'outcome': 'ANY',
                                                   'invariants': [{'not_class': ['record-invalid']}]}),
        c('countercase: an entry for a .py path whose method does not contain the l blob id', INVALID_DRIFT),
        c('countercase: an entry for a path a delegation class covers whose method does not contain the l blob id',
          INVALID_DRIFT)],
        'audit A rows M/X, blob ids, side_change_commits, conclusions and method (ranked items 4, 8, 9 and 10)'),
    row('CANON-JSON', ['R6.RECON.29', 'R6.ADAPT.2'], [
        c('a ledger_binding computed from the raw files entry, the path\'s raw splices in ledger order and the path\'s '
          'raw edit-list entries in edit-list order, canonical JSON with non-ASCII text written as UTF-8 (positive)',
          CLEAN),
        c('countercase: edit_records_sha256 computed with non-ASCII characters escaped as \\u sequences', rc('RC13')),
        c('countercase: splices_sha256 computed over the splices in another order', rc('RC13')),
        c('countercase: a ledger adapter that returns no raw edit-list entries (the interface is incomplete)',
          {'outcome': 'ERROR', 'invariants': [{'stop_class_in': ['LEDGER_INTEGRITY', 'CONFIG_INVALID']}]})],
        'audit A ledger_binding and ranked item 2: the canonical JSON and the raw entries in the ledger interface'),
    row('REVIEW-SCHEMA', ['R6.RECON.31', 'R6.REC.2'], [
        c('a review record with reviewer, reviewed {path, blob_sha256} matching the record, method naming a full object '
          'id, and verdicts {item, verdict, reason} covering the item ids of the table (positive)', CLEAN),
        c('countercase: a verdict entry without reason, or with a key outside the table', INVALID_DRIFT),
        c('countercase: reviewed naming the record\'s blob under another path', INVALID_DRIFT),
        c('countercase: method naming no full object id', INVALID_DRIFT),
        c('countercase: verdicts whose item strings are not the item ids of the table (for example "entry 1")',
          INVALID_DRIFT),
        c('countercase: a reconciliation record without a review in its own directory, its only review lying in '
          'another directory', INVALID_DRIFT)],
        'audit B: the review record\'s keys, identity, method and the item-id table'),
    row('WIDENING-ITEMS', ['R6.RECON.31'], [
        c('a widening review of kind widening with replaces naming the superseded blob and one verdict for each item id '
          'of the difference rule, all accept (positive)', CLEAN),
        c('countercase: a widening review without kind widening, or without replaces', INVALID),
        c('countercase: a widening review that omits the item field:<key> of a changed top-level key', INVALID),
        c('countercase: a configuration carrying a widening_review key', CONFIG_ERR)],
        'audit B widening review: kind, replaces and deterministic item ids'),
    row('CONFIG-REFS', ['R6.RECON.33', 'R6.CFG.4'], [
        c('a configuration whose records entries each carry a kind of the enumeration with a record of the mapped '
          'schema, roles.side_change_classes also listed in records with the same blob, retirement {name, issue} '
          '(positive)', CONFIG_OK),
        c('countercase: a records entry of a kind outside the enumeration', CONFIG_ERR),
        c('countercase: a records entry whose record has a schema other than its kind\'s', CONFIG_ERR),
        c('countercase: roles.side_change_classes not listed in records, or listed with another blob', CONFIG_ERR),
        c('countercase: retirement.issue a string, or retirement without name', CONFIG_ERR),
        c('countercase: a check carrying default_for (a key outside R6.CFG.4)', CONFIG_ERR)],
        'audit D (ranked item 7): the kind enumeration and schema map, the class role, retirement keys, default_for'),
    row('SUPERSEDES-RESOLVE', ['R6.RECON.33', 'R6.REC.7'], [
        c('a configuration version 2 at the fixed configuration path whose supersedes names version 1, overwritten at '
          'F: version 1 resolves at the newest commit on F\'s first-parent chain whose tree holds that path with that '
          'blob (positive)', CONFIG_OK),
        c('a finding made under version 1 binds version 2, resolved in that way, which carries the edit', BLOCKED),
        c('countercase: a supersedes blob that no commit on F\'s first-parent chain holds at that path',
          {'outcome': 'ERROR', 'invariants': [{'stop_class_in': ['CONFIG_INVALID', 'CONFIG_UNREVIEWED']}]})],
        'audit D supersedes resolution and lineage direction (ranked item 1)'),
    row('CLASS-SCHEMA', ['R6.RECON.34', 'R6.TREE.5'], [
        c('a class record whose classes carry id, prefixes and pins [{path, git_blob, blob_sha256}] (positive)', CLEAN),
        c('countercase: a pin without git_blob', INVALID),
        c('countercase: a class carrying the class-level paths form', INVALID),
        c('countercase: a superseding class record that adds a pin without a widening review', INVALID)],
        'audit E: side-change class record keys and widening'),
    row('SCAN-PARSE', ['R6.RECON.35', 'R6.RECON.2'], [
        c('a review record carrying a finding, stored without a .json suffix in a reconciliation directory', BLOCKED),
        c('a file under verification/audits/ containing the string oi-review-record/1 that fails strict parsing '
          '(invalid UTF-8, a byte-order mark, a duplicate key, NaN): a malformed finding, run level', BLOCKED_INV),
        c('two byte-identical reconciliation records at different paths covering one path: two records',
          INVALID_DRIFT),
        c('a review carrying a finding that lies in a reconciliation directory other than its record\'s', BLOCKED_INV),
        c('countercase: a non-JSON file under verification/audits/ that contains no schema string of a scanned kind '
          '(not in the scanned set) (positive)', {'outcome': 'ANY',
                                                   'invariants': [{'not_class': ['record-invalid',
                                                                                 'retirement-blocked']}]})],
        'audit F (ranked item 6): file selection, strict parsing, record identity, review location'),
    row('RESULT-FIELDS', ['R6.RECON.36', 'R6.OUT.18'], [
        c('an op C result with M: dispositions entries carry exactly path, disposition, category, record, failed, '
          'conflicts and why; category3 carries findings, blocked and reassessments; inputs.classify_records entries '
          'carry the review; inputs.record_base is present (positive)', {'outcome': 'ANY',
                                                                         'invariants': [{'schema_errors': 0}]}),
        c('countercase: a result whose dispositions entry lacks record', {'outcome': 'ANY',
                                                                         'invariants': [{'schema_errors': 1}]})],
        'audit A dispositions and H: the result fields'),
]

NEW_IDS = [r['id'] for r, _ in ROWS]
REQ_CONTROLS = {}
for _r, _ in ROWS:
    for _q in _r['requirements']:
        REQ_CONTROLS.setdefault(_q, []).append(_r['id'])
NEW_REQS = ['R6.RECON.28', 'R6.RECON.29', 'R6.RECON.30', 'R6.RECON.31', 'R6.RECON.32', 'R6.RECON.33', 'R6.RECON.34',
            'R6.RECON.35', 'R6.RECON.36']
TOUCHED = ['R6.RECON.26', 'R6.RECON.25', 'R6.RECON.24', 'R6.RECON.27', 'R6.RECON.21', 'R6.RECON.2', 'R6.REC.2',
           'R6.REC.6', 'R6.REC.7', 'R6.CFG.4', 'R6.ADAPT.2', 'R6.TREE.5', 'R6.OUT.18']
# the Controls line of each touched requirement, as it stands in the base (the new rows are appended to it)
CONTROLS_ANCHOR = {
    'R6.RECON.26': 'Controls: RECON-BLOCK, BLOCK-KEY.',
    'R6.RECON.25': 'Controls: RECON-SCI, RECON-BLOCK, BLOCK-KEY.',
    'R6.RECON.24': 'Controls: RECON-CONFLICT, RECON-CATEGORY, RECON-OVERLAP.',
    'R6.RECON.27': 'Controls: BLOCK-KEY, REASSESS-FORM.',
    'R6.RECON.21': 'RTL2-BIND, RECON-TRIAL, RECORD-BASE.',
    'R6.RECON.2': 'RB-C10, RB-C11.',
    'R6.REC.2': 'Sources: E-136, V2-056, RV-019. Controls: O1, O2, O3, O5, O7, I2-5.',
    'R6.REC.6': 'Controls: O1, O2, O3, O5, R3-F2, R4-B3, R4-B3-DUP, R5-N6, GV6.',
    'R6.REC.7': 'LN7, LN8, LN10, R6-G6, POSTF-4.',
    'R6.CFG.4': 'CONFIG-LINT, Z8, BLOCK-KEY.',
    'R6.ADAPT.2': 'E-1428. Controls: U10, U11, M3, M4, M5, Z9h.',
    'R6.TREE.5': 'Controls: R18, R18-engine, R19, R19-engine, Z11, TT13, RDIR-24.',
    'R6.OUT.18': 'S7-schema-and-checker, B4-MEANING, U2, U9, U10.',
}

RECON_BLOCK_OLD = ('countercase: the run under a revised plan, a new configuration whose ledger changes the invalidated '
                   'edit\'s edit-list entry (positive)')
RECON_BLOCK_NEW = ('countercase: the run under a revised plan, a new configuration whose ledger changes the invalidated '
                   'edit\'s edit-list entry and whose freeze cites an applying reassessment naming the finding '
                   '(R6.RECON.27) (positive)')
RECON_BLOCK_ADDED = {'case': 'a revised plan whose ledger changes the invalidated edit\'s edit-list entry (a wording '
                             'change, the same id and target) and cites no reassessment', 'outcome': 'FAIL',
                     'classes_include': ['retirement-blocked']}

FORM = '''

**Form of a finding** %(mark)s. (i) *Detection precedes lint.* The scan of this requirement reads
every review record in the sets it scans (R6.RECON.35), whether or not the review passes record lint. A review record
counts as a finding of the second kind when an entry of its `verdicts`, on any item of a reconciliation record entry,
has the verdict value `invalidates` or carries the key `invalidated`, unless its independence fails: its `reviewer`
equals the `author` of the record its `reviewed` names (R6.RECON.29), or is a run, check or Issue (R6.REC.6). Only
such an independence failure disqualifies it; a review whose `reviewed` names no record the scan finds, so that its
independence cannot be established, counts, as a form failure. Every other failure of such a review (its schema or
fields, R6.RECON.31; a missing `method`; verdicts that omit or duplicate an item; `invalidates` on an item other than
`<path>:scientific_effect`; `invalidated` with a verdict value other than `invalidates`; an empty or malformed
`invalidated`; a missing or unreadable `configuration`) is a form failure, FAIL `record-invalid`, and the finding still
blocks. A well-formed finding of the second kind is the verdict `invalidates` on `<path>:scientific_effect` with a
non-empty `invalidated` of the form (ii) and a `configuration` (iii); `oi-review-record/1` permits `invalidates` on that
item only (R6.REC.2). The verdict `invalidates` makes the reviewed record fail its own chain lint (R6.REC.6) and not
apply; it does not make the review invalid. A finding of the first kind is likewise read before the record's schema
and lint: an entry whose `scientific_effect` has the verdict `invalidates` or carries `invalidated` counts, and a
failure of the record's form is a form failure that still blocks. (ii) *The invalidated element.* Each element of
`invalidated`, in an entry's `scientific_effect` or in a review verdict, is `{id, sha256, target: {path, start_H,
old_sha256}}`, read against the configuration named in (iii): `id` is an edit id of that configuration's edit list
(R6.ADAPT.2 `edits`), a retained edit included; `sha256` is the canonical sha256 (R6.RECON.29) of that edit-list entry;
`target` gives, at that configuration's `H` (`roles.scientific_base`), the edit's file, its start and the sha256 of its
old bytes: for an edit with a splice, the splice's `file`, `start` and `old_sha256`; for a retained edit, the start and
the sha256 of its text's occurrence at `H` (R6.RECON.24 (b)). An element that lacks a key, or any of whose values
differs from that configuration's ledger, is a form failure, FAIL `record-invalid`, and blocks through the fallback of
(iii). (iii) *Configuration.* Every finding names `configuration`, the reference of the configuration under which it
was made: the entry's `scientific_effect` carries it for the first kind, the review verdict entry for the second. It is
resolved by the search of R6.RECON.33, and the plan lineage is computed from it: a configuration is in the lineage when
the finding's configuration lies on its `supersedes` chain, itself included, or when it names the same retirement
(R6.RECON.33). A finding whose `configuration` is absent or cannot be resolved, or one of whose `invalidated` elements
differs from the named configuration's ledger, is a form failure, FAIL `record-invalid`, and binds, besides the
lineage where one is readable, every configuration whose ledger carries one of its edits, whatever its lineage or
retirement; here a ledger carries an edit when it holds the edit's id, an id the edit was renamed to under
R6.RECON.28, or an edit of the target's path whose old bytes hash to the target's `old_sha256`. (iv) *The edits a
finding binds.* A finding binds the edits its `invalidated` elements name, by id and, where an element carries one, by
target. Where `invalidated` is absent, empty or unreadable, or the verdict lies on an item other than
`<path>:scientific_effect`, it binds every edit the entry's `conclusions` name, or, if they name none, every edit of
the entry's path. Where that set is empty (for example `conclusions: "none"` on a corpus path the ledger does not
list), or the finding names no entry the scan finds, it binds at run level every configuration of its lineage, and
every configuration when its `configuration` cannot be resolved: each such run has a run-level item FAIL
`retirement-blocked` naming the finding, as amendment 3 provides for a path that does not differ. That binding is
lifted only by a new freeze that cites an applying reassessment naming the finding, with `edit` null (R6.RECON.27).
(v) *Scope of the matches.* The id match and the migration match are scoped to the plan lineage; the
path-and-old-bytes match applies to every configuration, whatever its lineage, so a fork (a configuration with
`supersedes: null`, a new `config_id` and a new retirement name and Issue) that carries the invalidated edit's target
is blocked. A configuration bound only by an id collision (through the fallback of (iii), its edit of that id having
another target) proceeds by a new freeze that renames the colliding id, through an AGENTS.md sec. A.48 item 3
migration where records cite it; a configuration bound by the target proceeds, as any blocked plan does, by removing
the edit or by an applying reassessment. No later record narrows a finding's binding. (vi) The migrations the edit-id
match follows are those of R6.RECON.28.'''

KEYS27 = '''

**Keys** %(mark)s. `finding` is `{path, blob_sha256, item}`: the reference of the record or review
record carrying the finding, and `item`, which of its findings is meant: for a finding of the first kind, the entry's
path; for one of the second kind, the item id of the verdict entry carrying it (for example
`<path>:scientific_effect`). A reassessment lifts only the finding it names; a record or review that carries several
findings needs one reassessment for each. `repair` is `{commits, entry}`: `commits`, a non-empty array of distinct
commit ids (R6.RECON.29), each on `M`'s first-parent chain; `entry`, `{path, blob_sha256, entry_path}`, the reference of
the reconciliation record that records the repair and the path of its entry for the repairing change. `edit` is `{id,
sha256}`: `id`, an edit id of the citing configuration's edit list; `sha256`, the canonical sha256 (R6.RECON.29) of
that id's edit-list entry in the citing configuration, so that a later rewording of the edit needs a new
reassessment. `edit` is null exactly when the named finding is bound at run level (R6.RECON.26, Form of a finding
(iv)). A key that is missing, of another type, or outside the table of R6.RECON.32 is a form failure: the reassessment
does not apply, FAIL `record-invalid`, and the block stands.'''

NEW_REQ28 = '''
**R6.RECON.28** **Edit-id migration record** %(mark)s. A rename of a ledger edit id under AGENTS.md
sec. A.48 item 3 is recorded for the tool in a reviewed, immutable record of schema `oi-edit-id-migration/1`, under the
ownership chain of sec. 11, with the fields of R6.RECON.32: `migrations`, a list of `{old, new}` edit ids, and
`approval`, the owner's recorded approval quoted with its author and time. A configuration that carries a renamed edit
references the record in `records` with kind `edit-id-migration` (R6.CFG.4). For R6.RECON.26 the tool maps a finding's
edit id through every such record that the configuration, or a configuration on its `supersedes` chain, references,
taking the transitive closure. A record that fails record lint is FAIL `record-invalid` and maps nothing. A migration
record never lifts a block: the path-and-old-bytes match of R6.RECON.26 applies whether or not a migration is
recorded, and a mapping only adds edits the block binds. The tool checks `approval` for form only (R6.RECON.32); it
neither reads nor checks the owner's approval (R6.REC.3). Record lint also rejects a record in which an `old` or a
`new` repeats or an `old` equals its `new`, and a record referenced by a configuration on whose `supersedes` chain
(itself included) some configuration's ledger holds both an `old` and its `new`: the `new` id would then be an id in
use, which AGENTS.md sec. A.48 item 3 forbids. Only referenced records apply: a migration record that no configuration
on the chain references is not used (R6.REC.4, R6.REC.5), even where the scan finds it, so a record written for
another plan cannot map this plan's ids, and every mapping a run applies is pinned at the freeze by its blob sha256. A
rename that also rewrites the edit's old bytes is matched only through a recorded, referenced migration; otherwise it
rests on the review of the new freeze (R6.RECON.26).
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

RESOLUTION = '''
**Resolution schema** %(mark)s. Each element of `resolutions` is `{splice, start_M, end_M,
sha256, resolved, resolved_sha256}` (owner decision of 2026-11-26, #1169 comment 7189470338, item 1), with no other key:
- `splice`: the id of the conflicting retirement edit's splice in the configuration's ledger (R6.ADAPT.2
  `splices[].id`, unique there), whose `file` is the entry's path, and for which RC14 (a) fails or whose old bytes do
  not occur exactly once at `M`. An entry has at most one resolution per splice.
- `start_M`, `end_M`: the window, as offsets (R6.RECON.29) into the entry's `m` blob, the path's blob in `M`'s tree:
  0-based byte offsets, `start_M` included and `end_M` excluded, the convention of the ledger's byte spans, with
  `0 <= start_M < end_M <=` the blob's length, each at a UTF-8 character boundary of the blob.
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
counted; that the windows of an entry are pairwise disjoint and disjoint from the translated span of every unresolved
splice of the path; and the composed content, that the entry's `l` is `m` with each window replaced by its decoded
bytes and every unresolved splice applied at its translated offset (R6.TREE.12, R6.TREE.13). A failure of the keys,
types, encoding, a hash, the boundaries, disjointness or splice identity is FAIL `record-invalid`; a failure of the
occurrence or of containment fails RC14; a composition that differs fails RC7; in each case the resolution does not
apply and the path stays `base-drift`. **Review confirmation.** Each resolution is the item
`<path>:resolution:<splice>` of the record (R6.RECON.30). The review's verdict entry on it carries `confirms`, `{start_M,
end_M, sha256, resolved_sha256}`, equal to the resolution's, and its verdict `accept` confirms that window and those
replacement bytes: that the window covers every byte `M` changed in the splice's context, and that each byte `M`
changed inside the window is kept in the replacement bytes or that dropping it is justified. A verdict entry without
`confirms`, a `confirms` that differs from the resolution, or no verdict on the item is FAIL `record-invalid`, and the
resolution does not apply.'''

ADAPT2_OLD = ('`splices [{id, file, start, end, old_sha256,\nnew_sha256, new}]` (byte spans at `base`); `files {path: '
              '{base_sha256, expected_sha256}}`;\n`retained [{id, site_ref}]`;')
ADAPT2_NEW = ('`splices [{id, file, start, end, old_sha256,\nnew_sha256, new, raw}]` (byte spans at `base`); `files {path: '
              '{base_sha256, expected_sha256, raw}}`;\n`edits [{id, file, raw}]`, every entry of the edit list in '
              'edit-list order, retained edits included; `retained [{id, site_ref, text}]`, with `text` the bytes of the '
              'retained edit\'s pair selected at `base` (R6.RECON.24 (b)); each `raw` is the ledger\'s or edit list\'s own '
              'entry, unchanged, which R6.RECON.30\'s `ledger_binding` and R6.RECON.26\'s edit-list hashes read, so that '
              'the engine reads nothing outside the interface (R6.CORE.4) %s;' % MARK)

SCHEMA_REF = {'type': 'object', 'additionalProperties': False, 'required': ['path', 'blob_sha256'],
              'properties': {'path': {'$ref': '#/$defs/path'}, 'blob_sha256': {'$ref': '#/$defs/sha256'}}}
RECON_SCHEMA = {
    '$schema': 'https://json-schema.org/draft/2020-12/schema',
    'title': 'oi-reconciliation/2',
    'type': 'object', 'additionalProperties': False,
    'required': ['schema', 'record_id', 'supersedes', 'author', 'M', 'X', 'ledger_base', 'changes_decisions_on_X',
                 'paths'],
    'properties': {
        'schema': {'const': 'oi-reconciliation/2'},
        'record_id': {'type': 'string', 'minLength': 1},
        'supersedes': {'oneOf': [{'$ref': '#/$defs/ref'}, {'type': 'null'}]},
        'author': {'type': 'string', 'minLength': 1},
        'M': {'$ref': '#/$defs/commit'}, 'X': {'$ref': '#/$defs/commit'}, 'ledger_base': {'$ref': '#/$defs/commit'},
        'changes_decisions_on_X': {'type': 'array'},
        'paths': {'type': 'array', 'minItems': 1, 'items': {'$ref': '#/$defs/entry'}}},
    '$defs': {
        'commit': {'type': 'string', 'pattern': '^[0-9a-f]{40}$'},
        'blob': {'type': 'string', 'pattern': '^[0-9a-f]{40}$'},
        'sha256': {'type': 'string', 'pattern': '^[0-9a-f]{64}$'},
        'sha256_or_null': {'oneOf': [{'$ref': '#/$defs/sha256'}, {'type': 'null'}]},
        'offset': {'type': 'integer', 'minimum': 0},
        'path': {'type': 'string', 'pattern': '^(?!\\.{1,2}(/|$))(?!.*/\\.{1,2}(/|$))[^/]+(/[^/]+)*$'},
        'ref': SCHEMA_REF,
        'entry': {
            'type': 'object', 'additionalProperties': False,
            'required': ['path', 'ledger_binding', 'side_change_commits', 'scientific_effect', 'm', 'm_sha256', 'l',
                         'l_sha256', 'x', 'x_sha256', 'splices', 'protected'],
            'properties': {
                'path': {'$ref': '#/$defs/path'},
                'ledger_binding': {
                    'type': 'object', 'additionalProperties': False,
                    'required': ['files_entry_sha256', 'splices_sha256', 'edit_records_sha256'],
                    'properties': {'files_entry_sha256': {'$ref': '#/$defs/sha256_or_null'},
                                   'splices_sha256': {'$ref': '#/$defs/sha256_or_null'},
                                   'edit_records_sha256': {'$ref': '#/$defs/sha256_or_null'}}},
                'side_change_commits': {'type': 'array', 'items': {'$ref': '#/$defs/commit'}},
                'scientific_effect': {'$ref': '#/$defs/scientific_effect'},
                'm': {'$ref': '#/$defs/blob'}, 'm_sha256': {'$ref': '#/$defs/sha256'},
                'l': {'$ref': '#/$defs/blob'}, 'l_sha256': {'$ref': '#/$defs/sha256'},
                'x': {'$ref': '#/$defs/blob'}, 'x_sha256': {'$ref': '#/$defs/sha256'},
                'splices': {'type': 'array', 'items': {'$ref': '#/$defs/splice'}},
                'protected': {'type': 'array', 'items': {'$ref': '#/$defs/protected'}},
                'resolutions': {'type': 'array', 'items': {'$ref': '#/$defs/resolution'}}}},
        'scientific_effect': {
            'type': 'object', 'additionalProperties': False,
            'required': ['conclusions', 'assessment', 'method', 'verdict', 'configuration'],
            'properties': {
                'conclusions': {'oneOf': [{'const': 'none'},
                                          {'type': 'array', 'minItems': 1, 'uniqueItems': True,
                                           'items': {'type': 'string', 'minLength': 1}}]},
                'assessment': {'type': 'string', 'minLength': 1},
                'method': {'type': 'string', 'minLength': 1},
                'verdict': {'enum': ['no-effect', 'invalidates']},
                'configuration': {'$ref': '#/$defs/ref'},
                'invalidated': {'type': 'array', 'minItems': 1, 'items': {'$ref': '#/$defs/invalidated'}}},
            'if': {'properties': {'verdict': {'const': 'invalidates'}}},
            'then': {'required': ['invalidated']},
            'else': {'not': {'required': ['invalidated']}}},
        'invalidated': {
            'type': 'object', 'additionalProperties': False, 'required': ['id', 'sha256', 'target'],
            'properties': {
                'id': {'type': 'string', 'minLength': 1}, 'sha256': {'$ref': '#/$defs/sha256'},
                'target': {'type': 'object', 'additionalProperties': False,
                           'required': ['path', 'start_H', 'old_sha256'],
                           'properties': {'path': {'$ref': '#/$defs/path'}, 'start_H': {'$ref': '#/$defs/offset'},
                                          'old_sha256': {'$ref': '#/$defs/sha256'}}}}},
        'splice': {
            'type': 'object', 'additionalProperties': False,
            'required': ['id', 'start_H', 'end_H', 'start_M', 'end_M', 'new_sha256', 'translation'],
            'properties': {
                'id': {'type': 'string', 'minLength': 1},
                'start_H': {'$ref': '#/$defs/offset'}, 'end_H': {'$ref': '#/$defs/offset'},
                'start_M': {'$ref': '#/$defs/offset'}, 'end_M': {'$ref': '#/$defs/offset'},
                'new_sha256': {'$ref': '#/$defs/sha256'},
                'translation': {'oneOf': [{'const': 'identity'}, {'type': 'integer'}]}}},
        'protected': {
            'type': 'object', 'additionalProperties': False, 'required': ['start_M', 'end_M', 'sha256'],
            'properties': {'start_M': {'$ref': '#/$defs/offset'}, 'end_M': {'$ref': '#/$defs/offset'},
                           'sha256': {'$ref': '#/$defs/sha256'}}},
        'resolution': {
            'type': 'object', 'additionalProperties': False,
            'required': ['splice', 'start_M', 'end_M', 'sha256', 'resolved', 'resolved_sha256'],
            'properties': {
                'splice': {'type': 'string', 'minLength': 1},
                'start_M': {'$ref': '#/$defs/offset'}, 'end_M': {'$ref': '#/$defs/offset'},
                'sha256': {'$ref': '#/$defs/sha256'},
                'resolved': {'type': 'string',
                             'pattern': '^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$'},
                'resolved_sha256': {'$ref': '#/$defs/sha256'}}}}}
# the keys of the R6.RECON.30 table, which the schema must name exactly (self-check)
TABLE_TOP = ['schema', 'record_id', 'supersedes', 'author', 'M', 'X', 'ledger_base', 'changes_decisions_on_X', 'paths']
TABLE_ENTRY = ['path', 'ledger_binding', 'side_change_commits', 'scientific_effect', 'm', 'm_sha256', 'l', 'l_sha256',
               'x', 'x_sha256', 'splices', 'protected', 'resolutions']

R29 = '''
### 23.1 Schema contract of the reconciliation record kinds

**R6.RECON.29** **Common encodings and malformed input** %(mark)s. This requirement and R6.RECON.30
to R6.RECON.36 state, for the record kinds of the reconciliation route (reconciliation, review, reassessment, edit-id
migration and side-change class records), for the configuration's references to them and for the result fields of the
route, the field names, types, encodings, data sources, identity bindings, item ids, review requirements and
mechanical acceptance conditions that the requirements they cite state by meaning (owner decision of 2026-11-26, #1169
comment 7189470338, item 4; schema completeness audit, PR #1593 comment 7189621405). Where they give a key, type or
encoding, they govern.

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
| canonical JSON | the bytes that Python's `json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False)` produces, encoded as UTF-8: keys sorted by code point, no whitespace, non-ASCII characters written as themselves; a hashed value holds no number other than an integer. The canonical sha256 of a value is the sha256 of these bytes (R6.RECON.5, R6.RECON.25, R6.RECON.26, R6.RECON.27) |
| strict parse | the record's bytes are UTF-8 without a byte-order mark and hold one JSON value, an object; a duplicate key in any object, or `NaN`, `Infinity` or `-Infinity`, is a parse failure |

Each record kind of R6.RECON.30 to R6.RECON.34 has a key table. A record fails its schema when a required key is
missing, a value has another type or encoding, a key appears that its table does not list, or it fails strict
parsing. A schema failure of a record a run reads is FAIL `record-invalid`, decided before any condition RC1-RC14 is
evaluated, and the record does not apply: a malformed field is never reported only as a failed condition, and the path
the record would cover stays `base-drift` (R6.TREE.7). A schema failure never loses a finding (R6.RECON.26, Form of a
finding (i)).
Sources: PR #1593 comment 7189621405 (A, ledger_binding; ranked items 2, 3 and 10). Controls: RECON-SCHEMA, CANON-JSON.

**R6.RECON.30** **`oi-reconciliation/2`: fields, item ids and acceptance** %(mark)s. The fields that
R6.RECON.1 names by meaning are:

| Key | Type | Source and binding | Acceptance |
|---|---|---|---|
| `schema` | `"oi-reconciliation/2"` | | a record of schema `oi-reconciliation/1` that a run reads is FAIL `record-invalid` and never applies; the scans of R6.RECON.2 (d) and R6.RECON.26 include `/1` files |
| `record_id` | non-empty string | the record's lineage (R6.REC.7) | required on every reconciliation record |
| `supersedes` | reference or null | R6.REC.7 | |
| `author` | identity string | the writer (R6.REC.2) | |
| `M`, `X` | commit id | the run's `M` and `X` | equal, as strings, to the run's full ids |
| `ledger_base` | commit id | `roles.scientific_base` | equals `H` (RC13, R6.RECON.5) |
| `changes_decisions_on_X` | array | R6.RECON.3 | required; RC12 holds only for `[]` |
| `paths` | non-empty array of entries | the paths the record covers | each entry's `path` occurs once |
| entry `path` | path | a ledgered or corpus path that differs between `H` and `M` | |
| entry `ledger_binding` | `{files_entry_sha256, splices_sha256, edit_records_sha256}`, each a sha256 or null | the canonical sha256 of exactly one value each, read through the ledger interface (R6.ADAPT.2): the path's raw `files` entry; the list of the path's raw splices, in ledger order; the list of the raw edit-list entries whose `file` is the path, in edit-list order | RC13 (R6.RECON.5); all three null for a corpus path the ledger does not list |
| entry `side_change_commits` | array of commit ids | the commits on `M`'s first-parent chain after `H` that change the path, oldest first | RC1 |
| entry `scientific_effect` | object, below | R6.RECON.25 | |
| entry `m`, `m_sha256` | blob id, sha256 | the path's blob at `M` | RC2 |
| entry `l`, `l_sha256` | blob id, sha256 | the composed blob (R6.TREE.12, R6.RECON.19) | RC7 |
| entry `x`, `x_sha256` | blob id, sha256 | the path's blob at `X` | RC8 |
| entry `splices` | array of `{id, start_H, end_H, start_M, end_M, new_sha256, translation}` | one element for each splice of the path in the ledger, in ledger order: `id` the splice id; `start_H` and `end_H` its offsets at `H`; `start_M` its translated offset at `M`, and `end_M` equal to `start_M + end_H - start_H`; `new_sha256` the sha256 of its new bytes; `translation` `"identity"` when `start_M` equals `start_H`, otherwise the integer `start_M - start_H` | RC4 to RC6; RC5 also checks `translation` against the offsets |
| entry `protected` | array of `{start_M, end_M, sha256}` | the protected ranges at `M` | RC9 |
| entry `resolutions` | array (R6.RECON.24); optional, absent meaning `[]` | the explicit resolutions | R6.RECON.24 |

`scientific_effect` is `{conclusions, assessment, method, verdict, configuration}`, with `invalidated` present exactly
when `verdict` is `"invalidates"`: `conclusions` is the string `"none"` or a non-empty array of distinct edit ids;
`assessment` and `method` are non-empty strings; `verdict` is `"no-effect"` or `"invalidates"`; `configuration` is the
reference of the configuration under which the entry was assessed (R6.RECON.26 (iii)); `invalidated` is a non-empty
array of the elements of R6.RECON.26 (ii). The edit ids of `conclusions` and `invalidated` are checked against the edit
list of the configuration that `configuration` names, not the run's, so a revised plan that removes an edit does not
turn an earlier entry into a form failure. A path is executed by a check when its name ends in `.py`, `.lean`, `.yml`,
`.yaml` or `.sh`, or when a delegation class of the configuration covers it (sec. 13); for such an entry `method`
contains the entry's `l` blob id in full, or the record fails its schema; that the check was re-run, and its result,
rest on the review.

"Changes the path" means, for RC1 and for drift alike (R6.RECON.22), that the path's tree entry (mode and object id,
absence counted as an entry) in the commit differs from that in its first parent; a change of mode alone is therefore a
drift, and its commit is listed. A path absent at `M` or at `X` has no blob there: RC2 or RC8 fails, and the path stays
`base-drift`. `x` is read at `X`; R6.RECON.21's binding reads it at `X`, which is `C` in RT-L2.

The record's item ids are, for each entry, `<path>`, `<path>:scientific_effect` and, for each resolution,
`<path>:resolution:<splice id>`. The verdict `accept` on `<path>` confirms that the reviewer re-derived from the object
store the entry's `side_change_commits`, `ledger_binding`, blob ids and sha256 values, splice offsets and translations
and protected ranges, and the record's `M`, `X`, `ledger_base` and `changes_decisions_on_X` as they bear on the path;
on `<path>:scientific_effect` it confirms what R6.RECON.25 states, and on a resolution item what R6.RECON.24 states.

The JSON Schema below (draft 2020-12) is the machine form of the key table. The tool checks beside it what the schema
cannot state: the integer form of offsets in the record's text, unique paths, `end_M`, the `translation` value, the
edit ids against the ledger and the executed-path rule.

```json
%(schema)s
```
Sources: PR #1593 comment 7189621405 (A; ranked items 3, 4, 8, 9 and 10). Controls: RECON-SCHEMA, RECON-FIELDS.

**R6.RECON.31** **`oi-review-record/1`: fields, item ids and widening** %(mark)s.

| Key | Type | Acceptance |
|---|---|---|
| `schema` | `"oi-review-record/1"` | |
| `kind` | `"review"` or `"widening"`; optional, absent meaning `"review"` | |
| `reviewer` | identity string | not equal to the reviewed record's `author` (R6.RECON.29); for a widening review, also not equal to the reviewer of the superseding record's own review (R6.REC.13) |
| `reviewed` | reference | its `path` and `blob_sha256` both equal those of the reviewed record, in record lint, in the post-freeze route and in the scans of R6.RECON.26 alike |
| `replaces` | reference; present exactly when `kind` is `"widening"` | the superseded record (R6.REC.13) |
| `method` | non-empty string | contains at least one full 40-character object id that the reviewer read |
| `verdicts` | array of `{item, verdict, reason}`, with `invalidated` and `configuration` (R6.RECON.26) and `confirms` (R6.RECON.24) where those requirements admit them | `item` one of the reviewed record's item ids; `verdict` one of `accept`, `reject`, `dissent`, `invalidates`; `reason` a string, non-empty for a verdict other than `accept`; no other key |
| `dissent` | string; optional | |

Item ids, by the kind of the reviewed record:

| Reviewed kind | Item ids |
|---|---|
| `oi-reconciliation/2` | as R6.RECON.30 states |
| `oi-reassessment/1` | `finding`, `repair`, `edit`, `rederivation`, `verdict` |
| `oi-edit-id-migration/1` | `migration:<old>` for each element of `migrations`, and `approval` |
| `oi-side-change-classes/1` | the `id` of each element of `classes` |
| `oi-term-rules/2` | the `id` of each element of `rules` |
| `oi-hp-adjudication/1`, `oi-context-adjudication/1` | the `id` of each element of `entries` |
| `oi-hit-classification/1` | the `id` of each element of `classifications` |
| a kind without an item list (`oi-scope/1`, `oi-delegation/1`) and the configuration | the single item `record_id`, for the configuration `config_id` |

A review whose `item` values are not exactly these ids fails record lint (R6.REC.6). A widening review covers the items
of the difference between the superseding record (`reviewed`) and the superseded one (`replaces`): for a kind with an
item list, the id of each element added, removed or changed (elements matched by id), and `field:<key>` for each other
top-level key whose value differs, `supersedes`, `version` and the item list excluded; for the configuration,
`field:<key>` for each top-level key whose value differs. The configuration's widening review is a review record of
kind `"widening"` listed in `records` with kind `review` (R6.RECON.33); the configuration has no `widening_review` key,
and one is an unknown field (R6.VALID.2).
Sources: PR #1593 comment 7189621405 (B; ranked item 5). Controls: REVIEW-SCHEMA, WIDENING-ITEMS.

**R6.RECON.32** **`oi-reassessment/1` and `oi-edit-id-migration/1`: fields and location** %(mark)s.

| Kind | Key | Type and meaning |
|---|---|---|
| both | `schema` | `"oi-reassessment/1"` or `"oi-edit-id-migration/1"` |
| both | `record_id` | non-empty string, required |
| both | `supersedes` | reference or null (R6.REC.7) |
| both | `author` | identity string |
| reassessment | `finding` | `{path, blob_sha256, item}` (R6.RECON.27, Keys) |
| reassessment | `repair` | `{commits, entry: {path, blob_sha256, entry_path}}` (R6.RECON.27, Keys) |
| reassessment | `edit` | `{id, sha256}`, or null for a finding bound at run level (R6.RECON.27, Keys) |
| reassessment | `rederivation` | non-empty string: the edit's justification re-derived at the repaired state, stating what was re-run; that the re-run happened rests on the review |
| reassessment | `verdict` | `"no-effect"` |
| migration | `migrations` | non-empty array of `{old, new}`, each a non-empty edit-id string |
| migration | `approval` | `{quote, author, time}`: the owner's words, login (identity string) and time (R6.RECON.29); checked for form only (R6.REC.3) |

Both kinds lie, with their review records, in the plan's record directory (`D_rec`, R6.RDIR.1) of the configuration
that references them, and are read by their reference; a referenced record outside it is FAIL `record-invalid`. The
migrations a run applies are the transitive closure over every migration record that the configuration, or a
configuration on its `supersedes` chain, references; an `old` mapped to two different `new` ids, or a cycle, fails
each record involved.
Sources: PR #1593 comment 7189621405 (C, G). Controls: REASSESS-KEYS, MIGRATION-RECORD.

**R6.RECON.33** **Configuration references** %(mark)s. The kinds of `records` (R6.CFG.4) and the schema
each requires:

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
the number of the accountable Issue; two configurations name the same retirement when their names are equal strings or
their issues are equal integers. **Resolution of a reference.** A reference "at or before `F`" (R6.REC.7, R6.CFG.3) is
resolved by walking `F`'s first-parent chain from `F` towards the root: it resolves at the newest commit whose tree
holds the path with a blob of that sha256. Every configuration version lives at the same path (R6.CFG.1), so a
predecessor configuration is found at an older commit. A reference that no commit on that chain holds names no record
(R6.REC.7: FAIL `record-invalid`; for a configuration, ERROR `CONFIG_INVALID`). The same search resolves the
configurations and records that R6.RECON.26 (iii), R6.RECON.27 and R6.RECON.28 name. **Lineage direction.** A
configuration is in the plan lineage of a finding when the finding's configuration lies on its `supersedes` chain, the
configuration itself included, or when it names the same retirement. **Unknown keys.** A key that R6.CFG.4 does not
list, at the top level or inside a member whose keys it lists, such as a check's `default_for` or a top-level
`widening_review`, is an unknown field: ERROR `CONFIG_INVALID` (R6.VALID.2). A run of op B or op D names its plan check
(sec. 7), so no default check is defined.
Sources: PR #1593 comment 7189621405 (D; ranked items 1 and 7). Controls: CONFIG-REFS, SUPERSEDES-RESOLVE.

**R6.RECON.34** **Side-change class records** %(mark)s.

| Key | Type and meaning |
|---|---|
| `schema` | `"oi-side-change-classes/1"` |
| `record_id`, `supersedes`, `author` | as R6.RECON.30 |
| `classes` | non-empty array of `{id, prefixes, pins}`: `id` a non-empty string, defined once (R6.TREE.5); `prefixes` an array of paths, a path lying under a prefix when it begins with the prefix followed by `/`; `pins` an array of `{path, git_blob, blob_sha256}`, a blob id and a sha256, both required |

A class-level `paths` list is not a form of this record. A superseding class record that adds a pin or a prefix, or
changes a pin's blob, widens the record it supersedes and needs a widening review (R6.REC.13), as a changed class widens
the configuration (R6.CFG.7).
Sources: PR #1593 comment 7189621405 (E). Controls: CLASS-SCHEMA.

**R6.RECON.35** **The scanned sets: selection, parsing and identity** %(mark)s. The scans of R6.RECON.2
(d) and R6.RECON.26 select every regular file under `verification/audits/`, outside every prefix of the tool-landing
class and outside the plan's record directory, whose content begins with `{`, after an optional byte-order mark and
whitespace, whatever its name: no file name or suffix is required. Each selected file is parsed strictly
(R6.RECON.29). A file that parses and whose `schema` is `oi-reconciliation/1`, `oi-reconciliation/2` or
`oi-review-record/1` is in the scanned set. A selected file that fails to parse, or whose `schema` is not a string, and
whose bytes contain one of those schema ids, is in the scanned set as a malformed record: FAIL `record-invalid`, and,
where its bytes also contain `invalidates` or `invalidated`, a malformed finding, which binds at run level
(R6.RECON.26, Form of a finding (iv)). Record identity is the reference (R6.RECON.29): two byte-identical files at two
paths are two records, for R6.RECON.2 (e) and for findings alike. The review records of a reconciliation record lie in
its directory (R6.RECON.1, R6.RECON.2 (d)), and a review elsewhere is not its review for record lint; for finding
detection the scans read review records wherever they lie in the scanned sets, and one elsewhere that carries a
finding counts, as a form failure (R6.RECON.26, Form of a finding (i)).
Sources: PR #1593 comment 7189621405 (F; ranked item 6). Controls: SCAN-PARSE.

**R6.RECON.36** **Result fields of the reconciliation route** %(mark)s. An op C result with `M` carries:
- `dispositions`: one entry for each drifted ledgered or corpus path (R6.RECON.22), `{path, disposition, category,
  record, failed, conflicts, why}`: `disposition` one of `reconciled`, `reconciled-resolved`, `base-drift` and
  `retirement-blocked`; `category` 1, 2 or 3 where R6.RECON.22 assigns one, otherwise null; `record` the reference of
  the record whose entry for the path applies, or null; `failed` an array of condition names (`RC1` to `RC14`,
  `reconciled-state`, `no-record`); `conflicts` an array of splice and site ids; `why` a string, a diagnostic;
- `category3`: `{findings, blocked, reassessments}`: `findings` `[{record, item}]`, with `record` a reference and
  `item` as R6.RECON.27's `finding.item`; `blocked` `[{record, item, edit}]`, `edit` null for a run-level binding;
  `reassessments` the references of the applying reassessments;
- `inputs.classify_records` `[{rev, path, sha256, review: {path, sha256}}]` and `inputs.record_base`, a commit id or
  null (R6.RECON.2 (c)).

R6.OUT.18 lists these fields, and the result's JSON Schema file carries them.
Sources: PR #1593 comment 7189621405 (A, dispositions; H). Controls: RESULT-FIELDS.
'''

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
    ('RECON-BLOCK', ('expect', 'cases', 14), MISSING, RECON_BLOCK_ADDED),
    ('S11-2a', ('expect', 'sites', 0, 'added_relative_to_unmutated'), MISSING,
     {'items[class=unclassified,subject=$new_line]': 1}),
    ('RTL2-BIND', ('expect', 'cases', 6, 'case'), RTL2_OLD, RTL2_NEW),
    ('RT-D', ('direction', 'why'), RT_D_WHY_OLD, RT_D_WHY_NEW),
    ('RT-D', ('expect', 'sites', 1, 'classes_exact'), MISSING, ['unclassified']),
    ('RT-D', ('flags', 6), MISSING, RT_D_FLAG),
    ('RT-DR', ('expect', 'cases', 3, 'case'), RT_DR_OLD, RT_DR_NEW),
]
# amendment 5 r2's own strengthenings, pinned so that no later edit reverts them (delta review nit 4)
PINS = [
    ('L2', ('expect', 'counts', 'lines[rule=W2,state=PASS]'), 4),
    ('L2', ('expect', 'invariants', 0, 'all'), 'lines[rule=W2]'),
    ('V7a', ('expect', 'invariants', 0, 'items_include', 0, 'subject'), '$planted'),
    ('V23', ('expect', 'invariants', 1, 'items_include', 0, 'subject'), '$planted'),
    ('V24', ('expect', 'invariants', 1, 'items_include', 0, 'subject'), '$planted'),
    ('R18', ('expect', 'sites', 0, 'decision'), 'REVIEW_REQUIRED'),
    ('RT-D', ('expect', 'counts', 'lines[state=PASS,rule=W1|W2]'), 10),
    ('RT-D', ('expect', 'classes_exact'), ['unclassified']),
    ('RT-D', ('expect', 'sites', 1, 'subject'), 'papers/SM.md:1394'),
    ('RT-DR', ('expect', 'cases', 0, 'invariants', 0, 'items_include', 2, 'file'), 'book/ch09-universality.md'),
    ('RT-DR', ('expect', 'cases', 3, 'invariants', 0, 'none'),
     'items[rule_id=DR-1,file=book/The-Incompleteness-of-Observation-FULL.md,line=6504]'),
    ('RTL2-BIND', ('expect', 'cases', 6, 'invariants', 1, 'items_include', 0, 'subject'), '$planted'),
    ('S11-2a', ('expect', 'classes_include'), ['unclassified', 'deny-match']),
    ('U14', ('expect', 'cases', 1, 'sites', 0, 'classes_exact'), ['provenance-mismatch']),
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
    ('A.9', '`splices[]`', 'R6.RECON.30: keys, `end_M`, `translation` checked by RC5; R6.RECON.29 offsets; tool behaviour (float, boolean, missing offsets) contradicts the design; RECON-SCHEMA'),
    ('A.10', 'protected ranges', 'R6.RECON.30 `protected`; malformed is `record-invalid`; RECON-SCHEMA'),
    ('A.11', '`scientific_effect.conclusions`', 'R6.RECON.30: `"none"` or an array, checked against the configuration in (iii); RECON-FIELDS'),
    ('A.12', '`assessment`, `method`, `verdict`; executed paths', 'R6.RECON.30: types; executed-path predicate and `method` contains `l` (owner choice); RECON-FIELDS'),
    ('A.13', '`scientific_effect.configuration`', 'R6.RECON.30; resolved by R6.RECON.33\'s search'),
    ('A.14', 'record item ids', 'R6.RECON.30 item ids and what `accept` on `<path>` confirms; REVIEW-SCHEMA'),
    ('A.15', 'field malformation in general', 'R6.RECON.29: schema failure is `record-invalid` before any RC; JSON Schema in R6.RECON.30; RECON-SCHEMA'),
    ('A.16', 'schema `oi-reconciliation/1`', 'R6.RECON.30: retired, `record-invalid` when read, still scanned; RECON-SCHEMA'),
    ('A.17', 'dispositions in the result', 'R6.RECON.36, R6.OUT.18; RESULT-FIELDS'),
    ('B.1', '`verdicts[]` entry keys', 'R6.RECON.31: `{item, verdict, reason}` plus the admitted keys; REVIEW-SCHEMA'),
    ('B.2', '`reviewed`', 'R6.RECON.31: path and blob both match, one rule everywhere; REVIEW-SCHEMA'),
    ('B.3', '`reviewer` / `author`', 'R6.RECON.29 identity string (trim, case-fold); FINDING-FORM independence countercase'),
    ('B.4', '`method`', 'R6.RECON.31: contains a full object id (owner choice); REVIEW-SCHEMA'),
    ('B.5', 'widening review', 'R6.RECON.31: `kind`, `replaces`, `field:<key>` and element-id items; `widening_review` is an unknown configuration field; WIDENING-ITEMS'),
    ('B.6', 'item ids of every kind', 'R6.RECON.31 item-id table; REVIEW-SCHEMA'),
    ('C.1', '`rederivation`', 'R6.RECON.32: a non-empty string (owner choice); REASSESS-KEYS'),
    ('C.2', 'reassessment item ids', 'R6.RECON.31: `finding`, `repair`, `edit`, `rederivation`, `verdict`'),
    ('C.3', 'reassessment location', 'R6.RECON.32: the plan\'s record directory of the citing configuration (owner choice)'),
    ('D.1', '`records[].kind`', 'R6.RECON.33 enumeration and schema map; unknown or mismatched kind is ERROR `CONFIG_INVALID`; tool behaviour (skipping) contradicts R6.VALID.3; CONFIG-REFS'),
    ('D.2', '`roles.side_change_classes` and `records`', 'R6.RECON.33: also listed in `records` with the same blob; CONFIG-REFS'),
    ('D.3', '`retirement`', 'R6.RECON.33: `{name, issue}`, matched by equal name or issue; CONFIG-REFS'),
    ('D.4', 'supersedes resolution at or before `F`', 'R6.RECON.33: walk `F`\'s first-parent chain to the root (owner choice: the audit proposed back to `H`); SUPERSEDES-RESOLVE'),
    ('D.5', 'direction of "reachable through `supersedes`"', 'R6.RECON.33 and R6.RECON.26 (iii): the finding\'s configuration lies on the run configuration\'s chain'),
    ('D.6', '`checks[].default_for`', 'R6.RECON.33: an unknown field (R6.VALID.2), no default check; CONFIG-REFS'),
    ('E.1', 'class record keys', 'R6.RECON.34: `classes[{id, prefixes, pins[{path, git_blob, blob_sha256}]}]`, both hashes required, no `paths` form; CLASS-SCHEMA'),
    ('E.2', 'class record widening', 'R6.RECON.34: an added pin or prefix or changed blob needs a widening review (owner choice); CLASS-SCHEMA'),
    ('F.1', 'file selection', 'R6.RECON.35: no suffix filter; tool behaviour (`.json` filter) contradicts the design; SCAN-PARSE'),
    ('F.2', 'parse failure', 'R6.RECON.35 and R6.RECON.29 strict parse; a malformed record is `record-invalid`, a malformed finding blocks at run level; SCAN-PARSE'),
    ('F.3', 'record identity across copies', 'R6.RECON.29 and R6.RECON.35: identity is the reference; SCAN-PARSE'),
    ('F.4', 'first-kind finding review location', 'R6.RECON.35: same directory for lint; anywhere for detection; SCAN-PARSE, REVIEW-SCHEMA'),
    ('G.1', '`migrations[]` and chaining', 'R6.RECON.32 and R6.RECON.28: `{old, new}` strings, transitive closure; MIGRATION-RECORD'),
    ('G.2', '`approval`', 'R6.RECON.32: `{quote, author, time}`, time as R6.RECON.29, form only; MIGRATION-RECORD'),
    ('G.3', 'migration item ids and location', 'R6.RECON.31 (`migration:<old>`, `approval`) and R6.RECON.32 (plan\'s record directory)'),
    ('G.4', 'R6.CORE.5 allowlist', 'Tool change listed below: `oi-reassessment/1` and `oi-edit-id-migration/1` join the schema list; R6.CORE.5\'s list is illustrative ("among them"), so the text is not edited'),
    ('H.1', '`inputs.classify_records`', 'R6.OUT.18 and R6.RECON.36: `review: {path, sha256}`; RESULT-FIELDS'),
    ('H.2', '`inputs.record_base` and `category3`', 'R6.OUT.18 and R6.RECON.36; RESULT-FIELDS'),
]
AUDIT_LABELS = (['A.%d' % i for i in range(1, 18)] + ['B.%d' % i for i in range(1, 7)] + ['C.1', 'C.2', 'C.3']
                + ['D.%d' % i for i in range(1, 7)] + ['E.1', 'E.2'] + ['F.%d' % i for i in range(1, 5)]
                + ['G.%d' % i for i in range(1, 5)] + ['H.1', 'H.2'])
RANKED_MAP = [
    ('1', 'D.4, D.5'), ('2', 'A.6, FINDING-KEYS retained-edit case, R6.ADAPT.2 `edits`'), ('3', 'A.5, A.9, A.15'),
    ('4', 'A.11'), ('5', 'A.14, B.5, B.6'), ('6', 'F.1 to F.3'), ('7', 'D.1, D.2'), ('8', 'A.2'), ('9', 'A.7, A.8'),
    ('10', 'A.9, A.10, A.12'), ('11', 'B.3, D.3, C.1, C.3, G.3, H.1, H.2, D.6, E.1, G.4'),
]

OWNER_CHOICES = [
    'Points 1 to 4 as proposed (the value `invalidates`; lineage from `configuration` with the global target match; '
    'the `oi-edit-id-migration/1` record; the `invalidated` element).',
    'Review finding 6: no narrowing superseding finding; the remedy for an id collision is a rename.',
    'Review finding 7 (c): only referenced migration records apply.',
    'Item B1: reading (b), with `text` in the ledger interface\'s `retained` entry.',
    'Item B2: 0-based, end-exclusive byte offsets at UTF-8 character boundaries; base64 for `resolved`; `confirms` on '
    'the review item; a resolution of a splice without a conflict is `record-invalid`; `resolutions` optional.',
    '`record_id` required on reconciliation, reassessment, migration and class records.',
    'Canonical JSON as Python\'s `json.dumps(..., sort_keys=True, separators=(\',\', \':\'), ensure_ascii=False)`.',
    'Identity strings compared after trimming and Unicode case folding.',
    'A review\'s `method` contains a full object id (a mechanical check rather than review-only).',
    'The executed-path predicate (suffixes `.py`, `.lean`, `.yml`, `.yaml`, `.sh`, or delegation-class coverage) and '
    '`method` containing the `l` blob id.',
    '`x` read at `X`; R6.RECON.21 reads `X`, which is `C` in RT-L2.',
    '"Changes the path" by tree entry (mode and object id); a mode-only change drifts; a deletion stays `base-drift`.',
    '`oi-reconciliation/1` retired: `record-invalid` when read, still scanned.',
    'Review-record `kind` optional (absent meaning `review`); widening items `field:<key>` and element ids.',
    '`rederivation` a non-empty string.',
    'Reassessment and migration records in the citing configuration\'s record directory.',
    'The names of the `records` kinds (R6.RECON.33).',
    'Supersedes resolution along `F`\'s whole first-parent chain (the audit proposed stopping at `H`).',
    '`retirement` as `{name, issue}` with an integer issue.',
    '`default_for` and `widening_review` treated as unknown fields, with no default check.',
    'Widening review for a class record that adds a pin or prefix or changes a blob.',
    'Scanned-set selection by a leading `{` (no suffix), and the malformed-record rule.',
    'The `dispositions` and `category3` keys; `category` null where R6.RECON.22 assigns none.',
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
            'R6.RECON.29 to R6.RECON.36). Each resolution is a proposal for the owner\'s decision at adoption '
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
    # R6.RECON.26: detection before lint; the global target match
    t = once(t, "or a non-author review record (passing record lint) whose verdict",
             "or a non-author review record (detected before review-record lint, Form of a finding (i) below) whose "
             "verdict", 'R6.RECON.26 detection')
    t = once(t, "whose ledger holds the edit's id, an id the edit was renamed to under a migration recorded under AGENTS.md\n"
                "sec. A.48 item 3, or an edit of the same path whose old bytes hash to the recorded `old_sha256`, "
                "whatever its\noffset (so a renumbering on a new `H` is still matched).",
             "whose ledger holds the edit's id or an id the edit was renamed to under a migration recorded under AGENTS.md\n"
             "sec. A.48 item 3; and any configuration, whatever its lineage or retirement (Form of a finding (v) "
             "below), whose ledger holds an edit of the same path whose old bytes hash to the recorded `old_sha256`, "
             "whatever its\noffset (so a renumbering on a new `H` is still matched).", 'R6.RECON.26 match scope')
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
    a = t.index('**R6.RECON.27** **Reassessment of an invalidated edit**')
    b = t.index('\nSources: amendment 4 (#1169 comment 7185562871). Controls: BLOCK-KEY, REASSESS-FORM.', a)
    t = t[:b] + KEYS27 % {'mark': MARK} + t[b:]
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
    # the new requirements
    t = once(t, "\n***\n\n## 24. Engine, purity scope (Z9), generality",
             NEW_REQ28 % {'mark': MARK}
             + R29 % {'mark': MARK, 'schema': json.dumps(RECON_SCHEMA, indent=1, ensure_ascii=False)}
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
        new.append({'id': rid, 'section': 'RECON', 'section_number': 23, 'kind': 'testable',
                    'sources': sources.get(rid, ['#1169 comment 7189470338', 'PR #1593 comment 7189621405']),
                    'controls': list(REQ_CONTROLS[rid]), 'verification': ['controls', 'review'], 'open': [],
                    'pending_owner_confirmation': [PENDING], 'owner_decision': []})
    return R[:i + 1] + new + R[i + 1:]


def vocabulary(t):
    a = t.index('### 16.10 Annex: invariant vocabulary')
    b = t.index('***', a)
    return set(re.findall(r'`([A-Za-z_0-9]+)`', t[t.index('\n\n', t.index('A key outside it', a)):b]))


def block_of(t, rid):
    start = t.index('**%s**' % rid)
    nxt = re.compile(r'\n(?:\*\*R6\.|\*\*\*|#)').search(t, start + 1)
    return t[start:nxt.start() if nxt else len(t)]


def schema_keys(t):
    a = t.index('**R6.RECON.30**')
    b = t.index('```json\n', a)
    e = t.index('\n```', b + 8)
    return json.loads(t[b + 8:e])


def self_checks(E0, E, R0, R, t, base_texts):
    problems = []
    r0 = {r['id']: r for r in E0['rows']}
    r1 = {r['id']: r for r in E['rows']}
    reqs = {q['id']: q for q in R}
    declared = {}
    for rid, path, old, new in DECLARED_DIFFS:
        declared.setdefault(rid, []).append((path, old, new))
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
        if rid not in REQ_CONTROLS:
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
    if [q['id'] for q in R if q['id'] not in {x['id'] for x in R0}] != NEW_REQS:
        problems.append('new requirements differ from NEW_REQS')
    # the JSON Schema of R6.RECON.30 parses and names exactly the keys of its table
    s = schema_keys(t)
    if sorted(s['properties']) != sorted(TABLE_TOP) or sorted(s['required']) != sorted(TABLE_TOP):
        problems.append('R6.RECON.30 schema: top-level keys differ from the table')
    ent = s['$defs']['entry']
    if sorted(ent['properties']) != sorted(TABLE_ENTRY) or sorted(ent['required']) != sorted(
            k for k in TABLE_ENTRY if k != 'resolutions'):
        problems.append('R6.RECON.30 schema: entry keys differ from the table')
    blk = block_of(t, 'R6.RECON.30')
    for k in TABLE_TOP + TABLE_ENTRY:
        if '`%s`' % k not in blk:
            problems.append('R6.RECON.30 table does not name %s' % k)
    res = s['$defs']['resolution']
    if sorted(res['required']) != sorted(['splice', 'start_M', 'end_M', 'sha256', 'resolved', 'resolved_sha256']):
        problems.append('resolution schema keys')
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
    if [x[0] for x in NITS_MAP] != ['1', '2', '3', '4', '5']:
        problems.append('amendment 5 nit map incomplete')
    if [x[0] for x in B_MAP] != ['B1', 'B2']:
        problems.append('item B map incomplete')
    return problems


def change_record(owner, outs, gen_sha, owner_sha):
    lines = ['# r6 amendment 6: change record', '',
             'Owner directions, quoted in DESIGN-r6.md sec. 0.7: %s. Generated by generator-amendment6/amend6.py '
             '(sha256 %s) from the amendment-5 outputs (amendment 5 r2, e0706a4b) and '
             'generator-amendment6/owner-decisions-amendment6.json (sha256 %s). This is r2: it answers the independent '
             'review of the first draft (PR #1593 comment 7189446310), resolves items B1 and B2, and folds in the '
             'owner\'s schema completeness audit (PR #1593 comment 7189621405). Every resolution is a proposal; the '
             'choice is the owner\'s at adoption. It is kept separate from amendment 5.'
             % ('; '.join('%s, %s (%s), %s' % (d['author'], d['time'], d['record'], d['item'])
                          for d in owner['decisions']), gen_sha, owner_sha), '',
             'Safety rule for every point: no reading may let a category-3 finding be lost or lifted by rewording, and '
             'no rule is weakened to match the tool. The owner\'s lifecycle holds: the block persists for the frozen '
             'plan, a repair does not validate, and a revised plan may proceed (by removing the edit, or by citing an '
             'applying reassessment for each finding).', '',
             '## 1. The tool writer\'s points 1 to 5', '']
    for title, opts, rec, ctl in POINTS:
        lines += ['### ' + title, '', 'Options:', ''] + ['- ' + o for o in opts] + ['', rec, '',
                                                                                      'Controls: %s.' % ctl, '']
    lines += ['## 2. Review findings (PR #1593 comment 7189446310)', '', '| Finding | Disposition |', '|---|---|']
    lines += ['| %s | %s |' % (k, v) for k, v in REVIEW_MAP] + ['']
    lines += ['## 2a. Amendment 5 nits (delta review, PR #1592 comment 7189385508; routed here by the owner, #1169 '
              'comment 7189915409)', '', '| Nit | Disposition |', '|---|---|']
    lines += ['| %s | %s |' % (k, v) for k, v in NITS_MAP] + ['']
    lines += ['## 3. Items B (tool writer)', '']
    for k, title, opts, rec in B_MAP:
        lines += ['### %s. %s' % (k, title), '', 'Options:', ''] + ['- ' + o for o in opts] + ['', rec, '']
    lines += ['## 4. Schema completeness audit (PR #1593 comment 7189621405)', '',
              'Rows are labelled by the audit\'s section and their order in it.', '',
              '| Row | Field | Disposition |', '|---|---|---|']
    lines += ['| %s | %s | %s |' % x for x in AUDIT_MAP] + ['', 'Ranked gaps:', '', '| Rank | Covered by |', '|---|---|']
    lines += ['| %s | %s |' % x for x in RANKED_MAP] + ['']
    lines += ['Where the tool accepts input the design refuses, the design rule is stated and a countercontrol row is '
              'added: a missing or empty `changes_decisions_on_X` (RECON-SCHEMA), float, boolean or missing offsets '
              '(RECON-SCHEMA, RESOLUTION-SCHEMA), the `.json` suffix filter and silently skipped parse failures '
              '(SCAN-PARSE), skipped or unknown record kinds (CONFIG-REFS), an optional `git_blob` and the class-level '
              '`paths` form (CLASS-SCHEMA), and the configuration keys `default_for` and `widening_review` (CONFIG-REFS, '
              'WIDENING-ITEMS).', '']
    lines += ['## 5. Points for the owner\'s choice', '']
    lines += ['%d. %s' % (i + 1, x) for i, x in enumerate(OWNER_CHOICES)] + ['']
    lines += ['## 6. Changes', '', '| File | Place | Change |', '|---|---|---|',
              '| DESIGN-r6.md | R6.REC.2 | `invalidates`, `confirms`; keys per R6.RECON.31 |',
              '| DESIGN-r6.md | R6.REC.6 | every review naming the blob counts |',
              '| DESIGN-r6.md | R6.REC.7 | resolution of a reference per R6.RECON.33 |',
              '| DESIGN-r6.md | R6.RECON.24 | RC14 (b) from the retained text; resolution schema and review confirmation |',
              '| DESIGN-r6.md | R6.RECON.25 | `invalidated` form; parenthetical order |',
              '| DESIGN-r6.md | R6.RECON.26 | detection before lint; global target match; Form of a finding (i) to (vi) |',
              '| DESIGN-r6.md | R6.RECON.27 | Keys; `edit` null for a run-level binding |',
              '| DESIGN-r6.md | R6.RECON.21 | `x` read at `X` (= `C` in RT-L2) |',
              '| DESIGN-r6.md | R6.RECON.2 (d) | scanned set per R6.RECON.35 |',
              '| DESIGN-r6.md | R6.CFG.4 | kinds per R6.RECON.33; `retirement` keys; parenthetical order |',
              '| DESIGN-r6.md | R6.ADAPT.2 | raw entries, `edits`, retained `text` |',
              '| DESIGN-r6.md | R6.TREE.5 | class record keys per R6.RECON.34 |',
              '| DESIGN-r6.md | R6.OUT.18 | `classify_records` review, `record_base`, `dispositions`, `category3` |',
              '| DESIGN-r6.md | R6.RECON.28 (new); sec. 23.1, R6.RECON.29 to R6.RECON.36 (new) | the migration record; '
              'the schema contract |',
              '| DESIGN-r6.md | sec. 0.7, R6.CTRL.3, Table 17.1 | the note; %d rows counted and added |' % len(ROWS),
              '| EXPECTATIONS.json | %s (new) | both directions each |' % ', '.join(NEW_IDS),
              '| EXPECTATIONS.json | RECON-BLOCK | the revised-plan countercase requires a cited reassessment; a '
              'wording-change case is added (stays blocked); no expectation value changes |',
              '| EXPECTATIONS.json | S11-2a, RTL2-BIND, RT-D, RT-DR | the amendment 5 nits (sec. 2a), each a declared '
              'change |',
              '| DESIGN-r6.md | sec. 31 | the RT-D figure says 10 W1/W2 lines |',
              '| REQUIREMENTS.json | %s (new); %s | controls appended; `pending_owner_confirmation` |'
              % (', '.join(NEW_REQS), ', '.join(TOUCHED)), '',
              '## 7. Tool changes implied (not made here)', '',
              '- Finding detection before review-record lint; form failures that still block; the global '
              'path-and-old-bytes match; the fallback by id, migrated id or target; run-level binding (R6.RECON.26).',
              '- The reassessment keys and per-finding lifting (R6.RECON.27); migration lint and closure (R6.RECON.28).',
              '- RC14 (b) from the retained text; the resolution schema checks and `confirms` (R6.RECON.24).',
              '- The schema contract: strict parsing, the R6.RECON.30 JSON Schema before any RC, item ids, kinds, '
              'supersedes resolution along `F`\'s first-parent chain, class record keys, the scanned-set selection, the '
              'result fields (R6.RECON.29 to R6.RECON.36).',
              '- The ledger adapter returns `raw`, `edits` and the retained `text` (R6.ADAPT.2).',
              '- Allowlist and schema list (R6.CORE.5): `oi-reassessment/1`, `oi-edit-id-migration/1`, and the new '
              'keys and values where the engine holds them as literals.',
              '- Runners for %s.' % ', '.join(NEW_IDS), '',
              '## 8. Outputs', '', '| File | sha256 |', '|---|---|']
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
