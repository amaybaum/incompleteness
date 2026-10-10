p = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/v313/rd/controls.py'
t = open(p).read()
a = t.index('def bindings(stmt):')
b = t.index('class VirtualTree:')
new = '''SCOPES = (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda, ast.ClassDef, ast.ListComp,
          ast.SetComp, ast.DictComp, ast.GeneratorExp)


def module_nodes(stmt):
    """The nodes of a top-level statement that run in module scope: nothing inside a nested
    function, lambda, class or comprehension."""
    todo = [stmt]
    while todo:
        n = todo.pop()
        yield n
        for c in ast.iter_child_nodes(n):
            if not isinstance(c, SCOPES):
                todo.append(c)


def bindings(stmt):
    """The module-level names a top-level statement binds."""
    if isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
        return {stmt.name}
    out = set()
    for n in module_nodes(stmt):
        if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Store):
            out.add(n.id)
        elif isinstance(n, (ast.Import, ast.ImportFrom)):
            out |= {(a.asname or a.name).split('.')[0] for a in n.names}
    return out


def free_loads(stmt):
    """The names a top-level statement may read from module scope: every name it loads that is not
    bound locally in the function, lambda or comprehension that loads it."""
    local = set()
    for n in ast.walk(stmt):
        if isinstance(n, ast.arg):
            local.add(n.arg)
        elif isinstance(n, ast.Name) and isinstance(n.ctx, ast.Store) and not \\
                any(n is m for m in module_nodes(stmt)):
            local.add(n.id)
    top = {n.id for n in module_nodes(stmt) if isinstance(n, ast.Name)
           and isinstance(n.ctx, ast.Load)}
    inner = {n.id for n in ast.walk(stmt) if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load)}
    return top | (inner - local)


def closure(tree, roots, before):
    """The top-level statements before line `before` that bind a name the roots need, transitively
    (each such statement's own module-scope reads included), in file order."""
    body = [s for s in tree.body if s.lineno < before]
    binds = [bindings(s) for s in body]
    need, chosen, todo = set(), set(), set(roots)
    while todo:
        nm = todo.pop()
        if nm in need:
            continue
        need.add(nm)
        for i, s in enumerate(body):
            if i not in chosen and nm in binds[i]:
                chosen.add(i)
                todo |= free_loads(s)
    return [body[i] for i in sorted(chosen)]


'''
t = t[:a] + new + t[b:]
open(p, 'w').write(t)
