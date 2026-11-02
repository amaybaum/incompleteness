"""Exact-arithmetic review probe for Main.md Theorem (history readback + finite recurrence
implies indivisibility) and its Lemma (stochastic inverse).

Objects (all exact, fractions.Fraction):
  phi      : bijection of V x H, V = range(nV), H = range(nH)
  mu       : hidden prior on H (shared by every root; may contain zeros)
  pV       : visible prior on V (may contain zeros)
  Gamma_t  : rooted map, Gamma_t[a][j] = mu{h : pi_V phi^t(a,h) = j}, defined for EVERY root a
  C4 at k  : two distinct positive-probability histories (x_0..x_{k-1}) with common x_k = c whose
             next-step laws P(x_{k+1} | x_<k, x_k) differ.
Checks (decision rules fixed before running):
  A  C4 at order k  =>  some Gamma_s, 1 <= s <= k, is not a permutation matrix.
  A' C4 at order k  =>  some s <= k has two distinct rows of Gamma_s overlapping in a column
     (the Lean hypothesis shape); record whether both rows can be taken from supported roots.
  B  Gamma_s non-permutation and Gamma_L = I  =>  no stochastic Lambda with Gamma_s Lambda = I.
     Tested independently of the Lemma: Lambda must equal Gamma_s^{-1} (exact Gauss-Jordan);
     verdict = singular or some negative entry.  Countercontrol: permutation Gamma_s gives a
     stochastic inverse.
  R  Restricted reading: rows only for supported roots.  With a single supported root the
     restricted family is always P-divisible (Lambda = 1 * row_t); count C4 cases there.
  N  'Readback not needed': cases with full-support visible prior, some non-permutation Gamma_s,
     and NO C4 gap at any order <= L (still P-indivisible by B).
"""
import itertools
import sys
from fractions import Fraction as F

def compose_power(phi, t, s):
    for _ in range(t):
        s = phi[s]
    return s

def order(phi):
    n = len(phi)
    L = 1
    cur = list(phi)
    ident = list(range(n))
    while cur != ident:
        cur = [phi[c] for c in cur]
        L += 1
    return L

