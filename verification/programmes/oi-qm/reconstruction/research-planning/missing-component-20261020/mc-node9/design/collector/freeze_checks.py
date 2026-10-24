"""C-SPH-1: arithmetic of the proposed first numerical target (owner proposal, REFERENCE.md), checked rigorously.

Schedule identities are exact (Fractions); transcendental quantities use mpmath interval arithmetic (60 digits), so
each inequality below is certified, not rounded.
"""
from fractions import Fraction as F
import mpmath as mp
iv=mp.iv; iv.dps=60
def lo(x): return mp.nstr(mp.mpf(x.a),12)
def hi(x): return mp.nstr(mp.mpf(x.b),12)
T=F(1); K=8; tau=F(23,200)*T; Delta=T/100
ok=K*(tau+Delta)==T
print('schedule: K (tau + Delta) = %s = T: %s'%(K*(tau+Delta),ok))
lam=iv.mpf(200)/23*iv.log(iv.mpf(20))                 # Lambda = (T/tau) ln 20
fail=iv.exp(-lam*iv.mpf(23)/200)
ok&= (fail-iv.mpf('0.05')).a<=0<=(fail-iv.mpf('0.05')).b
print('Lambda in [%s, %s]; reference failure per call = e^(-Lambda tau/T) contains 0.05: %s'%(lo(lam),hi(lam),ok))
N=1_100_000
pool=16*lam**2/N
ok&= pool.b<iv.mpf('0.01').a
print('pool term 16 Lambda^2/N at N = %d: <= %s < 0.01: %s'%(N,hi(pool),pool.b<iv.mpf('0.01').a))
nmin=16*lam**2/iv.mpf('0.01')
print('minimum N for pool term < 0.01: %s (ceil of an interval inside (%s, %s))'%(int(mp.ceil(mp.mpf(nmin.b))),lo(nmin),hi(nmin)))
ok&= int(mp.ceil(mp.mpf(nmin.a)))==int(mp.ceil(mp.mpf(nmin.b)))==1085752
eta=4*lam/N
print('aperture fraction eta = 4 Lambda/N in [%s, %s]'%(lo(eta),hi(eta)))
# aperture: per-read discrepancy <= 4 r/(1-r) with r = rho/d; pairwise contribution 2 R delta_ap with R = 8 reads
r=F(1,6401); dap=4*r/(1-r); pair=2*8*dap
ok&= pair==F(1,100)
print('aperture: rho/d = 1/6401 gives delta_ap = %s per read and 2 R delta_ap = %s for R = 8: %s'%(dap,pair,pair==F(1,100)))
# direction: the same accounting for a finite carrier set needs a per-read outcome error <= 0.01/(2R)
print('direction (finite carrier only): per-read outcome error must be <= %s'%(F(1,100)/(2*8)))
print('all checks:','green' if ok else 'RED')
