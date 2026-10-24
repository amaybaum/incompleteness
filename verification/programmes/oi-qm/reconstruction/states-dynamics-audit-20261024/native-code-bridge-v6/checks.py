"""Exact common-code bridge diagnostic; no native engine or external input."""
from fractions import Fraction as F
from itertools import product
from collections import defaultdict
import json


def require(ok,label):
    if not ok:
        raise RuntimeError(label)


CODES=tuple(c for c in product((0,1),repeat=4)
            if c[0]!=c[1] or c[2]==c[0])


def sign(bit):
    return 1-2*bit


def native(axis,s):
    weights=(F(1,2),F(2,5),F(1,10)) if axis=='X' else (F(1,2),F(3,10),F(1,5))
    out=defaultdict(F)
    for (a,b),p in zip(((0,0),(1,0),(1,1)),weights):
        for z in (0,1):
            c=(s,s^a,s^b,z) if axis=='X' else (s^a,s,s^b,z)
            require(c in CODES,'native support')
            out[c]+=p/2
    return dict(out)


def solve(matrix,rhs):
    a=[list(map(F,row))+[F(b)] for row,b in zip(matrix,rhs)]
    for col in range(len(rhs)):
        pivot=next(i for i in range(col,len(rhs)) if a[i][col])
        a[col],a[pivot]=a[pivot],a[col]
        v=a[col][col]
        a[col]=[x/v for x in a[col]]
        for i in range(len(rhs)):
            if i!=col:
                v=a[i][col]
                a[i]=[x-v*y for x,y in zip(a[i],a[col])]
    return [row[-1] for row in a]


def geometric_pushforward(axis,s):
    # Hemisphere marginals and deterministic sign support specify the
    # three possible plane cells. Z-reflection splits each cell equally.
    ai=0 if axis=='X' else 1
    other=1-ai
    planes=[c for c in product((0,1),repeat=3)
            if (c[0]!=c[1] or c[2]==c[0]) and c[ai]==s]
    rmean=F(4,5) if axis=='X' else F(3,5)
    mass=solve([[1]*3,[sign(c[other]) for c in planes],
                [sign(c[2]) for c in planes]], [1,0,sign(s)*rmean])
    require(all(p>=0 for p in mass),'positive geometric plane solution')
    return {(*c,z):p/2 for c,p in zip(planes,mass) for z in (0,1)}


def tv(p,q):
    return sum(abs(p.get(k,F(0))-q.get(k,F(0))) for k in set(p)|set(q))/2


def bern(p):
    return {0:p,1:1-p}


# Independent exact rational complex matrix projector calculation.
ZERO=(F(0),F(0));ONE=(F(1),F(0));I=(F(0),F(1))


