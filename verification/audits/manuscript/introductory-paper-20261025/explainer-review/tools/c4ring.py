import sympy as sp
a,b=sp.Integer(1),sp.Rational(3,10); z=a+sp.I*b
H=sp.zeros(4)
for i in range(4):
    j=(i+1)%4; H[i,j]=z; H[j,i]=sp.conjugate(z)
Hb=H.conjugate(); Ds=sp.diag(1,-1,1,-1)
print('reflection branch: Hbar == -Ds*conj(H)*Ds^dag :', sp.simplify(Hb-(-Ds*H.conjugate()*Ds.H))==sp.zeros(4))
print('loop product H:',sp.expand(H[0,1]*H[1,2]*H[2,3]*H[3,0]),' Hbar:',sp.expand(Hb[0,1]*Hb[1,2]*Hb[2,3]*Hb[3,0]))
# countercontrol: a non-bipartite-compatible diagonal breaks the identity
H2=H.copy(); H2[0,0]=1; Hb2=H2.conjugate()
print('control (onsite term added): identity holds?', sp.simplify(Hb2-(-Ds*H2.conjugate()*Ds.H))==sp.zeros(4))
print('eigs',[sp.nsimplify(e) for e in H.eigenvals()])
