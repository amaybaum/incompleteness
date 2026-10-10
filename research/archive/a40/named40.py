import pickle, os, sys, itertools
from flats import Flat, TORUS, V0, vadd, vsub, Empty
src = open('probe38_landed.py', encoding='utf-8').read()
import contextlib, io
NS = {'__name__': 'h'}
with contextlib.redirect_stdout(io.StringIO()): exec(compile(src[:src.index("print('== 1. realizability")], 'h', 'exec'), NS)
SIGE, EA, EB, EC = NS['SIGE'], NS['EA'], NS['EB'], NS['EC']
i0 = src.index('\nCLASSES = ') + 1; exec(src[i0:src.index('\n', i0)], NS); CLASSES = NS['CLASSES']
M_COL = (((0, 2, 4, 6, 8, 10, 12, 14), (1, 3, 5, 7, 9, 11, 13, 15)), ((0, 2), (1, 3), (4, 6), (5, 15), (7, 13), (8, 10), (9, 11), (12, 14)))
M_ROW = (((0, 1, 2, 3, 8, 9, 10, 11), (4, 5, 6, 7, 12, 13, 14, 15)), ((0, 2), (1, 9), (3, 11), (4, 12), (5, 13), (6, 14), (7, 15), (8, 10)))
K = [[(EA(i, j), EB(i, j), EC(i, j)) for j in range(16)] for i in range(16)]
CST = [[SIGE[i][j] for j in range(16)] for i in range(16)]
ORIENT = {'column': (K, CST), 'row': ([list(c) for c in zip(*K)], [list(c) for c in zip(*CST)])}
def ksub(a, b): return tuple(x - y for x, y in zip(a, b))
def ent(form, i, j): Km, Cm = ORIENT[form]; return (Km[i][j], Cm[i][j])
def div(x, y): return (ksub(x[0], y[0]), vsub(x[1], y[1]))
def witnesses(form, cp, rows):
    """all 4-position proportionality identities H[i,j]H[i2,j0] = H[i,j0]H[i2,j] for i,i2 in one class, j,j0 in one block;
    each as (character k, constant c, positions): u^k * c = 1"""
    out = []
    for cl in rows:
        for i, i2 in itertools.combinations(cl, 2):
            for bl in cp:
                for j0, j in itertools.combinations(bl, 2):
                    k, c = div(div(ent(form, i, j), ent(form, i2, j)), div(ent(form, i, j0), ent(form, i2, j0)))
                    out.append((k, c, (i, j, i2, j0)))
    return out
def locus(ws):
    F = TORUS
    try:
        for k, c, _ in ws:
            if not any(k):
                if c != V0: return None
                continue
            F = F.add(k, vsub(V0, c))
    except Empty: return None
    return F
NAMED = [(nm, form, (m, n), tuple(map(tuple, cp)), tuple(map(tuple, rows))) for nm, m, n, cp, rows in CLASSES for form in ('column', 'row')]
NAMED += [('M_COL', 'column', (2, 8)) + M_COL, ('M_ROW', 'row', (2, 8)) + M_ROW]
if __name__ == '__main__':
    res = pickle.load(open('../a39/locus39.pkl', 'rb'))['res']
    rl = {(c[0], c[1], frozenset(map(frozenset, c[2])), frozenset(map(frozenset, c[3]))): Bs for c, Bs, Br in res}
    for nm, form, mn, cp, rows in NAMED:
        key = (form, mn, frozenset(map(frozenset, cp)), frozenset(map(frozenset, rows)))
        Bs = rl.get(key, 'NOT-A-CANDIDATE')
        ws = witnesses(form, cp, rows)
        P = locus(ws)
        # single witnesses whose character is a coordinate vector (the locus generators)
        coord = {}
        for k, c, pos in ws:
            if sorted(map(abs, k)) == [0, 0, 1]:
                kk = tuple(abs(x) for x in k); cc = c if sum(k) > 0 else vsub(V0, c)
                coord.setdefault((kk, cc), pos)
        bad_const = [(k, c) for k, c, _ in ws if not any(k) and c != V0]
        print('%-5s %-6s %s locus %s | prop-only locus %s | coordinate witnesses %s' % (nm, form, mn,
              'EMPTY' if Bs is None else (Bs if isinstance(Bs, str) else Flat.of(Bs).describe()),
              'EMPTY' if P is None else P.describe(), sorted(coord)))
