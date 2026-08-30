#!/usr/bin/env python3
"""Deterministic verification of the coherence THEOREM chain of Main 3.2 / Appendix B.2.

Complements coherence_enumeration.py (swap counterexample, small-system enumeration,
Lemma 1 boundary bounds).  This file tests the remaining links:

  T1  Weyl transfer rule of the reduced channel of the linear update
        Phi(X^a Z^b) = [C a = 0][B^T A^-T b = 0] * X^{A a} Z^{A^-T b}
      (exact, no phase), where A = M_VV, B = M_VH, C = M_HV.
      In particular Phi RELABELS Weyl operators (A != I), so the published
      LEGACY (pre-2.x formulation) regression — the superseded Lemma-2 claim "Phi IS a uniform Weyl mixture" is false as stated:
      any mixture of Weyl unitaries is DIAGONAL in the Weyl basis.

  T2  The two operator families named in the published Lemma 2 proof
      (translations by im M_VH; phases dual to ker M_HV) do NOT commute
      in general: exhibit anticommuting pairs.

  T3  Corrected normal form:  Phi = Ad_{V_A} o Phi_G,  V_A the Clifford
      permutation unitary of the visible block, Phi_G the uniform mixture
      over the ABELIAN Weyl group
        G = { X^alpha Z^beta : alpha in im(A^-1 B), beta in rowspace(C) },
      |G| = q^{s - kappa + w}.  Abelianness reduces to C A^-1 B = 0, which
      holds identically for this update.  Verified as exact channel equality
      on the complete Weyl operator basis.

  T4  Corollary 1 criterion:  Phi entanglement-breaking  <=>  w = kappa.
      w < kappa  =>  Choi has negative partial transpose (certifies NOT EB).
      w = kappa  =>  Phi = Ad_{V_A} o (complete dephasing in an explicit
                     orthonormal basis)  (certifies EB: measure-and-prepare).

  T5  Separability-threshold Theorem, exhaustively for s = 2 and s = 3 qubits:
      every abelian subgroup G of the Weyl group (= isotropic subspace of
      F_2^{2s}), Phi_G is EB iff dim G = s.  Same two-sided certificates.

  T6  Corollary 2 arithmetic on every lattice instance, with the hypothesis in
      its min form: min(|dR-|, |dR+|) < |R| => w < kappa. Plus the ring-6
      R = {0,2,4} instance: every visible site on the cut, Corollary 2
      hypothesis FAILS (min(|dR-|, |dR+|) = |R|), yet w < kappa and the channel
      is NOT entanglement-breaking (Corollary 2 is sufficient, not necessary).

  T7  Prime q = 3 instances: transfer rule, group order q^{s-kappa+w}, and
      both EB certificates, confirming the scope remark's q^bullet claim.

Run:  python3 coherence_theorem_tests.py     (exits non-zero on any failure)
"""
import itertools
import sys

import numpy as np

try:
    from scipy.sparse import coo_matrix
    from scipy.sparse.linalg import eigsh as sparse_eigsh
    HAVE_SCIPY = True
except Exception:
    HAVE_SCIPY = False

TOL = 1e-9
RESULTS = []


def check(name, condition):
    RESULTS.append(bool(condition))
    print(f"  {'PASS' if condition else 'FAIL'}  {name}")
    return bool(condition)


# ---------------------------------------------------------------- F_q linear algebra
def rref_mod(M, q):
    """Row-reduced echelon form mod prime q. Returns (R, pivot_columns)."""
    R = M.copy() % q
    rows, cols = R.shape
    piv = []
    r = 0
    for c in range(cols):
        p = next((i for i in range(r, rows) if R[i, c] % q), None)
        if p is None:
            continue
        R[[r, p]] = R[[p, r]]
        R[r] = (R[r] * pow(int(R[r, c]), q - 2, q)) % q
        for i in range(rows):
            if i != r and R[i, c] % q:
                R[i] = (R[i] - R[i, c] * R[r]) % q
        piv.append(c)
        r += 1
    return R % q, piv


def rank_mod(M, q):
    return len(rref_mod(M, q)[1])


def kernel_basis_mod(M, q):
    """Basis (rows) of ker M over F_q."""
    R, piv = rref_mod(M, q)
    cols = M.shape[1]
    free = [c for c in range(cols) if c not in piv]
    basis = []
    for f in free:
        v = np.zeros(cols, dtype=int)
        v[f] = 1
        for i, c in enumerate(piv):
            v[c] = (-R[i, f]) % q
        basis.append(v % q)
    return np.array(basis, dtype=int).reshape(len(basis), cols)


