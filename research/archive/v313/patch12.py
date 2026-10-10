p = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/v313/rd/retire.py'
t = open(p).read()
old = "RETIRE = {'redundant', 'retire-history', 'retire-machinery', 'retire-whole'}\n"
new = """RETIRE = {'redundant', 'retire-history', 'retire-machinery', 'retire-whole'}
# V3-13's amendment to V3-12's census: six predicates the census classes `retain`, reclassified by
# the owner's direction and retired with the census's 1,610. Each is named by check, line at D and
# the census's text hash, which must match the census row; V3-12's census is not edited.
AMENDMENT = (
    # the resolver could not resolve the record reader's path, so the census kept these as
    # unresolved; they read round PC4's seal record and nothing else (controls.py pc4s), a record
    # legacy-records pins
    ('R7-PC4S', 17854, '1459be91d4a5bcbb', 'legacy-seal-read'),
    ('R7-PC4S', 17999, 'cfaf77fc616d9bc3', 'legacy-seal-read'),
    ('R7-PC4S', 18000, '2e5e128c60b1684a', 'legacy-seal-read'),
    ('R7-PC4S', 18001, '3a685893e4885af0', 'legacy-seal-read'),
    # each looks for strings in the guard's own source that, after the census's retirements, occur
    # only in its own literals, so it holds whatever the rest of the guard says (controls.py vacuity)
    ('R7-OLT', 24113, '27f4b1d56c51ac71', 'self-satisfying'),
    ('R7-OLN', 24549, '2175b51bb131cb5f', 'self-satisfying'),
)
"""
assert t.count(old) == 1
t = t.replace(old, new)
old = """    removed, keep_texts, retained = set(), collections.Counter(), []
    for row in census['predicates']:
        chk, line, cls, sha = row[0], row[1], row[2], row[6]
        cands = [n for n in by_line[line] if sha16(n) == sha]
        if len(cands) != 1:
            raise SystemExit('retire: %s line %d does not match its text hash' % (chk, line))
        n = cands[0]
        if cls in RETIRE or (disp[chk] == 'removed whole'):
            removed.add(n)
        else:
            keep_texts[(chk, ast.unparse(n))] += 1
            retained.append(n)
"""
new = """    removed, keep_texts, retained = set(), collections.Counter(), []
    amended = {(c, l): h for c, l, h, _why in AMENDMENT}
    tally = collections.Counter()
    for row in census['predicates']:
        chk, line, cls, sha = row[0], row[1], row[2], row[6]
        cands = [n for n in by_line[line] if sha16(n) == sha]
        if len(cands) != 1:
            raise SystemExit('retire: %s line %d does not match its text hash' % (chk, line))
        n = cands[0]
        if (chk, line) in amended:
            if cls != 'retain' or amended.pop((chk, line)) != sha:
                raise SystemExit('retire: amendment row %s %d is not a retained census row with '
                                 'its hash' % (chk, line))
            removed.add(n)
            tally['amendment'] += 1
        elif cls in RETIRE or (disp[chk] == 'removed whole'):
            removed.add(n)
            tally['census' if cls in RETIRE else 'structural'] += 1
        else:
            keep_texts[(chk, ast.unparse(n))] += 1
            retained.append(n)
            tally[cls] += 1
    if amended:
        raise SystemExit('retire: amendment rows not in the census: %s' % sorted(amended))
    print('retire: %d predicates retired, %d as the census classes them and %d by the amendment; '
          '%d retained; %d structural rows removed with emptied checks, %d kept'
          % (tally['census'] + tally['amendment'], tally['census'], tally['amendment'],
             tally['retain'], tally['structural'], tally['structural'] and 0 or 0)
          if False else
          'retire: %d predicates retired, %d as the census classes them and %d by the amendment; '
          '%d retained' % (tally['census'] + tally['amendment'], tally['census'],
                           tally['amendment'], tally['retain']))
    print('retire: structural rows: %d removed with the emptied checks, %d kept'
          % (tally['structural'], tally['structural-kept']))
"""
assert t.count(old) == 1
t = t.replace(old, new)
open(p, 'w').write(t)
