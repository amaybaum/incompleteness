"""P4: classical observers in OI's own architecture (finite prefix-closed protocol towers, PT of the
oistage/SA notes), exact, finite horizon.

Claim tested (written proof in the ledger, "NG1-S"): for a finite carrier with full-support mu, a
reversible step phi and a menu of permutations, every protocol stage body is a SIMPLEX, whose vertices
are the images of the classes of the finest record partition.  Hence the classical observers of the
landed classical architecture fail PI / NRR (their bodies are simplices) -- the exact classical-failure
side (a) of the candidates.

  T0  'OI-incomplete but record-complete': a visible bit and two hidden bits that the step cycles; the
      hidden sector is never readable (every effect is constant on hidden fibres), yet the body is a
      segment and the visible readout with re-preparation reconstructs every stage preparation.
  R*  random toys (seeded): body affine rank, finest partition, brute-force simplex test (independent
      of the partition argument), and the partition prediction (#classes - 1 = affine dim, class
      images are the simplex vertices and are realised by preparations).
  C1  countercontrol, restricted readouts (NOT prefix closed: single-bit reads, no joint read) over two
      classical bits: the body is a square (not a simplex) -- so the simplex test discriminates, and
      prefix closure / joint readability is load-bearing.  C1b: adding the joint read gives a simplex.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import random
from fractions import Fraction as F
from itertools import product
from plib import affine_dim, is_simplex_hull, barycentric

checks = []


def chk(name, cond):
    checks.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)


class Tower:
    def __init__(self, N, phi, vis, acts):
        self.N, self.phi, self.vis, self.acts = N, phi, vis, acts
        self.mu = [F(1, N)] * N
        self.alpha = ['o', 'i'] + list(range(len(acts)))

    def run(self, sigma, w):
        rec = []
        for s in sigma:
            if s == 'o':
                rec.append(self.vis[w])
                w = self.phi[w]
            elif s == 'i':
                w = self.phi[w]
            else:
                w = self.acts[s][w]
        return tuple(rec), w

    def words(self, L):
        out = [()]
        for n in range(1, L + 1):
            out += list(product(self.alpha, repeat=n))
        return out

    def preparations(self, L):
        preps = []
        for sigma in self.words(L):
            groups = {}
            for w in range(self.N):
                r, w2 = self.run(sigma, w)
                groups.setdefault(r, []).append(w2)
            for r, finals in groups.items():
                nu = [F(0)] * self.N
                for w2 in finals:
                    nu[w2] += F(1, len(finals))
                preps.append(((sigma, r), tuple(nu)))
        return preps

    def effect_atoms(self, L):
        atoms = []
        for sigma in self.words(L):
            recs = sorted({self.run(sigma, w)[0] for w in range(self.N)})
            for r in recs:
                atoms.append((sigma, r))
        return atoms

    def vec(self, nu, atoms):
        return tuple(sum((nu[w] for w in range(self.N) if self.run(s, w)[0] == r), F(0)) for s, r in atoms)

    def finest_partition(self, L):
        key = {w: tuple(self.run(s, w)[0] for s in self.words(L)) for w in range(self.N)}
        classes = {}
        for w, k in key.items():
            classes.setdefault(k, []).append(w)
        return list(classes.values())


def analyse(name, T, Lp, Le):
    atoms = T.effect_atoms(Le)
    preps = T.preparations(Lp)
    vecs = []
    for _, nu in preps:
        v = T.vec(nu, atoms)
        if v not in vecs:
            vecs.append(v)
    k = affine_dim(vecs)
    simp, verts = is_simplex_hull(vecs)
    classes = T.finest_partition(Le)
    cls_imgs = []
    for c in classes:
        nu = [F(0)] * T.N
        nu[c[0]] = F(1)
        cls_imgs.append(T.vec(nu, atoms))
    realised = all(v in vecs for v in cls_imgs)
    indep = affine_dim(cls_imgs) == len(cls_imgs) - 1
    print(f"   {name}: N={T.N} |atoms|={len(atoms)} |distinct prep vecs|={len(vecs)} affine dim {k} "
          f"classes {classes} simplex {simp}")
    return dict(k=k, simp=simp, classes=classes, realised=realised, indep=indep, vecs=vecs, atoms=atoms,
                cls_imgs=cls_imgs, preps=preps)


# T0: visible bit (index 0) x hidden Z4 (index 1); state id = v*4 + h; step cycles h, keeps v
N0 = 8
phi0 = [(w // 4) * 4 + ((w % 4) + 1) % 4 for w in range(N0)]
vis0 = [w // 4 for w in range(N0)]
T0 = Tower(N0, phi0, vis0, [])
print("== T0 (hidden sector permanently hidden)")
A0 = analyse("T0", T0, 3, 3)
hidden_invisible = all(T0.vec(tuple(F(int(u == w)) for u in range(N0)), A0["atoms"]) ==
                       T0.vec(tuple(F(int(u == (w // 4) * 4)) for u in range(N0)), A0["atoms"]) for w in range(N0))
chk("T0: every effect is constant on hidden fibres (OI incompleteness: hidden never read)", hidden_invisible)
chk("T0: body is a segment (affine dim 1, simplex)", A0["k"] == 1 and A0["simp"])
# reconstructing record at the body level: readout 'o' (one observation), re-preparation y_v = posterior vec after reading v
yv = {}
for (sigma, r), nu in A0["preps"]:
    if sigma == ('o',):
        yv[r[0]] = T0.vec(nu, A0["atoms"])
idx = A0["atoms"].index((('o',), (0,)))
ok = True
for x in A0["vecs"]:
    p0 = x[idx]
    rec = tuple(p0 * a + (1 - p0) * b for a, b in zip(yv[0], yv[1]))
    ok &= (rec == x)
chk("T0: the visible readout + re-preparation reconstructs every stage preparation (record-complete)", ok)

print("== random passive towers (finite carrier, reversible step, permutation menu)")
rng = random.Random(20261006)
for t in range(8):
    N = rng.choice([3, 4, 5])
    phi = list(range(N)); rng.shuffle(phi)
    vis = [rng.choice([0, 1]) for _ in range(N)]
    if len(set(vis)) == 1:
        vis[0] = 1 - vis[0]
    acts = []
    for _ in range(rng.choice([0, 1])):
        a = list(range(N)); rng.shuffle(a); acts.append(a)
    T = Tower(N, phi, vis, acts)
    Le = 3 if acts else 4
    allsimp = True
    for Lp in (3, 4, 5):
        A = analyse(f"R{t} phi={phi} vis={vis} acts={acts} Lp={Lp}", T, Lp, Le)
        allsimp &= A["simp"]
        if A["realised"]:
            break
    chk(f"R{t}: stage body is a simplex at every preparation horizon tried (brute force)", allsimp)
    chk(f"R{t}: at horizon Lp={Lp}: affine dim = #finest classes - 1, class images independent and realised",
        A["k"] == len(A["classes"]) - 1 and A["indep"] and A["realised"])

print("== C1 countercontrol: restricted (non-prefix-closed) readouts on two classical bits")
pts = [(a, b) for a in (0, 1) for b in (0, 1)]
# effects: P(a=1), P(b=1) only (no joint read); preparations: the four point masses and mixtures
sq = [(F(a), F(b)) for a, b in pts]
s1, _ = is_simplex_hull(sq)
chk("C1: body with single-bit reads only is a square (NOT a simplex)", not s1)
joint = [(F(a), F(b), F(a * b)) for a, b in pts]  # adding the joint read P(a=1, b=1)
s2, _ = is_simplex_hull(joint)
chk("C1b: adding the joint read (prefix-closed: read a, swap, read) gives a simplex", s2)

npass = sum(1 for _, c in checks if c)
print(f"{'ALL-PASS' if npass == len(checks) else 'SOME-FAIL'} {npass}/{len(checks)}")
