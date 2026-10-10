p = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/v313/retire.py'
t = open(p).read()
old = """    ranges += [(k, k) for k in attached_comments(src.lines, drop)]
"""
new = """    ranges += [(k, k) for k in attached_comments(src.lines, drop)]
    ranges += [(k, k) for k in orphan_paragraphs(src.lines, drop)]
"""
assert t.count(old) == 1
t = t.replace(old, new)
old = '''def comment_paragraphs(text, at_d):'''
new = '''def orphan_paragraphs(lines, drop):
    """Comment-only paragraphs at D whose code is gone: a comment-only paragraph describes the code
    that follows it up to the next comment-only paragraph; when that code holds at least one line and
    every one of its lines is dropped, the paragraph goes too."""
    paras, cur = [], []
    for i, l in enumerate(lines, 1):
        if l.strip() == '':
            if cur:
                paras.append(cur)
            cur = []
        else:
            cur.append(i)
    if cur:
        paras.append(cur)
    only = [all(lines[i - 1].strip().startswith('#') for i in p) for p in paras]
    out = set()
    for k, p in enumerate(paras):
        if not only[k]:
            continue
        code = []
        for m in range(k + 1, len(paras)):
            if only[m]:
                break
            code += [i for i in paras[m] if not lines[i - 1].strip().startswith('#')]
        if code and all(i in drop for i in code):
            out.update(p)
    return out


def comment_paragraphs(text, at_d):'''
assert t.count(old) == 1
t = t.replace(old, new)
open(p, 'w').write(t)
