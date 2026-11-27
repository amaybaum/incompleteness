# Category-3 detection, finding form and binding (Amendment 6 r13 R6.RECON.26 Form of a finding (i)-(v), R6.RECON.29,
# .30, .31, .35, as the OBL-29 remedy r9 applies them to the cumulative record set R*).
#
# - R6.RECON.35 selection and classes: a selected file (optional BOM, ASCII whitespace, then `{` or `[`) is class (a)
# when it parses strictly (R6.RECON.29) as an object whose `schema` is exactly a reconciliation or review schema;
# class (b) when some object at any depth, parsed with duplicate keys and non-finite numbers admitted, has a schema
# string beginning (trimmed, case folded) `oi-review-record/` or `oi-reconciliation/`, or a review's shape; class (c)
# when it does not parse even so and its lossy text, `\uXXXX` escapes resolved and case folded, contains one of those
# prefixes. A class (b) or (c) file whose text, escapes resolved, contains `invalidates` or `invalidated` is a
# malformed finding.
# - Form (i): detection precedes lint. A first-kind finding is a reconciliation entry whose `scientific_effect` has the
# verdict `invalidates` or carries `invalidated`, whatever its review says; a second-kind finding is a review verdict
# entry with the verdict `invalidates` or the key `invalidated`, unless the reviewer equals the reviewed record's
# author or is a run, check or Issue.
# - The key tables of R6.RECON.30 and .31 decide a record's schema (a form failure of a finding still blocks).
import json
import re

from . import util

recon_schemas = ('oi-reconciliation/1', 'oi-reconciliation/2')
# the mechanical floor of the executed-path rule (R6.RECON.30, R6.CFG.4 executed_suffixes)
executed_floor = ('.py', '.lean', '.yml', '.yaml', '.sh')
review_schema = 'oi-review-record/1'
# the engine's internal tags of the R6.RECON.35 classes (a), (b) and (c)
tag_strict, tag_lenient, tag_textual = 'strict', 'lenient', 'textual'
_esc = re.compile(r'\\u([0-9a-fA-F]{4})')
_hex40 = re.compile(r'[0-9a-f]{40}\Z')
_hex64 = re.compile(r'[0-9a-f]{64}\Z')
_runlike = re.compile(r'://|/runs/|/actions|check[-_ ]run|/issues/\d+$|^#\d+$|/pull/\d+$')


class Unsettled(Exception):
    # A point the design text does not settle: the run stops with ERROR, never a verdict (fail closed).
    pass


class RunLevelBlock(Exception):
    # A finding whose binding cannot be decided from readable inputs: the named configuration's ledger cannot be read,
    # or a ledger target is ambiguous or missing. Owner decision of 2026-11-27: a run-level FAIL retirement-blocked with
    # FAIL record-invalid, its evidence and provenance kept; ERROR stays only for an unreadable object and for edit-id
    # migrations (R6.RECON.28, not implemented).
    pass


# ---- R6.RECON.35 selection and classes ------------------------------------------------------------------------

def _decode(data):
    """(text, utf16) for a selected file, or None when the file is not selected."""
    if data.startswith(b'\xef\xbb\xbf'):
        body, enc = data[3:], 'utf-8'
    elif data.startswith(b'\xff\xfe') or data.startswith(b'\xfe\xff'):
        enc = 'utf-16'
        text = data.decode('utf-16', 'replace').lstrip('﻿')
        stripped = text.lstrip(' \t\r\n')
        return (text, True) if stripped[:1] in ('{', '[') else None
    else:
        body, enc = data, 'utf-8'
    i = 0
    while i < len(body) and body[i:i + 1] in (b' ', b'\t', b'\r', b'\n'):
        i += 1
    if body[i:i + 1] not in (b'{', b'['):
        return None
    return body.decode(enc, 'replace'), False


