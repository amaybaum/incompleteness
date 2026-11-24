"""Configuration admission and its root of trust (design v5.5.8, sec. 6.3): the tool authority record `A`, the
versioned comment forms, the authority-change procedure, the freeze ledger with its approved appends, the
deterministic designation state, the plan's pin table, and the admission snapshot. Every comment's authority is judged
by "Owner at creation" (DI-1): its author against the owner of the version of `A` in force at its creation.

Every failure refuses admission (an error of class config-unreviewed). The caller supplies only the commits and the plan
and round names; every authority value comes from `A`, read from `main` of the attested repository.
"""
import json
import re

from . import util
from .host import HostUnavailable, first_line
from .records import OwnerTimeline

authority_path = 'tools/ledger_coverage/authority.json'
tool_dir = authority_path.rsplit('/', 1)[0] + '/'
authority_schema = 'oi-tool-authority/2'
ledger_schema = 'oi-freeze-ledger/1'
authority_fields = ['schema', 'owner', 'repository', 'workflow', 'engine_pins', 'plans', 'authority_thread',
                    'freeze_ledger_path', 'forms', 'supersedes']
overridable_never = ['owner', 'repository', 'workflow', 'engine_pins', 'plans', 'authority_thread',
                     'freeze_ledger_path', 'forms']


class Refused(Exception):
    def __init__(self, point, message):
        Exception.__init__(self, '%s: %s' % (point, message))
        self.point = point
        self.message = message


def refuse(point, message):
    raise Refused(point, message)


# ---- A --------------------------------------------------------------------------------------------------------

def parse_authority(data):
    try:
        a = json.loads(data.decode('utf-8'))
    except (ValueError, UnicodeDecodeError, AttributeError):
        refuse('authority', 'the authority record is not valid json')
    if not isinstance(a, dict) or a.get('schema') != authority_schema:
        refuse('authority', 'unknown authority schema')
    missing = [k for k in authority_fields if k not in a]
    unknown = [k for k in a if k not in authority_fields and k != 'status']
    if missing or unknown:
        refuse('authority', 'authority fields missing %s or unknown %s' % (missing, unknown))
    if not isinstance(a['owner'].get('id'), int) or not isinstance(a['repository'].get('id'), int):
        refuse('authority', 'owner and repository ids must be numeric')
    if a['repository'].get('fork') is not False:
        refuse('authority', 'the authority record must name a repository that is not a fork')
    if a['forms'].get('version') != 1:
        refuse('authority', 'unknown forms version')
    return a


# ---- forms ----------------------------------------------------------------------------------------------------

_slot = {'<plan_id>': r'(?P<plan>[A-Za-z0-9._-]+)', '<round_id>': r'(?P<round>[A-Za-z0-9._-]+)',
         '<F>': r'(?P<commit>[0-9a-f]{40})', '<F2>': r'(?P<by>[0-9a-f]{40})',
         '<from>': r'(?P<frm>none|[0-9a-f]{64})', '<to>': r'(?P<to>[0-9a-f]{64})'}


def compile_forms(a):
    """{name: compiled regex} from A's templates; and the reserved prefixes."""
    out = {}
    prefixes = set()
    for name, tmpl in a['forms']['templates'].items():
        rx = re.escape(tmpl)
        for k, v in _slot.items():
            rx = rx.replace(re.escape(k), v)
        out[name] = re.compile('^' + rx + '$')
        prefixes.add(tmpl.split('/', 1)[0] + '/')
    return out, sorted(prefixes)


def parse_form(a, body):
    """(name, fields) for a comment carrying a form; None if its first line has no reserved prefix;
    ('malformed', line) if it has one but matches no template exactly (refused by the caller)."""
    forms, prefixes = compile_forms(a)
    line = first_line(body)
    if not any(line.startswith(p) for p in prefixes):
        return None
    for name, rx in forms.items():
        m = rx.match(line)
        if m:
            return name, m.groupdict()
    return 'malformed', line


def reserved(a, text):
    forms, prefixes = compile_forms(a)
    return any(first_line(text).startswith(p) for p in prefixes)


# ---- threads --------------------------------------------------------------------------------------------------

def read_thread(host, repo_id, issue):
    """Point 2: every comment, page by page, with the count equal to the host's count."""
    try:
        cs, total = host.comments(repo_id, issue)
    except HostUnavailable as exc:
        refuse('thread', 'the thread cannot be read: %s' % exc)
    if len(cs) != total:
        refuse('thread', 'the thread listing has %d comments, the host reports %d' % (len(cs), total))
    return cs


