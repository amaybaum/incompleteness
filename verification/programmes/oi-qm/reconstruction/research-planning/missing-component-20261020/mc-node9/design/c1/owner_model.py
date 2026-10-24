"""Owner's candidate recording mechanism, abstract model (exact).  Scope: a checked
counterexample repair; not a closure theorem.

Model.  Toy h = (q, p), uniform prior.  ONE reused pointer (Q, P): Q = 0 known, P uniform.
Read R_u (u = (uq, up)):   Q += omega(u, h) = uq*p + up*q ;  q += uq*P ;  p += up*P.
Record REC (fresh memory (X_i, Y_i), X_i = 0, Y_i uniform, independent):
                           X_i += Q ;  P += Y_i          (owner's copy rule; Q, Y_i unchanged)
Pointer exchange SWP:      (Q, P) -> (P, Q)
Free readout FREE:         the observer sees the current Q without any back-action.
Observer's records:
  arm FREE-RET : the observer sees Q after every read (free retention, W4's setting);
  arm REC-ONLY : the observer sees only the X_i (each at its recording; X_i never changes later).
Every quantity is a linear functional of the initial unknowns (q, p, P, Y_1, ...), so the
posterior support of the toy given the records is 2^(dim T - dim(T meet R)), T = span of the
current toy functionals, R = span of the record functionals; it is the same in every branch.
An independent brute-force enumeration of branches checks the W4 cases.
"""
from itertools import product
from fractions import Fraction

READS = {"p": (1, 0), "q": (0, 1), "q+p": (1, 1)}   # name = the functional omega(u,.) read


def rank(vs):
    b = []
    for v in vs:
        for x in b:
            v = min(v, v ^ x)
        if v:
            b.append(v)
    return len(b)


class St:
    def __init__(self, nmem):
        # unknown indices: q=0, p=1, P=2, Y_i = 3+i
        self.q, self.p, self.P, self.Q = 1, 2, 4, 0
        self.nY = 0
        self.nmem = nmem
        self.X = []
        self.rec = []

    def fresh(self):
        b = 1 << (3 + self.nY)
        self.nY += 1
        return b

    def read(self, name, arm):
        uq, up = READS[name]
        w = (uq * self.p) ^ (up * self.q) if False else ((self.p if uq else 0) ^ (self.q if up else 0))
        self.Q ^= w
        if uq:
            self.q ^= self.P
        if up:
            self.p ^= self.P
        if arm == "FREE-RET":
            self.rec.append(self.Q)

    def record(self, Y=None):
        Yb = self.fresh() if Y is None else Y
        self.X.append(self.Q)
        self.P ^= Yb
        self.rec.append(self.Q)
        return Yb

    def swp(self):
        self.Q, self.P = self.P, self.Q

    def free(self):
        self.rec.append(self.Q)

    def toy_support(self):
        T = [self.q, self.p]
        dT = rank(T)
        dTR = dT + rank(self.rec) - rank(T + self.rec)
        return 2 ** (dT - dTR)


def run(seq, arm):
    s = St(0)
    for op in seq:
        if op in READS:
            s.read(op, arm)
        elif op == "REC":
            s.record()
        elif op == "SWP":
            s.swp()
        elif op == "FREE":
            s.free()
        else:
            raise ValueError(op)
    return s


def brute(seq, arm):
    """Independent check: enumerate every value of the unknowns, group by the record values,
    report the set of posterior toy-support sizes over branches and the branch count."""
    s0 = run(seq, arm)
    nunk = 3 + s0.nY
    branches = {}
    for vals in product((0, 1), repeat=nunk):
        x = sum(v << i for i, v in enumerate(vals))
        ev = lambda f: bin(f & x).count("1") & 1
        key = tuple(ev(f) for f in s0.rec)
        branches.setdefault(key, set()).add((ev(s0.q), ev(s0.p)))
    return sorted({len(v) for v in branches.values()}), len(branches)


ok = True


