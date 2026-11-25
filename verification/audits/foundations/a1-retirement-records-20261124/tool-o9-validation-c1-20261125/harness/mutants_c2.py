"""Mutants of correction 2 (4f4a9d58): the EI6 predicate's new parts. (id, file under tools/, [(old, new), ...], rule)."""
CC = 'ledger_coverage/adapters/conformance_controls.py'

MUTANTS = [
    ('D01', CC, [("    if any(rf == i or rf.startswith(i + os.sep) for i in installed):\n        return False\n    for s in stdlib:\n        if rf.startswith(s + os.sep) and not any(n in INSTALLED_NAMES for n in rf[len(s) + 1:].split(os.sep)[:-1]):\n            return True\n    return False",
                  "    return any(rf.startswith(s + os.sep) for s in stdlib)")],
     'R-B1: EI6\'s predicate as at 3184c7f9 (a prefix test on the -I -S path)'),
    ('D02', CC, [("    if any(rf == i or rf.startswith(i + os.sep) for i in installed):\n        return False\n", "")],
     'R-B1: the installed-package directories are excluded by real path (redundant with the name rule on this layout)'),
    ('D03', CC, [("        if rf.startswith(s + os.sep) and not any(n in INSTALLED_NAMES for n in rf[len(s) + 1:].split(os.sep)[:-1]):",
                  "        if rf.startswith(s + os.sep):")],
     'R-B1: a site-packages or dist-packages directory inside a standard-library directory is refused'),
]