def owner_comments(a, cs, tl):
    """Point 3 over every comment whose author numeric id is `A.owner.id` and every owner comment as "Owner at
    creation" defines it (its author was the owner of the version of A in force at its creation); returns those
    comments and the reported impostors (the owner's login with another numeric id)."""
    own, impostors = [], []
    for c in cs:
        if c.get('author_id') != a['owner']['id'] and not tl.owner_comment(c.get('author_id'), c.get('created_at')):
            if c.get('author_login') == a['owner']['login']:
                impostors.append(c['id'])
            continue
        if 'edits' not in c or 'hidden' not in c:
            refuse('edits', 'the edit status of owner comment %s cannot be read' % c.get('id'))
        if c['hidden']:
            refuse('edits', 'owner comment %s is hidden or minimized' % c['id'])
        edited = bool(c['edits']) or bool(c.get('edited'))
        if edited and parse_form(a, c['body']) is not None:
            refuse('edits', 'owner comment %s carries a form and has an edit' % c['id'])
        for old in c['edits']:
            if reserved(a, old):
                refuse('edits', 'the edit history of owner comment %s contained a form' % c['id'])
        own.append(c)
    return own, impostors


def comment_record(c, tl):
    v = tl.in_force(c['created_at'])
    return {'id': c['id'], 'author_id': c['author_id'], 'created_at': c['created_at'],
            'authority_in_force_sha256': None if v is None else v[2],
            'edited': bool(c['edits']) or bool(c.get('edited')), 'hidden': c['hidden'],
            'first_line': first_line(c['body']), 'body_sha256': util.sha256(c['body'])}


def counts_as_approval(tl, c, owner_id, merged_at):
    """Sec. 6.3, "Owner at creation", approvals: an owner comment, by `owner_id` (the owner of the authority record
    governing the evaluation), with no owner change merged between its creation and the merge it authorizes
    (`merged_at`, or None for a change not yet merged)."""
    return c['author_id'] == owner_id and tl.owner_comment(c['author_id'], c['created_at']) and \
        not tl.changed_between(c['created_at'], merged_at)


def find_approval(a, cs, name, fields, author_id, before):
    """An unedited, visible approval comment by `author_id` carrying exactly the form and fields, created
    before `before` (a host timestamp)."""
    hits = []
    for c in cs:
        if c.get('author_id') != author_id or c.get('hidden') or c.get('edits') or c.get('edited'):
            continue
        f = parse_form(a, c['body'])
        if f is None or f[0] != name:
            continue
        if all(f[1].get(k) == v for k, v in fields.items()) and (before is None or c['created_at'] < before):
            hits.append(c)
    return hits


def _fresh(hits, consumed, point, what):
    """Single use (sec. 6.3): an approval comment authorizes exactly one change. Returns the matching comments that
    no earlier verified change consumed; refuses when every match was consumed."""
    fresh = [c for c in hits if c['id'] not in consumed]
    if hits and not fresh:
        refuse(point, '%s: approval comment %s already authorized an earlier change' % (what, hits[0]['id']))
    return fresh


def _ledger_extension_problem(old, new):
    """None when the ledger blob `new` extends `old` (sec. 6.3, an append-only list): the events of `old` are a
    proper prefix of those of `new` and no other field changes. Otherwise the reason."""
    try:
        o, n = json.loads(old.decode('utf-8')), json.loads(new.decode('utf-8'))
    except (ValueError, UnicodeDecodeError):
        return 'a ledger version is not valid json'
    if not isinstance(o, dict) or not isinstance(n, dict) or not isinstance(o.get('events'), list) or \
            not isinstance(n.get('events'), list):
        return 'a ledger version has no event list'
    if {k: v for k, v in o.items() if k != 'events'} != {k: v for k, v in n.items() if k != 'events'}:
        return 'a field other than the events changed'
    if len(n['events']) <= len(o['events']) or n['events'][:len(o['events'])] != o['events']:
        return 'the earlier events are not a proper prefix of the later ones'
    return None


def _provenance_problem(host, repo_id, path, main, v, prev_blob, prev_merged_at):
    """None when the change `v` of `path` has a consistent merge record (sec. 6.3: every change lands by a pull
    request into main, and its approval predates that merge): a merge time; the merge commit the record names is the
    change's own commit; that commit is on main's first-parent chain, holds the version, and its first parent holds
    the previous version (so the history is continuous); and the merge times increase along the history.
    Otherwise the reason."""
    if v.get('merged_at') is None:
        return 'has no merge record'
    if v.get('merge_commit') != v['commit']:
        return 'has a merge record that names another commit (%s)' % str(v.get('merge_commit'))[:12]
    try:
        on_main = host.on_first_parent_chain(repo_id, v['commit'], main)
        here = host.file_at(repo_id, v['commit'], path)
        before = host.file_at(repo_id, v['parent'], path) if v.get('parent') else None
    except HostUnavailable as exc:
        refuse('history', 'the merge record of %s cannot be checked: %s' % (v['commit'][:12], exc))
    if not on_main:
        return 'is not on main\'s first-parent chain'
    if here != v['blob']:
        return 'does not hold the recorded version'
    if before != prev_blob:
        return 'is not the commit that introduced its version after the previous one'
    if prev_merged_at is not None and not v['merged_at'] > prev_merged_at:
        return 'has a merge time that does not follow the previous change\'s'
    return None


def _ledger_events(blob, what):
    """The event list of a ledger version; refuses when the version is not a ledger record."""
    try:
        d = json.loads(blob.decode('utf-8'))
    except (ValueError, UnicodeDecodeError):
        d = None
    if not isinstance(d, dict) or not isinstance(d.get('events'), list):
        refuse('ledger', '%s is not a freeze-ledger record with an event list' % what)
    return d['events']


