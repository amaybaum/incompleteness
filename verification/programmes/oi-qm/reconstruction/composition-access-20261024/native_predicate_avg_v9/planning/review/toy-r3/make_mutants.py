"""Reviewer probe: add direction-specific mutants to a COPY of the r3 design code.
Mutants (chosen before running, by the reviewer):
  rv_dir_ignore_fixed : -y tips ignore cover by fixed quantities (over-elimination, -y only)
  rv_dir_swap         : +y and -y tip labels swapped (labelling error; same tip set)
  rv_dir_wrong_far_y  : -y far tip at distance d instead of d-1 (over-elimination, -y only)
  rv_dir_cone_y       : cones lose their -y boundary shell cells (under-coverage, -y only)
  rv_blind_B_y        : -y tips treated as covered, B type only (over-retention)
  rv_blind_G_y        : -y tips treated as covered, convention G only (over-retention)
  rv_blind_plus_z     : +z tips treated as covered (port axis direction)
"""
import sys, re
d = sys.argv[1]
g = open(d + '/s0geom.py').read()
# extra rule fields
g = g.replace("nopar=False, symblind=False, blind_dir=None):",
              "nopar=False, symblind=False, blind_dir=None, rv=None):")
g = g.replace("        self.blind_dir = blind_dir      # mutant only: tips in this direction are treated as covered",
              "        self.blind_dir = blind_dir      # mutant only: tips in this direction are treated as covered\n        self.rv = rv")
g = g.replace("'blind_dir': None}", "'blind_dir': None, 'rv': None}")
# cone mutant
g = g.replace("""    if rr < 0 or r > rr:
        return False
    return rule.nopar""", """    if rr < 0 or r > rr:
        return False
    if rule.rv == 'cone_y' and r == rr and rr > 0 and uc[1] < c[1]:
        return False
    return rule.nopar""")
# tip label mutants
g = g.replace("""    out = [((e, 'near'), (vadd(c, e, d), near)) for e in AX]""",
"""    out = [((e, 'near'), (vadd(c, e, d), near)) for e in AX]
    if rule.rv == 'swap_y':
        sw = {(0, 1, 0): (0, -1, 0), (0, -1, 0): (0, 1, 0)}
        out = [((sw.get(e, e), 'near'), (vadd(c, e, d), near)) for e in AX]""")
g = g.replace("""        elif rule.far:
            out += [((e, 'far'), (vadd(c, e, d - 1), far)) for e in AX]""",
"""        elif rule.far:
            out += [((e, 'far'), (vadd(c, e, d - 1), far)) for e in AX]
            if rule.rv == 'wrong_far_y':
                out = [((lab, (vadd(c, lab[0], d), far)) if (len(lab) == 2 and lab == ((0, -1, 0), 'far')) else (lab, u))
                       for lab, u in out]
            if rule.rv == 'swap_y':
                sw = {(0, 1, 0): (0, -1, 0), (0, -1, 0): (0, 1, 0)}
                out = [(((sw.get(lab[0], lab[0]), 'far'), u) if lab[1] == 'far' else (lab, u)) for lab, u in out]""")
# closure: fixed-cover counts for ignore_fixed; type/convention-restricted blindness
g = g.replace("""    count = {u: 0 for u in all_tips}
    for q in allq:
        for u in covers[q]:
            count[u] += 1""", """    count = {u: 0 for u in all_tips}
    fcount = {u: 0 for u in all_tips}
    for q in allq:
        for u in covers[q]:
            count[u] += 1
            if q in fixed:
                fcount[u] += 1""")
g = g.replace("""            elif rule.blind_dir is not None and lab[0] == rule.blind_dir:
                st = 'covered'""", """            elif rule.blind_dir is not None and lab[0] == rule.blind_dir:
                st = 'covered'
            elif rule.rv == 'blind_B_y' and lab[0] == (0, -1, 0) and pair.depth(q)[1] == 'B':
                st = 'covered'
            elif rule.rv == 'blind_G_y' and lab[0] == (0, -1, 0) and pair.E == -1:
                st = 'covered'
            elif rule.rv == 'blind_plus_z' and lab[0] == (0, 0, 1):
                st = 'covered'
            elif rule.rv == 'ignore_fixed_y' and lab[0] == (0, -1, 0) and \\
                    count[u] - fcount[u] - (1 if u in covers[q] else 0) == 0:
                st = 'free'""")
open(d + '/s0geom.py', 'w').write(g)
c = open(d + '/s0controls.py').read()
c = c.replace("    'parity_dropped(equivalent)': G.Rule(nopar=True),",
"""    'rv_dir_ignore_fixed': G.Rule(rv='ignore_fixed_y'),
    'rv_dir_swap': G.Rule(rv='swap_y'),
    'rv_dir_wrong_far_y': G.Rule(rv='wrong_far_y'),
    'rv_dir_cone_y': G.Rule(rv='cone_y'),
    'rv_blind_B_y': G.Rule(rv='blind_B_y'),
    'rv_blind_G_y': G.Rule(rv='blind_G_y'),
    'rv_blind_plus_z': G.Rule(rv='blind_plus_z'),
    'parity_dropped(equivalent)': G.Rule(nopar=True),""")
open(d + '/s0controls.py', 'w').write(c)
