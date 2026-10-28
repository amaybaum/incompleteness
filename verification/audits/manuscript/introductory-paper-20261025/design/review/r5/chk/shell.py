from fractions import Fraction as F
import sympy as sp
p=sp.symbols('p',positive=True)
for m in (2,3,4,8):
    # Haar on C^m: |c_i|^2 ~ Dirichlet(1..1); marginal Beta(1,m-1), density (m-1)(1-p)^(m-2)
    e = m*sp.integrate(-p*sp.log(p)*(m-1)*(1-p)**(m-2),(p,0,1))
    Hm=sum(F(1,k) for k in range(1,m+1))
    page=sum(F(1,k) for k in range(m+1,m*m+1))-F(m-1,2*m)
    print(m,"diag-shell mean",sp.nsimplify(sp.simplify(e)),"= H_m-1:",sp.simplify(e-(sp.Rational(Hm.numerator,Hm.denominator)-1))==0,"Page S(m,m)=",page,float(page))
