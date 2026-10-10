import ast
STATE_NAMES = {'_MANIFEST_PROSPECTIVE', '_MANIFEST_BASELINE'}


def direct_kinds(node):
    k = set()
    for n in ast.walk(node):
        if isinstance(n, ast.Call):
            f = n.func
            fname = f.attr if isinstance(f, ast.Attribute) else (f.id if isinstance(f, ast.Name) else '')
            if fname in ('run', 'check_output', 'Popen', 'call', 'check_call'):
                for a in n.args[:1]:
                    for c in ast.walk(a):
                        if isinstance(c, ast.Constant) and c.value == 'git':
                            k.add('git')
            if isinstance(f, ast.Attribute) and f.attr == 'get' and isinstance(f.value, ast.Attribute) \
                    and f.value.attr == 'environ':
                k.add('env')
        if isinstance(n, ast.Attribute) and n.attr == 'environ':
            k.add('env')
        if isinstance(n, ast.Name) and n.id in STATE_NAMES:
            k.add('state')
        if isinstance(n, ast.Call):
            f = n.func
            fname = f.attr if isinstance(f, ast.Attribute) else (f.id if isinstance(f, ast.Name) else '')
            if fname in ('open', 'listdir', 'join', 'glob', 'isdir', 'exists', 'walk', 'scandir', 'isfile'):
                for a in n.args:
                    for c in ast.walk(a):
                        if isinstance(c, ast.Constant) and isinstance(c.value, str) and \
                                (c.value in ('seals', 'seals/') or 'verification/seals' in c.value):
                            k.add('seals-path')
    return k


def function_kinds(tree):
    funcs = {n.name: n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}
    calls = {k: {n.func.id for n in ast.walk(v) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
                 and n.func.id in funcs} for k, v in funcs.items()}
    kinds = {k: direct_kinds(v) for k, v in funcs.items()}
    changed = True
    while changed:
        changed = False
        for k in funcs:
            new = set(kinds[k])
            for c in calls[k]:
                new |= kinds[c]
            if new != kinds[k]:
                kinds[k] = new
                changed = True
    return kinds