def _ledger_append_approval(host, a, tl, old_sha, new_sha, merged_at, consumed, what):
    """N3 (sec. 6.3, "Approval of each acceptance-time append"): a ledger change that adds events is authorized only by
    its own `oi-freeze-ledger/1 append` comment, by the owner of `a` (the version of A governing the change), in the
    authorized thread of a plan `a` lists, naming that plan and one of the rounds `a` lists for it, quoting exactly the
    ledger hashes before and after, unedited and visible, created before the merge, counting as an approval under
    "Owner at creation" (DI-1), and used by no earlier change. An `oi-authority/1 approve` comment in the authority
    thread does not authorize an append. Returns the comment."""
    hits, threads = [], {}
    for p in a['plans']:
        key = (p['thread']['repository_id'], p['thread']['issue'])
        if key not in threads:
            threads[key] = read_thread(host, *key)
        for c in find_approval(a, threads[key], 'ledger-append', {'frm': old_sha, 'to': new_sha}, a['owner']['id'],
                               merged_at):
            f = parse_form(a, c['body'])[1]
            if f['plan'] == p['plan_id'] and f['round'] in p['rounds'] and c['id'] not in [h['id'] for h in hits]:
                hits.append(c)
    # single use first (an approval that authorized an earlier change refuses), then "Owner at creation"
    ok = [c for c in _fresh(hits, consumed, 'ledger', what) if counts_as_approval(tl, c, a['owner']['id'], merged_at)]
    if len(ok) != 1:
        refuse('ledger', '%s has no verified oi-freeze-ledger/1 append comment in a plan thread that counts under '
                         'Owner at creation' % what)
    return ok[0]


def _ledger_authority_approval(host, a, tl, old_sha, new_sha, merged_at, consumed, what):
    """The authority-change procedure's approval of a ledger change (sec. 6.3, "How it changes"): an
    `oi-authority/1 approve` comment by the owner of `a` in `a`'s authority thread, quoting exactly the ledger hashes
    before ("none" for the first ledger) and after, unedited and visible, created before the merge, counting as an
    approval under "Owner at creation" (DI-1), and used by no earlier change. Returns the comment."""
    cs = read_thread(host, a['authority_thread']['repository_id'], a['authority_thread']['issue'])
    hits = find_approval(a, cs, 'authority-approve', {'frm': old_sha, 'to': new_sha}, a['owner']['id'], merged_at)
    ok = [c for c in _fresh(hits, consumed, 'ledger', what) if counts_as_approval(tl, c, a['owner']['id'], merged_at)]
    if len(ok) != 1:
        refuse('ledger', '%s has no verified oi-authority/1 approve comment in the authority thread that counts under '
                         'Owner at creation' % what)
    return ok[0]


def added_event_ids(old, new):
    """The item ids of a ledger change's review (sec. 6.3: one verdict per item id of the reviewed record; the items of
    a ledger change's review are the events the change adds, each identified by its comment id). Returns (ids, None),
    or (None, reason) when an added event has no comment id or two added events share one."""
    o = _ledger_events(old, 'the previous ledger') if old is not None else []
    n = _ledger_events(new, 'the ledger')
    ids = []
    for ev in n[len(o):]:
        cid = ev.get('comment_id') if isinstance(ev, dict) else None
        if isinstance(cid, bool) or not isinstance(cid, (int, str)) or cid == '':
            return None, 'an added event has no comment id'
        ids.append(str(cid))
    if len(ids) != len(set(ids)):
        return None, 'two added events share a comment id'
    return ids, None


def _review_problem(rv, a, new_sha, old_sha, items=None):
    """None when `rv` (the bytes of the review record, or None) is a valid independent review record (sec. 6.3) of
    the change from `old_sha` to `new_sha`: schema oi-review-record/1, naming both blobs, by a reviewer other than the
    owner, with a method, at least one verdict and every verdict accept. With `items` (the event ids a ledger change
    adds), one verdict per item: an item without a verdict, an item with two, or one not `accept` refuses. Otherwise
    the reason."""
    try:
        rvd = json.loads(rv.decode('utf-8')) if rv else None
    except (ValueError, UnicodeDecodeError):
        rvd = None
    if not isinstance(rvd, dict) or rvd.get('schema') != 'oi-review-record/1' or \
            not isinstance(rvd.get('reviewed'), dict) or rvd['reviewed'].get('blob_sha256') != new_sha or \
            rvd.get('previous') != old_sha or rvd.get('reviewer') in (None, a['owner']['login']) or \
            not isinstance(rvd.get('verdicts'), list) or not rvd['verdicts'] or \
            any(not isinstance(x, dict) or x.get('verdict') != 'accept' for x in rvd['verdicts']):
        return 'has no valid independent review record'
    if items:
        named = [str(x.get('item')) for x in rvd['verdicts']]
        missing = [i for i in items if i not in named]
        if missing:
            return 'has a review record with no verdict for added event %s' % missing[0]
        dup = sorted({i for i in named if named.count(i) > 1})
        if dup:
            return 'has a review record with more than one verdict for item %s' % dup[0]
    return None