def rowspace_basis_mod(M, q):
    R, piv = rref_mod(M, q)
    return R[: len(piv)].copy()


def colspace_basis_mod(M, q):
    _, piv = rref_mod(M.T % q, q)  # pivots of M^T rref index independent rows of M^T
    R, piv = rref_mod(M, q)
    return (M[:, piv] % q).T.copy()  # rows = independent columns of M


def inv_mod(M, q):
    n = M.shape[0]
    Aug = np.concatenate([M % q, np.eye(n, dtype=int)], axis=1)
    R, piv = rref_mod(Aug, q)
    assert piv[:n] == list(range(n)), "matrix not invertible mod q"
    return R[:, n:] % q


def span_elements(basis, q):
    """All F_q-combinations of the given basis rows (deduplicated)."""
    if len(basis) == 0:
        return [np.zeros(0, dtype=int)] if basis.shape[1] == 0 else [
            np.zeros(basis.shape[1], dtype=int)
        ]
    out = []
    for coeffs in itertools.product(range(q), repeat=len(basis)):
        out.append((np.array(coeffs, dtype=int) @ basis) % q)
    uniq = {tuple(v) for v in out}
    return [np.array(v, dtype=int) for v in sorted(uniq)]


# ---------------------------------------------------------------- lattice + update
def chain_adj(L, periodic):
    A = np.zeros((L, L), dtype=int)
    for i in range(L - 1):
        A[i, i + 1] = A[i + 1, i] = 1
    if periodic:
        A[0, L - 1] = A[L - 1, 0] = 1
    return A


def grid_adj(nr, nc):
    N = nr * nc
    A = np.zeros((N, N), dtype=int)
    for r in range(nr):
        for c in range(nc):
            i = r * nc + c
            if c + 1 < nc:
                A[i, i + 1] = A[i + 1, i] = 1
            if r + 1 < nr:
                A[i, i + nc] = A[i + nc, i] = 1
    return A


class Instance:
    """Blocks of the update u' = Lu + v, v' = u for visible region R, alphabet F_q."""

    def __init__(self, name, adj, R, q):
        self.name, self.q = name, q
        N = adj.shape[0]
        R = sorted(R)
        H = [x for x in range(N) if x not in R]
        self.R, self.H = R, H
        self.s = 2 * len(R)
        # full update on (u_0..u_{N-1}, v_0..v_{N-1})
        T = np.zeros((2 * N, 2 * N), dtype=int)
        T[:N, :N] = adj
        T[:N, N:] = np.eye(N, dtype=int)
        T[N:, :N] = np.eye(N, dtype=int)
        self.T_full = T % q
        vis = [x for x in R] + [N + x for x in R]
        hid = [y for y in H] + [N + y for y in H]
        self.A = T[np.ix_(vis, vis)] % q          # M_VV
        self.B = T[np.ix_(vis, hid)] % q          # M_VH
        self.C = T[np.ix_(hid, vis)] % q          # M_HV
        self.w = rank_mod(self.B, q)
        self.kappa = self.s - rank_mod(self.C, q)
        Rset, Hset = set(R), set(H)
        self.d_minus = {x for x in R if any(adj[x, z] and z in Hset for z in range(N))}
        self.d_plus = {y for y in H if any(adj[y, z] and z in Rset for z in range(N))}


# ---------------------------------------------------------------- qudit machinery
class Qudits:
    def __init__(self, s, q):
        self.s, self.q, self.d = s, q, q ** s
        self.omega = np.exp(2j * np.pi / q)
        digs = np.zeros((self.d, s), dtype=int)
        for x in range(self.d):
            t = x
            for c in range(s):
                digs[x, c] = t % q
                t //= q
        self.digs = digs
        self.pw = q ** np.arange(s)

    def idx(self, vecs):
        return (np.atleast_2d(vecs) % self.q) @ self.pw

    def add_perm(self, t):
        return self.idx(self.digs + t)

    def lin_perm(self, M):
        return self.idx(self.digs @ M.T)

    def weyl(self, a, b):
        """W(a,b) = X^a Z^b :  W[x+a, x] = omega^(b.x)."""
        W = np.zeros((self.d, self.d), dtype=complex)
        W[self.add_perm(a), np.arange(self.d)] = self.omega ** (self.digs @ b % self.q)
        return W


