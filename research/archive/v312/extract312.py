#!/usr/bin/env python3
"""Scratch: extract every predicate of the guard, by top-level check, with the helper functions it
reaches, and tag each with the reads it performs. Never landed.

Usage: extract312.py <guard.py> <out.json>

A predicate is any statement that can change a check's verdict: an augmented assignment to the
check's accumulator (`ok_x &= ...`, `ok_x |= ...`), a plain reassignment of it, an entry written
into a `_*_checks` dict, or an append to a `_*_bad` list. Loops and branches are descended; each
predicate records the enclosing top-level statement's line span."""
import ast
import json
import re
import sys

SRC = open(sys.argv[1], encoding='utf-8').read()
LINES = SRC.split('\n')
TREE = ast.parse(SRC)

FUNCS = {n.name: n for n in ast.walk(TREE) if isinstance(n, ast.FunctionDef)}
def seg_of(n):
    return '\n'.join(LINES[n.lineno - 1:n.end_lineno])


FSRC = {k: seg_of(v) for k, v in FUNCS.items()}


def calls(node):
    out = set()
    for n in ast.walk(node):
        if isinstance(n, ast.Call):
            f = n.func
            if isinstance(f, ast.Name) and f.id in FUNCS:
                out.add(f.id)
    return out


CALLS = {k: calls(v) for k, v in FUNCS.items()}


def locals_of(f):
    loc = {a.arg for a in f.args.args + f.args.kwonlyargs + f.args.posonlyargs}
    if f.args.vararg:
        loc.add(f.args.vararg.arg)
    if f.args.kwarg:
        loc.add(f.args.kwarg.arg)
    glob = set()
    for n in ast.walk(f):
        if isinstance(n, ast.Global):
            glob.update(n.names)
        if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Store):
            loc.add(n.id)
        if isinstance(n, (ast.FunctionDef, ast.Lambda)) and n is not f:
            if isinstance(n, ast.FunctionDef):
                loc.add(n.name)
            loc.update(a.arg for a in n.args.args)
        if isinstance(n, ast.comprehension):
            for m in ast.walk(n.target):
                if isinstance(m, ast.Name):
                    loc.add(m.id)
    return loc - glob


LOCALS = {k: locals_of(v) for k, v in FUNCS.items()}


def reach(names):
    seen, todo = set(), list(names)
    while todo:
        n = todo.pop()
        if n in seen:
            continue
        seen.add(n)
        todo += list(CALLS.get(n, ()))
    return seen


# the reads a predicate performs, by lexical evidence in its own text and its reachable helpers
TAGS = [
    # history: the verdict depends on git objects, ancestry or refs, not on the working tree
    ('git-topology', r"merge-base|is-ancestor|rev-list|--first-parent|first_parent|\bparents\b|"
                     r"_strong\(|_rbr_ensure_present|refs/remotes|refs/pull"),
    ('git-object', r"'show', '%s:|\"show\"|'show'|cat-file|ls-tree|'rev-parse', '%s:|"
                   r"_git_text\(|_git\(|subprocess\.run\(\['git'|\['git', "),
    # protocol state: seal validator verdicts, manifest modes, prospective declarations, baselines
    ('seal-state', r"_si2_authority|_si2_manifest_verdicts|_si2_validate|_si1_validate|"
                   r"_MANIFEST_PROSPECTIVE|_MANIFEST_BASELINE|_si2_integrity|_seal_field"),
    ('seal-records', r"verification/seals|'seals'|_si1_load"),
    ('host-event', r"GITHUB_|event_name|GITHUB_EVENT"),
    ('certificates', r"verification/certificates|certificate_verifier|attestations/"),
    ('workflow-or-gate', r"verify\.yml|release_gate|workflows"),
    ('lean-kernel', r"\.lean|sorry|native_decide|#print axioms|OIBridge"),
    ('manuscript', r"papers/|book/|'papers'|'book'|\.md'|_artifact\(|README|ROADMAP|"
                   r"AGENTS\.md|FULL\.md"),
    ('computation', r"numpy|np\.|Fraction|itertools|random\.|permutations|linalg"),
]


def tags_of(text):
    return sorted(t for t, rx in TAGS if re.search(rx, text))


PATHLIT = re.compile(r"['\"]([A-Za-z0-9_./{}%*-]*(?:\.md|\.lean|\.json|\.py|\.yml|/)[A-Za-z0-9_./{}%*-]*)['\"]")


def lits_of(text):
    return set(m.group(1) for m in PATHLIT.finditer(text))


checks = []  # (tag, line, accumulator expr)
for node in TREE.body:
    if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call) and \
            isinstance(node.value.func, ast.Name) and node.value.func.id == 'check':
        a = node.value.args
        if a and isinstance(a[0], ast.Constant):
            checks.append((a[0].value, node.lineno, seg_of(a[1])))

