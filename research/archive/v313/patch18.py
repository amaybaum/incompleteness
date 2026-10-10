p = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/v313/rd/controls.py'
t = open(p).read()
old = """            ns['os'], ns['open'] = shim_os(vt), vt.open
            exec(compile(ast.Module([st], []), GUARD, 'exec'), ns)
        ns['os'], ns['open'] = shim_os(vt), vt.open
"""
new = """            shim(ns, vt)
            exec(compile(ast.Module([st], []), GUARD, 'exec'), ns)
        shim(ns, vt)
"""
assert t.count(old) == 1; t = t.replace(old, new)
old = "def run_predicates(repo, d, lines, override=None):"
new = '''def shim(ns, vt):
    """The module scope's file system is the virtual tree, and no child process can start."""
    def refused(*_a, **_k):
        raise PermissionError('a child process was started')
    ns['os'], ns['open'] = shim_os(vt), vt.open
    ns['subprocess'] = types.SimpleNamespace(run=refused, check_output=refused, Popen=refused,
                                             call=refused, check_call=refused)


def run_predicates(repo, d, lines, override=None):'''
assert t.count(old) == 1; t = t.replace(old, new)
open(p, 'w').write(t)
