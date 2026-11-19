"""Reviewer check for QC-2 and the CNOT-matching finding (Q-868-H unit 1). Comparator (quantum) side
only: generic 2x2/4x4 matrices. Encodes no OI rule, encoding, coupling or preparation; the native
pullbacks are derived by hand in the review. Self-contained; imports no earlier probe. sympy, exact."""
import sys, itertools
import sympy as sp
I2=sp.eye(2); X=sp.Matrix([[0,1],[1,0]]); Y=sp.Matrix([[0,-sp.I],[sp.I,0]]); Z=sp.Matrix([[1,0],[0,-1]])
P={"0":I2,"x":X,"y":Y,"z":Z}; K=lambda a,b: sp.kronecker_product(a,b)
res=[]
def chk(n,ok,d=""):
    res.append(bool(ok)); print(("PASS " if ok else "FAIL ")+n+(" :: "+d if d else ""))
Hd=sp.Matrix([[1,1],[1,-1]])/sp.sqrt(2); S=sp.diag(1,sp.I)
CN=sp.zeros(4,4)
for c,t in itertools.product(range(2),repeat=2): CN[2*c+((t+c)%2),2*c+t]=1   # control = first factor
# single-qubit table actions <s>_out = <U^dag s U>_in, compared with QP's stated pullbacks
def heis(U,s): return sp.simplify(U.H*P[s]*U)
chk("C2a H: <Z>out=<X>in, <X>out=<Z>in, <Y>out=-<Y>in (QP: f_z.H=f_x, f_x.H=f_z, f_y.H=f_y+1)",
    heis(Hd,"z")==X and heis(Hd,"x")==Z and heis(Hd,"y")==-Y)
chk("C2b S: <X>out=-<Y>in, <Y>out=<X>in, <Z>out=<Z>in (QP: f_x.S=f_y+1, f_y.S=f_x, f_z.S=f_z)",
    heis(S,"x")==-Y and heis(S,"y")==X and heis(S,"z")==Z)
k00=sp.Matrix([1,0,0,0]); phi=sp.Matrix([1,0,0,1])/sp.sqrt(2)
o1=CN*K(Hd,I2)*k00; o2=CN*K(Hd*S,I2)*k00
chk("C2c path 1 comparator: CNOT (H x I)|00> = Phi+", sp.simplify(o1-phi)==sp.zeros(4,1))
chk("C2d path 2 comparator: CNOT (HS x I)|00> = Phi+", sp.simplify(o2-phi)==sp.zeros(4,1))
yy=lambda v: sp.simplify((v.H*K(Y,Y)*v)[0])
chk("C2e both comparator outputs have <YY> = -1, <XX> = <ZZ> = +1",
    yy(o1)==-1 and yy(o2)==-1 and sp.simplify((o1.H*K(X,X)*o1)[0])==1 and sp.simplify((o1.H*K(Z,Z)*o1)[0])==1)
chk("C2f control: path-2 operator differs from path-1 operator (HS != H up to phase on the |1> input)",
    sp.simplify(K(Hd*S,I2)*sp.Matrix([0,0,1,0])-K(Hd,I2)*sp.Matrix([0,0,1,0]))!=sp.zeros(4,1))
# full CNOT conjugation sign table on the 15 non-identity Pauli products
img={}
for a,b in itertools.product("0xyz",repeat=2):
    if a=="0" and b=="0": continue
    Q=sp.simplify(CN*K(P[a],P[b])*CN)
    hit=[(s,c,d) for c,d in itertools.product("0xyz",repeat=2) for s in (1,-1) if Q==s*K(P[c],P[d])]
    img[(a,b)]=hit[0]
chk("C2g CNOT: YY -> -XZ, XY -> +YZ, YZ -> +XY",
    img[("y","y")]==(-1,"x","z") and img[("x","y")]==(1,"y","z") and img[("y","z")]==(1,"x","y"), str({k:img[k] for k in [("y","y"),("x","y"),("y","z")]}))
neg=sorted(k for k,v in img.items() if v[0]==-1)
chk("C2h the only CNOT image with a minus sign among the 15 is YY (and its partner XZ -> -YY)",
    set(neg)=={("y","y"),("x","z")}, str(neg))
# table (I+XX+ZZ+tYY)/4 is PSD only at t=-1: the two paths' YY values u and -u cannot both be -1
t=sp.Symbol("t",real=True)
ev=((sp.eye(4)+K(X,X)+K(Z,Z)+t*K(Y,Y))/4).eigenvals()
chk("C2i with XX=ZZ=1 the singlet-direction eigenvalue is (-1-t)/4, so <YY>=u and <YY>=-u are both quantum only if u=-u=-1 (impossible)",
    any(sp.simplify(e-(-1-t)/4)==0 for e in ev))
chk("C2j at <YY>=+1 min eigenvalue -1/2; at <YY>=0 min eigenvalue -1/4",
    min(sp.simplify(e.subs(t,1)) for e in ev)==sp.Rational(-1,2) and min(sp.simplify(e.subs(t,0)) for e in ev)==sp.Rational(-1,4))
nf=res.count(False); print(f"\n{len(res)} checks, {nf} failures"); sys.exit(1 if nf else 0)
