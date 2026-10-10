exec(open('k20_part4.py').read().split('for i,cl in enumerate(cs):')[0])
from fractions import Fraction as Fr
axes=[]
for i in (1,2,3):
    for sgn in (1,-1):
        v=[0,0,0,0]; v[0]=1; v[i]=sgn; axes.append(v)
diag=[[1,a,b,0] for a in (1,-1) for b in (1,-1)]   # unnormalised in-plane directions, scaled below
def exact_witness(h):
    """search pure axis states/effects (integer) for a negative product value; exact integer arithmetic"""
    h=[[int(round(x)) for x in row] for row in h]
    best=None
    for s in axes:
        for t in axes:
            st=[s[i]*t[j] for i in range(4) for j in range(4)]
            out=[sum(h[r][c]*st[c] for c in range(16)) for r in range(16)]
            for f in axes:
                for g in axes:
                    v=sum(f[i]*g[j]*out[4*i+j] for i in range(4) for j in range(4))
                    if best is None or v<best[0]: best=(v,s,t,f,g)
    return best
assert all(float(x).is_integer() for G in Gs.values() for x in G)
for i,cl in enumerate(cs):
    c=cl[0]; G=Gs[c]; H=group(G)
    g_alone=minval(np.array(G,dtype=float),trials=20)[0]
    w=min((exact_witness(h) for h in H),key=lambda b:b[0])
    print('SO-class %2d: G alone min ~ %.4f; exact axis-state minimum over the group = %d%s' % (i,g_alone,w[0],('  at s,t,f,g = %s' % (w[1:],)) if w[0]<0 else ''))
