"""Mutants of the 65650298 checker. Usage: make_mutants4.py <checks.py> <outdir>"""
import os, sys
src = open(sys.argv[1]).read()
M = {
 'BASE4': [],
 'S2_TRUE_FN': [("        return support(sub) == WORLDS\n", "        return True\n")],
 'S2_LEN_FN': [("        return len({(pool[l], w[l]) for l in sub})\n", "        return len(list(sub))\n")],
 'S2_TRUE_CALLSITE': [("    s2 = bijective(lanes)\n", "    s2 = True\n")],
 'CELLS_TRUE': [("        return ok, n_cells\n", "        return True, n_cells\n")],
 'X4_IDENT': [("    alias = [(l & ~(7 << 12)) | (((l >> 9) & 7) << 12) for l in lanes]\n", "    alias = list(lanes)\n")],
 'NONUNIF_REC': [("zip(vals[PORT, TAIL[0]], vals[PORT, TAIL[1]], vals[PORT, TAIL[2]])]",
                  "zip(vals[PORT, TAIL[0]], vals[PORT, TAIL[1]], [v & 6 for v in vals[PORT, TAIL[2]]])]")],
 'C1_NOG': [("    pool = [(a << 6) | (b << 3) | c for a, b, c in zip(q8, q10, mm)]\n",
             "    pool = [(a << 6) | (b << 3) | c for a, b, c in zip(q8, q10, mm)]\n    w = [l >> 9 for l in lanes]\n")],
 'M1b_both': [("        return var_planes(9+3*TAIL_SITES.index(x))", "        return const_planes(0)"),
              ("cur[bank_site(t)] = (lane >> (9+3*i)) & 7", "cur[bank_site(t)] = 0")],
 'X3_PIN': [("dup = [l for l in lanes if (l >> 12) & 7 == (l >> 9) & 7]", "dup = [l for l in lanes if (l >> 12) & 7 == 0]")],
 'READ_DROP': [(", 'q9+y': (0, S+1, 77)}", "}")],
 'S3_J_TAIL': [("j = (s, comp(a8, 1), comp(a10, 2), comp(a10, 1))",
                "j = (s, comp(a8, 1) ^ ((l >> 9) & 1), comp(a10, 2), comp(a10, 1))")],
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