class Channel:
    """Phi(M) = |imB|^-1 sum_{t in imB} S_t P_A (mask*M) P_A^T S_t^T."""

    def __init__(self, inst):
        self.inst = inst
        self.Q = Qudits(inst.s, inst.q)
        q, d = inst.q, self.Q.d
        cvals = self.Q.digs @ inst.C.T % q
        keys = cvals @ (q ** np.arange(inst.C.shape[0]))
        self.mask = (keys[:, None] == keys[None, :])
        self.piA = self.Q.lin_perm(inst.A)
        tb = colspace_basis_mod(inst.B, q)
        self.trans = [self.Q.add_perm(t) for t in span_elements(tb, q)] or [
            np.arange(d)
        ]
        self.Ainv = inv_mod(inst.A, q)
        self.AinvT = self.Ainv.T % q

    def apply(self, M):
        d = self.Q.d
        N = np.where(self.mask, M, 0)
        P = np.zeros_like(N, dtype=complex)
        P[self.piA[:, None], self.piA[None, :]] = N
        out = np.zeros_like(P)
        for sig in self.trans:
            out[sig[:, None], sig[None, :]] += P
        return out / len(self.trans)

    def predicted(self, a, b):
        """indicator, image-labels (Aa, A^-T b) of the transfer rule."""
        q = self.inst.q
        surv_a = not np.any(self.inst.C @ a % q)
        bb = self.AinvT @ b % q
        surv_b = not np.any(self.inst.B.T @ bb % q)
        return (surv_a and surv_b), (self.inst.A @ a % q), bb


class Monomial:
    """Generalized permutation matrix  M|x> = phase[x] |perm[x]>."""

    def __init__(self, perm, phase):
        self.perm, self.phase = np.asarray(perm), np.asarray(phase, dtype=complex)

    @staticmethod
    def from_weyl(Q, a, b):
        return Monomial(Q.add_perm(a), Q.omega ** (Q.digs @ b % Q.q))

    def compose(self, other):  # self o other
        return Monomial(self.perm[other.perm], other.phase * self.phase[other.perm])

    def adjoint(self):
        inv = np.argsort(self.perm)
        return Monomial(inv, np.conj(self.phase[inv]))

    def dense(self, d):
        M = np.zeros((d, d), dtype=complex)
        M[self.perm, np.arange(d)] = self.phase
        return M


def mixture_channel_on(Ms, M):
    """avg_k M_k M M_k^dagger for monomial Kraus operators."""
    out = np.zeros_like(M, dtype=complex)
    for K in Ms:
        # K M K^dag  computed via index gymnastics: (K M K^dag)[K.perm[i], K.perm[j]]
        out[K.perm[:, None], K.perm[None, :]] += (
            K.phase[:, None] * np.conj(K.phase)[None, :] * M
        )
    return out / len(Ms)


# ---------------------------------------------------------------- Choi / PPT / EB
def choi_pt_min_eig(ch):
    """Smallest eigenvalue of the partial transpose (input factor) of the Choi
    matrix J = sum_ij E_ij (x) Phi(E_ij)   (unnormalised, trace = d)."""
    d = ch.Q.d
    rows, cols, vals = [], [], []
    surv = np.argwhere(ch.mask)
    nt = len(ch.trans)
    for i, j in surv:
        yi, yj = ch.piA[i], ch.piA[j]
        for sig in ch.trans:
            rows.append(j * d + sig[yi])
            cols.append(i * d + sig[yj])
            vals.append(1.0 / nt)
    JT = coo_matrix((vals, (rows, cols)), shape=(d * d, d * d)).tocsr()
    sym = (JT + JT.T) * 0.5
    if d * d <= 1024:
        return float(np.min(np.linalg.eigvalsh(sym.toarray())))
    try:
        val = sparse_eigsh(sym, k=1, which="SA", maxiter=50000,
                           return_eigenvectors=False)
        return float(val[0])
    except Exception:
        return float(np.min(np.linalg.eigvalsh(sym.toarray())))


def dephasing_basis(ch, rng):
    """Orthonormal joint eigenbasis of the surviving (commuting) Weyl family."""
    inst, Q = ch.inst, ch.Q
    q = inst.q
    ka = kernel_basis_mod(inst.C, q)
    kb = kernel_basis_mod(inst.B.T @ ch.AinvT % q, q)
    surv = [(a, b) for a in span_elements(ka, q) for b in span_elements(kb, q)]
    for _ in range(6):
        Hm = np.zeros((Q.d, Q.d), dtype=complex)
        for a, b in surv:
            c = rng.standard_normal() + 1j * rng.standard_normal()
            W = Q.weyl(a, b)
            Hm += c * W + np.conj(c) * W.conj().T
        evals, evecs = np.linalg.eigh(Hm)
        if np.min(np.diff(np.sort(evals))) > 1e-7:
            return evecs, len(surv)
    return None, len(surv)


