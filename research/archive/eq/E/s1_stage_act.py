"""s1 -- QE1 nodes N1.2 (K-inf-Stage) and N1.3 (K-inf-Act) under the identification iota_Q.

Stage objects are built exactly as the kernel's FiniteStage (KInfFoundations:63): finite preparations, finite effects
with a unit, a table in [0,1]; DirectedStages with inclusions as forward maps (StageCompletion:63).

Decision rules (fixed before running):
  K-inf-Stage HOLDS for a QM system under iota_Q iff SCInf, BinaryVisible and FiniteRank hold exactly on its tower;
  it DELIMITS the elementary scope iff it fails for some non-elementary QM system (the qutrit control).
  K-inf-Act HOLDS under iota_Q iff unitary conjugation gives AffineRespect data with inverse data on an
  informationally complete (IC) tower; the non-IC countercontrol must FAIL StateRespect.
"""
import sys, itertools
from sympy import Matrix, Rational as R, I, eye, zeros, sqrt, simplify, symbols
from common import *

rep = Report("s1_stage_act")

# ------------------------------------------------------------- qubit tower (rational Bloch vectors)
def pyth_vectors(dmax):
    out = []
    for d in range(1, dmax + 1):
        for a in range(-d, d + 1):
            for b in range(-d, d + 1):
                c2 = d * d - a * a - b * b
                if c2 < 0:
                    continue
                c = __import__("math").isqrt(c2)
                if c * c != c2:
                    continue
                for cc in (sorted({c, -c}, reverse=True) if c else [0]):
                    v = (R(a, d), R(b, d), R(cc, d))
                    if v not in out:
                        out.append(v)
    return out

VEC = pyth_vectors(3)           # 6 axes, (+-1,+-2,+-2)/3 permutations ... : deterministic order
rep.note("qubit tower uses %d rational unit Bloch vectors (Pythagorean quadruples, d <= 3)" % len(VEC))
STAGES = [VEC[:k] for k in (6, 14, len(VEC))]   # an increasing family of finite stages


def stage_table(P):
    """effects: unit, visible pair (I +- Z)/2, and (I +- v.sigma)/2 for v in P; preparations P."""
    E = [("unit", None)] + [("vis", s) for s in (1, -1)] + [("sh", (s, v)) for v in P for s in (1, -1)]
    def p(e, x):
        kind, dat = e
        if kind == "unit":
            return R(1)
        if kind == "vis":
            return R(1, 2) + dat * x[2] / 2
        s, v = dat
        return R(1, 2) + s * sum(v[j] * x[j] for j in range(3)) / 2
    return E, p

ok_range = True
tables = []
for P in STAGES:
    E, p = stage_table(P)
    T = {(e, x): p(e, x) for e in E for x in P}
    ok_range &= all(0 <= v <= 1 for v in T.values()) and all(getattr(v, 'is_Rational', False) for v in T.values())
    tables.append((E, P, T))
rep.check("every stage table entry is an exact rational in [0,1]; unit = 1 (FiniteStage axioms)", ok_range)
# SC-inf: forward maps are inclusions; the later table restricted to earlier labels equals the earlier table
sc = all(tables[j][2][(e, x)] == tables[i][2][(e, x)]
         for i in range(len(tables)) for j in range(i, len(tables))
         for e in tables[i][0] for x in tables[i][1])
rep.check("SCInf: every forward map (inclusion) carries the probability table (StageCompletion:78)", sc)
bv = all(tables[i][2][(("vis", 1), x)] + tables[i][2][(("vis", -1), x)] == 1 for i in range(len(tables)) for x in tables[i][1])
rep.check("BinaryVisible: the pair (I+Z)/2, (I-Z)/2 is a test at every stage and is carried forward (SC:244)", bv)
# FiniteRank and injectivity of the preparation vector: prepVec is affine in x with linear part M
Etop, Ptop, Ttop = tables[-1]
M = Matrix([[0, 0, 0] if e[0] == "unit" else
             ([0, 0, e[1] / 2] if e[0] == "vis" else [e[1][0] * c / 2 for c in e[1][1]]) for e in Etop])
rep.check("prepVec = const + M x with rank M = 3: the completion chart is 3-dimensional and prepVec is injective (FiniteRank)",
          M.rank() == 3)
