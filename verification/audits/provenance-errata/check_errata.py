"""Check the provenance errata of this directory against the repository and the objects retained beside it.

Each entry of errata.json records a frozen line citing a CI run's head by an id that names no object, the run's real
head, what the line asserts and what was checked. CODES below names every check by its sub-code:
  E0  well-formed ids;
  E1  the citing record: its blob at HEAD, the receipt's pin, the line verbatim with its sha256, the run and the cited
      id on it;
  E2  the cited id: 7 to 40 hex digits, names no object, is not the real head or a prefix of it, and shares at least
      its first 7 hex digits with the real head;
  E3  the real head's tree, parent and content checks, read from the git objects stored in objects/ (and, for a commit
      on main, from the repository), so a clone of main checks them without the real heads; where the real heads are
      also in the repository, each check is repeated through git commands and the two routes must agree, as must the
      stored objects and the repository's;
  E4  the entry ids against the ids this checker pins, the README table parsed row by row against errata.json, the
      entry count, the vocabularies and the status rule, and the outcome records;
  E5  the object store: each file hashes to its name, the manifest lists exactly the files, and every stored object is
      read by some content check.
The job conclusions, job heads and served-log facts are host records read through the API; they are recorded with
their provenance and cannot be re-derived from the tree.

Verdicts: HOLDS (exit 0) when nothing fails and nothing is unchecked; UNCHECKED (exit 2) when nothing fails but an
object a check needs is neither stored nor on main; FAILS (exit 1) otherwise. --require-objects makes a missing
object a failure.

Usage: python3 -I check_errata.py [--require-objects] [--self-test]"""
import ast, copy, hashlib, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = subprocess.run(['git', '-C', HERE, 'rev-parse', '--show-toplevel'], capture_output=True, text=True,
                      check=True).stdout.strip()
HEX40 = re.compile(r'^[0-9a-f]{40}$')
HEX64 = re.compile(r'^[0-9a-f]{64}$')
RUN_TOKEN = r'(?<![0-9A-Za-z.])%s(?![0-9A-Za-z]|\.[0-9])'
HEX_TOKEN = r'(?<![0-9A-Za-z])%s(?![0-9A-Za-z])'
CITED = re.compile(r'^[0-9a-f]{7,40}$')
TREE_MODE = '40000'
VERDICTS = ('confirmed', 'not confirmed')
EXPLANATIONS = ('confirmed', 'incomplete', 'not confirmed')
# status = RULE[(verdict, explanation)]: an unconfirmed verdict does not hold; a confirmed one holds when its account
# is confirmed and partly holds otherwise.
RULE = {(v, x): ('does not hold' if v == 'not confirmed' else 'holds' if x == 'confirmed' else 'partly holds')
        for v in VERDICTS for x in EXPLANATIONS}
# The entry set is pinned here as well as in errata.json and the README, so a consistent edit of the data alone cannot
# remove an entry: adding or retiring one changes this line too.
ENTRY_IDS = ('PE-1', 'PE-2', 'PE-3', 'PE-4', 'PE-5')
README_HEADER = ['id', 'location', 'run, attempt', 'cited id', 'real head', 'shared digits', 'verdict', 'explanation',
                 'status']

CODES = {
    'E0a': 'an id field is not a full 40-hex id',
    'E1a': "the citing file's blob at HEAD is not the recorded citing blob",
    'E1b': "the receipt does not pin the citing blob (a control-plane pin, or the record directory at the receipt commit)",
    'E1c': 'the cited line is not the recorded verbatim assertion',
    'E1d': 'the cited line does not name the run id and the cited id',
    'E1e': "the recorded sha256 is not the verbatim assertion's",
    'E2a': 'the cited id names an object in this repository',
    'E2b': 'the cited id is the real head or a prefix of it',
    'E2c': 'the cited id shares fewer than 7 leading hex digits with the real head',
    'E2d': 'the cited id is not 7 to 40 lowercase hex digits',
    'E2e': 'the recorded shared-digit count is not the computed one',
    'E3a': "the real head's tree is not the recorded tree",
    'E3b': "the real head's parents are not the recorded parent",
    'E3c': 'the entry has no content checks',
    'E3d': 'count_lines_matching does not hold',
    'E3e': 'line_contains does not hold',
    'E3f': 'consecutive_lines does not hold',
    'E3g': 'diff_paths does not hold',
    'E3h': 'diff_adds_line does not hold',
    'E3i': 'diff_removes_line does not hold',
    'E3j': 'diff_line_counts does not hold',
    'E3k': 'tree_equals_cited does not hold',
    'E3l': 'blob_at does not hold',
    'E3m': 'blobs_equal_at does not hold',
    'E3n': "frozen_edit: the base with the recorded edits applied is not the real head's blob",
    'E3o': 'a content check of unknown kind',
    'E3p': 'frozen_edit: the recorded edits are not the frozen source, or a base or source blob is not the recorded one',
    'E3t': 'an object E3 reads is malformed, or is not of the type its use requires',
    'E3u': 'an object a check needs is neither stored nor on main (unchecked; a failure with --require-objects)',
    'E3x': 'the git route disagrees with the stored-object route, or a stored object differs from the repository',
    'E4a': 'the errata ids and the README rows are not in bijection',
    'E4b': 'the entry count or the README row count is not expected_count, or expected_count is not the pinned count',
    'E4c': 'a README cell differs from errata.json',
    'E4d': 'a verdict outside its vocabulary',
    'E4e': 'an explanation outside its vocabulary',
    'E4f': 'a status other than the one the rule derives',
    'E4g': "the stated status rule is not the checker's",
    'E4h': 'the outcome lists no jobs',
    'E4i': 'the outcome does not record that every job ran on the real head',
    'E4j': 'a log fact carries no served digest or no facts',
    'E4k': "the outcome's run record names another run, head or attempt",
    'E4l': 'the errata ids are not the ids this checker pins, in order',
    'E5a': 'a stored object does not hash to its name, or is malformed',
    'E5b': 'the object manifest and the objects directory differ',
    'E5c': 'a stored object no content check reads',
    'E5d': "a stored object's recorded type or size is not its own",
}


