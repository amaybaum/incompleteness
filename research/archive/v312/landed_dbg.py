#!/usr/bin/env python3
"""V3-12's census of the legacy protocol machinery, measured at one commit.

Usage: census.py <repository> <commit> <output directory>

Reads git objects at <commit> and nothing else, so the same commit gives the same bytes on any
checkout. Writes two files into the output directory:

- legacy-records.json -- the legacy-records population: the closed namespaces, and every legacy
  protocol record in them or pinned individually, by path and blob.
- census.json -- every predicate of the guard verification/lean/edge_rigidity_probe.py, with its
  class under the rules below, the files it reads, the history it executes, and the reason.

The rules, applied in order, first match wins:

  structural   bookkeeping of an accumulator: its initialization, or the line that lists the
               failed entries of a check table.
  retire-whole the predicates of R7-VIS and R7-ARCH, synthetic regressions of archive-mode
               chronology.
  retire-history
               the predicate, or anything it reaches through helper calls, module-level values
               and their in-place mutations, or the control-flow headers that decide whether it
               runs, executes a git subprocess, reads the host environment, reads the prospective
               seal declaration or baseline, or reads verification/seals/ through the filesystem.
  redundant    every file the predicate reads resolves statically, it reads at least one, and
               every one lies in the legacy-records population; or it is one of the adjudicated
               predicates listed in ADJUDICATED, each read by hand.
  retire-machinery
               a predicate of an infrastructure round whose subject is the retired machinery
               (R7-SI1, R7-SI2, R7-SI3, R7-GR1, R7-GR2, R7-CV1): the seal validator, the guard's
               own code text, the V2 store and its wiring.
  retain       everything else: it reads a file outside the population, reads no file (an exact
               computation over constants), or has a read site that does not resolve statically.

A predicate is any module-level statement that can change a check's verdict: an assignment or
augmented assignment to the check's accumulator, or an entry written into or appended to a check
table (`_<x>_checks`, `_<x>_bad`) the accumulator is computed from. Statements inside function bodies are not
predicates; they are reached as helpers."""
import ast
import bisect
import collections
import hashlib
import json
import os
import re
import subprocess
import sys

GUARD = 'verification/lean/edge_rigidity_probe.py'
MIGRATION = 'verification/migration-manifest.json'
CERTIFICATES = 'verification/certificates'
SEALS = 'verification/seals'
# The V2 conformance corpus tests the V2 implementation and retires with it; it is not a record.
NOT_RECORDS = ('verification/certificates/conformance',)
WHOLE = {'R7-VIS', 'R7-ARCH'}
MACHINERY = {'R7-SI1', 'R7-SI2', 'R7-SI3', 'R7-GR1', 'R7-GR2', 'R7-CV1'}
_DRIFT = ('the drift control of a redundant freeze pin: the pin run with a reader that appends one '
          'byte to the pinned record, so it reads only that record')
_HYE = 'the mutation control of the HYE seal comparison, run on a fabricated seal state'
# Read by hand: read sites the resolver leaves open, each reading legacy records only.
ADJUDICATED = {
    ('R7-HYE', 'ok_hye &= _hye_seals_untouched()'):
        'compares the seal records of HYA, HYB and HYE, read from verification/seals/ through the '
        'record reader, with constants, and reads the HYE preregistration',
    ('R7-HYE', 'ok_hye &= _hye_m26 != _hye_seal_state() and not _hye_seals_untouched(_hye_m26)'): _HYE,
    ('R7-HYE', 'ok_hye &= _hye_m27 != _hye_seal_state() and not _hye_seals_untouched(_hye_m27)'): _HYE,
    ('R7-NLV', "_nlv_checks['freeze drift'] = not _nlv_freeze_pin(lambda p: _bb_read(p) + (b'\\n' if "
               "p == _NLVDIR + 'preregistration.md' else b''))"): _DRIFT,
    ('R7-SI1', "ok_si1 &= _bb_blob(_SI1CENSUSREL, read=lambda p: _bb_read(p) + (b'\\n' if p == "
               "_SI1CENSUSREL else b'')) != _SI1_CENSUS_BLOB"): _DRIFT,
    ('R7-SI2', 'ok_si2 &= _si2_drift(_p)(_p) != _bb_read(_p)'): _DRIFT,
    ('R7-SI2', 'ok_si2 &= not _si2_freeze_pin(_p, _si2_drift(_p))'): _DRIFT,
    ('R7-SI2', 'ok_si2 &= _si2_freeze_pin(_q, _si2_drift(_p))'): _DRIFT,
    ('R7-SI2', "ok_si2 &= _bb_blob(_SI2CENSUSREL, read=lambda p: _bb_read(p) + (b'\\n' if p == "
               "_SI2CENSUSREL else b'')) != _SI2_CENSUS_BLOB"): _DRIFT,
    ('R7-SI3', 'ok_si3 &= _si3_drift(_SI3FRZ)(_SI3FRZ) != _bb_read(_SI3FRZ)'): _DRIFT,
    ('R7-SI3', 'ok_si3 &= not _si3_freeze_pin(_si3_drift(_SI3FRZ))'): _DRIFT,
    ('R7-SI3', 'ok_si3 &= _si3_drift(_SI3AMD)(_SI3AMD) != _bb_read(_SI3AMD)'): _DRIFT,
    ('R7-SI3', 'ok_si3 &= not _si3_amend_pin(_si3_drift(_SI3AMD))'): _DRIFT,
}


