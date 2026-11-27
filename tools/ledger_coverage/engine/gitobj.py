"""Read-only object access: the git object store, or in-memory commits layered over it."""
import hashlib
import os
import re
import subprocess
from types import MappingProxyType


class Unresolvable(Exception):
    pass


def blob_id_of(data):
    return hashlib.sha1(b'blob %d\x00' % len(data) + data).hexdigest()


_full = re.compile(r'^[0-9a-f]{40}$')
regular_modes = ('100644', '100755')


def tree_entry(repo, cid, path):
    """(mode, object id) of the path's entry in the commit's tree, or None: a commit changes a path when this
    differs from its parent's, so a mode-only change is a change (R6.RECON.2 (b), RC1)."""
    return repo.entries(cid).get(path)


def full_id(rev):
    """A role commit or object is named by its full 40-hex id; no ref name, abbreviation or upper case is resolved
    (sec. 6.3, object integrity)."""
    if not isinstance(rev, str) or not _full.match(rev):
        raise Unresolvable('not a full 40-hex object id (refs are not consulted): %r' % (rev,))
    return rev


def object_id(kind, data):
    return hashlib.sha1(kind.encode() + b' %d\x00' % len(data) + data).hexdigest()


def _reader_env():
    """The environment of every object read: replace refs disabled, no object fetched on demand (a lazy fetch of a
    partial clone has no permitted transport), no prompt."""
    env = dict(os.environ)
    env.update(GIT_NO_REPLACE_OBJECTS='1', GIT_NO_LAZY_FETCH='1', GIT_ALLOW_PROTOCOL='none-permitted',
               GIT_TERMINAL_PROMPT='0')
    return env