class Missing(Exception):
    pass


class Corrupt(Exception):
    pass


def run_git(*a, inp=None):
    return subprocess.run(['git', '-C', ROOT, *a], input=inp, capture_output=True)


def git(*a):
    p = run_git(*a)
    if p.returncode:
        raise RuntimeError('git %s: %s' % (' '.join(a), p.stderr.decode('utf-8', 'replace').strip()))
    return p.stdout


class Batch:
    """One git cat-file --batch process and one --batch-check process for the whole run."""

    def __init__(self):
        self.procs = {}

    def query(self, spec, check=False):
        """(oid, type, body) for a revision expression; (None, 'missing' or 'ambiguous', None) when it names none."""
        mode = '--batch-check' if check else '--batch'
        p = self.procs.get(mode)
        if p is None:
            p = self.procs[mode] = subprocess.Popen(['git', '-C', ROOT, 'cat-file', mode], stdin=subprocess.PIPE,
                                                    stdout=subprocess.PIPE)
        p.stdin.write(spec.encode('utf-8') + b'\n')
        p.stdin.flush()
        parts = p.stdout.readline().decode('utf-8', 'replace').rstrip('\n').split(' ')
        if parts[-1] in ('missing', 'ambiguous'):
            return None, parts[-1], None
        oid, typ, size = parts[-3:]
        body = None
        if not check:
            body = p.stdout.read(int(size))
            p.stdout.read(1)
        return oid, typ, body

    def oid(self, spec):
        return self.query(spec, True)[0]

    def body(self, spec):
        return self.query(spec)[2]


BATCH = Batch()
ANCESTOR = {}


def names_object(token):
    """True when the token names an object here: git cat-file --batch-check finds it or calls it ambiguous."""
    return BATCH.query(token, True)[1] != 'missing'


def is_ancestor_of_head(oid):
    if oid not in ANCESTOR:
        ANCESTOR[oid] = run_git('merge-base', '--is-ancestor', oid, 'HEAD').returncode == 0
    return ANCESTOR[oid]


def parse_raw(oid, raw):
    nul = raw.find(b'\0')
    if nul < 0:
        raise Corrupt('%s has no header' % oid)
    parts = raw[:nul].split(b' ')
    if len(parts) != 2 or parts[0] not in (b'commit', b'tree', b'blob') or not parts[1].isdigit():
        raise Corrupt('%s has a malformed header' % oid)
    body = raw[nul + 1:]
    if int(parts[1]) != len(body):
        raise Corrupt('%s: header size %s, body %d bytes' % (oid, parts[1].decode(), len(body)))
    if hashlib.sha1(raw).hexdigest() != oid:
        raise Corrupt('%s hashes to %s' % (oid, hashlib.sha1(raw).hexdigest()))
    return parts[0].decode(), body


def parse_tree(body):
    out, i = {}, 0
    while i < len(body):
        sp = body.index(b' ', i)
        nul = body.index(b'\0', sp)
        out[body[sp + 1:nul].decode('utf-8', 'surrogateescape')] = (body[i:sp].decode(), body[nul + 1:nul + 21].hex())
        i = nul + 21
    return out


def parse_commit(body):
    tree, parents = None, []
    for line in body.split(b'\n\n', 1)[0].decode('utf-8', 'replace').split('\n'):
        if line.startswith('tree '):
            tree = line[5:]
        elif line.startswith('parent '):
            parents.append(line[7:])
    return tree, parents


def lines_keepends(b):
    parts = b.split(b'\n')
    return [p + b'\n' for p in parts[:-1]] + ([parts[-1]] if parts[-1] else [])


def line_counts(a, b):
    """(added, removed) of a minimal line diff from a to b (Myers), lines kept with their terminators as git does."""
    i = 0
    while i < len(a) and i < len(b) and a[i] == b[i]:
        i += 1
    j = 0
    while j < len(a) - i and j < len(b) - i and a[len(a) - 1 - j] == b[len(b) - 1 - j]:
        j += 1
    a, b = a[i:len(a) - j], b[i:len(b) - j]
    n, m = len(a), len(b)
    d = n + m
    if n and m:
        v = {1: 0}
        for d in range(n + m + 1):
            done = False
            for k in range(-d, d + 1, 2):
                x = v[k + 1] if (k == -d or (k != d and v[k - 1] < v[k + 1])) else v[k - 1] + 1
                y = x - k
                while x < n and y < m and a[x] == b[y]:
                    x, y = x + 1, y + 1
                v[k] = x
                if x >= n and y >= m:
                    done = True
                    break
            if done:
                break
    lcs = (n + m - d) // 2
    return m - lcs, n - lcs


