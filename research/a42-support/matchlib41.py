"""Label matchings of a Dita structure, factorized by group.

Index sets: column blocks B_c (c < m, n columns each) and row groups G_b (b < n, m rows each; the rows of G_b are
proportional to each other on every block). The Dita form H[(a,b),(c,d)] = X[a][c] Y_c[b][d] also fixes, inside each
group, which row carries the label a (X is shared by the groups). With G_0 labelled in sorted order (a simultaneous
relabelling of every group changes nothing), a matching is a permutation s_b of range(m) per group b >= 1, row(a, b) =
G_b[s_b[a]]. Every rank-one condition involves one group b and group 0 only:
   strict   lam(a,b,c) = lam(a,0,c)                               lam(a,b,c) = H[row(a,b)][B_c[0]] / H[row(0,b)][B_c[0]]
   relaxed  lam(a,b,c) lam(a,0,0) = lam(a,0,c) lam(a,b,0)         (diagonal equivalence)
so the valid matchings are the product over b of the valid s_b, and linear membership of an exponent matrix factorizes
the same way. The act-36/37 search and the act-38 membership test use s_b = identity (sorted groups) only."""
import itertools


def lam(H, blocks, groups, sb, b, a, c, div):
    return div(H(groups[b][sb[a]], blocks[c][0]), H(groups[b][sb[0]], blocks[c][0]))


def group_valid(H, blocks, groups, b, sb, relaxed, div):
    m = len(groups[0]); s0 = tuple(range(m))
    for a in range(m):
        for c in range(m):
            l = lam(H, blocks, groups, sb, b, a, c, div); l0 = lam(H, blocks, groups, s0, 0, a, c, div)
            if not relaxed:
                if l != l0: return False
            elif div(l, l0) != div(lam(H, blocks, groups, sb, b, a, 0, div), lam(H, blocks, groups, s0, 0, a, 0, div)):
                return False
    return True


def valid_per_group(H, blocks, groups, relaxed, div):
    """[None] + [list of valid s_b for b = 1..n-1]; the valid matchings are their product"""
    m, n = len(groups[0]), len(groups)
    return [None] + [[sb for sb in itertools.permutations(range(m)) if group_valid(H, blocks, groups, b, sb, relaxed, div)]
                     for b in range(1, n)]


def n_matchings(vpg):
    out = 1
    for L in vpg[1:]: out *= len(L)
    return out


# ---- linear conditions on an exponent matrix E: entry (i,j) is variable 16 i + j; tr=True: the structure on E^T ----
def _v(i, j, tr): return (j * 16 + i) if tr else (i * 16 + j)


def prop_eqs(blocks, groups, tr):
    """rows of one group proportional on every block (matching independent); equations as {var: coef}"""
    eqs = []
    for B in blocks:
        for G_ in groups:
            for i in G_[1:]:
                for j in B[1:]:
                    e = {}
                    for (ii, jj, cf) in ((i, j, 1), (G_[0], j, -1), (i, B[0], -1), (G_[0], B[0], 1)):
                        k = _v(ii, jj, tr); e[k] = e.get(k, 0) + cf
                    e = {k: v for k, v in e.items() if v}
                    if e: eqs.append(e)
    return eqs


def lam_eqs(blocks, groups, b, sb, relaxed, tr):
    """the rank-one conditions of group b under s_b, linear in E"""
    m = len(groups[0]); s0 = tuple(range(m)); eqs = []

    def L(bb, s, a, c):
        return [(_v(groups[bb][s[a]], blocks[c][0], tr), 1), (_v(groups[bb][s[0]], blocks[c][0], tr), -1)]
    for a in range(m):
        for c in range(m):
            if relaxed and c == 0: continue
            terms = L(b, sb, a, c) + [(k, -x) for k, x in L(0, s0, a, c)]
            if relaxed: terms += [(k, -x) for k, x in L(b, sb, a, 0)] + L(0, s0, a, 0)
            e = {}
            for k, x in terms: e[k] = e.get(k, 0) + x
            e = {k: v for k, v in e.items() if v}
            if e: eqs.append(e)
    return eqs


def satisfies(flat, eqs):
    return all(sum(c * flat[k] for k, c in e.items()) == 0 for e in eqs)


def member_complete(flat, st, relaxed):
    """flat: 256 integers; st: a matchings.json entry. Identically Dita in the index structure under some valid matching."""
    blocks, groups, tr = st['blocks'], st['groups'], st['transpose']
    if not satisfies(flat, prop_eqs(blocks, groups, tr)): return False
    V = st['relaxed' if relaxed else 'strict']
    for b in range(1, len(groups)):
        if not any(satisfies(flat, lam_eqs(blocks, groups, b, tuple(sb), relaxed, tr)) for sb in V[b]): return False
    return True
