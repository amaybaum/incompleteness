import ast, json, sys
sys.path.insert(0, sys.argv[1]); import preserve as pv
d_text = open(sys.argv[2]).read(); census = json.load(open(sys.argv[3])); ledger = json.load(open(sys.argv[4]))
gone = pv.spliced(ledger['splices']); tree = ast.parse(d_text)
def whole(n): return set(range(n.lineno, n.end_lineno + 1)) <= gone
infunc = set()
for f in ast.walk(tree):
    if isinstance(f, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda, ast.ClassDef)):
        infunc |= {id(x) for x in ast.walk(f) if x is not f}
disp = {c['check']: c['disposition'] for c in census['checks']}
amend = {(c, l): h for c, l, h in pv.AMENDMENT}
retired = {r[1] for r in census['predicates'] if r[2] in pv.RETIRE or disp[r[0]] == 'removed whole' or amend.get((r[0], r[1])) == r[6]}
def binds(n):
    if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)): return {n.name}
    if isinstance(n, (ast.Import, ast.ImportFrom)): return {(a.asname or a.name).split('.')[0] for a in n.names}
    if isinstance(n, (ast.Assign, ast.AnnAssign)):
        tg = n.targets if isinstance(n, ast.Assign) else [n.target]
        return {x.id for t in tg if isinstance(t, (ast.Name, ast.Tuple, ast.List, ast.Starred)) for x in ast.walk(t) if isinstance(x, ast.Name)}
    if isinstance(n, ast.For): return {x.id for x in ast.walk(n.target) if isinstance(x, ast.Name)}
    if isinstance(n, ast.With): return {x.id for i in n.items if i.optional_vars is not None for x in ast.walk(i.optional_vars) if isinstance(x, ast.Name)}
    return set()
mod = [n for n in ast.walk(tree) if isinstance(n, ast.stmt) and id(n) not in infunc]
defs = [(n.lineno, x, whole(n)) for n in mod for x in binds(n)]
surv_defs = {}
for l, x, g in defs:
    if not g: surv_defs.setdefault(x, []).append(l)
localof = {}
for f in ast.walk(tree):
    if isinstance(f, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)):
        loc = {a.arg for a in ast.walk(f.args) if isinstance(a, ast.arg)}
        body = f.body if isinstance(f.body, list) else [f.body]
        for b in body:
            for x in ast.walk(b):
                if isinstance(x, ast.Name) and isinstance(x.ctx, (ast.Store, ast.Del)): loc.add(x.id)
                elif isinstance(x, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)): loc.add(x.name)
                elif isinstance(x, (ast.Global, ast.Nonlocal)): loc -= set(x.names)
        for x in ast.walk(f):
            if isinstance(x, ast.Name) and x is not f: localof.setdefault(id(x), set()).update(loc)
reads = [(n.lineno, n.id, id(n) in infunc) for n in ast.walk(tree) if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load) and n.lineno not in gone and n.id not in localof.get(id(n), set())]
import bisect
rd = {}
for l, x, f in reads: rd.setdefault(x, []).append((l, f))
bad, total = [], 0
for n in mod:
    if not whole(n) or n.lineno in retired: continue
    b = binds(n)
    if not b: continue
    total += 1
    for x in b:
        sd = sorted(surv_defs.get(x, []))
        for l, f in rd.get(x, []):
            if f:
                if not sd: bad.append((n.lineno, x, l, 'function read, no surviving binding')); break
            elif l > n.lineno and not any(n.lineno < s < l for s in sd) and not any(s < l for s in sd if s > n.lineno) :
                # nearest binding before l is this removed one (no surviving binding between)
                prev_surv = [s for s in sd if s <= l]
                if not prev_surv or max(prev_surv) < n.lineno:
                    bad.append((n.lineno, x, l, 'module read')); break
print('removed binding statements:', total, 'flagged:', len(bad))
for b in bad[:30]: print(b)
