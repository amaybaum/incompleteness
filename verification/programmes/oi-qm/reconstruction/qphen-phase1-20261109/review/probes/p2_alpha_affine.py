"""Reviewer probe P2 (QPHEN Phase 1 review). Exact; F_2 arithmetic and Fractions.

Checks QX3 A3.1 on generic objects only (no OI construction is built):
 (a) two affine functionals f_A, f_B on a uniform coset of F_2^n give
     alpha = P_AB/(P_A P_B) in {0, 1, 2} (or undefined), and alpha = 0 iff
     f_B = f_A + 1 on the coset with f_A non-constant;
 (b) whether 'number-conserving routing' needs a non-affine bijection depends on
     where number conservation is required: on the single-excitation ready
     support versus on the whole configuration space;
 (c) the controlled swap (Fredkin) is not affine over F_2.
"""
import itertools
from fractions import Fraction

def vecs(n):
    return list(itertools.product((0, 1), repeat=n))

def dot(a, s):
    return sum(x*y for x, y in zip(a, s)) % 2

def span(gens, n):
    S = {tuple([0]*n)}
    for g in gens:
        S |= {tuple((x+y) % 2 for x, y in zip(s, g)) for s in S}
    return S

def cosets(n):
    out = set()
    for k in range(n+1):
        for gens in itertools.combinations(vecs(n), k):
            L = frozenset(span(gens, n))
            for t in vecs(n):
                out.add(frozenset(tuple((x+y) % 2 for x, y in zip(l, t)) for l in L))
    return out

def part_a(n=4):
    vals = set()
    zero_cases_ok = True
    count = 0
    for C in cosets(n):
        C = list(C)
        N = len(C)
        for a, b in itertools.product(vecs(n), repeat=2):
            for cA, cB in itertools.product((0, 1), repeat=2):
                fA = [(dot(a, s) + cA) % 2 for s in C]
                fB = [(dot(b, s) + cB) % 2 for s in C]
                PA = Fraction(sum(fA), N); PB = Fraction(sum(fB), N)
                PAB = Fraction(sum(x*y for x, y in zip(fA, fB)), N)
                count += 1
                if PA == 0 or PB == 0:
                    vals.add('undef'); continue
                al = PAB / (PA*PB)
                vals.add(al)
                comp = all(y == 1-x for x, y in zip(fA, fB)) and len(set(fA)) == 2
                if (al == 0) != comp:
                    zero_cases_ok = False
    return sorted(vals, key=str), zero_cases_ok, count

def is_affine(F, n):
    # F affine over F_2 iff F(x)+F(y)+F(z)+F(x+y+z) == 0 for all x,y,z
    for x, y, z in itertools.product(vecs(n), repeat=3):
        w = tuple((p+q+r) % 2 for p, q, r in zip(x, y, z))
        s = tuple((F[x][i] + F[y][i] + F[z][i] + F[w][i]) % 2 for i in range(n))
        if any(s):
            return False
    return True

def weight(v):
    return sum(v)

def part_b():
    n = 3  # cells (s, c1, c2): supply bit s (uniform), two field cells c1, c2
    V = vecs(n)
    # linear map L(s, c1, c2) = (s, s+c1, s+c2)
    L = {v: (v[0], (v[0]+v[1]) % 2, (v[0]+v[2]) % 2) for v in V}
    assert len(set(L.values())) == 8, 'not a bijection'
    ready = [(s, 1, 0) for s in (0, 1)]  # one excitation in c1; s uniform (N2)
    outs = [L[v] for v in ready]
    PA = Fraction(sum(o[1] for o in outs), 2); PB = Fraction(sum(o[2] for o in outs), 2)
    PAB = Fraction(sum(o[1]*o[2] for o in outs), 2)
    res = {
        'L_is_affine': is_affine(L, n),
        'ready_support_outputs': outs,
        'alpha_own_cell_reads': str(PAB/(PA*PB)),
        'one_excitation_in_field_cells_on_ready_support': all(o[1]+o[2] == 1 for o in outs),
        'total_weight_conserved_on_ready_support': all(weight(L[v]) == weight(v) for v in ready),
        'total_weight_conserved_globally': all(weight(L[v]) == weight(v) for v in V),
    }
    # Fredkin: swap c1,c2 iff s
    Fr = {v: (v[0], v[2], v[1]) if v[0] else v for v in V}
    res['fredkin_is_affine'] = is_affine(Fr, n)
    res['fredkin_equals_L_on_single_excitation_sector'] = all(
        Fr[v] == L[v] for v in V if v[1] + v[2] == 1)
    # Exhaustive: all affine bijections of F_2^3 that conserve total weight
    # everywhere are coordinate permutations (so they cannot route by s).
    import itertools as it
    perms_ok = True
    n_wp = 0
    for cols in it.product(V, repeat=3):
        for c in V:
            F = {v: tuple((sum(cols[j][i]*v[j] for j in range(3)) + c[i]) % 2
                          for i in range(3)) for v in V}
            if len(set(F.values())) != 8:
                continue
            if all(weight(F[v]) == weight(v) for v in V):
                n_wp += 1
                is_perm = c == (0, 0, 0) and sorted(cols) == sorted(
                    [(1,0,0), (0,1,0), (0,0,1)])
                perms_ok &= is_perm
    res['globally_weight_preserving_affine_bijections_F2^3'] = n_wp
    res['all_are_coordinate_permutations'] = perms_ok
    # Count affine bijections with alpha = 0 on own-cell reads and weight
    # conserved on the ready support (s uniform, c1 = 1, c2 = 0)
    n_route = 0
    for cols in it.product(V, repeat=3):
        for c in V:
            F = {v: tuple((sum(cols[j][i]*v[j] for j in range(3)) + c[i]) % 2
                          for i in range(3)) for v in V}
            if len(set(F.values())) != 8:
                continue
            o = [F[v] for v in ready]
            if all(weight(F[v]) == weight(v) for v in ready) and \
               all(x[1] + x[2] == 1 for x in o) and o[0][1] != o[1][1]:
                n_route += 1
    res['affine_bijections_routing_on_ready_support'] = n_route
    return res

if __name__ == '__main__':
    vals, ok, cnt = part_a(4)
    print('A3.1(a) alpha values over all cosets of F_2^4 and functional pairs:', vals,
          '| cases:', cnt, '| alpha=0 iff complement:', ok)
    for k, v in part_b().items():
        print(f'{k}: {v}')
