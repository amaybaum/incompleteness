"""Scratch: the README surfaces the guard's A6P and A6I predicates read, checked on an edited
README by the guard's own scanner functions, extracted by AST from the guard file. Not the guard
run: only these pure text functions and their constants are executed.
Usage: readme_control.py <guard> <README at D> <README edited>"""
import ast, re, sys
g = open(sys.argv[1], encoding='utf-8').read()
t = ast.parse(g)
want = {'_A6P_NEG', '_A6P_PHRASES', '_A6I_NEG', '_A6I_PHRASES', '_a6p_affirms', '_a6i_affirms',
        '_a6p_paragraph', '_a6i_paragraph'}
ns = {'re': re}
for n in t.body:
    name = n.name if isinstance(n, ast.FunctionDef) else (
        n.targets[0].id if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Name) else None)
    if name in want:
        exec(compile(ast.Module([n], []), 'guard', 'exec'), ns)
assert want <= set(ns), want - set(ns)
for label, path in (('D', sys.argv[2]), ('edited', sys.argv[3])):
    rd = ' '.join(open(path, encoding='utf-8').read().split())
    p, i = ns['_a6p_paragraph'](rd), ns['_a6i_paragraph'](rd)
    print('%-6s A6P slice %6d chars, affirms=%s; A6I slice %6d chars, affirms=%s' % (
        label, len(p), ns['_a6p_affirms'](p), len(i), ns['_a6i_affirms'](i)))
