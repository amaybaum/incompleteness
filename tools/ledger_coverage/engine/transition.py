# The one-time transition to independently reviewed record roots (A1 staging amendment r2, sec. 2 and 3).
#
# The roles, their namespaces, root paths and record ids, and the names of the frozen control metadata are the tool's
# authority (`record_authority.transition_roles` and its neighbours), passed in by the caller: this module names no
# retirement. Everything is read from verified Git objects through the reader; an object the walk needs and cannot
# read is the reader's Unresolvable, which the caller turns into ERROR.
#
# - The activation descriptor and the prior-freeze declaration are read from the plan's Record pins table at F.
# - R6.REC.7 / R6.EVID.8 for the designated roles: the active tip of each role is determined by walking only the role's
# namespace over the verified first-parent path from B to F (or to a control snapshot S), endpoints included. B holds
# exactly the root and no other member; every later member is appended without edit at its own path, extends the
# single current tip by exact path and blob, and keeps kind and record id. A gap, rewrite, deletion, rename, mode
# change, fork, second root, foreign or malformed member blocks admission.
# - Prior-freeze continuity: a declared F_prev is a strict ancestor of F on that first-parent path, its pin table binds
# the same descriptor bytes, and a changed configuration supersedes the exact configuration F_prev's pin table binds.
import json
import re

from . import util

_hex40 = re.compile(r'^[0-9a-f]{40}$')
_sha = re.compile(r'^[0-9a-f]{64}$')
regular_modes = ('100644', '100755')


class Refused(Exception):
    """The transition does not admit the configuration: the message names the failed condition."""


def _ref(v, what):
    if not isinstance(v, dict) or set(v) != {'path', 'blob_sha256'} or not isinstance(v.get('path'), str) or \
            not v['path'] or not _sha.match(str(v.get('blob_sha256'))):
        raise Refused('%s is not {path, blob_sha256}' % what)
    return v


def _json(data, what):
    try:
        return json.loads(data.decode('utf-8'))
    except (ValueError, UnicodeDecodeError):
        raise Refused('%s is not json' % what)


def parse_descriptor(data, schema):
    """The activation descriptor: closed keys schema, base, custody, class_root, allow_root."""
    d = _json(data, 'the transition descriptor')
    if not isinstance(d, dict) or set(d) != {'schema', 'base', 'custody', 'class_root', 'allow_root'}:
        raise Refused('the transition descriptor does not have exactly the keys schema, base, custody, class_root, '
                      'allow_root')
    if d['schema'] != schema:
        raise Refused('the transition descriptor schema is not %s' % schema)
    if not isinstance(d['base'], str) or not _hex40.match(d['base']):
        raise Refused('the transition descriptor base is not a full commit id')
    for k in ('custody', 'class_root', 'allow_root'):
        _ref(d[k], 'the transition descriptor %s' % k)
    return d


def parse_prior(data, schema):
    """The prior-freeze declaration: closed keys schema, freeze (a full commit id or null)."""
    d = _json(data, 'the prior-freeze declaration')
    if not isinstance(d, dict) or set(d) != {'schema', 'freeze'}:
        raise Refused('the prior-freeze declaration does not have exactly the keys schema, freeze')
    if d['schema'] != schema:
        raise Refused('the prior-freeze declaration schema is not %s' % schema)
    if d['freeze'] is not None and (not isinstance(d['freeze'], str) or not _hex40.match(d['freeze'])):
        raise Refused('the prior-freeze declaration freeze is neither a full commit id nor null')
    return d


def first_parent_path(repo, B, F):
    """[B, ..., F] along F's verified first-parent chain; Refused if B is not on it."""
    out, c = [F], F
    while c != B:
        ps = repo.parents(c)
        if not ps:
            raise Refused('the base B %s is not on the first-parent chain of %s' % (B[:12], F[:12]))
        c = ps[0]
        out.append(c)
    out.reverse()
    return out


def in_namespace(path, role):
    d = role['directory']
    return path.startswith(d) and '/' not in path[len(d):] and path[len(d):].startswith(role['prefix'])


def members(repo, commit, role):
    """{path: (mode, object id)} of the entries directly in the role's directory whose name has its prefix."""
    return {p: e for p, e in repo.entries(commit).items() if in_namespace(p, role)}


