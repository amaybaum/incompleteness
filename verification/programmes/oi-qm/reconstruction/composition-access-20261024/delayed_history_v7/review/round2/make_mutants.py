"""Build mutants of checks.py. Usage: make_mutants.py <checks.py> <outdir>.

Each replacement must match exactly once. An instrumentation line printing the
s3 cell-comparison result to stderr is added to every mutant (and to a
baseline copy) so the cell check can be read separately from the TV check.
"""
import os
import sys

src_path, outdir = sys.argv[1], sys.argv[2]
with open(src_path) as fh:
    SRC = fh.read()

INSTR = [("    positive = 0\n",
          "    print('CELLS', seed, s3, file=__import__('sys').stderr)\n    positive = 0\n")]

MUTANTS = {
    'BASE': [],
    # x3: pinned (not duplicated) second tail triple.
    'X3_PIN': [("dup = [l for l in lanes if (l >> 12) & 7 == (l >> 9) & 7]",
                "dup = [l for l in lanes if (l >> 12) & 7 == 0]")],
    # x3: the TV statistic is blind (always 0).
    'X3_TVZERO': [("return F(acc_sum, 2*total), jt", "return F(0), jt")],
    # s3: selected carrier depends on a tail-bank bit.
    'S3_J_TAIL': [("j = (s, comp(a8, 1), comp(a10, 2), comp(a10, 1))",
                   "j = (s, comp(a8, 1) ^ ((l >> 9) & 1), comp(a10, 2), comp(a10, 1))")],
    # s2/s3: tail triple 2 aliased to tail triple 1 in both engines (full enumeration).
    'ALIAS_BOTH': [("return var_planes(9+3*TAIL_SITES.index(x))",
                    "return var_planes(9+3*(0 if TAIL_SITES.index(x) == 1 else TAIL_SITES.index(x)))"),
                   ("cur[bank_site(t)] = (lane >> (9+3*i)) & 7",
                    "cur[bank_site(t)] = (lane >> (9+3*(0 if i == 1 else i))) & 7")],
    # s3 cells: tail record non-uniform but still a function of the record (TV-blind).
    'NONUNIF_REC': [("zip(vals[PORT, TAIL[0]], vals[PORT, TAIL[1]], vals[PORT, TAIL[2]])]",
                     "zip(vals[PORT, TAIL[0]], vals[PORT, TAIL[1]], [v & 6 for v in vals[PORT, TAIL[2]]])]")],
    # x1: scalar engine only loses the nonlinearity.
    'X1_SCALAR': [("v = previous.get(p, 0) ^ H[x]", "v = previous.get(p, 0) ^ x")],
    # x1: bit-sliced engine only uses a wrong nonlinearity.
    'X1_BIT': [("ha, hb, hd = b, d, a ^ (b & d)", "ha, hb, hd = b, d, a ^ (b | d)")],
    # x2: both engines drop the old-local (previous-slice) term.
    'X2_BOTH': [("layer[x] = (oa ^ ha, ob ^ hb, od ^ hd)", "layer[x] = (ha, hb, hd)"),
                ("v = previous.get(p, 0) ^ H[x]", "v = H[x]")],
    # read set: carrier list drops q9+y.
    'READ_DROP': [(", 'q9+y': (0, S+1, 77)}", "}")],
    # read set: old q9 read at L-1 instead of L.
    'READ_TIME': [("carrier = [('q9', q9, L+2), ('q9', q9, L)]",
                   "carrier = [('q9', q9, L+2), ('q9', q9, L-1)]")],
    # s1: a pre-tail bank cell (t=5) carries the first tail triple's variable.
    'S1_PRE': [("    if x in TAIL_SITES:\n        return var_planes(9+3*TAIL_SITES.index(x))",
                "    if x == bank_site(5):\n        return var_planes(9)\n"
                "    if x in TAIL_SITES:\n        return var_planes(9+3*TAIL_SITES.index(x))"),
               ("    prev = {p: v for p, v in prev.items() if v}\n    cur = {p: v for p, v in cur.items() if v}\n    slices = {-1: prev, 0: cur}\n    for tau in range(1, HS+1):",
                "    cur[bank_site(5)] = (lane >> 9) & 7\n"
                "    prev = {p: v for p, v in prev.items() if v}\n    cur = {p: v for p, v in cur.items() if v}\n    slices = {-1: prev, 0: cur}\n    for tau in range(1, HS+1):")],
    # c1/c2: the tail record replaced by the raw tail bank (no G in the record).
    'C1_NOG': [("    pool = [(a << 6) | (b << 3) | c for a, b, c in zip(q8, q10, mm)]\n",
                "    pool = [(a << 6) | (b << 3) | c for a, b, c in zip(q8, q10, mm)]\n"
                "    w = [l >> 9 for l in lanes]\n")],
    # c3: frozen q8 (n+1) in place of the native continuation.
    'C3_FROZEN': [("q8late = vals[Q8, HS]", "q8late = vals[Q8, NS+1]")],
    # g1: tail lower bound moved 77 ticks earlier.
    'G1_SHIFT': [("lo, hi = max(deadlines[i], L)+1, H2", "lo, hi = max(deadlines[i], L)-76, H2")],
}

for name, reps in MUTANTS.items():
    text = SRC
    for old, new in INSTR + reps:
        n = text.count(old)
        if n != 1:
            raise SystemExit(f'{name}: pattern occurs {n} times: {old!r}')
        text = text.replace(old, new)
    d = os.path.join(outdir, name)
    os.makedirs(os.path.join(d, 'run'), exist_ok=True)
    with open(os.path.join(d, 'checks.py'), 'w') as fh:
        fh.write(text)
print('built', len(MUTANTS))
