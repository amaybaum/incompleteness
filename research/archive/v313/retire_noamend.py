#!/usr/bin/env python3
"""V3-13's retirement of the guard's legacy predicates: a deterministic transformation of the guard.

Usage: retire.py <guard at D> <census.json> <output guard> [<messages.json> [<headers.json>]]

Reads the guard verification/lean/edge_rigidity_probe.py as it stands at V3-13's D and V3-12's
census of it, and writes the guard with:

1. every predicate the census classes redundant, retire-history, retire-machinery or retire-whole
   removed, each identified by its line and the SHA-256 prefix of its unparsed text, which must
   match;
2. every check the census empties removed whole: its call and its bookkeeping;
3. every compound statement left with an empty body removed with it;
4. dead code removed to a fixpoint: a module-level function no remaining code names, an assignment
   or in-place mutation of a name no remaining code reads, an expression statement that reads a
   name nothing defines any longer, an import nothing uses, and a comment-only paragraph whose code
   is gone;
5. the messages of the split checks replaced by the texts in <messages.json>, when given;
6. the comment paragraphs describing the base and seal constants that round SI-3 removed deleted,
   and the header paragraphs of the checks named in <headers.json> replaced by its texts.

Deletion works on source line ranges, so every retained line is byte-identical to its line at D."""
import ast
import builtins
import collections
import hashlib
import json
import re
import sys

RETIRE = {'redundant', 'retire-history', 'retire-machinery', 'retire-whole'}
# Amendments to V3-12's census: predicates it retained that read legacy seal state. Each compares
# round PC4's seal record, read from verification/seals/ through the record reader `_si1_load`,
# with constants; the census's resolver could not resolve that reader's path (a starred join of a
# module constant), so it retained them as unresolved. legacy-records pins that record.
AMEND = set()
MUTATORS = ('append', 'extend', 'update', 'add', 'setdefault', 'insert', 'pop', 'remove',
            'discard', 'clear', 'sort')


def sha16(node):
    return hashlib.sha256(ast.unparse(node).encode('utf-8')).hexdigest()[:16]


def root_name(t):
    while isinstance(t, (ast.Subscript, ast.Attribute, ast.Starred)):
        t = t.value
    return t.id if isinstance(t, ast.Name) else None


def target_names(n):
    out = set()
    tg = n.targets if isinstance(n, ast.Assign) else [n.target]
    for t in tg:
        for m in ast.walk(t):
            if isinstance(m, ast.Name) and isinstance(m.ctx, ast.Store):
                out.add(m.id)
        r = root_name(t)
        if r:
            out.add(r)
    return out


class Source:
    def __init__(self, text):
        self.lines = text.split('\n')
        self.tree = ast.parse(text)
        self.parent = {}
        for p in ast.walk(self.tree):
            for c in ast.iter_child_nodes(p):
                self.parent[c] = p
        self.else_lines = set()
        self.func_lines = set()
        for f in ast.walk(self.tree):
            if isinstance(f, (ast.FunctionDef, ast.AsyncFunctionDef)):
                self.func_lines.update(range(f.lineno, f.end_lineno + 1))

    def text(self):
        return '\n'.join(self.lines)

    def delete(self, ranges):
        """Delete whole-line ranges [a, b] (1-based, inclusive)."""
        drop = set()
        for a, b in ranges:
            drop.update(range(a, b + 1))
        return '\n'.join(l for i, l in enumerate(self.lines, 1) if i not in drop)


def stmt_range(src, n):
    """The line range of a statement, with any decorators."""
    a = min([n.lineno] + [d.lineno for d in getattr(n, 'decorator_list', [])])
    b = n.end_lineno
    # a statement must own its lines: nothing else may start on them
    return a, b


def body_lists(n):
    if isinstance(n, ast.Module):
        yield 'body', n.body
        return
    for f in ('body', 'orelse', 'finalbody'):
        v = getattr(n, f, None)
        if isinstance(v, list):
            yield f, v
    for h in getattr(n, 'handlers', []) or []:
        yield 'handler', h.body


