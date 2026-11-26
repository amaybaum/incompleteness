# design r6 as amended by amendments 3 and 4: R6.RECON.25, R6.RECON.26 (first kind of finding), R6.RECON.27
"""Category 3: the blocking state (Amendment 6 r13 R6.RECON.26-.27, .35, as the OBL-29 remedy r9 applies them).

Every run that evaluates M detects findings over the cumulative record set R* (R6.OBL29.1-.7): every tree reachable
through any parent from M, F and each record commit the run names, with a fixed selector, and the records the run
reads. Detection precedes lint (Form of a finding (i)): a first-kind finding is an invalidating reconciliation entry,
a second-kind finding an independent reviewer's invalidating verdict, a malformed finding a class (b) or (c) file
with an invalidation signal (R6.RECON.35). A finding blocks a run whose M contains one of its entry's
side_change_commits when it binds the run's configuration (Form (ii)-(v)); removing, rewriting, moving or superseding
a record never lifts it (R6.OBL29.6). A reassessment the configuration cites lifts the binding it names, for its edit,
when it applies; until custody exists none applies (sec. 2.2).
"""
import json
import re
import posixpath

from . import findings as fd
from . import outcome as oc
from . import records as rec
from . import util

reassessment_schema = 'oi-reassessment/1'
custody_unverified = ('the custody of the relevant historical inputs is not established (OBL-29 sec. 2.2): the cited '
                      'discharge is inapplicable')
blocked_class = 'retirement-blocked'

# The keys of one element of `invalidated` (R6.RECON.30 table `invalidated`; Form of a finding (ii)).
invalidated_keys = {'id': 'id', 'sha256': 'sha256', 'target': 'target'}
target_keys = {'path': 'path', 'start_H': 'start_H', 'old_sha256': 'old_sha256'}


def read_invalidated(x):
    """(edit id, sha256, target or None) of one element of `invalidated`; target is {path, start_H, old_sha256}."""
    if not isinstance(x, dict):
        return None, None, None
    k = invalidated_keys
    t = x.get(k['target']) if k['target'] else None
    target = None
    if isinstance(t, dict):
        target = {name: t.get(key) for name, key in target_keys.items()}
    return x.get(k['id']), x.get(k['sha256']), target


def _reviewed(store, ref, sha):
    """Problems of the record's review: exactly one review record in its directory naming its exact reference (path
    and blob; a review naming the same bytes at another path is not its review, which narrows the current-review
    check of R6.OBL29.4 in the fail-closed direction), and the chain lint with that review admitted."""
    d = posixpath.dirname(ref['path'])
    reviews = [s for s, (p, rv) in store.by_sha.items()
               if isinstance(rv, dict) and rv.get('schema') == rec.review_schema and posixpath.dirname(p) == d
               and isinstance(rv.get('reviewed'), dict) and rv['reviewed'].get('blob_sha256') == sha
               and rv['reviewed'].get('path') == ref['path']]
    if len(reviews) != 1:
        return ['%d review records in the record directory name its blob, not one' % len(reviews)]
    return rec.lint_chain(ref, store, {sha, reviews[0]})


def findings_of_records(records, schemas):
    """The first-kind findings among records the run reads explicitly (R6.OBL29.1), in the form of
    Cumulative.findings."""
    out = []
    for r in records:
        if r.get('schema') not in schemas:
            continue
        doc = {k: v for k, v in r.items() if k != '_ref'}
        form = fd.record_schema_problems(doc)
        for e in fd.first_kind_entries(doc):
            se = e.get('scientific_effect') or {}
            out.append({'kind': 1, 'record': r.get('_ref'), 'item': e.get('path'), 'entry': e,
                        'path': e.get('path') if isinstance(e.get('path'), str) else (r.get('_ref') or {}).get('path'),
                        'configuration': se.get('configuration'), 'invalidated': se.get('invalidated'),
                        'verdict_item': None, 'form': list(form)})
    return out


def unique(found):
    seen, out = set(), []
    for f in found:
        # a finding is identified by its record's reference (path and blob) and its entry path
        key = ((f['record'] or {}).get('path'), (f['record'] or {}).get('blob_sha256'), f.get('kind'),
               f.get('item', f['path']), f['path'])
        if key not in seen:
            seen.add(key)
            out.append(f)
    return out