class Objects:
    """Objects by source. A commit stored in objects/ is read, with every tree and blob reached from it, from the store
    alone; a commit not stored but on main (an ancestor of HEAD) is read from the repository."""

    def __init__(self, store_dir, overlay=None):
        self.dir, self.overlay, self.read = store_dir, overlay or {}, set()

    def ids(self):
        names = set(os.listdir(self.dir)) if os.path.isdir(self.dir) else set()
        return (names | {k for k, v in self.overlay.items() if v is not None}) - {k for k, v in self.overlay.items() if v is None}

    def raw(self, oid):
        if oid in self.overlay:
            return self.overlay[oid]
        p = os.path.join(self.dir, oid)
        return open(p, 'rb').read() if os.path.isfile(p) else None

    def commit_source(self, oid):
        if self.raw(oid) is not None:
            return 'store'
        if is_ancestor_of_head(oid):
            return 'main'
        raise Missing('commit %s is neither stored nor on main' % oid)

    def get(self, src, oid, want):
        if src == 'store':
            raw = self.raw(oid)
            if raw is None:
                raise Missing('%s %s is not stored' % (want, oid))
            typ, body = parse_raw(oid, raw)
            self.read.add(oid)
        else:
            got, typ, body = BATCH.query(oid)
            if got != oid:
                raise Missing('%s %s of a commit on main is not in the repository' % (want, oid))
        if typ != want:
            raise Corrupt('%s is a %s, not a %s' % (oid, typ, want))
        return body

    def commit(self, oid):
        src = self.commit_source(oid)
        tree, parents = parse_commit(self.get(src, oid, 'commit'))
        return src, tree, parents

    def entry(self, src, tree, path):
        parts = path.split('/')
        for k, name in enumerate(parts):
            ents = parse_tree(self.get(src, tree, 'tree'))
            if name not in ents:
                return None
            mode, oid = ents[name]
            if k == len(parts) - 1:
                return mode, oid
            if mode != TREE_MODE:
                return None
            tree = oid
        return None

    def blob(self, src, tree, path):
        e = self.entry(src, tree, path)
        if e is None or e[0] == TREE_MODE:
            return None
        return self.get(src, e[1], 'blob')

    def diff(self, sa, ta, sb, tb, prefix=''):
        """Paths whose entries differ between two trees (git diff --no-renames --name-only)."""
        if ta == tb:
            return []
        ea = parse_tree(self.get(sa, ta, 'tree')) if ta else {}
        eb = parse_tree(self.get(sb, tb, 'tree')) if tb else {}
        out = []
        for name in sorted(set(ea) | set(eb)):
            a, b = ea.get(name), eb.get(name)
            if a == b:
                continue
            at, bt = bool(a and a[0] == TREE_MODE), bool(b and b[0] == TREE_MODE)
            if at or bt:
                out += self.diff(sa, a[1] if at else None, sb, b[1] if bt else None, prefix + name + '/')
            if (a and not at) or (b and not bt):
                out.append(prefix + name)
        return sorted(set(out))


def frozen_edits(source_text, name):
    """The module-level list assigned to `name` in a Python source, read with ast.literal_eval (nothing is run)."""
    for node in ast.parse(source_text).body:
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == name for t in node.targets):
            return [list(p) for p in ast.literal_eval(node.value)]
    return None


def apply_edits(text, edits):
    for old, new in edits:
        if text.count(old) != 1:
            return None
        text = text.replace(old, new)
    return text


def store_route(c, obj, head_src, head_tree):
    """Each content check from the objects: (code, holds, message)."""
    k = c['kind']
    if k in ('count_lines_matching', 'line_contains', 'consecutive_lines'):
        b = obj.blob(head_src, head_tree, c['path'])
        lines = b.decode('utf-8').split('\n') if b is not None else []
        if k == 'count_lines_matching':
            n = sum(1 for l in lines if re.search(c['regex'], l))
            return 'E3d', n == c['expect'], '%s: %d lines match %r, expected %d' % (c['path'], n, c['regex'], c['expect'])
        if k == 'line_contains':
            got = lines[c['line'] - 1] if 0 < c['line'] <= len(lines) else ''
            return 'E3e', c['text'] in got, '%s:%d does not contain %r' % (c['path'], c['line'], c['text'])
        want = c['lines']
        s = [l.strip() for l in lines]
        return 'E3f', any(s[i:i + len(want)] == want for i in range(len(s))), '%s: lines %r are not consecutive' % (c['path'], want)
    if k in ('diff_paths', 'diff_adds_line', 'diff_removes_line', 'diff_line_counts'):
        bsrc, btree, _ = obj.commit(c['against'])
        if k == 'diff_paths':
            got = obj.diff(bsrc, btree, head_src, head_tree)
            return 'E3g', got == sorted(c['expect']), 'diff from %s touches %r, expected %r' % (c['against'][:8], got, sorted(c['expect']))
        old = obj.blob(bsrc, btree, c['path']) or b''
        new = obj.blob(head_src, head_tree, c['path']) or b''
        if k == 'diff_line_counts':
            got = line_counts(lines_keepends(old), lines_keepends(new))
            return 'E3j', got == (c['added'], c['removed']), 'diff from %s: %r lines added/removed, expected %r' % (
                c['against'][:8], got, (c['added'], c['removed']))
        no = old.decode('utf-8').split('\n').count(c['text'])
        nn = new.decode('utf-8').split('\n').count(c['text'])
        if k == 'diff_adds_line':
            return 'E3h', nn > no, 'diff from %s does not add %r' % (c['against'][:8], c['text'])
        return 'E3i', no > nn, 'diff from %s does not remove %r' % (c['against'][:8], c['text'])
    if k == 'tree_equals_cited':
        return 'E3k', head_tree == c['cited_tree'], 'tree %s is not the cited tree %s' % (head_tree, c['cited_tree'])
    if k == 'blob_at':
        e = obj.entry(head_src, head_tree, c['path'])
        b = e[1] if e and e[0] != TREE_MODE else None
        return 'E3l', b == c['blob'], '%s is %s, expected %s' % (c['path'], b, c['blob'])
    if k == 'blobs_equal_at':
        osrc, otree, _ = obj.commit(c['other'])
        bad = []
        for p in c['paths']:
            x, y = obj.entry(head_src, head_tree, p), obj.entry(osrc, otree, p)
            if not x or x != y:
                bad.append(p)
        return 'E3m', not bad, '%r differ between the real head and %s' % (bad, c['other'][:8])
    if k == 'frozen_edit':
        def at(commit, path):
            s, t, _ = obj.commit(commit)
            return obj.entry(s, t, path), obj.blob(s, t, path)
        return frozen_edit_check(c, at, obj.blob(head_src, head_tree, c['path']))
    return 'E3o', False, 'unknown content check %r' % k