# dataflow: every module-level (non-function) assignment to a name, by name
DEFS = {}
FUNC_LINES = set()
for f in FUNCS.values():
    FUNC_LINES.update(range(f.lineno, f.end_lineno + 1))
for n in ast.walk(TREE):
    if isinstance(n, (ast.Assign, ast.AugAssign, ast.AnnAssign, ast.For, ast.With)) and n.lineno not in FUNC_LINES:
        tg = []
        if isinstance(n, ast.Assign):
            tg = n.targets
        elif isinstance(n, (ast.AugAssign, ast.AnnAssign)):
            tg = [n.target]
        elif isinstance(n, ast.For):
            tg = [n.target]
        elif isinstance(n, ast.With):
            tg = [i.optional_vars for i in n.items if i.optional_vars is not None]
        def _names(t):
            if isinstance(t, ast.Name):
                yield t
            elif isinstance(t, (ast.Tuple, ast.List)):
                for e in t.elts:
                    yield from _names(e)
            elif isinstance(t, ast.Starred):
                yield from _names(t.value)
        for t in tg:
            for m in _names(t):
                if True:
                    src = seg_of(n) if not isinstance(n, (ast.For, ast.With)) else LINES[n.lineno - 1]
                    if isinstance(n, ast.For):
                        src = LINES[n.lineno - 1] + '\n' + seg_of(n.iter)
                    DEFS.setdefault(m.id, []).append((n, src))
import bisect
for k in DEFS:
    DEFS[k].sort(key=lambda d: d[0].lineno)
DT = {}
LIT = {}


def latest_def(name, line):
    ds = DEFS.get(name, [])
    i = bisect.bisect_right([d[0].lineno for d in ds], line) - 1
    return ds[i] if i >= 0 else None


def name_tags(name, line, depth=0, seen=None):
    key = (name, line)
    if key in DT:
        return DT[key]
    seen = seen if seen is not None else set()
    if key in seen or depth > 8:
        return set()
    seen.add(key)
    d = latest_def(name, line)
    tg = set()
    if d is not None:
        n, src = d
        tg |= set(tags_of(src))
        LIT.setdefault(key, set()).update(lits_of(src))
        hs = reach(calls(n))
        htxt = '\n'.join(FSRC[h] for h in hs)
        tg |= set(tags_of(htxt))
        LIT[key].update(lits_of(htxt))
        root = n.value if isinstance(n, (ast.Assign, ast.AugAssign)) else (n.iter if isinstance(n, ast.For) else n)
        for m in ast.walk(root):
            if isinstance(m, ast.Name) and isinstance(m.ctx, ast.Load):
                sub = (m.id, n.lineno - 1 if m.id == name else n.lineno)
                tg |= name_tags(sub[0], sub[1], depth + 1, seen)
                LIT.setdefault(key, set()).update(LIT.get(sub, set()))
    DT[key] = tg
    return tg


PARENT = {}
for _p in ast.walk(TREE):
    for _c in ast.iter_child_nodes(_p):
        PARENT[_c] = _p


def context_of(n):
    """The enclosing control-flow headers that decide whether n runs: if/while tests, for
    iterables, with items, up to the module."""
    out = []
    a = PARENT.get(n)
    while a is not None and not isinstance(a, ast.Module):
        if isinstance(a, (ast.If, ast.While)):
            out.append(a.test)
        elif isinstance(a, ast.For):
            out.append(a.iter)
        elif isinstance(a, ast.With):
            out.extend(i.context_expr for i in a.items)
        elif isinstance(a, ast.IfExp):
            out.append(a.test)
        a = PARENT.get(a)
    return out




def _root_name(t):
    while isinstance(t, (ast.Subscript, ast.Attribute)):
        t = t.value
    return t.id if isinstance(t, ast.Name) else None


def own_targets(n):
    """The accumulator a predicate writes: its store target's root name, or its append receiver.
    Its other entries are other predicates, not inputs of this one."""
    if isinstance(n, ast.Assign):
        return {_root_name(t) for t in n.targets if isinstance(t, (ast.Subscript, ast.Attribute))} - {None}
    if isinstance(n, ast.AugAssign):
        return {_root_name(n.target)} - {None}
    if isinstance(n, ast.Expr) and isinstance(n.value, ast.Call) and isinstance(n.value.func, ast.Attribute):
        return {_root_name(n.value.func.value)} - {None}
    if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute):
        return {_root_name(n.func.value)} - {None}
    return set()


MUTS = {}
for n in ast.walk(TREE):
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


import importlib.util
_spec = importlib.util.spec_from_file_location('eh', __file__.replace('extract312.py', 'exec_history_lib.py'))
EH = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(EH)
FK = EH.function_kinds(TREE)
HK = {}