def in_m(repo, M, commits):
    for c in commits:
        try:
            if isinstance(c, str) and repo.is_ancestor(c, M):
                return True
        except Exception:  # a commit the object store does not hold is not in M
            continue
    return False


def blocked_items(repo, H, M, blocked, dispositions):
    # one failing retirement-blocked item per blocking finding, obligation RET
    """One blocked item per blocking finding; the entry's path takes the disposition retirement-blocked when it differs
    between H and M, else the item is a run-level item naming the path."""
    items = []
    by_path = {d['path']: d for d in dispositions}
    for f, eid in blocked:
        path = f['path']
        differs = repo.blob_id(H, path) != repo.blob_id(M, path)
        fp = {'record': f['record'], 'path': path, 'edit': eid}
        if eid is not None and differs and path in by_path:
            by_path[path].update(disposition=blocked_class, finding=f['record'], edit=eid)
            items.append(oc.make_item('RET', blocked_class, path, None, fp, file=path,
                                      detail='a finding invalidates edit %s' % eid))
        else:
            items.append(oc.make_item('RET', blocked_class, path, None, dict(fp, run_level=True),
                                      detail=('a finding invalidates edit %s (run-level)' % eid) if eid is not None
                                      else 'a finding binds this configuration at run level (Form (iv))'))
    return items


def edit_sha(led, eid):
    raw = led.get('raw') or {}
    for e in raw.get('edits') or []:
        if isinstance(e, dict) and e.get('id') == eid:
            return util.sha256(util.canonical(e))
    return None


# R6.RECON.27. The design names the parts of `repair` (its commits, and the {path, blob_sha256} of the reconciliation
# record entry that records it) and of `edit` (the edit id and its canonical sha256) but not their keys; this is the
# one place that reads them.
reassessment_keys = {'repair_commits': ('repair', 'commits'), 'repair_entry': ('repair', 'entry'),
                     'edit_id': ('edit', 'id'), 'edit_sha256': ('edit', 'sha256')}


def _part(doc, name):
    a, b = reassessment_keys[name]
    v = doc.get(a)
    return v.get(b) if isinstance(v, dict) else None


def _first_parent_chain(repo, M):
    out, c = set(), M
    while c:
        out.add(c)
        ps = repo.parents(c)
        c = ps[0] if ps else None
    return out


def predecessor_review_problems(doc, ref, store, cum):
    """R6.OBL29.3 predecessor reviews: every required supersedes hop of the reassessment's existing lineage check
    (resolved by that check's own inputs); each exact predecessor's eligible ordinary reviews in R* accept every item,
    and, where the lineage requires a widening review, every widening review in R* of it accepts each verdict."""
    out = []
    # predecessor reviews: every required supersedes hop of the reassessment's existing lineage check (resolved
    # by that check's own inputs), each exact predecessor's eligible reviews in R*
    cur, seen = doc, {ref.get('blob_sha256')}
    while isinstance(cur, dict) and isinstance(cur.get('supersedes'), dict):
        pref = cur['supersedes']
        if pref.get('blob_sha256') in seen:
            break
        seen.add(pref.get('blob_sha256'))
        prev = store.resolve(pref)
        if not isinstance(prev, dict):
            break  # an unresolvable predecessor is the lineage check's own failure (record lint, above)
        out += ['predecessor %s: %s' % (pref.get('path'), x)
                for x in eligible_review_problems(cum.reviews_naming(pref), prev)]
        # include a widening review where the original check requires one: every widening review in R* of the
        # exact predecessor accepts each of its verdicts
        older = store.resolve(prev['supersedes']) if isinstance(prev.get('supersedes'), dict) else None
        changed = store.widening(older, prev) if store.widening is not None else []
        if changed:
            for wp, wv in cum.reviews_naming(pref):
                if isinstance(wv, dict) and wv.get('kind') == 'widening':
                    for x in rec.widening_verdict_problems(wv, changed):
                        out.append('predecessor %s: the widening review %s in the cumulative record set: %s'
                                   % (pref.get('path'), wp, x))
        cur = prev
    return out


REASSESS_FINDING = {'path': ('path', True), 'blob_sha256': ('sha256', True),
                    'item': (('or', ('null',), 'nestr'), True)}
