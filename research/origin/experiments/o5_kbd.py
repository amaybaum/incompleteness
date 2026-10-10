"""o5_kbd.py -- research/origin, round 2, node O5: KB-D (the knowledge-balance readout: reading the frame
re-randomizes the memory) -- source it, or close it on the stated access.

QUESTION. KB-D is the only mechanism found in round 1 (O1-T7b, O2-G5) that gives the Discrete witness from
monomial input. Can it be derived from a premise at L, or from a premise that passes the disguise test? The
candidates named for this round are tested exactly: (a) incompleteness of observation read as a resource
bound on the observer's memory; (b) the kernel's record-writing instrument under a finite-memory bound;
(c) the native Lueders readout composed with a forgetful map; one further candidate found while preparing
the script: (d) symplectic couplings (the substratum's second-order linear rule is symplectic). The no-go
side: on the stated access every readout that is repeatable and passive excludes KB-D's body.

MODEL. Omega = {0,1}^2, configuration (z, x): z the frame bit, x the memory. States: probability vectors on
Omega (exact Fractions). Readouts are partitions of Omega into cells. Two instrument laws for a partition P:
  passive (Lueders = conditioning):   branch c: w -> w * 1_c        (on the classical carrier this is the
                                      kernel's native readout: readout_is_localLuders, OperationalAssembly:658)
  KB-D (measure and re-prepare):      branch c: w -> w(c) * unif(c)  (for the z partition: read z, re-randomize
                                      x; for the other partitions its conjugates by permutations)
An access is (a set of permutations, a list of instruments); reachable posteriors = BFS closure of the uniform
seed under the permutations and the normalized nonzero branches; the body is their convex hull.

CHECKS.
 A  the dichotomy (sharpened Lemma P on the classical carrier)
  A1 access (S4, passive z): every point mass reachable; extreme points of the body = the 4 point masses;
     every extreme point deterministic for every partition; no balanced extreme point.
  A2 access (S4, passive z, KB-D z): every point mass reachable (adding KB-D keeps the simplex).
  A3 access (S4, KB-D z): no point mass reachable; reachable posteriors = uniform + 6 pair states; extreme
     points = the 6 pair states; x+ is extreme and balanced for z; at x+ the z-readout is repeatable (its
     posteriors read z surely) and not passive (observe-and-forget(x+) = uniform != x+).
  A4 exclusivity: for each of the 14 nontrivial partitions P of Omega, access (S4, KB-D z, passive P)
     reaches every point mass.
  A5 the kernel's pure-seed pattern (read, feed-forward correction, forget the outcome:
     pureSeedPrep_available_of_swap, OperationalAssembly:675) applied to z, then to x through the swap: from the
     uniform seed it gives the point mass (0,0) with probability 1 under the passive readout, with no
     persistent memory; the same pattern with the KB-D readout ends in a pair state (no point mass).
  A6 the classical form of the theorem (design module OriginPassive, extreme_pointMass_of_passive): on the A1
     body every partition readout has the passive decomposition at every reachable state; on the A3 body the
     z-readout has none at x+ (the only body state with z-mass 1 is z+, and 2 x+ - z+ has a negative entry);
     separation control: on K = segment[z+, z-] the z-readout is passive, the extreme points are
     deterministic, and they are not point masses.
 B  candidate (a): incompleteness read as a memory bound
  B1 procedures (acceptance at the time) with a 1-bit memory prepare the point mass (0,0).
  B2 fully embedded (no acceptance; the observer's state is P(system | its memory)): over all 8! bijections
     of (z, x, m) from unif(z,x) x [m=0], some posterior is a point mass; over the 1344 affine bijections
     (AGL(3,2)) no posterior has support 1 or 3, and all six pair states occur.
  B3 frequencies under the memory bound (embedded, affine): the owner's sandwich with the dephasing realized
     as an embedded record into the 1-bit memory: frequencies given the preparation are 1 and 1 (V = 0);
     the memory-conditioned predictions are 1 and 1/2, the 1/2 arising because the record overwrites the
     preparation's record; with a fresh blank bit for the dephasing record the prediction is 1.
 C  candidate (b): the kernel recorder under a finite-memory bound
  C1 the recorder (Kraus |a,a><a,b|; recordInstr_apply, InternalObserver:249) on the classical carrier: into
     a separate register the system marginal is unchanged; into the memory x (x := z) the posterior of
     outcome a is the point mass (a,a).
  C2 reversible dilation on 3 bits (z, x, r), r the reused register: no bijection fixing z writes a perfect
     record into a register of unknown (uniform) content; with r blank, every perfect-record bijection fixing
     z leaves x a known function of (z, x).
 D  candidate (c): the Lueders readout composed with a forgetful map
  D1 KB-D z = (forget x: discard x, attach a uniform x) o (Lueders z), branch by branch, exactly.
  D2 the composite added to the stated access, which keeps the passive readout: = A2.
 E  candidate (d): symplectic couplings
  E1 4 bits (z, x, q, p): q a blank pointer, p its conjugate; omega = zx' + xz' + qp' + pq' (mod 2). Among
     the affine bijections with z' = z and a perfect record q' = z from q = 0: every symplectic one
     re-randomizes x when p is uniform; some non-symplectic one keeps x; with p known, x' is a known function
     of (z, x) for every one of them.
DECISION RULE (fixed before the first run; the verdict is generated from the measured booleans):
  NOGO := A1 and A2 and A3 and A4 and A5 and A6.
  CAND_a_FAILED := B1 and B2pm and B3;  the affine half of B2 (B2aff) is recorded as an epistemic restriction,
     not as a source of KB-D.
  CAND_b_FAILED := C1 and C2.   CAND_c_INSTRUMENT_ONLY := D1 and D2.   CAND_d_CONDITIONAL := E1.
  VERDICT VOID if any countercontrol is True or a normalization control fails.
  VERDICT NO-GO-ON-STATED-ACCESS iff NOGO and CAND_a_FAILED and CAND_b_FAILED and CAND_c_INSTRUMENT_ONLY
     and CAND_d_CONDITIONAL; otherwise VERDICT MIXED with the failing items listed.
COUNTERCONTROLS (must be False):
  CC1 the A1 body has a balanced extreme point;
  CC2 the A3 access reaches a point mass;
  CC3 the A1 body has exactly six extreme points;
  CC4 the plain CNOT (z, x, q, p) -> (z, x, q + z, p) is symplectic;
  CC5 the extremality test declares the uniform state extreme in the A3 body.

Run: python3 -I -B o5_kbd.py > o5_kbd.out 2> o5_kbd.err; echo "exit $?" >> o5_kbd.err
"""

