"""Reflow over-width prose blocks of a markdown file to <= 120 columns; tables, code, headings untouched."""
import re, sys, textwrap

W = 120
MARK = re.compile(r'^(\s*)(?:(> )|([-*] )|(\d+\. ))')


def prefix_of(line):
    m = MARK.match(line)
    if not m:
        ind = len(line) - len(line.lstrip(' '))
        return line[:ind], line[:ind]
    lead = m.group(0)
    if m.group(2):               # blockquote: continuation keeps the "> "
        return lead, lead
    return lead, ' ' * len(lead)


def reflow(text):
    lines = text.split('\n')
    out, i, fence = [], 0, False
    while i < len(lines):
        ln = lines[i]
        if ln.startswith('```'):
            fence = not fence
            out.append(ln); i += 1; continue
        if fence or not ln.strip() or ln.lstrip().startswith('|') or ln.startswith('#') or i == 0:
            out.append(ln); i += 1; continue
        first, cont = prefix_of(ln)
        block = [ln]
        j = i + 1
        while j < len(lines):
            nx = lines[j]
            if not nx.strip() or nx.startswith('```') or nx.lstrip().startswith('|') or nx.startswith('#'):
                break
            m = MARK.match(nx)
            if m and not m.group(2):          # a new list item starts a new block
                break
            if first.endswith('> ') and not nx.startswith(cont):
                break
            if not first.endswith('> ') and m and m.group(2):
                break
            block.append(nx); j += 1
        if max(len(b) for b in block) > W:
            words = ' '.join([block[0][len(first):]] + [b[len(cont):] if b.startswith(cont) else b.strip()
                                                        for b in block[1:]]).split()
            filled = textwrap.fill(' '.join(words), width=W, initial_indent=first, subsequent_indent=cont,
                                   break_long_words=False, break_on_hyphens=False)
            out.extend(filled.split('\n'))
        else:
            out.extend(block)
        i = j
    return '\n'.join(out)


for p in sys.argv[1:]:
    s = open(p, encoding='utf-8').read()
    r = reflow(s)
    assert ' '.join(r.split()) == ' '.join(s.split()), 'word sequence changed in ' + p
    open(p, 'w', encoding='utf-8').write(r)
    print('reflowed', p)