def emptied(src, removed):
    """Compound statements every statement of whose body is removed, and whose other arms are
    removed or empty: remove them too. An else arm emptied under a live body goes with its lone
    `else:` line. Fixpoint over removed; returns the else lines to delete."""
    grown = True
    while grown:
        grown = False
        for n in ast.walk(src.tree):
            if n in removed or not isinstance(n, (ast.For, ast.While, ast.If, ast.With, ast.Try)):
                continue
            arms = [v for f, v in body_lists(n) if f != 'body']
            if all(gone(s, removed) for s in n.body) and all(gone(s, removed) for v in arms for s in v):
                removed.add(n)
                grown = True
    else_lines = set()
    for n in ast.walk(src.tree):
        if n in removed or not isinstance(n, (ast.If, ast.For, ast.While)) or not n.orelse:
            continue
        if all(s in removed for s in n.orelse) and not all(s in removed for s in n.body):
            if isinstance(n.orelse[0], ast.If) and src.lines[n.orelse[0].lineno - 1].lstrip() \
                    .startswith('elif'):
                continue            # an elif is its own statement and its own lines
            k = n.orelse[0].lineno - 1
            if src.lines[k - 1].strip() != 'else:':
                raise SystemExit('retire: an emptied else arm without a lone else line at %d' % k)
            else_lines.add(k)
    return else_lines


def gone(s, removed):
    """A statement that is removed, or that is only control flow once the removed are gone:
    continue, break or pass, or an if whose arms hold nothing else."""
    if s in removed or isinstance(s, (ast.Continue, ast.Break, ast.Pass)):
        return True
    if isinstance(s, ast.If):
        return all(gone(x, removed) for x in s.body + s.orelse)
    return False


def validate(src, removed):
    """No live compound keeps an arm whose every statement is removed."""
    for n in ast.walk(src.tree):
        if n in removed or not isinstance(n, ast.stmt):
            continue
        if any(n in removed for n in []):
            continue
        for f, v in body_lists(n):
            if v and all(s in removed for s in v) and f == 'body':
                live = [s for f2, v2 in body_lists(n) if f2 != 'body' for s in v2
                        if s not in removed]
                for s in live[:8]:
                    print('  LIVE %d %s' % (s.lineno, ast.unparse(s)[:110].replace('\n', ' ')))
                names = set()
                for s in live:
                    names |= target_names(s) if isinstance(s, (ast.Assign, ast.AugAssign)) else set()
                skip = removed_ids(removed)
                for m in ast.walk(src.tree):
                    if isinstance(m, ast.Name) and m.id in names and isinstance(m.ctx, ast.Load) \
                            and id(m) not in skip:
                        top = m
                        while src.parent.get(top) is not src.tree and top in src.parent:
                            top = src.parent[top]
                        print('  READ %s at %d by top-level statement at %d: %s' % (
                            m.id, m.lineno, top.lineno, ast.unparse(top)[:90].replace('\n', ' ')))
                raise SystemExit('retire: the body of a live statement at line %d is removed'
                                 % n.lineno)
            if v and all(s in removed for s in v) and f == 'handler':
                raise SystemExit('retire: a handler at line %d is emptied' % n.lineno)


def removed_ids(removed):
    out = set()
    for s in removed:
        out.update(id(m) for m in ast.walk(s))
    return out


def loads(tree, skip):
    c = collections.Counter()
    for m in ast.walk(tree):
        if id(m) not in skip and isinstance(m, ast.Name) and isinstance(m.ctx, (ast.Load, ast.Del)):
            c[m.id] += 1
    return c


def defined_names(src, skip):
    """The names bound at module level by what is not removed: module-level stores, top-level
    functions and classes, imports, and the builtins."""
    tree = src.tree
    out = set(dir(builtins)) | {'__file__', '__name__', '__doc__'}
    for m in ast.walk(tree):
        if id(m) in skip:
            continue
        if isinstance(m, ast.Name) and isinstance(m.ctx, ast.Store) and \
                m.lineno not in src.func_lines:
            out.add(m.id)
        elif isinstance(m, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) and \
                src.parent.get(m) is tree:
            out.add(m.name)
        elif isinstance(m, (ast.Import, ast.ImportFrom)) and m.lineno not in src.func_lines:
            for a in m.names:
                out.add((a.asname or a.name).split('.')[0])
    return out


def mutated_root(n):
    if isinstance(n, ast.Expr) and isinstance(n.value, ast.Call) and \
            isinstance(n.value.func, ast.Attribute) and n.value.func.attr in MUTATORS:
        return root_name(n.value.func.value)
    return None


