# design r6 as amended by amendments 3 and 4: R6.RECON.25, R6.RECON.26 (first kind of finding), R6.RECON.27
"""Category 3: the blocking state.

A finding of the first kind is a reconciliation record entry whose scientific_effect has the verdict invalidates and
whose record passes record lint with a review that accepts every item. Every run that evaluates M scans M's tree, the
records the run reads, and the scanned sets of F's tree and of each record commit the run names, for findings,
whether or not any path differs between H and M. A finding blocks a run whose M contains one of the entry's
side_change_commits when the run's configuration carries an invalidated edit: its ledger holds the edit's id, or an
edit of the same path whose old bytes hash to the recorded old_sha256. A reassessment the configuration cites lifts
the block for the finding it names when it applies.

Not implemented here, pending a design decision: the second kind of finding (a review record's verdict), the plan
lineage of the configuration a finding was made under, and recorded identifier migrations.
"""
import posixpath

from . import outcome as oc
from . import records as rec
from . import util

reassessment_schema = 'oi-reassessment/1'
blocked_class = 'retirement-blocked'

# The keys of one element of `invalidated`. The design names its parts (an edit id, the canonical sha256 of its
# edit-list entry and its target: path, start_H, old_sha256) but not their keys; this is the one place that reads
# them. None: the part is not read.
invalidated_keys = {'id': 'id', 'sha256': 'sha256', 'target': None}
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
    """Problems of the record's review: exactly one review record in its directory naming its blob, and the chain
    lint with that review admitted."""
    d = posixpath.dirname(ref['path'])
    reviews = [s for s, (p, rv) in store.by_sha.items()
               if isinstance(rv, dict) and rv.get('schema') == rec.review_schema and posixpath.dirname(p) == d
               and isinstance(rv.get('reviewed'), dict) and rv['reviewed'].get('blob_sha256') == sha]
    if len(reviews) != 1:
        return ['%d review records in the record directory name its blob, not one' % len(reviews)]
    return rec.lint_chain(ref, store, {sha, reviews[0]})


def findings_in(entries, schemas):
    """entries: [(path, bytes)] of one scanned set. The findings of the first kind among its records:
    [{'record': ref, 'path': entry path, 'invalidated': [...], 'side_change_commits': [...]}]."""
    store = rec.Store(entries)
    out = []
    for sha, (path, doc) in sorted(store.by_sha.items()):
        if not isinstance(doc, dict) or doc.get('schema') not in schemas:
            continue
        ents = [e for e in doc.get('paths') or [] if isinstance(e, dict)
                and (e.get('scientific_effect') or {}).get('verdict') == 'invalidates']
        if not ents:
            continue
        ref = {'path': path, 'blob_sha256': sha}
        if _reviewed(store, ref, sha):
            continue
        for e in ents:
            out.append({'record': ref, 'path': e.get('path'),
                        'invalidated': list((e.get('scientific_effect') or {}).get('invalidated') or []),
                        'side_change_commits': list(e.get('side_change_commits') or [])})
    return out


def findings_of_records(records, schemas):
    """The findings among records the run reads (already admitted under their review chain)."""
    out = []
    for r in records:
        if r.get('schema') not in schemas:
            continue
        for e in r.get('paths') or []:
            if isinstance(e, dict) and (e.get('scientific_effect') or {}).get('verdict') == 'invalidates':
                out.append({'record': r.get('_ref'), 'path': e.get('path'),
                            'invalidated': list((e.get('scientific_effect') or {}).get('invalidated') or []),
                            'side_change_commits': list(e.get('side_change_commits') or [])})
    return out


def unique(found):
    seen, out = set(), []
    for f in found:
        key = ((f['record'] or {}).get('blob_sha256'), f['path'])
        if key not in seen:
            seen.add(key)
            out.append(f)
    return out


def carried(led, edit_id, target):
    """The edit of the run's ledger that carries an invalidated edit: the same id, or a splice of the same path whose
    old bytes hash to the recorded old_sha256, whatever its offset. None if the ledger carries none."""
    raw = led.get('raw') or {}
    for e in raw.get('edits') or []:
        if isinstance(e, dict) and edit_id is not None and e.get('id') == edit_id:
            return e.get('id')
    for s in led.get('splices') or []:
        if s.get('id') == edit_id and edit_id is not None:
            return s.get('id')
    if target and target.get('path') and target.get('old_sha256'):
        for s in led.get('splices') or []:
            if s.get('file') == target['path'] and s.get('old_sha256') == target['old_sha256']:
                return s.get('id')
    return None


