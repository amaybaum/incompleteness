p = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/v314/retire.py'
t = open(p).read()
def rep(old, new, n=1):
    global t
    assert t.count(old) == n, (t.count(old), old[:80])
    t = t.replace(old, new)
rep("""    mismatches = []
    rounds = 0
    while True:
        rounds += 1
        before = len(removed)
        dead, live = mark_sweep(src, removed, roots - removed)
        for x in dead:
            why.setdefault(x, 'dead-code')
        removed |= set(dead)
        for x in counters(src, removed, predicates, mismatches):
            why.setdefault(x, 'counter')
            removed.add(x)
        emptied(src, removed)
        if len(removed) == before:
            break
""", """    # dead code is removed to a fixpoint, but never from inside a module-level block that survives:
    # a statement there is kept, as a root, and the sweep is run again (V3-13's seventh damaged
    # site, a flag set late in a loop body and read by the loop's own condition)
    removed0, why0, protected = set(removed), dict(why), set()
    while True:
        removed, why, mismatches, rounds = set(removed0), dict(why0), [], 0
        while True:
            rounds += 1
            before = len(removed)
            dead, live = mark_sweep(src, removed, (roots | protected) - removed)
            for x in dead:
                why.setdefault(x, 'dead-code')
            removed |= set(dead)
            for x in counters(src, removed, predicates, mismatches):
                why.setdefault(x, 'counter')
                removed.add(x)
            emptied(src, removed)
            if len(removed) == before:
                break
        inner = {x for top in src.tree.body if isinstance(top, COMPOUND) and top not in removed
                 for x in ast.walk(top) if x is not top and x in removed and why.get(x) == 'dead-code'}
        if inner <= protected:
            break
        protected |= inner
    if protected:
        print('retire: %d statement(s) kept inside surviving module-level blocks' % len(protected))
""")
open(p, 'w').write(t)
