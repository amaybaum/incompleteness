import itertools, sympy as sp
exec(open('k20_classify.py').read().split('# 1. the relations')[0])
kr = sp.kronecker_product
I2=sp.eye(2); PX=sp.Matrix([[0,1],[1,0]]); PY=sp.Matrix([[0,-sp.I],[sp.I,0]]); PZ=sp.Matrix([[1,0],[0,-1]]); P=[I2,PX,PY,PZ]
def bloch(Um):
    B=[kr(P[i],P[j]) for i in range(4) for j in range(4)]
    return sp.Matrix(16,16,lambda i,j: sp.nsimplify(sp.simplify((Um*B[j]*Um.H*B[i]).trace()/4)))
CN=sp.Matrix([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
Gq=bloch(CN)
J=sp.Matrix([[0,-1],[1,0]])
print('(0) builder reproduces the complex CNOT with M0 = I, A = I, K = [[0,-1],[1,0]]:', build((1,1), sp.eye(2), J) == Gq)
# 2. the value formula on product states and effects, symbolic
s1,s2,sz,t1,t2,tz,a1_,a2_,az,b1,b2,bz=sp.symbols('s1 s2 sz t1 t2 tz f1 f2 fz g1 g2 gz')
a1,a2,k1,k2,e1,e2=sp.symbols('a1 a2 k1 k2 e1 e2')
A=sp.diag(a1,a2); K=sp.Matrix([[0,k1],[k2,0]])
def value(M0d,A,K):
    G=build(M0d,A,K)
    s=sp.Matrix([1,s1,s2,sz]); t=sp.Matrix([1,t1,t2,tz]); f=sp.Matrix([1,a1_,a2_,az]); g=sp.Matrix([1,b1,b2,bz])
    return sp.expand((kr(f,g).T*G*kr(s,t))[0])
for M0d in itertools.product((1,-1),repeat=2):
    v=value(M0d,A,K)
    tp=[1,M0d[0]*t1,M0d[1]*t2,tz]
    alpha=a1_*a1*s1+a2_*a2*s2; beta=a1_*k1*s2+a2_*k2*s1
    formula=(1+sz*az)*(1+b1*tp[1])+(sz+az)*(b2*tp[2]+bz*tp[3])+alpha*(b1+tp[1])+beta*(bz*tp[2]-b2*tp[3])
    print('(1) M0 =',M0d,': value = (1+s_z f_z)(1+g_x t\'_x) + (s_z+f_z)(g-.t\'-) + (f.As)(g_x+t\'_x) + (f.Ks)(g- x t\'-):', sp.expand(v-formula)==0)
# 3. positivity: necessity at exact points, and the resulting sign solutions
#    at s_z = f_z = 0, t'_x = g_x = 0, t'- and g- unit and aligned to make the last term -|beta| ... the value is
#    1 - |(alpha, beta)| at the worst direction, so P needs |(f.As, f.Ks)| <= 1 for unit f, s in T.
sols=[]
for a1v,a2v,k1v,k2v in itertools.product((1,-1),repeat=4):
    if a1v*k1v+a2v*k2v==0: sols.append((a1v,a2v,k1v,k2v))
print('(2) sign solutions of |a_i| = |k_i| = 1 with a1 k1 + a2 k2 = 0:',len(sols))
# the orthogonality of W(s) = [As, Ks] for all s is exactly a1 k1 + a2 k2 = 0 (column inner product s1 s2 (a1 k1 + a2 k2))
cands=[(m,w) for m in itertools.product((1,-1),repeat=2) for w in sols]
print('    candidate gates:',len(cands))
Gs={c: build(c[0],sp.diag(c[1][0],c[1][1]),sp.Matrix([[0,c[1][2]],[c[1][3],0]])) for c in cands}
k0,k1v_=E(U)+E(Z),E(U)-E(Z); kk=[k0,k1v_]
ok=all(all(G*kr(kk[p_],kk[q_])==kr(kk[p_],kk[p_^q_]) for p_ in (0,1) for q_ in (0,1)) and IN*G*IN==G and NI*G*NI==IN*G and G.det()!=0 for G in Gs.values())
inv_in=all(any(G.inv()==H for H in Gs.values()) for G in Gs.values())
print('    the inverse of each candidate is a candidate:',inv_in)
print('    all satisfy F, Rt, Rc and are invertible:',ok, '; G^2 = I for',sum(1 for G in Gs.values() if G*G==sp.eye(16)),'of',len(Gs))
# 4. orbits under local relabellings L = diag(1, sx, sy, 1) on each factor (fixing the corners, commuting with N)
Ls=[sp.diag(1,x,y,1) for x in (1,-1) for y in (1,-1)]
def orbits(group):
    seen={}; classes=[]
    keys=list(Gs)
    for c in keys:
        if c in seen: continue
        cls=[]
        for LA,LB in group:
            L=kr(LA,LB); H=L*Gs[c]*L.inv()
            for c2 in keys:
                if c2 not in seen and Gs[c2]==H: seen[c2]=len(classes); cls.append(c2)
        classes.append(sorted(set(cls)))
    return classes
O=[(LA,LB) for LA in Ls for LB in Ls]
SO=[(LA,LB) for LA in Ls for LB in Ls if LA.det()==1 and LB.det()==1]
co=orbits(O); cs=orbits(SO)
print('(3) classes under the 16 local O-type relabellings:',len(co),' sizes',[len(c) for c in co])
print('    classes under the 4 local SO-type relabellings:',len(cs),' sizes',[len(c) for c in cs])
# 5. which gates are quantum (unitary conjugations in the standard embedding)? Choi rank-1 PSD test
def superop(G):
    B=[kr(P[i],P[j]) for i in range(4) for j in range(4)]
    # S(B_j) = sum_i G[i,j] B_i ; Choi = sum_{kl} |k><l| (x) S(|k><l|)
    S=lambda Mx: sum((G[i,j]*B[i]*((B[j].H*Mx).trace()/4) for i in range(16) for j in range(16) if G[i,j]!=0), sp.zeros(4))
    C=sp.zeros(16)
    for kk_ in range(4):
        for ll in range(4):
            Ekl=sp.zeros(4); Ekl[kk_,ll]=1
            C+=kr(Ekl,S(Ekl))
    return C.applyfunc(sp.simplify)
def is_unitary_channel(G):
    C=superop(G); return C.rank()==1 and all(sp.re(C[i,i])>=0 for i in range(16)) and C==C.H
R=sp.diag(1,1,-1,1)
report=[]
for i,cl in enumerate(co):
    c=cl[0]; G=Gs[c]
    q=is_unitary_channel(G); qB=is_unitary_channel(kr(I4,R)*G*kr(I4,R)); qA=is_unitary_channel(kr(R,I4)*G*kr(R,I4)); qAB=is_unitary_channel(kr(R,R)*G*kr(R,R))
    m,w=c; detM0=m[0]*m[1]; detW=-w[2]*w[1]
    report.append((i,len(cl),c,detM0,detW,q,qA,qB,qAB))
    print('    O-class',i,'size',len(cl),'rep',c,'det M0',detM0,'det W',detW,'| unitary:',q,' after reflecting A:',qA,' B:',qB,' both:',qAB)
