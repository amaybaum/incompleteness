def must_fail(code, label, mod2):
    before, count = list(FAILS), COUNT[0]
    saved = sys.stdout
    sys.stdout = io.StringIO()
    try:
        module_checks(mod2)
    finally:
        sys.stdout = saved
    new = FAILS[len(before):]
    del FAILS[len(before):]
    COUNT[0] = count
    check('M', 'mutation %s fails with %s' % (label, code), code in new)


def replace_once(text, a, b):
    assert text.count(a) == 1, a
    return text.replace(a, b, 1)


def append_decl(text, decl):
    """Insert a declaration just before the verdict section (inside §P)."""
    i = text.index('\n/-! ### The verdict')
    return text[:i] + '\n' + decl + '\n' + text[i:]


def insert_before(text, anchor, decl):
    i = text.index(anchor)
    return text[:i] + decl + '\n\n' + text[i:]


