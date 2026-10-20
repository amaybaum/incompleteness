import sympy as sp, itertools, random
I4=sp.eye(4); pi=sp.pi
def pm(p):
    M=sp.zeros(4); 
    for col,row in enumerate(p): M[row,col]=1
    return M
def logm(P, choose=None):
    # independent path: sympy diagonalization; eigenvalue angles in (-pi,pi], with optional flip of arg(-1)
    Pm,D=P.diagonalize()
    Ld=sp.zeros(4)
    for k in range(4):
        lam=sp.nsimplify(sp.simplify(D[k,k]))
        a=sp.arg(lam)
        if choose is not None and sp.simplify(lam+1)==0: a=choose
        Ld[k,k]=sp.I*a
    L=sp.simplify(Pm*Ld*Pm.inv())
    return L
def realvec(A):
    v=[]
    for x in A:
        x=sp.expand(x); v+= [sp.re(x), sp.im(x)]
    return v
def lie(gens):
    mats=[]; rows=[]
    def ins(A):
        A=sp.simplify(A/pi)
        cand=rows+[realvec(A)]
        if sp.Matrix(cand).rank(simplify=True)>len(rows):
            rows.append(realvec(A)); mats.append(A); return True
        return False
    for g in gens: ins(g)
    ch=True
    while ch:
        ch=False; cur=list(mats)
        for a in range(len(cur)):
            for b in range(a+1,len(cur)):
                if ins((cur[a]*cur[b]-cur[b]*cur[a])*pi): ch=True
    return mats
one=sp.Matrix([1,1,1,1])
import mpmath as mp
mp.mp.dps=60
def tomp(A): return mp.matrix([[mp.mpc(str(sp.re(sp.N(x,70))),str(sp.im(sp.N(x,70)))) for x in A.row(i)] for i in range(A.rows)])
def expclose(L,T):
    E=mp.expm(tomp(L))-tomp(T); return max(abs(E[i,j]) for i in range(4) for j in range(4))<mp.mpf('1e-45')
def onesfix(A):
    w=A*one; return all(sp.simplify(w[i]-w[0])==0 for i in range(4))
perms=list(itertools.permutations(range(4)))
PL=[logm(pm(p)) for p in perms]
for p,L in zip(perms,PL):
    assert expclose(L,pm(p)), p
    assert sp.simplify(L*pm(p)-pm(p)*L)==sp.zeros(4) and sp.simplify(L+L.H)==sp.zeros(4)
print("principal logs exact: ok")
A0=lie(PL); print("dim principal", len(A0), "onesfix", all(onesfix(A) for A in A0))
# mixed branch choices: arg(-1) = -pi for random subsets
random.seed(1)
for trial in range(3):
    gens=[logm(pm(p), choose=(-pi if random.random()<0.5 else None)) for p in perms]
    A=lie(gens); print("mixed branch trial",trial,"dim",len(A),"onesfix",all(onesfix(x) for x in A))
gens=[logm(pm(p), choose=-pi) for p in perms]
A=lie(gens); print("all -pi dim",len(A),all(onesfix(x) for x in A))
CN=pm((0,1,3,2)); Lp=logm(CN); E00=sp.zeros(4); E00[0,0]=1
print("Lp =",Lp)
print("[Lp,E00]=0:", sp.simplify(Lp*E00-E00*Lp)==sp.zeros(4))
L=Lp+2*pi*sp.I*E00
print("exp(L)==CNOT (60-digit):", expclose(L,CN), " exp(Lp)==CNOT:", expclose(Lp,CN))
t=sp.Rational(1,2); Uh=sp.simplify((t*L).exp()); Uph=sp.simplify((t*Lp).exp()); print('Uh exact check', expclose(t*L,Uh))
print("Unp(1/2)=",Uh, " sq==CN", sp.simplify(Uh*Uh-CN)==sp.zeros(4), "onesfix", onesfix(Uh), "Up onesfix", onesfix(Uph))
A1=lie(PL+[L]); print("dim with L", len(A1), all(onesfix(x) for x in A1))
A1b=lie(PL+[sp.I*pi*E00]); print("dim with phase gen i*E00 (equivalence check)", len(A1b))
J=sp.ones(4)/4
print("[J,CN]=0",sp.simplify(J*CN-CN*J)==sp.zeros(4), "[J,Lp]=0", sp.simplify(J*Lp-Lp*J)==sp.zeros(4))
A2=lie(PL+[Lp+2*pi*sp.I*J]); print("dim with J/4", len(A2), all(onesfix(x) for x in A2))
# is J/4 a function of CNOT? span{I,CN}
a,b=sp.symbols('a b'); print("J/4 in span{I,CN}:", sp.solve(list(a*I4+b*CN-J),[a,b]))
# is i*J in the principal algebra already? (then adding it is no change but the dimension goes 9->10?)
