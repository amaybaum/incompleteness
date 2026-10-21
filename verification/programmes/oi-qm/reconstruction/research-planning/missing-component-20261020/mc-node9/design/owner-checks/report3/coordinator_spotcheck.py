from fractions import Fraction as F
# R = (1/5)[[3,-4],[4,3]] on |0>: amplitudes (3,4)/5; R^2: (-7,24)/25
def apply(M,v): return [M[0][0]*v[0]+M[0][1]*v[1], M[1][0]*v[0]+M[1][1]*v[1]]
R=[[F(3,5),F(-4,5)],[F(4,5),F(3,5)]]
v1=apply(R,[F(1),F(0)]); v2=apply(R,v1)
print('P0 after R:',v1[0]**2,' after R^2:',v2[0]**2)
# R;S;R with S=diag(1,i): amplitude a0 = R00*1*R00*... compute with Gaussian rationals (re,im)
def cm(a,b): return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])
def ca(a,b): return (a[0]+b[0],a[1]+b[1])
s=[(v1[0],F(0)),cm((v1[1],F(0)),(F(0),F(1)))]   # after S
a0=ca(cm((R[0][0],F(0)),s[0]),cm((R[0][1],F(0)),s[1]))
print('P0 after R S R:',a0[0]**2+a0[1]**2)
# dephasing after first R then R: P0 = 9/25*9/25 + 16/25*16/25
print('dephased R;R P0:',F(9,25)**2+F(16,25)**2)
# diamond L1 of R|0>: x = 2*a*b = 24/25, z = a^2-b^2 = -7/25
a,b=v1; print('|x|+|z| =',abs(2*a*b)+abs(a*a-b*b))
