p = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/v314/rd/preserve.py'
t = open(p).read()
def rep(old, new, n=1):
    global t
    assert t.count(old) == n, (t.count(old), old[:80])
    t = t.replace(old, new)
rep("""  S4  regression: the six statements V3-13's transformation deleted are in no splice.
""", """  S4  regression: the seven statements V3-13's transformation deleted from code it retained are in
      no splice;
  S5  surviving blocks: inside every module-level `for`, `while`, `if`, `with` or `try` whose first
      line lies in no splice, every statement that lies wholly in splices, with its enclosing
      statement not, is a predicate the census retires, one of the amendment's, a counter
      increment (`x += <int>`), or a block holding at least one such predicate and nothing but
      such predicates, counter increments and control flow. Dead code is never removed from a
      block that survives.
""")
rep("""the check named: for each regression site the statement deleted through a consistent splice (S3 or
S2, and S4);""", """the check named: for each regression site the statement deleted through a consistent splice (S2,
S3 or S5, and S4);""")
rep("""# the six statements V3-13's transformation deleted from code it retained: D line, exact text
REGRESSION = (""", """# the seven statements V3-13's transformation deleted from code it retained: D line, exact text
REGRESSION = (""")
rep("""    ((193, '                break'),),
""", """    ((193, '                break'),),
    ((292, '                changed = True'),),
""")
rep("""    # S4
    bad = [l for site in REGRESSION for l, txt in site if lines[l - 1] != txt or l in gone]
    res.append(('S4', not bad, '%d regression site(s) preserved%s' % (
        len(REGRESSION) - len({s for s in REGRESSION for l, _t in s if l in bad}),
        ('; lines ' + ', '.join(map(str, bad))) if bad else '')))
    return res
""", """    # S4
    bad = [l for site in REGRESSION for l, txt in site if lines[l - 1] != txt or l in gone]
    res.append(('S4', not bad, '%d regression site(s) preserved%s' % (
        len(REGRESSION) - len({s for s in REGRESSION for l, _t in s if l in bad}),
        ('; lines ' + ', '.join(map(str, bad))) if bad else '')))
    # S5
    retired = set()
    for row in census['predicates']:
        if row[2] in RETIRE or disp[row[0]] == 'removed whole' or \\
                amend.get((row[0], row[1])) == row[6]:
            retired.add(row[1])

    def whole(n):
        return set(range(n.lineno, n.end_lineno + 1)) <= gone

    def counter(n):
        return isinstance(n, ast.AugAssign) and isinstance(n.op, ast.Add) and \\
            isinstance(n.value, ast.Constant) and isinstance(n.value.value, int)

    def residue(n):
        simple = [x for x in ast.walk(n) if isinstance(x, ast.stmt) and not isinstance(
            x, (ast.For, ast.While, ast.If, ast.With, ast.Try))]
        return any(x.lineno in retired for x in simple) and all(
            x.lineno in retired or counter(x) or isinstance(
                x, (ast.Continue, ast.Break, ast.Pass)) for x in simple)
    bad, blocks = [], 0
    for top in tree.body:
        if not isinstance(top, (ast.For, ast.While, ast.If, ast.With, ast.Try)) or top.lineno in gone:
            continue
        blocks += 1
        for n in ast.walk(top):
            if n is top or not isinstance(n, ast.stmt) or not whole(n):
                continue
            if parent.get(n) is not top and isinstance(parent.get(n), ast.stmt) and \\
                    whole(parent[n]):
                continue
            if not (n.lineno in retired or counter(n) or residue(n)):
                bad.append('%s at %d' % (type(n).__name__, n.lineno))
    res.append(('S5', not bad, '%d surviving module-level block(s), no dead code removed from '
                'them%s' % (blocks, ('; ' + ', '.join(bad[:4])) if bad else '')))
    return res
""")
rep("""        inside = any(lo in range(f.lineno, f.end_lineno + 1) for f in ast.walk(ast.parse(d_text))
                     if isinstance(f, ast.FunctionDef))
        expect('regression site %d deleted' % lo, led, aft, ['S3', 'S4'] + (['S2'] if inside else []))""",
"""        inside = any(lo in range(f.lineno, f.end_lineno + 1) for f in ast.walk(ast.parse(d_text))
                     if isinstance(f, ast.FunctionDef))
        flow = any(isinstance(x, (ast.Continue, ast.Break)) for x in ast.walk(ast.parse(d_text))
                   if isinstance(x, ast.stmt) and lo <= x.lineno <= hi)
        expect('regression site %d deleted' % lo, led, aft,
               ['S4'] + (['S2'] if inside else ['S5']) + (['S3'] if flow else []))""")
open(p, 'w').write(t)
