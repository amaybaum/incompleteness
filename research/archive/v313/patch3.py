p = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/v313/retire.py'
t = open(p).read()
old = '''    """Comment-only paragraphs at D whose code is gone: a comment-only paragraph describes the code
    that follows it up to the next comment-only paragraph; when that code holds at least one line and
    every one of its lines is dropped, the paragraph goes too."""'''
new = '''    """Comment-only paragraphs at D whose code is gone: a comment-only paragraph describes the code
    that follows it up to the next comment-only paragraph or the next section header, a comment line
    opening `# ----` or `# ====`; when that code holds at least one line and every one of its lines
    is dropped, the paragraph goes too."""'''
assert t.count(old) == 1
t = t.replace(old, new)
old = '''        code = []
        for m in range(k + 1, len(paras)):
            if only[m]:
                break
            code += [i for i in paras[m] if not lines[i - 1].strip().startswith('#')]
'''
new = '''        code = []
        for m in range(k + 1, len(paras)):
            if only[m]:
                break
            stop = False
            for i in paras[m]:
                s = lines[i - 1].strip()
                if s.startswith('# ----') or s.startswith('# ===='):
                    stop = True
                    break
                if not s.startswith('#'):
                    code.append(i)
            if stop:
                break
'''
assert t.count(old) == 1
t = t.replace(old, new)
open(p, 'w').write(t)