def frozen_edit_check(c, at, head_blob):
    """`at(commit, path)` gives ((mode, oid) or None, bytes or None). Two codes: E3p for the recorded inputs against
    their frozen sources, E3n for the result."""
    bad = []
    be, base = at(c['base']['commit'], c['path'])
    if not be or be[1] != c['base']['blob']:
        bad.append('the base %s:%s is %s, recorded %s' % (c['base']['commit'][:8], c['path'], be and be[1], c['base']['blob']))
    se, src = at(c['source']['commit'], c['source']['path'])
    if not se or se[1] != c['source']['blob']:
        bad.append('the source %s:%s is %s, recorded %s' % (c['source']['commit'][:8], c['source']['path'], se and se[1], c['source']['blob']))
    frozen = frozen_edits(src.decode('utf-8'), c['source']['name']) if src is not None else None
    if frozen != c['edits']:
        bad.append('the recorded edits are not %s in the source' % c['source']['name'])
    if len(c['edits']) != c['places']:
        bad.append('%d edits recorded, %d places stated' % (len(c['edits']), c['places']))
    out = apply_edits(base.decode('utf-8'), c['edits']) if base is not None else None
    good = out is not None and head_blob is not None and out.encode('utf-8') == head_blob
    res = [('E3n', good, "%s: the base with the %d recorded edits is not the real head's blob" % (c['path'], len(c['edits'])))]
    res.append(('E3p', not bad, '; '.join(bad)))
    return res


def git_route(c, head):
    """The same content checks through git commands, used where the real head is in the repository."""
    k = c['kind']
    show = lambda rev, p: BATCH.body('%s:%s' % (rev, p))
    rev = BATCH.oid
    if k in ('count_lines_matching', 'line_contains', 'consecutive_lines'):
        lines = show(head, c['path']).decode('utf-8').split('\n')
        if k == 'count_lines_matching':
            return sum(1 for l in lines if re.search(c['regex'], l)) == c['expect']
        if k == 'line_contains':
            return c['text'] in (lines[c['line'] - 1] if 0 < c['line'] <= len(lines) else '')
        s = [l.strip() for l in lines]
        return any(s[i:i + len(c['lines'])] == c['lines'] for i in range(len(s)))
    if k == 'diff_paths':
        return sorted(git('diff', '--no-renames', '--name-only', c['against'], head).decode().split()) == sorted(c['expect'])
    if k in ('diff_adds_line', 'diff_removes_line'):
        d = git('diff', '--no-renames', c['against'], head, '--', c['path']).decode('utf-8').split('\n')
        return ('+' if k == 'diff_adds_line' else '-') + c['text'] in d
    if k == 'diff_line_counts':
        d = git('diff', '--no-renames', '--numstat', c['against'], head, '--', c['path']).decode().split()
        return (int(d[0]), int(d[1])) == (c['added'], c['removed']) if len(d) >= 2 else False
    if k == 'tree_equals_cited':
        return rev(head + '^{tree}') == c['cited_tree']
    if k == 'blob_at':
        return rev('%s:%s' % (head, c['path'])) == c['blob']
    if k == 'blobs_equal_at':
        return all(rev('%s:%s' % (head, p)) and rev('%s:%s' % (head, p)) == rev('%s:%s' % (c['other'], p)) for p in c['paths'])
    if k == 'frozen_edit':
        def at(commit, path):
            b = rev('%s:%s' % (commit, path))
            return ('100644', b) if b else None, show(commit, path) if b else None
        return [good for _, good, _ in frozen_edit_check(c, at, show(head, c['path']))]
    return False


class Finding:
    def __init__(self, code, eid, msg):
        self.code, self.eid, self.msg = code, eid, msg

    def __str__(self):
        return '%s %s %s' % (self.code, self.eid, self.msg)


def parse_readme(readme):
    lines = readme.split('\n')
    hdr = '| ' + ' | '.join(README_HEADER) + ' |'
    if hdr not in lines:
        return None
    rows = []
    for l in lines[lines.index(hdr) + 2:]:
        if not l.startswith('|'):
            break
        rows.append([x.strip() for x in l.strip().strip('|').split('|')])
    return rows


def readme_cells(e):
    return [e['id'], e['location'], '%s, %s' % (e['run_id'], e['attempt']), '`%s`' % e['cited_head'],
            '`%s`' % e['real_head'], str(e['shared_digits']), e['verdict'], e['explanation'], e['status']]


