"""Scratch: mutants of census.py that its self-test must reject. Never landed."""
import subprocess, sys
S = open(sys.argv[1]).read()
M = [
 ("muts = [m for m in self.muts.get(name, []) if start <= m.lineno < line and m not in ds]", "muts = []", 'in-place mutations ignored'),
 ("            if isinstance(a, (ast.If, ast.While, ast.IfExp)):\n                out.append(a.test)", "            if False:\n                out.append(a.test)", 'enclosing tests ignored'),
 ("        elif isinstance(n, ast.Expr) and g.mutated(n) in names:\n            out.append(n)", "        elif False:\n            out.append(n)", 'table appends not predicates'),
 ("        if fname and cn in self.rp.get(fname, {}):", "        if False:", 'reader-parameter defaults ignored'),
 ("                elif isinstance(d, ast.For) and isinstance(d.target, ast.Name) and \\\n                        isinstance(d.iter, (ast.Tuple, ast.List)):", "                elif False:", 'literal loop iterables not evaluated'),
 ("        if getattr(n, 'lineno', None) is None or n.lineno in g.func_lines or \\\n                n.lineno >= chk['line']:", "        if getattr(n, 'lineno', None) is None or n.lineno in g.func_lines or \\\n                n.lineno >= chk['line'] or n.lineno < chk['line'] - 12:", 'predicates only near their check'),
 ("    if hist:\n        return 'retire-history', 'history'", "    if False:\n        return 'retire-history', 'history'", 'history ignored'),
 ("    if reads and 'UNRESOLVED' not in reads and all(covered(p, pop) for p in reads):", "    if reads and all(covered(p, pop) or p == 'UNRESOLVED' for p in reads):", 'unresolved counted as covered'),
 ("        if isinstance(n, ast.Attribute) and n.attr == 'environ':\n            k.add('env')", "        if False:\n            k.add('env')", 'host environment ignored'),
 ("            if ast.unparse(n.func) in OPAQUE:", "            if False:", 'child processes treated as reading nothing'),
 ("            out.append(d)\n            if isinstance(d, (ast.Assign, ast.AnnAssign, ast.For, ast.With)) and \\\n                    self.parent.get(d) is self.tree:\n                break", "            out.append(d)\n            break", 'only the latest definition reaches'),
 ("            if isinstance(m, ast.Name) and isinstance(m.ctx, ast.Load) and m.id not in local:\n                k = self.resolve(m.id, scope)", "            if isinstance(m, ast.Name) and isinstance(m.ctx, ast.Load) and m.id not in local \\\n                    and isinstance(self.parent.get(m), ast.Call) and self.parent[m].func is m:\n                k = self.resolve(m.id, scope)", 'only called names reach functions'),
 ("        return name if f is not None and self.parent.get(f) is self.tree else None", "        return next((k for k, v in self.funcs.items() if v.name == name), None)", 'any function of the name, whatever its scope'),
 ("            if fname and isinstance(n.func, ast.Name) and n.func.id in self.rebound[fname] and \\", "            if False and fname and isinstance(n.func, ast.Name) and n.func.id in self.rebound[fname] and \\", 'calls of rebound names ignored'),
]
bad = 0
for a, b, name in M:
    if S.count(a) != 1:
        print('ANCHOR  %s  (%d occurrences)' % (name, S.count(a))); bad += 1; continue
    open('/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/v312/mut.py', 'w').write(S.replace(a, b))
    r = subprocess.run([sys.executable, '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/v312/mut.py', '--self-test'], capture_output=True, text=True)
    last = r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr.strip()[-120:]
    print('MUTANT  %-44s exit %d  %s' % (name, r.returncode, last))
    bad += r.returncode == 0
print('MUTANTS  %d of %d rejected' % (len(M) - bad, len(M)))
