"""C-SPH-1: the depletion-regime prediction corrected for first-arrival selection (owner review, 2026-10-22).

Specification (no acceptance rule is attached; one is to be preregistered separately):
- one station of N independent particles, never called before; L = v = 1; isotropic directions; depth z ~ U[0, 1);
- a particle with c = w.lambda > 0 crosses the plane at T = z/c and passes the aperture with probability eta,
  independently of (T, lambda) (uniform transverse positions);
- the station is called at t0 = (k-1)/4; the herald is the first aperture arrival in [t0, t0 + 1/4); the law is
  conditioned on that herald succeeding.
The selected arrival has density N eta f(t, lambda) S(t)^(N-1), with S(t) = 1 - eta (G(t) - G(t0)), f(t, lambda) =
c 1[t < 1/c] / (4 pi), and G the single-particle plane-crossing CDF: G(t) = t/4 for t <= 1 and 1/2 - 1/(4t) after.
Hence P(+ | w, n, k) = int S^(N-1) h_n dt / int S^(N-1) h dt over the window, with h_n(t) = int_0^min(1,1/t) c f(c) dc,
f the azimuth fraction with n.lambda > 0, and h(t) = min(1, 1/t)^2 / 2. N = 1 is the bulk-crossing average that
collector_predict.py computed. mpmath quadrature, 30 digits.
"""
import mpmath as mp, sys, os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import collector_predict as CP
mp.mp.dps=30
TAU=mp.mpf(1)/4
def G(t): return t/4 if t<=1 else mp.mpf(1)/2-1/(4*t)
def h_n(t,ca):
    kap=min(mp.mpf(1),1/t); sa=mp.sqrt(1-ca*ca)
    pts=sorted({mp.mpf(0),kap}|({sa} if 0<sa<kap else set()))
    return mp.quad(lambda c:c*CP.f_hemi(c,ca),pts)
def h(t): return min(mp.mpf(1),1/t)**2/2
def P_first(ca,k,N,eta):
    t0=(k-1)*TAU; t1=k*TAU; g0=G(t0)
    S=lambda t:(1-eta*(G(t)-g0))**(N-1)
    sa=mp.sqrt(1-ca*ca)                                  # h_n has kinks at t = 1 and t = 1/sin(alpha)
    pts=sorted({t0,t1}|{x for x in ((mp.mpf(1),1/sa) if sa>0 else (mp.mpf(1),)) if t0<x<t1})
    return mp.quad(lambda t:S(t)*h_n(t,ca),pts)/mp.quad(lambda t:S(t)*h(t),pts)
CONFIGS=[(1,mp.mpf(1)),(3,mp.mpf(1)),(3,mp.mpf(1)/4),(30,mp.mpf(1)/10),(300,mp.mpf(1)/100),(100,mp.mpf(1))]
if __name__=='__main__':
    print(__doc__.strip().splitlines()[0])
    ok=True
    for w,n,ca in CP.CASES[:2]:
        print('%s/%s (QM %s): P(+ | w, n, window k) by (N, eta)'%(w,n,mp.nstr((1+ca)/2,3)))
        for N,eta in CONFIGS:
            vals=[P_first(ca,k,N,eta) for k in range(1,9)]
            fast=max(abs(v-(1+ca)/2) for v in vals[:4])
            if N==1:
                bulk=max(abs(vals[k-1]-CP.P_window(ca,k)) for k in range(1,9)); ok&= bulk<mp.mpf(10)**-20
            ok&= fast<mp.mpf(10)**-20
            print('  N=%4d eta=%-5s N*eta=%-5s '%(N,mp.nstr(eta,3),mp.nstr(N*eta,3))+' '.join('k%d %s'%(k,mp.nstr(v,6)) for k,v in zip(range(5,9),vals[4:]))
                  +('   (fast band max deviation %s)'%mp.nstr(fast,2)))
    print('controls: windows 1-4 give (1 + cos alpha)/2 for every (N, eta); N = 1 reproduces collector_predict.py:',
          'green' if ok else 'RED')
