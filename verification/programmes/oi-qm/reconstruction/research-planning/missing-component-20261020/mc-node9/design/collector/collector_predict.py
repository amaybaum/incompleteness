"""Preregistered apparatus prediction for candidate C-SPH-1 (continuum, before the finite test is run).

The mechanism is fixed: a station with normal w heralds the first reservoir particle crossing its shutter plane;
positions uniform in a slab of depth L behind the plane, directions isotropic, speed v (here L = v = 1), windows of
length tau = 1/4. A particle with c = w.lambda > 0 crosses at T = z/(v c), z ~ U[0, L). The herald law of window k is
proportional to the depth band it uses, w_k(c) = min(k c tau, 1) - min((k-1) c tau, 1), times the isotropic measure;
for windows ending by L/v (k <= 4) this is proportional to c, the projected-area law. Readout along n reports the
hemisphere of lambda. The prediction is the first-read probability P(+ | w, n, window k) for windows past L/v,
computed here from that law alone (mpmath quadrature, 30 digits), and the preparation-equivalence residual it implies.
Nothing in this file reads a finite direction set.
"""
import mpmath as mp
mp.mp.dps=30
TAU=mp.mpf(1)/4

def f_hemi(c,ca):
    """Fraction of azimuth with n.lambda > 0, lambda at polar cosine c from w, n at angle alpha (cos alpha = ca)."""
    sa=mp.sqrt(1-ca*ca); A=c*ca; B=mp.sqrt(1-c*c)*sa
    if B==0: return mp.mpf(1) if A>0 else (mp.mpf(0) if A<0 else mp.mpf(1)/2)
    x=-A/B
    if x<=-1: return mp.mpf(1)
    if x>=1: return mp.mpf(0)
    return mp.acos(x)/mp.pi
def wk(c,k): return min(k*c*TAU,mp.mpf(1))-min((k-1)*c*TAU,mp.mpf(1))
def P_window(ca,k):
    pts=sorted({mp.mpf(0),mp.mpf(1)}|{p for p in (1/(k*TAU),1/((k-1)*TAU) if k>1 else 2,mp.sqrt(1-ca*ca)) if 0<p<1})
    num=mp.quad(lambda c:f_hemi(c,ca)*wk(c,k),pts); den=mp.quad(lambda c:wk(c,k),pts)
    return num/den
def P_kappa(ca,kap):
    """Time-resolved law at crossing time t: proportional to c on 0 < c < kappa = min(1, L/(v t))."""
    pts=sorted({mp.mpf(0),kap}|({mp.sqrt(1-ca*ca)} if 0<mp.sqrt(1-ca*ca)<kap else set()))
    return mp.quad(lambda c:f_hemi(c,ca)*c,pts)/(kap*kap/2)

CASES=[('X+','R',mp.mpf(4)/5),('Y+','R',mp.mpf(3)/5),('Z+','R',mp.mpf(0)),('R+','X',mp.mpf(4)/5)]
if __name__=='__main__':
    print(__doc__.strip().splitlines()[0])
    print('control: fast band reproduces (1 + cos alpha)/2 exactly in the continuum (quadrature residual shown)')
    for w,n,ca in CASES:
        print('  %s/%s  P_window(k=1) - (1+ca)/2 = %s   P_kappa(1) - (1+ca)/2 = %s'%(w,n,mp.nstr(P_window(ca,1)-(1+ca)/2,3),mp.nstr(P_kappa(ca,mp.mpf(1))-(1+ca)/2,3)))
    print('prediction: window-averaged first read past L/v (k = 5..8), and time-resolved at kappa = 1/2, 1/4')
    for w,n,ca in CASES:
        row=['k=%d %s'%(k,mp.nstr(P_window(ca,k),8)) for k in (4,5,6,7,8)]
        print('  %s/%s QM %s | '%(w,n,mp.nstr((1+ca)/2,4))+'  '.join(row)+' | kappa=1/2 %s kappa=1/4 %s'%(mp.nstr(P_kappa(ca,mp.mpf(1)/2),8),mp.nstr(P_kappa(ca,mp.mpf(1)/4),8)))
    # equivalence residual for relation 6 of D6, r_plus = 5/6 R+ + 1/6 X-, with r_plus prepared as 1/2 X+ + 1/2 Y+
    AX={'X':(1,0,0),'Y':(0,1,0),'Z':(0,0,1),'R':(mp.mpf(4)/5,mp.mpf(3)/5,0)}
    def P(wv,n,k):
        ca=sum(a*b for a,b in zip(wv,AX[n])); return P_window(mp.mpf(ca),k)
    print('prediction: relation-6 residual 1/2 P(X+) + 1/2 P(Y+) - 5/6 P(R+) - 1/6 P(X-), per menu axis')
    for k in (4,5,6,7,8):
        res={n:(P(AX['X'],n,k)+P(AX['Y'],n,k))/2-mp.mpf(5)/6*P(AX['R'],n,k)-P((-1,0,0),n,k)/6 for n in AX}
        print('  window %d: '%k+'  '.join('%s %s'%(n,mp.nstr(v,6)) for n,v in res.items()))