# ---------------------------------------------------------------------------------------------
# git at one commit
# ---------------------------------------------------------------------------------------------
def git(repo, *args):
    return subprocess.run(('git', '-C', repo) + args, check=True, capture_output=True).stdout


def tree(repo, commit):
    """{path: (mode, blob)} for every file at commit."""
    out = {}
    for rec in git(repo, 'ls-tree', '-r', '-z', commit).split(b'\0'):
        if rec:
            meta, path = rec.split(b'\t', 1)
            mode, _typ, blob = meta.split()
            out[path.decode('utf-8')] = (mode.decode(), blob.decode())
    return out


def show(repo, commit, path):
    return git(repo, 'show', '%s:%s' % (commit, path))


# ---------------------------------------------------------------------------------------------
# the legacy-records population
# ---------------------------------------------------------------------------------------------
def under(path, directory):
    return path == directory or path.startswith(directory + '/')


def population(repo, commit, files):
    """The closed namespaces and the records, at commit. A legacy round directory is a directory
    holding a preregistration.md that carries no `v3-round` block; a native round's directory is
    not legacy. Individual pins are the V2 evidence and control-plane paths outside the closed
    namespaces."""
    rounds = []
    for p in sorted(files):
        if p.startswith('verification/') and p.endswith('/preregistration.md'):
            if b'```v3-round' not in show(repo, commit, p):
                rounds.append(p[:-len('/preregistration.md')])
    for a in rounds:
        for b in rounds:
            if a != b and under(b, a):
                raise SystemExit('census: nested round directories %s, %s' % (a, b))
    closed = sorted([CERTIFICATES, SEALS] + rounds)
    pins = set()
    for p in sorted(files):
        if p.startswith(CERTIFICATES + '/') and p.count('/') == 2 and p.endswith('.json'):
            cert = json.loads(show(repo, commit, p))
            if cert.get('schema') != 'oi-round-certificate':
                continue
            for e in cert.get('evidence', []) + cert.get('control_plane', []):
                pins.add(e['path'])
    records = {}
    for p, (mode, blob) in files.items():
        if any(under(p, n) for n in NOT_RECORDS):
            continue
        if any(under(p, d) for d in closed) or p in pins:
            if mode != '100644':
                raise SystemExit('census: record %s has mode %s' % (p, mode))
            records[p] = blob
    missing = sorted(p for p in pins if p not in files)
    if missing:
        raise SystemExit('census: pinned paths absent at %s: %s' % (commit, missing))
    individual = sorted(p for p in pins if not any(under(p, d) for d in closed))
    return {'closed': closed, 'individual': individual, 'records': dict(sorted(records.items())),
            'rounds': rounds}


def covered(path, pop):
    if any(under(path, n) for n in NOT_RECORDS):
        return False
    return path in pop['individual'] or any(under(path, d) for d in pop['closed'])


