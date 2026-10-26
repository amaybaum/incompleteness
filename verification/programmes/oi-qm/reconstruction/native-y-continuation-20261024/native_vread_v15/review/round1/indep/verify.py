"""Independent reviewer re-derivation for native_vread_v15. Imports nothing from the author.

Usage: python3 -I -B verify.py <native-y-continuation root>
"""
import hashlib
import json
import random
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

ROOT = Path(sys.argv[1])
OUT = {}
FAIL = []


def chk(ok, label):
    if not ok:
        FAIL.append(label)
    return ok


DIRS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def plus(p, q, k=1):
    return (p[0]+k*q[0], p[1]+k*q[1], p[2]+k*q[2])


def l1(p, q):
    return abs(p[0]-q[0])+abs(p[1]-q[1])+abs(p[2]-q[2])


def H(v):
    # H(A,B,D) = (B, D, A xor B*D), code 4A+2B+D
    A, B, Dd = v >> 2 & 1, v >> 1 & 1, v & 1
    return 4*B+2*Dd+(A ^ (B & Dd))


# ------------------------------------------------------------ A. dependence cones
def dep_cones(nmax):
    """dep[(t,p)] = frozenset of initial labels (slice, pos); slice 0 = current, -1 = previous."""
    rad = nmax+3
    memo = {}

    def dep(t, p):
        key = (t, p)
        if key in memo:
            return memo[key]
        if t == 0:
            r = frozenset({(0, p)})
        elif t == -1:
            r = frozenset({(-1, p)})
        else:
            s = set(dep(t-2, p))
            for e in DIRS:
                s |= dep(t-1, plus(p, e))
            r = frozenset(s)
        memo[key] = r
        return r
    res = {}
    for n in range(1, nmax+1):
        o = (0, 0, 0)
        own = dep(n-1, o)
        nb = {e: dep(n, e) for e in DIRS}
        keys = {}
        for e in DIRS:
            others = set(own)
            for f in DIRS:
                if f != e:
                    others |= nb[f]
            keys[e] = sorted(nb[e]-others)
        cur = sorted(c for e in DIRS for c in keys[e] if c[0] == 0)
        prev = sorted(c for e in DIRS for c in keys[e] if c[0] == -1)
        res[n] = (cur, prev)
        chk(set(cur) == {(0, plus((0, 0, 0), e, n+1)) for e in DIRS}, 'A current keys axial n=%d' % n)
        chk(set(prev) == {(-1, plus((0, 0, 0), e, n)) for e in DIRS}, 'A previous keys axial n=%d' % n)
        # parity/dist formula check against the cone
        for (t, p), s in list(memo.items()):
            pass
    # formula: current cell c in dep(t,w) iff l1<=t and (t-l1) even ; previous iff l1<=t-1 and parity
    bad = 0
    tested = 0
    for (t, p), s in memo.items():
        if t < 1 or p not in [(0, 0, 0)]+DIRS:
            continue
        for c in product(range(-rad, rad+1), repeat=3):
            if l1(c, p) > t+1:
                continue
            tested += 1
            d = l1(c, p)
            if ((0, c) in s) != (d <= t and (t-d) % 2 == 0):
                bad += 1
            if ((-1, c) in s) != (d <= t-1 and (t-1-d) % 2 == 0):
                bad += 1
    chk(bad == 0, 'A cone formula')
    return {'n_range': [1, nmax], 'formula_mismatches': bad, 'formula_cells_tested': tested,
            'current_keys_axial_(n+1)e': True, 'previous_keys_axial_ne': True}


# --------------------------------------------------- B. functional permutation tests
def world(rng_seed, n, planted):
    rng = random.Random(rng_seed)
    bg = {}
    memo = {}

    def init(t, p):
        if t == 0 and p in planted:
            return planted[p]
        k = (t, p)
        if k not in bg:
            bg[k] = rng.randrange(8)
        return bg[k]

    def U(t, p):
        if t in (0, -1):
            return init(t, p)
        k = (t, p)
        if k in memo:
            return memo[k]
        acc = 0
        for e in DIRS:
            acc ^= U(t-1, plus(p, e))
        v = U(t-2, p) ^ H(acc)
        memo[k] = v
        return v
    return U