def in_m(repo, M, commits):
    for c in commits:
        try:
            if isinstance(c, str) and repo.is_ancestor(c, M):
                return True
        except Exception:  # a commit the object store does not hold is not in M
            continue
    return False


def blocks(repo, M, led, found, lifted=lambda finding, edit: False):
    """[(finding, edit id carried by the run's ledger)] of the findings that block the run."""
    out = []
    for f in found:
        if not in_m(repo, M, f['side_change_commits']):
            continue
        for x in f['invalidated']:
            eid, _sha, target = read_invalidated(x)
            have = carried(led, eid, target)
            if have is not None and not lifted(f, have):
                out.append((f, have))
                break
    return out


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
        if differs and path in by_path:
            by_path[path].update(disposition=blocked_class, finding=f['record'], edit=eid)
            items.append(oc.make_item('RET', blocked_class, path, None, fp, file=path,
                                      detail='a reviewed finding invalidates edit %s' % eid))
        else:
            items.append(oc.make_item('RET', blocked_class, path, None, dict(fp, run_level=True),
                                      detail='a reviewed finding invalidates edit %s (run-level)' % eid))
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


def reassessment_problems(repo, M, led, doc, ref, store, admitted, found, m_scan, schemas):
    """Why a cited reassessment does not apply (empty if it applies). m_scan: [(path, bytes)], the scanned set of M's
    tree."""
    out = []
    if not isinstance(doc, dict) or doc.get('schema') != reassessment_schema:
        return ['not a reassessment record']
    out += rec.lint_chain(ref, store, admitted)
    if out:
        return out
    reviewers = {rv.get('reviewer') for _s, (_p, rv) in store.by_sha.items()
                 if isinstance(rv, dict) and rv.get('schema') == rec.review_schema
                 and isinstance(rv.get('reviewed'), dict) and rv['reviewed'].get('blob_sha256') == ref['blob_sha256']}
    finding = doc.get('finding')
    if not (isinstance(finding, dict) and any((f['record'] or {}).get('path') == finding.get('path') and
                                               (f['record'] or {}).get('blob_sha256') == finding.get('blob_sha256')
                                               for f in found)):
        out.append('the named finding is not a finding at M')
    commits = _part(doc, 'repair_commits')
    chain = _first_parent_chain(repo, M)
    if not (isinstance(commits, list) and commits and all(isinstance(c, str) and c in chain for c in commits)):
        out.append("the repair's commits do not lie on M's first-parent chain")
    entry = _part(doc, 'repair_entry')
    m_store = rec.Store(m_scan)
    edoc = m_store.get(entry) if isinstance(entry, dict) else None
    if not isinstance(edoc, dict) or edoc.get('schema') not in schemas:
        out.append("the repair's reconciliation record entry is not present at M")
    else:
        if _reviewed(m_store, entry, entry.get('blob_sha256')):
            out.append("the repair's reconciliation record entry has no accepting non-author review")
        if edoc.get('author') in reviewers:
            out.append("the reviewer is the author of the repair's reconciliation record entry")
    if not (isinstance(doc.get('rederivation'), str) and doc['rederivation'].strip()):
        out.append('the rederivation is empty')
    if doc.get('verdict') != 'no-effect':
        out.append('the verdict is not no-effect')
    eid, esha = _part(doc, 'edit_id'), _part(doc, 'edit_sha256')
    if eid is None or edit_sha(led, eid) is None or edit_sha(led, eid) != esha:
        out.append("the edit is not an edit of the citing configuration's ledger as worded")
    return out


def lifting(reassessments):
    """lifted(finding, edit id) over the reassessments that apply: [(doc, ref)]."""
    def lifted(f, eid):
        fr = f['record'] or {}
        return any(isinstance(d.get('finding'), dict) and d['finding'].get('path') == fr.get('path')
                   and d['finding'].get('blob_sha256') == fr.get('blob_sha256') and _part(d, 'edit_id') == eid
                   for d, _r in reassessments)
    return lifted