class GitRepo:
    """The verified reader (sec. 6.3, object integrity): every commit, tree and blob is requested by its full id
    through `git cat-file --batch` with replacement disabled and no lazy fetch, and its id is recomputed from its type,
    length and content. Parents, trees and tree entries with their modes are parsed from the verified content; no ref,
    graft, shallow file or commit-graph decides anything. Never writes."""

    def __init__(self, path):
        self.path = path
        self._proc = None
        self._trees = {}
        self._entries = {}
        self._paths = {}
        self._commits = {}
        self._blobs = {}
        self._objs = {}
        r = subprocess.run(['git', '-C', path, 'rev-parse', '--git-dir'], capture_output=True, text=True)
        if r.returncode:
            raise Unresolvable('not a git repository: %s' % path)

    def _git(self, *args):
        r = subprocess.run(['git', '--no-replace-objects', '-C', self.path] + list(args), capture_output=True,
                           env=_reader_env())
        return r

    def _batch(self, oid):
        """(type, content) of the object `oid`, verified against its id; (None, None) when the store lacks it."""
        full_id(oid)
        if oid in self._objs:
            return self._objs[oid]
        if self._proc is None:
            self._proc = subprocess.Popen(['git', '--no-replace-objects', '-C', self.path, 'cat-file', '--batch'],
                                          stdin=-1, stdout=-1, stderr=open(os.devnull, 'wb'), env=_reader_env())
        self._proc.stdin.write(oid.encode() + b'\n')
        self._proc.stdin.flush()
        head = self._proc.stdout.readline().decode().split()
        if len(head) < 3 or head[1] == 'missing' or head[0] != oid:
            return None, None
        size = int(head[2])
        data = self._proc.stdout.read(size)
        self._proc.stdout.read(1)
        if len(data) != size or object_id(head[1], data) != oid:
            raise Unresolvable('object %s does not hash to its id' % oid)
        self._objs[oid] = (head[1], data)
        return head[1], data

    def resolve(self, rev):
        """A role commit: a full id of a commit the store holds, verified. Refs are never consulted."""
        full_id(rev)
        self._commit(rev)
        return rev

    def _commit(self, cid):
        if cid not in self._commits:
            kind, data = self._batch(cid)
            if kind != 'commit':
                raise Unresolvable('not a commit in the object store: %s' % cid)
            head, _, msg = data.partition(b'\n\n')
            lines = head.split(b'\n')
            if not lines or not lines[0].startswith(b'tree '):
                raise Unresolvable('commit %s has no tree line' % cid)
            tree = full_id(lines[0][5:].decode('ascii', 'replace'))
            parents = []
            for line in lines[1:]:
                if not line.startswith(b'parent '):
                    break
                parents.append(full_id(line[7:].decode('ascii', 'replace')))
            when = None
            for line in lines:
                if line.startswith(b'committer '):
                    parts = line.rsplit(b' ', 2)
                    try:
                        when = int(parts[-2])
                    except (ValueError, IndexError):
                        when = None
            self._commits[cid] = {'tree': tree, 'parents': parents, 'time': when,
                                  'subject': msg.decode('utf-8', 'replace').split('\n', 1)[0]}
        return self._commits[cid]

    def committer_time(self, cid):
        """The committer time of a commit, seconds since the epoch, or None (self-declared; R6.ADJ.3 reads it as a form
        check of chronology only)."""
        return self._commit(cid).get('time')

    def _tree(self, tid):
        """[(mode, name, id)] of a verified tree object."""
        if tid not in self._trees:
            kind, data = self._batch(tid)
            if kind != 'tree':
                raise Unresolvable('not a tree in the object store: %s' % tid)
            out, i = [], 0
            while i < len(data):
                sp = data.index(b' ', i)
                nul = data.index(b'\x00', sp)
                mode = data[i:sp].decode('ascii')
                name = data[sp + 1:nul].decode('utf-8', 'surrogateescape')
                out.append((mode.zfill(6) if mode == '40000' else mode, name, data[nul + 1:nul + 21].hex()))
                i = nul + 21
            self._trees[tid] = out
        return self._trees[tid]

    def parents(self, cid):
        return list(self._commit(cid)['parents'])

    def subject(self, cid):
        return self._commit(cid)['subject']

    def tree_id(self, cid, prefix=''):
        tid = self._commit(cid)['tree']
        for part in [x for x in prefix.strip('/').split('/') if x]:
            got = [e for e in self._tree(tid) if e[1] == part and e[0] == '040000']
            if not got:
                return None
            tid = got[0][2]
        return tid

    def entries(self, cid):
        """{path: (mode, id)} of every non-tree entry of the commit's tree (blobs, symlinks and submodules), parsed
        from verified tree objects. Built once per commit id, after every tree it lists has been verified, and
        returned as a read-only view, so that no caller can change what later calls return."""
        if cid not in self._entries:
            out = {}

            def walk(tid, pre):
                for mode, name, oid in self._tree(tid):
                    if mode == '040000':
                        walk(oid, pre + name + '/')
                    else:
                        out[pre + name] = (mode, oid)
            walk(self._commit(cid)['tree'], '')
            self._entries[cid] = MappingProxyType(out)
        return self._entries[cid]

    def paths(self, cid):
        """{path: blob id} of every blob entry (regular files and symlinks), as `ls-tree` listed them: a read-only
        view, built once per commit id from the verified entries."""
        if cid not in self._paths:
            self._paths[cid] = MappingProxyType({p: oid for p, (mode, oid) in self.entries(cid).items()
                                                 if mode != '160000'})
        return self._paths[cid]

    def mode(self, cid, path):
        e = self.entries(cid).get(path)
        return None if e is None else e[0]

    def regular_blob_at(self, cid, path):
        """The blob ID at one exact regular-file path in the verified tree."""
        directory, _, basename = path.rpartition('/')
        tree = self.tree_id(cid, directory)
        if tree is None:
            return None
        return next((oid for mode, name, oid in self._tree(tree)
                     if mode in regular_modes and name == basename), None)

    def blob_id(self, cid, path):
        return self.paths(cid).get(path)

    def prefix_entries(self, cid, prefix, keep):
        """(key, entries) for the regular-file entries under `prefix` of the commit's tree that `keep(blob id)`
        selects: entries a tuple of (path, mode, blob id). `key` identifies the selected content (the verified tree
        id of the prefix), so that a caller can process each distinct subtree once. The listing of each subtree is
        built once per tree id from verified tree objects, holding only the selected entries; nothing else of the
        commit's tree is listed."""
        tid = self.tree_id(cid, prefix)
        if tid is None:
            return None, ()
        memo = self.__dict__.setdefault('_prefix_memo', {}).setdefault(id(keep), {})

        def walk(t, pre):
            if t in memo:
                return tuple((pre + q, m, o) for q, m, o in memo[t])
            got = []
            for mode, name, oid in self._tree(t):
                if mode == '040000':
                    got.extend((name + '/' + q, m, o) for q, m, o in walk(oid, ''))
                elif mode in regular_modes and keep(oid):
                    got.append((name, mode, oid))
            memo[t] = tuple(got)
            return tuple((pre + q, m, o) for q, m, o in memo[t])
        base = prefix.rstrip('/') + '/' if prefix else ''
        return tid, walk(tid, base)

    def read_blob_uncached(self, bid):
        """A verified blob read that is not kept in the reader's object cache (for a history walk that reads each
        distinct blob once)."""
        kind, data = self._batch(bid)
        self._objs.pop(bid, None)
        if kind != 'blob':
            raise Unresolvable('missing blob %s' % bid)
        return data

    def read_blob(self, bid):
        if bid not in self._blobs:
            kind, data = self._batch(bid)
            if kind != 'blob':
                raise Unresolvable('missing blob %s' % bid)
            self._blobs[bid] = data
        return self._blobs[bid]

    def read(self, cid, path):
        """The bytes of a regular-file entry, or None when the path is absent; any other entry refuses."""
        e = self.entries(cid).get(path)
        if e is None:
            return None
        if e[0] not in regular_modes:
            raise Unresolvable('%s is not a regular file at %s (mode %s)' % (path, cid[:12], e[0]))
        return self.read_blob(e[1])

    def is_ancestor(self, a, b):
        """Is `a` an ancestor of (or equal to) `b`, from parsed parents only. A parent the walk needs and the store
        lacks is an unresolvable object."""
        if not isinstance(a, str) or not _full.match(a):
            return False
        todo, seen = [b], set()
        while todo:
            c = todo.pop()
            if c == a:
                return True
            if c in seen:
                continue
            seen.add(c)
            todo.extend(self.parents(c))
        return False

    def diff_u0(self, a, b, path):
        r = self._git('diff', '-U0', '--no-renames', '--no-color', '--diff-algorithm=myers', a, b, '--', path)
        return r.stdout.decode('utf-8', 'replace')