def perm_tests(nmax, seeds):
    o = (0, 0, 0)
    worlds = 0
    off_two = {}
    for n in range(1, nmax+1):
        for sd in seeds:
            for e in DIRS:
                key = plus(o, e, n+1)
                Vs, own, nbs = [], [], {f: [] for f in DIRS}
                for kv in range(8):
                    # same background seed for all key values: rng draws are position-ordered by first use;
                    # make background deterministic per (t,p) instead.
                    U = world2(sd, {key: kv})
                    Vs.append(U(n+1, o))
                    own.append(U(n-1, o))
                    for f in DIRS:
                        nbs[f].append(U(n, f))
                chk(len(set(Vs)) == 8, 'B V perm n=%d e=%s' % (n, e))
                chk(len(set(own)) == 1, 'B own q9 const')
                chk(len(set(nbs[e])) == 8, 'B own neighbour perm')
                chk(all(len(set(nbs[f])) == 1 for f in DIRS if f != e), 'B other neighbours const')
                worlds += 1
            # countercontrol: off-axis cell at distance n+1 with two nonzero comps
            off = (-n, 0, -1)
            changed = set()
            for kv in range(8):
                U = world2(sd, {off: kv})
                changed.add(tuple(U(n, f) for f in DIRS))
            per = [len({c[i] for c in changed}) > 1 for i in range(6)]
            off_two.setdefault(n, []).append(sum(per))
    return worlds, off_two


def world2(seed, planted):
    """Background is a deterministic hash-free PRNG of (seed,t,p) so changing the key changes nothing else."""
    memo = {}

    def init(t, p):
        if t == 0 and p in planted:
            return planted[p]
        r = random.Random('%d|%d|%d|%d|%d' % (seed, t, p[0], p[1], p[2]))
        return r.randrange(8)

    def U(t, p):
        if t in (0, -1):
            return init(t, p)
        k = (t, p)
        if k in memo:
            return memo[k]
        acc = 0
        for e in DIRS:
            acc ^= U(t-1, plus(p, e))
        v = U(t-2, p) ^ H(acc)
        memo[k] = v
        return v
    return U


# ------------------------------------------------------------ C. actual scale
T = 185
P = 12*840**185
S = P+T
R = S+68
L = R+9
Q9 = (0, S, 77)
Q10 = (0, S, 78)
PORTS = [(0, T, 0), (0, 0, -8*T), (T, P, 0), (-T, P, 0), (4*T, P, 0), (0, S, 0), (12*R, 0, 0), (48*L, 0, 0)]
DEADL = [T, T, S, S, S, S, R, L]
PDIR = [(0, -1, 0), (0, 0, -1), (0, 1, 0), (0, 1, 0), (0, 1, 0), (0, 1, 0), (-1, 0, 0), (1, 0, 0)]
READY = list(zip(PORTS, DEADL))
READY += [((T, 0, 0), T), ((-T, 0, 0), T), ((4*T, 0, 0), T), ((0, S, -68), R), ((-12*R, 0, 0), R)]
READY += [((0, S, 68+k), R+k) for k in range(10)]
READY += [((-48*L, 0, 0), L)]
EXTRA_READY = [(Q10, L+1),
               # branch_v10 / history_v11 variants
               ((0, S, 77), L), ((0, S, 76), L-1), ((48*L, 0, 0), L), ((0, S, 70), R+2), ((0, S, 71), R+3),
               ((12*R, 0, 0), R)]
LOCAL = {'O': (0, 0, 0), 'W': (0, -76, 76), 'E': (0, -78, 78), 'N': (0, S, S+156),
         'Q': (0, S, S+136), 'C': (0, S, S+150), 'G': (0, S, S+152), 'J': (0, S, S+154),
         'K+': (1, S, S+153), 'K-': (-1, S, S+153),
         'selY': (0, 2*S, 0), 'sel+': (T, P+S, 0), 'sel-': (-T, P+S, 0),
         'F10': (-(L+1), S, 78), 'F8(free)': (-(L+1), S, 76), 'zsrc': (-48*L, -L, 0)}
RECV = PORTS+[(-48*L, 0, 0)]
SIDE = 256*L+64*T+1


def tdist(p, q):
    return sum(min(abs(a-b) % SIDE, SIDE-abs(a-b) % SIDE) for a, b in zip(p, q))


def on_bank(cell):
    hits = []
    for i, (p, d, dl) in enumerate(zip(PORTS, PDIR, DEADL)):
        ax = [j for j in range(3) if d[j]][0]
        if all(cell[j] == p[j] for j in range(3) if j != ax):
            t = (cell[ax]-p[ax])*d[ax]
            hits.append((i, t, dl < t <= 2*L))
    return hits


def rel(v):
    return v-L if abs(v-L) < 10**6 else v


