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


def evs(node, line, env=None, depth=0):
    """Every value a string/path expression can take under module constants, env and literal
    loop iterables; raise U when it cannot be evaluated."""
    env = env or {}
    if depth > 20:
        raise U()
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return [node.value]
    if isinstance(node, ast.Name):
        if node.id in env:
            v = env[node.id]
            return list(v) if isinstance(v, list) else [v]
        if node.id == '__file__':
            return [ABS_FILE]
        d = latest(node.id, line)
        if isinstance(d, ast.Assign) and len(d.targets) == 1 and isinstance(d.targets[0], ast.Name):
            return evs(d.value, d.lineno - 1, None, depth + 1)
        if isinstance(d, ast.For) and isinstance(d.target, ast.Name) and \
                isinstance(d.iter, (ast.Tuple, ast.List)):
            out = []
            for e in d.iter.elts:
                out += evs(e, d.lineno - 1, None, depth + 1)
            return out
        raise U()
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        return [x + y for x in evs(node.left, line, env, depth + 1)
                for y in evs(node.right, line, env, depth + 1)]
    if isinstance(node, ast.JoinedStr):
        outs = ['']
        for v in node.values:
            vals = [v.value] if isinstance(v, ast.Constant) else evs(v.value, line, env, depth + 1)
            outs = [o + x for o in outs for x in vals]
        return outs
    if isinstance(node, ast.FormattedValue):
        return evs(node.value, line, env, depth + 1)
    if isinstance(node, ast.Call):
        dotted = ast.unparse(node.func)
        args = node.args
        if dotted == 'os.path.join':
            outs = [()]
            for a in args:
                outs = [o + (x,) for o in outs for x in evs(a, line, env, depth + 1)]
            return [os.path.join(*o) for o in outs]
        if dotted == 'os.path.dirname':
            return [os.path.dirname(x) for x in evs(args[0], line, env, depth + 1)]
        if dotted in ('os.path.abspath', 'os.path.normpath', 'os.path.realpath'):
            return [os.path.normpath(os.path.abspath(x)) for x in evs(args[0], line, env, depth + 1)]
        if dotted == '_artifact':
            return [os.path.join(REPO, 'verification', *MIGRATED.get(x, x).split('/'))
                    for x in evs(args[0], line, env, depth + 1)]
    raise U()


def ev(node, line, env=None, depth=0):
    vals = evs(node, line, env, depth)
    if len(vals) != 1:
        raise U()
    return vals[0]


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
    """The repository-relative paths one primitive read reads, or {'UNRESOLVED'}. A name bound
    locally (shadow) and not bound in env never resolves to a module value."""
    if {m.id for m in ast.walk(arg) if isinstance(m, ast.Name)} & (set(shadow) - set(env)):
        return {'UNRESOLVED'}
    try:
        vals = evs(arg, line, env)
    except (U, TypeError, IndexError, AttributeError):
        return {'UNRESOLVED'}
    out = set()
    for v in vals:
        if not isinstance(v, str):
            return {'UNRESOLVED'}
        if name in ('_bb_read', '_bb_blob', '_artifact'):
            p = os.path.join(REPO, 'verification', *MIGRATED.get(v, v).split('/'))
        elif name == '_a11p_root':
            p = os.path.join(REPO, v)
        else:
            p = v
        p = os.path.normpath(p)
        if not p.startswith(REPO + os.sep):
            return {'UNRESOLVED'}
        out.add(os.path.relpath(p, REPO))
    return out


LOCALS_ALL = None


def fparams(f):
    a = f.args
    return [x.arg for x in a.args + a.kwonlyargs]


def uses(node, names):
    return bool({m.id for m in ast.walk(node) if isinstance(m, ast.Name)} & set(names))


BASEPRIM = ('_bb_read', '_bb_blob', '_a11p_root', '_artifact')


def reader_params(f):
    """Parameters whose default is a reader: a call of such a parameter reads its first argument
    as that default would."""
    a = f.args
    pos = a.args[len(a.args) - len(a.defaults):] if a.defaults else []
    out = {}
    for p, dflt in list(zip(pos, a.defaults)) + [(k, d) for k, d in zip(a.kwonlyargs, a.kw_defaults) if d]:
        dn = ast.unparse(dflt)
        if dn in PRIMS or dn in BASEPRIM or dn in FUNCS:
            out[p.arg] = dn
    return out


RP = {k: reader_params(v) for k, v in FUNCS.items()}
LOCALS_ALL = {k: bound_in(v) for k, v in FUNCS.items()}


def callee(n, fname):
    """The reading function a call names: a primitive, a wrapper, or the default of a reader
    parameter of the enclosing function fname."""
    cn = ast.unparse(n.func)
    if fname and cn in RP.get(fname, {}):
        return RP[fname][cn]
    return cn


def is_prim(cn):
    return cn in PRIMS or cn in BASEPRIM


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
            cn = callee(n, name)
            if is_prim(cn):
                if uses(n.args[0], ps):
                    cur.append(n)
            elif cn in PSITES and PSITES[cn] and any(uses(a, ps) for a in n.args + [k.value for k in n.keywords]):
                cur.append(n)
        if len(cur) != len(PSITES.get(name, [])):
            PSITES[name] = cur
            changed = True