from fractions import Fraction as F
from itertools import permutations, combinations, product

OMEGA = [(0, 0), (0, 1), (1, 0), (1, 1)]  # (z, x)
N = 4
RES = {}
CC = {}


def vec(d):
    v = [F(0)] * N
    for i, p in d.items():
        v[i] = F(p)
    return tuple(v)


def unif(cells):
    cells = list(cells)
    return tuple(F(1, len(cells)) if i in cells else F(0) for i in range(N))


UNIFORM = unif(range(N))
PM = [unif([i]) for i in range(N)]


def apply_perm(sig, w):
    v = [F(0)] * N
    for i in range(N):
        v[sig[i]] += w[i]
    return tuple(v)


S4 = list(permutations(range(N)))


def partition_of(f):
    cells = {}
    for i in range(N):
        cells.setdefault(f(OMEGA[i]), []).append(i)
    return [tuple(c) for c in cells.values()]


PZ = partition_of(lambda c: c[0])
PX = partition_of(lambda c: c[1])
PPAR = partition_of(lambda c: c[0] ^ c[1])


def set_partitions(items):
    items = list(items)
    if not items:
        yield []
        return
    first, rest = items[0], items[1:]
    for p in set_partitions(rest):
        for k in range(len(p)):
            yield p[:k] + [[first] + p[k]] + p[k + 1:]
        yield [[first]] + p


ALLPART = [[tuple(sorted(c)) for c in p] for p in set_partitions(range(N))]
NONTRIV = [p for p in ALLPART if len(p) > 1]


def passive_inst(P):
    def br(c):
        return lambda w: tuple(w[i] if i in c else F(0) for i in range(N))
    return [br(c) for c in P]