# ---- the authority-change procedure ---------------------------------------------------------------------------

def review_path(a, to_sha):
    base = a['freeze_ledger_path'].rsplit('/', 1)[0]
    return '%s/authority-reviews/%s.json' % (base, to_sha)


def ledger_review_path(a, from_sha, to_sha):
    """The review record of a freeze-ledger change, named by both ledger blobs ("none" before the first)."""
    base = a['freeze_ledger_path'].rsplit('/', 1)[0]
    return '%s/ledger-reviews/%s-%s.json' % (base, from_sha, to_sha)


def timeline_of(a_versions):
    """The owner timeline (DI-1) of the verified versions of A: [(commit, A, merged_at, blob sha256)]."""
    return OwnerTimeline([(m, x['owner']['id'], b) for _, x, m, b in a_versions])


def in_force(a_versions, t, what):
    """The version of A in force at `t` (sec. 6.3, "Owner at creation"): the latest verified version whose merge time
    is strictly before `t`. A version merged at `t` is not yet in force."""
    got = None
    for _, a, m, _b in a_versions:
        if m < t:
            got = a
    if got is None:
        refuse('ledger', '%s merged when no verified authority record was in force' % what)
    return got


def _verify_ledger_change(host, a, tl, prev_blob, blob, merged_at, consumed, what, review_bytes):
    """One freeze-ledger change from `prev_blob` (None for the first) to `blob`, governed by `a`, merged at `merged_at`
    (None for a change not yet merged, as at an acceptance landing): append-only; the owner's oi-authority/1 approve
    comment; the independent review record, one verdict per added event; and, when it adds events, its own
    oi-freeze-ledger/1 append comment (N3). Each approval counts under "Owner at creation". Returns (approval id,
    append approval id or None); the caller consumes them."""
    new_sha = util.sha256(blob)
    old_sha = util.sha256(prev_blob) if prev_blob is not None else 'none'
    # the ledger is append-only (sec. 6.3): each version extends the previous one, so no change can be reverted and
    # re-applied under an approval already given
    if prev_blob is not None:
        why = _ledger_extension_problem(prev_blob, blob)
        if why:
            refuse('ledger', '%s is not an append: %s' % (what, why))
    approval = _ledger_authority_approval(host, a, tl, old_sha, new_sha, merged_at, consumed, what)
    items, why = added_event_ids(prev_blob, blob)
    if why:
        refuse('ledger', '%s: %s' % (what, why))
    why = _review_problem(review_bytes, a, new_sha, old_sha, items)
    if why:
        refuse('ledger', '%s %s' % (what, why))
    # and, for a change that adds events, its own append comment (N3): every change after the first adds events
    # (append-only, above); the first adds events unless it is empty
    append = None
    if prev_blob is not None or _ledger_events(blob, what):
        append = _ledger_append_approval(host, a, tl, old_sha, new_sha, merged_at, consumed, what)['id']
    return approval['id'], append