REASSESS_ENTRY = {'path': ('path', True), 'blob_sha256': ('sha256', True), 'entry_path': ('path', True)}
REASSESS_REPAIR = {'commits': (('distinct_commits',), True), 'entry': (('table', REASSESS_ENTRY), True)}
REASSESS_EDIT = {'id': ('nestr', True), 'sha256': ('sha256', True)}
REASSESS_RECORD = {'schema': (('lit', (reassessment_schema,)), True), 'record_id': ('nestr', True),
                   'supersedes': (('or', ('null',), ('table', fd.REF)), True), 'author': ('identity', True),
                   'finding': (('table', REASSESS_FINDING), True),
                   'repair': (('or', ('null',), ('table', REASSESS_REPAIR)), True),
                   'edit': (('or', ('null',), ('table', REASSESS_EDIT)), True), 'rederivation': ('nestr', True),
                   'verdict': (('lit', ('no-effect',)), True)}


def keys_problems(doc):
    """R6.RECON.27 Keys and R6.RECON.32 tables: a key missing, of another type or outside the table is a form
    failure (the reassessment does not apply)."""
    out = []
    fd.validate(REASSESS_RECORD, doc, '$', out)
    return out


def finding_of(found, fref):
    """The findings `fref` = {path, blob_sha256, item} names (several where duplicated verdicts share an item)."""
    if not isinstance(fref, dict):
        return []
    return [f for f in found if (f['record'] or {}).get('path') == fref.get('path') and
            (f['record'] or {}).get('blob_sha256') == fref.get('blob_sha256') and f.get('item') == fref.get('item')]


def repair_null_admitted(f, cum):
    """Keys: `repair` is null only where no independent reviewer asserts the invalidation: (a) a first-kind finding
    whose entry has a non-author review rejecting or dissenting on <path>:scientific_effect (one must exist; counted
    over R*); (b) a review whose reviewed names no record the scan finds; (c) a malformed file."""
    if f['kind'] == 'malformed':
        return True
    if f['kind'] == 2:
        return f.get('entry') is None and any('names no record the scan finds' in x for x in f.get('form') or [])
    item = '%s:scientific_effect' % f.get('item')
    rdoc = cum.record_at(f['record']) if cum is not None else None
    author = (rdoc or {}).get('author')
    for _p, rv in (cum.reviews_naming(f['record']) if cum is not None else []):
        if not isinstance(rv, dict) or rv.get('kind', 'review') != 'review' or fd.same_identity(rv.get('reviewer'),
                                                                                                author):
            continue
        for v in rv.get('verdicts') or []:
            if isinstance(v, dict) and v.get('item') == item and v.get('verdict') in ('reject', 'dissent'):
                return True
    return False