def lineage(repo, path, role, root_pin):
    """Walks one role's namespace over the first-parent path [B, ..., S]. Returns the chain of references from the
    root to the tip, in order."""
    B = path[0]
    root = role['directory'] + role['root']
    if root_pin['path'] != root:
        raise Refused('%s root: the descriptor names %s, not the designated root %s' % (role['role'],
                                                                                       root_pin['path'], root))
    known = members(repo, B, role)
    if set(known) != {root}:
        raise Refused('%s root: B holds %s in the namespace, not exactly the root' % (role['role'],
                                                                                     sorted(known) or 'nothing'))

    def record(commit, p):
        mode = known_or_new[p][0]
        if mode not in regular_modes:
            raise Refused('%s: %s is not a regular file (mode %s)' % (role['role'], p, mode))
        data = repo.read(commit, p)
        doc = _json(data, '%s member %s' % (role['role'], p))
        if not isinstance(doc, dict) or doc.get('schema') != role['schema'] or \
                doc.get('record_id') != role['record_id'] or 'supersedes' not in doc:
            raise Refused('%s: %s is not a %s record with record_id %s' % (role['role'], p, role['schema'],
                                                                           role['record_id']))
        return {'path': p, 'blob_sha256': util.sha256(data)}, doc

    known_or_new = dict(known)
    ref, doc = record(B, root)
    if ref['blob_sha256'] != root_pin['blob_sha256']:
        raise Refused('%s root: the root at B does not hash to the descriptor\'s pin' % role['role'])
    if doc['supersedes'] is not None:
        raise Refused('%s root: supersedes is not null' % role['role'])
    chain = [ref]
    for c in path[1:]:
        current = members(repo, c, role)
        for p, e in known.items():
            if current.get(p) != e:
                raise Refused('%s: %s is deleted, renamed, rewritten or changed in mode at %s'
                              % (role['role'], p, c[:12]))
        new = {p: e for p, e in current.items() if p not in known}
        known_or_new = dict(current)
        pending = {}
        for p in sorted(new):
            r, d = record(c, p)
            if not isinstance(d['supersedes'], dict):
                raise Refused('%s: %s added at %s is a second root (supersedes null)' % (role['role'], p, c[:12]))
            pending[p] = (r, d)
        while pending:
            tip = chain[-1]
            nxt = [p for p, (r, d) in pending.items() if d['supersedes'] == tip]
            if len(nxt) != 1:
                if len(nxt) > 1:
                    raise Refused('%s: a fork at %s: %s each supersede the tip %s'
                                  % (role['role'], c[:12], sorted(nxt), tip['path']))
                raise Refused('%s: %s added at %s does not extend the current tip %s by its exact path and blob'
                              % (role['role'], sorted(pending)[0], c[:12], tip['path']))
            chain.append(pending.pop(nxt[0])[0])
        known = current
    return chain


def walk(repo, B, S, roles, descriptor):
    """{role name: chain} for every role over the verified first-parent path from B to S."""
    path = first_parent_path(repo, B, S)
    pins = {'class': descriptor['class_root'], 'allow': descriptor['allow_root']}
    return path, {r['role']: lineage(repo, path, r, pins[r['role']]) for r in roles}


def prior_continuity(path, F, prior, read_table, descriptor_name, descriptor_sha, cfg_schema):
    # Prior-freeze continuity. `read_table(commit)` returns {name: sha256} of the plan's Record pins table at the
    # commit (raising Refused if it has none) and {name: bytes} of the members it admits there. Returns the prior
    # freeze and the configuration its pin table binds, which the caller compares under R6.CFG.3.
    fp = prior['freeze']
    if fp is None:
        return {'freeze': None}
    if fp == F or fp not in path[:-1]:
        raise Refused('the declared prior freeze %s is not a strict ancestor of F on the first-parent path from B'
                      % fp[:12])
    table, blobs = read_table(fp)
    if table.get(descriptor_name) != descriptor_sha or descriptor_name not in blobs:
        raise Refused('the prior freeze does not bind the same transition descriptor')
    prev = []
    for name, b in sorted(blobs.items()):
        try:
            d = json.loads(b.decode('utf-8'))
        except (ValueError, UnicodeDecodeError):
            continue
        if isinstance(d, dict) and d.get('schema') == cfg_schema:
            prev.append((name, util.sha256(b)))
    if len(prev) != 1:
        raise Refused('the prior freeze\'s pin table binds %d configurations, not one' % len(prev))
    return {'freeze': fp, 'configuration_sha256': prev[0][1], 'configuration_name': prev[0][0]}


def representative_binding(repo, B, S, M, roles, descriptor):
    # Staging r2 sec. 2, R6.EVID.8 for A1 representative controls that select the designated roles: the reviewed
    # control inputs supply a verified record snapshot S with the same descriptor and B and a complete first-parent
    # path B..S; the bounded namespace and records checks apply to that path, and the class reference resolved at S
    # equals, by path and digest, the landed class tip in the run's M tree (the head of the same lineage over the
    # first-parent path B..M). Returns {tips at S, class tip at M}; Refused when the snapshot or the role binding
    # cannot be verified (the affected controls then stay open).
    _path_s, chains_s = walk(repo, B, S, roles, descriptor)
    _path_m, chains_m = walk(repo, B, M, roles, descriptor)
    tip_s, tip_m = chains_s['class'][-1], chains_m['class'][-1]
    if tip_s != tip_m:
        raise Refused('the class tip resolved at S (%s) is not the landed class tip in M (%s)'
                      % (tip_s['path'], tip_m['path']))
    return {'tips_at_S': {k: v[-1] for k, v in chains_s.items()}, 'class_tip_at_M': tip_m}
