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
table (`_<x>_checks`, `_<x>_bad`) the accumulator is computed from. Statements inside function
bodies are not predicates; they are reached as helpers."""
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
    ('R7-HYE', 'ok_hye &= _hye_m26 != _hye_seal_state() and '
               'not _hye_seals_untouched(_hye_m26)'): _HYE,
    ('R7-HYE', 'ok_hye &= _hye_m27 != _hye_seal_state() and '
               'not _hye_seals_untouched(_hye_m27)'): _HYE,
    ('R7-NLV', "_nlv_checks['freeze drift'] = not _nlv_freeze_pin(lambda p: _bb_read(p) + "
               "(b'\\n' if p == _NLVDIR + 'preregistration.md' else b''))"): _DRIFT,
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
ADJUDICATED = {(c, ast.unparse(ast.parse(t))): why for (c, t), why in ADJUDICATED.items()}


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


V3_ROUND = re.compile(rb'(?m)^```v3-round\r?$')     # the block opener, by exact line (G10)


def population(repo, commit, files):
    """The closed namespaces and the records, at commit. A legacy round directory is a directory
    holding a preregistration.md with no `v3-round` block opener line; a native round's directory
    is not legacy. Individual pins are the V2 evidence and control-plane paths outside the closed
    namespaces."""
    rounds = []
    for p in sorted(files):
        if p.startswith('verification/') and p.endswith('/preregistration.md'):
            if not V3_ROUND.search(show(repo, commit, p)):
                rounds.append(p[:-len('/preregistration.md')])
    for a in rounds:
        for b in rounds:
            if a != b and under(b, a):
                raise SystemExit('census: nested round directories %s, %s' % (a, b))
    closed = sorted([CERTIFICATES, SEALS] + rounds)
    pins, pinned = set(), []
    for p in sorted(files):
        if p.startswith(CERTIFICATES + '/') and p.count('/') == 2 and p.endswith('.json'):
            cert = json.loads(show(repo, commit, p))
            if cert.get('schema') != 'oi-round-certificate':
                continue
            for e in cert.get('evidence', []) + cert.get('control_plane', []):
                pins.add(e['path'])
                pinned.append((e['path'], e['blob']))
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
    # the control: every blob V2 pins is the population's blob for that path
    disagree = sorted({p for p, b in pinned if records.get(p) != b})
    if disagree:
        raise SystemExit('census: V2 pins that disagree with the population: %s' % disagree)
    individual = sorted(p for p in pins if not any(under(p, d) for d in closed))
    return {'closed': closed, 'individual': individual, 'records': dict(sorted(records.items())),
            'rounds': rounds, 'v2_pins': len(pinned)}


def covered(path, pop):
    if any(under(path, n) for n in NOT_RECORDS):
        return False
    return path in pop['individual'] or any(under(path, d) for d in pop['closed'])


# ---------------------------------------------------------------------------------------------
# the guard's syntax
# ---------------------------------------------------------------------------------------------
class Guard:
    def __init__(self, src, migrated, repo_root):
        self.tree = ast.parse(src)
        self.migrated = migrated
        self.root = repo_root
        self.abs_file = os.path.join(repo_root, *GUARD.split('/'))
        self.parent = {}
        for p in ast.walk(self.tree):
            for c in ast.iter_child_nodes(p):
                self.parent[c] = p
        # functions keyed by definition: a top-level function by its name, a nested one by its
        # name and line, so that two definitions of one name stay two functions
        self.funcs, self.key_of, self.enclosing = {}, {}, {}
        for n in ast.walk(self.tree):
            if isinstance(n, ast.FunctionDef):
                top = self.parent.get(n) is self.tree
                key = n.name if top else '%s@%d' % (n.name, n.lineno)
                self.funcs[key] = n
                self.key_of[n] = key
        self.nested = collections.defaultdict(dict)
        for n, key in self.key_of.items():
            a = self.parent.get(n)
            while a is not None and not isinstance(a, ast.FunctionDef):
                a = self.parent.get(a)
            self.enclosing[key] = self.key_of.get(a)
            if a is not None:
                self.nested[self.key_of[a]][n.name] = key
        self.func_lines = set()
        for f in self.funcs.values():
            self.func_lines.update(range(f.lineno, f.end_lineno + 1))
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
        self.locals_of = {k: self.bound_in(v) for k, v in self.funcs.items()}
        self.calls_of = {k: self.calls(v, k) for k, v in self.funcs.items()}
        # the module-level names each function reads
        self.globals_of = {k: {m.id for m in ast.walk(v) if isinstance(m, ast.Name) and
                               isinstance(m.ctx, ast.Load) and m.id in self.defs and
                               m.id not in self.locals_of[k]}
                           for k, v in self.funcs.items()}

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
            return [x for i in n.items if i.optional_vars is not None
                    for x in self.names_in(i.optional_vars)]
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
        if isinstance(n, ast.Expr) and isinstance(n.value, ast.Call) and \
                isinstance(n.value.func, ast.Attribute):
            return {self.root_name(n.value.func.value)} - {None}
        return set()

    def reaching(self, name, line):
        """The module-level definitions of name that can reach line: walking back from line,
        every definition up to and including the nearest one that is a top-level statement. A
        definition inside a branch, a try or a loop body does not hide the ones before it, and an
        augmented assignment extends the value it follows."""
        ds = self.defs.get(name, [])
        i = bisect.bisect_right([d.lineno for d in ds], line) - 1
        out = []
        while i >= 0:
            d = ds[i]
            out.append(d)
            if isinstance(d, (ast.Assign, ast.AnnAssign, ast.For, ast.With)) and \
                    self.parent.get(d) is self.tree:
                break
            i -= 1
        return out

    def resolve(self, name, scope):
        """The function a name denotes inside scope (a function key, or None for the module):
        a function defined in scope or an enclosing function, unless a local binding of that scope
        shadows it first, and otherwise a top-level function."""
        s = scope
        while s is not None:
            if name in self.nested[s]:
                return self.nested[s][name]
            if name in self.locals_of[s]:
                return None
            s = self.enclosing[s]
        f = self.funcs.get(name)
        return name if f is not None and self.parent.get(f) is self.tree else None

    def calls(self, node, scope=None):
        """The functions node can run: every function it names, called or passed as a value.
        Inside a function, names resolve through its scope; at module level, a name bound inside
        node (a comprehension or lambda variable) is not a function."""
        local = set() if scope is not None else self.bound_in(node)
        out = set()
        for m in ast.walk(node):
            if isinstance(m, ast.Name) and isinstance(m.ctx, ast.Load) and m.id not in local:
                k = self.resolve(m.id, scope)
                if k is not None:
                    out.add(k)
        return out

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
                    out |= {m.id for m in ast.walk(n)
                            if isinstance(m, ast.Name) and isinstance(m.ctx, ast.Store)}
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
        """The module-level statements that determine a name's value at line: the definitions
        that reach it, and the in-place mutations after the earliest of them."""
        ds = self.reaching(name, line)
        start = min(d.lineno for d in ds) if ds else 0
        muts = [m for m in self.muts.get(name, []) if start <= m.lineno < line and m not in ds]
        return ds, muts

    @staticmethod
    def value_of(st):
        """The part of a definition that computes the value: an assignment's right-hand side, a
        for loop's iterable, or the whole of a with statement."""
        if isinstance(st, (ast.Assign, ast.AugAssign, ast.AnnAssign)) and st.value is not None:
            return st.value
        return st.iter if isinstance(st, ast.For) else st

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
            for d in g.reaching(nm, chk['line']):
                if not isinstance(d, ast.Assign) or isinstance(d.value, ast.Constant):
                    continue
                inner = g.bound_in(d.value)
                for m in ast.walk(d.value):
                    if isinstance(m, ast.Name) and m.id not in inner and m.id not in names and \
                            TABLE.fullmatch(m.id) and g.muts.get(m.id):
                        names.add(m.id)
                        grown = True
    out = []
    for n in ast.walk(g.tree):
        if getattr(n, 'lineno', None) is None or n.lineno in g.func_lines or \
                n.lineno >= chk['line']:
            continue
        if isinstance(n, (ast.Assign, ast.AugAssign)) and g.own_targets(n) & names:
            out.append(n)
        elif isinstance(n, ast.Expr) and g.mutated(n) in names:
            out.append(n)
    out.sort(key=lambda n: (n.lineno, n.col_offset))
    return out


