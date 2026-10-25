import sys, os
src = open(sys.argv[1]).read()
M = {
 'M1_drop_bank_mask': ("        return var_planes(9+3*TAIL_SITES.index(x))", "        return const_planes(0)"),
 'M2_shift_tail_lower_bound': ("        lo, hi = max(deadlines[i], L)+1, H2", "        lo, hi = max(deadlines[i], L)-76, H2"),
 'M3_remove_carrier_site': ("                 'q9+x': (1, S, 77), 'q9-y': (0, S-1, 77), 'q9+y': (0, S+1, 77)}", "                 'q9+x': (1, S, 77), 'q9-y': (0, S-1, 77)}"),
 'M4_x3_pinned_not_duplicated': ("    dup = [l for l in lanes if (l >> 12) & 7 == (l >> 9) & 7]", "    dup = [l for l in lanes if (l >> 12) & 7 == 0]"),
 'M5_drop_old_local_term_bitsliced': ("            layer[x] = (oa ^ ha, ob ^ hb, od ^ hd)", "            layer[x] = (ha, hb, hd)"),
 'M6_native_q8_as_carrier': ("    q8, q10, mm = vals[Q8, NS+1], vals[Q10, NS+1], vals[MM, NS+1]", "    q8, q10, mm = vals[Q8, HS], vals[Q10, NS+1], vals[MM, NS+1]"),
}
for name, (a, b) in M.items():
    assert src.count(a) == 1, name
    d = os.path.join(sys.argv[2], name); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'checks.py'), 'w').write(src.replace(a, b))
    print(name)