def verify_history(host, repo_id, path, governing, main, kind, a_versions=None, consumed=None):
    """Every version of `path` on main passed its approval procedure. kind: 'authority' or 'ledger'.
    Returns the list of versions with their approvals. For kind 'authority', `a_versions` (a list) receives
    (commit, parsed A, merge time, blob sha256) for every verified version; for kind 'ledger' it supplies them, and
    each ledger change is governed by the version of A in force when it merged. `consumed` (a set, shared between the
    authority and the ledger histories) holds the approval comment ids already used: each comment authorizes one
    change. Every approval counts under "Owner at creation" (DI-1). Each ledger version extends the previous one, and
    each ledger change has a merge record. Every ledger change passes the authority-change procedure (an approval
    comment in the authority thread, an independent review record naming both blobs with one verdict per added
    event, and a pull-request merge by the owner), and one that adds events also needs its own append comment in a
    plan thread (N3); none of these stands in for another."""
    if consumed is None:
        consumed = set()
    try:
        hist = host.file_history(repo_id, path)
    except HostUnavailable as exc:
        refuse('history', 'the history of %s cannot be read: %s' % (path, exc))
    out = []
    seen = [] if a_versions is None else a_versions
    prev_blob, prev_a, prev_merged_at = None, None, None
    for v in hist:
        blob = v['blob']
        if blob is None:
            refuse('history', '%s was deleted on main' % path)
        # every version, of A and of the ledger, landed by a verifiable pull-request merge (sec. 6.3)
        why = _provenance_problem(host, repo_id, path, main, v, prev_blob, prev_merged_at)
        if why:
            refuse('authority' if kind == 'authority' else 'ledger', '%s change %s %s' % (
                'authority' if kind == 'authority' else 'freeze-ledger', v['commit'][:12], why))
        new_sha = util.sha256(blob)
        old_sha = util.sha256(prev_blob) if prev_blob is not None else 'none'
        merged_at = v['merged_at']
        if kind == 'authority':
            new_a = parse_authority(blob)
            if prev_a is None and new_a.get('supersedes') is not None:
                refuse('authority', 'the first authority record must have supersedes null')
            # DI-2: A's lineage is its fixed path; supersedes names the version preceding it on main's first-parent
            # chain, at the same path
            if prev_a is not None and (not isinstance(new_a.get('supersedes'), dict) or
                                       new_a['supersedes'].get('blob_sha256') != old_sha or
                                       new_a['supersedes'].get('path') != path):
                refuse('authority', 'the authority record does not supersede the version preceding it on main')
            gov = prev_a or new_a
            tl = timeline_of(seen)
            cs = read_thread(host, gov['authority_thread']['repository_id'], gov['authority_thread']['issue'])
            what = 'authority change %s' % v['commit'][:12]
            found = _fresh(find_approval(gov, cs, 'authority-approve', {'frm': old_sha, 'to': new_sha},
                                         gov['owner']['id'], merged_at), consumed, 'authority', what)
            if prev_a is None:
                # the first A: approved by the id it pins, authenticated as that id, created before the merge
                hits = [c for c in found if not tl.changed_between(c['created_at'], merged_at)]
            else:
                hits = [c for c in found if counts_as_approval(tl, c, gov['owner']['id'], merged_at)]
            if len(hits) != 1:
                refuse('authority', 'authority change %s has %d valid approvals by the owner id that count under '
                                    'Owner at creation' % (v['commit'][:12], len(hits)))
            used = [hits[0]['id']]
            if prev_a is not None and new_a['owner']['id'] != prev_a['owner']['id']:
                # the new id's approval, authenticated as the id the new A pins: created before the merge, with no
                # owner change merged between its creation and the merge
                co = [c for c in _fresh(find_approval(gov, cs, 'authority-approve', {'frm': old_sha, 'to': new_sha},
                                                      new_a['owner']['id'], merged_at), consumed, 'authority', what)
                      if not tl.changed_between(c['created_at'], merged_at)]
                if len(co) != 1:
                    refuse('authority', 'an owner-id change needs the approval of the new id as well, created before '
                                        'the merge with no owner change merged in between')
                used.append(co[0]['id'])
            if v.get('merged_by_id') != gov['owner']['id']:
                refuse('authority', 'authority change %s was merged by another account' % v['commit'][:12])
            if _review_problem(host.file_at(repo_id, main, review_path(new_a, new_sha)), gov, new_sha, old_sha):
                refuse('authority', 'authority change %s has no valid independent review record' % v['commit'][:12])
            consumed.update(used)
            prev_a = new_a
            seen.append((v['commit'], new_a, merged_at, new_sha))
            out.append({'commit': v['commit'], 'blob_sha256': new_sha, 'approval': hits[0]['id'],
                        'owner_id': new_a['owner']['id'], 'merged_at': merged_at})
        else:
            what = 'freeze-ledger change %s' % v['commit'][:12]
            # the governing A is the version in force when this ledger change merged (sec. 6.3); the owner of a
            # superseded version keeps no authority over a change merged after its supersession
            a = in_force(seen, merged_at, what) if seen else governing
            tl = timeline_of(seen) if seen else OwnerTimeline([])
            review = host.file_at(repo_id, main, ledger_review_path(a, old_sha, new_sha))
            approval, append = _verify_ledger_change(host, a, tl, prev_blob, blob, merged_at, consumed, what, review)
            if v.get('merged_by_id') != a['owner']['id']:
                refuse('ledger', '%s was merged by another account' % what)
            consumed.update([approval] + ([append] if append is not None else []))
            out.append({'commit': v['commit'], 'blob_sha256': new_sha, 'approval': approval,
                        'append_approval': append, 'merged_at': merged_at})
        prev_blob = blob
        prev_merged_at = merged_at
    return out


def check_ledger_landing(host, repo_id, new_ledger, review_bytes):
    """The landing check of a freeze-ledger change not yet merged, as an acceptance landing carries it (sec. 6.3, N3):
    main's authority and ledger histories verify; the change extends main's ledger; and it carries all its components,
    each approval counting under "Owner at creation" with main's current A as the governing authority record and no
    owner change merged after the approval's creation. Raises Refused: the landing does not merge. Returns the
    approval ids."""
    try:
        main = host.main_head(repo_id)
        a_bytes = host.file_at(repo_id, main, authority_path)
    except HostUnavailable as exc:
        refuse('ledger', 'main cannot be read: %s' % exc)
    if a_bytes is None:
        refuse('ledger', 'no authority record on main')
    a = parse_authority(a_bytes)
    a_versions, consumed = [], set()
    versions = verify_history(host, repo_id, authority_path, None, main, 'authority', a_versions=a_versions,
                              consumed=consumed)
    if not versions or versions[-1]['blob_sha256'] != util.sha256(a_bytes):
        refuse('authority', 'the authority record on main has no verified history')
    verify_history(host, repo_id, a['freeze_ledger_path'], a, main, 'ledger', a_versions=a_versions,
                   consumed=consumed)
    old = host.file_at(repo_id, main, a['freeze_ledger_path'])
    approval, append = _verify_ledger_change(host, a, timeline_of(a_versions), old, new_ledger, None, consumed,
                                             'the freeze-ledger change of the landing', review_bytes)
    return {'approval': approval, 'append_approval': append}


