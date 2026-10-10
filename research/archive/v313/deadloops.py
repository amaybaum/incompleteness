"""Scratch: module-level for loops whose body only binds names (assignments to plain names and
function definitions) that no statement outside the loop reads before rebinding them."""
import ast, sys
src = open(sys.argv[1], encoding='utf-8').read(); t = ast.parse(src)
def binds(stmts):
    out = set()
    for s in stmts:
        if isinstance(s, ast.Assign) and all(isinstance(x, ast.Name) for x in s.targets):
            out |= {x.id for x in s.targets}
        elif isinstance(s, ast.FunctionDef):
            out.add(s.name)
        else:
            return None
    return out
def free_reads(node):
    """Names a statement reads before binding them itself, in straight-line order of its body."""
    if isinstance(node, ast.For):
        bound = {n.id for n in ast.walk(node.target) if isinstance(n, ast.Name)}
        reads = {n.id for n in ast.walk(node.iter) if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load)}
        body = node.body + node.orelse
    else:
        bound, reads, body = set(), set(), [node]
    for s in body:
        r = {n.id for n in ast.walk(s) if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load)}
        if isinstance(s, ast.FunctionDef):
            r = {n.id for d in s.args.defaults for n in ast.walk(d) if isinstance(n, ast.Name)} | \
                {n.id for n in ast.walk(s) if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load)}
        reads |= r - bound
        if isinstance(s, ast.Assign):
            bound |= {n.id for x in s.targets for n in ast.walk(x) if isinstance(n, ast.Name)}
        elif isinstance(s, ast.FunctionDef):
            bound.add(s.name)
    return reads
body = t.body
dead = set()
changed = True
while changed:
    changed = False
    for i, s in enumerate(body):
        if i in dead or not isinstance(s, ast.For):
            continue
        b = binds(s.body)
        if b is None or s.orelse:
            continue
        b |= {n.id for n in ast.walk(s.target) if isinstance(n, ast.Name)}
        others = set()
        for j, o in enumerate(body):
            if j != i and j not in dead:
                others |= free_reads(o)
        if not (b & others):
            dead.add(i); changed = True
for i in sorted(dead):
    s = body[i]
    print('DEAD LOOP  line %d-%d  %s' % (s.lineno, s.end_lineno, ast.unparse(s).split('\n')[0][:100]))