# ---------------------------------------------------------------------------------------------
# the guard's syntax
# ---------------------------------------------------------------------------------------------
class Guard:
    def __init__(self, src, migrated, repo_root):
        self.src = src
        self.lines = src.split('\n')
        self.tree = ast.parse(src)
        self.migrated = migrated
        self.root = repo_root
        self.abs_file = os.path.join(repo_root, *GUARD.split('/'))
        self.funcs = {n.name: n for n in ast.walk(self.tree) if isinstance(n, ast.FunctionDef)}
        self.func_lines = set()
        for f in ast.walk(self.tree):
            if isinstance(f, (ast.FunctionDef, ast.Lambda)):
                self.func_lines.update(range(f.lineno, f.end_lineno + 1))
        self.parent = {}
        for p in ast.walk(self.tree):
            for c in ast.iter_child_nodes(p):
                self.parent[c] = p
        self.defs = collections.defaultdict(list)
        self.muts = collections.defaultdict(list)
        for n in ast.walk(self.tree):
            if getattr(n, 'lineno', None) is None or n.lineno in self.func_lines:
                continue
            for name in self.bound_names(n):
                self.defs[name].append(n)
            m = self.mutated(n)
            if m:
                self.muts[m].append(n)
        for k in self.defs:
            self.defs[k].sort(key=lambda d: d.lineno)
        self.calls_of = {k: self.calls(v) for k, v in self.funcs.items()}
        self.locals_of = {k: self.bound_in(v) for k, v in self.funcs.items()}

    @staticmethod
    def names_in(t):
        if isinstance(t, ast.Name):
            yield t.id
        elif isinstance(t, (ast.Tuple, ast.List)):
            for e in t.elts:
                yield from Guard.names_in(e)
        elif isinstance(t, ast.Starred):
            yield from Guard.names_in(t.value)

    def bound_names(self, n):
        if isinstance(n, ast.Assign):
            return [x for t in n.targets for x in self.names_in(t)]
        if isinstance(n, (ast.AugAssign, ast.AnnAssign, ast.For)):
            return list(self.names_in(n.target))
        if isinstance(n, ast.With):
            return [x for i in n.items if i.optional_vars is not None for x in self.names_in(i.optional_vars)]
        return []

    @staticmethod
    def root_name(t):
        while isinstance(t, (ast.Subscript, ast.Attribute)):
            t = t.value
        return t.id if isinstance(t, ast.Name) else None

    def mutated(self, n):
        """The module-level name a statement mutates in place, if any."""
        if isinstance(n, ast.Assign):
            for t in n.targets:
                if isinstance(t, (ast.Subscript, ast.Attribute)):
                    return self.root_name(t)
        elif isinstance(n, ast.AugAssign) and isinstance(n.target, (ast.Subscript, ast.Attribute)):
            return self.root_name(n.target)
        elif isinstance(n, ast.Expr) and isinstance(n.value, ast.Call) and \
                isinstance(n.value.func, ast.Attribute) and n.value.func.attr in (
                    'append', 'extend', 'update', 'add', 'setdefault', 'insert'):
            return self.root_name(n.value.func.value)
        return None

    def own_targets(self, n):
        """The accumulator or table a predicate writes. Its other writes are other predicates, not
        inputs of this one."""
        if isinstance(n, ast.Assign):
            return {self.root_name(t) for t in n.targets} - {None}
        if isinstance(n, ast.AugAssign):
            return {self.root_name(n.target)} - {None}
        if isinstance(n, ast.Expr) and isinstance(n.value, ast.Call) and isinstance(n.value.func, ast.Attribute):
            return {self.root_name(n.value.func.value)} - {None}
        return set()

    def latest(self, name, line):
        ds = self.defs.get(name, [])
        i = bisect.bisect_right([d.lineno for d in ds], line) - 1
        return ds[i] if i >= 0 else None

    def calls(self, node):
        return {m.func.id for m in ast.walk(node) if isinstance(m, ast.Call) and
                isinstance(m.func, ast.Name) and m.func.id in self.funcs}

    def reach(self, seed):
        seen, todo = set(), list(seed)
        while todo:
            f = todo.pop()
            if f not in seen:
                seen.add(f)
                todo += list(self.calls_of[f])
        return seen

    @staticmethod
    def bound_in(node):
        """Names bound inside node other than at module level: comprehension targets, lambda and
        function parameters, and every name a function body stores."""
        out = set()
        for n in ast.walk(node):
            if isinstance(n, ast.comprehension):
                out |= {m.id for m in ast.walk(n.target) if isinstance(m, ast.Name)}
            elif isinstance(n, (ast.Lambda, ast.FunctionDef)):
                a = n.args
                out |= {x.arg for x in a.posonlyargs + a.args + a.kwonlyargs}
                out |= {x.arg for x in (a.vararg, a.kwarg) if x}
                if isinstance(n, ast.FunctionDef):
                    out |= {m.id for m in ast.walk(n) if isinstance(m, ast.Name) and isinstance(m.ctx, ast.Store)}
        return out

    def context_of(self, n):
        """The control-flow headers that decide whether n runs: if and while tests, conditional
        expression tests, for iterables and with items, up to the module."""
        out = []
        a = self.parent.get(n)
        while a is not None and not isinstance(a, ast.Module):
            if isinstance(a, (ast.If, ast.While, ast.IfExp)):
                out.append(a.test)
            elif isinstance(a, ast.For):
                out.append(a.iter)
            elif isinstance(a, ast.With):
                out.extend(i.context_expr for i in a.items)
            a = self.parent.get(a)
        return out

    def statements(self, name, line):
        """The module-level statements that determine a name's value at line: its latest
        definition, the in-place mutations after it, and the headers deciding each of them."""
        d = self.latest(name, line)
        start = d.lineno if d is not None else 0
        muts = [m for m in self.muts.get(name, []) if start <= m.lineno < line and m is not d]
        return d, muts

    def seg(self, n):
        return '\n'.join(self.lines[n.lineno - 1:n.end_lineno])

    @staticmethod
    def text(n):
        """The statement's canonical text: its unparsed syntax, without comments or layout."""
        return ast.unparse(n)


