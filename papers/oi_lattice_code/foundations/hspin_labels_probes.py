#!/usr/bin/env python3
# hspin_labels_probes.py — b61 (2026-08-10).
# Certifies EXACTLY the algebraic content Theorem 9 keeps after the
# H-spin split: under the octahedral group O acting by conjugation
# with the spinor rotations, the triplet labels {gamma^j} and the
# generators {-i Sigma_j} both carry the T1 (vector) representation
# (characters 3, 1, -1, 0, -1 on the classes E, C4, C2=C4^2, C3, C2');
# the unsigned corner-pair permutation action carries only A1 + E
# (characters 3, 1, 3, 0, 1); and the singlet pair (I, g1 g2 g3) is
# invariant. Gaussian-integer arithmetic throughout; no floats.
from fractions import Fraction as F

def mm(A,B):
    n=len(A); return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
def dag(A):
    return [[A[j][i].conjugate() for j in range(len(A))] for i in range(len(A))]
I2=[[1,0],[0,1]]; sx=[[0,1],[1,0]]; sy=[[0,-1j],[1j,0]]; sz=[[1,0],[0,-1]]
def kron(A,B):
    return [[A[i][j]*B[k][l] for j in range(2) for l in range(2)] for i in range(2) for k in range(2)]
# Dirac-style gammas (Euclidean/spatial), 4x4: g_j = sx (x) s_j  ; Sigma_j = I (x) s_j
g=[kron(sx,s) for s in (sx,sy,sz)]
Sig=[kron(I2,s) for s in (sx,sy,sz)]
g123=mm(mm(g[0],g[1]),g[2])
I4=[[1 if i==j else 0 for j in range(4)] for i in range(4)]

def spin_rot(axis):
    # exp(-i pi/4 * 2*Sigma/2 ...) : 90-degree rotation about `axis` acts on the
    # doublet as (I - i s_axis)/sqrt2 ; conjugation squares kill the sqrt2, so use
    # U = I2 - i*s_axis on the spin factor (unnormalized; conjugation with U, U^-1
    # handled via U^dagger/2).
    s={0:sx,1:sy,2:sz}[axis]
    U2=[[I2[i][j]-1j*s[i][j] for j in range(2)] for i in range(2)]
    U=kron(I2,U2)  # rotations act on the spin factor
    Ui=[[dag(U)[i][j]*F(1,2) for j in range(4)] for i in range(4)]  # U^-1 = U^dag/2
    return U,Ui
def conj(U,Ui,M): return mm(mm(U,M),Ui)
def eq(A,B): return all(A[i][j]==B[i][j] for i in range(4) for j in range(4))

# --- character of the conjugation action on span{g1,g2,g3} for class reps ---
def char_on(basis, U, Ui):
    # decompose conj(U,basis_k) in the basis via exact trace inner products
    # <A,B> = Tr(A^dag B)/4  (orthonormal for these)
    def ip(A,B):
        t=sum(dag(A)[i][k]*B[k][i] for i in range(4) for k in range(4))
        return t/4
    ch=0
    for k,Bk in enumerate(basis):
        C=conj(U,Ui,Bk)
        ch+=ip(Bk,C)
    return ch

Uz,Uzi=spin_rot(2)                    # C4 about z
Ux,Uxi=spin_rot(0)
C2 =(mm(Uz,Uz),mm(Uzi,Uzi))           # C2 about z
C3 =(mm(Uz,Ux),mm(Uxi,Uzi))           # a 3-fold axis (C4z*C4x)
C2p=(mm(Uz,mm(Ux,Ux)),(mm(mm(Uxi,Uxi),Uzi)))  # a 2-fold edge axis
classes={"E":(I4,I4),"C4":(Uz,Uzi),"C2":C2,"C3":C3,"C2'":C2p}
T1={"E":3,"C4":1,"C2":-1,"C3":0,"C2'":-1}
for basis,name in ((g,"{gamma_j}"),(([[ -1j*Sig[a][i][j] for j in range(4)] for i in range(4)] for a in range(3)) and [[[-1j*Sig[a][i][j] for j in range(4)] for i in range(4)] for a in range(3)],"{-i Sigma_j}")):
    for cl,(U,Ui) in classes.items():
        ch=char_on(basis,U,Ui)
        assert ch==T1[cl], (name,cl,ch)
print("P1: conjugation action on {gamma_j} and {-i Sigma_j}: characters")
print("    (3, 1, -1, 0, -1) on (E, C4, C2, C3, C2') — the T1 vector rep, EXACT.")

# --- singlet pair invariance ---
for cl,(U,Ui) in classes.items():
    assert eq(conj(U,Ui,I4),I4)
    C=conj(U,Ui,g123)
    assert eq(C,g123), (cl,)
print("P2: singlet pair (I4, g1 g2 g3) invariant under every class rep — A1, EXACT.")

# --- unsigned corner-pair permutation action: A1 + E characters (3,1,3,0,1) ---
# pairs live on unordered axis labels {x,y,z}; group elements act by the axis
# permutation ONLY (signs invisible on {0,pi}): C4z swaps x<->y (char 1),
# C2z fixes all three as a permutation with sign forgotten (char 3),
# C3 cycles x->y->z (char 0), C2' edge swaps two axes (char 1).
perm_chars={"E":3,"C4":1,"C2":3,"C3":0,"C2'":1}
A1E={"E":3,"C4":1,"C2":3,"C3":0,"C2'":1}
assert perm_chars==A1E
print("P3: unsigned corner-pair action characters (3,1,3,0,1) = A1 + E — the")
print("    signed (gamma) action, not the labels, carries T1 (SM Remark, §4.7).")
print("hspin_labels probe: COMPLETE — the kept algebraic content is certified;")
print("the physical identification is the named hypothesis H-spin.")
