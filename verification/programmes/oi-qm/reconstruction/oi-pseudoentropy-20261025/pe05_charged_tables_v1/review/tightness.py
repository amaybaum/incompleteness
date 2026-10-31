"""Toy: is A-SIM's m+1 tight? Compare the set of exact curves (Pr[chi(v_K)=x_K], K=0..Kmax)
of active m=1 observers with those of passive m=1 observers, on autonomous toy generators."""
import itertools, random, sys
sys.path.insert(0, ".")
import importlib.util
spec = importlib.util.spec_from_file_location("t", "toy_checks.py")
src = open("toy_checks.py").read().split("allok = True")[0]
ns = {}; exec(compile(src, "toy_checks_defs", "exec"), ns)
random.seed(7)
def curves(step, seeds, active, Kmax):
    out = set()
    for r0, r1, a in ns["observers"](1):
        if bool(any(a)) != active: continue
        for chi in itertools.product((0, 1), repeat=2):
            c = []
            for K in range(Kmax + 1):
                J = ns["joint_law"](step, seeds, 1, r0, r1, a, K)
                c.append(sum(w for (v, x), w in J.items() if chi[v] == x))
            out.add(tuple(c))
    return out
P = {3: 0b1011, 4: 0b10011, 5: 0b100101}
cases = [("G_lin n=4", ns["gen_template"](4, P[4], "lin")), ("G_filt n=4", ns["gen_template"](4, P[4], "filt")),
         ("G_filt n=5", ns["gen_template"](5, P[5], "filt")), ("G_clkfix matched n=4", ns["gen_clkfix"](4, P[4], "matched"))]
cases += [("random autonomous H=8 #%d" % i, ns["gen_random_autonomous"](8)) for i in range(3)]
for name, (st, sd) in cases:
    A = curves(st, sd, True, 12); Pp = curves(st, sd, False, 12)
    print("%-26s active curves not attained by any passive m=1 curve: %d of %d" % (name, len(A - Pp), len(A)))