# ---------------------------------------------------------------------------------------------
# the predicates
# ---------------------------------------------------------------------------------------------
def checks_of(g):
    out = []
    for n in g.tree.body:
        if isinstance(n, ast.Expr) and isinstance(n.value, ast.Call) and \
                isinstance(n.value.func, ast.Name) and n.value.func.id == 'check':
            a = n.value.args
            msg = ''.join(c.value for c in ast.walk(a[2]) if isinstance(c, ast.Constant)
                          and isinstance(c.value, str)) if len(a) > 2 else ''
            out.append({'check': a[0].value, 'line': n.lineno, 'accumulator': ast.unparse(a[1]),
                        'node': a[1], 'message': msg})
    return out


TABLE = re.compile(r'_[a-z0-9]+_(checks|bad)')


def predicates_of(g, chk):
    """The module-level writes before the check's call to its accumulator names and to the check
    tables (`_<x>_checks`, `_<x>_bad`) those names are computed from."""
    names = {m.id for m in ast.walk(chk['node']) if isinstance(m, ast.Name)}
    grown = True
    while grown:
        grown = False
        for nm in list(names):
            d = g.latest(nm, chk['line'])
            if isinstance(d, ast.Assign) and not isinstance(d.value, ast.Constant):
                inner = g.bound_in(d.value)
                for m in ast.walk(d.value):
                    if isinstance(m, ast.Name) and m.id in inner:
                        continue
                    if isinstance(m, ast.Name) and m.id not in names and TABLE.fullmatch(m.id) and \
                            g.muts.get(m.id):
                        names.add(m.id)
                        grown = True
    out = []
    for n in ast.walk(g.tree):
        if getattr(n, 'lineno', None) is None or n.lineno in g.func_lines or n.lineno >= chk['line']:
            continue
        if isinstance(n, (ast.Assign, ast.AugAssign)) and g.own_targets(n) & names:
            out.append(n)
        elif isinstance(n, ast.Expr) and g.mutated(n) in names:
            out.append(n)
    out.sort(key=lambda n: (n.lineno, n.col_offset))
    return out


# ---------------------------------------------------------------------------------------------
# history: git, host environment, seal state, the seals directory
# ---------------------------------------------------------------------------------------------
STATE_NAMES = {'_MANIFEST_PROSPECTIVE', '_MANIFEST_BASELINE'}
FS_CALLS = ('open', 'listdir', 'join', 'glob', 'isdir', 'exists', 'walk', 'scandir', 'isfile')


def direct_kinds(node):
    k = set()
    for n in ast.walk(node):
        if isinstance(n, ast.Call):
            f = n.func
            fname = f.attr if isinstance(f, ast.Attribute) else (f.id if isinstance(f, ast.Name) else '')
            if fname in ('run', 'check_output', 'Popen', 'call', 'check_call'):
                for a in n.args[:1]:
                    if any(isinstance(c, ast.Constant) and c.value == 'git' for c in ast.walk(a)):
                        k.add('git')
            if fname in FS_CALLS:
                for a in n.args:
                    for c in ast.walk(a):
                        if isinstance(c, ast.Constant) and isinstance(c.value, str) and \
                                (c.value in ('seals', 'seals/') or 'verification/seals' in c.value):
                            k.add('seals-path')
        if isinstance(n, ast.Attribute) and n.attr == 'environ':
            k.add('env')
        if isinstance(n, ast.Name) and n.id in STATE_NAMES:
            k.add('state')
    return k