def reassessment_problems(repo, M, led, doc, ref, store, admitted, found, m_scan, schemas, cum=None,
                          run_level=lambda f: False):
    """Why a cited reassessment does not apply (empty if it applies). m_scan: [(path, bytes)], the scanned set of M's
    tree; `found`: the findings of the cumulative record set; `cum`: that set, whose eligible reviews of the
    reassessment and of its repair record must all accept (R6.OBL29.3); run_level(finding): whether it binds the
    citing configuration at run level (Form (iv); `edit` is null exactly then)."""
    out = []
    if not isinstance(doc, dict) or doc.get('schema') != reassessment_schema:
        return ['not a reassessment record']
    out += ['a form failure of its keys: %s' % x for x in keys_problems(doc)]
    out += rec.lint_chain(ref, store, admitted)
    if out:
        return out + [custody_unverified]
    reviewers = {rv.get('reviewer') for _s, (_p, rv) in store.by_sha.items()
                 if isinstance(rv, dict) and rv.get('schema') == rec.review_schema
                 and isinstance(rv.get('reviewed'), dict) and rv['reviewed'].get('blob_sha256') == ref['blob_sha256']}
    named = finding_of(found, doc.get('finding'))
    if not named:
        out.append('the named finding is not a finding in the cumulative record set')
    if doc.get('repair') is None:
        if not named or not all(repair_null_admitted(f, cum) for f in named):
            out.append('repair is null where an independent reviewer asserts the invalidation (Keys)')
        entry = edoc = None
    else:
        commits = _part(doc, 'repair_commits')
        chain = _first_parent_chain(repo, M)
        if not (isinstance(commits, list) and commits and all(isinstance(c, str) and c in chain for c in commits)):
            out.append("the repair's commits do not lie on M's first-parent chain")
        entry = _part(doc, 'repair_entry')
        m_store = rec.Store(m_scan)
        eref = {'path': entry.get('path'), 'blob_sha256': entry.get('blob_sha256')} if isinstance(entry, dict) else None
        edoc = m_store.get(eref) if eref else None
        if not isinstance(edoc, dict) or edoc.get('schema') not in schemas:
            out.append("the repair's reconciliation record entry is not present at M")
        else:
            if not any(isinstance(e, dict) and e.get('path') == entry.get('entry_path') for e in edoc.get('paths') or []):
                out.append("the repair's reconciliation record has no entry for entry_path")
            if _reviewed(m_store, eref, eref['blob_sha256']):
                out.append("the repair's reconciliation record entry has no accepting non-author review")
            if edoc.get('author') in reviewers:
                out.append("the reviewer is the author of the repair's reconciliation record entry")
        entry = eref
    rl = bool(named) and all(run_level(f) for f in named)
    if rl and doc.get('edit') is not None:
        out.append('edit is not null for a finding bound at run level (Keys)')
    if not rl and doc.get('edit') is None:
        out.append('edit is null for a finding not bound at run level (Keys)')
    if cum is not None:
        # R6.OBL29.3: every eligible ordinary review in R* of the reassessment's exact reference, and of the repair
        # record's exact reference within its own directory, accepts every item; historical review evidence never
        # supplies the current accepting review (R6.OBL29.4, above)
        out += eligible_review_problems(cum.reviews_naming(ref), doc)
        out += predecessor_review_problems(doc, ref, store, cum)
        if isinstance(entry, dict) and isinstance(edoc, dict):
            out += eligible_review_problems(cum.reviews_naming(entry, posixpath.dirname(entry.get('path') or '')),
                                            edoc)
    if not (isinstance(doc.get('rederivation'), str) and doc['rederivation'].strip()):
        out.append('the rederivation is empty')
    if doc.get('verdict') != 'no-effect':
        out.append('the verdict is not no-effect')
    eid, esha = _part(doc, 'edit_id'), _part(doc, 'edit_sha256')
    if doc.get('edit') is not None and (eid is None or edit_sha(led, eid) is None or edit_sha(led, eid) != esha):
        out.append("the edit is not an edit of the citing configuration's ledger as worded")
    # OBL-29 remedy r9 sec. 2.2, Custody and lookup: before an applying discharge is returned, the custody starting
    # point and its coverage for the repair under consideration are verified; missing required custody leaves the
    # cited discharge inapplicable (FAIL record-invalid and retirement-blocked). The custody format, bootstrap record
    # and mapping to admitted inputs are not yet fixed and independently verified, so no custody can be established
    # and every cited discharge fails closed here, whatever else holds.
    out.append(custody_unverified)
    return out


def lifting(reassessments):
    """lifted(finding, edit id) over the reassessments that apply: [(doc, ref)]."""
    def lifted(f, eid):
        # Keys: a reassessment lifts only the finding it names (path, blob and item), for its edit only; edit null
        # lifts a run-level binding
        fr = f['record'] or {}
        return any(isinstance(d.get('finding'), dict) and d['finding'].get('path') == fr.get('path')
                   and d['finding'].get('blob_sha256') == fr.get('blob_sha256')
                   and d['finding'].get('item', f.get('item')) == f.get('item')
                   and ((eid is None and d.get('edit') is None) or (eid is not None and _part(d, 'edit_id') == eid))
                   for d, _r in reassessments)
    return lifted


# ---- the cumulative record set R* (OBL-29 remedy r9, R6.OBL29.1-.8) ---------------------------------------------

