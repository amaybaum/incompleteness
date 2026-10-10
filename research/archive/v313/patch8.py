p = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/v313/retire.py'
t = open(p).read()
for old, new in (
    ("    unit_set = set(units)\n", ""),
    ("                name = st.target.id\n", ""),
    ("        if any(n in removed for n in []):\n            continue\n", ""),
    ("WHY = {}\n", ""),
    ("                WHY[d] = n\n", ""),
):
    assert t.count(old) == 1, old
    t = t.replace(old, new)
open(p, 'w').write(t)
