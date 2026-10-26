from fractions import Fraction as Fr
import math
try:
    import numpy as np
except ImportError:
    np=None
def S(m,n):
    assert m<=n
    return sum(Fr(1,k) for k in range(n+1,m*n+1)) - Fr(m-1,2*n)
print("m=n=2 exact mean:", S(2,2), "(known 1/3)")
for m in [2,3,4,8,16,32,64]:
    print("m=n=%d  ln m - S = %.8f"%(m, math.log(m)-float(S(m,m))))
for (m,n) in [(2,4),(2,16),(2,256),(4,64),(4,1024),(8,8*64)]:
    d=math.log(m)-float(S(m,n)); print("m=%d n=%d deficit=%.6g m/2n=%.6g ratio=%.4f"%(m,n,d,m/(2*n),d/(m/(2*n))))
# in mode language d_R=q^{nR}, d_B=q^{nB}: deficit ~ q^{-(nB-nR)}/2 : exponential in mode difference, independent of total size
if np is not None:
    rng=np.random.default_rng(1)
    for (m,n) in [(2,2),(3,5),(4,4)]:
        vals=[]
        for _ in range(40000):
            z=rng.normal(size=(m,n))+1j*rng.normal(size=(m,n)); z/=np.linalg.norm(z)
            p=np.linalg.svd(z,compute_uv=False)**2; p=p[p>1e-15]; vals.append(-(p*np.log(p)).sum())
        print("MC m=%d n=%d mean=%.4f +- %.4f exact=%.4f"%(m,n,np.mean(vals),np.std(vals)/200,float(S(m,n))))
    # concentration: std shrinks fast with total dim
    for (m,n) in [(2,2),(4,4),(8,8),(16,16),(32,32)]:
        vals=[]
        for _ in range(2000):
            z=rng.normal(size=(m,n))+1j*rng.normal(size=(m,n)); z/=np.linalg.norm(z)
            p=np.linalg.svd(z,compute_uv=False)**2; p=p[p>1e-15]; vals.append(-(p*np.log(p)).sum())
        print("m=n=%d std=%.5f mean-ln m=%.4f"%(m,np.std(vals),np.mean(vals)-math.log(m)))
