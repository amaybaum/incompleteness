#!/usr/bin/env python3
"""Scratch: resolve, statically, the files every guard predicate reads. Never landed.

Usage: resolve312.py <guard.py> <guard.json> <out reads.json>

A read site is a call of open, _bb_read, _bb_blob, _a11p_root, _artifact, os.listdir, os.path.exists,
os.path.isdir, glob.glob or os.path.getsize whose path argument evaluates, under the module's
constants, to a repository path. A site whose argument does not evaluate is UNRESOLVED; a predicate
with an unresolved site is never called redundant."""
import ast
import bisect
import json
import os
import sys

GUARD = sys.argv[1]
REPO = os.path.abspath(os.path.join(os.path.dirname(GUARD), '..', '..'))
SRC = open(GUARD, encoding='utf-8').read()
LINES = SRC.split('\n')
T = ast.parse(SRC)
FUNCS = {n.name: n for n in ast.walk(T) if isinstance(n, ast.FunctionDef)}
FUNC_LINES = set()
for f in FUNCS.values():
    FUNC_LINES.update(range(f.lineno, f.end_lineno + 1))
MIGRATED = {k: v['to'] for k, v in json.load(open(os.path.join(REPO, 'verification',
                                                               'migration-manifest.json')))['entries'].items()}
ABS_FILE = os.path.join(REPO, 'verification', 'lean', 'edge_rigidity_probe.py')


def names_of(t):
    if isinstance(t, ast.Name):
        yield t
    elif isinstance(t, (ast.Tuple, ast.List)):
        for e in t.elts:
            yield from names_of(e)


DEFS = {}
for n in ast.walk(T):
    if isinstance(n, (ast.Assign, ast.AnnAssign)) and n.lineno not in FUNC_LINES:
        tg = n.targets if isinstance(n, ast.Assign) else [n.target]
        for t in tg:
            for m in names_of(t):
                DEFS.setdefault(m.id, []).append(n)
    if isinstance(n, (ast.For, ast.With)) and n.lineno not in FUNC_LINES:
        tg = [n.target] if isinstance(n, ast.For) else [i.optional_vars for i in n.items if i.optional_vars]
        for t in tg:
            for m in names_of(t):
                DEFS.setdefault(m.id, []).append(n)
for k in DEFS:
    DEFS[k].sort(key=lambda d: d.lineno)


def latest(name, line):
    ds = DEFS.get(name, [])
    i = bisect.bisect_right([d.lineno for d in ds], line) - 1
    return ds[i] if i >= 0 else None


class U(Exception):
    pass


def ev(node, line, env=None, depth=0):
    """Evaluate a string/path expression under module constants; raise U when it does not."""
    env = env or {}
    if depth > 20:
        raise U()
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.Name):
        if node.id in env:
            return env[node.id]
        if node.id == '__file__':
            return ABS_FILE
        d = latest(node.id, line)
        if d is None or not isinstance(d, ast.Assign) or len(d.targets) != 1 or \
                not isinstance(d.targets[0], ast.Name):
            raise U()
        return ev(d.value, d.lineno - 1, None, depth + 1)
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        return ev(node.left, line, env, depth + 1) + ev(node.right, line, env, depth + 1)
    if isinstance(node, ast.JoinedStr):
        out = ''
        for v in node.values:
            out += v.value if isinstance(v, ast.Constant) else ev(v.value, line, env, depth + 1)
        return out
    if isinstance(node, ast.FormattedValue):
        return ev(node.value, line, env, depth + 1)
    if isinstance(node, ast.Call):
        f = node.func
        dotted = ast.unparse(f)
        args = node.args
        if dotted in ('os.path.join',):
            return os.path.join(*[ev(a, line, env, depth + 1) for a in args])
        if dotted in ('os.path.dirname',):
            return os.path.dirname(ev(args[0], line, env, depth + 1))
        if dotted in ('os.path.abspath', 'os.path.normpath', 'os.path.realpath'):
            return os.path.normpath(os.path.abspath(ev(args[0], line, env, depth + 1)))
        if dotted == '_artifact':
            name = ev(args[0], line, env, depth + 1)
            return os.path.join(REPO, 'verification', *MIGRATED.get(name, name).split('/'))
        if isinstance(f, ast.Attribute) and f.attr in ('join',) and isinstance(f.value, ast.Constant):
            raise U()
    raise U()


