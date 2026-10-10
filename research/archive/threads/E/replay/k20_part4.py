import sympy as sp, itertools, numpy as np
src=open('k20_part2.py').read().split('# 5. which gates')[0]
src=src.replace("print('(0)","_=('(0)").replace("    print('(1)","    _=('(1)").replace("print('(2)","_=('(2)").replace("print('    candidate","_=('    candidate").replace("print('    the inverse","_=('    the inverse").replace("print('    all satisfy","_=('    all satisfy").replace("print('(3)","_=('(3)").replace("print('    classes under","_=('    classes under")
exec(src)
U_={((-1,-1),(-1,-1,1,-1)),((-1,-1),(1,1,-1,1)),((1,1),(-1,-1,1,-1)),((1,1),(1,1,-1,1))}
def group(G):
    gens=[np.array(G,dtype=float),np.array(NI,dtype=float),np.array(IN,dtype=float)]
    H={np.eye(16).round(9).tobytes():np.eye(16)}; fr=[np.eye(16)]
    while fr:
        new=[]
        for h in fr:
            for g in gens:
                k=g@h; key=k.round(9).tobytes()
                if key not in H: H[key]=k; new.append(k)
        fr=new
        if len(H)>5000: return None
    return list(H.values())
rng=np.random.default_rng(1)
def minval(h,trials=60):
    """block-coordinate minimisation of (f(x)g) h (s(x)t) over four unit balls; each block step is exact (affine)"""
    best=9.0; arg=None
    for _ in range(trials):
        v=[np.r_[1,x/np.linalg.norm(x)] for x in rng.normal(size=(4,3))]
        for it in range(60):
            for b in range(4):
                s,t,f,g=v
                if b==0: c=np.einsum('i,j,ijkl,l->k',f,g,h.reshape(4,4,4,4),t)
                elif b==1: c=np.einsum('i,j,ijkl,k->l',f,g,h.reshape(4,4,4,4),s)
                elif b==2: c=np.einsum('j,ijkl,k,l->i',g,h.reshape(4,4,4,4),s,t)
                else: c=np.einsum('i,ijkl,k,l->j',f,h.reshape(4,4,4,4),s,t)
                w=c[1:]; n=np.linalg.norm(w)
                v[b]=np.r_[1,-w/n] if n>1e-14 else v[b]
        s,t,f,g=v; val=np.einsum('i,j,ijkl,k,l->',f,g,h.reshape(4,4,4,4),s,t)
        if val<best: best=val; arg=[x.copy() for x in v]
    return best,arg
for i,cl in enumerate(cs):
    c=cl[0]; H=group(Gs[c])
    if H is None: print('SO-class',i,'group > 5000'); continue
    worst=min((minval(h,trials=8)[0],j) for j,h in enumerate(H))
    print('SO-class %2d rep %s unitary=%s |<G,N(x)I,I(x)N>| = %d  min over group of product value ~ %.4f' % (i,c,c in U_ or cl[1] in U_,len(H),worst[0]))