def completeness(g):
    """The control on predicates_of: the number of module-level assignments whose target's root is
    a check's accumulator name or check table, and those placed after their check's call."""
    owner = {}
    for chk in checks_of(g):
        for m in ast.walk(chk['node']):
            if isinstance(m, ast.Name):
                owner[m.id] = chk
    for chk in checks_of(g):
        for m in ast.walk(chk['node']):
            if isinstance(m, ast.Name):
                for d in g.reaching(m.id, chk['line']):
                    if isinstance(d, ast.Assign):
                        for x in ast.walk(d.value):
                            if isinstance(x, ast.Name) and TABLE.fullmatch(x.id):
                                owner.setdefault(x.id, chk)
    writes, late = 0, []
    for n in ast.walk(g.tree):
        if isinstance(n, (ast.Assign, ast.AugAssign)) and n.lineno not in g.func_lines:
            for t in (n.targets if isinstance(n, ast.Assign) else [n.target]):
                r = g.root_name(t)
                if r in owner:
                    if n.lineno < owner[r]['line']:
                        writes += 1
                    else:
                        late.append((owner[r]['check'], n.lineno))
                    break
    return writes, late


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
            fname = f.attr if isinstance(f, ast.Attribute) else \
                (f.id if isinstance(f, ast.Name) else '')
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
            loads |= {m.id for m in ast.walk(x)
                      if isinstance(m, ast.Name) and isinstance(m.ctx, ast.Load)}
        for h in g.reach(helpers):
            k |= self.fk[h]
            loads |= g.globals_of[h]
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
        ds, muts = g.statements(nm, line)
        k = set()
        for st in ds + muts:
            if st in ds:
                parts = [g.value_of(st)] + g.context_of(st)
            else:
                parts = [st] + g.context_of(st)
            for x in parts:
                k |= direct_kinds(x)
                for h in g.reach(g.calls(x)):
                    k |= self.fk[h]
                    for gl in g.globals_of[h]:
                        k |= self.name(gl, st.lineno, depth + 1, seen)
                for m in ast.walk(x):
                    if isinstance(m, ast.Name) and isinstance(m.ctx, ast.Load):
                        if m.id != nm:
                            k |= self.name(m.id, st.lineno, depth + 1, seen)
                        elif st in ds:          # x = f(x): the value before this definition
                            k |= self.name(nm, st.lineno - 1, depth + 1, seen)
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
        # the names each function assigns in its own body, parameters included when reassigned
        self.rebound = {k: {m.id for m in ast.walk(v) if isinstance(m, ast.Name) and
                            isinstance(m.ctx, ast.Store)} for k, v in g.funcs.items()}
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
        pairs = list(zip(pos, a.defaults))
        pairs += [(k, d) for k, d in zip(a.kwonlyargs, a.kw_defaults) if d]
        for p, dflt in pairs:
            dn = ast.unparse(dflt)
            if self.is_prim(dn):
                out[p.arg] = dn
            elif isinstance(dflt, ast.Name):
                k = self.g.resolve(dn, self.g.enclosing[self.g.key_of[f]])
                if k is not None:
                    out[p.arg] = k
        return out

    def callee(self, n, fname):
        """What a call runs: a primitive by its dotted name, the default of a reader parameter,
        or the key of the function its name denotes in scope fname."""
        cn = ast.unparse(n.func)
        if fname and cn in self.rp.get(fname, {}):
            return self.rp[fname][cn]
        if self.is_prim(cn) or not isinstance(n.func, ast.Name):
            return cn
        k = self.g.resolve(cn, fname)
        return k if k is not None else cn

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
            ds = g.reaching(node.id, line)
            if not ds:
                raise U()
            out = []
            for d in ds:                # every value any reaching definition can give
                if isinstance(d, ast.Assign) and len(d.targets) == 1 and \
                        isinstance(d.targets[0], ast.Name):
                    out += self.evs(d.value, d.lineno - 1, None, depth + 1)
                elif isinstance(d, ast.For) and isinstance(d.target, ast.Name) and \
                        isinstance(d.iter, (ast.Tuple, ast.List)):
                    out += [v for e in d.iter.elts
                            for v in self.evs(e, d.lineno - 1, None, depth + 1)]
                else:
                    raise U()
            return sorted(set(out))
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
            return [x + y for x in self.evs(node.left, line, env, depth + 1)
                    for y in self.evs(node.right, line, env, depth + 1)]
        if isinstance(node, ast.JoinedStr):
            outs = ['']
            for v in node.values:
                vals = [v.value] if isinstance(v, ast.Constant) else \
                    self.evs(v.value, line, env, depth + 1)
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
                return [os.path.normpath(os.path.abspath(v))
                        for v in self.evs(a[0], line, env, depth + 1)]
            if dotted == '_artifact':
                return [self.artifact(v) for v in self.evs(a[0], line, env, depth + 1)]
        raise U()

    def artifact(self, name):
        rel = self.g.migrated.get(name, name)
        return os.path.join(self.g.root, 'verification', *rel.split('/'))

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
        loaded = {m.id for a in self.args(n) for m in ast.walk(a) if isinstance(m, ast.Name)}
        if loaded & (set(shadow) - set(env)):
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
            out |= self.call_reads(inner, line, bind, depth + 1,
                                   self.g.locals_of[cn] - set(bind), cn)
        return out

    def sites(self, node, line, helper_params=(), shadow=None, fname=None):
        out = set()
        shadow = self.g.bound_in(node) if shadow is None else shadow
        out |= self.passed(node, shadow, fname)
        for n in ast.walk(node):
            if not isinstance(n, ast.Call):
                continue
            if ast.unparse(n.func) in OPAQUE:
                out.add('UNRESOLVED')   # a child process or executed text reads what it reads
                continue
            if fname and isinstance(n.func, ast.Name) and n.func.id in self.rebound[fname] and \
                    n.func.id not in self.rp[fname] and self.g.resolve(n.func.id, fname) is None:
                out.add('UNRESOLVED')   # a call of a name the function rebinds: any callable
                continue
            if not n.args:
                continue
            cn = self.callee(n, fname)
            if self.is_prim(cn):
                if helper_params and self.uses(n.args[0], helper_params):
                    continue            # the helper's own parameter: resolved at its call site
                out |= self.call_reads(n, line, {}, 0, shadow, fname)
            elif self.psites.get(cn):
                if helper_params and any(self.uses(a, helper_params) for a in self.args(n)):
                    continue
                out |= self.call_reads(n, line, {}, 0, shadow, fname)
        return out

    def passed(self, node, shadow, fname):
        """A function passed as a value, rather than called, whose reads depend on its own
        parameters reads what its eventual caller passes it: unresolved, unless it is passed to a
        reader parameter, which reads the paths the receiving function names."""
        called, to_reader = set(), set()
        for n in ast.walk(node):
            if isinstance(n, ast.Call):
                called.add(id(n.func))
                cn = self.callee(n, fname)
                rp = self.rp.get(cn, {})
                if rp:
                    ps = self.fparams(self.g.funcs[cn])
                    for p, a in zip(ps, n.args):
                        if p in rp:
                            to_reader.add(id(a))
                    for k in n.keywords:
                        if k.arg in rp:
                            to_reader.add(id(k.value))
        for m in ast.walk(node):
            if isinstance(m, ast.Name) and isinstance(m.ctx, ast.Load) and id(m) not in called \
                    and id(m) not in to_reader and (fname is not None or m.id not in shadow):
                k = self.g.resolve(m.id, fname)
                if k is not None and self.psites.get(k):
                    return {'UNRESOLVED'}
        return set()

    def of_nodes(self, nodes, line, own=frozenset()):
        g = self.g
        out, helpers, loads = set(), set(), set()
        for x in nodes:
            out |= self.sites(x, line)
            helpers |= g.calls(x)
            loads |= {m.id for m in ast.walk(x)
                      if isinstance(m, ast.Name) and isinstance(m.ctx, ast.Load)}
        for h in g.reach(helpers):
            out |= self.fsites[h]
            loads |= g.globals_of[h]
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
        ds, muts = g.statements(nm, line)
        out = set()
        for st in ds + muts:
            if st in ds:
                parts = [g.value_of(st)] + g.context_of(st)
            else:
                parts = [st] + g.context_of(st)
            for x in parts:
                out |= self.sites(x, st.lineno)
                for h in g.reach(g.calls(x)):
                    out |= self.fsites[h]
                    for gl in g.globals_of[h]:
                        out |= self.name(gl, st.lineno, depth + 1, seen)
                for m in ast.walk(x):
                    if isinstance(m, ast.Name) and isinstance(m.ctx, ast.Load):
                        if m.id != nm:
                            out |= self.name(m.id, st.lineno, depth + 1, seen)
                        elif st in ds:          # x = f(x): the value before this definition
                            out |= self.name(nm, st.lineno - 1, depth + 1, seen)
        self.memo[key] = out
        return out