PRIMS = {'open': 0, '_bb_read': 0, '_bb_blob': 0, '_a11p_root': 0, 'os.listdir': 0,
         'os.path.exists': 0, 'os.path.isdir': 0, 'os.path.isfile': 0, 'glob.glob': 0,
         'os.path.getsize': 0, 'listdir': 0}


OPAQUE = ('subprocess.run', 'exec', 'eval', 'subprocess.check_output', 'subprocess.Popen')


def bound_in(node):
    """Names bound inside node other than at module level: comprehension targets, lambda and
    function parameters, and every name a function body stores."""
    out = set()
    for n in ast.walk(node):
        if isinstance(n, ast.comprehension):
            out |= {m.id for m in ast.walk(n.target) if isinstance(m, ast.Name)}
        elif isinstance(n, (ast.Lambda, ast.FunctionDef)):
            out |= {a.arg for a in n.args.args + n.args.kwonlyargs}
            if isinstance(n, ast.FunctionDef):
                out |= {m.id for m in ast.walk(n) if isinstance(m, ast.Name) and isinstance(m.ctx, ast.Store)}
    return out


def prim_path(name, arg, line, env, shadow=frozenset()):
    """The repository-relative path one primitive read reads, or 'UNRESOLVED'. A name bound
    locally (shadow) and not bound in env never resolves to a module value."""
    if {m.id for m in ast.walk(arg) if isinstance(m, ast.Name)} & (set(shadow) - set(env)):
        return 'UNRESOLVED'
    try:
        if name in ('_bb_read', '_bb_blob', '_artifact'):
            p = os.path.join(REPO, 'verification', *MIGRATED.get(ev(arg, line, env), ev(arg, line, env)).split('/'))
        elif name == '_a11p_root':
            p = os.path.join(REPO, ev(arg, line, env))
        else:
            p = ev(arg, line, env)
    except (U, TypeError, IndexError, AttributeError):
        return 'UNRESOLVED'
    p = os.path.normpath(p)
    if not p.startswith(REPO + os.sep):
        return 'UNRESOLVED'
    return os.path.relpath(p, REPO)


def fparams(f):
    a = f.args
    return [x.arg for x in a.args + a.kwonlyargs]


def uses(node, names):
    return bool({m.id for m in ast.walk(node) if isinstance(m, ast.Name)} & set(names))


LOCALS_ALL = {k: bound_in(v) for k, v in FUNCS.items()}
BASEPRIM = ('_bb_read', '_bb_blob', '_a11p_root', '_artifact')
# PSITES[f]: the calls inside f whose path argument depends on f's own parameters
PSITES = {}
changed = True
while changed:
    changed = False
    for name, f in FUNCS.items():
        if name in BASEPRIM:
            continue
        ps = fparams(f)
        cur = []
        for n in ast.walk(f):
            if not (isinstance(n, ast.Call) and n.args):
                continue
            cn = ast.unparse(n.func)
            if cn in PRIMS or cn in BASEPRIM:
                if uses(n.args[0], ps):
                    cur.append(n)
            elif cn in PSITES and PSITES[cn] and any(uses(a, ps) for a in n.args + [k.value for k in n.keywords]):
                cur.append(n)
        if len(cur) != len(PSITES.get(name, [])):
            PSITES[name] = cur
            changed = True


def call_reads(n, line, env, depth=0, shadow=frozenset()):
    """The paths a call reads through its parameter-dependent sites, under env."""
    cn = ast.unparse(n.func)
    if cn in PRIMS or cn in BASEPRIM:
        return {prim_path(cn, n.args[0], line, env, shadow)}
    if {m.id for a in n.args + [k.value for k in n.keywords] for m in ast.walk(a)
            if isinstance(m, ast.Name)} & (set(shadow) - set(env)):
        return {'UNRESOLVED'}
    f = FUNCS[cn]
    if depth > 12:
        return {'UNRESOLVED'}
    ps = fparams(f)
    bind = {}
    for p, a in zip(ps, n.args):
        try:
            bind[p] = ev(a, line, env)
        except (U, TypeError, IndexError, AttributeError):
            pass
    for k in n.keywords:
        if k.arg in ps:
            try:
                bind[k.arg] = ev(k.value, line, env)
            except (U, TypeError, IndexError, AttributeError):
                pass
    out = set()
    for inner in PSITES[cn]:
        out |= call_reads(inner, line, bind, depth + 1, LOCALS_ALL[cn])
    return out


