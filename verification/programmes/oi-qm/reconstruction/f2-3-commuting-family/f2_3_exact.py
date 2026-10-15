#!/usr/bin/env python3
"""F2-3: the commuting generator family of E1-L, as frozen in RULES.md and amendments/amendment-1.md.

Run:  python3 -I f2_3_exact.py > f2-3-exact-output.txt
Standard library only. Imports, by path and unchanged, the frozen F2-2 module
../f2-2-local-continuity/f2_2_exact.py (which itself imports the frozen F2-1 module), and prints the
sha256 of both. Labels: [X] exact (every line unless tagged), [W] written argument.
The output is deterministic (no randomness, no timing, no hash-order dependence).
"""
import hashlib
import importlib.util
import itertools
import os
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
F22_PATH = os.path.join(HERE, "..", "f2-2-local-continuity", "f2_2_exact.py")
E1_PATH = os.path.join(HERE, "..", "f2-1-e1-consistency", "e1_exact.py")
E1_SHA = "e7d257bb09f5b75d4628cd0ebd85a0b189d377b3bdf91a48fd1196705a31e7a6"
F22_SHA = "246adb2bc6590a3d84234f6937409f2042bba796d646eae633f6383a62a90e57"


def sha256(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


f22 = _load("f2_2_exact", F22_PATH)
e1 = f22.e1
out = e1.out
header = e1.header
CTRL = []
TOK = []
FR = Fraction


def control(name, ok):
    CTRL.append((name, bool(ok)))
    out("CONTROL %-58s %s" % (name, "PASS" if ok else "FAIL"))


def token(cell, size, tok):
    TOK.append((cell, size, tok))
    out("TOKEN   %-14s %-22s %s" % (cell, size, tok))


# ============================================================================ couplings and layers


def couplings(q, N, rep):
    """Symmetric couplings as tuples of tuples. rep: 'self', 'cf', or 'star' (cf with M[1][2] = 0, N = 3)."""
    res = []
    if rep == "self":
        for M in e1.symmetric_couplings(q, N):
            res.append(tuple(tuple(r) for r in M))
    else:
        for M in e1.symmetric_couplings(q, N):
            if any(M[i][i] % q for i in range(N)):
                continue
            if rep == "star" and M[1][2] % q:
                continue
            res.append(tuple(tuple(r) for r in M))
    return res


def restrict_graph(Ms, N, graph):
    """graph 'chain': drop couplings with an edge outside {i, i+1}; 'complete': keep all."""
    if graph == "complete":
        return Ms
    return [M for M in Ms if all(M[i][j] == 0 for i in range(N) for j in range(i + 2, N))]


def layer_terms(M, q):
    """[('site', (i,), a)] and [('pair', (i, j), m)] for the nonzero entries, i < j (first factor at i)."""
    N = len(M)
    t = []
    for i in range(N):
        if M[i][i] % q:
            t.append(("site", (i,), M[i][i] % q))
    for i in range(N):
        for j in range(i + 1, N):
            if M[i][j] % q:
                t.append(("pair", (i, j), M[i][j] % q))
    return t


# ============================================================================ E1: the necessary commutant


def pair_states(q):
    return list(itertools.product(range(q), repeat=2))


def conserved_quantities(q, N, Ms):
    """For each pair value m: the set of conserved functions on the pair's states (y1, y2), derived
    mechanically from every layer in which an edge of value m co-occurs with another term sharing a site.

    Each function is returned as a key; evaluation is in eval_q below.
      ('own',)               y1*y2 mod q            (the gate's own eigenspace classes)
      ('pair', role, b)      (b*y_role*z mod q for z in F_q)   another pair gate delta(b) sharing that site
      ('site', role, a)      (-h a y_role^2 mod q)             a site gate delta(a) on that site
    role 0 = first factor, 1 = second factor of the edge carrying value m."""
    keys = {m: {("own",)} for m in range(1, q)}
    for M in Ms:
        terms = layer_terms(M, q)
        for kind, sites, m in terms:
            if kind != "pair":
                continue
            for kind2, sites2, v2 in terms:
                if (kind2, sites2) == (kind, sites):
                    continue
                shared = set(sites) & set(sites2)
                for s in shared:
                    role = sites.index(s)
                    keys[m].add((kind2, role, v2))
    return keys


def eval_q(key, y, q):
    h = pow(2, -1, q)
    if key[0] == "own":
        return (y[0] * y[1]) % q
    kind, role, v = key
    x = y[role]
    if kind == "pair":
        return tuple((v * x * z) % q for z in range(q))
    return (-h * v * x * x) % q


def commutant_units(q, keys):
    """Allowed matrix units (s, t): s and t agree on every conserved quantity."""
    st = pair_states(q)
    sig = {s: tuple(eval_q(k, s, q) for k in sorted(keys, key=str)) for s in st}
    return [(s, t) for s in st for t in st if sig[s] == sig[t]]


def e1_cell(q, N, graph, rep):
    size = "q=%d,N=%d" % (q, N)
    Ms = restrict_graph(couplings(q, N, rep), N, graph)
    keys = conserved_quantities(q, N, Ms)
    res = {}
    for m in range(1, q):
        units = commutant_units(q, keys[m])
        diag = all(s == t for s, t in units)
        res[m] = (len(units), diag)
    allforced = all(d == q * q and diag for d, diag in res.values())
    out("E1 %s %-8s R_%-4s layers %5d; dim K(m) for m = 1..%d: %s; diagonal: %s"
        % (size, graph, rep, len(Ms), q - 1, [res[m][0] for m in range(1, q)],
           [res[m][1] for m in range(1, q)]))
    return allforced, res, keys, Ms


# ============================================================================ sparse rational operators


class Op:
    """Sparse operator on (F_q)^N basis: dict {(row_index, col_index): Fraction}."""

    def __init__(self, q, N, entries=None):
        self.q, self.N = q, N
        self.d = q ** N
        self.e = dict(entries or {})

    def __add__(self, other):
        r = dict(self.e)
        for k, v in other.e.items():
            r[k] = r.get(k, 0) + v
            if r[k] == 0:
                del r[k]
        return Op(self.q, self.N, r)

    def mul(self, other):
        rows = {}
        for (i, j), v in self.e.items():
            rows.setdefault(j, []).append((i, v))
        r = {}
        for (j, k), w in other.e.items():
            for i, v in rows.get(j, ()):
                r[(i, k)] = r.get((i, k), 0) + v * w
        return Op(self.q, self.N, {k: v for k, v in r.items() if v != 0})

    def comm(self, other):
        a = self.mul(other)
        b = other.mul(self)
        r = dict(a.e)
        for k, v in b.e.items():
            r[k] = r.get(k, 0) - v
            if r[k] == 0:
                del r[k]
        return Op(self.q, self.N, r)

    def is_zero(self):
        return not self.e


def index(y, q):
    i = 0
    for x in y:
        i = i * q + x
    return i


def embed(local, sites, q, N):
    """local: dict {(s_tuple, t_tuple): Fraction} on the given sites (in that order)."""
    others = [k for k in range(N) if k not in sites]
    e = {}
    for rest in itertools.product(range(q), repeat=len(others)):
        for (s, t), v in local.items():
            ys = [0] * N
            yt = [0] * N
            for k, x in zip(sites, s):
                ys[k] = x
            for k, x in zip(sites, t):
                yt[k] = x
            for k, x in zip(others, rest):
                ys[k] = x
                yt[k] = x
            e[(index(ys, q), index(yt, q))] = v
    return Op(q, N, e)


def theta(e, q):
    return Fraction(f22.sym_rep(e % q, q), q)


def G0_pair(m, q):
    """Principal diagonal pair generator of delta(m) = diag(w^{-m y1 y2})."""
    return {((a, b), (a, b)): theta(-m * a * b, q) for a in range(q) for b in range(q)}


def g0_site(a, q):
    h = pow(2, -1, q)
    return {((y,), (y,)): theta(-h * a * y * y, q) for y in range(q)}


def proj(vec):
    """vec: dict {state: Fraction amplitude} (real); projector onto it as a dict of entries."""
    nrm = sum(v * v for v in vec.values())
    return {(s, t): vec[s] * vec[t] / nrm for s in vec for t in vec}


def add_local(A, B):
    r = dict(A)
    for k, v in B.items():
        r[k] = r.get(k, 0) + v
        if r[k] == 0:
            del r[k]
    return r


def local_mul(A, B):
    r = {}
    for (s, t), v in A.items():
        for (t2, u), w in B.items():
            if t2 == t:
                r[(s, u)] = r.get((s, u), 0) + v * w
    return {k: v for k, v in r.items() if v != 0}


def K_phi(q):
    return proj({(1, 1): FR(1), (2, 2): FR(1)})


def K_C(q):
    """(1 - C(x)C)/2 with C|y> = |-y>."""
    r = {}
    for a in range(q):
        for b in range(q):
            s = (a, b)
            r[(s, s)] = r.get((s, s), 0) + FR(1, 2)
            t = ((-a) % q, (-b) % q)
            r[(t, s)] = r.get((t, s), 0) - FR(1, 2)
    return {k: v for k, v in r.items() if v != 0}


def K_star(q):
    """|0><0| (x) |chi><chi|, chi = (|1> + |2>)/sqrt2."""
    chi = {(0, 1): FR(1), (0, 2): FR(1)}
    return proj(chi)


def lifted_pair(m, q):
    """Diagonal, state-dependent lift: theta + 1 on the states with y1 = 1 (outside Gamma_spec)."""
    G = G0_pair(m, q)
    return {k: (v + (1 if k[0][0] == 1 else 0)) for k, v in G.items()}


def lifted_site(a, q):
    """Diagonal site generator separating y from -y: + 1 on 1 <= y <= (q-1)/2."""
    g = g0_site(a, q)
    return {k: (v + (1 if 1 <= k[0][0] <= (q - 1) // 2 else 0)) for k, v in g.items()}


def layers_commute(Ms, q, N, pairgen, sitegen, first_fail=True):
    """Every pair of terms of every layer commutes. Pairwise commutation depends only on the two terms,
    so each distinct pair of terms is checked once (cached), and each term is embedded once."""
    cache = {}
    emb = {}
    fails = []

    def op(t):
        if t not in emb:
            kind, sites, v = t
            loc = pairgen(v) if kind == "pair" else sitegen(v)
            emb[t] = embed(loc, sites, q, N)
        return emb[t]
    for M in Ms:
        terms = layer_terms(M, q)
        for t1, t2 in itertools.combinations(terms, 2):
            key = (t1, t2)
            if key not in cache:
                cache[key] = op(t1).comm(op(t2)).is_zero()
            if not cache[key]:
                fails.append((M, t1, t2))
                if first_fail:
                    return False, fails, len(cache)
    return not fails, fails, len(cache)


# ============================================================================ K-gen


def class_of(s, q):
    return (s[0] * s[1]) % q


def kgen(name, K, m, q, single_class):
    G0 = G0_pair(m, q)
    herm = all(K.get((t, s), 0) == v for (s, t), v in K.items())
    idem = local_mul(K, K) == K
    commG0 = local_mul(K, G0) == local_mul(G0, K)
    blockd = all(class_of(s, q) == class_of(t, q) for (s, t) in K)
    one = len({class_of(s, q) for (s, t) in K} | {class_of(t, q) for (s, t) in K}) == 1
    ok = herm and idem and commG0 and blockd and (one if single_class else True)
    out("K-gen %-8s m=%d: Hermitian %s, K^2 = K %s, [K, G0] = 0 %s, block-diagonal over classes %s, "
        "inside one class %s%s" % (name, m, herm, idem, commG0, blockd, one,
                                   "" if single_class else " (not required, amendment 1)"))
    return ok


# ============================================================================ K-brute


def kbrute(q):
    """(q,3) chain, R_cf: nullspace of X -> ([X (x) 1, 1 (x) delta_23(b)] for b != 0, [X, delta(m)]) over Q(zeta_q),
    computed by explicit matrix arithmetic on every matrix unit, for one m (the count is m-independent
    for m != 0, and both m are run)."""
    F = e1.field(q)
    d2 = q * q
    I1 = e1.eye(F, q)

    def gate_pair(b):
        D = e1.zeros(F, d2)
        for a in range(q):
            for c in range(q):
                D[a * q + c][a * q + c] = F.root(q, (-b * a * c) % q)
        return D
    res = {}
    for m in range(1, q):
        Dm = gate_pair(m)
        images = []
        for s in range(d2):
            for t in range(d2):
                E = e1.zeros(F, d2)
                E[s][t] = F.one
                vec = []
                XI = e1.kron(F, E, I1)
                for b in range(1, q):
                    IB = e1.kron(F, I1, gate_pair(b))
                    C = e1.mat_sub(F, e1.mat_mul(F, XI, IB), e1.mat_mul(F, IB, XI))
                    vec.extend(x for row in C for x in row)
                IB2 = e1.kron(F, gate_pair(b=1), I1)          # site 2 as the second factor of the other edge
                EI = e1.kron(F, I1, E)
                C2 = e1.mat_sub(F, e1.mat_mul(F, EI, IB2), e1.mat_mul(F, IB2, EI))
                vec.extend(x for row in C2 for x in row)
                Cm = e1.mat_sub(F, e1.mat_mul(F, E, Dm), e1.mat_mul(F, Dm, E))
                vec.extend(x for row in Cm for x in row)
                images.append(vec)
        rank = e1.mat_rank(F, images)
        res[m] = d2 * d2 - rank
    return res


# ============================================================================ E3: the N = 2 residual


def e3_cell(q):
    size = "q=%d,N=2" % q
    # site commutant: X on site 1 commuting with delta_12(b) embedded, every b != 0
    keys_site = [("pair", 0, b) for b in range(1, q)]
    sig = {y: tuple(tuple((b * y * z) % q for z in range(q)) for b in range(1, q)) for y in range(q)}
    units = [(s, t) for s in range(q) for t in range(q) if sig[s] == sig[t]]
    site_diag = all(s == t for s, t in units)
    out("E3 %s site commutant: dimension %d, diagonal %s" % (size, len(units), site_diag))
    token("E3-site", size, "F23-SITE-DIAG" if site_diag else "F23-SITE-NONDIAG")

    def pair_dim(sitegen):
        st = pair_states(q)
        sg = {}
        for s in st:
            sgv = [(s[0] * s[1]) % q]
            for a in range(1, q):
                g = sitegen(a)
                sgv.append(g[((s[0],), (s[0],))])
                sgv.append(g[((s[1],), (s[1],))])
            sg[s] = tuple(sgv)
        u = [(s, t) for s in st for t in st if sg[s] == sg[t]]
        return len(u), all(s == t for s, t in u)
    d_pr, diag_pr = pair_dim(lambda a: g0_site(a, q))
    d_li, diag_li = pair_dim(lambda a: lifted_site(a, q))
    out("E3 %s pair commutant with principal site generators: dimension %d (q^2 = %d), diagonal %s"
        % (size, d_pr, q * q, diag_pr))
    out("E3 %s pair commutant with y/-y-separating site generators: dimension %d, diagonal %s"
        % (size, d_li, diag_li))
    token("E3-pair(i)", size, "F23-N2-NONDIAG" if d_pr > q * q else "F23-N2-DIAG-UNDER-PRINCIPAL")
    token("E3-pair(ii)", size, "F23-N2-DIAG" if d_li == q * q else "F23-N2-NONDIAG-UNDER-LIFT")
    return site_diag, d_pr, d_li


# ============================================================================ C1, C2 at (3, 2)


def to_field_mat(F, loc_full, d):
    A = e1.zeros(F, d)
    for (i, j), v in loc_full.e.items():
        A[i][j] = F.add(A[i][j], F.frac(v))
    return A


def c_cells(R):
    q, N = 3, 2
    size = "q=3,N=2"
    Fc = e1.field(8 * q)
    GS = f22.GateSet(q, Fc)
    S = f22.Sites(GS, N)
    C = S.C
    d = S.d
    full = d * d - 1
    P0 = GS.principal_member()
    Ms = [M for M in couplings(q, N, "self") if any(x for r in M for x in r)]
    members = {"diag-principal": None, "M_phi": K_phi(q), "M_C": K_C(q)}
    dims = {}
    header("[%s] C1  all-duration Lie algebra, R_self" % size)
    for name, K in members.items():
        gens = [S.gen_free(P0)]
        for M in Ms:
            G = S.gen_coup(M, P0)
            if K is not None and M[0][1] % q:
                G = e1.mat_add(Fc, G, to_field_mat(Fc, embed(K, (0, 1), q, N), d))
            gens.append(G)
        gens += [S.gen_X(P0, k) for k in range(N)]
        dim = e1.lie_closure_dim(Fc, [[G] for G in gens], stop_at=d * d) - 1
        dims[name] = dim
        out("C1 %-15s %d generators; dimension modulo the identity %d (full = %d)" % (name, len(gens), dim, full))
        if name == "diag-principal":
            dim_nt = e1.lie_closure_dim(Fc, [[G] for G in gens[:1 + len(Ms)]], stop_at=d * d) - 1
            out("K-lie: translations removed: dimension %d" % dim_nt)
            control("K-lie dropped translations (3,2) R_self", dim_nt < full)
    token("C1", size, "F23-NONDIAG-FULL" if dims["M_phi"] == full and dims["M_C"] == full
          else "F23-NONDIAG-NOT-FULL %s" % dims)

    header("[%s] C2  half-layer gates h = exp(pi i G_coup(M))" % size)
    inv = {}
    for Mname, M in (("[[0,1],[1,0]]", ((0, 1), (1, 0))), ("[[1,1],[1,1]]", ((1, 1), (1, 1)))):
        for name, K in members.items():
            h = S.coup_flow(M, P0, Fraction(1, 2))
            if K is not None:
                Ke = to_field_mat(Fc, embed(K, (0, 1), q, N), d)
                corr = e1.mat_sub(Fc, e1.eye(Fc, d), e1.mat_scale(Fc, Fc.frac(2), Ke))
                h = e1.mat_mul(Fc, h, corr)
            unit = e1.unitary_check(Fc, h)
            sr = e1.schmidt_rank(Fc, h, q)
            nf = e1.normalizer_failures(C, h)
            v = [row[0] for row in h]
            W = e1.wigner(C, v)
            neg = any(e1.real_sign(Fc, w) < 0 for w in W.values())
            isdiag = all(Fc.is_zero(h[i][j]) for i in range(d) for j in range(d) if i != j)
            inv[(Mname, name)] = (sr, not nf, neg, isdiag)
            out("C2 M=%s %-15s unitary %s; Schmidt rank %d; Clifford %s; h|00> Wigner-negative %s; diagonal %s"
                % (Mname, name, unit, sr, not nf, neg, isdiag))
    diffs = []
    for Mname in ("[[0,1],[1,0]]", "[[1,1],[1,1]]"):
        base = inv[(Mname, "diag-principal")]
        for name in ("M_phi", "M_C"):
            labels = ["Schmidt rank", "Clifford", "Wigner-negative", "diagonal"]
            dd = [labels[i] for i in range(4) if inv[(Mname, name)][i] != base[i]]
            if dd:
                diffs.append("%s at %s: %s" % (name, Mname, ", ".join(dd)))
    same_alg = dims["M_phi"] == dims["diag-principal"] and dims["M_C"] == dims["diag-principal"]
    token("C2", size, ("F23-NO-NEW-ALGEBRA" if same_alg else "F23-ALGEBRA-DIFFERS"))
    token("C2", size, "F23-GATE-DIFFERENCES: " + ("; ".join(diffs) if diffs else "none"))
    R["c1"] = dims
    R["c2_diffs"] = diffs
    return dims, diffs


# ============================================================================ main


def main():
    R = {}
    header("F2-3  the commuting generator family of E1-L")
    e1_sha = sha256(E1_PATH)
    f22_sha = sha256(F22_PATH)
    out("imported F2-1 module sha256 %s" % e1_sha)
    out("imported F2-2 module sha256 %s" % f22_sha)
    st = e1.self_tests()
    control("K0 module hashes and F2-1 self-tests", e1_sha == E1_SHA and f22_sha == F22_SHA and st)

    header("E1  the necessary commutant (combinatorial, exact), and E2 diagonal sufficiency")
    forced = {}
    for q in (3, 5, 7):
        N = 3
        size = "q=%d,N=3" % q
        for graph in ("chain", "complete"):
            for rep in ("cf", "self"):
                ok, res, keys, Ms = e1_cell(q, N, graph, rep)
                forced[(q, graph, rep)] = ok
                token("E1", "%s %s R_%s" % (size, graph, rep), "F23-DIAG-FORCED" if ok else
                      "F23-NONDIAG-ALLOWED dims %s" % [res[m][0] for m in range(1, q)])
                # E2: two diagonal members commute on every layer
                okp, _, npairs = layers_commute(Ms, q, N, lambda m: G0_pair(m, q), lambda a: g0_site(a, q))
                okl, _, _ = layers_commute(Ms, q, N, lambda m: lifted_pair(m, q), lambda a: g0_site(a, q))
                out("E2 %s %-8s R_%-4s principal diagonal: all layers commute %s (%d distinct term pairs); "
                    "state-dependent lifted diagonal: %s" % (size, graph, rep, okp, npairs, okl))
                control("K-pos diagonal members commute %s %s R_%s" % (size, graph, rep), okp and okl)
                token("E2", "%s %s R_%s" % (size, graph, rep), "F23-DIAG-SUFFICES" if (okp and okl) else
                      "F23-DIAG-FAILS")

    header("K-gen  the exhibited generators exponentiate to their gates")
    q = 3
    okg = True
    for m in range(1, q):
        okg &= kgen("M_phi", K_phi(q), m, q, True)
        okg &= kgen("M_C", K_C(q), m, q, False)
        okg &= kgen("R_star", K_star(q), m, q, True)
    control("K-gen exhibited generators", okg)

    header("K-neg  the (3,2) non-diagonal members on the (3,3) chain")
    q, N = 3, 3
    Ms_chain = restrict_graph(couplings(q, N, "cf"), N, "chain")
    _, res_chain, _, _ = e1_cell(q, N, "chain", "cf")
    for name, K in (("M_phi", K_phi(q)), ("M_C", K_C(q))):
        okc, fails, _ = layers_commute(Ms_chain, q, N, lambda m, K=K: add_local(G0_pair(m, q), K),
                                       lambda a: g0_site(a, q))
        outside = any(s != t for (s, t) in K)
        out("K-neg %s: all chain layers commute %s; first failing layer %s; has off-diagonal units outside the "
            "chain's diagonal K(m): %s" % (name, okc, fails[0][0] if fails else None, outside))
        control("K-neg %s fails on the (3,3) chain" % name, (not okc) and outside)

    header("K-mut  the single-role star repertoire R_star at (3,3)")
    Ms_star = couplings(q, N, "star")
    keys = conserved_quantities(q, N, Ms_star)
    dims = {m: len(commutant_units(q, keys[m])) for m in range(1, q)}
    out("K-mut R_star layers %d; dim K(m) %s (q^2 = %d)" % (len(Ms_star), [dims[m] for m in range(1, q)], q * q))
    oks, _, _ = layers_commute(Ms_star, q, N, lambda m: add_local(G0_pair(m, q), K_star(q)), lambda a: g0_site(a, q))
    okc, _, _ = layers_commute(Ms_chain, q, N, lambda m: add_local(G0_pair(m, q), K_star(q)), lambda a: g0_site(a, q))
    out("K-mut star member: commutes on every R_star layer %s; on every chain layer %s" % (oks, okc))
    control("K-mut star commutant larger than diagonal", all(v > q * q for v in dims.values()))
    control("K-mut star member commutes on R_star and fails on the chain", oks and not okc)

    header("K-brute  independent nullspace computation, (3,3) chain, R_cf")
    kb = kbrute(3)
    comb = {m: res_chain[m][0] for m in range(1, 3)}
    out("K-brute nullity per m %s; combinatorial dim K(m) %s" % (kb, comb))
    control("K-brute agrees with E1 at (3,3) chain R_cf", kb == comb)

    header("E3  the N = 2 residual under R_self")
    e3 = {q: e3_cell(q) for q in (3, 5)}

    c_cells(R)

    header("Summary")
    for t in TOK:
        out("%-14s %-24s %s" % t)
    verdict(forced)


def verdict(forced):
    header("Verdict")
    bad = [n for n, ok in CTRL if not ok]
    if bad:
        out("failed controls: %s" % bad)
        out("VERDICT VOID")
        return
    out("outcome rule: F23-DIAG-FORCED and F23-DIAG-SUFFICES at every N = 3 size, graph and repertoire")
    alld = all(forced.values()) and all(t[2] == "F23-DIAG-SUFFICES" for t in TOK if t[0] == "E2")
    out("VERDICT " + ("F23-DIAGONAL-AT-N3" if alld else "F23-NONDIAGONAL-AT-N3"))


if __name__ == "__main__":
    main()