def show(label, seq, arm, expect=None):
    global ok
    s = run(seq, arm)
    sup = s.toy_support()
    bs, nb = brute(seq, arm)
    agree = (bs == [sup])
    line = f"  {label:58s} arm={arm:8s} toy support {sup}  (brute force: {bs} over {nb} branches)"
    if expect is not None:
        good = (sup == expect) and agree
        ok &= good
        line += f"  expected {expect}: {'PASS' if good else 'FAIL'}"
    else:
        ok &= agree
    print(line)
    return sup


print("W4 and the owner's repair")
show("W4: reads p, q, p (one reused pointer)", ["p", "q", "p"], "FREE-RET", 1)
s = run(["p", "q", "p"], "FREE-RET")
print(f"    readings as functionals of (q,p,P): r = {[bin(r) for r in s.rec]};  final toy q={bin(s.q)}, p={bin(s.p)}")
show("W4 + REC after every read, observer sees only X's", ["p", "REC", "q", "REC", "p", "REC"], "REC-ONLY", 2)
print("W3' and condition (iii): exchange then unrestricted free readout")
show("W3': SWP, FREE (learn old P), then reads p, q (P now known)", ["SWP", "FREE", "p", "q"], "FREE-RET", 1)
show("(iii) SWP, FREE, then p REC q REC (records only via REC)", ["SWP", "FREE", "p", "REC", "q", "REC"], "REC-ONLY")
show("(iii) SWP, FREE, then p FREE q FREE", ["SWP", "FREE", "p", "FREE", "q", "FREE"], "REC-ONLY", 1)
show("(iii) control: SWP, then p REC q REC (no free readout)", ["SWP", "p", "REC", "q", "REC"], "REC-ONLY")
show("(iii) control: p REC SWP REC (exchange, record the new Q)", ["p", "REC", "SWP", "REC"], "REC-ONLY")

print("Condition (ii): memory conjugates must be independent and fresh")
# same Y reused for two recordings
def w4_sameY():
    s = St(0)
    s.read("p", "REC-ONLY"); Y = s.record()
    s.read("q", "REC-ONLY"); s.record(Y)
    s.read("p", "REC-ONLY"); s.record(Y)
    return s
s = w4_sameY()
print(f"  W4 + REC with ONE memory conjugate Y reused for all three records: toy support {s.toy_support()}")
def w4_knownY():
    s = St(0)
    for r in ("p", "q", "p"):
        s.read(r, "REC-ONLY"); s.record(Y=0)
    return s
s = w4_knownY()
print(f"  W4 + REC with Y supplied known (Y = 0, no back-action): toy support {s.toy_support()}")
ok &= (w4_knownY().toy_support() == 1)

# access to Y later: the observer learns every Y_i (e.g. memory exchange then reading X)
def w4_Yaccess():
    s = St(0)
    Ys = []
    for r in ("p", "q", "p"):
        s.read(r, "REC-ONLY"); Ys.append(s.record())
    s.rec += Ys
    return s
print(f"  W4 + REC, then later access to every Y_i (memory exchange + read): toy support {w4_Yaccess().toy_support()}")

print("Condition (iv): exhaustive adversarial sequences in the REC-ONLY arm (no FREE)")
ops = ["p", "q", "q+p", "REC", "SWP"]
for L in range(1, 8):
    worst = None
    cnt = 0
    for seq in product(ops, repeat=L):
        cnt += 1
        sup = run(list(seq), "REC-ONLY").toy_support()
        if worst is None or sup < worst[0]:
            worst = (sup, seq)
    print(f"  length {L}: {cnt} sequences; minimum toy support {worst[0]}  (e.g. {' '.join(worst[1])})")
    if worst[0] == 1:
        print("    -> a point mass is reachable without free readout")
print("  same with FREE allowed (unrestricted free readout of Q):")
for L in range(1, 6):
    worst = None
    for seq in product(ops + ["FREE"], repeat=L):
        sup = run(list(seq), "REC-ONLY").toy_support()
        if worst is None or sup < worst[0]:
            worst = (sup, seq)
    print(f"  length {L}: minimum toy support {worst[0]}  (e.g. {' '.join(worst[1])})")
print("OWNER MODEL CHECKS:", "ALL CONSISTENT" if ok else "SOME FAIL")
