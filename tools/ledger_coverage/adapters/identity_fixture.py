"""Fixture identities and the review records of the control fixtures (staging S-2): identity strings (S2.1) for the
fixture parties, the one constructor of a review record, which carries S2.3's independence declaration, and the
binding of a review to the commit its reviewer read (`revision`, S-1 sec. 3 as S-2 S2.3 keeps it).
"""
import json

from ledger_coverage import record_authority as ra
from ledger_coverage.engine import gitobj, util

WRITER = 'session.fixture-writer'
REVIEWER = 'session.fixture-reviewer'
WIDENER = 'session.fixture-widener'
OWNER = ra.OWNER_IDENTITIES[0]
REVIEW_SCHEMA = 'oi-review-record/1'


def review_record(fields):
    """Every review record the fixtures and controls construct is built here, from its fields. It carries staging S-2
    S2.3's independence declaration, {not_author: true, depends_on: []}, unless the fields give one."""
    out = dict(fields)
    out.setdefault('independence', {'not_author': True, 'depends_on': []})
    return out


def bind(review, revision):
    """A review carrying `revision`, a commit holding the reviewed bytes and reachable from the root the review is
    read from (S-1 sec. 3), and its independence declaration (S-2 S2.3)."""
    out = review_record(review)
    out['revision'] = revision
    return out


def is_review(data):
    try:
        d = json.loads(data.decode('utf-8'))
    except (ValueError, UnicodeDecodeError, AttributeError):
        return False
    return isinstance(d, dict) and d.get('schema') == REVIEW_SCHEMA


UNBOUND = '__unbound__'


def bind_files(files, revision):
    """`files` with every review record that has no `revision` bound to `revision` (a review whose revision is
    UNBOUND loses the key instead), each re-serialized as the fixture wrote it."""
    out = dict(files)
    for p, v in files.items():
        d = _review_doc(v)
        if d is None or ('revision' in d and d['revision'] != UNBOUND):
            continue
        d = dict(d)
        if d.get('revision') == UNBOUND:
            d.pop('revision')
        else:
            d['revision'] = revision
        out[p] = _same_format(v, d)
    return out


def unbind(data):
    """A review's bytes without `revision`, so that the commit that adds it binds it anew (a review copied into
    another history, where the commit it named is not an ancestor); other bytes unchanged."""
    d = _review_doc(data)
    if d is None or 'revision' not in d:
        return data
    d = dict(d)
    d.pop('revision')
    return _same_format(data, d)


def unit_store(entries, extra=None):
    """For an in-memory Store of a unit control: (repo, root, entries) where root is a commit holding every entry
    that is not a review and the files in `extra`, and every review without `revision` names root (S-1 sec. 3)."""
    ov = gitobj.Overlay()
    held = {q: b for q, b in entries if _review_doc(b) is None}
    held.update(extra or {})
    root = ov.add_commit(held, [], 'unit root')
    out = [(q, bind_files({q: b}, root)[q] if _review_doc(b) is not None else b) for q, b in entries]
    return ov, root, out


def commit_bound(repo, base, files, parents, subject, config_path=None):
    """One commit adding `files` on `base` whose reviews bind (S-1 sec. 3): when a review names a record the commit
    adds, the other files land first in a layer it names, and the configuration at `config_path`, its references to
    the rebound reviews repinned, lands in a second layer that its own reviews name. Returns (commit, files as
    committed); `files` is updated in place to the committed bytes."""
    unbound = {q: d for q, d in ((q, _review_doc(b)) for q, b in files.items()) if d is not None and
               'revision' not in d}
    if not unbound:
        return repo.derive(base, files, parents=parents, subject=subject), files
    cfg_reviews = {q for q, d in unbound.items() if (d.get('reviewed') or {}).get('path') == config_path}
    plain = {q: b for q, b in files.items() if q not in unbound and q != config_path}
    l1 = gitobj.Overlay.derive(repo, base, plain, parents=parents, subject=subject + ' (reviewed files)')
    shas = {}
    for q, d in unbound.items():
        if q not in cfg_reviews:
            new = _same_format(files[q], dict(d, revision=l1))
            shas[q] = util.sha256(new)
            files[q] = new
    top = l1
    if config_path is not None and config_path in files:
        cfg = json.loads(files[config_path].decode('utf-8'))
        for key in ('records', 'rules'):
            for x in cfg.get(key) or []:
                if isinstance(x, dict) and x.get('path') in shas:
                    x['blob_sha256'] = shas[x['path']]
        files[config_path] = _same_format(files[config_path], cfg)
        csha = util.sha256(files[config_path])
        if cfg_reviews:
            top = gitobj.Overlay.derive(repo, l1, {config_path: files[config_path]}, parents=[l1],
                                        subject=subject + ' (configuration)')
            for q in cfg_reviews:
                d = dict(unbound[q], revision=top)
                d['reviewed'] = dict(d['reviewed'], blob_sha256=csha)
                files[q] = _same_format(files[q], d)
    return gitobj.Overlay.derive(repo, top, files, parents=[top], subject=subject), files


class BindingOverlay(gitobj.Overlay):
    """An in-memory repository whose commits bind every review record they add (S-1 sec. 3, kept by staging S-2
    S2.3): a review without `revision` names the parent commit when that commit holds the reviewed bytes, and
    otherwise a commit, the new first parent, that adds the commit's other files first. A review whose revision is
    UNBOUND is committed without the key."""

    def derive(self, base_commit, changes, parents=None, subject='in-memory'):
        parents = list(parents if parents is not None else [base_commit])
        found, layer = {}, False
        for p, v in changes.items():
            d = _review_doc(v)
            if d is None or ('revision' in d and d['revision'] != UNBOUND):
                continue
            found[p] = d
            rv = d.get('reviewed') if isinstance(d.get('reviewed'), dict) else {}
            if d.get('revision') != UNBOUND and not self._holds(base_commit, rv) and \
                    _sha_of(changes.get(rv.get('path'))) == rv.get('blob_sha256'):
                layer = True
        if not found:
            return gitobj.Overlay.derive(self, base_commit, changes, parents, subject)
        first = base_commit
        if layer:
            first = gitobj.Overlay.derive(self, base_commit, {p: v for p, v in changes.items() if p not in found},
                                          parents=[base_commit], subject=subject + ' (reviewed files)')
        out = bind_files(changes, first)
        return gitobj.Overlay.derive(self, base_commit, out, parents=[first] + parents[1:] if layer else parents,
                                     subject=subject)

    def _holds(self, commit, ref):
        try:
            ent = self.entries(commit).get(ref.get('path'))
            return ent is not None and util.sha256(self.read(commit, ref['path'])) == ref.get('blob_sha256')
        except (gitobj.Unresolvable, KeyError, TypeError):
            return False


def _review_doc(v):
    if not isinstance(v, (bytes, bytearray)):
        return None
    try:
        d = json.loads(v.decode('utf-8'))
    except (ValueError, UnicodeDecodeError):
        return None
    return d if isinstance(d, dict) and d.get('schema') == REVIEW_SCHEMA else None


def _sha_of(v):
    return util.sha256(v) if isinstance(v, (bytes, bytearray)) else None


def _same_format(old, doc):
    """A JSON document re-serialized as the fixture wrote it: canonical bytes, or indented JSON with a newline."""
    return util.canonical(doc) if old == util.canonical(json.loads(old.decode('utf-8'))) else \
        (json.dumps(doc, indent=1, sort_keys=True) + '\n').encode()
