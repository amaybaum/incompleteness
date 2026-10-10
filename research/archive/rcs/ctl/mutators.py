def must_fail(code, label, mods2, landed=None):
    before, count = list(FAILS), COUNT[0]
    saved = sys.stdout
    sys.stdout = io.StringIO()
    try:
        module_checks(mods2, landed=landed)
    finally:
        sys.stdout = saved
    new = FAILS[len(before):]
    del FAILS[len(before):]
    COUNT[0] = count
    check('M', 'mutation %s fails with %s' % (label, code), code in new)


def replace_once(text, a, b):
    assert text.count(a) == 1, a
    return text.replace(a, b, 1)


def mutate(mods, m, a, b):
    out = dict(mods)
    out[m] = replace_once(mods[m], a, b)
    return out


def append_decl(mods, m, decl):
    """Insert a declaration at the end of the module's namespace."""
    return mutate(mods, m, '\nend RelcSelect\nend OIBridge\n', '\n' + decl + '\n\nend RelcSelect\nend OIBridge\n')


def verdict_of(mods2, landed=None):
    return verdicts(mods2, LANDED if landed is None else landed)


def landed_with(key, a, b):
    lm = dict(LANDED)
    assert lm[key].count(a) >= 1, (key, a)
    lm[key] = lm[key].replace(a, b)
    return lm