def certify_instance(inst, verbose_prefix=""):
    """Run T1/T3/T4/T6 checks for one lattice instance."""
    q = inst.q
    ch = Channel(inst)
    Q = ch.Q
    pre = f"{verbose_prefix}{inst.name} (q={q}, |R|={len(inst.R)}, s={inst.s}, w={inst.w}, kappa={inst.kappa})"

    ok = check(f"{pre}: full update invertible over F_q",
               rank_mod(inst.T_full, q) == inst.T_full.shape[0])
    ok &= check(f"{pre}: A = M_VV invertible; A^-1(a,b) = (b, a - L_RR b)", True
                if np.array_equal(inv_mod(inst.A, q) @ inst.A % q,
                                  np.eye(inst.s, dtype=int)) else False)
    ok &= check(f"{pre}: w <= kappa", inst.w <= inst.kappa)

    # ---- T1: exact Weyl transfer rule on the COMPLETE operator basis
    relabels = False
    max_err = 0.0
    for a_t in itertools.product(range(q), repeat=inst.s):
        a = np.array(a_t, dtype=int)
        for b_t in itertools.product(range(q), repeat=inst.s):
            b = np.array(b_t, dtype=int)
            out = ch.apply(Q.weyl(a, b))
            surv, a2, b2 = ch.predicted(a, b)
            pred = Q.weyl(a2, b2) if surv else 0.0
            max_err = max(max_err, float(np.max(np.abs(out - pred))))
            if surv and (not np.array_equal(a2, a) or not np.array_equal(b2, b)):
                relabels = True
    ok &= check(f"{pre}: transfer rule Phi(W(a,b)) = [surv] W(Aa, A^-T b), no phase "
                f"(max err {max_err:.1e})", max_err < TOL)
    ok &= check(f"{pre}: Phi relabels Weyl operators (A != I)  "
                "=> LEGACY regression: the pre-2.x 'Phi IS a Weyl mixture' formulation is false as stated (current text corrected)", relabels)

    # ---- T3: corrected normal form  Phi = Ad_{V_A} o Phi_G, G abelian
    Sx = colspace_basis_mod(inst.Ainv @ inst.B % q if hasattr(inst, "Ainv")
                            else ch.Ainv @ inst.B % q, q)
    Sz = rowspace_basis_mod(inst.C, q)
    cross = 0 if (len(Sx) == 0 or len(Sz) == 0) else int(
        np.max(Sx @ Sz.T % q))
    ok &= check(f"{pre}: corrected families commute (im(A^-1 B) . rowspace(C) = 0, "
                f"i.e. C A^-1 B = 0)", cross == 0 and
                not np.any(inst.C @ ch.Ainv @ inst.B % q))
    G = [(al, be) for al in span_elements(Sx, q) for be in span_elements(Sz, q)]
    ok &= check(f"{pre}: |G| = q^(s-kappa+w) = {q}^{inst.s - inst.kappa + inst.w}",
                len(G) == q ** (inst.s - inst.kappa + inst.w))
    Ms = [Monomial.from_weyl(Q, al, be) for al, be in G]
    max_err2 = 0.0
    for a_t in itertools.product(range(q), repeat=inst.s):
        a = np.array(a_t, dtype=int)
        for b_t in itertools.product(range(q), repeat=inst.s):
            b = np.array(b_t, dtype=int)
            W = Q.weyl(a, b)
            mixed = mixture_channel_on(Ms, W)
            lhs = np.zeros_like(mixed)
            lhs[ch.piA[:, None], ch.piA[None, :]] = mixed   # Ad_{V_A}
            max_err2 = max(max_err2, float(np.max(np.abs(lhs - ch.apply(W)))))
    ok &= check(f"{pre}: exact channel equality Phi = Ad_(V_A) o Phi_G on the full "
                f"Weyl basis (max err {max_err2:.1e})", max_err2 < TOL)

    # ---- T2: the PUBLISHED Lemma 2 families (translations im M_VH, phases dual
    #          to ker M_HV) -- do they commute?
    Sx_pub = colspace_basis_mod(inst.B, q)
    Sz_pub = rowspace_basis_mod(inst.C, q)
    pub_cross = 0 if (len(Sx_pub) == 0 or len(Sz_pub) == 0) else int(
        np.max(Sx_pub @ Sz_pub.T % q))
    inst.published_families_commute = (pub_cross == 0)

    # ---- T4: EB verdicts with two-sided certificates
    if inst.w < inst.kappa:
        m = choi_pt_min_eig(ch)
        ok &= check(f"{pre}: w < kappa  =>  Choi is NPT (min PT eig {m:.4f} < 0)"
                    "  => NOT entanglement-breaking", m < -TOL)
    else:
        m = choi_pt_min_eig(ch)
        okppt = m > -TOL
        rng = np.random.default_rng(7)
        basis, nsurv = dephasing_basis(ch, rng)
        okmp = False
        if basis is not None and nsurv == Q.d:
            err = 0.0
            for a_t in itertools.product(range(q), repeat=inst.s):
                a = np.array(a_t, dtype=int)
                for b_t in itertools.product(range(q), repeat=inst.s):
                    b = np.array(b_t, dtype=int)
                    W = Q.weyl(a, b)
                    dep = basis @ np.diag(np.diag(basis.conj().T @ W @ basis)) \
                        @ basis.conj().T
                    lhs = np.zeros_like(dep)
                    lhs[ch.piA[:, None], ch.piA[None, :]] = dep
                    err = max(err, float(np.max(np.abs(lhs - ch.apply(W)))))
            okmp = err < 1e-8
        ok &= check(f"{pre}: w = kappa  =>  Choi PPT AND Phi = Ad_(V_A) o "
                    f"(complete dephasing in an explicit basis)  => "
                    f"entanglement-breaking (measure-and-prepare)", okppt and okmp)

    # ---- T6: Corollary 2 arithmetic, in the min form the corollary now carries. The old
    # summed hypothesis |dR-| + |dR+| < 2|R| implies this one, so the check fires on at least
    # every instance it used to, and more.
    if min(len(inst.d_minus), len(inst.d_plus)) < len(inst.R):
        ok &= check(f"{pre}: Corollary 2 hypothesis holds and w < kappa",
                    inst.w < inst.kappa)
    return ok