def kbd_inst(P):
    def br(c):
        def f(w):
            m = sum(w[i] for i in c)
            return tuple(m / len(c) if i in c else F(0) for i in range(N))
        return f
    return [br(c) for c in P]


def normalize(v):
    s = sum(v)
    return tuple(a / s for a in v)


def reach(perms, insts, seed=UNIFORM, cap=5000):
    seen = {seed}
    frontier = [seed]
    while frontier:
        new = []
        for w in frontier:
            outs = [apply_perm(s, w) for s in perms]
            for inst in insts:
                for br in inst:
                    v = br(w)
                    if sum(v) > 0:
                        outs.append(normalize(v))
            for u in outs:
                if u not in seen:
                    seen.add(u)
                    new.append(u)
                    if len(seen) > cap:
                        raise RuntimeError("reach cap exceeded")
        frontier = new
    return seen


def rank(rows):
    M = [list(r) for r in rows]
    if not M:
        return 0
    rk = 0
    for col in range(len(M[0])):
        piv = None
        for r in range(rk, len(M)):
            if M[r][col] != 0:
                piv = r
                break
        if piv is None:
            continue
        M[rk], M[piv] = M[piv], M[rk]
        for r in range(len(M)):
            if r != rk and M[r][col] != 0:
                f = M[r][col] / M[rk][col]
                M[r] = [a - f * b for a, b in zip(M[r], M[rk])]
        rk += 1
    return rk


def aff_indep(R):
    if len(R) == 1:
        return True
    return rank([tuple(a - b for a, b in zip(r, R[0])) for r in R[1:]]) == len(R) - 1


def solve_bary(p, R):
    k = len(R)
    M = [[R[j][i] for j in range(k)] + [p[i]] for i in range(N)] + [[F(1)] * k + [F(1)]]
    rk = 0
    pivcols = []
    for col in range(k):
        piv = None
        for r in range(rk, len(M)):
            if M[r][col] != 0:
                piv = r
                break
        if piv is None:
            continue
        M[rk], M[piv] = M[piv], M[rk]
        pv = M[rk][col]
        M[rk] = [a / pv for a in M[rk]]
        for r in range(len(M)):
            if r != rk and M[r][col] != 0:
                f = M[r][col]
                M[r] = [a - f * b for a, b in zip(M[r], M[rk])]
        pivcols.append(col)
        rk += 1
    for r in range(rk, len(M)):
        if M[r][k] != 0:
            return None
    if rk < k:
        return None
    lam = [F(0)] * k
    for r, col in enumerate(pivcols):
        lam[col] = M[r][k]
    return lam


def in_hull(p, T):
    T = list(T)
    for k in range(1, 5):
        for R in combinations(T, k):
            if not aff_indep(list(R)):
                continue
            lam = solve_bary(p, list(R))
            if lam is not None and all(l >= 0 for l in lam):
                return True
    return False


def extreme_points(S):
    S = list(S)
    return [p for p in S if not in_hull(p, [q for q in S if q != p])]


def cell_mass(w, c):
    return sum(w[i] for i in c)


def fmt(w):
    return "(" + ", ".join(str(a) for a in w) + ")"


def is_pm(w):
    return sum(1 for a in w if a != 0) == 1


ZP = unif([0, 1])   # z = 0, x uniform
ZM = unif([2, 3])
XP = unif([0, 2])   # x = 0, z uniform

print("== o5_kbd ==")
print(f"nontrivial partitions of Omega: {len(NONTRIV)} (Bell(4) - 1 = 14)")
print()
print("-- A: the dichotomy on the classical carrier")
# A1
R1 = reach(S4, [passive_inst(PZ)])
E1 = extreme_points(R1)
a1_pm = all(PM[i] in R1 for i in range(N))
a1_ext = sorted(E1) == sorted(PM)
a1_det = all(cell_mass(w, c) in (0, 1) for w in E1 for P in ALLPART for c in P)
a1_bal = any(cell_mass(w, c) == F(1, 2) for w in E1 for P in NONTRIV for c in P)
RES["A1"] = a1_pm and a1_ext and a1_det and not a1_bal
CC["CC1"] = a1_bal
CC["CC3"] = len(E1) == 6
print(f"A1  access (S4, passive z): {len(R1)} posteriors; all point masses reachable: {a1_pm}; extreme points = "
      f"the 4 point masses: {a1_ext}; extreme points deterministic for all {len(ALLPART)} partitions: {a1_det}; "
      f"balanced extreme point: {a1_bal}  -> {RES['A1']}")