class Cumulative:
    """R*: the regular-file entries under the fixed category-3 prefix in every tree reachable through any parent from
    the roots (R6.OBL29.1, .7). One walk through the verified reader visits each commit once, keyed by full id, until
    no unvisited parent remains; parents are read only from verified commit content (no ref, reflog, replace ref,
    graft, shallow file or commit-graph). A commit, tree or blob the walk needs that the store lacks or that does not
    hash to its id raises the reader's Unresolvable (ERROR, no verdict). There is no depth or count limit.

    Selection is fixed (R6.OBL29.5): the prefix, the regular mode and the file's bytes; no tool-landing or plan
    directory exclusion. Each distinct blob is classified once by R6.RECON.35 (findings.classify): class (a)
    reconciliation and review records, and malformed class (b) and (c) files, are kept. Detection follows Form (i)
    ("detection precedes lint"): a first-kind finding is an invalidating entry of a class (a) reconciliation record,
    whatever its review says; a second-kind finding is an invalidating verdict entry of a class (a) review whose
    reviewer is independent of the reviewed record's author; a class (b) or (c) file with an invalidation signal is a
    malformed finding (R6.OBL29.2). Each is decided from the one file and the reviewed record it names, so detection
    is monotone: adding history only adds findings.
    """

    def __init__(self, repo, roots, schemas, prefix):
        self.repo, self.schemas, self.prefix = repo, schemas, prefix
        self.visited = []
        self.holders = {}
        self.subtrees = {}
        cache = repo.__dict__.setdefault('_c3_keep', {})
        ckey = (id(repo), tuple(schemas))
        keep = cache.get(ckey)
        if keep is None:
            info = {}
            classify = self._classify

            def keep(oid):
                if oid not in info:
                    info[oid] = classify(repo.read_blob_uncached(oid))
                return info[oid] is not None
            keep.info = info
            cache[ckey] = keep
        self.keep = keep
        self.info = keep.info
        seen, stack = set(), [r for r in roots if r]
        while stack:
            c = stack.pop()
            if c in seen:
                continue
            seen.add(c)
            self.visited.append(c)
            ps = repo.parents(c)
            key, ents = repo.prefix_entries(c, prefix, keep)
            if key is not None and key not in self.subtrees:
                self.subtrees[key] = ents
            for p, _m, o in ents:
                if self.info[o][3]:
                    self.holders.setdefault((p, o), set()).add(c)
            stack.extend(ps)

    def _classify(self, data):
        """(class, schema or signal, sha256, carries a finding, reviewed path, reviewed sha256), or None."""
        got = fd.classify(data)
        if got is None:
            return None
        sha = util.sha256(data)
        if got[0] in ('b', 'c'):
            return (got[0], got[1], sha, bool(got[1]), None, None)
        doc = fd.strict_parse(data)
        if got[1] == fd.review_schema:
            rv = doc.get('reviewed') if isinstance(doc.get('reviewed'), dict) else {}
            return ('a', got[1], sha, bool(fd.second_kind_verdicts(doc)), rv.get('path'), rv.get('blob_sha256'))
        return ('a', got[1], sha, bool(fd.first_kind_entries(doc)), None, None)

    def entries(self):
        """The distinct (path, blob id) entries of R*."""
        out = set()
        for ents in self.subtrees.values():
            for p, _m, o in ents:
                out.add((p, o))
        return sorted(out)

    def record_at(self, ref):
        """The class (a) reconciliation record of R* at exactly {path, blob_sha256}: its parsed content, or None."""
        if getattr(self, '_recon_index', None) is None:
            self._recon_index = {}
            for p, o in self.entries():
                inf = self.info[o]
                if inf[0] == 'a' and inf[1] in fd.recon_schemas:
                    self._recon_index.setdefault((p, inf[2]), o)
        o = self._recon_index.get((ref.get('path'), ref.get('blob_sha256'))) if isinstance(ref, dict) else None
        return fd.strict_parse(self.repo.read_blob_uncached(o)) if o is not None else None

    def findings(self):
        """Every finding of R* (Form (i), R6.RECON.35, R6.OBL29.2), one per carrying file reference and item:
        {kind (1, 2 or 'malformed'), record, item, entry, path, configuration, invalidated, verdict_item, form}.
        `entry` is the reconciliation entry the finding names, or None where the scan finds none."""
        out = []
        for p, o in self.entries():
            inf = self.info[o]
            if not inf[3]:
                continue
            ref = {'path': p, 'blob_sha256': inf[2]}
            data = self.repo.read_blob_uncached(o)
            if inf[0] in ('b', 'c'):
                out.append({'kind': 'malformed', 'record': ref, 'item': None, 'entry': None, 'path': p,
                            'configuration': None, 'invalidated': None, 'verdict_item': None,
                            'form': ['a malformed record of R6.RECON.35 class (%s)' % inf[0]]})
                continue
            doc = fd.strict_parse(data)
            if inf[1] in fd.recon_schemas:
                form = fd.record_schema_problems(doc)
                for e in fd.first_kind_entries(doc):
                    se = e.get('scientific_effect') or {}
                    out.append({'kind': 1, 'record': ref, 'item': e.get('path'), 'entry': e,
                                'path': e.get('path') if isinstance(e.get('path'), str) else p,
                                'configuration': se.get('configuration'), 'invalidated': se.get('invalidated'),
                                'verdict_item': None, 'form': list(form)})
                continue
            reviewed = self.record_at(doc.get('reviewed'))
            who = doc.get('reviewer')
            if isinstance(reviewed, dict) and fd.same_identity(who, reviewed.get('author')):
                continue  # an independence failure disqualifies the review (Form (i))
            if fd.run_like(who):
                continue
            for v in fd.second_kind_verdicts(doc):
                form = fd.second_kind_form_problems(doc, reviewed, v)
                if reviewed is None:
                    form.append('its reviewed names no record the scan finds')
                entry = fd.entry_of_item(reviewed, v.get('item')) if isinstance(reviewed, dict) else None
                out.append({'kind': 2, 'record': ref, 'item': v.get('item'), 'entry': entry,
                            'path': entry.get('path') if isinstance(entry, dict) else p,
                            'configuration': v.get('configuration'), 'invalidated': v.get('invalidated'),
                            'verdict_item': v.get('item'), 'form': form})
        return unique(out)

    def reviews_naming(self, ref, directory=None):
        """[(path, doc)] of every review record in R* whose `reviewed` names `ref` exactly (path and blob), only in
        `directory` when one is given."""
        out = []
        for p, o in self.entries():
            inf = self.info[o]
            if inf[0] != 'a' or inf[1] != fd.review_schema or inf[4] != ref.get('path') or \
                    inf[5] != ref.get('blob_sha256'):
                continue
            if directory is not None and posixpath.dirname(p) != directory:
                continue
            doc = fd.strict_parse(self.repo.read_blob_uncached(o))
            if doc is not None:
                out.append((p, doc))
        return out

    def malformed_at(self, commit, excluded):
        """The class (b) and (c) files without an invalidation signal in one tree, outside `excluded(path)`: the
        ordinary malformed-nonfinding lint of the current snapshot (R6.OBL29.2, R6.RECON.35)."""
        key, ents = self.repo.prefix_entries(commit, self.prefix, self.keep)
        return sorted(p for p, _m, o in ents if self.info[o][0] in ('b', 'c') and not self.info[o][3]
                      and not excluded(p))

    def witness(self, ref, M, rev, F):
        """(present_at_M, witness) of a finding's record reference (R6.OBL29.8): present_at_M when M's tree holds
        its path and blob at a regular mode; the witness chosen from M, REV, F, then the newest commit on M's
        first-parent chain, then the smallest full id among the other commits that supply it."""
        holders = set()
        for (p, o), cs in self.holders.items():
            if p == ref.get('path') and self.info[o][2] == ref.get('blob_sha256'):
                holders |= cs
        present = M in holders
        for c in [M] + sorted(rev or []) + [F]:
            if c and c in holders:
                return present, c
        c = M
        while c:
            if c in holders:
                return present, c
            ps = self.repo.parents(c)
            c = ps[0] if ps else None
        return present, (min(holders) if holders else None)


