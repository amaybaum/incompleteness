from fractions import Fraction as F
# amplitudes over |q1 q2 q3>, exact: H on q1,q2 from |000> gives amplitude 1/2 on |x y 0>; Toffoli swaps |110>,|111>
amp={}
for x in (0,1):
    for y in (0,1):
        amp[(x,y,0)]=F(1,2)
amp[(1,1,1)]=amp.pop((1,1,0))
norm=sum(a*a for a in amp.values())
# reduced state of q3: rho_{ab} = sum_{x,y} amp(x,y,a) amp(x,y,b)
rho={(a,b):sum(amp.get((x,y,a),0)*amp.get((x,y,b),0) for x in (0,1) for y in (0,1)) for a in (0,1) for b in (0,1)}
print('norm',norm,'reduced q3:',rho)
# is Toffoli affine over F2? check f(u)+f(v)+f(0) == f(u+v)
def tof(s): x,y,z=s; return (x,y,z^(x&y))
import itertools
pts=list(itertools.product((0,1),repeat=3)); add=lambda a,b: tuple((i+j)%2 for i,j in zip(a,b))
aff=all(add(add(tof(u),tof(v)),tof((0,0,0)))==tof(add(u,v)) for u in pts for v in pts)
print('Toffoli affine over F2:',aff)