def ca(a,b):return (a[0]+b[0],a[1]+b[1])
def cm(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def scale(a,t):return (a[0]*t,a[1]*t)


PAULI=(((ZERO,ONE),(ONE,ZERO)),
       ((ZERO,(F(0),F(-1))),(I,ZERO)),
       ((ONE,ZERO),(ZERO,(F(-1),F(0)))))


def density(r):
    return tuple(tuple(scale(ca(ONE if i==j else ZERO,
                     sum_complex(scale(PAULI[k][i][j],r[k]) for k in range(3))),F(1,2))
                     for j in range(2)) for i in range(2))


def sum_complex(xs):
    out=ZERO
    for x in xs:out=ca(out,x)
    return out


def quantum_plus(r,a):
    rho=density(r);p=density(a)
    value=sum_complex(cm(p[i][j],rho[j][i]) for i in range(2) for j in range(2))
    require(value[1]==0 and 0<=value[0]<=1,'projector probability')
    return value[0]


def main():
    require(len(CODES)==12,'twelve valid sign codes')
    pushforwards=0
    old_menu=0
    axes=[(1,0,0),(0,1,0),(F(4,5),F(3,5),0),(0,0,1)]
    for axis in ('X','Y'):
        for s in (0,1):
            p=native(axis,s)
            require(sum(p.values())==1,'native normalization')
            require(p==geometric_pushforward(axis,s),'full sphere/native pushforward')
            require(all(sum(v for c,v in p.items() if c[3]==z)==F(1,2) for z in (0,1)),
                    'fair Z')
            r=(sign(s),0,0) if axis=='X' else (0,sign(s),0)
            for k,a in enumerate(axes):
                plus=sum(v for c,v in p.items() if c[k]==0)
                require(plus==quantum_plus(r,a),'old observable projector comparison')
                old_menu+=1
            pushforwards+=1

    px,py=native('X',0),native('Y',0)
    source_tv=tv(px,py)
    a=(F(3,5),F(-4,5),0)
    qx=bern(quantum_plus((1,0,0),a))
    qy=bern(quantum_plus((0,1,0),a))
    target_tv=tv(qx,qy)
    floor=(target_tv-source_tv)/2
    require((source_tv,target_tv,floor)==(F(1,2),F(7,10),F(1,10)),
            'exact common-code pair bound')
    overlap={c:min(px.get(c,F(0)),py.get(c,F(0))) for c in CODES}
    require(sum(overlap.values())==F(1,2),'overlap mass')
    require({c for c,v in overlap.items() if v}=={(0,0,0,0),(0,0,0,1)},
            'shared geometric sign cells')

    wx=[int(20*px.get(c,F(0))) for c in CODES]
    wy=[int(20*py.get(c,F(0))) for c in CODES]
    best=20;maximum_distance=0
    for response in range(1<<12):
        x=sum(w for j,w in enumerate(wx) if (response>>j)&1)
        y=sum(w for j,w in enumerate(wy) if (response>>j)&1)
        require(abs(x-y)<=10,'deterministic response contraction')
        maximum_distance=max(maximum_distance,abs(x-y))
        best=min(best,max(abs(x-16),abs(y-2)))
    require((best,maximum_distance)==(3,10),'complete deterministic response control')

    def kernel(c):
        if c[:3]==(0,0,0):return F(2,5)
        return F(1) if c[0]==0 and c[1]==1 else F(0)
    rx=bern(sum(p*kernel(c) for c,p in px.items()))
    ry=bern(sum(p*kernel(c) for c,p in py.items()))
    require(rx[0]==F(7,10) and ry[0]==F(1,5),'sharp stochastic pair control')
    require(tv(rx,qx)==tv(ry,qy)==floor,'pair floor attained')
    source_apparatus_x={(c,j):p/5 for c,p in px.items() for j in range(5)}
    source_apparatus_y={(c,j):p/5 for c,p in py.items() for j in range(5)}
    require(tv(source_apparatus_x,source_apparatus_y)==source_tv,'independent apparatus')
    inverse_cases=0
    for c,j,bit in product(CODES,range(5),(0,1)):
        out=int(j<2) if c[:3]==(0,0,0) else int(c[0]==0 and c[1]==1)
        require((bit^out)^out==bit,'retained reversible record control')
        inverse_cases+=1

    labelled_x={(0,c):p for c,p in px.items()}
    labelled_y={(1,c):p for c,p in py.items()}
    require(tv(labelled_x,labelled_y)==1,'preparation label changes source information')
    labelled_qx=bern(F(sum(j<8 for j in range(10)),10))
    labelled_qy=bern(F(sum(j<1 for j in range(10)),10))
    require(labelled_qx==qx and labelled_qy==qy,'label-dependent controller control')

    # Two open-cell witnesses of information discarded by the sign quotient.
    sphere_points=((F(6,7),F(2,7),F(3,7)),(F(2,3),F(2,3),F(1,3)))
    new_signs=[]
    for v in sphere_points:
        require(sum(x*x for x in v)==1,'unit sphere witness')
        code=tuple(int(sum(x*y for x,y in zip(v,n))<0) for n in axes)
        require(code==(0,0,0,0),'same finite sign cell')
        value=sum(x*y for x,y in zip(v,a))
        require(value!=0,'open measurement witness')
        new_signs.append(int(value<0))
    require(new_signs==[0,1],'new read splits one old code cell')
    require(F(1,2)>target_tv**2,'continuous pure-pair TV permits target')

    print(json.dumps({'schema':'oi.native-code-bridge.v6',
        'source_codes':12,'full_native_sphere_pushforwards':pushforwards,
        'old_menu_projector_comparisons':old_menu,'source_pair_tv':str(source_tv),
        'target_new_read_pair_tv':str(target_tv),'sharp_stochastic_pair_error':str(floor),
        'deterministic_responses_checked':4096,'best_deterministic_pair_error':str(F(best,20)),
        'independent_five_value_apparatus_inverse_cases':inverse_cases,
        'labelled_source_tv':'1','same_cell_opposite_new_sign_witnesses':2,
        'continuous_pure_pair_tv_squared':'1/2',
        'scope':'Common selected twelve-code interface and common independent apparatus only; actual native full phase/history/response memory not excluded.',
        'verdict':'PASS_SCOPED_COARSE_CODE_BRIDGE_AND_ERROR_BOUND'},sort_keys=True,indent=2))


if __name__=='__main__':main()