# ---------------------------------------------------------------------------------------------
# the rules
# ---------------------------------------------------------------------------------------------
STRUCTURAL = (re.compile(r'ok_[a-z0-9]+ = True'),
              re.compile(r'_[a-z0-9]+_bad = sorted\(.*'),
              re.compile(r'_[a-z0-9]+_bad = \[name for .*'),
              re.compile(r'_[a-z0-9]+_bad = \[k for k, v in _[a-z0-9]+_checks\.items\(\) '
                         r'if not v\]'),
              re.compile(r'_[a-z0-9]+_checks = \{\}'),
              re.compile(r'_[a-z0-9]+_bad = \[\]'))


REASONS = {
    'bookkeeping': 'accumulator bookkeeping',
    'archive-regression': 'a synthetic regression of archive-mode chronology',
    'history': 'executes a git subprocess, a host-environment read, a seal-state read or a '
               'filesystem read of verification/seals/ (the kinds are listed with the row)',
    'records': 'every file it reads is a legacy record',
    'adjudicated': 'read by hand; the adjudication is listed with the row',
    'machinery': 'tests the retired machinery its infrastructure round installed',
    'unresolved': 'a read site does not resolve statically',
    'computation': 'reads no file: an exact computation over constants',
    'live': 'reads a file outside the legacy records',
}