# A2
R2 = reach(S4, [passive_inst(PZ), kbd_inst(PZ)])
RES["A2"] = all(PM[i] in R2 for i in range(N))
print(f"A2  access (S4, passive z, KB-D z): {len(R2)} posteriors; all point masses reachable: {RES['A2']}")
# A3
R3 = reach(S4, [kbd_inst(PZ)])
E3 = extreme_points(R3)
pairs = sorted(unif(c) for c in combinations(range(N), 2))
a3_nopm = not any(is_pm(w) for w in R3)
a3_set = sorted(R3) == sorted(pairs + [UNIFORM])
a3_ext = sorted(E3) == pairs
a3_xp = XP in E3 and cell_mass(XP, PZ[0]) == F(1, 2)
post = [normalize(br(XP)) for br in kbd_inst(PZ) if sum(br(XP)) > 0]
a3_rep = all(max(cell_mass(q, c) for c in PZ) == 1 for q in post)
oaf = tuple(sum(br(XP)[i] for br in kbd_inst(PZ)) for i in range(N))
a3_inv = oaf == UNIFORM and oaf != XP
RES["A3"] = a3_nopm and a3_set and a3_ext and a3_xp and a3_rep and a3_inv
CC["CC2"] = not a3_nopm
CC["CC5"] = UNIFORM in E3
print(f"A3  access (S4, KB-D z): {len(R3)} posteriors; no point mass: {a3_nopm}; = uniform + 6 pair states: {a3_set}; "
      f"extreme points = the 6 pair states: {a3_ext}; x+ extreme and z-balanced: {a3_xp}; z-readout repeatable at x+ "
      f"(posteriors {', '.join(fmt(q) for q in post)}): {a3_rep}; observe-and-forget(x+) = {fmt(oaf)} = uniform != x+: "
      f"{a3_inv}  -> {RES['A3']}")
# A4
a4 = []
for P in NONTRIV:
    Rp = reach(S4, [kbd_inst(PZ), passive_inst(P)])
    a4.append(all(PM[i] in Rp for i in range(N)))
RES["A4"] = all(a4)
print(f"A4  access (S4, KB-D z, passive P) reaches every point mass, for each of the 14 nontrivial partitions P: "
      f"{sum(a4)}/14  -> {RES['A4']}")
# A5
FLIPZ = tuple(OMEGA.index((c[0] ^ 1, c[1])) for c in OMEGA)
SWAP = tuple(OMEGA.index((c[1], c[0])) for c in OMEGA)


def seed_step(w, inst):
    """read z with the given instrument, correct z -> 0 by feed-forward, forget the outcome."""
    out = [F(0)] * N
    for k, br in enumerate(inst):
        v = br(w)
        if PZ[k] == (2, 3):
            v = apply_perm(FLIPZ, v)
        out = [a + b for a, b in zip(out, v)]
    return tuple(out)


def pure_seed_pattern(inst):
    w = seed_step(UNIFORM, inst)
    w = apply_perm(SWAP, w)
    w = seed_step(w, inst)
    w = apply_perm(SWAP, w)
    return w


assert PZ == [(0, 1), (2, 3)]
w_pas = pure_seed_pattern(passive_inst(PZ))
w_kbd = pure_seed_pattern(kbd_inst(PZ))
RES["A5"] = w_pas == PM[0] and sum(w_pas) == 1 and not is_pm(w_kbd) and w_kbd in pairs
print(f"A5  pure-seed pattern (read z, correct, forget; swap; repeat; swap back): passive readout -> {fmt(w_pas)} "
      f"(point mass (0,0), probability 1); KB-D readout -> {fmt(w_kbd)} (pair state)  -> {RES['A5']}")


# A6
def passive_decomp_exists(w, c, body_pts):
    m = cell_mass(w, c)
    if m == 0 or m == 1:
        return True
    w0 = tuple(w[i] / m if i in c else F(0) for i in range(N))
    w1 = tuple((w[i] - m * w0[i]) / (1 - m) for i in range(N))
    return in_hull(w0, body_pts) and all(a >= 0 for a in w1) and in_hull(w1, body_pts)