def eligible_review_problems(reviews, doc):
    """R6.OBL29.3 direct review checks over R*: every eligible ordinary review of the record's exact reference (kind
    review; reviewer a person other than the record's author) accepts every item id of the record exactly once and
    carries no dissent. A review whose verdict is not accept, that omits or duplicates an item, or that dissents fails
    the discharge even if it has left the current tree."""
    out = []
    ids = rec.item_ids(doc) if isinstance(doc, dict) else []
    author = doc.get('author') if isinstance(doc, dict) else None
    for path, rv in reviews:
        if not isinstance(rv, dict) or rv.get('kind', 'review') != 'review':
            continue
        who = rv.get('reviewer')
        if not rec._person(who) or who == author:
            continue
        named = [v.get('item') for v in rv.get('verdicts') or [] if isinstance(v, dict)]
        verdicts = {v.get('item'): v.get('verdict') for v in rv.get('verdicts') or [] if isinstance(v, dict)}
        bad = []
        if len(named) != len(set(named)):
            bad.append('an item has more than one verdict')
        if set(ids) - set(verdicts):
            bad.append('an item is omitted')
        if any(verdicts.get(i) != 'accept' for i in ids):
            bad.append('an item is not accepted')
        if isinstance(rv.get('dissent'), str) and rv['dissent'].strip():
            bad.append('it dissents')
        if bad:
            out.append('the review %s in the cumulative record set: %s' % (path, '; '.join(bad)))
    return out


