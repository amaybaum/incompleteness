"""List declarations (with namespace) of Lean files, and grep design files for their short names.

Usage: python3 -I decls.py --decls <file.lean>...            -> 'file:line fullname kind'
       python3 -I decls.py --uses <declfile> <design.lean>...  -> occurrences of short names as identifiers
"""
import re
import sys

KW = r'(?:def|theorem|lemma|abbrev|structure|inductive|class|instance|opaque|axiom|irreducible_def)'
DECL_RE = re.compile(r'^\s*(?:@\[[^\]]*\]\s*)?(?:(?:private|protected|noncomputable|nonrec|partial|unsafe|scoped|local)\s+)*(' + KW + r')\s+([^\s:({\[]+)')
NS_RE = re.compile(r'^\s*namespace\s+(\S+)')
SEC_RE = re.compile(r'^\s*(?:noncomputable\s+)?section\b\s*(\S*)')
END_RE = re.compile(r'^\s*end\b\s*(\S*)')


def strip_comments(text):
    out, i, n, depth = [], 0, len(text), 0
    while i < n:
        if text.startswith('/-', i):
            depth += 1; i += 2; continue
        if depth:
            if text.startswith('-/', i):
                depth -= 1; i += 2
            else:
                if text[i] == '\n':
                    out.append('\n')
                i += 1
            continue
        if text.startswith('--', i):
            j = text.find('\n', i)
            i = n if j < 0 else j
            continue
        out.append(text[i]); i += 1
    return ''.join(out)


def decls(path):
    text = strip_comments(open(path, encoding='utf-8').read())
    stack = []  # entries: ('ns', name) or ('sec', name)
    res = []
    for ln, line in enumerate(text.splitlines(), 1):
        m = NS_RE.match(line)
        if m:
            stack.append(('ns', m.group(1))); continue
        m = END_RE.match(line)
        if m and not line.strip().startswith('end_'):
            if stack:
                stack.pop()
            continue
        m = SEC_RE.match(line)
        if m and not DECL_RE.match(line):
            stack.append(('sec', m.group(1))); continue
        m = DECL_RE.match(line)
        if m:
            kind, name = m.group(1), m.group(2)
            ns = '.'.join(x for k, x in stack if k == 'ns')
            full = name[len('_root_.'):] if name.startswith('_root_.') else (ns + '.' + name if ns else name)
            res.append((path, ln, full, kind))
    return res


def main():
    if sys.argv[1] == '--decls':
        for p in sys.argv[2:]:
            for path, ln, full, kind in decls(p):
                print('%s:%d %s %s' % (path.rsplit('/', 1)[-1], ln, full, kind))
    elif sys.argv[1] == '--uses':
        names = {}
        for line in open(sys.argv[2], encoding='utf-8'):
            loc, full, kind = line.split()
            names.setdefault(full.rsplit('.', 1)[-1], []).append((full, loc))
        for p in sys.argv[3:]:
            text = strip_comments(open(p, encoding='utf-8').read())
            for ln, line in enumerate(text.splitlines(), 1):
                for tok in set(re.findall(r'[A-Za-z_][A-Za-z0-9_\'!?₀-₉]*(?:\.[A-Za-z_][A-Za-z0-9_\'!?₀-₉]*)*', line)):
                    last = tok.rsplit('.', 1)[-1]
                    if last in names:
                        print('%s:%d token %s matches %s' % (p.rsplit('/', 1)[-1], ln, tok,
                              '; '.join('%s (%s)' % x for x in names[last])))


if __name__ == '__main__':
    main()
