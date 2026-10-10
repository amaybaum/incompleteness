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


def insert_in_section(text, marker, decl):
    """Insert a declaration just before the section marker `marker`."""
    i = text.index(marker)
    return text[:i] + decl + '\n\n' + text[i:]


def append_end(text, decl):
    """Insert a declaration at the end of §C, before `end OddChar`."""
    return replace_once(text, '\nend OddChar\n', '\n' + decl + '\n\nend OddChar\n')


def verdict_of(mod2, landed=None):
    return verdicts(mod2, LANDED if landed is None else landed)