a6_simplex = all(passive_decomp_exists(w, c, list(R1)) for w in R1 for P in ALLPART for c in P)
# on the octahedron at x+: every body state with z-mass 1 is a mixture of reachable states with z-mass 1
face = [q for q in R3 if cell_mass(q, PZ[0]) == 1]
w1x = tuple(2 * XP[i] - ZP[i] for i in range(N))
a6_oct = face == [ZP] and any(a < 0 for a in w1x)
seg = [ZP, ZM]
seg_ext = extreme_points(seg)
a6_sep = (all(passive_decomp_exists(w, c, seg) for w in seg for c in PZ)
          and all(cell_mass(w, c) in (0, 1) for w in seg_ext for c in PZ) and not any(is_pm(w) for w in seg_ext))
RES["A6"] = a6_simplex and a6_oct and a6_sep
print(f"A6  passive decompositions on the A1 body for every partition at every reachable state: {a6_simplex}; on the "
      f"A3 body at x+: z-face = {{z+}}: {face == [ZP]}, 2x+ - z+ = {fmt(w1x)} not a state: {a6_oct}; separation "
      f"control (segment [z+, z-]: passive, deterministic extreme points that are not point masses): {a6_sep}  "
      f"-> {RES['A6']}")

print()
print("-- B: candidate (a), incompleteness read as a memory bound")
# configurations (z, x, m) in {0,1}^3, index 4 z + 2 x + m
C3 = [(z, x, m) for z in range(2) for x in range(2) for m in range(2)]
I3 = {c: i for i, c in enumerate(C3)}


def perm3(f):
    return tuple(I3[f(c)] for c in C3)


def ap3(sig, w):
    v = [F(0)] * 8
    for i in range(8):
        v[sig[i]] += w[i]
    return v


def cond_m(w, mval, mi=2):
    v = [w[i] if C3[i][mi] == mval else F(0) for i in range(8)]
    s = sum(v)
    return [a / s for a in v], s


def marg_zx(w):
    out = [F(0)] * N
    for i, c in enumerate(C3):
        out[OMEGA.index((c[0], c[1]))] += w[i]
    return tuple(out)


CNOT_ZM = perm3(lambda c: (c[0], c[1], c[2] ^ c[0]))
SWAP3 = perm3(lambda c: (c[1], c[0], c[2]))
init3 = [F(1, 4) if c[2] == 0 else F(0) for c in C3]
w = ap3(CNOT_ZM, init3)
w, p1 = cond_m(w, 0)
w = ap3(SWAP3, w)
w = ap3(CNOT_ZM, w)
w, p2 = cond_m(w, 0)
w = ap3(SWAP3, w)
b1_state = marg_zx(w)
RES["B1"] = b1_state == PM[0]
print(f"B1  1-bit memory, acceptance at the time (CNOT z->m, accept m=0, swap, CNOT z->m, accept m=0, swap): state "
      f"{fmt(b1_state)}, acceptance probabilities {p1}, {p2}  -> point mass: {RES['B1']}")

support0 = [i for i in range(8) if init3[i] != 0]


def posterior_supports(sig):
    img = [sig[i] for i in support0]
    sup = {}
    for j in img:
        z, x, m = C3[j]
        sup.setdefault(m, []).append((z, x))
    return [tuple(sorted(s)) for s in sup.values()]


n_pm = 0
for sig in permutations(range(8)):
    if any(len(s) == 1 for s in posterior_supports(sig)):
        n_pm += 1
RES["B2pm"] = n_pm > 0


def gl_matrices(n):
    for bits in product(range(2), repeat=n * n):
        M = [list(bits[r * n:(r + 1) * n]) for r in range(n)]
        A = [row[:] for row in M]
        rk = 0
        for col in range(n):
            piv = None
            for r in range(rk, n):
                if A[r][col]:
                    piv = r
                    break
            if piv is None:
                continue
            A[rk], A[piv] = A[piv], A[rk]
            for r in range(n):
                if r != rk and A[r][col]:
                    A[r] = [a ^ b for a, b in zip(A[r], A[rk])]
            rk += 1
        if rk == n:
            yield M


