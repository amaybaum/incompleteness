exec(open('k20_part3.py').read().split("U_=set(")[0])
def unitary(G):
    C=superop(G); return C.rank()==1 and C==C.H and all(sp.re(C[i,i])>=0 for i in range(16))
Ry=sp.diag(1,1,-1,1)
T=kr(Ry,Ry)                                   # the full transpose in Pauli coordinates (y -> -y on both)
PB=kr(sp.eye(4),Ry)
surv=[0,1,6,7,10,11,12,13]; dead=[2,3,4,5,8,9,14,15]
for i in range(16):
    c=cs[i][0]; G=Gs[c]
    tags=[]
    if unitary(G): tags.append('unitary')
    if unitary(T*G): tags.append('antiunitary (T.U)')
    if unitary(PB*G*PB): tags.append('PT_B-conjugate of a unitary')
    if unitary(T*PB*G*PB): tags.append('PT_B-conjugate of an antiunitary')
    if unitary(PB*G): tags.append('PT_B after a unitary')
    if unitary(G*PB): tags.append('unitary after PT_B')
    print('SO-class %2d %s %-9s: %s' % (i, c, 'survives' if i in surv else 'fails', ', '.join(tags) or 'none of these'))