class History:
    def __init__(self, g):
        self.g = g
        kinds = {k: direct_kinds(v) for k, v in g.funcs.items()}
        changed = True
        while changed:
            changed = False
            for k in g.funcs:
                new = set(kinds[k])
                for c in g.calls_of[k]:
                    new |= kinds[c]
                if new != kinds[k]:
                    kinds[k], changed = new, True
        self.fk = kinds
        self.memo = {}

    def of_nodes(self, nodes, line, own=frozenset(), seen=None):
        g = self.g
        k = set()
        loads = set()
        helpers = set()
        for x in nodes:
            k |= direct_kinds(x)
            helpers |= g.calls(x)
            loads |= {m.id for m in ast.walk(x) if isinstance(m, ast.Name) and isinstance(m.ctx, ast.Load)}
        for h in g.reach(helpers):
            k |= self.fk[h]
            loads |= {m.id for m in ast.walk(g.funcs[h]) if isinstance(m, ast.Name) and
                      isinstance(m.ctx, ast.Load) and m.id in g.defs and m.id not in g.locals_of[h]}
        for nm in sorted(loads - set(own)):
            k |= self.name(nm, line, 0, seen)
        return k

    def name(self, nm, line, depth, seen):
        key = (nm, line)
        if key in self.memo:
            return self.memo[key]
        seen = set() if seen is None else seen
        if key in seen or depth > 8:
            return set()
        seen.add(key)
        g = self.g
        d, muts = g.statements(nm, line)
        k = set()
        for st in ([d] if d is not None else []) + muts:
            if st is d:
                root = st.value if isinstance(st, (ast.Assign, ast.AugAssign, ast.AnnAssign)) and st.value \
                    else (st.iter if isinstance(st, ast.For) else st)
                parts = [root] + g.context_of(st)
            else:
                parts = [st] + g.context_of(st)
            for x in parts:
                k |= direct_kinds(x)
                for h in g.reach(g.calls(x)):
                    k |= self.fk[h]
                    for m in ast.walk(g.funcs[h]):
                        if isinstance(m, ast.Name) and isinstance(m.ctx, ast.Load) and m.id in g.defs \
                                and m.id not in g.locals_of[h]:
                            k |= self.name(m.id, st.lineno, depth + 1, seen)
                for m in ast.walk(x):
                    if isinstance(m, ast.Name) and isinstance(m.ctx, ast.Load) and m.id != nm:
                        k |= self.name(m.id, st.lineno - 1 if st is d and m.id == nm else st.lineno,
                                       depth + 1, seen)
        self.memo[key] = k
        return k


# ---------------------------------------------------------------------------------------------
# reads: which repository files a predicate reads, resolved statically
# ---------------------------------------------------------------------------------------------
class U(Exception):
    pass


PRIMS = {'open', 'os.listdir', 'os.path.exists', 'os.path.isdir', 'os.path.isfile', 'glob.glob',
         'os.path.getsize', 'listdir'}
READERS = ('_bb_read', '_bb_blob', '_a11p_root', '_artifact')   # the guard's own path primitives
OPAQUE = ('subprocess.run', 'subprocess.check_output', 'subprocess.Popen', 'exec', 'eval')
FAIL = (U, TypeError, IndexError, AttributeError, KeyError)