def strict_parse(data):
    # R6.RECON.29 strict parse: UTF-8 without a BOM, one JSON object, no duplicate key, no NaN or Infinity.
    if data.startswith(b'\xef\xbb\xbf'):
        return None

    def pairs(ps):
        d = {}
        for k, v in ps:
            if k in d:
                raise ValueError('duplicate key')
            d[k] = v
        return d

    def nonfinite(_x):
        raise ValueError('a NaN or Infinity constant')
    try:
        doc = json.loads(data.decode('utf-8'), object_pairs_hook=pairs, parse_constant=nonfinite)
    except (ValueError, UnicodeDecodeError):
        return None
    return doc if isinstance(doc, dict) else None


def _lenient(text):
    try:
        return json.loads(text)
    except ValueError:
        return None


def _resolve_escapes(text):
    return _esc.sub(lambda m: chr(int(m.group(1), 16)), text)


def _objects(v):
    if isinstance(v, dict):
        yield v
        for x in v.values():
            yield from _objects(x)
    elif isinstance(v, list):
        for x in v:
            yield from _objects(x)


def _schema_like(o):
    s = o.get('schema')
    if isinstance(s, str):
        t = s.strip().casefold()
        return t.startswith('oi-review-record/') or t.startswith('oi-reconciliation/')
    return 'schema' not in o and 'reviewed' in o and isinstance(o.get('verdicts'), list) and any(
        isinstance(v, dict) and (v.get('verdict') == 'invalidates' or 'invalidated' in v) for v in o['verdicts'])


def classify(data):
    """(class, detail) of one blob: (tag_strict, schema), (tag_lenient, signal) or (tag_textual, signal), the scan's
    classes (a), (b) and (c), or None (not selected or no class)."""
    dec = _decode(data)
    if dec is None:
        return None
    text, _ = dec
    doc = strict_parse(data)
    if isinstance(doc, dict) and doc.get('schema') in recon_schemas + (review_schema,):
        return (tag_strict, doc['schema'])
    resolved = _resolve_escapes(text)
    signal = 'invalidates' in resolved or 'invalidated' in resolved
    loose = _lenient(text.lstrip('﻿'))
    if loose is not None:
        if any(_schema_like(o) for o in _objects(loose)):
            return (tag_lenient, signal)
        return None
    folded = resolved.casefold()
    if 'oi-review-record/' in folded or 'oi-reconciliation/' in folded:
        return (tag_textual, signal)
    return None


# ---- identity strings (R6.RECON.29) ---------------------------------------------------------------------------

_identity = re.compile(r'[A-Za-z0-9][A-Za-z0-9._:-]{0,127}\Z')
_key_drop = str.maketrans('', '', '._:-')


def identity_ok(v):
    # Staging S-2 S2.1: an identity string matches [A-Za-z0-9][A-Za-z0-9._:-]{0,127} as a whole and is not made
    # only of digits (a run or check id): no whitespace, no `/`, no non-ASCII character.
    return isinstance(v, str) and v.isascii() and _identity.match(v) is not None and not v.isdigit()


def identity_key(v):
    # S2.2: ASCII letters made lowercase and `.`, `_`, `:` and `-` removed.
    return v.lower().translate(_key_drop)


def same_identity(a, b):
    """S2.2: two identity strings whose keys are equal (a string that is not an identity string is the same
    identity as nothing)."""
    return identity_ok(a) and identity_ok(b) and identity_key(a) == identity_key(b)


def independence_problems(review, X):
    """S2.4: [] when the review is independent of the identity strings X (members of X that are not identity
    strings are skipped): its reviewer an identity string; `independence` exactly {not_author: true, depends_on: an
    array of identity strings, no two the same identity}; the reviewer and every depends_on element the same identity
    as no member of X."""
    out = []
    who = review.get('reviewer') if isinstance(review, dict) else None
    if not identity_ok(who):
        out.append('the reviewer is not an identity string')
    ind = review.get('independence') if isinstance(review, dict) else None
    deps = ind.get('depends_on') if isinstance(ind, dict) else None
    if not (isinstance(ind, dict) and set(ind) == {'not_author', 'depends_on'} and ind['not_author'] is True and
            isinstance(deps, list) and all(identity_ok(d) for d in deps) and
            len({identity_key(d) for d in deps}) == len(deps)):
        out.append('the independence declaration is missing or malformed')
        deps = []
    xs = [x for x in X if identity_ok(x)]
    if identity_ok(who) and any(same_identity(who, x) for x in xs):
        out.append('the reviewer is the same identity as a party it must be independent of')
    if any(same_identity(d, x) for d in deps for x in xs):
        out.append('the independence declaration names a party the reviewer must be independent of')
    return out