def mutation_of(s):
    """The name a statement mutates in place, if it only mutates one."""
    if isinstance(s, ast.Expr):
        return mutated_root(s)
    if isinstance(s, (ast.Assign, ast.AugAssign)):
        tg = s.targets if isinstance(s, ast.Assign) else [s.target]
        roots = {root_name(t) for t in tg if isinstance(t, (ast.Subscript, ast.Attribute))}
        if len(roots) == 1 and all(isinstance(t, (ast.Subscript, ast.Attribute)) for t in tg):
            return roots.pop()
    return None


WHY = {}
SIMPLE = (ast.Assign, ast.AugAssign, ast.AnnAssign, ast.Expr, ast.Import, ast.ImportFrom,
          ast.Assert, ast.Delete, ast.Raise, ast.Global, ast.Pass, ast.Continue, ast.Break)
COMPOUND = (ast.For, ast.While, ast.If, ast.With, ast.Try)


def headers_of(src, n):
    """The expressions of the compound statements enclosing n that decide whether it runs."""
    out = []
    a = src.parent.get(n)
    while a is not None and a is not src.tree:
        if isinstance(a, (ast.If, ast.While)):
            out.append(a.test)
        elif isinstance(a, ast.For):
            out.append(a.iter)
        elif isinstance(a, ast.With):
            out.extend(i.context_expr for i in a.items)
        a = src.parent.get(a)
    return out


def local_bindings(n):
    out = set()
    for m in ast.walk(n):
        if isinstance(m, ast.arg):
            out.add(m.arg)
        elif isinstance(m, ast.Name) and isinstance(m.ctx, ast.Store):
            out.add(m.id)
        elif isinstance(m, ast.comprehension):
            out |= {x.id for x in ast.walk(m.target) if isinstance(x, ast.Name)}
    return out


def uses_of(src, n):
    """The module-level names a statement needs: what it and its enclosing headers read; for a
    function, what its body reads that it does not bind itself."""
    if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
        loc = local_bindings(n) - {n.name}
        return {m.id for m in ast.walk(n) if isinstance(m, ast.Name)
                and isinstance(m.ctx, (ast.Load, ast.Del)) and m.id not in loc} - {n.name}
    parts = [n] + headers_of(src, n)
    comp = set()
    for x in parts:
        for m in ast.walk(x):
            if isinstance(m, ast.comprehension):
                comp |= {y.id for y in ast.walk(m.target) if isinstance(y, ast.Name)}
            elif isinstance(m, ast.Lambda):
                comp |= {y.arg for y in ast.walk(m.args) if isinstance(y, ast.arg)}
    return {m.id for x in parts for m in ast.walk(x) if isinstance(m, ast.Name)
            and isinstance(m.ctx, (ast.Load, ast.Del)) and m.id not in comp}


def binds_of(src, n):
    """The module-level names a simple statement or function binds or mutates."""
    if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
        return {n.name}
    if isinstance(n, (ast.Import, ast.ImportFrom)):
        return {(a.asname or a.name).split('.')[0] for a in n.names}
    out = set()
    if isinstance(n, (ast.Assign, ast.AnnAssign, ast.AugAssign)):
        out |= target_names(n)
    m = mutated_root(n) if isinstance(n, ast.Expr) else None
    if m:
        out.add(m)
    return out


def header_binds(src, n):
    """Names bound by the compound headers enclosing n (for targets, with-as)."""
    out = set()
    a = src.parent.get(n)
    while a is not None and a is not src.tree:
        if isinstance(a, ast.For):
            out |= {x.id for x in ast.walk(a.target) if isinstance(x, ast.Name)}
        elif isinstance(a, ast.With):
            for i in a.items:
                if i.optional_vars is not None:
                    out |= {x.id for x in ast.walk(i.optional_vars) if isinstance(x, ast.Name)}
        a = src.parent.get(a)
    return out


