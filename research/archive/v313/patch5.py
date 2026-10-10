p = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/v313/retire.py'
t = open(p).read()
old = '''        elif m and m.group(2) == ':' and m.group(1) in headers:
            out.extend(headers[m.group(1)].split('\\n'))
            done.add(m.group(1))
        elif m and m.group(1) in emptied:
            pass
'''
new = '''        elif m and m.group(2) == ':' and m.group(1) in headers:
            out.extend(headers[m.group(1)].split('\\n'))
            done.add(m.group(1))
        elif m and m.group(1) in emptied:
            pass
        elif para[0] in headers:
            if headers[para[0]]:
                out.extend(headers[para[0]].split('\\n'))
            done.add(para[0])
'''
assert t.count(old) == 1
t = t.replace(old, new)
open(p, 'w').write(t)
