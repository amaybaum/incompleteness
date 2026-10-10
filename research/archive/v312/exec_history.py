#!/usr/bin/env python3
"""Scratch: which guard functions EXECUTE a history read (a git subprocess, the host environment, or
protocol seal state), by AST and fixpoint over calls; then which predicates of guard.json execute one,
directly or through the module-level values they read. Never landed."""
import ast, json, sys, re
SRC = open(sys.argv[1], encoding='utf-8').read()
LINES = SRC.split('\n')
T = ast.parse(SRC)
FUNCS = {n.name: n for n in ast.walk(T) if isinstance(n, ast.FunctionDef)}
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
        if isinstance(n, ast.Subscript) and isinstance(n.value, ast.Attribute) and n.value.attr == 'environ':
            k.add('env')
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr == 'get' \
                and isinstance(n.func.value, ast.Attribute) and n.func.value.attr == 'environ':
            k.add('env')
        if isinstance(n, ast.Name) and n.id in STATE_NAMES:
            k.add('state')
        if isinstance(n, ast.Constant) and isinstance(n.value, str) and 'verification/seals' in n.value:
            k.add('seals-path')
    return k

calls = {k: {n.func.id for n in ast.walk(v) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in FUNCS} for k, v in FUNCS.items()}
kinds = {k: direct_kinds(v) for k, v in FUNCS.items()}
changed = True
while changed:
    changed = False
    for k in FUNCS:
        new = set(kinds[k])
        for c in calls[k]:
            new |= kinds[c]
        if new != kinds[k]:
            kinds[k] = new; changed = True
json.dump({k: sorted(v) for k, v in kinds.items() if v}, open('func_history.json', 'w'), indent=1)
print(len([k for k in kinds if kinds[k]]), 'of', len(FUNCS), 'functions execute a history/state read')
for kk in ('git', 'env', 'state', 'seals-path'):
    print(kk, sum(1 for v in kinds.values() if kk in v))