def check(data, readme, require_objects=False, overlay=None, xflip=None):
    """Returns (fails, unchecked, info). `overlay` and `xflip` exist for the self-test: the first replaces or hides
    stored objects, the second inverts one check of the git route."""
    fails, unchecked = [], []
    info = {'e3_entries': 0, 'cross_checked': [], 'stored': 0, 'entries': len(data.get('entries', []))}

    def fail(code, eid, msg, missing=False):
        (unchecked if missing and not require_objects else fails).append(Finding(code, eid, msg))

    store = data.get('object_store', {})
    obj = Objects(os.path.join(HERE, store.get('directory', 'objects')), overlay)
    # E5: the store itself
    ids = obj.ids()
    info['stored'] = len(ids)
    parsed = {}
    for oid in sorted(ids):
        try:
            if not HEX40.match(oid):
                raise Corrupt('%s is not an object id' % oid)
            parsed[oid] = parse_raw(oid, obj.raw(oid))
        except Corrupt as x:
            fail('E5a', '-', str(x))
    manifest = {m['oid']: m for m in store.get('objects', [])}
    if len(manifest) != len(store.get('objects', [])) or set(manifest) != ids:
        fail('E5b', '-', 'manifest only %r, directory only %r' % (sorted(set(manifest) - ids), sorted(ids - set(manifest))))
    for oid, (typ, body) in parsed.items():
        m = manifest.get(oid)
        if m and (m.get('type') != typ or m.get('size') != len(body)):
            fail('E5d', '-', '%s is a %s of %d bytes, recorded %s of %s' % (oid, typ, len(body), m.get('type'), m.get('size')))
    entries = data.get('entries', [])
    # E4: entry set, count, rule
    rows = parse_readme(readme)
    rows = rows if rows is not None else []
    rids = [r[0] for r in rows]
    eids = [e.get('id') for e in entries]
    if sorted(rids) != sorted(set(rids)) or sorted(eids) != sorted(set(eids)) or set(rids) != set(eids):
        fail('E4a', '-', 'README rows %r, errata entries %r' % (rids, eids))
    if len(entries) != data.get('expected_count') or len(rows) != data.get('expected_count') or data.get('expected_count') != len(ENTRY_IDS):
        fail('E4b', '-', '%d entries and %d README rows, expected_count %r, %d pinned' % (
            len(entries), len(rows), data.get('expected_count'), len(ENTRY_IDS)))
    if tuple(eids) != ENTRY_IDS:
        fail('E4l', '-', 'errata ids %r, pinned %r' % (eids, list(ENTRY_IDS)))
    stated = {(r.get('verdict'), r.get('explanation')): r.get('status') for r in data.get('status_rule', {}).get('table', [])}
    if stated != RULE or len(data.get('status_rule', {}).get('table', [])) != len(RULE):
        fail('E4g', '-', 'the stated rule %r is not %r' % (sorted(stated.items()), sorted(RULE.items())))
    complete = True
    for e in entries:
        eid = e['id']
        for key in ('citing_blob', 'real_head', 'real_tree', 'real_parent'):
            if not HEX40.match(e.get(key, '')):
                fail('E0a', eid, '%s is not a full 40-hex id' % key)
        # E1: the citing record
        path, line = e['location'].rsplit(':', 1)
        line = int(line)
        blob = BATCH.oid('HEAD:' + path)
        if blob != e['citing_blob']:
            fail('E1a', eid, '%s has blob %s at HEAD, recorded %s' % (path, blob, e['citing_blob']))
        pin = e.get('pin', {})
        if pin.get('kind') == 'control_plane_blob':
            rb = BATCH.body('HEAD:' + pin.get('receipt', ''))
            pins = json.loads(rb).get('control_plane_blobs', []) if rb is not None else []
            if {'path': path, 'blob': e['citing_blob']} not in pins:
                fail('E1b', eid, '%s does not pin %s at %s' % (pin.get('receipt'), path, e['citing_blob']))
        elif pin.get('kind') == 'record_directory':
            last = run_git('log', '-1', '--format=%H', 'HEAD', '--', pin.get('receipt', '')).stdout.decode().strip()
            at_q = BATCH.oid('%s:%s' % (pin.get('receipt_commit', ''), path))
            if last != pin.get('receipt_commit') or at_q != e['citing_blob'] or not path.startswith(pin.get('record_directory') or '\0'):
                fail('E1b', eid, '%s at the receipt commit %s (last writer of %s: %s) is %s, recorded %s' % (
                    path, pin.get('receipt_commit'), pin.get('receipt'), last, at_q, e['citing_blob']))
        else:
            fail('E1b', eid, 'no receipt pin of a known kind')
        text = BATCH.body('HEAD:' + path).decode('utf-8').split('\n') if blob else []
        got = text[line - 1] if 0 < line <= len(text) else ''
        if got != e.get('assertion_verbatim'):
            fail('E1c', eid, '%s is not the recorded verbatim line' % e['location'])
        if hashlib.sha256(e.get('assertion_verbatim', '').encode('utf-8')).hexdigest() != e.get('assertion_sha256'):
            fail('E1e', eid, 'the recorded sha256 is not that of the verbatim line')
        if not re.search(RUN_TOKEN % re.escape(e['run_id']), got) or not re.search(HEX_TOKEN % re.escape(e['cited_head']), got):
            fail('E1d', eid, '%s does not name run %s and %s' % (e['location'], e['run_id'], e['cited_head']))
        # E2: the cited id
        c, h = e['cited_head'], e['real_head']
        if not CITED.match(c):
            fail('E2d', eid, 'the cited id %r is not 7 to 40 lowercase hex digits' % c)
        else:
            if names_object(c):
                fail('E2a', eid, 'the cited id %s names an object in this repository' % c)
            if h.startswith(c):
                fail('E2b', eid, 'the cited id %s is the real head or a prefix of it' % c)
            shared = len(os.path.commonprefix([c, h]))
            if shared < 7:
                fail('E2c', eid, 'the cited id %s shares %d leading hex digits with %s' % (c, shared, h))
            if e.get('shared_digits') != shared:
                fail('E2e', eid, 'shared_digits %r, computed %d' % (e.get('shared_digits'), shared))
        # E3: the real head's objects
        if not e.get('content_checks'):
            fail('E3c', eid, 'no content checks')
        results = []
        try:
            src, tree, parents = obj.commit(h)
            if src != 'store':
                raise Missing('the real head %s is not stored' % h)
            if tree != e['real_tree']:
                fail('E3a', eid, 'real head tree %s, recorded %s' % (tree, e['real_tree']))
            if parents != [e['real_parent']]:
                fail('E3b', eid, 'real head parents %r, recorded %s' % (parents, e['real_parent']))
            for c in e.get('content_checks', []):
                try:
                    res = store_route(c, obj, src, tree)
                    res = res if isinstance(res, list) else [res]
                    results.append([good for _, good, _ in res])
                    for code, good, msg in res:
                        if not good:
                            fail(code, eid, msg)
                except Missing as x:
                    complete = False
                    results.append(None)
                    fail('E3u', eid, str(x), missing=True)
            info['e3_entries'] += 1
        except Missing as x:
            complete = False
            results = None
            fail('E3u', eid, str(x), missing=True)
        except Corrupt as x:
            complete = False
            results = None
            fail('E3t', eid, str(x))
        # E3x: the git route, where the real head is in the repository
        if results is not None and BATCH.query(h, True)[1] == 'commit':
            disagree = []
            for j, c in enumerate(e.get('content_checks', [])):
                try:
                    g = git_route(c, h)
                except RuntimeError as x:
                    g = 'error: %s' % x
                g = g if isinstance(g, list) else [g]
                if xflip == (eid, j):
                    g = [not x for x in g]
                if results[j] is not None and g != results[j]:
                    disagree.append('%s check %d: git %r, objects %r' % (c['kind'], j, g, results[j]))
            for oid in sorted(obj.read & set(parsed)):
                typ, body = parsed[oid]
                got, gtyp, gbody = BATCH.query(oid)
                if got == oid and (gtyp, gbody) != (typ, body):
                    disagree.append('stored %s %s differs from the repository' % (typ, oid))
            if run_git('log', '-1', '--format=%T %P', h).stdout.decode().split() != [tree] + parents:
                disagree.append('git reads another tree or parent for %s than the stored commit' % h)
            if disagree:
                fail('E3x', eid, '; '.join(disagree))
            info['cross_checked'].append(eid)
        # E4: the README row, the vocabularies, the rule, the outcome
        row = next((r for r in rows if r and r[0] == eid), None)
        if row is not None:
            want = readme_cells(e)
            for col, (x, y) in enumerate(zip(row + [None] * (len(want) - len(row)), want)):
                if x != y:
                    fail('E4c', eid, 'README column %r is %r, errata.json gives %r' % (README_HEADER[col], x, y))
            if len(row) > len(want):
                fail('E4c', eid, 'README row has %d cells, expected %d' % (len(row), len(want)))
        if e.get('verdict') not in VERDICTS:
            fail('E4d', eid, 'verdict %r is not one of %r' % (e.get('verdict'), VERDICTS))
        if e.get('explanation') not in EXPLANATIONS:
            fail('E4e', eid, 'explanation %r is not one of %r' % (e.get('explanation'), EXPLANATIONS))
        if (e.get('verdict'), e.get('explanation')) in RULE and e.get('status') != RULE[(e['verdict'], e['explanation'])]:
            fail('E4f', eid, 'status %r, the rule gives %r' % (e.get('status'), RULE[(e['verdict'], e['explanation'])]))
        out = e.get('outcome', {})
        if not out.get('jobs'):
            fail('E4h', eid, 'the outcome lists no jobs')
        if out.get('every_job_head_is_the_real_head') is not True:
            fail('E4i', eid, 'the outcome does not record that every job ran on the real head')
        for lf in out.get('log_facts', []):
            if not HEX64.match(lf.get('served_sha256', '')) or not lf.get('facts'):
                fail('E4j', eid, 'log facts of job %s carry no served digest or no facts' % lf.get('job'))
        r = out.get('run', {})
        if (r.get('id'), r.get('head_sha'), r.get('attempt')) != (e['run_id'], h, e['attempt']):
            fail('E4k', eid, 'run record %r, entry run %s head %s attempt %s' % (r, e['run_id'], h, e['attempt']))
    # E5c: exactness, once every entry's content was read
    if complete:
        extra = sorted(set(parsed) - obj.read)
        if extra:
            fail('E5c', '-', 'stored but read by no check: %r' % extra)
    return fails, unchecked, info