def actual_scale(sources):
    rows = {}
    for slice_name, k in (('current', L+2), ('previous', L+1)):
        for e in DIRS:
            c = plus(Q9, e, k)
            row = {
                'in_ready': [i for i, (cc, r) in enumerate(READY) if l1(c, cc) <= r],
                'in_extra_ready': [i for i, (cc, r) in enumerate(EXTRA_READY) if l1(c, cc) <= r],
                'min_ready_margin': min(l1(c, cc)-r for cc, r in READY+EXTRA_READY),
                'local_source_hit': [n for n, p in LOCAL.items() if p == c],
                'min_local_dist': min(l1(c, p) for p in LOCAL.values()),
                'inherited_hit': c in sources,
                'min_inherited_dist': min(l1(c, p) for p in sources),
                'bank': on_bank(c),
                'min_recv_minus_L': rel(min(l1(c, p) for p in RECV)),
                'torus_equals_l1_recv': all(tdist(c, p) == l1(c, p) for p in RECV),
                'dist_q9_nbrs': [l1(c, plus(Q9, f))-L for f in DIRS],
                'dist_q9_minus_L': l1(c, Q9)-L,
            }
            rows['%s %s' % (slice_name, e)] = row
    # herald source family (49L-1-q, +-(q+1), 0), (49L-1-q,0,q+1): min x distance >= 47L from keys
    herald_gap = min(49*L-1-(L-1)-abs(plus(Q9, e, L+2)[0]) for e in DIRS)
    return rows, herald_gap


def shell_banks():
    out = []
    for i, (p, d, dl) in enumerate(zip(PORTS, PDIR, DEADL)):
        ax = [j for j in range(3) if d[j]][0]
        rest = sum(abs(p[j]-Q9[j]) for j in range(3) if j != ax)
        t0 = (Q9[ax]-p[ax])*d[ax]
        sl = L+2-rest
        if sl < 0:
            continue
        for t in range(max(dl+1, t0-sl), min(2*L, t0+sl)+1):
            c = plus(p, d, t)
            dd = l1(c, Q9)
            if dd > L+2:
                continue
            reach = [f for f in DIRS if l1(c, plus(Q9, f)) <= L+1 and (L+1-l1(c, plus(Q9, f))) % 2 == 0]
            out.append((i, t-dl, dd-L, (L+2-dd) % 2 == 0, reach))
    return out


# ------------------------------------------------------------ D/E. table checks
def load(rel_, digest):
    raw = (ROOT/rel_).read_bytes()
    chk(hashlib.sha256(raw).hexdigest() == digest, 'pin '+rel_)
    return json.loads(raw)


def table_checks():
    route = load('native_route_v13/result.json', '762b9799db7448c4eecf2c994c8c68ff94e1be83a7f6884b4a36385505df5a02')
    v14 = load('native_decode_v14/result.json', '3172e7d013c09cdcdf638a7ace68e0eff98bb3cd0411e8666b76a8226ad59034')
    q9j = load('branch_v10/local-controller/symmetric-result.json', 'd8e7c1f5841192165beefb3fe35b069cc14cc93f2faa2bd68619aa7748b3db2f')
    rev = load('native_route_v13/review/result.json', '73780def8505d68d1967936116a88a49d471eb32aeb83d528ff3cd41025ae6e4')
    tab = route['q10_table_hex']
    chk(hashlib.sha256(tab.encode()).hexdigest() == 'b2f32466113dede2fa9e43469f5c209fde5d610180ed748dcd025d4cd2a4b3cc', 'table digest')
    chk(rev['independent_native_table']['sha256'] == hashlib.sha256(tab.encode()).hexdigest(), 'review digest')
    q9 = q9j['q9_table_hex']
    entry = [r for r in v14['post_hoc_degree_one_readouts'] if r['readout_bits'] == 240][0]
    law = entry['fewest_seed_law_field_coefficients_EA_EB_ED_NA_NB_ND']

    def q10(x, u, my, mr, a, b, e, n):
        i = ((((((x*2+u)*2+my)*2+mr)*2+a)*2+b)*8+e)*8+n
        return int(tab[i], 16)

    def oldq9(x, u, my, mr, a, b):
        i = (((((((x*2+u)*2+my)*2+mr)*2+a)*2+b)*8+4)*8+5)*8+7
        return int(q9[i], 16)
    acc = 0
    codes = {0: set(), 1: set()}
    q10A_s = cancel = q9ok = 0
    otp_rows = 0
    mi_terms = []
    for x, u, my, mr, a, b in product((0, 1), repeat=6):
        if (a, b) == (0, 1):
            continue
        acc += 1
        s = x ^ u ^ a
        pq = oldq9(x, u, my, mr, a, b)
        q9ok += pq == 2*s+(s ^ a ^ b)
        feat = [1, u, my, mr, a, b]
        bits = [sum(((c >> i) & 1)*feat[i] for i in range(6)) % 2 for c in law]
        e = 4*bits[0]+2*bits[1]+bits[2]
        n = 4*bits[3]+2*bits[4]+bits[5]
        c = q10(x, u, my, mr, a, b, e, n)
        q10A_s += (c >> 2) == s
        cancel += ((c >> 2) ^ (pq & 1)) == (a ^ b)
        codes[s].add(c)
        for rest in range(8):
            vals = sorted(pq ^ H(c ^ m ^ rest) for m in range(8))
            otp_rows += vals == list(range(8))
    chk(acc == 48 and q9ok == 48 and q10A_s == 48 and cancel == 48 and otp_rows == 384, 'table numbers')
    counts = v14['readout_solution_counts']
    return {'accepted': acc, 'old_q9_is_0_s_s^a^b': q9ok, 'q10A_eq_s': q10A_s,
            'q10A_xor_pD_eq_a^b': cancel, 'distinct_q10_codes_s0_s1': [len(codes[0]), len(codes[1])],
            'otp_rows': otp_rows, 'v14_count_readout240': counts[239], 'law': law}