def mark_sweep(src, removed, roots):
    """Everything no root needs: the module-level simple statements and top-level functions that
    no live statement reaches. A module-level statement needs the definitions of each name it reads
    that can reach it (walking back to the nearest top-level definition) and the in-place
    mutations after the earliest of them; a function needs every module-level definition of each
    global it reads, since it may run at any call."""
    tree = src.tree
    units = [n for n in ast.walk(tree) if
             (isinstance(n, SIMPLE) and n.lineno not in src.func_lines) or
             (isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and src.parent.get(n) is tree)]
    units = [n for n in units if n not in removed and not any(
        a in removed for a in ancestors(src, n))]
    unit_set = set(units)
    binders = collections.defaultdict(list)       # plain (re)definitions, by line
    mutators = collections.defaultdict(list)      # in-place mutations, by line
    for n in units:
        m = mutation_of(n)
        for nm in binds_of(src, n):
            (mutators if nm == m else binders)[nm].append(n)
    # compound headers bind names too (for targets, with-as); they count as definitions
    for n in ast.walk(tree):
        if isinstance(n, (ast.For, ast.With)) and n.lineno not in src.func_lines:
            names = set()
            if isinstance(n, ast.For):
                names = {x.id for x in ast.walk(n.target) if isinstance(x, ast.Name)}
            else:
                for i in n.items:
                    if i.optional_vars is not None:
                        names |= {x.id for x in ast.walk(i.optional_vars) if isinstance(x, ast.Name)}
            for nm in names:
                binders[nm].append(n)
    for k in binders:
        binders[k].sort(key=lambda d: d.lineno)
    for k in mutators:
        mutators[k].sort(key=lambda d: d.lineno)

    def reaching(nm, line):
        ds = [d for d in binders.get(nm, []) if d.lineno < line]
        out = []
        for d in reversed(ds):
            out.append(d)
            if src.parent.get(d) is tree and not isinstance(d, ast.AugAssign):
                break
        start = min((d.lineno for d in out), default=0)
        out += [m for m in mutators.get(nm, []) if start <= m.lineno < line]
        return out
    live, todo = set(), []
    for r in roots:
        if r not in live:
            live.add(r)
            todo.append(r)
    while todo:
        n = todo.pop()
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
            deps = [d for nm in uses_of(src, n) for d in binders.get(nm, []) + mutators.get(nm, [])]
        elif isinstance(n, (ast.For, ast.With)):
            deps = [d for x in headers_of_self(n) for nm in names_in(x)
                    for d in reaching(nm, n.lineno)] + [a for a in ancestors(src, n)]
            deps += [d for a in ancestors(src, n) for x in headers_of_self(a)
                     for nm in names_in(x) for d in reaching(nm, a.lineno)]
        else:
            hb = header_binds(src, n)
            deps = [d for nm in uses_of(src, n) - hb for d in reaching(nm, n.lineno)]
            deps += [d for nm in (uses_of(src, n) & hb) for d in reaching(nm, n.lineno)
                     if isinstance(d, (ast.For, ast.With))]
            if isinstance(n, (ast.AugAssign,)) or mutation_of(n):
                for nm in binds_of(src, n):
                    deps += reaching(nm, n.lineno)
        for d in deps:
            if d not in live:
                live.add(d)
                WHY[d] = n
                todo.append(d)
    return [n for n in units if n not in live], live


def counters(src, removed, predicates, mismatches):
    """Counter increments that count retired predicates only: `c += <int>` whose run of immediately
    preceding sibling predicates (or the one compound statement holding predicates just before it)
    is removed entirely. A run mixing removed and retained predicates is a count the
    transformation cannot restate, and is reported."""
    out = set()
    for n in ast.walk(src.tree):
        for f, v in body_lists(n) if isinstance(n, (ast.Module,) + COMPOUND) else []:
            for i, st in enumerate(v):
                if st in removed or not (isinstance(st, ast.AugAssign) and
                                         isinstance(st.target, ast.Name) and
                                         isinstance(st.op, ast.Add) and
                                         isinstance(st.value, ast.Constant) and
                                         isinstance(st.value.value, int)):
                    continue
                if st.lineno in src.func_lines:
                    continue
                name = st.target.id
                preds = []
                for s2 in reversed(v[:i]):
                    if s2 in predicates:
                        preds.append(s2)
                    elif isinstance(s2, COMPOUND) and any(y in predicates for y in ast.walk(s2)) \
                            and not preds:
                        preds.append(s2)
                        break
                    else:
                        break
                if not preds:
                    continue
                gone_ = [x for x in preds if x in removed or (isinstance(x, COMPOUND) and all(
                    y in removed for y in ast.walk(x) if y in predicates))]
                if len(gone_) == len(preds):
                    out.add(st)
                elif gone_:
                    mismatches.append(st.lineno)
    return out