def sites(node, line, helper_params=(), shadow=None):
    out = set()
    shadow = bound_in(node) if shadow is None else shadow
    for n in ast.walk(node):
        if not isinstance(n, ast.Call):
            continue
        name = ast.unparse(n.func)
        if name in OPAQUE:
            out.add('UNRESOLVED')     # opaque: a child process or executed text reads what it reads
            continue
        if not n.args:
            continue
        if name in PRIMS or name in BASEPRIM or (name in PSITES and PSITES[name]):
            args = n.args + [k.value for k in n.keywords]
            if helper_params and any(uses(a, helper_params) for a in args):
                continue            # depends on the helper's own parameter: resolved at its call site
            out |= call_reads(n, line, {}, 0, shadow)
    return out


def calls(node):
    return {m.func.id for m in ast.walk(node) if isinstance(m, ast.Call) and isinstance(m.func, ast.Name)
            and m.func.id in FUNCS}


def reach(seed):
    seen, todo = set(), list(seed)
    while todo:
        f = todo.pop()
        if f in seen:
            continue
        seen.add(f)
        todo += list(calls(FUNCS[f]))
    return seen


FSITES = {}
for name, f in FUNCS.items():
    if name in BASEPRIM:
        FSITES[name] = set()
        continue
    FSITES[name] = sites(f, f.lineno, fparams(f), LOCALS_ALL[name])


def locals_of(f):
    loc = set(fparams(f))
    for n in ast.walk(f):
        if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Store):
            loc.add(n.id)
    return loc


LOCALS = {k: locals_of(v) for k, v in FUNCS.items()}
MEMO = {}


def name_reads(name, line, depth=0, seen=None):
    key = (name, line)
    if key in MEMO:
        return MEMO[key]
    seen = seen if seen is not None else set()
    if key in seen or depth > 10:
        return set()
    seen.add(key)
    d = latest(name, line)
    out = set()
    if d is not None:
        root = d.value if isinstance(d, (ast.Assign, ast.AnnAssign)) else (d.iter if isinstance(d, ast.For) else d)
        out |= sites(d if isinstance(d, ast.With) else root, d.lineno)
        hs = reach(calls(root))
        for h in hs:
            out |= FSITES[h]
            for m in ast.walk(FUNCS[h]):
                if isinstance(m, ast.Name) and isinstance(m.ctx, ast.Load) and m.id in DEFS \
                        and m.id not in LOCALS[h]:
                    out |= name_reads(m.id, d.lineno, depth + 1, seen)
        for m in ast.walk(root):
            if isinstance(m, ast.Name) and isinstance(m.ctx, ast.Load) and m.id != name:
                out |= name_reads(m.id, d.lineno, depth + 1, seen)
    MEMO[key] = out
    return out


guard = json.load(open(sys.argv[2]))
res = {}
for c in guard:
    for p in c['predicates']:
        line = p['line']
        node = None
        for n in ast.walk(T):
            if getattr(n, 'lineno', None) == line and isinstance(n, (ast.AugAssign, ast.Assign, ast.Expr)):
                node = n
                break
        if node is None:
            res['%s %d' % (c['check'], line)] = ['UNRESOLVED']
            continue
        out = sites(node, line)
        hs = reach(calls(node))
        for h in hs:
            out |= FSITES[h]
            for m in ast.walk(FUNCS[h]):
                if isinstance(m, ast.Name) and isinstance(m.ctx, ast.Load) and m.id in DEFS and m.id not in LOCALS[h]:
                    out |= name_reads(m.id, line)
        for m in ast.walk(node):
            if isinstance(m, ast.Name) and isinstance(m.ctx, ast.Load):
                out |= name_reads(m.id, line)
        res['%s %d' % (c['check'], line)] = sorted(out)
json.dump(res, open(sys.argv[3], 'w'), indent=0)
n_un = sum(1 for v in res.values() if 'UNRESOLVED' in v)
print('%d predicates; %d with an unresolved read site; %d reading no file' %
      (len(res), n_un, sum(1 for v in res.values() if not v)))