def name_hist(name, line, depth=0, seen=None):
    key = (name, line)
    if key in HK:
        return HK[key]
    seen = seen if seen is not None else set()
    if key in seen or depth > 8:
        return set()
    seen.add(key)
    d = latest_def(name, line)
    k = set()
    if d is not None:
        n, _src = d
        root = n.value if isinstance(n, (ast.Assign, ast.AugAssign)) else (n.iter if isinstance(n, ast.For) else n)
        k |= EH.direct_kinds(root)
        for h in reach(calls(root)):
            k |= set(FK.get(h, ()))
        for m in ast.walk(root):
            if isinstance(m, ast.Name) and isinstance(m.ctx, ast.Load):
                k |= name_hist(m.id, n.lineno - 1 if m.id == name else n.lineno, depth + 1, seen)
    # in-place mutations before the use, and the headers that decide the definition and them
    stmts = ([d[0]] if d is not None else []) + [m for m in MUTS.get(name, []) if (d[0].lineno if d is not None else 0) <= m.lineno < line]
    for st in stmts:
        for x in context_of(st) + ([st] if d is None or st is not d[0] else []):
            k |= EH.direct_kinds(x)
            for h in reach(calls(x)):
                k |= set(FK.get(h, ()))
            for m in ast.walk(x):
                if isinstance(m, ast.Name) and isinstance(m.ctx, ast.Load) and m.id != name:
                    k |= name_hist(m.id, st.lineno, depth + 1, seen)
    HK[key] = k
    return k


HT = {}
out = []
prev_end = 0
body = TREE.body
for tag, line, acc in checks:
    names = set(re.findall(r'[A-Za-z_][A-Za-z0-9_]*', acc))
    base = sorted(n for n in names if n not in ('not', 'and', 'or', 'True', 'False'))
    preds = []
    for node in body:
        if not (prev_end < node.lineno < line):
            continue
        for n in ast.walk(node):
            kind = None
            if isinstance(n, ast.AugAssign) and isinstance(n.target, ast.Name) and n.target.id in names:
                kind = 'accumulate'
            elif isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id in names
                                                   for t in n.targets):
                kind = 'assign'
            elif isinstance(n, ast.Assign) and any(isinstance(t, ast.Subscript) and
                                                   isinstance(t.value, ast.Name) and
                                                   t.value.id.endswith('_checks')
                                                   for t in n.targets):
                kind = 'checks-entry'
            elif isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and \
                    n.func.attr == 'append' and isinstance(n.func.value, ast.Name) and \
                    (n.func.value.id in names or n.func.value.id.endswith('_bad')):
                kind = 'bad-append'
            if kind is None:
                continue
            seg = seg_of(n)
            ctx = context_of(n)
            helpers = reach(calls(n) | set().union(*[calls(x) for x in ctx]) if ctx else calls(n))
            key = frozenset(helpers)
            if key not in HT:
                HT[key] = tags_of('\n'.join(FSRC[h] for h in helpers))
            flow = set()
            lits = set(lits_of(seg)) | set(lits_of('\n'.join(FSRC[h] for h in helpers)))
            gnames = set()
            own = own_targets(n)
            for x in [n] + ctx:
                for m in ast.walk(x):
                    if isinstance(m, ast.Name) and isinstance(m.ctx, ast.Load) and m.id not in names \
                            and m.id not in own:
                        gnames.add(m.id)
            for h in helpers:
                for m in ast.walk(FUNCS[h]):
                    if isinstance(m, ast.Name) and isinstance(m.ctx, ast.Load) and m.id in DEFS \
                            and m.id not in names and m.id not in LOCALS[h]:
                        gnames.add(m.id)
            hist = set(EH.direct_kinds(n))
            for x in ctx:
                hist |= set(EH.direct_kinds(x))
            ctxseg = '\n'.join(ast.unparse(x) for x in ctx)
            for h in helpers:
                hist |= set(FK.get(h, ()))
            for g in gnames:
                flow |= name_tags(g, n.lineno)
                lits |= LIT.get((g, n.lineno), set())
                hist |= name_hist(g, n.lineno)
            tg = sorted(set(HT[key]) | set(tags_of(seg)) | set(tags_of(ctxseg)) | flow)
            lits |= set(lits_of(ctxseg))
            preds.append({'line': n.lineno, 'kind': kind, 'text': seg[:400],
                          'helpers': sorted(helpers), 'tags': tg, 'reads': sorted(lits)[:40], 'hist': sorted(hist),
                          'own_tags': tags_of(seg), 'context': ctxseg[:400]})
    msg_node = [n for n in body if n.lineno == line][0]
    msg = ''.join(c.value for c in ast.walk(msg_node.value.args[2]) if isinstance(c, ast.Constant)
                  and isinstance(c.value, str)) if len(msg_node.value.args) > 2 else ''
    out.append({'check': tag, 'line': line, 'span': [prev_end + 1, line],
                'accumulator': acc, 'predicates': preds, 'message': msg[:600]})
    prev_end = line
json.dump(out, open(sys.argv[2], 'w'), indent=1)
print('%d checks, %d predicates' % (len(out), sum(len(c['predicates']) for c in out)))