def classify(chk, text, hist, reads, pop):
    """(class, reason code) for one predicate."""
    if any(r.fullmatch(text) for r in STRUCTURAL):
        return 'structural', 'bookkeeping'
    if chk in WHOLE:
        return 'retire-whole', 'archive-regression'
    if hist:
        return 'retire-history', 'history'
    if (chk, text) in ADJUDICATED:
        return 'redundant', 'adjudicated'
    if reads and 'UNRESOLVED' not in reads and all(covered(p, pop) for p in reads):
        return 'redundant', 'records'
    if chk in MACHINERY:
        return 'retire-machinery', 'machinery'
    if 'UNRESOLVED' in reads:
        return 'retain', 'unresolved'
    if not reads:
        return 'retain', 'computation'
    return 'retain', 'live'


SELF_TEST_GUARD = r"""
import os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
_REC = 'programmes/p/round-a/'
_LIVE = os.path.join(os.path.dirname(os.path.dirname(HERE)), 'papers', 'Main.md')


def _bb_read(path):
    return open(_artifact(path), 'rb').read()


def _git(*args):
    return subprocess.run(('git',) + args, capture_output=True, text=True)


def _pin(read=_bb_read):
    return read(_REC + 'preregistration.md') == b''


def _live(path):
    return open(path).read()


def _probe():
    return subprocess.run(('python3', 'probe.py'), capture_output=True).returncode == 0


def _chk_live(t=None):
    return 'x' in (_live(_LIVE) if t is None else t)


def _outer():
    def _vx():
        return _git('x')
    return _vx


def _rebind(read=None):
    read = open if read is None else read
    return read(_LIVE).read()


ok_far = True
ok_far &= _bb_read(_REC + 'result.md') != b''
ok_a = True
ok_a &= _pin()
ok_a &= not _pin(lambda p: _bb_read(p) + b'x')
ok_a &= 'x' in _live(_LIVE)
ok_a &= _git('rev-parse', 'HEAD').returncode == 0
ok_a &= 2 + 2 == 4
if _git('status').returncode:
    ok_a = False
_T = {}
for _p in (_REC + 'result.md', _REC + 'preregistration.md'):
    _T[_p] = _bb_read(_p)
ok_a &= all(_T.values())
_U = {}
_U['k'] = _live(_LIVE)
ok_a &= bool(_U)
_V = {}
_V['h'] = _git('log').stdout
ok_a &= bool(_V)
ok_a &= all(open(q).read() for q in [_LIVE])
ok_a &= 'CI' in os.environ
ok_a &= _probe() and _bb_read(_REC + 'result.md') != b''
try:
    with open(_LIVE) as _fh:
        _S = _fh.read()
except OSError:
    _S = ''
ok_a &= 'x' in _S and _bb_read(_REC + 'result.md') != b''
try:
    _H = _git('log').stdout
except OSError:
    _H = ''
ok_a &= bool(_H)
for _pred in (_chk_live,):
    ok_a &= _pred() and _bb_read(_REC + 'result.md') != b''
_vx = 'a'
ok_a &= _vx == 'a' and _bb_read(_REC + 'result.md') != b''
ok_a &= 'x' in _rebind() and _bb_read(_REC + 'result.md') != b''
check('T-A', ok_a, 'message')

_t_checks = {}
_t_checks['rec'] = _bb_read(_REC + 'result.md') != b''
_t_checks['seal'] = os.path.isdir(os.path.join(os.path.dirname(HERE), 'seals'))
_t_bad = [k for k, v in _t_checks.items() if not v]
check('T-B', not _t_bad, 'message')

ok_c = True
ok_c &= 1 < 2
check('T-C', ok_c, 'message')
check('T-D', ok_far, 'message')

_e_bad = []
if not _bb_read(_REC + 'result.md'):
    _e_bad.append('record')
check('T-E', not _e_bad, 'message')
"""
# (predicate text, expected class): the self-test's table of verdicts
SELF_TEST_EXPECT = [
    ('ok_a = True', 'structural'),
    ('ok_a &= _pin()', 'redundant'),
    ("ok_a &= not _pin(lambda p: _bb_read(p) + b'x')", 'retain'),
    ("ok_a &= 'x' in _live(_LIVE)", 'retain'),
    ("ok_a &= _git('rev-parse', 'HEAD').returncode == 0", 'retire-history'),
    ('ok_a &= 2 + 2 == 4', 'retain'),
    ('ok_a = False', 'retire-history'),
    ('ok_a &= all(_T.values())', 'redundant'),
    ('ok_a &= bool(_U)', 'retain'),
    ('ok_a &= bool(_V)', 'retire-history'),
    ('ok_a &= all((open(q).read() for q in [_LIVE]))', 'retain'),
    ("ok_a &= 'CI' in os.environ", 'retire-history'),
    ("ok_a &= _probe() and _bb_read(_REC + 'result.md') != b''", 'retain'),
    ("ok_a &= 'x' in _S and _bb_read(_REC + 'result.md') != b''", 'retain'),
    ('ok_a &= bool(_H)', 'retire-history'),
    ("ok_a &= _pred() and _bb_read(_REC + 'result.md') != b''", 'retain'),
    ("ok_a &= _vx == 'a' and _bb_read(_REC + 'result.md') != b''", 'redundant'),
    ("ok_a &= 'x' in _rebind() and _bb_read(_REC + 'result.md') != b''", 'retain'),
    ('_t_checks = {}', 'structural'),
    ("_t_checks['rec'] = _bb_read(_REC + 'result.md') != b''", 'redundant'),
    ("_t_checks['seal'] = os.path.isdir(os.path.join(os.path.dirname(HERE), 'seals'))",
     'retire-history'),
    ('_t_bad = [k for k, v in _t_checks.items() if not v]', 'structural'),
    ('ok_c = True', 'structural'),
    ('ok_c &= 1 < 2', 'retain'),
    ('ok_far = True', 'structural'),
    ("ok_far &= _bb_read(_REC + 'result.md') != b''", 'redundant'),
    ('_e_bad = []', 'structural'),
    ("_e_bad.append('record')", 'redundant'),
]


