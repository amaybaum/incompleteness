"""Ownership chain of every reviewed record kind: writer, independent reviewer, owner authorization (sec. 6.3)."""
import json
import re

from . import util

review_schema = 'oi-review-record/1'
auth_schema = 'oi-owner-authorization/1'
record_schemas = ('oi-term-rules/2', 'oi-hp-adjudication/1', 'oi-context-adjudication/1', 'oi-hit-classification/1',
                  'oi-scope/1', 'oi-side-change-classes/1', 'oi-reconciliation/1', 'oi-retirement-config/1',
                  'oi-delegation/1')

_url = re.compile(r'://|/runs/|/actions|check[-_ ]run|/issues/\d+$|^#\d+$|/pull/\d+$')


item_lists = (('rules', 'id'), ('sites', 'site_id'), ('entries', 'id'), ('classifications', 'id'), ('records', 'id'),
              ('classes', 'id'))


def item_list_problems(doc):
    """A description of every item list field present in a record that is not a list (sec. 6.3: a field error is
    record-invalid)."""
    if not isinstance(doc, dict) or doc.get('schema') == 'oi-retirement-config/1':
        return []
    return ['%s is not a list' % key for key, _ in item_lists if key in doc and not isinstance(doc[key], list)]


def entries_without_id(doc):
    """[(list key, index)] of every entry of an item list that is not an object carrying its id field as a non-empty
    string (sec. 6.3: a missing field is record-invalid)."""
    if not isinstance(doc, dict) or doc.get('schema') == 'oi-retirement-config/1':
        return []
    out = []
    for key, idf in item_lists:
        if isinstance(doc.get(key), list):
            out += [(key, i) for i, x in enumerate(doc[key])
                    if not (isinstance(x, dict) and isinstance(x.get(idf), str) and x[idf])]
    return out


def item_ids(doc):
    """The item ids a review gives one verdict each (sec. 6.3). The ids of every non-empty item list; a record with
    no item list is one item, its record id. A record any of whose list entries lacks its id field has no item ids,
    and is record-invalid: the record id never stands in for an entry's id."""
    if doc.get('schema') == 'oi-retirement-config/1':
        return [doc.get('config_id')]
    if item_list_problems(doc) or entries_without_id(doc):
        return []
    ids = []
    for key, idf in item_lists:
        if isinstance(doc.get(key), list):
            ids += [x[idf] for x in doc[key]]
    if ids:
        return sorted(ids)
    for key in ('config_id', 'record_id', 'site_id', 'id'):
        if isinstance(doc.get(key), str):
            return [doc[key]]
    return []


def _person(v):
    return isinstance(v, str) and v.strip() and not _url.search(v) and '/' not in v and not v.isdigit()


def _owner(v):
    """An owner is a numeric host user id (sec. 6.3, A-D1); a login never matches."""
    return isinstance(v, int) and not isinstance(v, bool) and v > 0


def _comment(v):
    return isinstance(v, str) and v.strip() and not _url.search(v)


class Store:
    """Records read from the object store: {path: (sha256, doc)}; nothing is read from a working tree."""

    def __init__(self, entries):
        self.by_path = {}
        self.by_sha = {}
        for path, data in entries:
            sha = util.sha256(data)
            try:
                doc = json.loads(data.decode('utf-8'))
            except (ValueError, UnicodeDecodeError):
                doc = None
            self.by_path.setdefault(path, []).append((sha, doc))
            self.by_sha[sha] = (path, doc)

    resolver = None

    def get(self, ref):
        hit = self.by_sha.get(ref.get('blob_sha256'))
        if hit is None or hit[0] != ref.get('path'):
            return None
        return hit[1]

    def resolve(self, ref):
        """A record read from the object store (at or before F) by {path, blob_sha256}, or None."""
        if not isinstance(ref, dict) or not isinstance(ref.get('path'), str) or \
                not isinstance(ref.get('blob_sha256'), str):
            return None
        got = self.get(ref)
        if got is None and self.resolver is not None:
            got = self.resolver(ref)
        return got


