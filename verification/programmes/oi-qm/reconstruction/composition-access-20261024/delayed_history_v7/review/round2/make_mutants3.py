"""Mutants of the 98cf4647 checker. Usage: make_mutants3.py <checks.py> <outdir>"""
import os, sys
src = open(sys.argv[1]).read()
M = {
 'BASE3': [],
 # s2 statistic forced to pass (support treated as WORLDS).
 'S2_TRUE': [("    s2 = len(set(zip(pool, w))) == WORLDS\n", "    s2 = True\n")],
 # s2 statistic computed on the lane list length (always WORLDS).
 'S2_LEN': [("    s2 = len(set(zip(pool, w))) == WORLDS\n", "    s2 = len(list(zip(pool, w))) == WORLDS\n")],
 # cell comparator always True.
 'CELLS_TRUE': [("        return ok, n_cells\n", "        return True, n_cells\n")],
 # tail record non-uniform but carrier-independent.
 'NONUNIF_REC': [("zip(vals[PORT, TAIL[0]], vals[PORT, TAIL[1]], vals[PORT, TAIL[2]])]",
                  "zip(vals[PORT, TAIL[0]], vals[PORT, TAIL[1]], [v & 6 for v in vals[PORT, TAIL[2]]])]")],
 # record carries no G (raw tail bank): does x4 still pass?
 'C1_NOG': [("    pool = [(a << 6) | (b << 3) | c for a, b, c in zip(q8, q10, mm)]\n",
             "    pool = [(a << 6) | (b << 3) | c for a, b, c in zip(q8, q10, mm)]\n    w = [l >> 9 for l in lanes]\n")],
 # bank mask dropped in both engines: does x4 still pass?
 'M1b_both': [("        return var_planes(9+3*TAIL_SITES.index(x))", "        return const_planes(0)"),
              ("cur[bank_site(t)] = (lane >> (9+3*i)) & 7", "cur[bank_site(t)] = 0")],
 # alias map replaced by identity: x4 must fail.
 'X4_IDENT': [("    alias = [(l & ~(7 << 12)) | (((l >> 9) & 7) << 12) for l in lanes]\n", "    alias = list(lanes)\n")],
}
for name, reps in M.items():
    t = src
    for a, b in reps:
        if t.count(a) != 1:
            raise SystemExit(f'{name}: {t.count(a)}')
        t = t.replace(a, b)
    d = os.path.join(sys.argv[2], name); os.makedirs(os.path.join(d, 'run'), exist_ok=True)
    open(os.path.join(d, 'checks.py'), 'w').write(t)
    print(name)
