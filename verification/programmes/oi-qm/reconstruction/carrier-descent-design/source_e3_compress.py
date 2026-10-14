"""E3 probe -- K_n: does drivability descend from a large carrier to every smaller carrier inside a K3 architecture?
(exact: sympy, symbolic time parameter)

KERNEL OBJECTS AT L (quoted in NOTES-E3).
  ImplementationClass (ImplementationLocality.lean:244): S |-> (Matrix S S C -> Prop) at every finite carrier S.
  ContextStable (:359):  I S K -> I (R x S) (tensorOf (1 : Matrix R R C) K)       [tensorOf: MonoidalCompletion.lean:193]
  LabelInvariant (:364): I S K -> I S' (Matrix.reindex e e K) for every bijection e : S ~ S'
  Architecture.block (:506-517): I (S x Fin m) K -> I S (ancBlock K f e),  ancBlock K f e = of fun s t => K (s, f) (t, e)
                                                                              [AncillaClosure.lean:457]
  DrivesElementary (SubstratumSource.lean:77): at every carrier S, flow (transition a b) t, permMatrix (swap a b) and
  phaseGate a are admissible; transition a b = single a b 1 + single b a 1 (LieRankSource.lean:199);
  phaseGate a = diagonal (if a = p then I else 1) (:209); flow H t = exp((-t I) H) (ReachabilitySeam.lean:95).

THE WRITTEN CLAIM UNDER TEST (W-DESC).  For finite S nonempty, T, an injection iota : S -> T and K with I T K:
  (1) ContextStable gives I (S x T) (1_S (x) K);
  (2) a bijection e : S x T ~ S x Fin |T| with e (s0, iota s) = (s, 0) for all s (it exists: both sides have |S| |T|
      elements and the prescribed part is injective) and LabelInvariant give I (S x Fin |T|) (reindex e e (1_S (x) K));
  (3) block at (0, 0) gives I S B with B s s' = (1_S (x) K) (s0, iota s) (s0, iota s') = K (iota s) (iota s'), i.e. the
      compression of K along iota.
  For the three generator families with indices iota a, iota b, the compression is the same generator at a, b on S;
  so DrivesElementary at T gives DrivesElementary at every S with |S| <= |T|.
THE PROBE builds steps (1)-(3) literally (tensor, an explicit bijection, reindex, block) and compares with the
generators on S, for (|S|, |T|, iota) in {(3, 4, id), (3, 8, (0,3,5)), (5, 8, (7,1,4,2,6))}, every pair a != b.
CHECKS.
  F0  the closed form M(t) = (1 - P) + cos t P - i sin t H of flow(H) t for H = transition a b (P = H^2) satisfies
      M(0) = 1 and M'(t) = -i H M(t) exactly (so it is the exponential, by uniqueness of linear ODE solutions [L])
  G1  every transition-flow compression equals flow(transition a b) t on S, identically in t
  G2  every swap compression equals permMatrix (swap a b) on S
  G3  every phase-gate compression equals phaseGate a on S
  B1  the bijection used is a bijection with the prescribed values (checked as a permutation of the index set)
  K1  countercontrol: compressing flow(transition (iota a) x) t with x outside iota(S) gives a block B with
      B B^H != 1 for generic t (the invariance of the coordinate subspace is what makes the block a generator)
  K2  countercontrol (load-bearing ContextStable, instance part): with |S| = 3, |T| = 4 there is no bijection
      T ~ S x Fin m (4 is not a multiple of 3), so block + LabelInvariant cannot reach S from T without step (1); and
      the class "every matrix at carriers of size 2^k, unit-disk diagonals elsewhere" violates ContextStable at the
      explicit pair R = Fin 3, K = X on Fin 2 (1_3 (x) X is not diagonal) and violates DrivesElementary at Fin 3
      (transition flow not diagonal at t = 1) while being drivable at every size 2^k (written: its other closure
      clauses -- one, mul, smul, proj, block, LabelInvariant, DaggerStable -- hold because unit-disk diagonals are closed
      under products, scalars of modulus <= 1, reindexing, diagonal blocks and adjoints, and |S| m = 2^k forces |S| = 2^j)
DECISION RULE (fixed before the first run).  VERDICT COMPRESSION-DESCENT-EXACT iff F0, G1-G3, B1, K1, K2 all pass.  The
verdict supports W-DESC on these instances; W-DESC itself stays a written argument (CONJECTURE [W] + [X]) until a
kernel proof exists.  Nothing here says that OI supplies drivability at any carrier.
"""
import sys
import sympy as sp

RESULTS = []


def check(name, ok, detail=''):
    RESULTS.append((name, bool(ok)))
    print('%s %s%s' % ('PASS' if ok else 'FAIL', name, (' -- ' + detail) if detail else ''))


t = sp.symbols('t', real=True)
I = sp.I


def transition(n, a, b):
    M = sp.zeros(n)
    M[a, b] = 1
    M[b, a] = 1
    return M


def flow_transition(n, a, b, tt):
    H = transition(n, a, b)
    P = H * H
    return (sp.eye(n) - P) + sp.cos(tt) * P - I * sp.sin(tt) * H


def perm_swap(n, a, b):
    M = sp.eye(n)
    M[a, a] = 0
    M[b, b] = 0
    M[a, b] = 1
    M[b, a] = 1
    return M


def phase_gate(n, a):
    return sp.diag(*[I if p == a else 1 for p in range(n)])