class Overlay:
    """In-memory commits on top of a base reader; nothing reaches the repository. A file value is the bytes of a
    regular file, ('exec', bytes) for an executable regular file (mode 100755), or a tuple ('symlink', target) or
    ('submodule', commit id) for a non-regular entry."""

    def __init__(self, base=None):
        self.base = base
        self.mem = {}
        self._paths = {}
        self._entries = {}

    def add_commit(self, files, parents, subject='in-memory'):
        """files: {path: bytes}; returns a synthetic 40-hex id."""
        h = hashlib.sha1()
        h.update(subject.encode())
        for p in parents:
            h.update(p.encode())
        for path in sorted(files):
            h.update(path.encode() + b'\x00' + _value_id(files[path]).encode())
        cid = h.hexdigest()
        self.mem[cid] = {'files': dict(files), 'parents': list(parents), 'subject': subject}
        return cid

    def committer_time(self, cid):
        """An in-memory commit's committer time (seconds since the epoch) when a control set one in its record, else
        None; a base commit's from the base reader."""
        if cid in self.mem:
            return self.mem[cid].get('time')
        return self.base.committer_time(cid) if self.base is not None else None

    def derive(self, base_commit, changes, parents=None, subject='in-memory'):
        """A commit equal to base_commit's tree with changes {path: bytes or None}."""
        cid_files = _LazyTree(self, base_commit)
        for p, v in changes.items():
            cid_files.changes[p] = v
        h = hashlib.sha1()
        h.update(subject.encode())
        h.update(base_commit.encode())
        for p in sorted(changes):
            h.update(p.encode() + b'\x00' + (_value_id(changes[p]).encode() if changes[p] is not None else b'-'))
        for p in (parents if parents is not None else [base_commit]):
            h.update(p.encode())
        cid = h.hexdigest()
        self.mem[cid] = {'files': cid_files, 'parents': list(parents if parents is not None else [base_commit]),
                         'subject': subject}
        return cid

    def resolve(self, rev):
        full_id(rev)
        if rev in self.mem:
            return rev
        if self.base is None:
            raise Unresolvable('cannot resolve %r' % rev)
        return self.base.resolve(rev)

    def parents(self, cid):
        if cid in self.mem:
            return list(self.mem[cid]['parents'])
        if self.base is None:
            raise Unresolvable('not a commit: %s' % cid)
        return self.base.parents(cid)

    def subject(self, cid):
        if cid in self.mem:
            return self.mem[cid]['subject']
        return self.base.subject(cid)

    def tree_id(self, cid, prefix=''):
        if cid in self.mem:
            f = self.mem[cid]['files']
            if isinstance(f, _LazyTree) and prefix and not any(p.startswith(prefix.rstrip('/') + '/')
                                                              for p in f.changes):
                return self.tree_id(f.base_commit, prefix)
            ps = sorted((p, _value_id(d)) for p, d in self._files(cid).items() if p.startswith(prefix))
            return hashlib.sha1(repr(ps).encode()).hexdigest()
        return self.base.tree_id(cid, prefix)

    def _files(self, cid):
        f = self.mem[cid]['files']
        if isinstance(f, _LazyTree):
            return f.materialize()
        return f

    def entries(self, cid):
        """{path: (mode, id)} of every entry, symlinks and submodules included."""
        if cid in self.mem:
            if cid not in self._entries:
                f = self.mem[cid]['files']
                self._entries[cid] = MappingProxyType(dict(f.entries()) if isinstance(f, _LazyTree) else
                                                      {p: _entry_of(d) for p, d in f.items()})
            return self._entries[cid]
        return self.base.entries(cid)

    def paths(self, cid):
        """A read-only view, built once per in-memory commit id (base commits: the base reader's own view)."""
        if cid in self.mem:
            if cid not in self._paths:
                self._paths[cid] = MappingProxyType({p: oid for p, (mode, oid) in self.entries(cid).items()
                                                     if mode != '160000'})
            return self._paths[cid]
        return self.base.paths(cid)

    def mode(self, cid, path):
        e = self.entries(cid).get(path)
        return None if e is None else e[0]

    def regular_blob_at(self, cid, path):
        entry = self.entries(cid).get(path)
        return entry[1] if entry is not None and entry[0] in regular_modes else None

    def blob_id(self, cid, path):
        return self.paths(cid).get(path)

    def prefix_entries(self, cid, prefix, keep):
        """As GitRepo.prefix_entries, for an in-memory commit (its key is the selected entries themselves)."""
        if cid not in self.mem:
            if self.base is None:
                raise Unresolvable('not a commit: %s' % cid)
            return self.base.prefix_entries(cid, prefix, keep)
        got = tuple(sorted((p, m, o) for p, (m, o) in self.entries(cid).items()
                           if p.startswith(prefix) and m in regular_modes and keep(o)))
        return ('mem', got), got

    def read_blob_uncached(self, bid):
        return self.read_blob(bid)

    def read(self, cid, path):
        if cid in self.mem:
            f = self.mem[cid]['files']
            v = f.get(path)
            if isinstance(v, tuple) and v[0] == 'exec':
                return v[1]
            if isinstance(v, tuple):
                raise Unresolvable('%s is not a regular file at %s' % (path, cid[:12]))
            return v
        return self.base.read(cid, path)

    def read_blob(self, bid):
        for c in self.mem.values():
            f = c['files']
            if isinstance(f, _LazyTree):
                d = f.find_blob(bid)
                if d is not None:
                    return d
                continue
            for d in f.values():
                d = d[1] if isinstance(d, tuple) and d[0] == 'exec' else d
                if isinstance(d, bytes) and blob_id_of(d) == bid:
                    return d
        if self.base is None:
            raise Unresolvable('missing blob %s' % bid)
        return self.base.read_blob(bid)

    def diff_u0(self, a, b, path):
        if a in self.mem or b in self.mem or self.base is None:
            return None
        return self.base.diff_u0(a, b, path)

    def is_ancestor(self, a, b):
        if not isinstance(a, str) or not _full.match(a):
            return False
        todo, seen = [b], set()
        while todo:
            c = todo.pop()
            if c == a:
                return True
            if c in seen:
                continue
            seen.add(c)
            if c in self.mem:
                todo.extend(self.mem[c]['parents'])
            elif a in self.mem:
                continue  # a commit of the base store has no in-memory ancestor
            elif self.base is not None and self.base.is_ancestor(a, c):
                return True
        return False


