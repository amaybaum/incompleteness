p = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/v313/rd/controls.py'
t = open(p).read()
a = t.index('def free_loads(stmt):')
b = t.index('def closure(tree, roots, before):')
new = '''def free_loads(stmt):
    """The names a top-level statement may read from module scope. For a function or class: every
    name loaded anywhere in it that is not an argument or a name stored anywhere in it. Otherwise:
    the names loaded in module scope, and those loaded in a nested scope that the nested scope
    does not bind."""
    def loads(x):
        return {n.id for n in ast.walk(x) if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load)}

    def binds(x):
        return {n.arg for n in ast.walk(x) if isinstance(n, ast.arg)} | \\
            {n.id for n in ast.walk(x) if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Store)}
    if isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
        return loads(stmt) - binds(stmt)
    out = set()
    for n in module_nodes(stmt):
        if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load):
            out.add(n.id)
        for c in ast.iter_child_nodes(n):
            if isinstance(c, SCOPES):
                out |= loads(c) - binds(c)
    return out


'''
t = t[:a] + new + t[b:]
open(p, 'w').write(t)
