"""Test of K2 (control), K8, K9 and the earlier K1/K3-K7 against the alignment-free loci of s5 (reads loci_af.pkl)."""
import pickle, sys, itertools
from align import *
from splitters import cells_to_mat
S0 = [[SIGE[i][j] for j in range(16)] for i in range(16)]
OR0 = orientations_d([], S0)
C0, _ = enumerate_candidates_d(OR0, 0)
SIG_STRUCTS = [k for k in C0 if locus_alignfree(OR0, k[0], k[1], k[2], k[3], False, 0)]
assert len(SIG_STRUCTS) == 20
def identically_Dita(pieces, relaxed=False):
    """the (d-1)-family lies identically in some alignment-free structure of SIG (necessarily one of SIG's 20)"""
    d = len(pieces); OR = orientations_d(pieces)
    for f, mn, cp, rows in SIG_STRUCTS:
        U = locus_alignfree(OR, f, mn, cp, rows, relaxed, d)
        if any(F.rank() == 0 for F in U): return (f, mn, cp, rows)
    return None
def flip_perm(P):
    """if SIG o (-1)^P is SIG with rows permuted (or columns permuted), return ('row', pi) / ('col', pi), pi[i] = source index"""
    _, base = rebase([P], [-1])
    rows = {tuple(S0[i]): i for i in range(16)}
    pi = [rows.get(tuple(base[i])) for i in range(16)]
    if None not in pi and sorted(pi) == list(range(16)): return ('row', pi)
    cols = {tuple(S0[i][j] for i in range(16)): j for j in range(16)}
    pj = [cols.get(tuple(base[i][j] for i in range(16))) for j in range(16)]
    if None not in pj and sorted(pj) == list(range(16)): return ('col', pj)
    return None
def transport(P, fp):
    kind, pi = fp
    # base'[i][j] = SIG[pi[i]][j]  => F(-1,u')[i][j] = SIG[pi i][j] u'^{P[i][j]} = (Pi . SIG o u'^{P o pi^-1})[i][j]
    # i.e. the family through SIG with atoms Q[pi[i]][j] = P[i][j]
    Q = [[0] * 16 for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if kind == 'row': Q[pi[i]][j] = P[i][j]
            else: Q[i][pi[j]] = P[i][j]
    return Q
def faces_of(Bs, d):
    """codim-1 coordinate faces in a union (as {(k, s)}), and the rest"""
    faces = set(); rest = []
    for B in Bs:
        F = FlatD.of(d, B)
        if F.rank() == 1 and F.is_coordinate():
            (k, s), = F.coord_dict().items(); faces.add((k, s))
        else: rest.append(F.show())
    return faces, rest
if __name__ == '__main__':
    L = pickle.load(open(os.path.join(HERE, sys.argv[1] if len(sys.argv) > 1 else 'loci_af.pkl'), 'rb'))
    tot = {'K1': [0, 0], 'K2': [0, 0], 'K3': [0, 0], 'K4': [0, 0], 'K5': [0, 0], 'K7': [0, 0], 'K8': [0, 0], 'K9': [0, 0], 'SR': [0, 0], 'SORT': [0, 0]}
    def tally(k, ok): tot[k][0] += bool(ok); tot[k][1] += 1
    for t in sorted(L):
        r = L[t]; Ms = [cells_to_mat(a) for a in r['atoms']]; d = len(Ms)
        faces, rest = faces_of(r['U_strict'], d); facesR, restR = faces_of(r['U_relaxed'], d)
        fS, _ = faces_of(r['U_sorted'], d)
        pred = set(); detail = []
        for k in range(d):
            others = [M for j, M in enumerate(Ms) if j != k]
            plus = identically_Dita(others) is not None
            if plus: pred.add((k, 1))
            fp = flip_perm(Ms[k])
            minus = False
            if fp is not None:
                minus = identically_Dita([transport(M, fp) for M in others]) is not None
            if minus: pred.add((k, -1))
            detail.append('%s%s%s%s' % ('%dx%d' % r['shapes'][k], '+' if (k, 1) in faces else '.', '-' if (k, -1) in faces else '.', ('P' + fp[0][0]) if fp else ''))
        tally('K2', set(x for x in pred if x[1] == 1) == set(x for x in faces if x[1] == 1))
        tally('K8', set(x for x in pred if x[1] == -1) == set(x for x in faces if x[1] == -1))
        tally('K9', all(FlatD.of(d, B).is_coordinate() for B in r['U_strict'] + r['U_relaxed']))
        tally('K1', not rest and r['U_strict'] == r['U_relaxed'] and all(all(FlatD.of(d, B).is_coordinate() for B in v[0]) for v in r['loci'].values()))
        tally('K3', all((k, 1) in faces for k in range(d)))
        tally('K4', all(((k, -1) in faces) == ((k, 1) in faces and sorted(r['shapes'][k]) == [2, 8]) for k in range(d)))
        tally('K5', all((k, 1) in faces for (k, s) in faces if s == -1))
        tally('K7', (set(r['line']['show_strict']) == ({'u1 = 1', 'u1 = -1'} if any(s == -1 for k, s in faces) else {'u1 = 1'})))
        tally('SR', r['U_strict'] == r['U_relaxed'])
        tally('SORT', r['U_sorted'] == r['U_strict'])
        print('orbit %2d d=%d atoms %s | faces %s | other comps %s | pred(+/-) %s | K8 %s | strict=relaxed %s | sorted=af %s | line %s' % (
            t, d, ' '.join(detail), sorted(faces), rest, sorted(pred), set(x for x in pred if x[1] == -1) == set(x for x in faces if x[1] == -1),
            r['U_strict'] == r['U_relaxed'], r['U_sorted'] == r['U_strict'], r['line']['show_strict']), flush=True)
    print()
    for k, (a, n) in tot.items(): print('%-5s holds on %d of %d orbits' % (k, a, n))