def affine_perm(M, c, coords):
    n = len(c)
    idx = {v: i for i, v in enumerate(coords)}
    out = []
    for v in coords:
        img = tuple((sum(M[r][k] * v[k] for k in range(n)) + c[r]) % 2 for r in range(n))
        out.append(idx[img])
    return tuple(out)


GL3 = list(gl_matrices(3))
aff_sizes = set()
pairs_seen = set()
n_aff = 0
for M in GL3:
    for c in product(range(2), repeat=3):
        sig = affine_perm(M, c, C3)
        n_aff += 1
        for s in posterior_supports(sig):
            aff_sizes.add(len(s))
            if len(s) == 2:
                pairs_seen.add(s)
RES["B2aff"] = aff_sizes <= {2, 4} and len(pairs_seen) == 6
print(f"B2  embedded, no acceptance: of 40320 bijections of (z, x, m), {n_pm} give a point-mass posterior "
      f"-> {RES['B2pm']}; |GL(3,2)| = {len(GL3)}, affine bijections {n_aff}: posterior support sizes {sorted(aff_sizes)}, "
      f"pair states occurring {len(pairs_seen)}/6 -> knowledge-balanced posteriors: {RES['B2aff']}")

# B3: 1-bit memory, frequencies and memory-conditioned predictions
init_prep = ap3(CNOT_ZM, init3)
w_acc, _ = cond_m(init_prep, 0)


def pz0(w):
    return sum(w[i] for i, c in enumerate(C3) if c[0] == 0)


f_coh = pz0(ap3(SWAP3, ap3(SWAP3, w_acc)))
f_dep = pz0(ap3(SWAP3, ap3(CNOT_ZM, ap3(SWAP3, w_acc))))
emb_coh = ap3(SWAP3, ap3(SWAP3, init_prep))
emb_dep = ap3(SWAP3, ap3(CNOT_ZM, ap3(SWAP3, init_prep)))
pred_coh = pz0(cond_m(emb_coh, 0)[0])
pred_dep = sorted(set(pz0(cond_m(emb_dep, mv)[0]) for mv in range(2)))
# fresh blank bit m2 for the dephasing record: configurations (z, x, m1, m2)
C4 = [(z, x, a, b) for z in range(2) for x in range(2) for a in range(2) for b in range(2)]
I4 = {c: i for i, c in enumerate(C4)}


def perm4(f):
    return tuple(I4[f(c)] for c in C4)


def ap4(sig, w):
    v = [F(0)] * 16
    for i in range(16):
        v[sig[i]] += w[i]
    return v


init4 = [F(1, 4) if (c[2] == 0 and c[3] == 0) else F(0) for c in C4]
w4 = ap4(perm4(lambda c: (c[0], c[1], c[2] ^ c[0], c[3])), init4)
w4 = ap4(perm4(lambda c: (c[1], c[0], c[2], c[3])), w4)
w4 = ap4(perm4(lambda c: (c[0], c[1], c[2], c[3] ^ c[0])), w4)
w4 = ap4(perm4(lambda c: (c[1], c[0], c[2], c[3])), w4)
preds_fresh = set()
for m2 in range(2):
    v = [w4[i] if (C4[i][2] == 0 and C4[i][3] == m2) else F(0) for i in range(16)]
    s = sum(v)
    if s > 0:
        preds_fresh.add(sum(v[i] for i, c in enumerate(C4) if c[0] == 0) / s)
RES["B3"] = (f_coh == 1 and f_dep == 1 and pred_coh == 1 and pred_dep == [F(1, 2)]
             and preds_fresh == {F(1)})
print(f"B3  frequencies given the preparation: coherent {f_coh}, dephased {f_dep} (V = {f_coh - f_dep}); "
      f"memory-conditioned predictions: coherent {pred_coh}, dephased {pred_dep} (the record overwrote the "
      f"preparation's record); with a fresh blank bit for the dephasing record: {sorted(preds_fresh)}  -> {RES['B3']}")

