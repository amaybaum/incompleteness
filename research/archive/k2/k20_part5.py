exec(open('k20_part4.py').read().split('for i,cl in enumerate(cs):')[0])
from scipy.spatial.transform import Rotation as Rot
def loc(V): M=np.eye(4); M[1:,1:]=V; return M
surv=[0,1,6,7,10,11,12,13]
# exact witness for one failing class (-2): print the minimiser, rounded
H=group(Gs[cs[2][0]]); rs=[minval(h,trials=8) for h in H]; best=(min(rs,key=lambda r:r[0]),0)
(val,arg),j=best
print('witness for SO-class 2: value %.6f at s,t,f,g =' % val, [np.round(x,4).tolist() for x in arg])
Vs=[Rot.from_rotvec(r).as_matrix() for r in np.random.default_rng(7).normal(size=(6,3))]
for i in surv:
    c=cs[i][0]; G=np.array(Gs[c],dtype=float)
    worst=9
    for V in Vs:
        for W in (np.kron(loc(V),np.eye(4)), np.kron(np.eye(4),loc(V)), np.kron(loc(V),loc(Vs[0]))):
            for word in (G@W@G, G@W@G@W@G, G@np.linalg.inv(W)@G@W):
                worst=min(worst,minval(word,trials=6)[0])
    print('SO-class %2d rep %s unitary=%s : min product value over words with generic local rotations ~ %.4f' % (i,c,c in U_ or cs[i][1] in U_,worst))