# ---- the binding of a finding (R6.RECON.26, Form of a finding (ii)-(v)) -------------------------------------------

class Binding:
    """The run's view for binding: its reader, M, configuration (doc and reference) and ledger, and two callbacks
    the CLI supplies: resolve_cfg(ref) -> (doc, commit) or None (R6.RECON.33 resolution), and ledger_of(ref, commit)
    -> the configuration's ledger (raises findings.Unsettled when it cannot be read)."""

    def __init__(self, repo, M, cfg, cfg_ref, led, resolve_cfg, ledger_of):
        self.repo, self.M, self.cfg, self.cfg_ref, self.led = repo, M, cfg, cfg_ref, led
        self.resolve_cfg, self.ledger_of = resolve_cfg, ledger_of
        self._ledgers = {}
        if any(isinstance(r, dict) and r.get('kind') == 'edit-id-migration' for r in cfg.get('records') or []):
            # Form (iv)-(vi) follow R6.RECON.28 migrations, which this tool revision does not read; a configuration
            # that references one cannot be bound faithfully
            raise fd.Unsettled('the configuration references an edit-id-migration record (R6.RECON.28), which this '
                               'tool revision does not implement')

    def finding_config(self, cref):
        """(doc, ledger, H) of the configuration a finding names, or None when it is absent or does not resolve."""
        if not (isinstance(cref, dict) and isinstance(cref.get('path'), str) and
                isinstance(cref.get('blob_sha256'), str)):
            return None
        key = (cref['path'], cref['blob_sha256'])
        if key == (self.cfg_ref['path'], self.cfg_ref['blob_sha256']):
            return self.cfg, self.led, self.cfg['roles']['scientific_base']
        if key not in self._ledgers:
            got = self.resolve_cfg(cref)
            if got is None:
                self._ledgers[key] = None
            else:
                doc, commit = got
                self._ledgers[key] = (doc, self.ledger_of(cref, commit),
                                      (doc.get('roles') or {}).get('scientific_base'))
        return self._ledgers[key]

    def in_lineage(self, fdoc, fref):
        """R6.RECON.33 plan lineage of the finding's configuration: the run's configuration lies on whose supersedes
        chain (itself included) the finding's configuration lies, or names the same retirement by name or Issue."""
        ra, rb = self.cfg.get('retirement') or {}, (fdoc or {}).get('retirement') or {}
        if (ra.get('name') is not None and ra.get('name') == rb.get('name')) or \
                (ra.get('issue') is not None and ra.get('issue') == rb.get('issue')):
            return True
        cur, ref, seen = self.cfg, dict(self.cfg_ref), set()
        while isinstance(cur, dict):
            if (ref.get('path'), ref.get('blob_sha256')) == (fref.get('path'), fref.get('blob_sha256')):
                return True
            sup = cur.get('supersedes')
            if not isinstance(sup, dict) or (sup.get('path'), sup.get('blob_sha256')) in seen:
                return False
            seen.add((sup.get('path'), sup.get('blob_sha256')))
            got = self.resolve_cfg(sup)
            cur, ref = (got[0] if got else None), sup
        return False


def _edits(led):
    return {e.get('id'): e for e in ((led or {}).get('raw') or {}).get('edits') or [] if isinstance(e, dict)}


def expected_target(repo, led, H, eid):
    """Form (ii): the target of edit `eid` at that configuration's H: its splice's file, start and old_sha256, or a
    retained edit's file, the start of its text at H and the sha256 of the text."""
    sps = [s for s in (led or {}).get('splices') or [] if s.get('id') == eid]
    if len(sps) == 1:
        return {'path': sps[0].get('file'), 'start_H': sps[0].get('start'), 'old_sha256': sps[0].get('old_sha256')}
    if len(sps) > 1:
        raise fd.Unsettled('Form (ii): edit %s has %d splices; the design names one target per edit' % (eid, len(sps)))
    ret = [r for r in (led or {}).get('retained') or [] if isinstance(r, dict) and r.get('id') == eid]
    if len(ret) == 1 and isinstance(ret[0].get('text'), str) and isinstance(ret[0].get('file'), str):
        text = ret[0]['text'].encode('utf-8')
        data = repo.read(H, ret[0]['file']) if H else None
        hits = [] if data is None else [m.start() for m in re.finditer(re.escape(text), data)]
        if len(hits) != 1:
            raise fd.Unsettled('Form (ii): the text of retained edit %s occurs %d times at H; "the start of its text at '
                               'H" names one start' % (eid, len(hits)))
        return {'path': ret[0]['file'], 'start_H': hits[0], 'old_sha256': util.sha256(text)}
    if eid in _edits(led):
        raise fd.Unsettled('Form (ii): edit %s has neither a splice of its id nor a retained entry' % eid)
    return None