class Reads:
    def __init__(self, g):
        self.g = g
        self.rp = {k: self.reader_params(v) for k, v in g.funcs.items()}
        self.psites = {}
        changed = True
        while changed:
            changed = False
            for name, f in g.funcs.items():
                if name in READERS:
                    continue
                ps = self.fparams(f)
                cur = []
                for n in ast.walk(f):
                    if not (isinstance(n, ast.Call) and n.args):
                        continue
                    cn = self.callee(n, name)
                    if self.is_prim(cn):
                        if self.uses(n.args[0], ps):
                            cur.append(n)
                    elif self.psites.get(cn) and any(self.uses(a, ps) for a in self.args(n)):
                        cur.append(n)
                if len(cur) != len(self.psites.get(name, [])):
                    self.psites[name], changed = cur, True
        self.fsites = {k: (set() if k in READERS else self.sites(v, v.lineno, self.fparams(v),
                                                                  g.locals_of[k], k))
                       for k, v in g.funcs.items()}
        self.memo = {}

    @staticmethod
    def fparams(f):
        a = f.args
        return [x.arg for x in a.posonlyargs + a.args + a.kwonlyargs]

    @staticmethod
    def args(n):
        return n.args + [k.value for k in n.keywords]

    @staticmethod
    def uses(node, names):
        return bool({m.id for m in ast.walk(node) if isinstance(m, ast.Name)} & set(names))

    @staticmethod
    def is_prim(cn):
        return cn in PRIMS or cn in READERS

    def reader_params(self, f):
        """Parameters whose default is a reader: calling one reads its first argument as that
        default would."""
        a = f.args
        pos = a.args[len(a.args) - len(a.defaults):] if a.defaults else []
        out = {}
        for p, dflt in list(zip(pos, a.defaults)) + [(k, d) for k, d in zip(a.kwonlyargs, a.kw_defaults) if d]:
            dn = ast.unparse(dflt)
            if self.is_prim(dn) or dn in self.g.funcs:
                out[p.arg] = dn
        return out

    def callee(self, n, fname):
        cn = ast.unparse(n.func)
        if fname and cn in self.rp.get(fname, {}):
            return self.rp[fname][cn]
        return cn

    def evs(self, node, line, env=None, depth=0):
        """Every value a path expression can take under module constants, env and literal loop
        iterables; U when it cannot be evaluated."""
        g, env = self.g, env or {}
        if depth > 20:
            raise U()
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            return [node.value]
        if isinstance(node, ast.Name):
            if node.id in env:
                return list(env[node.id])
            if node.id == '__file__':
                return [g.abs_file]
            d = g.latest(node.id, line)
            if isinstance(d, ast.Assign) and len(d.targets) == 1 and isinstance(d.targets[0], ast.Name):
                return self.evs(d.value, d.lineno - 1, None, depth + 1)
            if isinstance(d, ast.For) and isinstance(d.target, ast.Name) and isinstance(d.iter, (ast.Tuple, ast.List)):
                return [v for e in d.iter.elts for v in self.evs(e, d.lineno - 1, None, depth + 1)]
            raise U()
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
            return [x + y for x in self.evs(node.left, line, env, depth + 1)
                    for y in self.evs(node.right, line, env, depth + 1)]
        if isinstance(node, ast.JoinedStr):
            outs = ['']
            for v in node.values:
                vals = [v.value] if isinstance(v, ast.Constant) else self.evs(v.value, line, env, depth + 1)
                outs = [o + x for o in outs for x in vals]
            return outs
        if isinstance(node, ast.Call):
            dotted = ast.unparse(node.func)
            a = node.args
            if dotted == 'os.path.join':
                outs = [()]
                for x in a:
                    outs = [o + (v,) for o in outs for v in self.evs(x, line, env, depth + 1)]
                return [os.path.join(*o) for o in outs]
            if dotted == 'os.path.dirname':
                return [os.path.dirname(v) for v in self.evs(a[0], line, env, depth + 1)]
            if dotted in ('os.path.abspath', 'os.path.normpath', 'os.path.realpath'):
                return [os.path.normpath(os.path.abspath(v)) for v in self.evs(a[0], line, env, depth + 1)]
            if dotted == '_artifact':
                return [self.artifact(v) for v in self.evs(a[0], line, env, depth + 1)]
        raise U()

    def artifact(self, name):
        return os.path.join(self.g.root, 'verification', *self.g.migrated.get(name, name).split('/'))

    def prim_paths(self, cn, arg, line, env, shadow):
        if {m.id for m in ast.walk(arg) if isinstance(m, ast.Name)} & (set(shadow) - set(env)):
            return {'UNRESOLVED'}
        try:
            vals = self.evs(arg, line, env)
        except FAIL:
            return {'UNRESOLVED'}
        out = set()
        for v in vals:
            if not isinstance(v, str):
                return {'UNRESOLVED'}
            if cn in ('_bb_read', '_bb_blob', '_artifact'):
                p = self.artifact(v)
            elif cn == '_a11p_root':
                p = os.path.join(self.g.root, v)
            else:
                p = v
            p = os.path.normpath(p)
            if not p.startswith(self.g.root + os.sep):
                return {'UNRESOLVED'}
            out.add(os.path.relpath(p, self.g.root).replace(os.sep, '/'))
        return out

    def call_reads(self, n, line, env, depth, shadow, fname):
        cn = self.callee(n, fname)
        if self.is_prim(cn):
            return self.prim_paths(cn, n.args[0], line, env, shadow)
        if {m.id for a in self.args(n) for m in ast.walk(a) if isinstance(m, ast.Name)} & (set(shadow) - set(env)):
            return {'UNRESOLVED'}
        if depth > 12:
            return {'UNRESOLVED'}
        f = self.g.funcs[cn]
        ps = self.fparams(f)
        bind = {}
        for p, a in zip(ps, n.args):
            try:
                bind[p] = self.evs(a, line, env)
            except FAIL:
                pass
        for k in n.keywords:
            if k.arg in ps:
                try:
                    bind[k.arg] = self.evs(k.value, line, env)
                except FAIL:
                    pass
        out = set()
        for inner in self.psites[cn]:
            out |= self.call_reads(inner, line, bind, depth + 1, self.g.locals_of[cn] - set(bind), cn)
        return out

    def sites(self, node, line, helper_params=(), shadow=None, fname=None):
        out = set()
        shadow = self.g.bound_in(node) if shadow is None else shadow
        for n in ast.walk(node):
            if not isinstance(n, ast.Call):
                continue
            if ast.unparse(n.func) in OPAQUE:
                out.add('UNRESOLVED')           # a child process or executed text reads what it reads
                continue
            if not n.args:
                continue
            cn = self.callee(n, fname)
            if self.is_prim(cn):
                if helper_params and self.uses(n.args[0], helper_params):
                    continue                    # the helper's own parameter: resolved at its call site
                out |= self.call_reads(n, line, {}, 0, shadow, fname)
            elif self.psites.get(cn):
                if helper_params and any(self.uses(a, helper_params) for a in self.args(n)):
                    continue
                out |= self.call_reads(n, line, {}, 0, shadow, fname)
        return out

    def of_nodes(self, nodes, line, own=frozenset()):
        g = self.g
        out, helpers, loads = set(), set(), set()
        for x in nodes:
            out |= self.sites(x, line)
            helpers |= g.calls(x)
            loads |= {m.id for m in ast.walk(x) if isinstance(m, ast.Name) and isinstance(m.ctx, ast.Load)}
        for h in g.reach(helpers):
            out |= self.fsites[h]
            loads |= {m.id for m in ast.walk(g.funcs[h]) if isinstance(m, ast.Name) and
                      isinstance(m.ctx, ast.Load) and m.id in g.defs and m.id not in g.locals_of[h]}
        for nm in sorted(loads - set(own)):
            out |= self.name(nm, line, 0, None)
        return out

    def name(self, nm, line, depth, seen):
        key = (nm, line)
        if key in self.memo:
            return self.memo[key]
        seen = set() if seen is None else seen
        if key in seen or depth > 10:
            return set()
        seen.add(key)
        g = self.g
        d, muts = g.statements(nm, line)
        out = set()
        for st in ([d] if d is not None else []) + muts:
            if st is d:
                root = st.value if isinstance(st, (ast.Assign, ast.AugAssign, ast.AnnAssign)) and st.value \
                    else (st.iter if isinstance(st, ast.For) else st)
                parts = [st if isinstance(st, ast.With) else root] + g.context_of(st)
            else:
                parts = [st] + g.context_of(st)
            for x in parts:
                out |= self.sites(x, st.lineno)
                for h in g.reach(g.calls(x)):
                    out |= self.fsites[h]
                    for m in ast.walk(g.funcs[h]):
                        if isinstance(m, ast.Name) and isinstance(m.ctx, ast.Load) and m.id in g.defs \
                                and m.id not in g.locals_of[h]:
                            out |= self.name(m.id, st.lineno, depth + 1, seen)
                for m in ast.walk(x):
                    if isinstance(m, ast.Name) and isinstance(m.ctx, ast.Load) and m.id != nm:
                        out |= self.name(m.id, st.lineno, depth + 1, seen)
        self.memo[key] = out
        return out


