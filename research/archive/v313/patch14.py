p = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/v313/rd/retire.py'
t = open(p).read()
old = """def main():
    guard, census_path, outpath = sys.argv[1:4]
    messages = json.load(open(sys.argv[4], encoding='utf-8')) if len(sys.argv) > 4 else {}
    headers = json.load(open(sys.argv[5], encoding='utf-8')) if len(sys.argv) > 5 else {}
"""
new = """def main():
    argv = sys.argv[1:]
    amendment = AMENDMENT
    if argv[:1] == ['--census-only']:
        argv, amendment = argv[1:], ()
    guard, census_path, outpath = argv[0:3]
    messages = json.load(open(argv[3], encoding='utf-8')) if len(argv) > 3 else {}
    headers = json.load(open(argv[4], encoding='utf-8')) if len(argv) > 4 else {}
"""
assert t.count(old) == 1; t = t.replace(old, new)
old = "    amended = {(c, l): h for c, l, h, _why in AMENDMENT}\n"
new = "    amended = {(c, l): h for c, l, h, _why in amendment}\n"
assert t.count(old) == 1; t = t.replace(old, new)
old = "Usage: retire.py <guard at D> <census.json> <output guard> [<messages.json> [<headers.json>]]\n"
new = """Usage: retire.py [--census-only] <guard at D> <census.json> <output guard> [<messages.json>
                 [<headers.json>]]

--census-only applies the census's classes without AMENDMENT: the 1,610 transformation, against
which controls.py measures the amendment's two self-satisfying predicates.
"""
assert t.count(old) == 1; t = t.replace(old, new)
open(p, 'w').write(t)