# ---- admission ------------------------------------------------------------------------------------------------

def read_pin_table(prereg):
    """The digest table of the last "Record pins" subsection: rows "| `file` | `sha256` |"."""
    t = prereg.decode('utf-8')
    heads = [m.start() for m in re.finditer(r'^### \d+\.\d+ Record pins\b', t, re.M)]
    if not heads:
        return {}
    i = heads[-1]
    j = t.find('\n#', i + 5)
    return dict(re.findall(r'^\| `([\w./-]+)` \| `([0-9a-f]{64})` \|', t[i:j if j > 0 else None], re.M))


def snapshot_events(data, path):
    """The events of a committed admission snapshot (sec. 6.3, reconciliation), each carrying its plan and round. The
    admission snapshot records `plan` and `round` once, at its top level; an event's own value, where it has one, must
    agree with it. An event with neither, or with one that contradicts the top level, refuses: an event whose plan and
    round cannot be established would otherwise never bind."""
    try:
        doc = json.loads(data.decode('utf-8'))
    except (ValueError, UnicodeDecodeError, AttributeError):
        refuse('ledger', 'a committed snapshot cannot be read: %s' % path)
    if not isinstance(doc, dict) or not isinstance(doc.get('events', []), list):
        refuse('ledger', 'a committed snapshot cannot be read: %s' % path)
    out = []
    for ev in doc.get('events', []):
        if not isinstance(ev, dict):
            refuse('ledger', 'a committed snapshot has an event that is not an object: %s' % path)
        ev = dict(ev)
        for key in ('plan', 'round'):
            top = doc.get(key)
            if ev.get(key) is None:
                if top is None:
                    refuse('ledger', 'an event of committed snapshot %s has no %s, in the event or at the top level'
                           % (path, key))
                ev[key] = top
            elif top is not None and ev[key] != top:
                refuse('ledger', 'an event of committed snapshot %s names %s %r, the snapshot %r'
                       % (path, key, ev[key], top))
        out.append(ev)
    return out


