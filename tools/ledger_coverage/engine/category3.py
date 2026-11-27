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


def second_kind_findings(doc, ref, record_at):
    """Form (i) second-kind findings of one review record (its reference `ref`); record_at(reference) returns the
    reconciliation record the review names, or None when the scan finds none."""
    reviewed = record_at(doc.get('reviewed'))
    who = doc.get('reviewer')
    if isinstance(reviewed, dict) and fd.same_identity(who, reviewed.get('author')):
        return []  # an independence failure disqualifies the review (Form (i))
    if fd.run_like(who):
        return []
    out = []
    for v in fd.second_kind_verdicts(doc):
        form = fd.second_kind_form_problems(doc, reviewed, v)
        if reviewed is None:
            form.append('its reviewed names no record the scan finds')
        entry = fd.entry_of_item(reviewed, v.get('item')) if isinstance(reviewed, dict) else None
        out.append({'kind': 2, 'record': ref, 'item': v.get('item'), 'entry': entry,
                    'path': entry.get('path') if isinstance(entry, dict) else ref.get('path'),
                    'configuration': v.get('configuration'), 'invalidated': v.get('invalidated'),
                    'verdict_item': v.get('item'), 'form': form})
    return out


def findings_of_records(records, schemas, record_at=lambda ref: None):
    """The first-kind findings among records the run reads explicitly (R6.OBL29.1), in the form of
    Cumulative.findings."""
    out = []
    for r in records:
        doc = {k: v for k, v in r.items() if k not in ('_ref', '_source')}
        if r.get('schema') == fd.review_schema:
            # an explicitly read review record carries second-kind findings like a scanned one
            out += second_kind_findings(doc, r.get('_ref') or {}, record_at)
            continue
        if r.get('schema') not in schemas:
            continue
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