def rooted(phi, nV, nH, mu, t):
    G = [[F(0)] * nV for _ in range(nV)]
    for a in range(nV):
        for h in range(nH):
            if mu[h] == 0:
                continue
            s = a * nH + h
            s = compose_power(phi, t, s)
            G[a][s // nH] += mu[h]
    return G

def is_perm(G):
    n = len(G)
    cols = set()
    for row in G:
        nz = [j for j, v in enumerate(row) if v != 0]
        if len(nz) != 1 or row[nz[0]] != 1:
            return False
        cols.add(nz[0])
    return len(cols) == n

def overlap_pairs(G, rows=None):
    n = len(G)
    rows = range(n) if rows is None else rows
    out = []
    for a, b in itertools.combinations(rows, 2):
        for j in range(n):
            if G[a][j] > 0 and G[b][j] > 0:
                out.append((a, b, j))
                break
    return out

def inverse(G):
    n = len(G)
    M = [list(G[i]) + [F(int(i == j)) for j in range(n)] for i in range(n)]
    for c in range(n):
        p = next((r for r in range(c, n) if M[r][c] != 0), None)
        if p is None:
            return None
        M[c], M[p] = M[p], M[c]
        pv = M[c][c]
        M[c] = [v / pv for v in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]
                M[r] = [x - f * y for x, y in zip(M[r], M[c])]
    return [row[n:] for row in M]

def has_stochastic_right_inverse(G):
    inv = inverse(G)
    if inv is None:
        return False
    return all(v >= 0 for row in inv for v in row)  # rows of inverse sum to 1 automatically

def path_law(phi, nV, nH, mu, pV, T):
    """Joint law of (x_0..x_T) as dict tuple -> prob."""
    law = {}
    for a in range(nV):
        if pV[a] == 0:
            continue
        for h in range(nH):
            if mu[h] == 0:
                continue
            s = a * nH + h
            xs = [a]
            for _ in range(T):
                s = phi[s]
                xs.append(s // nH)
            key = tuple(xs)
            law[key] = law.get(key, F(0)) + pV[a] * mu[h]
    return law

def c4_gap(phi, nV, nH, mu, pV, k):
    """Return a witness (p, p', c) of a C4 gap at order k, or None."""
    law = path_law(phi, nV, nH, mu, pV, k + 1)
    # group by (x_<k, x_k): next-step law
    cond = {}
    for path, pr in law.items():
        hist, now, nxt = path[:k], path[k], path[k + 1]
        d = cond.setdefault((hist, now), {})
        d[nxt] = d.get(nxt, F(0)) + pr
    laws = {}
    for (hist, now), d in cond.items():
        tot = sum(d.values())
        laws[(hist, now)] = tuple(d.get(j, F(0)) / tot for j in range(nV))
    bynow = {}
    for (hist, now), lw in laws.items():
        bynow.setdefault(now, []).append((hist, lw))
    for now, lst in bynow.items():
        for (h1, l1), (h2, l2) in itertools.combinations(lst, 2):
            if l1 != l2:
                return (h1, h2, now)
    return None

def distinct_hist_same_present(phi, nV, nH, mu, pV, k):
    law = path_law(phi, nV, nH, mu, pV, k)
    seen = {}
    for path in law:
        seen.setdefault(path[k], set()).add(path[:k])
    return any(len(v) > 1 for v in seen.values())

def analyse(phi, nV, nH, mu, pV, stats, examples):
    L = order(phi)
    G = [rooted(phi, nV, nH, mu, t) for t in range(L + 1)]
    assert G[L] == [[F(int(i == j)) for j in range(nV)] for i in range(nV)], "identity return"
    assert G[0] == G[L]
    supp = [a for a in range(nV) if pV[a] > 0]
    nonperm = [s for s in range(1, L) if not is_perm(G[s])]
    # B and its countercontrol, on every s < L
    for s in range(1, L):
        sri = has_stochastic_right_inverse(G[s])
        if is_perm(G[s]):
            stats['B_ctrl_perm'] += 1
            if not sri:
                stats['B_ctrl_FAIL'] += 1
        else:
            stats['B_nonperm'] += 1
            if sri:
                stats['B_FAIL'] += 1
                examples.setdefault('B_FAIL', (phi, mu, pV, s))
        # pigeonhole: non-perm stochastic square <=> some two distinct rows overlap
        if (not is_perm(G[s])) != bool(overlap_pairs(G[s])):
            stats['pigeonhole_FAIL'] += 1
    c4_orders = [k for k in range(1, L + 1) if c4_gap(phi, nV, nH, mu, pV, k)]
    if c4_orders:
        stats['C4'] += 1
        k = c4_orders[0]
        s_ok = [s for s in range(1, k + 1) if not is_perm(G[s])]
        if not s_ok:
            stats['A_FAIL'] += 1
            examples.setdefault('A_FAIL', (phi, mu, pV, k))
        if not [s for s in range(1, k + 1) if overlap_pairs(G[s])]:
            stats['Aprime_FAIL'] += 1
        if not [s for s in range(1, k + 1) if overlap_pairs(G[s], supp)]:
            stats['C4_overlap_needs_unsupported_row'] += 1
            examples.setdefault('needs_unsupported', (phi, mu, pV, k))
        if min(s_ok) == k:
            stats['first_nonperm_equals_k'] += 1
        else:
            stats['first_nonperm_below_k'] += 1
        # indivisibility witnessed on pair (s, L) for s = first non-perm
        if has_stochastic_right_inverse(G[min(s_ok)]):
            stats['THEOREM_FAIL'] += 1
        if len(supp) == 1:
            stats['R_single_root_C4'] += 1
            examples.setdefault('R_single_root', (phi, mu, pV, k))
    else:
        if len(supp) == nV and nonperm:
            stats['N_nonperm_without_C4'] += 1
            examples.setdefault('N', (phi, mu, pV))
    if len(supp) == nV and not nonperm and c4_orders:
        stats['A_FAIL2'] += 1

def run(nV, nH, priors, vpriors, limit=None, stride=1):
    from collections import Counter
    stats = Counter()
    examples = {}
    n = nV * nH
    for idx, perm in enumerate(itertools.permutations(range(n))):
        if idx % stride:
            continue
        if limit and idx >= limit:
            break
        phi = list(perm)
        for mu in priors:
            for pV in vpriors:
                stats['cases'] += 1
                analyse(phi, nV, nH, mu, pV, stats, examples)
    return stats, examples

def fr(*xs):
    return [F(x) for x in xs]

if __name__ == '__main__':
    configs = {
        (2, 2): [[F(1, 2), F(1, 2)], [F(1), F(0)], [F(2, 3), F(1, 3)]],
        (2, 3): [[F(1, 3)] * 3, [F(1, 2), F(1, 2), F(0)], [F(1, 2), F(1, 3), F(1, 6)]],
        (3, 2): [[F(1, 2)] * 2, [F(1), F(0)], [F(3, 4), F(1, 4)]],
        (2, 4): [[F(1, 4)] * 4, [F(1, 2), F(1, 4), F(1, 4), F(0)]],
    }
    for (nV, nH), priors in configs.items():
        vpriors = [[F(1, nV)] * nV] + [[F(int(i == a)) for i in range(nV)] for a in range(nV)]
        if nV == 3:
            vpriors.append([F(1, 2), F(1, 2), F(0)])
        stats, ex = run(nV, nH, priors, vpriors)
        print(f"(nV,nH)=({nV},{nH})", dict(sorted(stats.items())))
        for key in ('R_single_root', 'needs_unsupported', 'N'):
            if key in ex:
                print('   example', key, ex[key])
    sys.stdout.flush()