def self_test():
    """The rules and the resolver on a synthetic guard: a record pin through an injectable reader,
    its drift control (which the resolver leaves open), a live read through a wrapper, git in a
    helper and in an enclosing if, a table filled in a loop over records, tables filled from a
    live file and from git, a comprehension variable, the host environment, a check table, a
    seals-directory probe, a child process, values assigned in both arms of a try, a function
    called through a loop variable, a variable named like a nested function, a reader rebound
    inside a helper, an append to a check
    list under a test that reads a record, and an accumulator written far above its check, beyond
    the other checks."""
    root = '/r'
    g = Guard(SELF_TEST_GUARD.replace('__file__', repr(root + '/' + GUARD)), {}, root)
    g.abs_file = root + '/' + GUARD
    pop = {'closed': ['verification/programmes/p/round-a'], 'individual': [], 'records': {},
           'rounds': []}
    hist, reads = History(g), Reads(g)
    got = []
    for chk in checks_of(g):
        for n in predicates_of(g, chk):
            own = g.own_targets(n)
            ctx = g.context_of(n)
            r = sorted(reads.of_nodes([n] + ctx, n.lineno, own))
            h = hist.of_nodes([n] + ctx, n.lineno, own)
            got.append((g.text(n), classify(chk['check'], g.text(n), h, r, pop)[0]))
    want = [(ast.unparse(ast.parse(t)), c) for t, c in SELF_TEST_EXPECT]
    ok = got == want
    for (t, c), (t2, c2) in zip(got, want):
        if (t, c) != (t2, c2):
            print('SELF-TEST  %s  got %s, want %s  %s'
                  % ('MISMATCH' if t == t2 else 'ORDER', c, c2, t))
    if len(got) != len(want):
        print('SELF-TEST  %d predicates, want %d' % (len(got), len(want)))
    print('SELF-TEST  %d predicates, %s' % (len(got), 'all as expected' if ok else 'FAILED'))
    return ok


