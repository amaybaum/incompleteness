"""Small helpers over `git cat-file --batch` for the off-main preservation prototype."""
import subprocess


class Store:
    def __init__(self, gitdir):
        self.gitdir = gitdir
        self._p = subprocess.Popen(["git", "--git-dir", gitdir, "cat-file", "--batch"],
                                   stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        self._c = subprocess.Popen(["git", "--git-dir", gitdir, "cat-file", "--batch-check"],
                                   stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    def check(self, oid):
        """(type, size) or None."""
        self._c.stdin.write((oid + "\n").encode()); self._c.stdin.flush()
        line = self._c.stdout.readline().decode().split()
        if len(line) == 3 and line[1] != "missing":
            return line[1], int(line[2])
        return None

    def read(self, oid):
        """(type, content bytes) or None."""
        self._p.stdin.write((oid + "\n").encode()); self._p.stdin.flush()
        head = self._p.stdout.readline().decode().split()
        if len(head) != 3 or head[1] == "missing":
            return None
        n = int(head[2]); data = self._p.stdout.read(n); self._p.stdout.read(1)
        return head[1], data

    def git(self, *args, check=True):
        r = subprocess.run(["git", "--git-dir", self.gitdir, *args], capture_output=True)
        if check and r.returncode:
            raise RuntimeError(f"git {' '.join(args)}: {r.stderr.decode()}")
        return r.stdout.decode()


def parse_tree(data):
    """Entries (mode, name, oid) of a raw tree object."""
    out, i = [], 0
    while i < len(data):
        sp = data.index(b" ", i); nul = data.index(b"\0", sp)
        mode = data[i:sp].decode(); name = data[sp + 1:nul].decode("utf-8", "surrogateescape")
        oid = data[nul + 1:nul + 21].hex(); out.append((mode, name, oid)); i = nul + 21
    return out


def parse_commit(data):
    """(tree, [parents], headers dict of first values, message)."""
    text = data.decode("utf-8", "surrogateescape")
    head, _, msg = text.partition("\n\n")
    tree, parents, hdr = None, [], {}
    for line in head.split("\n"):
        if line.startswith(" "):
            continue
        k, _, v = line.partition(" ")
        if k == "tree": tree = v
        elif k == "parent": parents.append(v)
        hdr.setdefault(k, v)
    return tree, parents, hdr, msg
