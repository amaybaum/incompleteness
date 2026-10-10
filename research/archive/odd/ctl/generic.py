IDENT = re.compile(r'(?<![\w.\'@])[A-Za-z_][\w\'.]*')
BINDER_OPEN, BINDER_CLOSE = '({[⦃', ')}]⦄'


def stmt_parts(texts, name):
    b, c = split_statement(texts.get(name, ''))
    return norm(b), norm(c)


def def_body(text):
    j = text.find(' :=')
    return norm(text[j + 3:]) if j != -1 else ''


def groups(b):
    """The top-level bracketed binder groups of a binder string, in order."""
    out, depth, start = [], 0, None
    for i, c in enumerate(b):
        if c in BINDER_OPEN:
            if depth == 0:
                start = i
            depth += 1
        elif c in BINDER_CLOSE:
            depth -= 1
            if depth == 0 and start is not None:
                out.append(norm(b[start:i + 1]))
                start = None
    return out


def group_names(g):
    """The bound names of a binder group (none for an anonymous instance group)."""
    inner = g[1:-1]
    j = inner.find(' : ')
    if j == -1:
        return []
    return inner[:j].split()


def scopes_at(text):
    """[(position, variable groups in scope, namespaces in scope, opened namespaces in scope)] at each declaration."""
    stack = [([], [], [])]
    out = {}
    lines = text.split('\n')
    pos = 0
    k = 0
    decl_at = {m.start(): m.group(2) for m in DECL.finditer(text)}
    while k < len(lines):
        line = lines[k]
        block = [line]
        j = k + 1
        if line.startswith('variable') or line.startswith('open '):
            while j < len(lines) and lines[j].startswith('  '):
                block.append(lines[j])
                j += 1
        whole = '\n'.join(block)
        m = re.match(r'^(namespace|section|noncomputable section)\b\s*(\S*)', line)
        if m:
            stack.append(([], [m.group(2)] if m.group(1) == 'namespace' else [], []))
        elif re.match(r'^end\b', line):
            if len(stack) > 1:
                stack.pop()
        elif line.startswith('variable'):
            stack[-1][0].extend(groups(whole[len('variable'):]))
        elif line.startswith('open '):
            stack[-1][2].extend(whole[len('open '):].split())
        if pos in decl_at:
            vs = [g for s in stack for g in s[0]]
            nss = [n for s in stack for n in s[1]]
            ops = [o for s in stack for o in s[2]]
            out[decl_at[pos]] = (vs, nss, ops)
        for l in block:
            pos += len(l) + 1
        k = j
    return out


def effective(text, name):
    """The effective statement of a declaration: the section variables its statement uses (closed under use by the
    included groups, an instance group included with a variable it mentions), in declared order, then its own binders
    and conclusion. None when the declaration is absent."""
    chunks = decl_chunks(text)
    if name not in chunks:
        return None
    stmt = chunks[name][1]
    vs = scopes_at(text).get(name, ([], [], []))[0]
    b, c = split_statement(stmt)
    used = norm(b) + ' : ' + norm(c)
    inc = [False] * len(vs)
    changed = True
    while changed:
        changed = False
        hay = used + ' ' + ' '.join(g for g, i in zip(vs, inc) if i)
        for n, g in enumerate(vs):
            if inc[n]:
                continue
            names = group_names(g)
            if names and any(token(x, hay) for x in names):
                inc[n] = True
                changed = True
            elif not names and g.startswith('[') and any(token(x, g) for gg, i in zip(vs, inc) if i
                                                          for x in group_names(gg)):
                inc[n] = True
                changed = True
    pre = ' '.join(g for g, i in zip(vs, inc) if i)
    return norm(pre + ' ' + norm(b) + ' : ' + norm(c))


_INV_CACHE = {}


def inventory(files):
    """{fully qualified name} of every declaration in the given module texts, with the namespaces they declare."""
    names, spaces = set(), set()
    for text in files:
        if text in _INV_CACHE:
            n, sp = _INV_CACHE[text]
            names |= n
            spaces |= sp
            continue
        n, sp = inventory_one(text)
        if len(_INV_CACHE) < 4096:
            _INV_CACHE[text] = (n, sp)
        names |= n
        spaces |= sp
    return names, spaces


def inventory_one(text):
    names, spaces = set(), set()
    for text in [text]:
        sc = scopes_at(text)
        for kind, name in decls(text):
            nss = sc.get(name, ([], [], []))[1]
            prefix = '.'.join(nss)
            names.add((prefix + '.' if prefix else '') + name)
            for i in range(1, len(nss) + 1):
                spaces.add('.'.join(nss[:i]))
    return names, spaces


def visible(nss, ops, spaces):
    """The namespaces whose members are in scope: every prefix of the current namespace, and each opened namespace,
    resolved against the current namespace prefixes when that names an OIBridge namespace."""
    out = [''] + ['.'.join(nss[:i]) for i in range(1, len(nss) + 1)]
    for o in ops:
        hit = [p + '.' + o for p in ['.'.join(nss[:i]) for i in range(len(nss), 0, -1)] if p + '.' + o in spaces]
        out.append(hit[0] if hit else o)
    return out


def resolve(tok, vis, names):
    return sorted({(v + '.' if v else '') + tok for v in vis} & names)


def top_colon(s):
    """Index of the first colon at bracket depth 0 that is not part of `:=`."""
    depth = 0
    for j, c in enumerate(s):
        if c in BINDER_OPEN:
            depth += 1
        elif c in BINDER_CLOSE:
            depth -= 1
        elif c == ':' and depth == 0 and s[j:j + 2] != ':=':
            return j
    return len(s)


def strip_binders(eff):
    """The identifiers of an effective statement, without the names it binds: the names of its binder groups and the
    names bound by `∃`, `∀` and `fun` in its conclusion."""
    k = top_colon(eff)
    bound = set()
    for g in groups(eff[:k]):
        bound.update(group_names(g))
    for m in re.finditer(r'(?:∃|∀|fun)\s+([^,:=]+?)\s*(?::|,|=>)', eff[k:]):
        bound.update(x for x in m.group(1).split() if re.match(r"^[A-Za-zΩ_][\w']*$", x))
    return [t for t in IDENT.findall(eff) if t not in bound]

