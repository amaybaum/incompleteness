# Independent ODE check: dM/dt = -a * M^-(2+p); Page time at M = M0/sqrt2 (beta=1, S_BH ~ M^2)
# time to go from M0 to m: integral M^(2+p) dM / a
from fractions import Fraction as Fr
import math
def frac_numeric(p, N=200000):
    # Simpson integration of dt = M^(2+p)/a dM, a=1, M0=1
    def integ(lo,hi):
        h=(hi-lo)/N; s=0.0
        for i in range(N+1):
            x=lo+i*h; w=1 if i in (0,N) else (4 if i%2 else 2)
            s+=w*x**(2+p)
        return s*h/3
    tP=integ(1/math.sqrt(2),1.0); te=integ(0.0,1.0)
    return tP/te
for p in [0,0.5,1,2]:
    print("p=%g ODE=%.8f formula=%.8f"%(p,frac_numeric(p),1-2**(-(3+p)/2)))
# beta general with p: turnover S_BH/S0 = beta/(1+beta) -> M/M0 = sqrt(beta/(1+beta)); fraction = 1-(beta/(1+beta))^((3+p)/2)
