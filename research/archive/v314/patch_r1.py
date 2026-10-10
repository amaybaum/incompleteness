p = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/v314/retire.py'
t = open(p).read()
def rep(old, new, n=1):
    global t
    assert t.count(old) == n, (t.count(old), old[:80])
    t = t.replace(old, new)

# 1. the emptied-block rule: collapse only a block the transformation actually removed content from
rep('''            arms = [v for f, v in body_lists(n) if f != 'body']
            if all(gone(s, removed) for s in n.body) and all(gone(s, removed) for v in arms for s in v):
                removed.add(n)
                grown = True''',
'''            arms = [v for f, v in body_lists(n) if f != 'body']
            if all(gone(s, removed) for s in n.body) and all(gone(s, removed) for v in arms for s in v) \\
                    and any(x in removed for x in ast.walk(n) if x is not n):
                removed.add(n)
                grown = True''')
rep('''def emptied(src, removed):
    """Compound statements every statement of whose body is removed, and whose other arms are
    removed or empty: remove them too.''',
'''def emptied(src, removed):
    """Compound statements the transformation removed content from, every statement of whose body is
    removed, and whose other arms are removed or empty: remove them too. A block whose statements
    are only `continue`, `break` or `pass` and from which nothing was removed is kept: it is the
    code, not the residue of a removal (V3-13's five damaged sites).''')
rep('''def gone(s, removed):
    """A statement that is removed, or that is only control flow once the removed are gone:
    continue, break or pass, or an if whose arms hold nothing else."""''',
'''def gone(s, removed):
    """A statement that is removed, or that is only control flow once the removed are gone:
    continue, break or pass, or an if whose arms hold nothing else. Used only for a block the
    transformation removed content from (emptied)."""''')
open(p, 'w').write(t)
