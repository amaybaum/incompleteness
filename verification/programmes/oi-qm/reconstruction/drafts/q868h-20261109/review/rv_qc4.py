"""Reviewer check for QC-4 (Q-868-H unit 1). Generic Pauli matrices, plus a formal F2 identity over six
free symbols (no OI rule, encoding, coupling or preparation; the symplectic data of U' is used by hand
in the review). Self-contained; imports no earlier probe. sympy, exact."""
import sys, itertools
import sympy as sp
I2=sp.eye(2); X=sp.Matrix([[0,1],[1,0]]); Y=sp.Matrix([[0,-sp.I],[sp.I,0]]); Z=sp.Matrix([[1,0],[0,-1]])
K=lambda a,b: sp.kronecker_product(a,b)
res=[]
def chk(n,ok,d=""):
    res.append(bool(ok)); print(("PASS " if ok else "FAIL ")+n+(" :: "+d if d else ""))
row=[K(X,Z),K(Z,X),K(Y,Y)]; col=[K(X,X),K(Z,Z),K(Y,Y)]
chk("M4a row product (XZ)(ZX)(YY) = +I", row[0]*row[1]*row[2]==sp.eye(4))
chk("M4b column product (XX)(ZZ)(YY) = -I", col[0]*col[1]*col[2]==-sp.eye(4))
chk("M4c each line pairwise commutes", all(a*b==b*a for L in (row,col) for a,b in itertools.combinations(L,2)))
chk("M4d control: the non-line pair X(x)Z, Z(x)Z anticommutes", K(X,Z)*K(Z,Z)==-K(Z,Z)*K(X,Z))
# QM: joint eigenbasis outcome bits of a line have sum = 0 (row) or 1 (column) mod 2 on every eigenvector
def line_bits_ok(L,parity):
    # simultaneous eigenvectors: eigenvectors of a generic combination
    G=L[0]+2*L[1]+5*L[2]
    for val,mult,vecs in G.eigenvects():
        for v in vecs:
            bits=[]
            for O in L:
                w=O*v; lam=sp.simplify((v.H*w)[0]/(v.H*v)[0])
                if sp.simplify(w-lam*v)!=sp.zeros(4,1): return False
                bits.append(0 if lam==1 else 1)
            if sum(bits)%2!=parity: return False
    return True
chk("M4e QM: on every joint eigenvector the row's outcome bits sum to 0 mod 2", line_bits_ok(row,0))
chk("M4f QM: on every joint eigenvector the column's outcome bits sum to 1 mod 2", line_bits_ok(col,1))
# formal F2 identity: with p_W := f_x^W + f_y^W + f_z^W (free symbols), both line sums equal p_A + p_B
fxA,fyA,fzA,fxB,fyB,fzB=sp.symbols("fxA fyA fzA fxB fyB fzB")
pA=fxA+fyA+fzA; pB=fxB+fyB+fzB
red=lambda e: sp.Poly(sp.expand(e),fxA,fyA,fzA,fxB,fyB,fzB).trunc(2).as_expr()
chk("M4g formal: (fxA+fzB)+(fzA+fxB)+(fyA+fyB) = pA+pB over F2", red((fxA+fzB)+(fzA+fxB)+(fyA+fyB)-(pA+pB))==0)
chk("M4h formal: (fxA+fxB)+(fzA+fzB)+(fyA+fyB) = pA+pB over F2", red((fxA+fxB)+(fzA+fzB)+(fyA+fyB)-(pA+pB))==0)
chk("M4i control: a non-line triple (fxA+fxB)+(fzA+fzB)+(fxA+fzB) != pA+pB", red((fxA+fxB)+(fzA+fzB)+(fxA+fzB)-(pA+pB))!=0)
nf=res.count(False); print(f"\n{len(res)} checks, {nf} failures"); sys.exit(1 if nf else 0)