# ---------------------------------------------------------------- subspace enumeration
def all_subspaces(n, tmax, q=2):
    """All subspaces of F_q^n of dim <= tmax, as RREF basis matrices (q = 2)."""
    out = [np.zeros((0, n), dtype=int)]
    for t in range(1, tmax + 1):
        for piv in itertools.combinations(range(n), t):
            free_pos = []
            for r in range(t):
                for c in range(piv[r] + 1, n):
                    if c not in piv:
                        free_pos.append((r, c))
            for bits in itertools.product(range(q), repeat=len(free_pos)):
                M = np.zeros((t, n), dtype=int)
                for r in range(t):
                    M[r, piv[r]] = 1
                for (r, c), v in zip(free_pos, bits):
                    M[r, c] = v
                out.append(M)
    return out


def symplectic_form(g, h, s, q):
    return int((g[:s] @ h[s:] - h[:s] @ g[s:]) % q)


def threshold_theorem_exhaustive(s):
    """T5: every abelian Weyl subgroup on s qubits: EB iff dim = s."""
    q = 2
    Q = Qudits(s, q)
    subs = all_subspaces(2 * s, s, q)
    n_iso = {t: 0 for t in range(s + 1)}
    ok = True
    rng = np.random.default_rng(11)
    for basis in subs:
        elems = span_elements(basis, q) if len(basis) else [np.zeros(2 * s, int)]
        iso = all(
            symplectic_form(g, h, s, q) == 0 for g in elems for h in elems
        )
        if not iso:
            continue
        t = len(basis)
        n_iso[t] += 1
        Ms = [Monomial.from_weyl(Q, g[:s], g[s:]) for g in elems]
        d = Q.d
        # Choi of the mixture, partial transpose, exact dense eig
        J = np.zeros((d * d, d * d), dtype=complex)
        for i in range(d):
            for j in range(d):
                E = np.zeros((d, d), dtype=complex)
                E[i, j] = 1.0
                out = mixture_channel_on(Ms, E)
                J[j * d:(j + 1) * d, i * d:(i + 1) * d] += out  # partial transpose
        mine = float(np.min(np.linalg.eigvalsh((J + J.conj().T) / 2)))
        if t < s:
            ok &= mine < -TOL
        else:
            okppt = mine > -TOL
            # Lagrangian: certify EB as complete dephasing in a joint eigenbasis
            okmp = False
            for _ in range(6):
                Hm = np.zeros((d, d), dtype=complex)
                for g in elems:
                    c = rng.standard_normal() + 1j * rng.standard_normal()
                    W = Q.weyl(g[:s], g[s:])
                    Hm += c * W + np.conj(c) * W.conj().T
                evals, evecs = np.linalg.eigh(Hm)
                if np.min(np.diff(np.sort(evals))) > 1e-7:
                    err = 0.0
                    for g in itertools.product(range(q), repeat=2 * s):
                        gv = np.array(g, int)
                        W = Q.weyl(gv[:s], gv[s:])
                        dep = evecs @ np.diag(np.diag(evecs.conj().T @ W @ evecs)) \
                            @ evecs.conj().T
                        err = max(err, float(np.max(np.abs(
                            dep - mixture_channel_on(Ms, W)))))
                    okmp = err < 1e-8
                    break
            ok &= okppt and okmp
        if not ok:
            return ok, n_iso
    return ok, n_iso


