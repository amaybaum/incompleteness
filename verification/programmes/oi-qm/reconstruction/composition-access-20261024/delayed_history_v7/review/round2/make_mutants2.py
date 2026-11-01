"""First review's M1, M1b, M5, M6 re-applied to the candidate. Usage: make_mutants2.py <checks.py> <outdir>"""
import os, sys
src = open(sys.argv[1]).read()
M = {
 'R1_M1_drop_bank_mask_bitsliced': [("        return var_planes(9+3*TAIL_SITES.index(x))", "        return const_planes(0)")],
 'R1_M1b_drop_bank_mask_both': [("        return var_planes(9+3*TAIL_SITES.index(x))", "        return const_planes(0)"),
                                ("cur[bank_site(t)] = (lane >> (9+3*i)) & 7", "cur[bank_site(t)] = 0")],
 'R1_M5_drop_old_local_bitsliced': [("            layer[x] = (oa ^ ha, ob ^ hb, od ^ hd)", "            layer[x] = (ha, hb, hd)")],
 'R1_M6_native_q8_as_carrier': [("    q8, q10, mm = vals[Q8, NS+1], vals[Q10, NS+1], vals[MM, NS+1]", "    q8, q10, mm = vals[Q8, HS], vals[Q10, NS+1], vals[MM, NS+1]")],
}
INSTR = ("    positive = 0\n", "    print('CELLS', seed, s3, file=__import__('sys').stderr)\n    positive = 0\n")
for name, reps in M.items():
    t = src
    for a, b in [INSTR] + reps:
        if t.count(a) != 1:
            raise SystemExit(name)
        t = t.replace(a, b)
    d = os.path.join(sys.argv[2], name); os.makedirs(os.path.join(d, 'run'), exist_ok=True)
    open(os.path.join(d, 'checks.py'), 'w').write(t)
    print(name)
