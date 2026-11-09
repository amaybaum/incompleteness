# Reviewer probe (exact, not evidence). A CLASSICAL two-bit register (ontic space F_2^2, point
# preparations, deterministic reads) is "contextual" for a prepare-measure LP whose operational
# equivalences are taken from the fragment's own reads when the reads are not tomographically
# complete (read bit 1, read bit 2; no joint/parity read). This is parity-oblivious multiplexing
# relative to an incomplete read set. Adding the parity read removes the equivalence.
import itertools
from fractions import Fraction as Fr
preps=[(0,0),(1,1),(0,1),(1,0)]                  # P1..P4: point laws on the register
def table(reads):
    return [[Fr(1) if r(p)==0 else Fr(0) for r in reads] for p in preps]
def linear_relations(T):
    # exact: find all c with sum_i c_i [1, T_i] = 0 (unit effect included) over small integer c
    rel=[]
    for c in itertools.product(range(-1,2),repeat=4):
        if any(c) and sum(c)==0 and all(sum(ci*T[i][e] for i,ci in enumerate(c))==0 for e in range(len(T[0]))):
            rel.append(c)
    return rel
def pnc_feasible(T, rel):
    # PNC with deterministic responses WLOG (no measurement equivalences). In any model each point
    # preparation P_i gives outcome 0 w.p. T[i][e] in {0,1}, so mu_i is supported on ontic states
    # whose response vector equals row i. A relation sum c_i mu_i = 0 is then satisfiable iff for
    # every response vector the positive and negative coefficient sums on preps with that row agree.
    for c in rel:
        rows={}
        for i,ci in enumerate(c):
            k=tuple(T[i]); rows[k]=rows.get(k,0)+ci
        if any(v!=0 for v in rows.values()): return False, c
    return True, None
r1=lambda p:p[0]; r2=lambda p:p[1]; par=lambda p:(p[0]+p[1])%2
for name,reads in (('reads {bit1, bit2} (incomplete)',[r1,r2]),('reads {bit1, bit2, parity} (spanning)',[r1,r2,par])):
    T=table(reads); rel=linear_relations(T)
    print(name,'| equivalences:',rel,'| PNC model:',pnc_feasible(T,rel))
# POM success on the incomplete fragment: decode bit b of (a0,a1) by read b
succ=Fr(sum(1 for p in preps for b in (0,1) if (r1,r2)[b](p)==p[b]),8)
print('POM success =',succ,'; preparation-noncontextual bound (Spekkens et al. 2009) = 3/4')