def bind(f, b):
    """(bound edit ids, run_level, form problems) of one finding for the run's configuration (Form (ii)-(v))."""
    form = list(f.get('form') or [])
    entry = f.get('entry')
    got = b.finding_config(f.get('configuration'))
    unresolved = got is None
    if unresolved:
        form.append('its configuration is absent or cannot be resolved (Form (iii))')
        fdoc = fled = fH = None
        lineage = False
    else:
        fdoc, fled, fH = got
        lineage = b.in_lineage(fdoc, f['configuration'])
    run_edits = _edits(b.led)
    global_scope = unresolved
    elems = []
    inv = f.get('invalidated')
    usable = isinstance(inv, list) and bool(inv) and \
        (f['kind'] == 1 or (isinstance(f.get('verdict_item'), str) and f['verdict_item'].endswith(':scientific_effect')))
    if usable:
        for x in inv:
            if not fd.element_ok(x):
                form.append('an invalidated element lacks a key or has another type (Form (ii))')
                global_scope = True
                if isinstance(x, dict):
                    elems.append((x.get('id'), x.get('target') if isinstance(x.get('target'), dict) else None))
                continue
            elems.append((x['id'], x['target']))
            if not unresolved:
                e = _edits(fled).get(x['id'])
                if e is None or util.sha256(util.canonical(e)) != x['sha256'] or \
                        expected_target(b.repo, fled, fH, x['id']) != x['target']:
                    form.append('invalidated element %s differs from the named configuration\'s ledger (Form (ii))'
                                % x['id'])
                    global_scope = True
    bound = []

    def carry_id(eid, path):
        if not isinstance(eid, str) or eid not in run_edits:
            return False
        if lineage or global_scope:
            return True
        return path is not None and run_edits[eid].get('file') == path

    if usable:
        for eid, tgt in elems:
            path = (tgt or {}).get('path')
            if carry_id(eid, path):
                bound.append(eid)
                continue
            if isinstance(tgt, dict) and tgt.get('path') and tgt.get('old_sha256'):
                for s in b.led.get('splices') or []:
                    if s.get('file') == tgt['path'] and s.get('old_sha256') == tgt['old_sha256']:
                        bound.append(s.get('id'))
                        break
                else:
                    for r in b.led.get('retained') or []:
                        if isinstance(r, dict) and r.get('file') == tgt['path'] and isinstance(r.get('text'), str) \
                                and util.sha256(r['text'].encode('utf-8')) == tgt['old_sha256']:
                            bound.append(r.get('id'))
                            break
        return sorted(set(x for x in bound if x)), False, form
    # Form (iv) fallback: the entry's conclusions, or every edit of the entry's path
    if entry is None:
        return [], True, form
    se = entry.get('scientific_effect') if isinstance(entry.get('scientific_effect'), dict) else {}
    concl = se.get('conclusions')
    if isinstance(concl, list) and concl:
        named = [(c, (_edits(fled).get(c) or {}).get('file')) for c in concl if isinstance(c, str)]
    elif unresolved:
        # every edit of the entry's path, read from a configuration that does not resolve: every configuration whose
        # ledger carries an edit of that path is bound (Form (iii) scope)
        named = [(eid, entry.get('path')) for eid, e in run_edits.items() if e.get('file') == entry.get('path')]
    else:
        named = [(eid, e.get('file')) for eid, e in _edits(fled).items() if e.get('file') == entry.get('path')]
    if not named:
        return [], (lineage or unresolved), form
    for eid, path in named:
        if carry_id(eid, path):
            bound.append(eid)
    return sorted(set(bound)), False, form
