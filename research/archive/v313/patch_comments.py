p = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/v313/retire.py'
t = open(p).read()
old = """    text = src.delete([stmt_range(src, n) for n in removed] + [(k, k) for k in else_lines])
    text = comment_paragraphs(text)
"""
new = """    ranges = [stmt_range(src, n) for n in removed] + [(k, k) for k in else_lines]
    drop = {i for a, b in ranges for i in range(a, b + 1)}
    ranges += [(k, k) for k in attached_comments(src.lines, drop)]
    text = src.delete(ranges)
    text = comment_paragraphs(text, comment_only_paragraphs(text0))
"""
assert t.count(old) == 1
t = t.replace(old, new)
old = '''def comment_paragraphs(text):
    """Remove paragraphs (blank-line separated) consisting only of comments."""
    lines = text.split('\\n')
    out, para = [], []

    def flush():
        if para and all(l.strip().startswith('#') for l in para):
            return
        out.extend(para)
'''
new = '''def paragraphs(text):
    """The blank-line separated paragraphs of a text, each a list of lines."""
    out, para = [], []
    for l in text.split('\\n'):
        if l.strip() == '':
            if para:
                out.append(para)
            para = []
        else:
            para.append(l)
    if para:
        out.append(para)
    return out


def comment_only_paragraphs(text):
    """The paragraphs of a text that consist only of comments, as joined strings."""
    return {'\\n'.join(p) for p in paragraphs(text) if all(l.strip().startswith('#') for l in p)}


def attached_comments(lines, drop):
    """Comment lines whose code is gone: a block of comment lines at one indentation describes the
    code that follows it up to the next blank line, the next comment line at no deeper indentation,
    or a dedent; when that code holds at least one line and every one of its lines is dropped, the
    block goes too. Check headers, `# ---- ...`, are left to comment_paragraphs and the header
    texts."""
    out, i, n = set(), 0, len(lines)
    while i < n:
        s = lines[i]
        if not s.strip().startswith('#') or (i + 1) in drop:
            i += 1
            continue
        ind = len(s) - len(s.lstrip())
        j = i
        while j < n and lines[j].strip().startswith('#') and \\
                len(lines[j]) - len(lines[j].lstrip()) == ind:
            j += 1
        code, k = [], j
        while k < n:
            l = lines[k]
            if l.strip() == '':
                break
            li = len(l) - len(l.lstrip())
            if l.strip().startswith('#') and li <= ind:
                break
            if li < ind:
                break
            if not l.strip().startswith('#'):
                code.append(k + 1)
            k += 1
        if code and all(c in drop for c in code) and not s.lstrip().startswith('# ----'):
            out.update(range(i + 1, j + 1))
        i = j
    return out


def comment_paragraphs(text, at_d):
    """Remove the paragraphs (blank-line separated) that consist only of comments and did not at D:
    the comments whose code the transformation removed. A paragraph that was comment-only at D is
    kept."""
    lines = text.split('\\n')
    out, para = [], []

    def flush():
        if para and all(l.strip().startswith('#') for l in para) and '\\n'.join(para) not in at_d:
            return
        out.extend(para)
'''
assert t.count(old) == 1, 'second'
t = t.replace(old, new)
open(p, 'w').write(t)