def supersedes_problems(ref, doc, store):
    """S4: a supersedes chain must name records of the same kind, schema and lineage that exist in the object
    store; a first record has supersedes null."""
    out = []
    seen = {ref.get('blob_sha256')}
    cur = doc
    while isinstance(cur, dict) and cur.get('supersedes') is not None:
        sup = cur['supersedes']
        prev = store.resolve(sup)
        if prev is None:
            out.append('record %s: supersedes names %r, which is not a record in the object store'
                       % (ref.get('path'), sup))
            break
        if not isinstance(prev, dict) or prev.get('schema') != doc.get('schema') or \
                (doc.get('schema') == 'oi-retirement-config/1' and prev.get('config_id') != doc.get('config_id')):
            out.append('record %s: supersedes names a record of another kind, schema or lineage' % ref.get('path'))
            break
        if sup.get('blob_sha256') in seen:
            out.append('record %s: supersedes chain loops' % ref.get('path'))
            break
        seen.add(sup.get('blob_sha256'))
        cur = prev
    return out


def lint_chain(ref, store, owner, admitted_shas):
    """Problems with one record's chain. ref = {path, blob_sha256}; admitted_shas: the blobs the configuration
    references (records, reviews, authorizations)."""
    out = []
    doc = store.get(ref)
    if doc is None:
        return ['record %s: blob not in the object store at its path' % ref.get('path')]
    if ref['blob_sha256'] not in admitted_shas:
        out.append('record %s: not referenced by the configuration' % ref['path'])
    if doc.get('schema') not in record_schemas:
        out.append('record %s: unknown schema %r' % (ref['path'], doc.get('schema')))
    if 'supersedes' not in doc:
        out.append('record %s: no supersedes field' % ref['path'])
    out += supersedes_problems(ref, doc, store)
    author = doc.get('author')
    if not _person(author):
        out.append('record %s: author missing or not a person' % ref['path'])
    reviews = [(sha, path, d) for sha, (path, d) in store.by_sha.items()
               if isinstance(d, dict) and d.get('schema') == review_schema and sha in admitted_shas
               and isinstance(d.get('reviewed'), dict) and d['reviewed'].get('path') == ref['path']
               and d.get('kind', 'review') == 'review']
    exact = [r for r in reviews if r[2]['reviewed'].get('blob_sha256') == ref['blob_sha256']]
    if not exact:
        if reviews:
            out.append('record %s: review names another blob of the same path' % ref['path'])
        else:
            out.append('record %s: no review record' % ref['path'])
        return out
    shape = item_list_problems(doc)
    if shape:
        out.append('record %s: %s' % (ref['path'], shape[0]))
        return out
    missing = entries_without_id(doc)
    if missing:
        out.append('record %s: %s entry %d lacks its id field' % ((ref['path'],) + missing[0]))
        return out
    ids = item_ids(doc)
    # one verdict per item id (sec. 6.3): an id given to two items is record-invalid. Two classes of a side-change
    # class record sharing an id are instead the configuration inconsistency of S7 (ERROR CONFIG_INCONSISTENT,
    # control Z11), raised where the classes are collected
    dup = sorted({i for i in ids if ids.count(i) > 1})
    if dup and doc.get('schema') != 'oi-side-change-classes/1':
        out.append('record %s: item id %s is given to more than one item' % (ref['path'], dup[0]))
        return out
    if not ids:
        # a review gives one verdict per item id (sec. 6.3); a record whose items cannot be identified is refused
        # rather than covered by a single verdict
        out.append('record %s: no item ids can be identified' % ref['path'])
        return out
    good_reviews = []
    for sha, path, rv in exact:
        bad = []
        if not _person(rv.get('reviewer')):
            bad.append('reviewer is not a person')
        if rv.get('reviewer') == author:
            bad.append('reviewer equals author')
        verdicts = {v.get('item'): v.get('verdict') for v in rv.get('verdicts', []) if isinstance(v, dict)}
        named = [v.get('item') for v in rv.get('verdicts', []) if isinstance(v, dict)]
        if len(named) != len(set(named)):
            bad.append('an item has more than one verdict')
        if set(ids) - set(verdicts):
            bad.append('verdicts do not cover every item')
        if any(verdicts.get(i) != 'accept' for i in ids):
            bad.append('an item is not accepted')
        if not rv.get('method'):
            bad.append('no method')
        if bad:
            out.append('record %s: review %s: %s' % (ref['path'], path, '; '.join(bad)))
        else:
            good_reviews.append((sha, path, rv))
    if not good_reviews:
        return out
    auths = [d for sha, (path, d) in store.by_sha.items()
             if isinstance(d, dict) and d.get('schema') == auth_schema and sha in admitted_shas]
    ok = False
    for a in auths:
        for e in a.get('authorizes', []):
            rec, rv = e.get('record', {}), e.get('review', {})
            if rec.get('path') == ref['path'] and 'blob_sha256' not in rec:
                out.append('record %s: authorization names the path without a hash' % ref['path'])
                continue
            if rec.get('blob_sha256') != ref['blob_sha256']:
                continue
            if not any(rv.get('blob_sha256') == g[0] and rv.get('path') == g[1] for g in good_reviews):
                continue
            if a.get('owner') != owner:
                out.append('record %s: authorization owner differs from the configuration owner' % ref['path'])
                continue
            if not _owner(a.get('owner')) or not _comment(str(a.get('comment_id') or '')) or not a.get('time'):
                out.append('record %s: authorization lacks owner, time or comment id' % ref['path'])
                continue
            ok = True
    if not ok:
        out.append('record %s: no owner authorization listing the record and its review' % ref['path'])
    return out


