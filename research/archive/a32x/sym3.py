import sympy as sp
exec(open('sym2.py').read().split("print('q_inj raw:'")[0])
for ri in (4,5,7,8):
    for q in IDX:
        a, b = mtr(Fr(z,zb),q), mtr(circr(ri,w,wb),q)
        if a.has(zb) or b.has(w) or b.has(wb) or b == 0: continue
        if sp.simplify(a - z*sp.Rational(1,64))==0 or sp.simplify(a + z*sp.Rational(1,64))==0:
            print('circle', ri, q, a, b); break