def call_reads(n, line, env, depth=0, shadow=frozenset(), fname=None):
    """The paths a call reads through its parameter-dependent sites, under env."""
    cn = callee(n, fname)
    if is_prim(cn):
        return prim_path(cn, n.args[0], line, env, shadow)
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
            bind[p] = evs(a, line, env)
        except (U, TypeError, IndexError, AttributeError):
            pass
    for k in n.keywords:
        if k.arg in ps:
            try:
                bind[k.arg] = evs(k.value, line, env)
            except (U, TypeError, IndexError, AttributeError):
                pass
    out = set()
    for inner in PSITES[cn]:
        out |= call_reads(inner, line, bind, depth + 1, LOCALS_ALL[cn] - set(bind), cn)
    return out


def sites(node, line, helper_params=(), shadow=None, fname=None):
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
        cn = callee(n, fname)
        if is_prim(cn):
            if helper_params and uses(n.args[0], helper_params):
                continue            # the path is the helper's own parameter: resolved at its call site
            out |= call_reads(n, line, {}, 0, shadow, fname)
        elif cn in PSITES and PSITES[cn]:
            args = n.args + [k.value for k in n.keywords]
            if helper_params and any(uses(a, helper_params) for a in args):
                continue
            out |= call_reads(n, line, {}, 0, shadow, fname)
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
    FSITES[name] = sites(f, f.lineno, fparams(f), LOCALS_ALL[name], name)


PARENT = {}
for _p in ast.walk(T):
    for _c in ast.iter_child_nodes(_p):
        PARENT[_c] = _p


def context_of(n):
    out = []
    a = PARENT.get(n)
    while a is not None and not isinstance(a, ast.Module):
        if isinstance(a, (ast.If, ast.While, ast.IfExp)):
            out.append(a.test)
        elif isinstance(a, ast.For):
            out.append(a.iter)
        elif isinstance(a, ast.With):
            out.extend(i.context_expr for i in a.items)
        a = PARENT.get(a)
    return out




def _root_name(t):
    while isinstance(t, (ast.Subscript, ast.Attribute)):
        t = t.value
    return t.id if isinstance(t, ast.Name) else None


def own_targets(n):
    if isinstance(n, ast.Assign):
        return {_root_name(t) for t in n.targets if isinstance(t, (ast.Subscript, ast.Attribute))} - {None}
    if isinstance(n, ast.AugAssign):
        return {_root_name(n.target)} - {None}
    if isinstance(n, ast.Expr) and isinstance(n.value, ast.Call) and isinstance(n.value.func, ast.Attribute):
        return {_root_name(n.value.func.value)} - {None}
    return set()


MUTS = {}
for n in ast.walk(T):
    if getattr(n, 'lineno', None) is None or n.lineno in FUNC_LINES:
        continue
    tgt = None
    if isinstance(n, ast.Assign):
        for t in n.targets:
            if isinstance(t, (ast.Subscript, ast.Attribute)):
                tgt = _root_name(t)
    elif isinstance(n, ast.AugAssign):
        tgt = _root_name(n.target)
    elif isinstance(n, ast.Expr) and isinstance(n.value, ast.Call) and \
            isinstance(n.value.func, ast.Attribute) and n.value.func.attr in (
                'append', 'extend', 'update', 'add', 'setdefault', 'insert', '__setitem__'):
        tgt = _root_name(n.value.func.value)
    if tgt:
        MUTS.setdefault(tgt, []).append(n)


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
    # the statements that mutate the value in place, and the headers that decide whether they and
    # the definition run
    stmts = ([d] if d is not None else []) + [m for m in MUTS.get(name, []) if (d.lineno if d is not None else 0) <= m.lineno < line]
    for st in stmts:
        parts = context_of(st) + ([st] if st is not d else [])
        for x in parts:
            out |= sites(x, st.lineno)
            for h in reach(calls(x)):
                out |= FSITES[h]
                for m in ast.walk(FUNCS[h]):
                    if isinstance(m, ast.Name) and isinstance(m.ctx, ast.Load) and m.id in DEFS \
                            and m.id not in LOCALS[h]:
                        out |= name_reads(m.id, st.lineno, depth + 1, seen)
            for m in ast.walk(x):
                if isinstance(m, ast.Name) and isinstance(m.ctx, ast.Load) and m.id != name:
                    out |= name_reads(m.id, st.lineno, depth + 1, seen)
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
        ctx = context_of(node)
        out = sites(node, line)
        for x in ctx:
            out |= sites(x, line)
        hs = reach(calls(node).union(*[calls(x) for x in ctx]))
        for h in hs:
            out |= FSITES[h]
            for m in ast.walk(FUNCS[h]):
                if isinstance(m, ast.Name) and isinstance(m.ctx, ast.Load) and m.id in DEFS and m.id not in LOCALS[h]:
                    out |= name_reads(m.id, line)
        own = own_targets(node)
        for x in [node] + ctx:
            for m in ast.walk(x):
                if isinstance(m, ast.Name) and isinstance(m.ctx, ast.Load) and m.id not in own:
                    out |= name_reads(m.id, line)
        res['%s %d' % (c['check'], line)] = sorted(out)
json.dump(res, open(sys.argv[3], 'w'), indent=0)
n_un = sum(1 for v in res.values() if 'UNRESOLVED' in v)
print('%d predicates; %d with an unresolved read site; %d reading no file' %
      (len(res), n_un, sum(1 for v in res.values() if not v)))
