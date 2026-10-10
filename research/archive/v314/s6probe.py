import ast, json, sys
sys.path.insert(0, sys.argv[1])
import preserve as pv
d_text = open(sys.argv[2]).read(); census = json.load(open(sys.argv[3])); ledger = json.load(open(sys.argv[4]))
gone = pv.spliced(ledger['splices'])
tree = ast.parse(d_text)
parent = {}
for p in ast.walk(tree):
    for c in ast.iter_child_nodes(p):
        parent[c] = p
infunc = set()
for f in ast.walk(tree):
    if isinstance(f, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)):
        infunc.update(id(x) for x in ast.walk(f) if x is not f)
def base(e):
    while isinstance(e, (ast.Attribute, ast.Subscript, ast.Starred)):
        e = e.value
    return e.id if isinstance(e, ast.Name) else None
MUT = {'append', 'extend', 'insert', 'update', 'pop', 'popitem', 'remove', 'clear', 'setdefault',
       'add', 'discard', 'sort', 'reverse', 'write', 'writelines', 'difference_update',
       'intersection_update', 'symmetric_difference_update', 'appendleft', 'extendleft', 'seek',
       'truncate', 'close'}
def roots(s):
    out = set()
    if isinstance(s, ast.Expr):
        for c in ast.walk(s.value):
            if isinstance(c, ast.Call):
                if isinstance(c.func, ast.Attribute):
                    b = base(c.func.value)
                    if b: out.add(b)
                for a in list(c.args) + [k.value for k in c.keywords]:
                    b = base(a)
                    if b: out.add(b)
    elif isinstance(s, (ast.Assign, ast.AugAssign, ast.AnnAssign, ast.Delete)):
        tg = s.targets if isinstance(s, (ast.Assign, ast.Delete)) else [s.target]
        for t in tg:
            if isinstance(t, (ast.Subscript, ast.Attribute)) or isinstance(s, ast.Delete):
                b = base(t)
                if b: out.add(b)
        if getattr(s, 'value', None) is not None:
            for c in ast.walk(s.value):
                if isinstance(c, ast.Call) and isinstance(c.func, ast.Attribute) and c.func.attr in MUT:
                    b = base(c.func.value)
                    if b: out.add(b)
    return out
def src_names(e):
    """names an expression's value may alias: loaded names, not callees"""
    callee = set()
    for c in ast.walk(e):
        if isinstance(c, ast.Call):
            callee.update(id(x) for x in ast.walk(c.func))
    return {x.id for x in ast.walk(e) if isinstance(x, ast.Name) and isinstance(x.ctx, ast.Load) and id(x) not in callee}
modstmts = [n for n in ast.walk(tree) if isinstance(n, ast.stmt) and id(n) not in infunc]
binders = []
for n in modstmts:
    if isinstance(n, (ast.For, ast.AsyncFor)):
        binders.append((n.lineno, {x.id for x in ast.walk(n.target) if isinstance(x, ast.Name)}, src_names(n.iter)))
    elif isinstance(n, (ast.Assign, ast.AnnAssign)) and n.value is not None:
        tg = n.targets if isinstance(n, ast.Assign) else [n.target]
        nm = {x.id for t in tg for x in ast.walk(t) if isinstance(x, ast.Name) and isinstance(x.ctx, ast.Store)}
        binders.append((n.lineno, nm, src_names(n.value)))
    elif isinstance(n, ast.With):
        for i in n.items:
            if i.optional_vars is not None:
                binders.append((n.lineno, {x.id for x in ast.walk(i.optional_vars) if isinstance(x, ast.Name)}, src_names(i.context_expr)))
def aliases(nm, line):
    out, todo = {nm}, [(nm, line)]
    while todo:
        a, l = todo.pop()
        prev = [b for b in binders if a in b[1] and b[0] <= l]
        if not prev: continue
        b = max(prev, key=lambda b: b[0])
        for s in b[2]:
            if s not in out:
                out.add(s); todo.append((s, b[0]))
    return out
def whole(n): return set(range(n.lineno, n.end_lineno + 1)) <= gone
disp = {c['check']: c['disposition'] for c in census['checks']}
amend = {(c, l): h for c, l, h in pv.AMENDMENT}
retired = set()
for row in census['predicates']:
    if row[2] in pv.RETIRE or disp[row[0]] == 'removed whole' or amend.get((row[0], row[1])) == row[6]:
        retired.add(row[1])
def binder_at(x, line):
    prev = [b for b in binders if x in b[1] and b[0] <= line]
    return max(prev, key=lambda b: b[0])[0] if prev else None
reads = []
for n in ast.walk(tree):
    if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load) and n.lineno not in gone:
        reads.append((n.lineno, n.id, id(n) in infunc))
flags = []
cnt = 0
for s in modstmts:
    if isinstance(s, (ast.For, ast.While, ast.If, ast.With, ast.Try, ast.FunctionDef, ast.ClassDef)) or not whole(s):
        continue
    if s.lineno in retired:
        continue
    r = roots(s)
    if isinstance(s, ast.Expr) and isinstance(s.value, ast.Call) and getattr(s.value.func, 'id', None) == 'print':
        r = set()
    if not r: continue
    cnt += 1
    A = set().union(*(aliases(x, s.lineno) for x in r))
    hit = sorted({nm for l, nm, f in reads if nm in A and (f or (l > s.lineno and binder_at(nm, l) == binder_at(nm, s.lineno)))})
    if hit:
        flags.append((s.lineno, sorted(r), hit, d_text.split('\n')[s.lineno-1].strip()[:90]))
print('removed mutating statements:', cnt, 'flagged:', len(flags))
for f in flags: print(f)