def run_like(v):
    # A run, check or Issue named where an identity string belongs (R6.REC.6).
    return isinstance(v, str) and (bool(_runlike.search(v.strip())) or v.strip().isdigit())


# ---- the key tables (R6.RECON.30, .31) ------------------------------------------------------------------------

def _enc(t, v):
    if t == 'commit' or t == 'blob':
        return isinstance(v, str) and bool(_hex40.match(v))
    if t == 'sha256':
        return isinstance(v, str) and bool(_hex64.match(v))
    if t == 'offset':
        return type(v) is int and v >= 0
    if t == 'path':
        return isinstance(v, str) and bool(v) and not v.startswith('/') and not v.endswith('/') and \
            all(p not in ('', '.', '..') for p in v.split('/'))
    if t == 'identity':
        return identity_ok(v)
    if t == 'nestr':
        return isinstance(v, str) and bool(v)
    if t == 'str':
        return isinstance(v, str)
    if t == 'array':
        return isinstance(v, list)
    if t == 'b64':
        import base64
        if not isinstance(v, str):
            return False
        try:
            return base64.b64encode(base64.b64decode(v, validate=True)).decode() == v
        except ValueError:
            return False
    raise AssertionError(t)


ref_keys = {'path': ('path', True), 'blob_sha256': ('sha256', True)}
target_keys = {'path': ('path', True), 'start_H': ('offset', True), 'old_sha256': ('sha256', True)}
invalidated_keys = {'id': ('nestr', True), 'sha256': ('sha256', True), 'target': (('keyed', target_keys), True)}
sci_keys = {'conclusions': (('or', ('lit', ('none',)), ('distinct_ids',)), True), 'assessment': ('nestr', True),
       'method': ('nestr', True), 'verdict': (('lit', ('no-effect', 'invalidates')), True),
       'configuration': (('keyed', ref_keys), True), 'invalidated': (('nearray', ('keyed', invalidated_keys)), False)}
binding_keys = {k: (('or', ('null',), 'sha256'), True) for k in ('files_entry_sha256', 'splices_sha256',
                                                            'edit_records_sha256')}
splice_keys = {'id': ('nestr', True), 'start_H': ('offset', True), 'end_H': ('offset', True), 'start_M': ('offset', True),
          'end_M': ('offset', True), 'new_sha256': ('sha256', True),
          'translation': (('or', ('lit', ('identity',)), ('int',)), True)}
protected_keys = {'start_M': ('offset', True), 'end_M': ('offset', True), 'sha256': ('sha256', True)}
resolution_keys = {'splice': ('nestr', True), 'start_M': ('offset', True), 'end_M': ('offset', True),
              'sha256': ('sha256', True), 'resolved': ('b64', True), 'resolved_sha256': ('sha256', True)}
entry_keys = {'path': ('path', True), 'ledger_binding': (('keyed', binding_keys), True),
         'side_change_commits': (('arr', 'commit'), True), 'scientific_effect': (('keyed', sci_keys), True),
         'm': ('blob', True), 'm_sha256': ('sha256', True), 'l': ('blob', True), 'l_sha256': ('sha256', True),
         'x': ('blob', True), 'x_sha256': ('sha256', True), 'splices': (('arr', ('keyed', splice_keys)), True),
         'protected': (('arr', ('keyed', protected_keys)), True), 'resolutions': (('arr', ('keyed', resolution_keys)), False)}
RECORD = {'schema': (('lit', ('oi-reconciliation/2',)), True), 'record_id': ('nestr', True),
          'supersedes': (('or', ('null',), ('keyed', ref_keys)), True), 'author': ('identity', True),
          'M': ('commit', True), 'X': ('commit', True), 'ledger_base': ('commit', True),
          'changes_decisions_on_X': ('array', True), 'paths': (('nearray', ('keyed', entry_keys)), True)}
