p = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/v313/retire.py'
t = open(p).read()
old = "ORPHAN = '# The mandated execution base: '\n"
new = """ORPHAN = '# The mandated execution base: '
# comment lines naming a drift control whose code the census retires, which open a mixed paragraph
# and so fall to neither comment rule
DRIFT_LINES = (
    '# the drift control: one byte appended to the frozen file, every other file read normally',
    '# the two drift controls: one byte appended to one frozen file, every other file read normally')
"""
assert t.count(old) == 1
t = t.replace(old, new)
old = """        if para[0].startswith(ORPHAN):
            pass
"""
new = """        if para[0].startswith(ORPHAN):
            pass
        elif para == [para[0]] and para[0] in DRIFT_LINES:
            pass
"""
assert t.count(old) == 1
t = t.replace(old, new)
open(p, 'w').write(t)
