"""Ownership chain of every reviewed record kind: writer, independent reviewer, owner authorization (design v5.5.8,
sec. 6.3), with each authorization counted under "Owner at creation" (DI-1) and the lineage of every `supersedes`
chain (DI-2)."""
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


_iso = re.compile(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$')


class OwnerTimeline:
    """The owner of `A` over time (sec. 6.3, "Owner at creation", DI-1). `versions` are the verified versions of `A`
    on main's first-parent chain, oldest first, as (host merge time, owner id, blob sha256). The version in force at a
    time `t` is the latest version whose merge time is strictly before `t`; an owner change is the merge of a version
    whose owner id differs from that of the version it replaces. Host times are UTC timestamps
    YYYY-MM-DDTHH:MM:SSZ, which order as strings.

    `constant(owner)` is the timeline of a control-harness run that has no host: one owner at every time and no owner
    change, so that an authorization counts exactly when its owner is that owner."""

    def __init__(self, versions, host=True):
        self.versions = list(versions)
        self.host = host

    @classmethod
    def constant(cls, owner):
        return cls([(None, owner, None)], host=False)

    @classmethod
    def from_versions(cls, versions):
        """From the `authority_versions` of an admission snapshot (each with merged_at, owner_id, blob_sha256)."""
        out = []
        for v in versions or []:
            if not isinstance(v, dict) or not _iso.match(str(v.get('merged_at'))):
                return None
            out.append((v['merged_at'], v.get('owner_id'), v.get('blob_sha256')))
        return cls(out) if out else None

    def valid_time(self, t):
        if not isinstance(t, str) or not t.strip():
            return False
        return bool(_iso.match(t)) if self.host else True

    def in_force(self, t):
        """(merged_at, owner id, blob sha256) of the version in force at `t`, or None."""
        if not self.host:
            return self.versions[-1]
        if not self.valid_time(t):
            return None
        got = None
        for v in self.versions:
            if v[0] < t:
                got = v
        return got

    def owner_at(self, t):
        v = self.in_force(t)
        return None if v is None else v[1]

    def owner_changes(self):
        return [v[0] for i, v in enumerate(self.versions) if i and v[1] != self.versions[i - 1][1]]

    def changed_between(self, t1, t2=None):
        """True if an owner change merged strictly after `t1` (and strictly before `t2`, when given)."""
        return any(t1 < m and (t2 is None or m < t2) for m in self.owner_changes())

    @property
    def governing_owner(self):
        return self.versions[-1][1] if self.versions else None

    def owner_comment(self, author_id, created_at):
        """An owner comment: its author numeric id equals the owner of the version in force at its creation."""
        return author_id is not None and self.owner_at(created_at) == author_id

    def authorization_problem(self, a, predecessor=False):
        """Sec. 6.3, "Owner authorizations": None when the `oi-owner-authorization/1` record `a` counts. For a record
        the run uses: the version of A in force at its `time` has the authorization's `owner`, that owner is the owner
        of the governing A, and no owner change merged after its `time`. For a predecessor named by a `supersedes` (a
        completed action): the version of A in force at its `time` has the authorization's `owner`."""
        t = a.get('time')
        if not self.valid_time(t):
            return 'its time is not a host timestamp'
        if self.owner_at(t) != a.get('owner'):
            return 'its owner was not the owner of the authority record in force at its time'
        if predecessor:
            return None
        if a.get('owner') != self.governing_owner:
            return 'its owner is not the owner of the governing authority record'
        if self.changed_between(t):
            return 'an owner change merged after its time'
        return None


class Store:
    """Records read from the object store: {path: (sha256, doc)}; nothing is read from a working tree.

    `scan` (set by the configuration loader) returns [(path, bytes)] of every record in the audit directory and the
    plan's record directory at F; it is read only when a `supersedes` chain is walked (DI-2). `timeline` is the
    owner timeline of the admission (DI-1); `widening` maps (old doc, new doc) to the widening items of a rule file or
    configuration."""

    def __init__(self, entries):
        self.by_path = {}
        self.by_sha = {}
        for path, data in entries:
            self.add(path, data)
        self._scanned = None
        self._pred_cache = {}

    resolver = None
    scan = None
    timeline = None
    widening = None
    heads_problems = None

    def add(self, path, data):
        sha = util.sha256(data)
        try:
            doc = json.loads(data.decode('utf-8'))
        except (ValueError, UnicodeDecodeError):
            doc = None
        self.by_path.setdefault(path, []).append((sha, doc))
        self.by_sha[sha] = (path, doc)
        return sha

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

    def scanned(self):
        """{sha: (path, doc)} of the records of the audit and plan record directories at F, and of this store."""
        if self._scanned is None:
            self._scanned = dict(self.by_sha)
            for path, data in (self.scan() if self.scan is not None else []):
                sha = util.sha256(data)
                if sha in self._scanned:
                    continue
                try:
                    self._scanned[sha] = (path, json.loads(data.decode('utf-8')))
                except (ValueError, UnicodeDecodeError):
                    continue
        return self._scanned


def lineage_id(doc):
    """DI-2: a record's lineage is its `record_id`; the configuration's is its `config_id`. None if not a non-empty
    string."""
    if not isinstance(doc, dict):
        return None
    v = doc.get('config_id') if doc.get('schema') == 'oi-retirement-config/1' else doc.get('record_id')
    return v if isinstance(v, str) and v else None


def supersedes_problems(ref, doc, store, owner=None):
    """S4 and DI-2 over the `supersedes` chain of one record: every step names a record that exists in the object
    store at or before F and has the same kind, schema and lineage (`record_id`, or `config_id` for the
    configuration); a record that supersedes, or is named by a `supersedes`, carries a valid lineage id; every
    predecessor passes the lint itself, verified independently of the superseding record, its authorizations (a
    widening review's included) counted as "Owner at creation" states for a predecessor; the chain has no cycle; and no
    other record in the audit directory, the plan's record directory or the records the run reads supersedes the
    same predecessor (ambiguous ancestry)."""
    out = []
    if not isinstance(doc, dict) or doc.get('supersedes') is None:
        return out
    lid = lineage_id(doc)
    if lid is None:
        return ['record %s: supersedes another record but has no valid lineage id (record_id)' % ref.get('path')]
    seen = {ref.get('blob_sha256')}
    cur = doc
    while isinstance(cur, dict) and cur.get('supersedes') is not None:
        sup = cur['supersedes']
        prev = store.resolve(sup)
        if prev is None:
            out.append('record %s: supersedes names %r, which is not a record in the object store'
                       % (ref.get('path'), sup))
            break
        if not isinstance(prev, dict) or prev.get('schema') != doc.get('schema'):
            out.append('record %s: supersedes names a record of another kind, schema or lineage' % ref.get('path'))
            break
        if lineage_id(prev) is None:
            out.append('record %s: supersedes names a record without a valid lineage id (record_id)' % ref.get('path'))
            break
        if lineage_id(prev) != lid:
            out.append('record %s: supersedes names a record of another lineage (an unrelated chain)'
                       % ref.get('path'))
            break
        if sup.get('blob_sha256') in seen:
            out.append('record %s: supersedes chain loops' % ref.get('path'))
            break
        seen.add(sup.get('blob_sha256'))
        forks = sorted({p for s, (p, d) in store.scanned().items()
                        if s != sup.get('blob_sha256') and s not in seen and isinstance(d, dict)
                        and isinstance(d.get('supersedes'), dict)
                        and d['supersedes'].get('blob_sha256') == sup.get('blob_sha256')})
        if forks:
            out.append('record %s: ambiguous ancestry: %s also supersedes %s' % (ref.get('path'), forks[0],
                                                                               sup.get('path')))
            break
        why = predecessor_problems(sup, prev, store, owner)
        if why:
            out.append('record %s: its predecessor %s does not pass the lint: %s' % (ref.get('path'), sup.get('path'),
                                                                                    why[0]))
            break
        cur = prev
    return out


def predecessor_problems(ref, doc, store, owner=None):
    """DI-2: the lint of a predecessor named by a `supersedes`, read from the object store at or before F and verified
    independently of the superseding record: its own review and authorization (found among the records of the audit
    and plan record directories), and, when it widens the record it supersedes, its widening review with that review's
    authorization; each authorization counted as a completed action (sec. 6.3, "Owner at creation"). Its own chain is
    walked by the caller. `owner` is the configuration's owner, used only by the constant timeline of a run without
    a host."""
    key = ref.get('blob_sha256')
    if key in store._pred_cache:
        return store._pred_cache[key]
    store._pred_cache[key] = ['the predecessor chain is being evaluated']
    out = lint_chain(ref, store, owner, None, predecessor=True)
    if not out and store.widening is not None:
        old = store.resolve(doc.get('supersedes')) if doc.get('supersedes') is not None else None
        changed = store.widening(old, doc)
        if changed:
            wp = widening_review_problems(ref, store, None, reviewers_of(ref, store, everywhere=True),
                                          doc.get('author'), doc.get('supersedes'), changed, owner, predecessor=True)
            if wp:
                out = ['widening without a valid widening review: %s' % wp[0]]
    store._pred_cache[key] = out
    return out


def lint_chain(ref, store, owner, admitted_shas, predecessor=False):
    """Problems with one record's chain. ref = {path, blob_sha256}; admitted_shas: the blobs the configuration
    references (records, reviews, authorizations). Each authorization must count under "Owner at creation" (DI-1)
    on the store's owner timeline (a constant timeline of `owner` when the run has no host). With `predecessor`, the
    record is a predecessor named by a `supersedes` (DI-2): it need not be referenced, its review and authorization
    are found among the records of the object store at F, and its authorization counts as a completed action."""
    tl = store.timeline or OwnerTimeline.constant(owner)
    out = []
    doc = store.resolve(ref) if predecessor else store.get(ref)
    if doc is None:
        return ['record %s: blob not in the object store at its path' % ref.get('path')]
    pool = store.scanned() if predecessor else store.by_sha
    if not predecessor and ref['blob_sha256'] not in admitted_shas:
        out.append('record %s: not referenced by the configuration' % ref['path'])
    if doc.get('schema') not in record_schemas:
        out.append('record %s: unknown schema %r' % (ref['path'], doc.get('schema')))
    if 'supersedes' not in doc:
        out.append('record %s: no supersedes field' % ref['path'])
    if not predecessor:
        out += supersedes_problems(ref, doc, store, owner)
        if store.heads_problems:
            out += [p for p in store.heads_problems.get(ref['blob_sha256'], [])]
    author = doc.get('author')
    if not _person(author):
        out.append('record %s: author missing or not a person' % ref['path'])

    def usable(sha):
        return predecessor or sha in admitted_shas
    reviews = [(sha, path, d) for sha, (path, d) in pool.items()
               if isinstance(d, dict) and d.get('schema') == review_schema and usable(sha)
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
    auths = [d for sha, (path, d) in pool.items()
             if isinstance(d, dict) and d.get('schema') == auth_schema and usable(sha)]
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
            if not predecessor and a.get('owner') != owner:
                out.append('record %s: authorization owner differs from the configuration owner' % ref['path'])
                continue
            if not _owner(a.get('owner')) or not _comment(str(a.get('comment_id') or '')) or not a.get('time'):
                out.append('record %s: authorization lacks owner, time or comment id' % ref['path'])
                continue
            why = tl.authorization_problem(a, predecessor)
            if why:
                out.append('record %s: the authorization does not count under "Owner at creation": %s'
                           % (ref['path'], why))
                continue
            ok = True
    if not ok:
        out.append('record %s: no owner authorization listing the record and its review' % ref['path'])
    return out


def lineage_heads(refs, store):
    """DI-2, two heads: {blob sha: [problem]} for every record of a lineage that has two heads among the records the
    run reads (the records the configuration references and every record their `supersedes` chains name), a head being
    a record of the lineage that no other record the run reads supersedes."""
    read = {}
    for ref in refs:
        cur_ref, steps = ref, 0
        while isinstance(cur_ref, dict) and steps < 1000:
            d = store.resolve(cur_ref)
            if not isinstance(d, dict) or d.get('schema') not in record_schemas or \
                    cur_ref.get('blob_sha256') in read:
                break
            read[cur_ref.get('blob_sha256')] = (cur_ref, d)
            cur_ref, steps = d.get('supersedes'), steps + 1
    named = {d['supersedes'].get('blob_sha256') for _, d in read.values() if isinstance(d.get('supersedes'), dict)}
    groups = {}
    for sha, (r, d) in read.items():
        lid = lineage_id(d)
        if lid is not None and sha not in named:
            groups.setdefault((d.get('schema'), lid), []).append(r)
    out = {}
    for (schema, lid), heads in groups.items():
        if len(heads) > 1:
            for r in heads:
                out.setdefault(r.get('blob_sha256'), []).append(
                    'record %s: lineage %s has two heads among the records the run reads (%s)'
                    % (r.get('path'), lid, ', '.join(sorted(h.get('path') for h in heads))))
    # every record the configuration references in such a lineage fails, a head or not
    for ref in refs:
        d = store.resolve(ref)
        lid = lineage_id(d)
        if lid is not None and len(groups.get((d.get('schema'), lid), [])) > 1 and ref.get('blob_sha256') not in out:
            out[ref.get('blob_sha256')] = ['record %s: lineage %s has two heads among the records the run reads'
                                           % (ref.get('path'), lid)]
    return out


def widening_review_problems(ref, store, admitted_shas, regular_reviewers, author, old_ref, changed, owner,
                             predecessor=False):
    """Sec. 6.3 (B4): a review of kind widening naming the new blob and the blob it replaces, admitted, by a
    non-author reviewer other than the record's own reviewers, with an `accept` verdict for every changed item,
    and an owner authorization listing the widening review's blob, counted under "Owner at creation" (DI-1; for a
    predecessor named by a `supersedes`, as a completed action, and the widening review and its authorization found
    among the records of the object store at F). Returns [] when one such review exists."""
    tl = store.timeline or OwnerTimeline.constant(owner)
    pool = store.scanned() if predecessor else store.by_sha

    def usable(sha):
        return predecessor or sha in admitted_shas
    why = []
    for sha, (path, d) in sorted(pool.items()):
        if not isinstance(d, dict) or d.get('schema') != review_schema or d.get('kind') != 'widening':
            continue
        if not usable(sha) or d.get('reviewed', {}).get('blob_sha256') != ref['blob_sha256']:
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
        auth = any(isinstance(a, dict) and a.get('schema') == auth_schema and usable(s2) and
                   (predecessor or a.get('owner') == owner) and _owner(a.get('owner')) and a.get('comment_id') and
                   a.get('time') and tl.authorization_problem(a, predecessor) is None and
                   any((e.get('review') or {}).get('blob_sha256') == sha or
                       (e.get('record') or {}).get('blob_sha256') == sha for e in a.get('authorizes', []))
                   for s2, (_, a) in pool.items())
        if not auth:
            bad.append('no owner authorization that counts under "Owner at creation" lists the widening review')
        if not bad:
            return []
        why.append('widening review %s: %s' % (path, '; '.join(bad)))
    return why or ['no widening review names the superseding blob']


def widening_review_ok(ref, store, admitted_shas, regular_reviewers, author, old_ref=None, changed=(), owner=None):
    return not widening_review_problems(ref, store, admitted_shas, regular_reviewers, author, old_ref, changed, owner)


def reviewers_of(ref, store, everywhere=False):
    pool = store.scanned() if everywhere else store.by_sha
    return {d.get('reviewer') for sha, (p, d) in pool.items()
            if isinstance(d, dict) and d.get('schema') == review_schema and d.get('kind', 'review') == 'review'
            and d.get('reviewed', {}).get('blob_sha256') == ref['blob_sha256']}
