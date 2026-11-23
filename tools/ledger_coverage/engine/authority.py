"""Configuration admission and its root of trust (sec. 6.3): the tool authority record `A`, the versioned comment
forms, the authority-change procedure, the freeze ledger with its approved appends, the deterministic designation
state, the plan's pin table, and the admission snapshot.

Every failure refuses admission (an error of class config-unreviewed). The caller supplies only the commits and the plan
and round names; every authority value comes from `A`, read from `main` of the attested repository.
"""
import json
import re

from . import util
from .host import HostUnavailable, first_line

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


def owner_comments(a, cs):
    """Point 3 over every owner comment; returns the owner comments and the reported impostors."""
    own, impostors = [], []
    for c in cs:
        if c.get('author_id') != a['owner']['id']:
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


def comment_record(c):
    return {'id': c['id'], 'author_id': c['author_id'], 'created_at': c['created_at'],
            'edited': bool(c['edits']) or bool(c.get('edited')), 'hidden': c['hidden'],
            'first_line': first_line(c['body']), 'body_sha256': util.sha256(c['body'])}


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


# ---- the authority-change procedure ---------------------------------------------------------------------------

def review_path(a, to_sha):
    base = a['freeze_ledger_path'].rsplit('/', 1)[0]
    return '%s/authority-reviews/%s.json' % (base, to_sha)


def in_force(host, repo_id, a_versions, commit):
    """The version of A in force when `commit` merged: the latest verified version of A merged before it on main's
    first-parent chain. A version merged in the same commit takes effect with that merge, so it governs a change
    only when no version merged before it exists (the first landing of A and the ledger together)."""
    before, same = None, None
    for c, a in a_versions:
        if c == commit:
            same = a
        else:
            try:
                earlier = host.on_first_parent_chain(repo_id, c, commit)
            except HostUnavailable as exc:
                refuse('history', 'the order of the authority and ledger changes cannot be read: %s' % exc)
            if earlier:
                before = a
    got = before or same
    if got is None:
        refuse('ledger', 'freeze-ledger change %s precedes every verified authority record' % commit[:12])
    return got