def admit(host, git, run_id, plan_id, round_id, freeze, config_path, config_sha=None, attested_repo=None):
    """Points 1-8. Returns (A, the admission snapshot, the pin table). Raises Refused."""
    snap = {'plan': plan_id, 'round': round_id, 'freeze': freeze}
    # point 1: the host's attestation of the run
    try:
        run = host.run_record(run_id, attested_repo)
    except HostUnavailable as exc:
        refuse('run', 'the run record cannot be read: %s' % exc)
    if run is None:
        refuse('run', 'no run record')
    repo_id = run['repository_id']
    if run.get('fork'):
        refuse('run', 'the run is in a fork')
    # point 2: A from main of the attested repository
    try:
        main = host.main_head(repo_id)
        a_bytes = host.file_at(repo_id, main, authority_path)
    except HostUnavailable as exc:
        refuse('authority', 'main cannot be read: %s' % exc)
    if a_bytes is None:
        refuse('authority', 'no authority record on main')
    a = parse_authority(a_bytes)
    if a['repository']['id'] != repo_id:
        refuse('run', 'the attested repository is not the authority record\'s')
    if run['workflow_path'] != a['workflow']['path']:
        refuse('run', 'the run\'s workflow is not the pinned workflow path')
    # point 3: execution identity
    head = run['head_sha']
    try:
        on_main = host.on_first_parent_chain(repo_id, head, main)
        wf = host.file_at(repo_id, head, a['workflow']['path'])
        a_head = host.file_at(repo_id, head, authority_path)
        tool_entries = host.entries_at(repo_id, head, tool_dir)
    except HostUnavailable as exc:
        refuse('identity', 'execution identity cannot be read: %s' % exc)
    if not on_main:
        refuse('identity', 'the run\'s commit is not on main\'s first-parent chain')
    if head == freeze or head in (snap.get('x'),):
        refuse('identity', 'the run\'s commit is an evaluated commit')
    if wf is None or util.sha256(wf) != a['workflow']['content_sha256']:
        refuse('identity', 'the workflow at the run\'s commit does not hash to its pin')
    if a_head is None:
        refuse('identity', 'the run\'s commit does not contain the authority record')
    pins = a['engine_pins']
    # point 3 (K7, design v5.5.8): besides the files A.engine_pins names, exactly the authority record (blob equal to the
    # admitted A) and the workflow at A.workflow.path (if it lies there), each only as a regular file; any other
    # entry, a second copy of either, a changed file, a symlink or a submodule refuses
    permitted = {authority_path: util.sha256(a_bytes), a['workflow']['path']: a['workflow']['content_sha256']}
    for p, kind in tool_entries:
        if p not in pins and p not in permitted:
            refuse('identity', 'a file under the tool is neither pinned nor permitted: %s' % p)
        if kind != 'file':
            refuse('identity', '%s at the run\'s commit is a %s, not a regular file' % (p, kind))
    if util.sha256(a_head) != util.sha256(a_bytes):
        refuse('identity', 'the authority record at the run\'s commit differs from the admitted one')
    for p, want in sorted(pins.items()):
        b = host.file_at(repo_id, head, p)
        if b is None or util.sha256(b) != want:
            refuse('identity', 'tool file %s at the run\'s commit differs from its pin' % p)
    # the authority-change procedure over every version of A on main
    a_versions = []
    consumed = set()
    versions = verify_history(host, repo_id, authority_path, None, main, 'authority', a_versions=a_versions,
                              consumed=consumed)
    if not versions or versions[-1]['blob_sha256'] != util.sha256(a_bytes):
        refuse('authority', 'the authority record on main has no verified history')
    # F must contain A, a verified version
    f_a = git.read(freeze, authority_path)
    if f_a is None:
        refuse('authority', 'the freeze does not descend from a main commit with the authority record')
    if util.sha256(f_a) not in {v['blob_sha256'] for v in versions}:
        refuse('authority', 'the freeze carries an authority record that main never adopted')
    plan = [p for p in a['plans'] if p['plan_id'] == plan_id]
    if len(plan) != 1 or round_id not in plan[0]['rounds']:
        refuse('plan', 'plan or round not listed in the authority record')
    plan = plan[0]
    thread = (plan['thread']['repository_id'], plan['thread']['issue'])
    # point 2 and 3 on the plan's thread
    cs = read_thread(host, *thread)
    deleted = host.deletion_events(*thread)
    if deleted:
        refuse('thread', 'the host reports deleted comments in the thread')
    # DI-1: the owner timeline of the verified versions of A, for "Owner at creation"
    tl = timeline_of(a_versions)
    own, impostors = owner_comments(a, cs, tl)
    # the freeze ledger, its approvals, and the committed snapshots
    try:
        led_b = host.file_at(repo_id, main, a['freeze_ledger_path'])
    except HostUnavailable as exc:
        refuse('ledger', 'the freeze ledger cannot be read: %s' % exc)
    if led_b is None:
        refuse('ledger', 'no freeze ledger on main')
    try:
        ledger = json.loads(led_b.decode('utf-8'))
    except ValueError:
        refuse('ledger', 'the freeze ledger is not valid json')
    if ledger.get('schema') != ledger_schema or not isinstance(ledger.get('events'), list):
        refuse('ledger', 'the freeze ledger is not an oi-freeze-ledger/1 record')
    led_versions = verify_history(host, repo_id, a['freeze_ledger_path'], a, main, 'ledger', a_versions=a_versions,
                                  consumed=consumed)
    if not led_versions or led_versions[-1]['blob_sha256'] != util.sha256(led_b):
        refuse('ledger', 'the freeze ledger on main has no verified history')
    snap_events = []
    snaps_dir = a['freeze_ledger_path'].rsplit('/', 1)[0] + '/landings/'
    for p in host.paths_at(repo_id, main, snaps_dir):
        if p.endswith('/snapshot.json'):
            snap_events += snapshot_events(host.file_at(repo_id, main, p), p)
    # point 4: the forms
    forms = []
    for c in own:
        f = parse_form(a, c['body'])
        if f is None:
            continue
        if f[0] == 'malformed':
            refuse('forms', 'owner comment %s has a malformed or unknown form: %r' % (c['id'], f[1]))
        if f[0].startswith('freeze-'):
            if f[1]['plan'] not in [p['plan_id'] for p in a['plans']]:
                refuse('forms', 'owner comment %s names a plan the authority record does not list' % c['id'])
            forms.append((c, f))
    # reconciliation of the thread with the ledger and the snapshots. A recorded event is no source of authority: a
    # withdrawal or supersession binds only by revoking its commit, even when its comment is gone; a recorded event
    # that names a comment present in the thread must agree with it, and that comment must have been an owner comment
    # at its creation (sec. 6.3, "Owner at creation")
    by_id = {c['id']: c for c in cs}
    bound = []
    for ev in list(ledger['events']) + snap_events:
        if ev.get('plan') != plan_id or ev.get('round') != round_id:
            continue
        c = by_id.get(ev['comment_id'])
        if c is not None and (c['author_id'] != ev['author_id'] or first_line(c['body']) != ev['first_line']):
            refuse('ledger', 'a recorded event conflicts with the thread (comment %s)' % ev['comment_id'])
        if c is not None and not tl.owner_comment(c['author_id'], c['created_at']):
            refuse('ledger', 'a recorded event names comment %s, which was not an owner comment at its creation'
                   % ev['comment_id'])
        if ev['kind'] in ('withdraw', 'supersede'):
            bound.append(ev)
        elif ev['kind'] == 'designate' and c is None:
            pass  # a ledger entry alone never designates
    # point 5: deterministic state. Each form, and each half of a supersession, is processed only if it counts under
    # "Owner at creation": a withdrawal and the revoking half of a supersession if they are owner comments; a
    # designation and the designating half of a supersession if they are owner comments by the owner of the governing
    # A with no owner change merged since their creation. A recorded supersession only revokes.
    events = []
    for c, (name, fields) in forms:
        if fields['plan'] != plan_id or fields['round'] != round_id:
            continue
        kind = name[len('freeze') + 1:]
        events.append({'kind': kind, 'commit': fields['commit'], 'by': fields.get('by'), 'comment_id': c['id'],
                       'created_at': c['created_at'], 'author_id': c['author_id'], 'first_line': first_line(c['body'])})
    seen = {e['comment_id'] for e in events}
    for ev in bound:
        if ev['comment_id'] not in seen:
            events.append({'kind': ev['kind'], 'commit': ev['commit'], 'by': ev.get('by'),
                           'comment_id': ev['comment_id'], 'created_at': ev['created_at'],
                           'author_id': ev['author_id'], 'first_line': ev['first_line'], 'bound': True})
    events.sort(key=lambda e: (e['created_at'], e['comment_id']))
    for e in events:
        e['owner_comment'] = tl.owner_comment(e['author_id'], e['created_at'])
        e['designates'] = not e.get('bound') and e['owner_comment'] and e['author_id'] == a['owner']['id'] and \
            not tl.changed_between(e['created_at'])
    state = {}
    # for the test "naming a commit never designated", a designation that was an owner comment at its creation has
    # designated its commit, even if it is not processed (point 5)
    ever = set()

    def revoke(e, commit):
        if state.get(commit) == 'revoked':
            refuse('state', 'a %s names a revoked commit' % e['kind'])
        if state.get(commit) != 'designated' and commit not in ever:
            refuse('state', 'a %s names a commit never designated' % ('withdrawal' if e['kind'] == 'withdraw'
                                                                      else 'supersession'))
        state[commit] = 'revoked'

    def designate(e, commit):
        if state.get(commit) == 'revoked':
            refuse('state', 'a revoked commit is designated again')
        live = [k for k, v in state.items() if v == 'designated' and k != commit]
        if live:
            refuse('state', 'two live designations in one round')
        state[commit] = 'designated'
        e['processed'] = True
    for e in events:
        if e['kind'] == 'designate':
            if e['owner_comment'] and not e.get('bound'):
                ever.add(e['commit'])
            if e['designates']:
                designate(e, e['commit'])
        elif e['kind'] == 'withdraw':
            if e['owner_comment']:
                revoke(e, e['commit'])
                e['processed'] = True
        elif e['kind'] == 'supersede':
            if e['owner_comment']:
                revoke(e, e['commit'])
                e['processed'] = True
                if not e.get('bound'):
                    ever.add(e['by'])
            if e['designates']:
                designate(e, e['by'])
    live = [k for k, v in state.items() if v == 'designated']
    if live != [freeze]:
        refuse('state', 'the freeze is not the one designated commit of the round (designated: %s)' % live)
    designation = [e for e in events if e['designates'] and e['kind'] in ('designate', 'supersede') and
                   (e['commit'] == freeze if e['kind'] == 'designate' else e['by'] == freeze)][-1]
    # point 6: the pin table, authenticated by the designation of exactly F
    prereg = git.read(freeze, plan['pin_table_path'])
    if prereg is None:
        refuse('pins', 'the freeze has no pin table at %s' % plan['pin_table_path'])
    table = read_pin_table(prereg)
    rec_dir = plan['pin_table_path'].rsplit('/', 1)[0] + '/'
    cfg_b = git.read(freeze, config_path)
    if cfg_b is None or not config_path.startswith(rec_dir):
        refuse('pins', 'the configuration is not in the plan\'s record directory at the freeze')
    name = config_path[len(rec_dir):]
    if table.get(name) != util.sha256(cfg_b):
        refuse('pins', 'the configuration is absent from the freeze\'s pin table, or has another sha256 there')
    if config_sha is not None and config_sha != util.sha256(cfg_b):
        refuse('pins', 'the configuration does not equal --config-sha256')
    snap.update({
        'owner_id': a['owner']['id'], 'repository_id': a['repository']['id'],
        'authority_sha256': util.sha256(a_bytes), 'authority_versions': versions,
        'run': {'run_id': run_id, 'repository_id': repo_id, 'fork': bool(run.get('fork')),
                'workflow_path': run['workflow_path'], 'workflow_sha256': util.sha256(wf), 'head_sha': head,
                'tool_blobs': {p: pins[p] for p in sorted(pins)}},
        'main': main, 'thread': {'repository_id': thread[0], 'issue': thread[1],
                                 'comment_ids': [c['id'] for c in cs], 'count': len(cs)},
        'owner_comments': [comment_record(c, tl) for c in own], 'impostor_comments': impostors,
        'freeze_ledger': {'path': a['freeze_ledger_path'], 'blob_sha256': util.sha256(led_b),
                          'versions': led_versions},
        'events': events, 'designation_comment_id': designation['comment_id'],
        'pin_table': {'path': plan['pin_table_path'], 'blob_sha256': util.sha256(prereg), 'entries': table},
        'pin_table_sha256': util.sha256(prereg),
    })
    return a, snap, table, rec_dir


def admitted_by_table(git, freeze, rec_dir, table):
    """Blobs the pin table admits, read from the freeze's tree: {path: bytes}."""
    out = {}
    for name, want in table.items():
        b = git.read(freeze, rec_dir + name)
        if b is not None and util.sha256(b) == want:
            out[rec_dir + name] = b
    return out


def snapshot_sha(snap):
    return util.fingerprint(snap)
