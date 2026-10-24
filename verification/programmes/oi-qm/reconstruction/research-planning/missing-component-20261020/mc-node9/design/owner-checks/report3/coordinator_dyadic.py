# Exact check: H+Toffoli(+CNOT,X) circuits from |0..0> give dyadic probabilities
# (amplitude = integer/sqrt(2)^h), whereas R^n gives denominator 25^n.
# Amplitudes are stored as integer numerators over a common sqrt(2)^h.
import random
from fractions import Fraction as F
random.seed(20261021)
def run(n,depth):
    v=[0]*(2**n); v[0]=1; h=0
    for _ in range(depth):
        g=random.choice(['H','TOF','CX','X'])
        q=random.sample(range(n),3)
        if g=='H':
            m=1<<q[0]; w=v[:]
            for i in range(2**n):
                w[i]=(v[i&~m]+v[i|m]) if not i&m else (v[i&~m]-v[i|m])
            v=w; h+=1
        else:
            w=v[:]
            for i in range(2**n):
                c = (g=='X') or (g=='CX' and i>>q[1]&1) or (g=='TOF' and i>>q[1]&1 and i>>q[2]&1)
                w[i]=v[i^(1<<q[0])] if c else v[i]
            v=w
    assert sum(a*a for a in v)==2**h          # normalisation, exact
    p0=F(sum(v[i]**2 for i in range(2**n) if not i&1),2**h)
    d=p0.denominator
    return d&(d-1)==0
print('H+Toffoli dyadic, 2000 random circuits n=4 depth<=30:',all(run(4,random.randint(1,30)) for _ in range(2000)))