D = Matrix([[Ttop[(e, x)] - Ttop[(e, Ptop[0])] for e in Etop] for x in Ptop[1:]])
rep.check("affine rank of the top stage's preparation vectors = 3 (exact)", D.rank() == 3)
# K-inf-Seed source: a stage effect with values 1 and 0 at two stage preparations (sharpSeed_completion SC:224)
zp, zm = (R(0), R(0), R(1)), (R(0), R(0), R(-1))   # run 1 passed Python ints here: 1/2 became a float
rep.check("sharpSeed_completion's hypothesis: (I+Z)/2 has value 1 at z3 and 0 at -z3, both stage preparations",
          zp in [tuple(v) for v in STAGES[0]] and zm in [tuple(v) for v in STAGES[0]] and
          stage_table(STAGES[0])[1](("vis", 1), zp) == 1 and stage_table(STAGES[0])[1](("vis", 1), zm) == 0)

# ------------------------------------------------------------- K-inf-Act: unitary conjugation is AffineRespect data
Rot = ptm1(Matrix([[1, 0], [0, (3 + 4 * I) / 5]]))[1:, 1:]          # rational SO(3) element (z-rotation, cos = 3/5)
Had = ptm1(Matrix([[1, 1], [1, -1]]) / sqrt(2))[1:, 1:]             # Hadamard: (x,y,z) -> (z,-y,x)
Xs = [Matrix(v) for v in Ptop]
A1 = Matrix([[1] * len(Xs)]).col_join(Matrix.hstack(*Xs))            # 4 x K: affine relations = nullspace
rels = A1.nullspace()
rep.note("top stage: %d preparations, %d independent affine relations among their Bloch vectors" % (len(Xs), len(rels)))

def prep_vec(x):
    return Matrix([stage_table(Ptop)[1](e, x) for e in Etop])

def affine_respect(Rm):
    imgs = [prep_vec(list(Rm * x)) for x in Xs]
    return all(sum((c[k] * imgs[k] for k in range(len(Xs))), zeros(len(Etop), 1)) == zeros(len(Etop), 1)
               for c in rels)

pv = [prep_vec(list(x)) for x in Xs]
rels_ok = all(sum((c[k] * pv[k] for k in range(len(Xs))), zeros(len(Etop), 1)) == zeros(len(Etop), 1) for c in rels)
rep.check("control: the computed relations are relations among the preparation vectors themselves", rels_ok)
rep.check("AffineRespect for the rational rotation (3+4i)/5 phase gate (CompletionAction:58)", affine_respect(Rot))
rep.check("AffineRespect for the Hadamard rotation", affine_respect(Had))
rep.check("inverse datum: R^T R = I for both (Undoes), images in the Bloch ball (|Rx| = 1)",
          Rot.T * Rot == eye(3) and Had.T * Had == eye(3) and all((Rot * x).dot(Rot * x) == 1 for x in Xs))
rep.check("note: the transpose (reflY, det -1, antiunitary) is ALSO AffineRespect data on the IC tower -- "
          "K-inf-Act alone does not exclude antiunitary maps", affine_respect(REFLY))

# ------------------------------------------------------------- countercontrol: a non-IC tower
EZ = [("unit", None), ("vis", 1), ("vis", -1)]
pz = stage_table([])[1]
xa, xb = (R(1), R(0), R(0)), (R(0), R(1), R(0))
same = all(pz(e, xa) == pz(e, xb) for e in EZ)
Hx = lambda x: tuple(Had * Matrix(x))
diff = any(pz(e, Hx(xa)) != pz(e, Hx(xb)) for e in EZ)
rep.check("COUNTERCONTROL: on the Z-only (non-IC) tower |+> and |+i> have equal preparation vectors but their Hadamard "
          "images do not -- StateRespect (hence AffineRespect) FAILS for a unitary", same and diff)

# ------------------------------------------------------------- qutrit tower: the formalized K-inf-Stage predicates hold
k = [Matrix([1 if i == j else 0 for i in range(3)]) for j in range(3)]
kets = list(k)
for (a, b) in ((0, 1), (0, 2), (1, 2)):
    kets.append((k[a] + k[b]) / sqrt(2))
    kets.append((k[a] + I * k[b]) / sqrt(2))
projs = [(v * dag(v)).applyfunc(simplify) for v in kets]
P0q = projs[0]
effq = [eye(3), P0q, eye(3) - P0q] + projs
tabq = Matrix([[simplify(tr(E * rho)) for E in effq] for rho in projs])
rep.check("qutrit tower (9 rational pure states, IC projector effects): every entry in [0,1], exact",
          all(0 <= v <= 1 for v in tabq) and all(v.is_rational for v in tabq))
