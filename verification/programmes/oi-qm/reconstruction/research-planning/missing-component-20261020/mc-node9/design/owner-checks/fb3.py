from fractions import Fraction as F
import itertools
# (3) W for psi=(15|00>+8|11>)/17
a,b=F(15,17),F(8,17)
ZA=a*a-b*b; XX=2*a*b
print('(3) <Z_A>',ZA,'<X_A X_B>',XX,'W',ZA+XX, '>1:',ZA+XX>1)
# (4) rational rotation
print('(4) 161^2+240^2 == 289^2:',161**2+240**2==289**2,'; cos =',F(161,289),'(Niven: rational cos of rational multiple of pi only 0,+-1/2,+-1)')
# (8) D_t two-copy agree weight, exact with Gaussian rationals represented as (re,im)
def cm(x,y): return (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0])
for t in (F(0),F(1,4),F(1,2),F(1)):
    D={(0,0):(F(1,2),F(0)),(0,1):(F(0),t),(1,0):(F(0),-t),(1,1):(F(1,2),F(0))}
    # mu(E) = sum_{h,h' in E} D2[h,h'] with D2 = D (x) D; E = {(0,0),(1,1)}
    E=[(0,0),(1,1)]; s=(F(0),F(0))
    for h in E:
        for hp in E:
            v=cm(D[(h[0],hp[0])],D[(h[1],hp[1])]); s=(s[0]+v[0],s[1]+v[1])
    print('(8) t',t,'mu(agree)',s[0],'(imag',s[1],') formula 1/2-2t^2 =',F(1,2)-2*t*t)
# (10) classical: P(rA != rB) with independent signs of means 2t, 2s
for tA,sB in ((F(1,4),F(1,3)),(F(1,2),F(1,2))):
    pA=(1+2*tA)/2; pB=(1+2*sB)/2   # P(r=+1)
    p=pA*(1-pB)+(1-pA)*pB
    print('(10) P(rA!=rB)',p,'formula',F(1,2)-2*tA*sB)
