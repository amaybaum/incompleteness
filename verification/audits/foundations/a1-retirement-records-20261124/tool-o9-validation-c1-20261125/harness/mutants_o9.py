"""Mutants of design amendment r4 (O-9): O9-m1 to O9-m17 of A.10. (id, file under tools/, [(old, new), ...], rule)."""
RC = 'ledger_coverage/engine/reconcile.py'
EX = 'ledger_coverage/engine/execution.py'

MUTANTS = [
    ('O9-m1', RC, [("        for p in sorted(set(e_f) | set(e_m)):\n            if p not in e_m:",
                    "        for p in sorted(e_m):\n            if p not in e_m:")],
     'A.5 omitted for paths of F absent at M: only the H-to-M scan finds the directory\'s files (O9-4)'),
    ('O9-m2', RC, [("    return path.startswith(d + '/')", "    return path.startswith(d)")],
     'the shared membership predicate without the trailing / (O9-6)'),
    ('O9-m3', RC, [("        if e_h:\n            self._stop('D2'", "        if False:\n            self._stop('D2'")],
     'D2 removed (O9-11)'),
    ('O9-m4', RC, [("        self.authorized = self.d in tuple(authorized)", "        self.authorized = True")],
     'the authority check (A.3) removed (O9-16)'),
    ('O9-m5', RC, [("            if mf != mm or of != om:", "            if of != om:")],
     'mode not compared (O9-8, mode case)'),
    ('O9-m6', RC, [("        e_f = {p: e for p, e in repo.entries(F).items() if inside(self.d, p)}",
                    "        e_f = {p: e for p, e in repo.entries(H).items() if inside(self.d, p)}")],
     'the entries at M compared with H instead of F (O9-1)'),
    ('O9-m7', RC, [("            if p in ledgered or in_corpus(p) or any(p.startswith(x) for x in prefixes) or p.startswith('.github/'):",
                    "            if False:")],
     'D3 removed (O9-12)'),
    ('O9-m8', RC, [("    return all(c not in ('', '.', '..') for c in path.split('/'))", "    return True")],
     'the clean-path test removed (O9-7)'),
    ('O9-m9', RC, [("    if cid is not None or named or not active:", "    if cid is not None or not active:")],
     'A.6 row 2 bypassed: the rule applied when a class pin names the path but differs (O9-13)'),
    ('O9-m10', RC, [("            (mf, of), (mm, om) = e_f[p], e_m[p]\n",
                     "            (mf, of), (mm, om) = e_f[p], e_m[p]\n            self.repo.read(self.F, p), self.repo.read(self.M, p)\n")],
     'A.5 reads bytes before checking the entry type (O9-8, symbolic link and submodule cases)'),
    ('O9-m11', RC, [("    if rd is not None and rd.active and rd.unequal:\n        r11 = False\n", "")],
     'R11 uses the classifier without A.5 (O9-19)'),
    ('O9-m12', RC, [("        if any(isinstance(c, dict) and c.get('id') == record_directory_class for c in classes):",
                     "        if False:")],
     'D5 removed (O9-17, O9-24)'),
    ('O9-m13', EX, [("            for path, why in sorted(rd.unequal.items()):\n",
                     "            for path, why in sorted(rd.unequal.items()):\n"
                     "                if self.repo.entries(M).get(path, ('',))[0] in ('100644', '100755') and \\\n"
                     "                        rc.classify_side(self.repo, M, path, self.side_classes, getattr(self, 'record_refs', {}))[0]:\n"
                     "                    continue\n")],
     'A.5\'s items suppressed for a path a matching class pin classifies (O9-21)'),
    ('O9-m14', RC, [("    if active and inside(rd.d, path):\n        e = repo.entries(M).get(path)",
                     "    if False:\n        e = repo.entries(M).get(path)")],
     'a non-regular entry inside D passed to the existing classifier (O9-8, full-path cases)'),
    ('O9-m15', RC, [("            if e_h:\n                self.state = 'inactive: unauthorized, present at H'\n                return\n", "")],
     'the authority ERROR raised for an unauthorized D that H holds (O9-25)'),
    ('O9-m16', RC, [("            if not e_m:\n                self.state = 'inactive: unauthorized, absent on M'\n                return\n"
                     "            if e_h:\n                self.state = 'inactive: unauthorized, present at H'\n                return\n", "")],
     'the authority ERROR raised whenever D is unauthorized, whatever M holds (O9-22)'),
    ('O9-m17', RC, [("            self._stop('authority', 'the configuration\\'s directory is not an authorized record directory, is absent '\n"
                     "                                    'at H and appears on M')",
                     "            self.state = 'inactive'\n            return")],
     'the authority ERROR removed for an unauthorized D absent at H and present on M (O9-16)'),
]