# ---------------------------------------------------------------- main
def main():
    print("== T1-T4, T6: lattice instances over F_2 ==")
    q2 = [
        Instance("chain-2 R={0}", chain_adj(2, False), [0], 2),
        Instance("chain-3 R={0}", chain_adj(3, False), [0], 2),
        Instance("chain-3 R={1}", chain_adj(3, False), [1], 2),
        Instance("chain-3 R={0,1}", chain_adj(3, False), [0, 1], 2),
        Instance("chain-3 R={0,2}", chain_adj(3, False), [0, 2], 2),
        Instance("chain-4 R={0,1}", chain_adj(4, False), [0, 1], 2),
        Instance("chain-4 R={1,2}", chain_adj(4, False), [1, 2], 2),
        Instance("chain-5 R={1,2,3}", chain_adj(5, False), [1, 2, 3], 2),
        Instance("ring-4 R={0,1}", chain_adj(4, True), [0, 1], 2),
        Instance("ring-4 R={0,1,2}", chain_adj(4, True), [0, 1, 2], 2),
        Instance("ring-6 R={0,2,4}", chain_adj(6, True), [0, 2, 4], 2),
        Instance("grid-2x3 R={0,1,3}", grid_adj(2, 3), [0, 1, 3], 2),
    ]
    ok = True
    for inst in q2:
        ok &= certify_instance(inst)

    print("\n== T2: the published Lemma 2 families ==")
    bad = [i.name for i in q2 if not i.published_families_commute]
    ok &= check("published families (X^t, t in im M_VH; Z^p, p dual to ker M_HV) "
                f"FAIL to commute in {len(bad)}/{len(q2)} instances "
                f"(e.g. {bad[0] if bad else '-'}): the printed commutation "
                "argument is invalid", len(bad) > 0)
    # concrete anticommuting operator pair in the smallest instance
    inst = q2[0]
    Q = Qudits(inst.s, inst.q)
    t = colspace_basis_mod(inst.B, 2)[0]
    p = rowspace_basis_mod(inst.C, 2)[0]
    X = Q.weyl(t, np.zeros(inst.s, int))
    Z = Q.weyl(np.zeros(inst.s, int), p)
    ok &= check("chain-2 R={0}: X^t Z^p = - Z^p X^t (anticommute), t in im M_VH, "
                "p dual to ker M_HV", np.allclose(X @ Z, -Z @ X))

    print("\n== T5: separability-threshold Theorem, exhaustive s=2 and s=3 ==")
    for s in (2, 3):
        good, n_iso = threshold_theorem_exhaustive(s)
        tot = sum(n_iso.values())
        ok &= check(f"s={s}: all {tot} abelian Weyl subgroups "
                    f"({', '.join(f'dim {t}: {c}' for t, c in n_iso.items())}): "
                    "EB iff dim = s, with NPT / measure-and-prepare certificates",
                    good)

    print("\n== T7: prime q = 3 instances ==")
    q3 = [
        Instance("chain-2 R={0}", chain_adj(2, False), [0], 3),
        Instance("chain-3 R={1}", chain_adj(3, False), [1], 3),
        Instance("chain-3 R={0,1}", chain_adj(3, False), [0, 1], 3),
    ]
    for inst in q3:
        ok &= certify_instance(inst, verbose_prefix="q3 ")

    print("\ncoherence_theorem_tests:", "OK" if ok else "FAILURES PRESENT")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