print()
print("-- C: candidate (b), the kernel recorder under a finite-memory bound")
# recorder on (system value a, register b): branch a maps P to (sum_b P(a,b)) delta_(a,a)
# (i) separate register r, system (z, x): configurations (z, x, r)
P0 = {c: F(1, 8) for c in C3}
after = {c: F(0) for c in C3}
for (z, x, r), p in P0.items():
    after[(z, x, z)] += p
sys_before = marg_zx([P0[c] for c in C3])
sys_after = marg_zx([after[c] for c in C3])
c1_sep = sys_before == sys_after
# (ii) register = the memory x of the system (z, x): branch a: P -> (sum_x P(a, x)) delta_(a, a)
c1_mem = True
for w0 in [UNIFORM, XP, ZP]:
    for a in range(2):
        mass = sum(w0[OMEGA.index((a, x))] for x in range(2))
        if mass == 0:
            continue
        postv = tuple(F(1) if OMEGA[i] == (a, a) else F(0) for i in range(N))
        c1_mem = c1_mem and is_pm(postv)
RES["C1"] = c1_sep and c1_mem
print(f"C1  recorder into a separate register: system marginal unchanged: {c1_sep}; recorder into the memory x: every "
      f"outcome's posterior is the point mass (a, a): {c1_mem}  -> {RES['C1']}")
# C2: bijections of (z, x, r) fixing z
XR = [(x, r) for x in range(2) for r in range(2)]
n_fix = 0
n_perfect_unknown = 0
n_perfect_blank = 0
blank_known = True
for s0 in permutations(range(4)):
    for s1 in permutations(range(4)):
        n_fix += 1
        maps = {0: s0, 1: s1}

        def img(z, x, r):
            return (z,) + XR[maps[z][XR.index((x, r))]]
        if all(img(z, x, r)[2] == z for z in range(2) for x in range(2) for r in range(2)):
            n_perfect_unknown += 1
        if all(img(z, x, 0)[2] == z for z in range(2) for x in range(2)):
            n_perfect_blank += 1
            # x' a function of (z, x): deterministic by construction; record whether it is a bijection of x
            for z in range(2):
                xs = [img(z, x, 0)[1] for x in range(2)]
                blank_known = blank_known and sorted(xs) == [0, 1]
RES["C2"] = n_fix == 576 and n_perfect_unknown == 0 and n_perfect_blank > 0 and blank_known
print(f"C2  {n_fix} bijections of (z, x, r) fixing z: perfect record into an unknown register: {n_perfect_unknown}; "
      f"into a blank register: {n_perfect_blank}, each keeping x as a known bijective relabeling: {blank_known}  "
      f"-> {RES['C2']}")

print()
print("-- D: candidate (c), Lueders readout composed with a forgetful map")


def forget_x(v):
    out = [F(0)] * N
    for i, (z, x) in enumerate(OMEGA):
        for x2 in range(2):
            out[OMEGA.index((z, x2))] += v[i] / 2
    return tuple(out)


test_states = sorted(R1 | R3)
d1 = all(forget_x(pb(w)) == kb(w) for w in test_states
         for pb, kb in zip(passive_inst(PZ), kbd_inst(PZ)))
RES["D1"] = d1
RES["D2"] = RES["A2"]
print(f"D1  KB-D z = forget_x o Lueders z on all {len(test_states)} reachable states of A1 and A3, branch by branch: {d1}")
print(f"D2  the composite added to the stated access (passive readout kept): every point mass reachable (A2): "
      f"{RES['D2']}")

print()
print("-- E: candidate (d), symplectic couplings")
C16 = [v for v in product(range(2), repeat=4)]  # (z, x, q, p)


def omega_form(u, v):
    return (u[0] * v[1] + u[1] * v[0] + u[2] * v[3] + u[3] * v[2]) % 2


E = [tuple(1 if k == j else 0 for k in range(4)) for j in range(4)]


def matvec(M, v):
    return tuple(sum(M[r][k] * v[k] for k in range(4)) % 2 for r in range(4))


def symplectic(M):
    return all(omega_form(matvec(M, E[a]), matvec(M, E[b])) == omega_form(E[a], E[b])
               for a in range(4) for b in range(4))


