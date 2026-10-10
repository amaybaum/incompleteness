p = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/v313/retire.py'
t = open(p).read()
old = "    text = comments(text, headers)\n"
new = ("    text = comments(text, headers, {c for c, d in disp.items() if d == 'removed whole'})\n")
assert t.count(old) == 1
t = t.replace(old, new)
old = '''def comments(text, headers):
    """The comment paragraphs: each paragraph opening with ORPHAN -- the description of a base or
    seal constant that round SI-3 removed and whose comment it left -- deleted, and each
    retained check's header paragraph, `# ---- <tag>: ...`, replaced by its text in `headers`."""'''
new = '''def comments(text, headers, emptied):
    """The comment paragraphs: each paragraph opening with ORPHAN -- the description of a base or
    seal constant that round SI-3 removed and whose comment it left -- deleted; each check's header
    paragraph, `# ---- <tag>: ...`, replaced by its text in `headers`; and the header and end marker
    of every check removed whole, `# ---- <tag>: ...` and `# ---- <tag> ends.`, deleted when
    `headers` gives no text for it."""'''
assert t.count(old) == 1
t = t.replace(old, new)
old = '''        m = re.match(r'# ---- (R7-[A-Z0-9]+):', para[0])
        if para[0].startswith(ORPHAN):
            pass
        elif m and m.group(1) in headers:
            out.extend(headers[m.group(1)].split('\\n'))
            done.add(m.group(1))
'''
new = '''        m = re.match(r'# ---- (R7-[A-Z0-9]+)(:| ends\\.)', para[0])
        if para[0].startswith(ORPHAN):
            pass
        elif m and m.group(2) == ':' and m.group(1) in headers:
            out.extend(headers[m.group(1)].split('\\n'))
            done.add(m.group(1))
        elif m and m.group(1) in emptied:
            pass
'''
assert t.count(old) == 1, 'c'
t = t.replace(old, new)
open(p, 'w').write(t)