# F0: the closed form is the exponential
okF0 = True
for n, a, b in [(3, 0, 1), (4, 1, 3), (5, 2, 4)]:
    H = transition(n, a, b)
    M = flow_transition(n, a, b, t)
    okF0 &= (M.subs(t, 0) == sp.eye(n)) and sp.simplify(M.diff(t) + I * H * M) == sp.zeros(n)
check('F0 closed form of flow(transition a b) t: M(0) = 1 and M\'(t) = -i H M(t)', okF0)


def compress_via_architecture(K, nS, nT, iota, s0=0):
    """steps (1)-(3) of W-DESC, literally: tensor 1_S (x) K on S x T, an explicit bijection e : S x T -> S x Fin nT with
    e(s0, iota s) = (s, 0), reindex, block (0, 0).  Returns the block and the bijection."""
    SxT = [(r, x) for r in range(nS) for x in range(nT)]
    SxF = [(s, f) for s in range(nS) for f in range(nT)]
    e = {}
    for s in range(nS):
        e[(s0, iota[s])] = (s, 0)
    rest_src = [p for p in SxT if p not in e]
    used = set(e.values())
    rest_dst = [q for q in SxF if q not in used]
    assert len(rest_src) == len(rest_dst)
    for p, q in zip(rest_src, rest_dst):
        e[p] = q
    einv = {q: p for p, q in e.items()}
    # 1_S (x) K as a function of index pairs (tensorOf (1 : Matrix R R C) K with R = S)
    def tens(p, q):
        return K[p[1], q[1]] if p[0] == q[0] else 0
    # reindex e e: M'(i, j) = M(e^-1 i, e^-1 j); block at (0,0): B s s' = M'((s,0),(s',0))
    B = sp.zeros(nS)
    for s in range(nS):
        for s2 in range(nS):
            B[s, s2] = tens(einv[(s, 0)], einv[(s2, 0)])
    return B, e


CASES = [(3, 4, (0, 1, 2)), (3, 8, (0, 3, 5)), (5, 8, (7, 1, 4, 2, 6))]
okG1 = okG2 = okG3 = okB1 = True
count = 0
for nS, nT, iota in CASES:
    assert len(set(iota)) == nS and all(0 <= x < nT for x in iota)
    for a in range(nS):
        for b in range(nS):
            if a == b:
                continue
            B, e = compress_via_architecture(flow_transition(nT, iota[a], iota[b], t), nS, nT, iota)
            okG1 &= sp.simplify(B - flow_transition(nS, a, b, t)) == sp.zeros(nS)
            B2, _ = compress_via_architecture(perm_swap(nT, iota[a], iota[b]), nS, nT, iota)
            okG2 &= (B2 == perm_swap(nS, a, b))
            okB1 &= (len(set(e.values())) == nS * nT and set(e.values()) == {(s, f) for s in range(nS) for f in range(nT)}
                     and all(e[(0, iota[s])] == (s, 0) for s in range(nS)))
            count += 1
        B3, _ = compress_via_architecture(phase_gate(nT, iota[a]), nS, nT, iota)
        okG3 &= (B3 == phase_gate(nS, a))
check('G1 transition-flow compressions equal flow(transition a b) t on S (%d ordered pairs, 3 carrier pairs)' % count, okG1)
check('G2 swap compressions equal permMatrix (swap a b) on S', okG2)
check('G3 phase-gate compressions equal phaseGate a on S', okG3)
check('B1 every bijection used is a bijection S x T -> S x Fin |T| with e(s0, iota s) = (s, 0)', okB1)

# K1: an index outside the image of iota
nS, nT, iota = 3, 4, (0, 1, 2)
Bk, _ = compress_via_architecture(flow_transition(nT, iota[0], 3, t), nS, nT, iota)
gram = sp.simplify(Bk * Bk.H - sp.eye(nS))
check('K1 compression of a flow leaving iota(S) is not unitary: B B^H - 1 = %s' % (list(gram),),
      gram != sp.zeros(nS) and sp.simplify(gram.subs(t, 1)) != sp.zeros(nS))

# K2: ContextStable is load-bearing (instance part)
no_bij = all(4 % (3 * m) != 0 or 3 * m != 4 for m in range(1, 5)) and 4 % 3 != 0
X = sp.Matrix([[0, 1], [1, 0]])
one3X = sp.zeros(6)
for r in range(3):
    for x in range(2):
        for x2 in range(2):
            one3X[2 * r + x, 2 * r + x2] = X[x, x2]
not_diag = any(one3X[i, j] != 0 for i in range(6) for j in range(6) if i != j)
fl3 = flow_transition(3, 0, 1, 1)
not_diag3 = any(fl3[i, j] != 0 for i in range(3) for j in range(3) if i != j)
check('K2 4 is not a multiple of 3 (no bijection Fin 4 ~ Fin 3 x Fin m); 1_3 (x) X is not diagonal; the Fin-3 '
      'transition flow at t = 1 is not diagonal', no_bij and not_diag and not_diag3)

fails = [nm for nm, ok in RESULTS if not ok]
print('checks: %d, failures: %d' % (len(RESULTS), len(fails)))
if not fails:
    print('VERDICT COMPRESSION-DESCENT-EXACT')
else:
    print('VERDICT NOT RENDERED: ' + '; '.join(fails))
sys.exit(0)