def _value_id(v):
    return '%s:%s' % _entry_of(v)


def _entry_of(v):
    """(mode, id) of an in-memory file value."""
    if isinstance(v, tuple):
        if v[0] == 'submodule':
            return '160000', v[1]
        if v[0] == 'exec':
            return '100755', blob_id_of(v[1])
        return '120000', blob_id_of(v[1].encode() if isinstance(v[1], str) else v[1])
    return '100644', blob_id_of(v)


class _LazyTree:
    """A tree equal to a base commit's tree plus a few changed paths."""

    def __init__(self, repo, base_commit):
        self.repo = repo
        self.base_commit = base_commit
        self.changes = {}

    def __setitem__(self, k, v):
        self.changes[k] = v

    def pop(self, k, d=None):
        self.changes[k] = None
        return d

    def get(self, path):
        if path in self.changes:
            return self.changes[path]
        if self.repo.mode(self.base_commit, path) not in (None,) + regular_modes:
            return ('symlink', b'')
        return self.repo.read(self.base_commit, path)

    def entries(self):
        if getattr(self, '_entries', None) is not None:
            return self._entries
        out = dict(self.repo.entries(self.base_commit))
        for p, v in self.changes.items():
            if v is None:
                out.pop(p, None)
            else:
                out[p] = _entry_of(v)
        self._entries = out
        return out

    def paths(self):
        return {p: oid for p, (mode, oid) in self.entries().items() if mode != '160000'}

    def find_blob(self, bid):
        for v in self.changes.values():
            v = v[1] if isinstance(v, tuple) and v[0] == 'exec' else v
            if isinstance(v, bytes) and blob_id_of(v) == bid:
                return v
        return None

    def materialize(self):
        return {p: self.get(p) for p in self.paths()}


def first_parent_chain(repo, a, b):
    """Commits on b's first-parent chain strictly after a, oldest first; None if a is not on it."""
    out = []
    c = b
    seen = 0
    while c != a:
        out.append(c)
        ps = repo.parents(c)
        if not ps:
            return None
        c = ps[0]
        seen += 1
        if seen > 100000:
            return None
    out.reverse()
    return out


def on_first_parent_chain(repo, a, b, limit=200000):
    c = b
    n = 0
    while True:
        if c == a:
            return True
        ps = repo.parents(c)
        if not ps:
            return False
        c = ps[0]
        n += 1
        if n > limit:
            return False