def verify_history(host, repo_id, path, governing, main, kind, plan_threads=None, a_versions=None, consumed=None):
    """Every version of `path` on main passed its approval procedure. kind: 'authority' or 'ledger'.
    Returns the list of versions with their approvals. For kind 'authority', `a_versions` (a list) receives
    (commit, parsed A) for every verified version; for kind 'ledger' it supplies them, and each ledger change is
    approved by the owner of the version in force when it merged. `consumed` (a set, shared between the authority
    and the ledger histories) holds the approval comment ids already used: each comment authorizes one change.
    Each ledger version extends the previous one, and each ledger change has a merge record."""
    if consumed is None:
        consumed = set()
    try:
        hist = host.file_history(repo_id, path)
    except HostUnavailable as exc:
        refuse('history', 'the history of %s cannot be read: %s' % (path, exc))
    out = []
    prev_blob, prev_a = None, None
    for v in hist:
        blob = v['blob']
        if blob is None:
            refuse('history', '%s was deleted on main' % path)
        new_sha = util.sha256(blob)
        old_sha = util.sha256(prev_blob) if prev_blob is not None else 'none'
        if kind == 'authority':
            new_a = parse_authority(blob)
            if prev_a is None and new_a.get('supersedes') is not None:
                refuse('authority', 'the first authority record must have supersedes null')
            if prev_a is not None and (new_a.get('supersedes') or {}).get('blob_sha256') != old_sha:
                refuse('authority', 'the authority record does not supersede the previous one')
            gov = prev_a or new_a
            cs = read_thread(host, gov['authority_thread']['repository_id'], gov['authority_thread']['issue'])
            what = 'authority change %s' % v['commit'][:12]
            hits = _fresh(find_approval(gov, cs, 'authority-approve', {'frm': old_sha, 'to': new_sha},
                                        gov['owner']['id'], v.get('merged_at')), consumed, 'authority', what)
            if len(hits) != 1:
                refuse('authority', 'authority change %s has %d valid approvals by the owner id' % (v['commit'][:12],
                                                                                                   len(hits)))
            used = [hits[0]['id']]
            if prev_a is not None and new_a['owner']['id'] != prev_a['owner']['id']:
                co = _fresh(find_approval(gov, cs, 'authority-approve', {'frm': old_sha, 'to': new_sha},
                                          new_a['owner']['id'], v.get('merged_at')), consumed, 'authority', what)
                if len(co) != 1:
                    refuse('authority', 'an owner-id change needs the approval of the new id as well')
                used.append(co[0]['id'])
            if v.get('merged_by_id') != gov['owner']['id']:
                refuse('authority', 'authority change %s was merged by another account' % v['commit'][:12])
            rv = host.file_at(repo_id, main, review_path(new_a, new_sha))
            try:
                rvd = json.loads(rv.decode('utf-8')) if rv else None
            except ValueError:
                rvd = None
            if not rvd or rvd.get('schema') != 'oi-review-record/1' or \
                    rvd.get('reviewed', {}).get('blob_sha256') != new_sha or rvd.get('previous') != old_sha or \
                    rvd.get('reviewer') in (None, gov['owner']['login']) or \
                    any(x.get('verdict') != 'accept' for x in rvd.get('verdicts', [])) or not rvd.get('verdicts'):
                refuse('authority', 'authority change %s has no valid independent review record' % v['commit'][:12])
            consumed.update(used)
            prev_a = new_a
            if a_versions is not None:
                a_versions.append((v['commit'], new_a))
            out.append({'commit': v['commit'], 'blob_sha256': new_sha, 'approval': hits[0]['id'],
                        'owner_id': new_a['owner']['id']})
        else:
            what = 'freeze-ledger change %s' % v['commit'][:12]
            # a ledger change lands by a pull-request merge, whose time bounds its approval (sec. 6.3); a change
            # with no merge record (a direct push) is refused
            if v.get('merged_at') is None:
                refuse('ledger', '%s has no merge record' % what)
            # the ledger is append-only (sec. 6.3): each version extends the previous one, so no change can be
            # reverted and re-applied under an approval already given
            if prev_blob is not None:
                why = _ledger_extension_problem(prev_blob, blob)
                if why:
                    refuse('ledger', '%s is not an append: %s' % (what, why))
            # the approver is the owner of the version of A in force when this ledger change merged (sec. 6.3); the
            # owner of a superseded version keeps no authority over a change merged after its supersession
            a = in_force(host, repo_id, a_versions, v['commit']) if a_versions else governing
            oid = a['owner']['id']
            cs_auth = read_thread(host, a['authority_thread']['repository_id'], a['authority_thread']['issue'])
            hits = find_approval(a, cs_auth, 'authority-approve', {'frm': old_sha, 'to': new_sha}, oid,
                                 v.get('merged_at'))
            if not [c for c in hits if c['id'] not in consumed]:
                for (rid, issue), (plan, rnd) in (plan_threads or {}).items():
                    cs = read_thread(host, rid, issue)
                    h = find_approval(a, cs, 'ledger-append', {'frm': old_sha, 'to': new_sha}, oid,
                                      v.get('merged_at'))
                    hits += h
                    if [c for c in h if c['id'] not in consumed]:
                        break
            ok = _fresh(hits, consumed, 'ledger', what)
            if len(ok) != 1:
                refuse('ledger', '%s has no verified approval comment' % what)
            consumed.add(ok[0]['id'])
            out.append({'commit': v['commit'], 'blob_sha256': new_sha, 'approval': ok[0]['id']})
        prev_blob = blob
    return out


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
    # point 3 (K7, v5.5.3): besides the files A.engine_pins names, exactly the authority record (blob equal to the
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
    own, impostors = owner_comments(a, cs)
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
    led_versions = verify_history(host, repo_id, a['freeze_ledger_path'], a, main, 'ledger',
                                  {thread: (plan_id, round_id)}, a_versions=a_versions, consumed=consumed)
    if not led_versions or led_versions[-1]['blob_sha256'] != util.sha256(led_b):
        refuse('ledger', 'the freeze ledger on main has no verified history')
    snap_events = []
    snaps_dir = a['freeze_ledger_path'].rsplit('/', 1)[0] + '/landings/'
    for p in host.paths_at(repo_id, main, snaps_dir):
        if p.endswith('/snapshot.json'):
            try:
                snap_events += json.loads(host.file_at(repo_id, main, p).decode('utf-8')).get('events', [])
            except (ValueError, AttributeError):
                refuse('ledger', 'a committed snapshot cannot be read: %s' % p)
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
    # reconciliation of the thread with the ledger and the snapshots
    by_id = {c['id']: c for c in cs}
    bound = []
    for ev in list(ledger['events']) + snap_events:
        if ev.get('plan') != plan_id or ev.get('round') != round_id:
            continue
        c = by_id.get(ev['comment_id'])
        if c is not None and (c['author_id'] != ev['author_id'] or first_line(c['body']) != ev['first_line']):
            refuse('ledger', 'a recorded event conflicts with the thread (comment %s)' % ev['comment_id'])
        if ev['kind'] in ('withdraw', 'supersede'):
            bound.append(ev)
        elif ev['kind'] == 'designate' and c is None:
            pass  # a ledger entry alone never designates
    # point 5: deterministic state
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
    state = {}
    for e in events:
        if e['kind'] == 'designate':
            if state.get(e['commit']) == 'revoked':
                refuse('state', 'a revoked commit is designated again')
            live = [k for k, v in state.items() if v == 'designated' and k != e['commit']]
            if live:
                refuse('state', 'two live designations in one round')
            state[e['commit']] = 'designated'
        elif e['kind'] == 'withdraw':
            if state.get(e['commit']) != 'designated':
                refuse('state', 'a withdrawal names a commit that is not designated')
            state[e['commit']] = 'revoked'
        elif e['kind'] == 'supersede':
            if state.get(e['commit']) != 'designated':
                refuse('state', 'a supersession names a commit that is not designated')
            state[e['commit']] = 'revoked'
            if state.get(e['by']) == 'revoked':
                refuse('state', 'a supersession designates a revoked commit')
            state[e['by']] = 'designated'
    live = [k for k, v in state.items() if v == 'designated']
    if live != [freeze]:
        refuse('state', 'the freeze is not the one designated commit of the round (designated: %s)' % live)
    designation = [e for e in events if e['kind'] in ('designate', 'supersede') and
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
        'owner_comments': [comment_record(c) for c in own], 'impostor_comments': impostors,
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