def widening_review_problems(ref, store, admitted_shas, regular_reviewers, author, old_ref, changed, owner):
    """Sec. 6.3 (B4): a review of kind widening naming the new blob and the blob it replaces, admitted, by a
    non-author reviewer other than the record's own reviewers, with an `accept` verdict for every changed item,
    and an owner authorization listing the widening review's blob. Returns [] when one such review exists."""
    why = []
    for sha, (path, d) in sorted(store.by_sha.items()):
        if not isinstance(d, dict) or d.get('schema') != review_schema or d.get('kind') != 'widening':
            continue
        if sha not in admitted_shas or d.get('reviewed', {}).get('blob_sha256') != ref['blob_sha256']:
            continue
        bad = []
        if old_ref is not None and (d.get('replaces') or {}).get('blob_sha256') != old_ref.get('blob_sha256'):
            bad.append('does not name the blob it replaces')
        who = d.get('reviewer')
        if not _person(who) or who == author or who in regular_reviewers:
            bad.append('reviewer is the author, a regular reviewer, or not a person')
        verdicts = {v.get('item'): v.get('verdict') for v in d.get('verdicts', []) if isinstance(v, dict)}
        miss = [c for c in changed if verdicts.get(c) != 'accept']
        if miss or any(v != 'accept' for v in verdicts.values()) or not verdicts:
            bad.append('verdicts do not accept every changed item (%s)' % ', '.join(miss[:3]))
        auth = any(isinstance(a, dict) and a.get('schema') == auth_schema and s2 in admitted_shas and
                   a.get('owner') == owner and _owner(a.get('owner')) and a.get('comment_id') and a.get('time') and
                   any((e.get('review') or {}).get('blob_sha256') == sha or
                       (e.get('record') or {}).get('blob_sha256') == sha for e in a.get('authorizes', []))
                   for s2, (_, a) in store.by_sha.items())
        if not auth:
            bad.append('no owner authorization lists the widening review')
        if not bad:
            return []
        why.append('widening review %s: %s' % (path, '; '.join(bad)))
    return why or ['no widening review names the superseding blob']


def widening_review_ok(ref, store, admitted_shas, regular_reviewers, author, old_ref=None, changed=(), owner=None):
    return not widening_review_problems(ref, store, admitted_shas, regular_reviewers, author, old_ref, changed, owner)


def reviewers_of(ref, store):
    return {d.get('reviewer') for sha, (p, d) in store.by_sha.items()
            if isinstance(d, dict) and d.get('schema') == review_schema and d.get('kind', 'review') == 'review'
            and d.get('reviewed', {}).get('blob_sha256') == ref['blob_sha256']}