GL4 = list(gl_matrices(4))
counts = {("symp", "KBD"): 0, ("symp", "KEPT"): 0, ("nonsymp", "KBD"): 0, ("nonsymp", "KEPT"): 0}
known_p_ok = True
for M in GL4:
    if M[0] != [1, 0, 0, 0]:
        continue
    if not (M[2][0] == 1 and M[2][1] == 0 and M[2][3] == 0):
        continue
    for cx, cp in product(range(2), repeat=2):
        c = (0, cx, 0, cp)
        # perfect record: q' = z on inputs with q = 0 (holds by the row conditions; checked)
        ok = all((matvec(M, (z, x, 0, p))[2] + c[2]) % 2 == z for z in range(2) for x in range(2) for p in range(2))
        if not ok:
            continue
        cls = "KBD" if M[1][3] == 1 else "KEPT"
        key = ("symp" if symplectic(M) else "nonsymp", cls)
        counts[key] += 1
        # with p known (p = 0): x' is a function of (z, x) -- affine, deterministic
        for z in range(2):
            for x in range(2):
                xs = {(matvec(M, (z, x, 0, 0))[1] + cx) % 2}
                known_p_ok = known_p_ok and len(xs) == 1
CNOT = [[1, 0, 0, 0], [0, 1, 0, 0], [1, 0, 1, 0], [0, 0, 0, 1]]
KICK = [[1, 0, 0, 0], [0, 1, 0, 1], [1, 0, 1, 0], [0, 0, 0, 1]]
CC["CC4"] = symplectic(CNOT)
e1 = (counts[("symp", "KEPT")] == 0 and counts[("symp", "KBD")] > 0 and counts[("nonsymp", "KEPT")] > 0
      and known_p_ok)
RES["E1"] = e1
print(f"E1  |GL(4,2)| = {len(GL4)}; record couplings (z' = z, q' = z from q = 0), by class: symplectic & KB-D "
      f"{counts[('symp', 'KBD')]}, symplectic & x kept {counts[('symp', 'KEPT')]}, non-symplectic & KB-D "
      f"{counts[('nonsymp', 'KBD')]}, non-symplectic & x kept {counts[('nonsymp', 'KEPT')]}; with p known x' is a "
      f"function of (z, x) in every case: {known_p_ok}; the kickback coupling (x' = x + p) symplectic: "
      f"{symplectic(KICK)}  -> {e1}")

NORM = all(sum(w) == 1 and all(a >= 0 for a in w) for Rs in (R1, R2, R3) for w in Rs)
print()
print(f"normalization control: every reachable posterior of A1, A2, A3 is a probability vector: {NORM}")
print()
print("-- countercontrols (must be False)")
for k in sorted(CC):
    print(f"{k}  {'CC-OK (False as required)' if not CC[k] else 'CC-FAIL (True)'}")

print()
NOGO = all(RES[k] for k in ["A1", "A2", "A3", "A4", "A5", "A6"])
CA = RES["B1"] and RES["B2pm"] and RES["B3"]
CB = RES["C1"] and RES["C2"]
CCI = RES["D1"] and RES["D2"]
CD = RES["E1"]
for k in sorted(RES):
    print(f"  {k}: {RES[k]}")
if any(CC.values()) or not NORM:
    print("VERDICT VOID: a countercontrol returned True or the normalization control failed.")
elif NOGO and CA and CB and CCI and CD:
    print("VERDICT NO-GO-ON-STATED-ACCESS: with a passive repeatable readout in the access (the kernel's native Lueders")
    print("  readout on the classical carrier) the body is the simplex, every extreme state is deterministic, and KB-D's")
    print("  octahedron is excluded whatever is added (A1-A6); candidate (a) FAILED (procedures reach point masses with")
    print("  one memory bit; embedded, the memory bound restricts posteriors (B2aff = %s) but not frequencies, V = 0);"
          % RES["B2aff"])
    print("  candidate (b) FAILED (the recorder is passive on the system or erases the memory to a known value);")
    print("  candidate (c) sources the KB-D instrument only, not its exclusivity; candidate (d) forces KB-D, CONDITIONAL")
    print("  on symplectic couplings together with an unknown pointer conjugate.")
else:
    bad = [k for k, v in [("NOGO", NOGO), ("CAND_a", CA), ("CAND_b", CB), ("CAND_c", CCI), ("CAND_d", CD)] if not v]
    print(f"VERDICT MIXED: failing items {bad}")