def main():
    if sys.argv[1:] == ['--self-test']:
        sys.exit(0 if self_test() else 1)
    repo, commit, outdir = sys.argv[1:4]
    root = os.path.realpath(repo)
    commit = git(repo, 'rev-parse', '--verify', commit + '^{commit}').decode().strip()
    files = tree(repo, commit)
    pop = population(repo, commit, files)
    migrated = {k: v['to'] for k, v in json.loads(show(repo, commit, MIGRATION))['entries'].items()}
    g = Guard(show(repo, commit, GUARD).decode('utf-8'), migrated, root)
    hist, reads = History(g), Reads(g)
    lookup = {MIGRATION}            # read only to locate an artifact, never a protected read
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
            kind = 'augassign' if isinstance(n, ast.AugAssign) else \
                'assign' if isinstance(n, ast.Assign) else 'append'
            rows.append({'check': chk['check'], 'line': n.lineno, 'kind': kind, 'class': c,
                         'reason': why,
                         'history': sorted(h), 'reads': r,
                         'text_sha256': hashlib.sha256(text.encode('utf-8')).hexdigest()[:16],
                         'text': text})
        live = cls['retain']
        pred = sum(v for k, v in cls.items() if k != 'structural')
        checks.append({'check': chk['check'], 'line': chk['line'], 'predicates': pred,
                       'classes': dict(sorted(cls.items())),
                       'disposition': 'computed' if pred == 0 else 'retained whole' if live == pred
                       else 'removed whole' if live == 0 else 'split'})
    writes, late = completeness(g)
    if late:
        raise SystemExit('census: accumulator writes after their check: %s' % late)
    assigned = sum(1 for r in rows if r['kind'] in ('assign', 'augassign'))
    if assigned != writes:
        raise SystemExit('census: %d accumulator writes, %d counted' % (writes, assigned))
    used = {(r['check'], r['text']) for r in rows if r['reason'] == 'adjudicated'}
    if used != set(ADJUDICATED):
        raise SystemExit('census: adjudications naming no predicate: %s'
                         % sorted(set(ADJUDICATED) - used))
    totals = collections.Counter(r['class'] for r in rows)
    files_read = sorted({p for r in rows for p in r['reads']})
    index = {p: i for i, p in enumerate(files_read)}
    adjud = sorted({ADJUDICATED[(r['check'], r['text'])] for r in rows
                    if r['reason'] == 'adjudicated'})
    table = []
    for r in rows:
        row = [r['check'], r['line'], r['class'], r['reason'], r['history'],
               [index[p] for p in r['reads']], r['text_sha256']]
        if r['reason'] == 'adjudicated':
            row.append(adjud.index(ADJUDICATED[(r['check'], r['text'])]))
        table.append(row)
    head = {
        'schema': 'v3-12-census', 'version': 1, 'commit': commit,
        'guard': {'path': GUARD, 'blob': files[GUARD][1],
                  'totals': dict(sorted(totals.items())),
                  'dispositions': dict(sorted(collections.Counter(
                      c['disposition'] for c in checks).items())),
                  'accumulator_writes': writes},
        'legacy_records': {'closed_namespaces': len(pop['closed']),
                           'legacy_round_directories': len(pop['rounds']),
                           'individual_pins': pop['individual'], 'records': len(pop['records']),
                           'v2_pins_agreeing': pop['v2_pins'],
                           'not_records': list(NOT_RECORDS)},
        'reasons': REASONS,
        'adjudications': adjud,
        'row_format': ['check', 'line at the commit', 'class', 'reason', 'history kinds executed',
                       'files read, as indices into files_read',
                       'first 16 hex digits of the SHA-256 of the statement\'s unparsed text',
                       'adjudication index, when adjudicated'],
        'files_read': files_read,
        'checks': checks,
    }
    manifest = {'schema': 'oi-legacy-records', 'version': 1,
                'closed_namespaces': pop['closed'], 'records': pop['records']}
    os.makedirs(outdir, exist_ok=True)
    body = json.dumps(head, indent=1, ensure_ascii=False)
    lines = ['  ' + json.dumps(t, ensure_ascii=False, separators=(', ', ': ')) for t in table]
    body = body[:-2] + ',\n "predicates": [\n' + ',\n'.join(lines) + '\n ]\n}\n'
    json.loads(body)
    with open(os.path.join(outdir, 'census.json'), 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(body)
    path = os.path.join(outdir, 'legacy-records.json')
    with open(path, 'w', encoding='utf-8', newline='\n') as fh:
        json.dump(manifest, fh, indent=1, ensure_ascii=False)
        fh.write('\n')
    print('census  %s' % commit)
    print('guard   %d checks, %d predicates: %s'
          % (len(checks), len(rows), dict(sorted(totals.items()))))
    print('checks  %s' % head['guard']['dispositions'])
    print('records %d in %d closed namespaces (%d legacy round directories) and %d individual pins'
          % (len(pop['records']), len(pop['closed']), len(pop['rounds']), len(pop['individual'])))


if __name__ == '__main__':
    main()