def custody_problems(custody):
    """The custody conditions a cited discharge fails: none when custody is established (R6.CUST.7), each custody-*
    failure otherwise; without a custody check (no report) the discharge fails closed."""
    if custody is None:
        return [custody_unverified]
    if custody.get('status') == 'established':
        return []
    return ['%s: %s' % (p['item'], p['why']) for p in custody.get('problems') or []] or [custody_unverified]


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
                          run_level=lambda f: False, custody=None):
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
        return out + custody_problems(custody)
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
    # R6.CUST.7 (OBL-29 custody c7): before an applying discharge is returned, custody must be established at
    # effective M; any custody failure makes every cited discharge inapplicable (R6.CUST.9, global to the run)
    out += custody_problems(custody)
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
        self.first_seen = {}
        self.roots = [r for r in roots if r]
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
                self.first_seen.setdefault((p, o), c)
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

    explicit_record_at = None

    def resolve_reviewed(self, ref):
        """The record a second-kind review names, by exact reference, in the run's whole R*: the walk's record set, or a
        record the run reads explicitly (`explicit_record_at`, set by the run). r9 Amendment 1 A1.4 and A1.5: a record
        seen through F, REV or an explicit input resolves a provisional block for the runs that reach it."""
        got = self.record_at(ref)
        if got is None and self.explicit_record_at is not None:
            got = self.explicit_record_at(ref)
        return got

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
                out.append({'kind': 'malformed', 'class': inf[0], 'record': ref, 'item': None, 'entry': None, 'path': p,
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
            out += second_kind_findings(doc, ref, self.resolve_reviewed)
        return unique(out)

    def git_id(self, ref):
        """The git blob id of the R* entry at exactly {path, blob_sha256}, or None."""
        for p, o in self.entries():
            if isinstance(ref, dict) and p == ref.get('path') and self.info[o][2] == ref.get('blob_sha256'):
                return o
        return None

    def reviews_naming_ids(self, ref, directory=None):
        """As reviews_naming, as [(path, git blob id, doc)]."""
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
                out.append((p, o, doc))
        return out

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

    def read_domain(self, explicit=()):
        """The category-3 read domain (OBL-29 r9 sec. 5.3): the roots of the walk, and for each record the scan read
        from a tree, the commit it was first read from (a root or a commit of its verified history), its path and its
        blob; and each explicitly read record with its admitted source."""
        return {'prefix': self.prefix, 'roots': list(self.roots),
                'reads': [{'commit': c, 'path': p, 'blob_sha256': self.info[o][2]}
                          for (p, o), c in sorted(self.first_seen.items())],
                'explicit': [dict(x) for x in explicit]}

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

    def __init__(self, repo, M, cfg, cfg_ref, led, resolve_cfg, ledger_of, record_at=None, cfg_commit=None):
        self.repo, self.M, self.cfg, self.cfg_ref, self.led = repo, M, cfg, cfg_ref, led
        self.resolve_cfg, self.ledger_of, self.record_at, self.cfg_commit = resolve_cfg, ledger_of, record_at, cfg_commit
        self._commit_of = {}
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
                self._commit_of[id(doc)] = commit
                self._ledgers[key] = (doc, self.ledger_of(cref, commit),
                                      (doc.get('roles') or {}).get('scientific_base'))
        return self._ledgers[key]

    def delegated_paths(self, fdoc):
        """The paths of the delegation classes of a configuration (R6.RECON.30 executed paths), read at its commit;
        an unreadable delegation contract stops the run (the floor cannot be decided)."""
        dref = fdoc.get('delegation')
        if not isinstance(dref, dict):
            return set()
        commit = self.cfg_commit if fdoc is self.cfg else self._commit_of.get(id(fdoc))
        data = self.repo.read(commit, dref.get('path')) if commit else None
        try:
            doc = json.loads(data.decode('utf-8'))
        except (AttributeError, ValueError, UnicodeDecodeError):
            # an in-scope reading of the owner's decision of 2026-11-27 (ledger-unreadable and ledger-target stops
            # bind at run level): the contract's object reads (an unreadable object stays ERROR), only its content
            # is unusable, so the named configuration's binding inputs cannot be read
            raise fd.RunLevelBlock('R6.RECON.30 executed paths: the delegation contract of the named configuration '
                                   'cannot be read')
        return {q for c in doc.get('classes') or [] if isinstance(c, dict) for q in c.get('paths') or []
                if isinstance(q, str)}

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
        raise fd.RunLevelBlock('Form (ii): edit %s has %d splices in the named configuration\'s ledger; one target per '
                               'edit is required' % (eid, len(sps)))
    ret = [r for r in (led or {}).get('retained') or [] if isinstance(r, dict) and r.get('id') == eid]
    if len(ret) == 1 and isinstance(ret[0].get('text'), str) and isinstance(ret[0].get('file'), str):
        text = ret[0]['text'].encode('utf-8')
        data = repo.read(H, ret[0]['file']) if H else None
        hits = [] if data is None else [m.start() for m in re.finditer(re.escape(text), data)]
        if len(hits) != 1:
            raise fd.RunLevelBlock('Form (ii): the text of retained edit %s occurs %d times at H; "the start of its '
                                   'text at H" names one start' % (eid, len(hits)))
        return {'path': ret[0]['file'], 'start_H': hits[0], 'old_sha256': util.sha256(text)}
    if eid in _edits(led):
        raise fd.RunLevelBlock('Form (ii): edit %s has neither a splice of its id nor a retained entry' % eid)
    return None


def beside_table_problems(b, f, fled, fH, fdoc):
    """The checks R6.RECON.30 makes beside its key tables, on the finding's reconciliation record: each entry's
    splices are exactly the named configuration's ledger splices of the path, in order, with their start_H and end_H;
    end_M = start_M + end_H - start_H; the translation agrees with the offsets (R6.RECON.10: identity requires
    start_M = start and H and M equal up to the splice's end; an integer equals start_M - start); and, for an executed
    path (a floor or configured suffix, or a delegated path), `method` names the entry's l blob id."""
    rdoc = b.record_at(f['record']) if b.record_at else None
    if not isinstance(rdoc, dict):
        return []
    out = []
    suffixes = tuple(set(fd.executed_floor) | set((fdoc or {}).get('executed_suffixes') or []))
    delegated = b.delegated_paths(fdoc) if fdoc is not None else set()
    for e in rdoc.get('paths') or []:
        if not isinstance(e, dict) or not isinstance(e.get('path'), str):
            continue
        path = e['path']
        sps = e.get('splices') if isinstance(e.get('splices'), list) else []
        if fled is not None:
            want = [s_ for s_ in fled.get('splices') or [] if s_.get('file') == path]
            if [x.get('id') for x in sps if isinstance(x, dict)] != [x.get('id') for x in want]:
                out.append('%s: its splices are not the ledger\'s splices of the path in ledger order' % path)
            else:
                for x, w_ in zip(sps, want):
                    if x.get('start_H') != w_.get('start') or x.get('end_H') != w_.get('end'):
                        out.append('%s: splice %s offsets differ from the ledger\'s' % (path, x.get('id')))
        for x in sps:
            if not isinstance(x, dict):
                continue
            if all(type(x.get(k)) is int for k in ('start_M', 'end_M', 'start_H', 'end_H')) and \
                    x['end_M'] != x['start_M'] + x['end_H'] - x['start_H']:
                out.append('%s: splice %s end_M is not start_M + end_H - start_H' % (path, x.get('id')))
            t = x.get('translation')
            if type(t) is int and type(x.get('start_M')) is int and type(x.get('start_H')) is int and \
                    t != x['start_M'] - x['start_H']:
                out.append('%s: splice %s translation disagrees with its offsets' % (path, x.get('id')))
            if t == 'identity':
                if x.get('start_M') != x.get('start_H'):
                    out.append('%s: splice %s translation identity with start_M != start' % (path, x.get('id')))
                else:
                    # H and M as the record states them (ledger_base, M): the record's own claim of prefix agreement
                    hb = b.repo.read(rdoc.get('ledger_base'), path) if isinstance(rdoc.get('ledger_base'), str) else None
                    mb = b.repo.read(rdoc.get('M'), path) if isinstance(rdoc.get('M'), str) else None
                    end = x.get('end_H') if type(x.get('end_H')) is int else -1
                    if hb is None or mb is None or end < 0 or hb[:end] != mb[:end]:
                        out.append('%s: splice %s translation identity without prefix agreement of H and M'
                                   % (path, x.get('id')))
        if path.endswith(suffixes) or path in delegated:
            if not (isinstance(e.get('l'), str) and isinstance((e.get('scientific_effect') or {}).get('method'), str)
                    and e['l'] in e['scientific_effect']['method']):
                out.append('%s: an executed path whose method does not name its l blob id' % path)
    return out


def bind(f, b):
    """(bound edit ids, run_level, form problems) of one finding for the run's configuration (Form (ii)-(v)). A finding
    whose binding cannot be decided from readable inputs (findings.RunLevelBlock) binds at run level, with the reason
    as a form failure (FAIL record-invalid)."""
    try:
        return _bind(f, b)
    except fd.RunLevelBlock as exc:
        return [], True, list(f.get('form') or []) + ['%s; the finding binds at run level' % exc]


def _bind(f, b):
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
    if f['kind'] == 1:
        beside = beside_table_problems(b, f, fled, fH, fdoc)
        if beside:
            # a failure of the record's form beside its tables (R6.RECON.30): a malformed finding, which blocks at run
            # level with FAIL record-invalid (owner decision 5 of 2026-11-27)
            return [], True, form + ['beside its tables (R6.RECON.30): %s' % x for x in beside]
    elems = []
    inv = f.get('invalidated')
    # Form (iv): `invalidated` absent, empty or unreadable (no element is a readable {id, sha256, target}), or the
    # verdict on another item than <path>:scientific_effect, falls back to the conclusions or the entry's path
    usable = isinstance(inv, list) and any(fd.element_ok(x) for x in inv) and \
        (f['kind'] == 1 or (isinstance(f.get('verdict_item'), str) and f['verdict_item'].endswith(':scientific_effect')))
    if isinstance(inv, list) and inv and not usable:
        form.append('invalidated has no readable element (Form (ii)); bound through the Form (iv) fallback')
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
    # Form (iv) fallback: the entry's conclusions, or every edit of the entry's path. Elements that carry an id but
    # lack another key "block through the fallback of (iii)" (Form (ii)): the id match is then global, and those ids
    # are bound as well
    partial = [x.get('id') for x in (inv if isinstance(inv, list) else []) if isinstance(x, dict) and
               isinstance(x.get('id'), str) and not fd.element_ok(x)]
    if partial:
        global_scope = True
        bound += [eid for eid in partial if carry_id(eid, None)]
    if entry is None:
        return sorted(set(bound)), True, form
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
        return sorted(set(bound)), (lineage or unresolved), form
    for eid, path in named:
        if carry_id(eid, path):
            bound.append(eid)
    return sorted(set(bound)), False, form


# ---- OBL-29 custody R6.CUST.6: the replay of each run of each context, and r9 sec. 2.2 over its witnesses --------

class ReplayFailure(Exception):
    """A mapping input of R6.CUST.6 that does not admit, resolve or verify as its row states: a custody failure
    (R6.CUST.9), reported as custody-replay."""


replay_selector_schema = 'oi-reconciliation/2'


def _ref(r):
    return {'path': r.get('path'), 'blob_sha256': r.get('blob_sha256')} if isinstance(r, dict) else None


def _git_at(repo, commit, ref):
    """The git blob id of the regular entry at ref's path in commit's tree when its bytes have ref's SHA-256."""
    e = repo.entries(commit).get(ref.get('path')) if isinstance(ref, dict) else None
    if e is None or e[0] not in ('100644', '100755'):
        return None
    data = repo.read(commit, ref['path'])
    return e[1] if data is not None and util.sha256(data) == ref.get('blob_sha256') else None


def _review_witnesses(cum, ref, doc, git, base, directory=None, contested=()):
    """Review witnesses (r9 sec. 2.2): each eligible ordinary review in R* of the record's exact reference (kind review,
    reviewer a person other than the record's author; for a reconciliation record, in its own directory) that is
    adverse or defective (R6.OBL29.3, the checks of eligible_review_problems) stands against that record."""
    from . import obl29
    out = []
    author = doc.get('author') if isinstance(doc, dict) else None
    for path, oid, rv in cum.reviews_naming_ids(ref, directory):
        if not isinstance(rv, dict) or rv.get('kind', 'review') != 'review':
            continue
        who = rv.get('reviewer')
        if not rec._person(who) or who == author:
            continue
        if obl29.adverse_items(rv, doc):
            out.append(dict(base, kind='review', disputed=dict(ref), disputed_doc=doc, disputed_git=git, edge=None,
                            forming=[{'doc': rv, 'git': oid, 'path': path,
                                      'ref': {'path': path, 'blob_sha256': cum.info[oid][2]}}],
                            contested=list(contested)))
    return out


def competing_successors(repo, cum_m, scope, uref, U):
    """r9 R6.OBL29.3, qualifying competing successors from the mutable scan, for the operative edge U -> P (P the
    exact reference U names in `supersedes`): each durable record S in the M-derived portion of R* (`cum_m`, the walk
    from M alone) whose regular entry the R6.RECON.2 (d) scan would select under `scope` (a json file under the
    reconciliation root, outside the tool-landing prefixes and the plan's record directory, of schema
    oi-reconciliation/2), whose exact reference differs from U's, and which names the same exact P in `supersedes`
    with U's schema and lineage (R6.REC.7). Each exact reference is counted once. Returns [(S, ref, git blob id)]."""
    from . import recon_route
    pref, lid = _ref(U.get('supersedes')), rec.lineage_id(U)
    out, counted = [], set()
    for p, o in cum_m.entries():
        inf = cum_m.info[o]
        if inf[0] != 'a' or inf[1] != replay_selector_schema or not p.endswith('.json') or \
                not p.startswith(recon_route.audits_root) or any(p.startswith(x) for x in scope.prefixes) or \
                (scope.plan_dir and p.startswith(scope.plan_dir)):
            continue
        if (p, inf[2]) == (uref['path'], uref['blob_sha256']) or (p, inf[2]) in counted:
            continue
        S = fd.strict_parse(repo.read_blob_uncached(o))
        if not isinstance(S, dict) or S.get('schema') != U.get('schema') or rec.lineage_id(S) != lid or \
                _ref(S.get('supersedes')) != pref:
            continue
        counted.add((p, inf[2]))
        out.append((S, {'path': p, 'blob_sha256': inf[2]}, o))
    return out


def lineage_edges(store, ref, doc):
    """The edges of a record's lineage resolved from the anchor `store` (U1 -> P1, P1 -> P2, ...): ([(successor
    reference, successor doc, predecessor reference)], unresolved), unresolved True when a `supersedes` reference does
    not resolve there (the walk stops at it) or the chain loops."""
    out, seen, cur, cref = [], {ref.get('blob_sha256')}, doc, ref
    while isinstance(cur, dict) and isinstance(cur.get('supersedes'), dict):
        pref = _ref(cur['supersedes'])
        if pref['blob_sha256'] in seen:
            return out, True
        out.append((cref, cur, pref))
        prev = store.resolve(pref)
        if not isinstance(prev, dict):
            return out, True
        seen.add(pref['blob_sha256'])
        cur, cref = prev, pref
    return out, False


def live_lineage_problems(repo, M, doc, cfg, store, scope, m_scan, cum_m, schemas):
    """r9 R6.OBL29.3 on the current run's own lineage checks: where the configuration cites the repair record U of a
    cited reassessment (an existing route making its R6.REC.7 check operative for the discharge, in every admission
    mode in which the R6.RECON.2 (d) scan can run), every edge of U's lineage resolved under the prescribed anchor F
    (U -> P1, P1 -> P2, ...) is checked, and each qualifying competing successor S in M's ancestry fails the discharge
    (FAIL record-invalid), with or without custody. A lineage that does not resolve under F, or whose required check
    fails, fails the discharge as well. `cum_m` is a callable returning the walk from M alone (built only when needed).

    Citation is the only route that makes a repair record's lineage check operative for a discharge in this tool
    revision: the discharge reads its repair entry only from M's scanned set (R6.OBL29.4), and a record admitted
    through the post-freeze route (R6.RECON.2, REV) serves the reconciliation of drifted paths, not a discharge's
    repair (its record lies in REV's tree, not M's, so an entry naming it is not present at M). A REV-admitted record
    therefore needs no separate trigger here."""
    if not isinstance(doc, dict) or doc.get('repair') is None:
        return []
    eref = _ref(_part(doc, 'repair_entry'))
    cited = {(r.get('path'), r.get('blob_sha256')) for r in cfg.get('records') or [] if isinstance(r, dict)
             and r.get('kind') == 'reconciliation'}
    if not eref or (eref['path'], eref['blob_sha256']) not in cited:
        return []
    U = store.get(eref)
    if not isinstance(U, dict) or U.get('schema') not in schemas or not isinstance(U.get('supersedes'), dict):
        return []
    edges, unresolved = lineage_edges(store, eref, U)
    if unresolved:
        return ['the required lineage of the cited repair record %s does not resolve under F (R6.REC.7, R6.OBL29.3)'
                % eref['path']]
    lint = rec.supersedes_problems(eref, U, store)
    if lint:
        return ['the required lineage check of the cited repair record %s fails: %s' % (eref['path'], lint[0])]
    out = []
    for xref, X, pref in edges:
        out += ['the competing successor %s in M\'s ancestry supersedes %s, which %s in the lineage of the cited '
                'repair record %s supersedes (R6.OBL29.3, R6.REC.7)' % (sref['path'], pref['path'], xref['path'],
                                                                        eref['path'])
                for _S, sref, _g in competing_successors(repo, cum_m(), scope, xref, X)]
    return out


def run_roles_x(repo, c_, m, rev):
    """(roles.X, admitted classify records) of the run (m, rev) of a context, from its landed result (owner decision
    of 2026-11-27: roles.X is a named, verdict-readable field): the evaluating results under the configuration's
    op-c-runs/ in the landing tree whose roles.M is m and whose classify_records name rev. Exactly one X, a full commit
    id, is required, and one set of {(path, sha256)} of the records the run admitted (ReplayFailure otherwise)."""
    import json as _json
    d = posixpath.dirname(c_['config']['path']) + '/op-c-runs/'
    xs, listings = set(), set()
    for p_, (mode, _o) in sorted(repo.entries(c_['landing']).items()):
        if not p_.startswith(d) or posixpath.basename(p_) != 'result.json' or mode not in ('100644', '100755'):
            continue
        res = fd.strict_parse(repo.read(c_['landing'], p_))
        if not isinstance(res, dict) or res.get('outcome') in ('USAGE', 'ERROR', 'VOID', 'INTERNAL'):
            continue
        roles = res.get('roles') if isinstance(res.get('roles'), dict) else {}
        revs = {x.get('rev') for x in (res.get('inputs') or {}).get('classify_records') or [] if isinstance(x, dict)}
        if roles.get('M') == m and revs == {rev}:
            xs.add(roles.get('X'))
            listings.add(frozenset((x.get('path'), x.get('sha256')) for x in
                                   (res.get('inputs') or {}).get('classify_records') or [] if isinstance(x, dict)))
    del _json
    if len(xs) != 1 or not isinstance(next(iter(xs)), str) or not re.match(r'^[0-9a-f]{40}$', next(iter(xs))):
        raise ReplayFailure('the landed result of run (%s, %s) records no single roles.X (%d values)'
                            % (m, rev, len(xs)))
    if len(listings) != 1:
        raise ReplayFailure('the landed results of run (%s, %s) disagree on the records the run admitted' % (m, rev))
    return next(iter(xs)), next(iter(listings))


def replay_rev_admission(repo, f, m, rev, X, cfg, loaded, cref, pinned_doc, ledgered, landed_admitted):
    """R6.RECON.2 (a)-(g) replayed with that REV, m, the run's X and the context's configuration: the reconciliation
    records REV adds, admitted under the context's scope as the run's route admitted them. The replayed admitted set
    {(path, sha256)} must equal the set the landed result records in inputs.classify_records (`landed_admitted`) and
    be non-empty; a record the route refuses is not by itself a failure. Returns the admitted records {(path, sha256):
    record}; a difference or an empty set is a custody failure (ReplayFailure)."""
    from . import recon_route
    corpus = cfg.get('corpus') or {}
    rx = [re.compile(x) for x in corpus.get('patterns') or [] if isinstance(x, str)]
    exact = set(corpus.get('paths') or []) if isinstance(corpus.get('paths'), list) else set()
    config_recon = []
    for r in cfg.get('records') or []:
        if isinstance(r, dict) and r.get('kind') == 'reconciliation':
            d = loaded.store.get(r)
            if isinstance(d, dict):
                config_recon.append(dict(d, _ref=_ref(r), _source=f))
    roles = cfg.get('roles') if isinstance(cfg.get('roles'), dict) else {}
    rscope = recon_route.Scope(repo, roles.get('scientific_base'), m, X, f, False, pinned_doc,
                               posixpath.dirname(cref['path']), ledgered,
                               lambda p: p in exact or any(x.search(p) for x in rx), config_recon)
    # the candidates are the records the run named and admitted, as its landed result lists them, read at REV (a
    # record REV adds that the run did not name plays no part: the original run took only its --classify records; a
    # listed record absent from REV, or of another blob, fails the comparison below)
    cands = []
    for p_, sha_ in sorted(landed_admitted, key=str):
        e = repo.entries(rev).get(p_) if isinstance(p_, str) else None
        if e is None or e[0] not in ('100644', '100755'):
            raise ReplayFailure('the run\'s REV %s does not hold the listed record %s' % (rev, p_))
        data = repo.read(rev, p_)
        doc = fd.strict_parse(data)
        if isinstance(doc, dict) and doc.get('schema') in recon_route.recon_schemas:
            cands.append((rev, rev, p_, data, doc))
    items = []
    admitted, _listing, _clash = recon_route.admit(repo, cands, rscope, items)
    got = {(r['_ref']['path'], r['_ref']['blob_sha256']) for r in admitted}
    if not got or got != set(landed_admitted):
        why = [d for i in items for d in (i.get('detail') or [i.get('why')]) if d]
        raise ReplayFailure('the run\'s REV %s does not replay under R6.RECON.2: the replayed admitted records %s '
                            'differ from those its landed result records %s%s'
                            % (rev, sorted(got), sorted(landed_admitted), ('; ' + why[0]) if why else ''))
    return {(r['_ref']['path'], r['_ref']['blob_sha256']): {k: v for k, v in r.items() if k not in ('_ref', '_source')}
            for r in admitted}


def replay_run(repo, c_, m, rev, load_config, schemas, prefix, context_ledger=None):
    """R6.CUST.6 for one run (m, rev) of the context c_ = {f, config}: the run's operative discharge checks
    re-established and their witnesses qualified under R6.OBL29.3 as a run with roots m, f and rev would have, from the
    inputs of the design's mapping table only. Returns the witnesses (r9 sec. 2.2). A mapping input that does not
    admit or resolve raises ReplayFailure (custody-replay); an unreadable object raises the reader's Unresolvable."""
    from . import recon_route
    f, cref = c_['f'], c_['config']
    try:
        loaded = load_config(f, cref)
    except fd.Unsettled:
        raise
    except Exception as exc:  # the configuration does not admit at f (R6.CFG.1-.2); an unreadable object is ERROR
        if type(exc).__name__ == 'Unresolvable':
            raise
        raise ReplayFailure('the configuration %s does not admit at %s: %s' % (cref.get('path'), f, exc))
    cfg = loaded.config
    roles = cfg.get('roles') if isinstance(cfg.get('roles'), dict) else {}
    pinned = roles.get('side_change_classes')
    pinned_doc = None
    if isinstance(pinned, dict) and pinned.get('path'):
        pinned_doc = loaded.store.get(pinned)
        if not isinstance(pinned_doc, dict):
            raise ReplayFailure('the original selector %s does not resolve at %s' % (pinned.get('path'), f))
    # the original selector: the context's class record, its prefixes and the plan's record directory at f
    scope = recon_route.Scope(repo, roles.get('scientific_base'), m, None, f, False, pinned_doc,
                              posixpath.dirname(cref['path']), (), lambda p: False, [])
    # R*(m): the finding lookup, the reviews that qualify witnesses for this run and the competing successors are
    # read over the record set of m (the mapping table's rows; rev is null here)
    cum_m = Cumulative(repo, [m], schemas, prefix)
    found = cum_m.findings()
    # a run naming REV: R6.RECON.2 (a)-(g) replayed with that REV, m, the run's X (roles.X of its landed result,
    # roles.M = m) and the context's configuration, the admitted set equal to the landed result's; the competing
    # successors are read over R*(m) and REV's tree. The repair entry is still read in the scanned set of m only
    # (mapping table; R6.CUST.9; r9 sec. 2.2: no witness for a frozen discharge that never made the lineage check
    # operative), so a repair record that only REV holds is custody-replay
    cum_s = cum_m
    if rev is not None:
        X, landed_admitted = run_roles_x(repo, c_, m, rev)
        try:
            ledgered = set(context_ledger(loaded)) if context_ledger else None
        except Exception as exc:  # the context's ledger cannot be read: the scope is undecided
            if type(exc).__name__ == 'Unresolvable':
                raise
            ledgered = None
        if ledgered is None:
            raise ReplayFailure('the ledgered paths of the configuration %s cannot be read at %s' % (cref['path'], f))
        replay_rev_admission(repo, f, m, rev, X, cfg, loaded, cref, pinned_doc, ledgered, landed_admitted)
        cum_s = Cumulative(repo, [m, rev], schemas, prefix)
    chain = _first_parent_chain(repo, m)
    m_store = rec.Store(recon_route.scanned(repo, m, scope))
    cited = {(r.get('path'), r.get('blob_sha256')) for r in cfg.get('records') or [] if isinstance(r, dict)}
    out = []
    for r in cfg.get('records') or []:
        if not isinstance(r, dict) or r.get('kind') != 'reassessment':
            continue
        aref = _ref(r)
        A = loaded.store.get(aref)
        if not isinstance(A, dict) or A.get('schema') != reassessment_schema:
            raise ReplayFailure('the reassessment %s does not resolve at %s' % (aref['path'], f))
        fref = A.get('finding')
        named = finding_of(found, fref)
        if not named:
            raise ReplayFailure('the finding the reassessment %s names does not resolve in R*(m) at %s'
                                % (aref['path'], m))
        base = {'context': f, 'run': m, 'rev': rev, 'original': (_ref(fref), fref.get('item'))}
        out += _review_witnesses(cum_m, aref, A, _git_at(repo, f, aref), base)
        # the predecessors of the reassessment's existing lineage check, resolved from the context's anchor f. Their
        # ordinary reviews form review witnesses; widening reviews do not, since a widening review applies to rule
        # files and configurations (records.widening_review_problems), and the predecessors here are of the
        # reassessment kind, as the repair record's are of the reconciliation kind: for these two kinds no widening
        # review is required, so none can fail
        cur, seen = A, {aref['blob_sha256']}
        while isinstance(cur, dict) and isinstance(cur.get('supersedes'), dict):
            pref = _ref(cur['supersedes'])
            if pref['blob_sha256'] in seen:
                break
            seen.add(pref['blob_sha256'])
            prev = loaded.store.resolve(pref)
            if not isinstance(prev, dict):
                raise ReplayFailure('a predecessor %s of the reassessment %s does not resolve from %s'
                                    % (pref['path'], aref['path'], f))
            out += _review_witnesses(cum_m, pref, prev, cum_m.git_id(pref) or _git_at(repo, f, pref), base,
                                     contested=[pref['blob_sha256']])
            cur = prev
        if A.get('repair') is None:
            continue
        entry = _part(A, 'repair_entry')
        eref = _ref(entry)
        Q = m_store.get(eref) if eref else None
        if not isinstance(Q, dict) or Q.get('schema') not in schemas:
            raise ReplayFailure('the repair entry the reassessment %s names does not resolve in the scanned set of %s'
                                % (aref['path'], m))
        qgit = cum_m.git_id(eref) or _git_at(repo, m, eref)
        out += _review_witnesses(cum_m, eref, Q, qgit, base, directory=posixpath.dirname(eref['path']))
        # lineage witnesses: the repair record's existing R6.REC.7 check is operative only where the context's
        # configuration admits it (a repair found solely by the entry lookup at m has no lineage check), and only
        # where the original positive route made its edge operative at m: the repair commits on m's first-parent
        # chain, the finding applicable at m (R6.RECON.26) and the edge resolved from f without failure
        sup = Q.get('supersedes')
        if (eref['path'], eref['blob_sha256']) not in cited or not isinstance(sup, dict):
            continue
        anchor = loaded.store
        commits = _part(A, 'repair_commits')
        applies = any(in_m(repo, m, (x.get('entry') or {}).get('side_change_commits') or []) for x in named
                      if isinstance(x.get('entry'), dict))
        edges, unresolved = lineage_edges(anchor, eref, Q)
        if not (isinstance(commits, list) and commits and all(c in chain for c in commits)) or not applies or \
                unresolved or rec.supersedes_problems(eref, Q, anchor):
            continue
        # every edge of Q's lineage resolved from f; the witness stands against Q, whose required check covers them
        for xref, X, pref in edges:
            for S, sref, sgit in competing_successors(repo, cum_s, scope, xref, X):
                out.append(dict(base, kind='lineage', disputed=dict(eref), disputed_doc=Q, disputed_git=qgit,
                                edge=(xref['blob_sha256'], pref['blob_sha256']),
                                forming=[{'doc': S, 'git': sgit, 'path': sref['path'], 'ref': sref}],
                                contested=[pref['blob_sha256']]))
    return out


def witness_report(W):
    """A witness as the result reports it (OQ-12): its context, run, kind and exact references."""
    return {'context': W['context'], 'run': W['run'], 'rev': W.get('rev'), 'kind': W['kind'],
            'disputed': W['disputed'], 'edge': list(W['edge']) if W.get('edge') else None,
            'forming': [x['ref'] for x in W.get('forming') or []],
            'original': {'finding': W['original'][0], 'item': W['original'][1]}}


def _lineage(store, ref, doc):
    """(blobs, edges, unresolved) of a record's resolved lineage, the record included. `store` resolves a reference
    (an object with resolve(ref))."""
    blobs, edges, unresolved = [ref['blob_sha256']], [], False
    cur, cref = doc, ref
    while isinstance(cur, dict) and isinstance(cur.get('supersedes'), dict):
        pref = _ref(cur['supersedes'])
        if pref['blob_sha256'] in blobs:
            break
        edges.append((cref['blob_sha256'], pref['blob_sha256']))
        prev = store.resolve(pref)
        if not isinstance(prev, dict):
            unresolved = True
            break
        blobs.append(pref['blob_sha256'])
        cur, cref = prev, pref
    return blobs, edges, unresolved


class _Either:
    def __init__(self, *stores):
        self.stores = stores

    def resolve(self, ref):
        for st in self.stores:
            got = st.resolve(ref)
            if isinstance(got, dict):
                return got
        return None


def custody_decisions(repo, witnesses, applying, loaded, m_scan, cum, schemas):
    """r9 sec. 2.2 `blocked(D, W)` for each applying discharge D of the current run and each witness W from custody
    (R6.CUST.6). Custody only adds witnesses: clearance reads only the current freeze's own admitted records. Returns
    (blocked [(D's (doc, ref), W, clauses)], report rows)."""
    from . import obl29
    m_store = rec.Store(m_scan)
    cited = {(r.get('path'), r.get('blob_sha256')) for r in loaded.config.get('records') or [] if isinstance(r, dict)}
    blocked, rows = [], []
    for d, r in applying:
        aref = _ref(r)
        ab, ae, au = _lineage(loaded.store, aref, d)
        fref = d.get('finding') if isinstance(d.get('finding'), dict) else {}
        D = {'reassessment': {'doc': d, 'ref': aref}, 'finding': (_ref(fref), fref.get('item')), 'repair': None,
             'lineage_blobs': list(ab), 'lineage_edges': list(ae), 'unresolved': au}
        R, nr2, reviews_of_R, candidates = None, False, [], [None]
        if d.get('repair') is not None:
            entry = _part(d, 'repair_entry')
            eref = _ref(entry)
            Q = m_store.get(eref) if eref else None
            D['repair'] = {'entry': eref, 'entry_doc': Q, 'entry_path': (entry or {}).get('entry_path'),
                           'commits': _part(d, 'repair_commits')}
            if isinstance(Q, dict):
                # a repair found by the entry lookup at M resolves its lineage in M's scanned set, where it was found,
                # then from F; an unresolved reference counts as reliance (undecidable)
                qb, qe, qu = _lineage(_Either(m_store, loaded.store), eref, Q)
                D['lineage_blobs'] += qb
                D['lineage_edges'] += qe
                D['unresolved'] = D['unresolved'] or qu
                # NR-2: the current freeze admits R through an existing route making its R6.REC.6 and R6.REC.7 checks
                # operative (the configuration cites it), and they pass on their prescribed inputs and on R*
                qdir = posixpath.dirname(eref['path'])
                reviews_of_R = [dict(x, _dir=qdir) for _p, x in cum.reviews_naming(eref, qdir)]
                if (eref['path'], eref['blob_sha256']) in cited:
                    R = {'ref': eref, 'doc': Q, 'lineage_blobs': qb, 'lineage_edges': qe}
                    nr2 = not rec.lint_chain(eref, loaded.store, loaded.admitted) and \
                        not eligible_review_problems(cum.reviews_naming(eref, qdir), Q)
                    candidates = [dict(x, _dir=posixpath.dirname(p)) for p, x in m_store.by_sha.values()
                                  if isinstance(x, dict) and x.get('schema') == rec.review_schema and
                                  x.get('reviewed') == eref] or [None]
            else:
                D['unresolved'] = True
        fgit = cum.git_id(_ref(fref))
        for W in witnesses:
            disputed_reviewers = [x.get('reviewer') for _p, x in cum.reviews_naming(W['disputed'])
                                  if isinstance(x, dict) and not obl29.adverse_items(x, W.get('disputed_doc'))]
            excluded = {d.get('author'), (W.get('disputed_doc') or {}).get('author')}
            excluded |= {(x['doc'] or {}).get('author') for x in W.get('forming') or []}
            excluded |= {(x['doc'] or {}).get('reviewer') for x in W.get('forming') or []}
            excluded |= set(disputed_reviewers)
            if R is not None:
                excluded.add(Q.get('author'))
            for sha in W.get('contested') or []:
                prev = [x for _s, (_p, x) in loaded.store.scanned().items() if _s == sha]
                excluded |= {(x or {}).get('author') for x in prev}
            got = None
            for z in candidates:
                b, clauses, route = obl29.decide(D, W, R=R, Z=[z] if z else None, required_review=z,
                                                 excluded=excluded, reviews_of_R=reviews_of_R, nr2=nr2,
                                                 finding_git=fgit)
                got = (b, clauses, route)
                if not b:
                    break
            b, clauses, route = got
            row = {'reassessment': aref, 'witness': witness_report(W), 'clauses': clauses,
                   'blocked': b, 'route': route}
            rows.append(row)
            if b:
                blocked.append(((d, r), W, clauses))
    return blocked, rows
