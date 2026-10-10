"""A39 Dita-locus measurement (read-only, exact): the locus in T^3 of every Dita structure of H(u1,u2,u3) = SIG o u1^A u2^B u3^C,
over every admissible shape (4x4, 8x2, 2x8), every index map and both orientations, strict and up to diagonal equivalence.

Entry (i, j) of H is the character u^{k_ij} times the constant c_ij, k_ij = (A_ij, B_ij, C_ij), c_ij = SIG's (p, q, r).
step 1  every pair-block proportionality locus (row pair, column block of size 2, 4 or 8), as an exact flat;
step 2  the closure of those loci under intersection (the stratification of T^3 by proportionality pattern);
step 3  at a generic point of each flat of the closure (and of T^3), the exhaustive structure search with monomials compared
        modulo the flat; every candidate found anywhere is then given its exact locus = the intersection of all its
        conditions (proportionality and rank-one), and its relaxed locus (rank-one up to a row factor).
A structure admitted at u is a candidate at a generic point of F_u = the intersection of the pair-block loci through u, since
the proportionality pattern at u is the generic pattern of F_u; so step 3 finds every structure admitted anywhere."""
import itertools, json, os, pickle, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from flats import Flat, Empty, TORUS, V0, vadd, vsub
S = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(S, 'probe38_landed.py'), encoding='utf-8').read()
NS = {'__name__': 'h'}; exec(compile(src[:src.index("print('== 1. realizability")], 'h', 'exec'), NS)
SIGE, EA, EB, EC, structures, SHAPES = NS['SIGE'], NS['EA'], NS['EB'], NS['EC'], NS['structures'], NS['SHAPES']
CLASSES = NS.get('CLASSES')
t0 = time.time()
K = [[(EA(i, j), EB(i, j), EC(i, j)) for j in range(16)] for i in range(16)]
CST = [[SIGE[i][j] for j in range(16)] for i in range(16)]
def ksub(a, b): return tuple(x - y for x, y in zip(a, b))
def kadd(a, b): return tuple(x + y for x, y in zip(a, b))
ORIENT = {'column': (K, CST), 'row': ([list(c) for c in zip(*K)], [list(c) for c in zip(*CST)])}

# ---- step 1: pair-block loci --------------------------------------------------------------------------------------
cache = {}
def pair_block_flat(vals):
    """vals: tuple of distinct (d, e) over the block; the locus where all u^d e are equal"""
    if vals in cache: return cache[vals]
    d0, e0 = vals[0]
    try:
        F = TORUS
        for d, e in vals[1:]:
            F = F.add(ksub(d, d0), vsub(e0, e))
        r = F
    except Empty:
        r = None
    cache[vals] = r
    return r
loci = set()
for form, (Km, Cm) in ORIENT.items():
    for i, i2 in itertools.combinations(range(16), 2):
        de = [(ksub(Km[i][j], Km[i2][j]), vsub(Cm[i][j], Cm[i2][j])) for j in range(16)]
        for n in (2, 4, 8):
            for Sb in itertools.combinations(range(16), n):
                vals = tuple(sorted(set(de[j] for j in Sb)))
                F = pair_block_flat(vals)
                if F is not None and F.rank() > 0: loci.add(F)
print('step 1: %d distinct proper pair-block loci (%d cached systems)  %.0fs' % (len(loci), len(cache), time.time() - t0), flush=True)
by_dim = {}
for F in loci: by_dim[F.dim()] = by_dim.get(F.dim(), 0) + 1
print('        by dimension:', dict(sorted(by_dim.items())), flush=True)

# ---- step 2: closure under intersection ---------------------------------------------------------------------------
closure = set(loci)
frontier = set(loci)
base = list(loci)
while frontier:
    new = set()
    for F in frontier:
        for G in base:
            try:
                M = F.meet(G)
            except Empty:
                continue
            if M not in closure: new.add(M)
    closure |= new; frontier = new
    print('        closure size %d (+%d)  %.0fs' % (len(closure), len(new), time.time() - t0), flush=True)
by_dim = {}
for F in closure: by_dim[F.dim()] = by_dim.get(F.dim(), 0) + 1
print('step 2: closure %d flats, by dimension %s  %.0fs' % (len(closure), dict(sorted(by_dim.items())), time.time() - t0), flush=True)
pickle.dump([F.B for F in closure], open(os.path.join(S, 'closure39.pkl'), 'wb'))