# ---------------------------------------------------------------------------------------------
# the rules
# ---------------------------------------------------------------------------------------------
STRUCTURAL = (re.compile(r'ok_[a-z0-9]+ = True'),
              re.compile(r'_[a-z0-9]+_bad = sorted\(.*'),
              re.compile(r'_[a-z0-9]+_bad = \[name for .*'),
              re.compile(r'_[a-z0-9]+_bad = \[k for k, v in _[a-z0-9]+_checks\.items\(\) if not v\]'),
              re.compile(r'_[a-z0-9]+_checks = \{\}'),
              re.compile(r'_[a-z0-9]+_bad = \[\]'))


def classify(chk, text, hist, reads, pop):
    if any(r.fullmatch(text) for r in STRUCTURAL):
        return 'structural', 'accumulator bookkeeping'
    if chk in WHOLE:
        return 'retire-whole', 'a synthetic regression of archive-mode chronology'
    if hist:
        return 'retire-history', 'executes ' + ', '.join(sorted(hist))
    if (chk, text) in ADJUDICATED:
        return 'redundant', 'adjudicated: ' + ADJUDICATED[(chk, text)]
    if reads and 'UNRESOLVED' not in reads and all(covered(p, pop) for p in reads):
        return 'redundant', 'every file it reads is a legacy record'
    if chk in MACHINERY:
        return 'retire-machinery', 'tests the retired machinery its round installed'
    if 'UNRESOLVED' in reads:
        return 'retain', 'a read site does not resolve statically'
    if not reads:
        return 'retain', 'reads no file: an exact computation over constants'
    return 'retain', 'reads a file outside the legacy records'


