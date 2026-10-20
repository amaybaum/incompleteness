"""Independent reviewer checks for mc-node5 (exact; no floats).
A. M2 countermodel at the zero-pattern level (covers every parameter value of each family), deeper words.
B. Mutation: adding one non-CM primitive (|+> attach) to the M2 alphabet must produce a non-monomial unitary word.
C. M3 can fail: a real destructive test in place of the Y test gives no unitary branch.
D. R-closure mutation: adding diag(1,i) to the real alphabet must be detected.
E. P2 value and PFR flow at level two; P5.
"""
import itertools, sympy as sp
from fractions import Fraction as Fr
I=sp.I; R2=sp.sqrt(2)
out=[]
def chk(t,c,n=""):
    out.append(bool(c)); print(("PASS " if c else "FAIL ")+t+(" : "+n if n else ""))
# ---------- A: pattern level
def pat(M):  # boolean structural pattern
    return tuple(tuple(bool(x) for x in row) for row in M)
def pmul(A,B):
    n=len(A); m=len(B[0]); k=len(B)
    return tuple(tuple(any(A[i][l] and B[l][j] for l in range(k)) for j in range(m)) for i in range(n))
def pcm(A): return all(sum(A[i][j] for i in range(len(A)))<=1 for j in range(len(A[0])))
def prm(A): return all(sum(r)<=1 for r in A)
def kronp(A,B):
    return tuple(tuple(A[i//len(B)][j//len(B[0])] and B[i%len(B)][j%len(B[0])] for j in range(len(A[0])*len(B[0]))) for i in range(len(A)*len(B)))
I2=((1,0),(0,1)); I2=tuple(tuple(bool(x) for x in r) for r in I2)
full_row=((True,True),)      # <w| with both entries generically nonzero (real or complex basis): every w(phi), <+-i|
diag=((True,False),(False,True))   # diag(1,e^{i theta}), Z
Xp=((False,True),(True,False))
ket0=((True,),(False,))
P0=((True,False),(False,False))
def perm4(p): return tuple(tuple(p[j]==i for j in range(4)) for i in range(4))
CNOT12=perm4([0,1,3,2]); SWAP=perm4([0,2,1,3]); CNOT21=perm4([0,3,2,1])
alph=[]
alph.append(kronp(full_row,I2)); alph.append(kronp(I2,full_row))   # destructive test on either token, 4->2
alph += [kronp(diag,I2),kronp(I2,diag),diag, CNOT12,CNOT21,SWAP,kronp(Xp,I2),kronp(I2,Xp),Xp, kronp(ket0,I2),kronp(I2,ket0),kronp(P0,I2),kronp(I2,P0)]
# uniform attach / discard
alph += [kronp(((True,),(True,)),I2)]  # this is NOT a Kraus op of uniform attach; uniform attach has Kraus |j>/sqrt2 each CM. Use them:
alph.pop()
alph += [kronp(((False,),(True,)),I2), kronp(((True,False),),I2), kronp(((False,True),),I2)]
def bfs(alph,depth):
    dims={}
    for K in alph: dims.setdefault(len(K[0]),[]).append(K)
    seen=set(); frontier=[tuple(tuple(i==j for j in range(d)) for i in range(d)) for d in (2,4)]
    for _ in range(depth):
        nxt=[]
        for W in frontier:
            for K in dims.get(len(W),[]):
                P=pmul(K,W)
                if P not in seen:
                    seen.add(P); nxt.append(P)
        frontier=nxt
    return seen
words=bfs(alph,8)
chk("A1 M2 alphabet (pattern level, all parameter values): every reachable word pattern to depth 8 is CM",
    all(pcm(W) for W in words), f"{len(words)} distinct patterns")
sq_nonmono=[W for W in words if len(W)==len(W[0]) and not (prm(W) and pcm(W)) and all(any(r) for r in W)]
# a square CM word with no zero row and no zero column is a permutation pattern; one with a zero column is singular
chk("A2 every square word pattern with all rows and columns nonzero is a permutation pattern (so any unitary word is monomial)",
    all(prm(W) and pcm(W) for W in words if len(W)==len(W[0]) and all(any(r) for r in W) and all(any(W[i][j] for i in range(len(W))) for j in range(len(W)))))
# ---------- B: mutation, add |+> attach (RM, not CM) -> must reach a non-CM / non-monomial square full-rank pattern
plus_att=kronp(I2,((True,),(True,)))
words2=bfs(alph+[plus_att],4)
chk("B1 mutation detected: with a |+> attach added, some word pattern is not CM", not all(pcm(W) for W in words2))
# exact: the M3 gadget then gives a non-monomial unitary
def kr(*m):
    o=m[0]
    for x in m[1:]: o=sp.kronecker_product(o,x)
    return o
Id=sp.eye(2); X=sp.Matrix([[0,1],[1,0]])
C21=sp.Matrix(4,4,lambda i,j: 1 if [0,3,2,1][j]==i else 0)
plus=sp.Matrix([1,1])/R2
def branch(bra): return sp.simplify(kr(bra,Id)*C21*kr(Id,plus))
by=sp.Matrix([[1,-I]])/R2
Kp=branch(by)
G=sp.simplify(Kp.H*Kp)
chk("B2 exact: <+i| test after |+> attach + CNOT gives a branch prop. to a non-monomial unitary", sp.simplify(G-G[0,0]*Id)==sp.zeros(2) and G[0,0]!=0 and all(x!=0 for x in Kp))
# ---------- C: M3 can fail
br=sp.Matrix([[1,1]])/R2
Kr=branch(br); Gr=sp.simplify(Kr.H*Kr)
chk("C1 M3 countercontrol can fail: with a real destructive test <+| the branch is not prop. to a unitary (rank one)",
    not (sp.simplify(Gr-Gr[0,0]*Id)==sp.zeros(2)) and Kr.rank()==1, str(Kr))
# ---------- D: R mutation
Ry=sp.Matrix([[sp.Rational(3,5),-sp.Rational(4,5)],[sp.Rational(4,5),sp.Rational(3,5)]])
S=sp.diag(1,I)
w=S*Ry*S
chk("D1 adding the quarter phase to the real alphabet yields a word not real up to scalar", any(sp.im(sp.expand(x*sp.conjugate(w[0,0])))!=0 for x in w))
# ---------- E: flow
Xab=sp.zeros(4); Xab[0,1]=Xab[1,0]=1
t=sp.symbols('t',real=True)
F=sp.exp(-I*t*Xab)
F=F.applyfunc(sp.simplify)
v=sp.simplify(F.subs(t,sp.pi/2)*sp.ones(4,1))
chk("E1 exp(-i pi/2 X_ab) 1 = (-i,-i,1,1) via sympy matrix exp", list(v)==[-I,-I,1,1], str(list(v)))
# ---------- F: G3 surrogate check: Phi_n as defined in MC1 PLAN (1-2^-n) Ad Z + 2^-n id
n=sp.symbols('n',positive=True,integer=True)
rho=sp.Matrix([[1,1],[1,1]])/2; Z=sp.diag(1,-1); E=plus*plus.H
gap=sp.simplify((E*((1-2**-n)*Z*rho*Z+2**-n*rho)).trace()-(E*Z*rho*Z).trace())
chk("F1 G3 gap is 2^-n (reproduces the formula; the X-test on |+> is the maximally discriminating test here)", sp.simplify(gap-2**-n)==0)
print("TOTAL", len(out), "PASS", sum(out))