def headers_of_self(n):
    if isinstance(n, (ast.If, ast.While)):
        return [n.test]
    if isinstance(n, ast.For):
        return [n.iter]
    if isinstance(n, ast.With):
        return [i.context_expr for i in n.items]
    return []


def names_in(x):
    return {m.id for m in ast.walk(x) if isinstance(m, ast.Name) and isinstance(m.ctx, ast.Load)}


def ancestors(src, n):
    a = src.parent.get(n)
    while a is not None and a is not src.tree:
        yield a
        a = src.parent.get(a)


def comment_paragraphs(text):
    """Remove paragraphs (blank-line separated) consisting only of comments."""
    lines = text.split('\n')
    out, para = [], []

    def flush():
        if para and all(l.strip().startswith('#') for l in para):
            return
        out.extend(para)

    for l in lines:
        if l.strip() == '':
            flush()
            para.clear()
            out.append(l)
        else:
            para.append(l)
    flush()
    # collapse runs of more than two blank lines left behind
    res, blanks = [], 0
    for l in out:
        blanks = blanks + 1 if l.strip() == '' else 0
        if blanks <= 2:
            res.append(l)
    return '\n'.join(res)


def checks_of(tree):
    out = {}
    for n in tree.body:
        if isinstance(n, ast.Expr) and isinstance(n.value, ast.Call) and \
                isinstance(n.value.func, ast.Name) and n.value.func.id == 'check':
            out[n.value.args[0].value] = n
    return out


def main():
    guard, census_path, outpath = sys.argv[1:4]
    messages = json.load(open(sys.argv[4], encoding='utf-8')) if len(sys.argv) > 4 else {}
    headers = json.load(open(sys.argv[5], encoding='utf-8')) if len(sys.argv) > 5 else {}
    text0 = open(guard, encoding='utf-8').read()
    census = json.load(open(census_path, encoding='utf-8'))
    src = Source(text0)
    by_line = collections.defaultdict(list)
    for n in ast.walk(src.tree):
        if isinstance(n, (ast.Assign, ast.AugAssign, ast.Expr)) and n.lineno not in src.func_lines:
            by_line[n.lineno].append(n)
    disp = {c['check']: c['disposition'] for c in census['checks']}
    removed, keep_texts, retained = set(), collections.Counter(), []
    for row in census['predicates']:
        chk, line, cls, sha = row[0], row[1], row[2], row[6]
        cands = [n for n in by_line[line] if sha16(n) == sha]
        if len(cands) != 1:
            raise SystemExit('retire: %s line %d does not match its text hash' % (chk, line))
        n = cands[0]
        if cls in RETIRE or (disp[chk] == 'removed whole') or (chk, line) in AMEND:
            removed.add(n)
        else:
            keep_texts[(chk, ast.unparse(n))] += 1
            retained.append(n)
    checks = checks_of(src.tree)
    for chk, d in disp.items():
        if d == 'removed whole':
            removed.add(checks[chk])
    # the roots: the retained predicates and check calls, the side-effect statements of retained
    # checks, and everything after the last check call
    kept = [n for n in checks.values() if n not in removed]
    check_lines = sorted((n.lineno, n in removed) for n in checks.values())
    last_check = max(l for l, _r in check_lines)

    def owner_removed(line):
        for l, r in check_lines:
            if l >= line:
                return r
        return False
    roots = set(kept) | {n for n in retained}
    for n in ast.walk(src.tree):
        if isinstance(n, SIMPLE) and n.lineno not in src.func_lines and n not in removed and \
                not any(a in removed for a in ancestors(src, n)):
            if n.lineno > last_check:
                roots.add(n)
            elif isinstance(n, ast.Expr) and not mutated_root(n) and not owner_removed(n.lineno) \
                    and not (isinstance(n.value, ast.Call) and isinstance(n.value.func, ast.Name)
                             and n.value.func.id == 'check'):
                roots.add(n)
            elif isinstance(n, (ast.Import, ast.ImportFrom)) and n.lineno < check_lines[0][0]:
                pass
    predicates = set(retained) | {n for n in removed if isinstance(n, (ast.Assign, ast.AugAssign,
                                                                        ast.Expr))}
    mismatches = []
    rounds = 0
    while True:
        rounds += 1
        before = len(removed)
        dead, live = mark_sweep(src, removed, roots - removed)
        removed |= set(dead)
        removed |= counters(src, removed, predicates, mismatches)
        emptied(src, removed)
        if len(removed) == before:
            break
    for m in sorted(set(mismatches)):
        print('retire: COUNTER counts retired and retained controls at line %d' % m)
    else_lines = emptied(src, removed)
    validate(src, removed)
    text = src.delete([stmt_range(src, n) for n in removed] + [(k, k) for k in else_lines])
    text = comment_paragraphs(text)
    # messages
    s = Source(text)
    checks = checks_of(s.tree)
    for chk, new in sorted(messages.items()):
        n = checks[chk]
        arg = n.value.args[2]
        a, b = arg.lineno, arg.end_lineno
        first, last = s.lines[a - 1], s.lines[b - 1]
        pre, post = first[:arg.col_offset], last[arg.end_col_offset:]
        body = format_message(new, len(pre))
        s.lines[a - 1:b] = [pre + body[0]] + body[1:-1] + ([body[-1] + post] if len(body) > 1 else [])
        if len(body) == 1:
            s.lines[a - 1] = pre + body[0] + post
        text = s.text()
        s = Source(text)
        checks = checks_of(s.tree)
    text = comments(text, headers)
    open(outpath, 'w', encoding='utf-8', newline='\n').write(text)
    # the controls
    s = Source(text)
    after = collections.Counter()
    ch = checks_of(s.tree)
    for n in ast.walk(s.tree):
        if isinstance(n, (ast.Assign, ast.AugAssign, ast.Expr)) and n.lineno not in s.func_lines:
            after[ast.unparse(n)] += 1
    missing = [k for k, v in keep_texts.items() if after[k[1]] < v]
    gone_checks = sorted(set(disp) - set(ch))
    print('retire: %d statements removed directly, %d dead-code rounds, %d lines -> %d lines'
          % (len(removed), rounds, len(text0.split('\n')), len(text.split('\n'))))
    print('retire: %d checks remain; emptied: %s' % (len(ch), ', '.join(gone_checks)))
    print('retire: retained predicates missing: %d' % len(missing))
    for k in missing[:20]:
        print('  MISSING', k[0], k[1][:120])
    return 0 if not missing else 1