def exact_otp():
    """Exact joint law: others O = (p, c, rest, s) with arbitrary non-uniform weights; key uniform.
    Show Pr(V, O) = Pr(V) Pr(O) exactly; countercontrol: key with non-uniform law gives dependence."""
    rng = random.Random(910)
    others = [(p, c, r) for p in range(8) for c in range(8) for r in range(8)]
    w = {o: Fraction(rng.randrange(1, 50)) for o in others}
    Z = sum(w.values())
    w = {o: v/Z for o, v in w.items()}

    def joint(keylaw):
        J = {}
        for o, po in w.items():
            p, c, r = o
            for m, pm in keylaw.items():
                v = p ^ H(c ^ m ^ r)
                J[(v, o)] = J.get((v, o), 0)+po*pm
        return J

    def indep(J):
        PV, PO = {}, {}
        for (v, o), pr in J.items():
            PV[v] = PV.get(v, 0)+pr
            PO[o] = PO.get(o, 0)+pr
        return all(J.get((v, o), 0) == PV[v]*PO[o] for v in range(8) for o in PO), PV
    uni = {m: Fraction(1, 8) for m in range(8)}
    ok, PV = indep(joint(uni))
    chk(ok and all(PV[v] == Fraction(1, 8) for v in range(8)), 'exact OTP')
    skew = {m: Fraction(1, 8) for m in range(8)}
    skew[0] += Fraction(1, 16)
    skew[1] -= Fraction(1, 16)
    ok2, _ = indep(joint(skew))
    chk(not ok2, 'OTP countercontrol non-uniform key gives dependence')
    fixed = {3: Fraction(1)}
    ok3, _ = indep(joint(fixed))
    chk(not ok3, 'OTP countercontrol fixed key gives dependence')
    return {'uniform_key_V_indep_of_arbitrary_others_exact': ok, 'skewed_key_dependence': not ok2,
            'fixed_key_dependence': not ok3}


def main():
    sg = json.loads((ROOT/'parallel_v3/history_control/SOURCE-GEOMETRY.json').read_bytes())
    sources = {tuple(r['position']) for r in sg['sources']}
    chk(len(sg['sources']) == 1479, 'source count')
    OUT['A_cones'] = dep_cones(6)
    worlds, off = perm_tests(5, (1, 2, 3, 4))
    OUT['B_perm_worlds'] = worlds
    OUT['B_offaxis_neighbours_changed_per_n'] = {str(k): v for k, v in off.items()}
    rows, hgap = actual_scale(sources)
    OUT['C_keys'] = {k: {kk: (str(vv) if isinstance(vv, int) and abs(vv) > 10**6 else vv) for kk, vv in v.items()}
                     for k, v in rows.items()}
    OUT['C_herald_family_x_gap_over_L'] = (hgap)//L
    sb = shell_banks()
    OUT['shell_banks'] = [[i, di, dd, act, [DIRS.index(f) for f in reach]] for i, di, dd, act, reach in sb]
    OUT['D_table'] = table_checks()
    OUT['D_exact_otp'] = exact_otp()
    OUT['failures'] = FAIL
    print(json.dumps(OUT, indent=1, sort_keys=True, default=str))


main()
