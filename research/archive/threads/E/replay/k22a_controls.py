exec(open('k22a_closure.py').read().split("surv={0:")[0])
def closure_dim(G):
    pows=[[[int(a==b) for b in range(16)] for a in range(16)]]; P=G
    while P!=pows[0]: pows.append(P); P=mul(P,G)
    gens=[]
    for Pw in pows:
        Pi=inv_signed_perm(Pw); gens+=[mul(mul(Pw,x),Pi) for x in local]
    L=lie_closure(gens); return len(L), same(L,su4), same(L,su4PT)
Id=[[int(a==b) for b in range(16)] for a in range(16)]
SW=[[int(b==(a%4)*4+a//4) for b in range(16)] for a in range(16)]            # SWAP in Bloch coordinates
print('control identity  :', closure_dim(Id))
print('control SWAP      :', closure_dim(SW))
print('control N(x)N     :', closure_dim(kron([[1,0,0,0],[0,1,0,0],[0,0,-1,0],[0,0,0,-1]],[[1,0,0,0],[0,1,0,0],[0,0,-1,0],[0,0,0,-1]])))
for i in (2,3,4,5,8,9,14,15):
    print('failing SO-class %2d:' % i, closure_dim(M(Gs[cs[i][0]])))