def main():
    repo, commit, outdir = sys.argv[1:4]
    root = os.path.realpath(repo)
    commit = git(repo, 'rev-parse', '--verify', commit + '^{commit}').decode().strip()
    files = tree(repo, commit)
    pop = population(repo, commit, files)
    migrated = {k: v['to'] for k, v in json.loads(show(repo, commit, MIGRATION))['entries'].items()}
    g = Guard(show(repo, commit, GUARD).decode('utf-8'), migrated, root)
    hist, reads = History(g), Reads(g)
    lookup = {MIGRATION}                    # read only to locate an artifact, never a protected read
    rows, checks, seen = [], [], set()
    for chk in checks_of(g):
        cls = collections.Counter()
        for n in predicates_of(g, chk):
            if (chk['check'], n.lineno, n.col_offset) in seen:
                raise SystemExit('census: a predicate counted twice at line %d' % n.lineno)
            seen.add((chk['check'], n.lineno, n.col_offset))
            own = g.own_targets(n)
            ctx = g.context_of(n)
            h = hist.of_nodes([n] + ctx, n.lineno, own)
            r = sorted(reads.of_nodes([n] + ctx, n.lineno, own) - lookup)
            text = g.text(n)
            c, why = classify(chk['check'], text, h, r, pop)
            cls[c] += 1
            rows.append({'check': chk['check'], 'line': n.lineno, 'class': c, 'reason': why,
                         'history': sorted(h), 'reads': r,
                         'text_sha256': hashlib.sha256(text.encode('utf-8')).hexdigest(),
                         'text': text})
        live = cls['retain']
        pred = sum(v for k, v in cls.items() if k != 'structural')
        checks.append({'check': chk['check'], 'line': chk['line'], 'predicates': pred,
                       'classes': dict(sorted(cls.items())),
                       'disposition': 'computed' if pred == 0 else 'retained whole' if live == pred
                       else 'removed whole' if live == 0 else 'split'})
    used = {(r['check'], r['text']) for r in rows if r['reason'].startswith('adjudicated')}
    if used != set(ADJUDICATED):
        print('WARN unused')
    totals = collections.Counter(r['class'] for r in rows)
    census = {
        'schema': 'v3-12-census', 'version': 1, 'commit': commit,
        'guard': {'path': GUARD, 'blob': files[GUARD][1], 'checks': checks, 'predicates': rows,
                  'totals': dict(sorted(totals.items())),
                  'dispositions': dict(sorted(collections.Counter(c['disposition'] for c in checks).items()))},
        'legacy_records': {'closed_namespaces': len(pop['closed']), 'legacy_round_directories': len(pop['rounds']),
                           'individual_pins': pop['individual'], 'records': len(pop['records']),
                           'excluded': list(NOT_RECORDS)},
    }
    manifest = {'schema': 'oi-legacy-records', 'version': 1,
                'closed_namespaces': pop['closed'], 'records': pop['records']}
    os.makedirs(outdir, exist_ok=True)
    for name, obj in (('census.json', census), ('legacy-records.json', manifest)):
        with open(os.path.join(outdir, name), 'w', encoding='utf-8', newline='\n') as fh:
            json.dump(obj, fh, indent=1, sort_keys=False, ensure_ascii=False)
            fh.write('\n')
    print('census  %s' % commit)
    print('guard   %d checks, %d predicates: %s' % (len(checks), len(rows), dict(sorted(totals.items()))))
    print('checks  %s' % census['guard']['dispositions'])
    print('records %d in %d closed namespaces (%d legacy round directories) and %d individual pins'
          % (len(pop['records']), len(pop['closed']), len(pop['rounds']), len(pop['individual'])))


if __name__ == '__main__':
    main()