confirms_keys = {'start_M': ('offset', True), 'end_M': ('offset', True), 'sha256': ('sha256', True),
            'resolved_sha256': ('sha256', True)}
verdict_keys = {'item': ('nestr', True), 'verdict': (('lit', ('accept', 'reject', 'dissent', 'invalidates')), True),
           'reason': ('str', True), 'invalidated': (('nearray', ('keyed', invalidated_keys)), False),
           'configuration': (('keyed', ref_keys), False), 'confirms': (('keyed', confirms_keys), False)}
review_keys = {'schema': (('lit', (review_schema,)), True), 'kind': (('lit', ('review', 'widening')), False),
          'reviewer': ('identity', True), 'reviewed': (('keyed', ref_keys), True), 'replaces': (('keyed', ref_keys), False),
          'method': ('nestr', True), 'verdicts': (('arr', ('keyed', verdict_keys)), True), 'dissent': ('str', False)}


def _type_ok(t, v, where, out):
    if isinstance(t, str):
        if not _enc(t, v):
            out.append('%s: not %s' % (where, t))
        return
    head = t[0]
    if head == 'lit':
        if v not in t[1] or not isinstance(v, str):
            out.append('%s: not one of %s' % (where, list(t[1])))
    elif head == 'null':
        if v is not None:
            out.append('%s: not null' % where)
    elif head == 'int':
        if type(v) is not int:
            out.append('%s: not an integer' % where)
    elif head == 'distinct_commits':
        if not (isinstance(v, list) and v and all(isinstance(x, str) and _hex40.match(x) for x in v) and
                len(set(v)) == len(v)):
            out.append('%s: not a non-empty array of distinct commit ids' % where)
    elif head == 'distinct_ids':
        if not (isinstance(v, list) and v and all(isinstance(x, str) and x for x in v) and len(set(v)) == len(v)):
            out.append('%s: not a non-empty array of distinct edit ids' % where)
    elif head == 'or':
        for alt in t[1:]:
            tmp = []
            _type_ok(alt, v, where, tmp)
            if not tmp:
                return
        out.append('%s: of no admitted type' % where)
    elif head == 'keyed':
        validate(t[1], v, where, out)
    elif head in ('arr', 'nearray'):
        if not isinstance(v, list) or (head == 'nearray' and not v):
            out.append('%s: not a%s array' % (where, ' non-empty' if head == 'nearray' else 'n'))
            return
        for i, x in enumerate(v):
            _type_ok(t[1], x, '%s[%d]' % (where, i), out)
    else:
        raise AssertionError(t)


def validate(table, doc, where, out):
    if not isinstance(doc, dict):
        out.append('%s: not an object' % where)
        return
    for k, (t, req) in table.items():
        if k not in doc:
            if req:
                out.append('%s.%s: missing' % (where, k))
            continue
        _type_ok(t, doc[k], '%s.%s' % (where, k), out)
    for k in doc:
        if k not in table:
            out.append('%s.%s: unlisted key' % (where, k))


def record_schema_problems(doc):
    # R6.RECON.30 key tables of an oi-reconciliation/2 record, with its conditional presence (`invalidated` exactly
    # when the verdict is `invalidates`) and each entry path once. A record of schema oi-reconciliation/1 fails.
    out = []
    if isinstance(doc, dict) and doc.get('schema') == 'oi-reconciliation/1':
        return ['$.schema: oi-reconciliation/1 is not accepted']
    validate(RECORD, doc, '$', out)
    for i, e in enumerate(doc.get('paths') or [] if isinstance(doc, dict) else []):
        se = e.get('scientific_effect') if isinstance(e, dict) else None
        if isinstance(se, dict) and (('invalidated' in se) != (se.get('verdict') == 'invalidates')):
            out.append('$.paths[%d].scientific_effect: invalidated present exactly when the verdict is invalidates'
                       % i)
    paths = [e.get('path') for e in (doc.get('paths') or []) if isinstance(e, dict)] if isinstance(doc, dict) else []
    if len(paths) != len(set(map(str, paths))):
        out.append('$.paths: an entry path occurs more than once')
    return out