def summary_line(fails, unchecked, info):
    n = info['entries']
    if not n:
        cross = 'none (no entries)'
    elif info['cross_checked']:
        cross = ', '.join(info['cross_checked'])
    else:
        cross = 'none (no real head in this repository)'
    return ('ERRATA  %s (%d entr%s; E3 from %d stored objects on %d entr%s; git cross-check on %s; %d failure(s), %d unchecked)'
            % (verdict(fails, unchecked), n, 'y' if n == 1 else 'ies', info['stored'], info['e3_entries'],
               'y' if info['e3_entries'] == 1 else 'ies', cross, len(fails), len(unchecked)))


def verdict(fails, unchecked):
    return 'FAILS' if fails else 'UNCHECKED' if unchecked else 'HOLDS'


EXIT = {'HOLDS': 0, 'FAILS': 1, 'UNCHECKED': 2}


def self_test(data, readme):
    """Each mutation must be caught by the sub-code it targets; the unmutated errata must hold."""
    base_f, base_u, info = check(data, readme)
    assert not base_f and not base_u, [str(x) for x in base_f + base_u]
    ix = {e['id']: i for i, e in enumerate(data['entries'])}
    E = lambda d, eid: d['entries'][ix[eid]]
    def ck(eid, kind, n=0):
        js = [j for j, c in enumerate(data['entries'][ix[eid]]['content_checks']) if c['kind'] == kind]
        return js[n]
    def put(eid, key, val):
        def m(d, r):
            E(d, eid)[key] = val
            return d, r
        return m
    def put_check(eid, kind, key, val, n=0):
        def m(d, r):
            E(d, eid)['content_checks'][ck(eid, kind, n)][key] = val
            return d, r
        return m
    def edit(f):
        def m(d, r):
            f(d)
            return d, r
        return m
    store = Objects(os.path.join(HERE, data['object_store']['directory']))
    first_stored = sorted(store.ids())
    a_blob = next(m['oid'] for m in data['object_store']['objects'] if m['type'] == 'blob')
    head = git('rev-parse', 'HEAD').decode().strip()
    extra_raw = b'blob %d\0' % len(b'x\n') + b'x\n'
    extra_oid = hashlib.sha1(extra_raw).hexdigest()
    pe3_row = '| PE-3 |'
    h5 = data['entries'][ix['PE-5']]['real_head']
    pe1_line = next(l for l in readme.split('\n') if l.startswith('| PE-1 |'))
    no_rows = '\n'.join(l for l in readme.split('\n') if not l.startswith('| PE-'))
    no_pe5 = '\n'.join(l for l in readme.split('\n') if not l.startswith('| PE-5 |'))
    def drop(oids):
        def m(d, r):
            d['object_store']['objects'] = [x for x in d['object_store']['objects'] if x['oid'] not in oids]
            return d, r
        return m
    def emptied(d, r):
        d['entries'], d['expected_count'], d['object_store']['objects'] = [], 0, []
        return d, no_rows
    def without_pe5(d, r):
        d['entries'] = [e for e in d['entries'] if e['id'] != 'PE-5']
        d['expected_count'] = 4
        return d, no_pe5
    cases = [
        ('E0a', 'a truncated id', put('PE-4', 'real_tree', '12a695df'), {}),
        ('E1a', 'a changed citing blob', put('PE-1', 'citing_blob', '0' * 40), {}),
        ('E1b', 'a control-plane pin in another receipt', edit(lambda d: E(d, 'PE-1')['pin'].__setitem__('receipt', 'verification/receipts/A35.json')), {}),
        ('E1b', 'a record-directory pin at another commit', edit(lambda d: E(d, 'PE-3')['pin'].__setitem__('receipt_commit', head)), {}),
        ('E1b', 'a pin of no known kind', put('PE-2', 'pin', {}), {}),
        ('E1c', 'a cited line that is not the recorded one', edit(lambda d: E(d, 'PE-2').__setitem__('location', E(d, 'PE-2')['location'].rsplit(':', 1)[0] + ':1')), {}),
        ('E1c', 'a paraphrase in place of the verbatim line', edit(lambda d: E(d, 'PE-4').__setitem__('assertion_verbatim', E(d, 'PE-4')['summary'])), {}),
        ('E1d', 'a run id the line does not name', put('PE-1', 'run_id', '36257341186'), {}),
        ('E1e', 'a wrong digest of the verbatim line', put('PE-5', 'assertion_sha256', '0' * 64), {}),
        ('E2a', 'a cited id that names an object', put('PE-1', 'cited_head', head), {}),
        ('E2b', 'a cited id that is a prefix of the real head', edit(lambda d: E(d, 'PE-2').__setitem__('cited_head', E(d, 'PE-2')['real_head'][:12])), {}),
        ('E2c', 'a cited id sharing 6 digits', edit(lambda d: E(d, 'PE-3').__setitem__('cited_head', E(d, 'PE-3')['real_head'][:6] + ('0' if E(d, 'PE-3')['real_head'][6] != '0' else '1') + 'abcdef')), {}),
        ('E2d', 'a cited id of 6 digits', put('PE-5', 'cited_head', '085028'), {}),
        ('E2e', 'a wrong shared-digit count', put('PE-5', 'shared_digits', 8), {}),
        ('E3a', 'a wrong recorded tree', put('PE-1', 'real_tree', '0' * 40), {}),
        ('E3b', 'a wrong recorded parent', put('PE-2', 'real_parent', '0' * 40), {}),
        ('E3c', 'empty content checks', put('PE-3', 'content_checks', []), {}),
        ('E3d', 'a wrong #check count', put_check('PE-1', 'count_lines_matching', 'expect', 21), {}),
        ('E3d', 'a wrong theorem count', put_check('PE-3', 'count_lines_matching', 'expect', 53), {}),
        ('E3e', 'a line without the notation', put_check('PE-1', 'line_contains', 'line', 357), {}),
        ('E3f', 'an import order that does not hold', edit(lambda d: E(d, 'PE-1')['content_checks'][ck('PE-1', 'consecutive_lines')].__setitem__('lines', list(reversed(E(d, 'PE-1')['content_checks'][ck('PE-1', 'consecutive_lines')]['lines'])))), {}),
        ('E3g', 'a diff touching other paths', edit(lambda d: E(d, 'PE-2')['content_checks'][ck('PE-2', 'diff_paths')]['expect'].append('papers/Main.md')), {}),
        ('E3g', 'a diff from a parent off main missing a path', edit(lambda d: E(d, 'PE-3')['content_checks'][ck('PE-3', 'diff_paths')].__setitem__('expect', [])), {}),
        ('E3h', 'a line the diff does not add', put_check('PE-2', 'diff_adds_line', 'text', 'import Mathlib.Foo'), {}),
        ('E3i', 'a line the diff does not remove', put_check('PE-5', 'diff_removes_line', 'text', 'variable {V : Type}'), {}),
        ('E3j', 'wrong diff line counts', put_check('PE-2', 'diff_line_counts', 'removed', 2), {}),
        ('E3j', 'wrong diff line counts off main', put_check('PE-5', 'diff_line_counts', 'added', 2), {}),
        ('E3k', 'a tree that is not the cited tree', put_check('PE-4', 'tree_equals_cited', 'cited_tree', '0' * 40), {}),
        ('E3l', 'a wrong blob at a path', put_check('PE-4', 'blob_at', 'blob', '0' * 40), {}),
        ('E3m', 'blobs compared with a commit that differs', put_check('PE-4', 'blobs_equal_at', 'other', data['entries'][ix['PE-4']]['content_checks'][ck('PE-4', 'frozen_edit')]['base']['commit']), {}),
        ('E3n', 'an edit that is not the frozen one', edit(lambda d: E(d, 'PE-4')['content_checks'][ck('PE-4', 'frozen_edit')]['edits'][1].__setitem__(1, 'probes_a41_hulls, probes_foundations, probes_a45]')), {}),
        ('E3p', 'edits read from another name in the source', edit(lambda d: E(d, 'PE-4')['content_checks'][ck('PE-4', 'frozen_edit')]['source'].__setitem__('name', 'IMPORT_EDIT')), {}),
        ('E3p', 'a base blob that is not the frozen one', edit(lambda d: E(d, 'PE-4')['content_checks'][ck('PE-4', 'frozen_edit')]['base'].__setitem__('blob', '0' * 40)), {}),
        ('E3o', 'a content check of unknown kind', edit(lambda d: E(d, 'PE-1')['content_checks'].append({'kind': 'line_count'})), {}),
        ('E3t', 'a diff base that is a stored blob, not a commit', put_check('PE-2', 'diff_paths', 'against', a_blob), {}),
        ('E4a', 'a README without a row', lambda d, r: (d, r.replace(pe3_row, '| PE-X |')), {}),
        ('E4a', 'an entry missing from errata.json', edit(lambda d: d['entries'].pop(ix['PE-5'])), {}),
        ('E4b', 'a wrong expected count', put_top('expected_count', 6), {}),
        ('E4c', 'a README location mismatch', lambda d, r: (d, r.replace(E(d, 'PE-2')['location'] + ' |', E(d, 'PE-2')['location'][:-1] + '2 |')), {}),
        ('E4c', 'a README row with another status', lambda d, r: (d, r.replace('| incomplete | partly holds |', '| incomplete | holds |')), {}),
        ('E4c', 'a README row with an extra cell', lambda d, r: (d, r.replace(pe1_line, pe1_line + ' extra |')), {}),
        ('E4d', 'a verdict outside the vocabulary', put('PE-1', 'verdict', 'mostly'), {}),
        ('E4e', 'an explanation outside the vocabulary', put('PE-2', 'explanation', 'partial'), {}),
        ('E4f', 'a status the rule does not derive', put('PE-3', 'status', 'holds'), {}),
        ('E4g', 'a stated rule that is not the checker\'s', edit(lambda d: d['status_rule']['table'][1].__setitem__('status', 'holds')), {}),
        ('E4h', 'an empty jobs list', edit(lambda d: E(d, 'PE-4')['outcome'].__setitem__('jobs', [])), {}),
        ('E4i', 'every_job_head_is_the_real_head false', edit(lambda d: E(d, 'PE-5')['outcome'].__setitem__('every_job_head_is_the_real_head', False)), {}),
        ('E4j', 'an outcome without a served digest', edit(lambda d: E(d, 'PE-4')['outcome']['log_facts'][0].__setitem__('served_sha256', '')), {}),
        ('E4k', 'a run record with another attempt', edit(lambda d: E(d, 'PE-5')['outcome']['run'].__setitem__('attempt', 2)), {}),
        ('E4l', 'an entry removed from errata.json, the README and the count alike', without_pe5, {}),
        ('E4l', 'a consistent emptying: no entries, no rows, count 0, no objects', emptied, {'overlay': {o: None for o in first_stored}}),
        ('E5a', 'a stored object whose bytes changed', lambda d, r: (d, r), {'overlay': {first_stored[0]: (lambda raw: raw[:-1] + bytes([raw[-1] ^ 1]))(store.raw(first_stored[0]))}}),
        ('E5a', 'a stored file no check reads that does not hash to its name', edit(lambda d: d['object_store']['objects'].append({'oid': '0' * 40, 'type': 'blob', 'size': 1})), {'overlay': {'0' * 40: b'blob 1\0x'}}),
        ('E5b', 'a manifest without one of the stored objects', edit(lambda d: d['object_store']['objects'].pop()), {}),
        ('E5c', 'a stored object no check reads', edit(lambda d: d['object_store']['objects'].append({'oid': extra_oid, 'type': 'blob', 'size': 2})), {'overlay': {extra_oid: extra_raw}}),
        ('E5d', 'a wrong recorded size', edit(lambda d: d['object_store']['objects'][0].__setitem__('size', d['object_store']['objects'][0]['size'] + 1)), {}),
        ('E3u', 'a stored blob removed, with --require-objects', drop({a_blob}), {'overlay': {a_blob: None}, 'require': True}),
        ('E3u', "PE-5's real-head commit removed, with --require-objects", drop({h5}), {'overlay': {h5: None}, 'require': True}),
    ]
    if info['cross_checked']:
        cases.append(('E3x', 'a git route that disagrees', lambda d, r: (d, r), {'xflip': ('PE-1', 0)}))
    caught = []
    for code, name, mut, opts in cases:
        d, r = mut(copy.deepcopy(data), readme)
        f, u, i = check(d, r, opts.get('require', False), opts.get('overlay'), opts.get('xflip'))
        if not any(x.code == code for x in f):
            raise AssertionError('mutation not caught as %s: %s (%r)' % (code, name, [str(x) for x in f + u]))
        if not d['entries'] and ('no real head' in summary_line(f, u, i) or 'no entries' not in summary_line(f, u, i)):
            raise AssertionError('with no entries the summary reads %r' % summary_line(f, u, i))
        caught.append(code)
    # without --require-objects a missing object, a blob or a real head, leaves the verdict UNCHECKED, never HOLDS,
    # and the exit nonzero
    for name, oid in (('a stored blob', a_blob), ("PE-5's real-head commit", h5)):
        d, _ = drop({oid})(copy.deepcopy(data), readme)
        f, u, _ = check(d, readme, False, {oid: None})
        if f or not any(x.code == 'E3u' for x in u) or verdict(f, u) != 'UNCHECKED' or not EXIT[verdict(f, u)]:
            raise AssertionError('%s removed was not reported UNCHECKED with a nonzero exit: %r %r' % (
                name, [str(x) for x in f], [str(x) for x in u]))
    caught.append('E3u')
    missing = sorted(set(CODES) - set(caught) - ({'E3x'} if not info['cross_checked'] else set()))
    if missing:
        raise AssertionError('sub-codes without a mutation: %r' % missing)
    return len(cases) + 2, info


def put_top(key, val):
    def m(d, r):
        d[key] = val
        return d, r
    return m


def main():
    args = sys.argv[1:]
    data = json.load(open(os.path.join(HERE, 'errata.json'), encoding='utf-8'))
    readme = open(os.path.join(HERE, 'README.md'), encoding='utf-8').read()
    if '--self-test' in args:
        n, info = self_test(data, readme)
        print('errata self-test: OK (%d mutations, each caught by its own sub-code; %d sub-codes; git cross-check %s)'
              % (n, len(CODES), 'exercised on ' + ', '.join(info['cross_checked']) if info['cross_checked']
                 else 'not exercised: no real head is in this repository'))
        return 0
    fails, unchecked, info = check(data, readme, '--require-objects' in args)
    for x in fails:
        print('FAIL', x)
    for x in unchecked:
        print('UNCHECKED', x)
    print(summary_line(fails, unchecked, info))
    return EXIT[verdict(fails, unchecked)]


if __name__ == '__main__':
    sys.exit(main())