ORPHAN = '# The mandated execution base: '


def comments(text, headers):
    """The comment paragraphs: each paragraph opening with ORPHAN -- the description of a base or
    seal constant that round SI-3 removed and whose comment it left -- deleted, and each
    retained check's header paragraph, `# ---- <tag>: ...`, replaced by its text in `headers`."""
    lines, out, i, done = text.split('\n'), [], 0, set()
    while i < len(lines):
        j = i
        while j < len(lines) and lines[j].startswith('#'):
            j += 1
        if j == i:
            out.append(lines[i])
            i += 1
            continue
        para = lines[i:j]
        m = re.match(r'# ---- (R7-[A-Z0-9]+):', para[0])
        if para[0].startswith(ORPHAN):
            pass
        elif m and m.group(1) in headers:
            out.extend(headers[m.group(1)].split('\n'))
            done.add(m.group(1))
        else:
            out.extend(para)
        i = j
    if done != set(headers):
        raise SystemExit('retire: header paragraphs not found: %s' % sorted(set(headers) - done))
    text = '\n'.join(out)
    while '\n\n\n\n' in text:
        text = text.replace('\n\n\n\n', '\n\n\n')
    return text


def format_message(msg, indent):
    """A message as adjacent string literals wrapped at 100 columns, first line after `indent`."""
    words, lines, cur = msg.split(' '), [], ''
    width = 100 - indent - 3
    for w in words:
        cand = (cur + ' ' + w) if cur else w
        if len(cand) > width and cur:
            lines.append(cur + ' ')
            cur = w
        else:
            cur = cand
    lines.append(cur)
    out = [repr(lines[0])] + [' ' * indent + repr(l) for l in lines[1:]]
    return out


if __name__ == '__main__':
    sys.exit(main())
