"""Read-only object access: the git object store, or in-memory commits layered over it."""
import hashlib
import subprocess


class Unresolvable(Exception):
    pass


def blob_id_of(data):
    return hashlib.sha1(b'blob %d\x00' % len(data) + data).hexdigest()


class GitRepo:
    """Reads commits, trees and blobs through `git cat-file --batch`; never writes."""

    def __init__(self, path):
        self.path = path
        self._proc = None
        self._trees = {}
        self._commits = {}
        self._blobs = {}
        r = subprocess.run(['git', '-C', path, 'rev-parse', '--git-dir'], capture_output=True, text=True)
        if r.returncode:
            raise Unresolvable('not a git repository: %s' % path)

    def _git(self, *args):
        r = subprocess.run(['git', '-C', self.path] + list(args), capture_output=True)
        return r

    def _batch(self, spec):
        if self._proc is None:
            self._proc = subprocess.Popen(['git', '-C', self.path, 'cat-file', '--batch'], stdin=-1,
                                          stdout=-1)
        self._proc.stdin.write(spec.encode() + b'\n')
        self._proc.stdin.flush()
        head = self._proc.stdout.readline().decode().split()
        if len(head) < 3 or head[1] == 'missing':
            return None, None
        size = int(head[2])
        data = self._proc.stdout.read(size)
        self._proc.stdout.read(1)
        return head[1], data

    def resolve(self, rev):
        if rev in self._commits:
            return rev
        r = self._git('rev-parse', '--verify', '--quiet', rev + '^{commit}')
        if r.returncode:
            raise Unresolvable('cannot resolve %r to a commit' % rev)
        return r.stdout.decode().strip()

    def _commit(self, cid):
        if cid not in self._commits:
            kind, data = self._batch(cid)
            if kind != 'commit':
                raise Unresolvable('not a commit: %s' % cid)
            text = data.decode('utf-8', 'replace')
            head, _, msg = text.partition('\n\n')
            parents, tree = [], None
            for line in head.split('\n'):
                if line.startswith('tree '):
                    tree = line[5:]
                elif line.startswith('parent '):
                    parents.append(line[7:])
            self._commits[cid] = {'tree': tree, 'parents': parents, 'subject': msg.split('\n', 1)[0]}
        return self._commits[cid]

    def parents(self, cid):
        return list(self._commit(cid)['parents'])

    def subject(self, cid):
        return self._commit(cid)['subject']

    def tree_id(self, cid, prefix=''):
        if not prefix:
            return self._commit(cid)['tree']
        r = self._git('rev-parse', '--verify', '--quiet', '%s:%s' % (cid, prefix.rstrip('/')))
        return r.stdout.decode().strip() if r.returncode == 0 else None

    def paths(self, cid):
        if cid not in self._trees:
            r = self._git('ls-tree', '-r', '-z', '--full-tree', cid)
            if r.returncode:
                raise Unresolvable('cannot list %s' % cid)
            out = {}
            for rec in r.stdout.split(b'\x00'):
                if not rec:
                    continue
                meta, _, path = rec.partition(b'\t')
                parts = meta.split()
                if parts[1] != b'blob':
                    continue
                out[path.decode('utf-8')] = parts[2].decode()
            self._trees[cid] = out
        return self._trees[cid]

    def blob_id(self, cid, path):
        return self.paths(cid).get(path)

    def read_blob(self, bid):
        if bid not in self._blobs:
            kind, data = self._batch(bid)
            if kind != 'blob':
                raise Unresolvable('missing blob %s' % bid)
            self._blobs[bid] = data
        return self._blobs[bid]

    def read(self, cid, path):
        bid = self.blob_id(cid, path)
        return None if bid is None else self.read_blob(bid)

    def is_ancestor(self, a, b):
        r = self._git('merge-base', '--is-ancestor', a, b)
        return r.returncode == 0

    def diff_u0(self, a, b, path):
        r = self._git('diff', '-U0', '--no-renames', '--no-color', '--diff-algorithm=myers', a, b, '--', path)
        return r.stdout.decode('utf-8', 'replace')


class Overlay:
    """In-memory commits on top of a base reader; nothing reaches the repository."""

    def __init__(self, base=None):
        self.base = base
        self.mem = {}

    def add_commit(self, files, parents, subject='in-memory'):
        """files: {path: bytes}; returns a synthetic 40-hex id."""
        h = hashlib.sha1()
        h.update(subject.encode())
        for p in parents:
            h.update(p.encode())
        for path in sorted(files):
            h.update(path.encode() + b'\x00' + blob_id_of(files[path]).encode())
        cid = h.hexdigest()
        self.mem[cid] = {'files': dict(files), 'parents': list(parents), 'subject': subject}
        return cid

    def derive(self, base_commit, changes, parents=None, subject='in-memory'):
        """A commit equal to base_commit's tree with changes {path: bytes or None}."""
        cid_files = _LazyTree(self, base_commit)
        for p, v in changes.items():
            cid_files.changes[p] = v
        h = hashlib.sha1()
        h.update(subject.encode())
        h.update(base_commit.encode())
        for p in sorted(changes):
            h.update(p.encode() + b'\x00' + (blob_id_of(changes[p]).encode() if changes[p] is not None else b'-'))
        for p in (parents if parents is not None else [base_commit]):
            h.update(p.encode())
        cid = h.hexdigest()
        self.mem[cid] = {'files': cid_files, 'parents': list(parents if parents is not None else [base_commit]),
                         'subject': subject}
        return cid

    def resolve(self, rev):
        if rev in self.mem:
            return rev
        if self.base is None:
            raise Unresolvable('cannot resolve %r' % rev)
        return self.base.resolve(rev)

    def parents(self, cid):
        if cid in self.mem:
            return list(self.mem[cid]['parents'])
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
            ps = sorted((p, blob_id_of(d)) for p, d in self._files(cid).items() if p.startswith(prefix))
            return hashlib.sha1(repr(ps).encode()).hexdigest()
        return self.base.tree_id(cid, prefix)

    def _files(self, cid):
        f = self.mem[cid]['files']
        if isinstance(f, _LazyTree):
            return f.materialize()
        return f

    def paths(self, cid):
        if cid in self.mem:
            f = self.mem[cid]['files']
            if isinstance(f, _LazyTree):
                return f.paths()
            return {p: blob_id_of(d) for p, d in f.items()}
        return self.base.paths(cid)

    def blob_id(self, cid, path):
        return self.paths(cid).get(path)

    def read(self, cid, path):
        if cid in self.mem:
            f = self.mem[cid]['files']
            if isinstance(f, _LazyTree):
                return f.get(path)
            return f.get(path)
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
                if blob_id_of(d) == bid:
                    return d
        if self.base is None:
            raise Unresolvable('missing blob %s' % bid)
        return self.base.read_blob(bid)

    def diff_u0(self, a, b, path):
        if a in self.mem or b in self.mem or self.base is None:
            return None
        return self.base.diff_u0(a, b, path)

    def is_ancestor(self, a, b):
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
            elif self.base is not None and hasattr(self.base, 'is_ancestor'):
                if self.base.is_ancestor(a, c):
                    return True
        return False


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
        return self.repo.read(self.base_commit, path)

    def paths(self):
        if getattr(self, '_paths', None) is not None:
            return self._paths
        out = dict(self.repo.paths(self.base_commit))
        for p, v in self.changes.items():
            if v is None:
                out.pop(p, None)
            else:
                out[p] = blob_id_of(v)
        self._paths = out
        return out

    def find_blob(self, bid):
        for v in self.changes.values():
            if v is not None and blob_id_of(v) == bid:
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
