p = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/v313/rd/retire.py'
t = open(p).read()
a = t.index("        elif cls in RETIRE or (disp[chk] == 'removed whole'):")
b = t.index("    print('retire: structural rows:")
b = t.index('\n', t.index("% (tally['structural'], tally['structural-kept']))", b)) + 1
new = """        elif cls in RETIRE or (disp[chk] == 'removed whole'):
            removed.add(n)
            tally['census' if cls in RETIRE else 'structural removed'] += 1
        else:
            keep_texts[(chk, ast.unparse(n))] += 1
            retained.append(n)
            tally['retain' if cls == 'retain' else 'structural kept'] += 1
    if amended:
        raise SystemExit('retire: amendment rows not in the census: %s' % sorted(amended))
    print('retire: %d predicates retired, %d as the census classes them and %d by the amendment; '
          '%d retained' % (tally['census'] + tally['amendment'], tally['census'],
                           tally['amendment'], tally['retain']))
    print('retire: structural rows: %d removed with the emptied checks, %d kept'
          % (tally['structural removed'], tally['structural kept']))
"""
t = t[:a] + new + t[b:]
t = t.replace("""1. every predicate the census classes redundant, retire-history, retire-machinery or retire-whole
   removed, each identified by its line and the SHA-256 prefix of its unparsed text, which must
   match;""", """1. every predicate the census classes redundant, retire-history, retire-machinery or retire-whole
   removed, and the six of AMENDMENT, each identified by its line and the SHA-256 prefix of its
   unparsed text, which must match;""")
open(p, 'w').write(t)
