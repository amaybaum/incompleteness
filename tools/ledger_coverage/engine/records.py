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


def item_ids(doc):
    if doc.get('schema') == 'oi-retirement-config/1':
        return [doc.get('config_id')]
    for key, idf in (('rules', 'id'), ('sites', 'site_id'), ('entries', 'id'), ('classifications', 'id'),
                     ('records', 'id'), ('classes', 'id')):
        if isinstance(doc.get(key), list) and doc[key] and all(isinstance(x, dict) and idf in x for x in doc[key]):
            return sorted(x[idf] for x in doc[key])
    for key in ('config_id', 'record_id', 'site_id', 'id'):
        if isinstance(doc.get(key), str):
            return [doc[key]]
    return ['*']


def _person(v):
    return isinstance(v, str) and v.strip() and not _url.search(v) and '/' not in v and not v.isdigit()


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

    def get(self, ref):
        hit = self.by_sha.get(ref.get('blob_sha256'))
        if hit is None or hit[0] != ref.get('path'):
            return None
        return hit[1]


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
    ids = item_ids(doc)
    good_reviews = []
    for sha, path, rv in exact:
        bad = []
        if not _person(rv.get('reviewer')):
            bad.append('reviewer is not a person')
        if rv.get('reviewer') == author:
            bad.append('reviewer equals author')
        verdicts = {v.get('item'): v.get('verdict') for v in rv.get('verdicts', []) if isinstance(v, dict)}
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
            if not _person(a.get('owner')) or not _comment(a.get('comment_id')) or not a.get('time'):
                out.append('record %s: authorization lacks owner, time or comment id' % ref['path'])
                continue
            ok = True
    if not ok:
        out.append('record %s: no owner authorization listing the record and its review' % ref['path'])
    return out


def widening_review_ok(ref, store, admitted_shas, regular_reviewers, author):
    """A review record of kind widening naming exactly this blob, admitted by the configuration, by a non-author
    reviewer other than the record's own reviewers, accepting every item."""
    for sha, (path, d) in store.by_sha.items():
        if not isinstance(d, dict) or d.get('schema') != review_schema or d.get('kind') != 'widening':
            continue
        if sha not in admitted_shas or d.get('reviewed', {}).get('blob_sha256') != ref['blob_sha256']:
            continue
        who = d.get('reviewer')
        if _person(who) and who != author and who not in regular_reviewers and d.get('verdicts') and \
                all(v.get('verdict') == 'accept' for v in d.get('verdicts', [])):
            return True
    return False


def reviewers_of(ref, store):
    return {d.get('reviewer') for sha, (p, d) in store.by_sha.items()
            if isinstance(d, dict) and d.get('schema') == review_schema and d.get('kind', 'review') == 'review'
            and d.get('reviewed', {}).get('blob_sha256') == ref['blob_sha256']}