rep.check("qutrit: BinaryVisible with (|0><0|, I - |0><0|)", all(tabq[r, 1] + tabq[r, 2] == 1 for r in range(9)))
Dq = Matrix([[tabq[r, c] - tabq[0, c] for c in range(len(effq))] for r in range(1, 9)])
rep.check("qutrit: FiniteRank with affine rank 8 (= dim of the qutrit state space)", Dq.rank() == 8)
# capacity: qutrit 3 (orthonormal basis + its projectors), qubit <= 2 (kernel: card_le_two_of_centrallySymmetric KF:632,
# the Bloch ball being centrally symmetric about 0)
cap3 = all(simplify(tr(projs[i] * projs[j])) == (1 if i == j else 0) for i in range(3) for j in range(3)) and \
    projs[0] + projs[1] + projs[2] == eye(3)
rep.check("qutrit capacity >= 3: |0>,|1>,|2> perfectly distinguishable by projectors summing to I", cap3)
rep.check("Bloch ball centrally symmetric about 0 (x -> -x keeps |x| <= 1): Lemma D gives qubit capacity <= 2",
          all((-Matrix(v)).dot(-Matrix(v)) == 1 for v in VEC))
rep.note("so SCInf, BinaryVisible and FiniteRank hold for the qubit AND the qutrit: the formalized part of K-inf-Stage does "
         "not delimit the elementary scope; capacity two does (qubit 2, qutrit 3)")

# ------------------------------------------------------------- horizons: the stage tower of a fixed-basis observer
# Stage T: outcome strings of a Z readout (Lueders) after each step of a fixed rational unitary Ustep, T steps.
# Effects E_s = K_s1^dag ... K_sT^dag K_sT ... K_s1, K_b = P_b Ustep; preparations: the 30 rational Bloch states.
Ustep = Matrix([[R(3, 5), R(-4, 5)], [R(4, 5), R(3, 5)]])
Pb = [Matrix([[1, 0], [0, 0]]), Matrix([[0, 0], [0, 1]])]
def horizon_effects(T, menu):
    out = []
    for ctx in menu:                                  # a context = a unitary applied before the first step
        for sstr in __import__("itertools").product((0, 1), repeat=T):
            Kp = eye(2)
            for b in sstr:
                Kp = Pb[b] * Ustep * Kp
            out.append(dag(ctx * eye(2)) * dag(Kp) * Kp * ctx)
    return out
rhos = [rho1([R(v[0]), R(v[1]), R(v[2])]) for v in VEC]
def tab(effs):
    return Matrix([[simplify(tr(Ee * r)) for Ee in effs] for r in rhos])
cons = True
for T in (1, 2):
    e_T, e_T1 = horizon_effects(T, [eye(2)]), horizon_effects(T + 1, [eye(2)])
    # forward map: string s of length T  ->  marginal over the last outcome at horizon T+1
    for i in range(len(e_T)):
        cons &= (e_T1[2 * i] + e_T1[2 * i + 1]).applyfunc(simplify) == e_T[i].applyfunc(simplify)
rep.check("horizon tower of a fixed-basis observer: SCInf holds as marginal consistency (horizons 1 -> 2 -> 3, exact)", cons)
t3 = tab(horizon_effects(3, [eye(2)]))
D3 = Matrix([[t3[r, c] - t3[0, c] for c in range(t3.cols)] for r in range(1, t3.rows)])
rep.check("FIXED-BASIS HORIZON TOWER COMPLETES TO A SEGMENT: affine rank of the qubit's preparation vectors = 1 "
          "(every horizon-3 effect is c_s . Ustep^dag P_b Ustep), so the elementary body read this way is d = 1",
          D3.rank() == 1 and all(v.is_Rational for v in t3))
Hd2 = Matrix([[1, 1], [1, -1]]) / sqrt(2)
menu = [eye(2), Hd2, Hd2 * Matrix([[1, 0], [0, -I]])]
tm = tab(horizon_effects(1, menu))
Dm = Matrix([[simplify(tm[r, c] - tm[0, c]) for c in range(tm.cols)] for r in range(1, tm.rows)])
rep.check("with a three-context instrument menu {I, H, H S^dag} before the readout the affine rank is 3 (the Bloch ball)",
          Dm.rank() == 3)
rep.note("so the identification of OI's horizons with stages yields the quantum elementary body only when the stage "
         "effects include context choices (rotated readouts); a fixed-basis horizon tower yields the classical bit. "
         "K-inf-V4 with K-inf-Trans is the premise that forces the rotated readouts into the available family.")

ok = rep.out()
sys.exit(0 if ok else 1)