def review_schema_problems(doc):
    # R6.RECON.31 key tables of a review record, with its conditional presence (`replaces` exactly when the kind
    # is widening; `invalidated` and `configuration` only with `invalidates`).
    out = []
    validate(review_keys, doc, '$', out)
    if isinstance(doc, dict) and ('replaces' in doc) != (doc.get('kind') == 'widening'):
        out.append('$.replaces: present exactly when the kind is widening')
    verdicts = doc.get('verdicts') if isinstance(doc, dict) else None
    for i, v in enumerate(verdicts if isinstance(verdicts, list) else []):
        if isinstance(v, dict) and v.get('verdict') != 'invalidates':
            for k in ('invalidated', 'configuration'):
                if k in v:
                    out.append('$.verdicts[%d].%s: only with the verdict invalidates' % (i, k))
    return out


def item_ids_of_record(doc):
    ids = []
    for e in doc.get('paths') or [] if isinstance(doc, dict) else []:
        if isinstance(e, dict) and isinstance(e.get('path'), str):
            ids += [e['path'], e['path'] + ':scientific_effect']
            ids += [e['path'] + ':resolution:' + str(x.get('splice')) for x in (e.get('resolutions') or [])
                    if isinstance(x, dict)]
    return ids


def entry_of_item(doc, item):
    """The entry of a reconciliation record that an item id of it names, or None."""
    for e in doc.get('paths') or [] if isinstance(doc, dict) else []:
        if isinstance(e, dict) and isinstance(e.get('path'), str) and item in item_ids_of_record({'paths': [e]}):
            return e
    return None


def first_kind_entries(doc):
    """Form (i): the entries of a reconciliation record that carry a finding of the first kind."""
    out = []
    for e in doc.get('paths') or [] if isinstance(doc, dict) and isinstance(doc.get('paths'), list) else []:
        se = e.get('scientific_effect') if isinstance(e, dict) else None
        if isinstance(se, dict) and (se.get('verdict') == 'invalidates' or 'invalidated' in se):
            out.append(e)
    return out


def second_kind_verdicts(doc):
    """Form (i): the verdict entries of a review record that carry a finding of the second kind."""
    verdicts = doc.get('verdicts') if isinstance(doc, dict) else None
    if not isinstance(verdicts, list):
        return []
    return [v for v in verdicts if isinstance(v, dict) and
            (v.get('verdict') == 'invalidates' or 'invalidated' in v)]


def second_kind_form_problems(review, reviewed_doc, verdict):
    """The form failures of a second-kind finding (Form (i)): the review's schema, a missing method, verdicts that
    omit or duplicate an item, invalidates on another item than <path>:scientific_effect, invalidated without the
    verdict invalidates, an empty or malformed invalidated, a missing configuration."""
    out = review_schema_problems(review)
    if not (isinstance(review.get('method'), str) and review['method']):
        out.append('a missing method')
    if isinstance(reviewed_doc, dict):
        ids = item_ids_of_record(reviewed_doc)
        named = [v.get('item') for v in review.get('verdicts') or [] if isinstance(v, dict)]
        if set(ids) - set(named) or len(named) != len(set(map(str, named))):
            out.append('verdicts that omit or duplicate an item')
    item = verdict.get('item')
    if verdict.get('verdict') == 'invalidates' and not (isinstance(item, str) and item.endswith(':scientific_effect')):
        out.append('invalidates on an item other than <path>:scientific_effect')
    if 'invalidated' in verdict and verdict.get('verdict') != 'invalidates':
        out.append('invalidated with a verdict value other than invalidates')
    inv = verdict.get('invalidated')
    tmp = []
    _type_ok(('nearray', ('keyed', invalidated_keys)), inv, 'invalidated', tmp)
    if tmp:
        out.append('an empty or malformed invalidated')
    if not isinstance(verdict.get('configuration'), dict):
        out.append('a missing or unreadable configuration')
    return out


def element_ok(x):
    tmp = []
    validate(invalidated_keys, x, 'invalidated', tmp)
    return not tmp
