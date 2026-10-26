"""Independent q7 and two-upper-pulse correction, with reviewed v5 helpers.

No author dynamics imported. Uses the previous independent review's generic
native recursion and geometry functions, bound by SHA256. No files are written.
"""
from pathlib import Path
from hashlib import sha256
import json
import runpy

HERE=Path(__file__).resolve().parent
CANDIDATES=(HERE.parent/'six_source_v5_review/checks.py',
            HERE.parent.parent/'six_source_v5/review/checks.py')
HELPER=next((p for p in CANDIDATES if p.exists()),None)
if HELPER is None:
    raise RuntimeError('Missing independently reviewed v5 helper')
if sha256(HELPER.read_bytes()).hexdigest()!='467fbff795407b2a2744465166ac6fd0958dbef768606b2a40a9ed6b97120728':
    raise RuntimeError('Independent helper digest mismatch')
V=runpy.run_path(str(HELPER),run_name='independent_v5_helpers')
for name in ('need','Z','xx','hh','variable','direct','strip_keys','ball','norm','hp','odd','native_update','T','P','S','R'):
    globals()[name]=V[name]

KEYS=strip_keys(14)
GROUPS={ell:[key for key in KEYS if key[0]==ell] for ell in range(15)}


def advance(old):
    look=[{} for _ in range(9)]
    for ell in range(15):
        for jump in range((14-ell)//2+1):
            for _,a,b in GROUPS[ell]:
                if ell+abs(a)+abs(b)>14-2*jump:
                    continue
                prior=old[ell,a,b] if jump==0 else look[jump-1][ell,a,b]
                terms=[prior,look[jump+1].get((ell-2,a,b),Z)]
                terms.extend(look[jump].get((ell-1,aa,bb),Z)
                             for aa,bb in ((a-1,b),(a+1,b),(a,b-1),(a,b+1)))
                look[jump][ell,a,b]=xx(look[jump].get((ell-2,a,b),Z),hh(xx(*terms)))
    return look[0]


def triple(value,lane):
    return tuple(word>>lane&1 for word in value)


def code(value,lane):
    return sum((word>>lane&1)<<field for field,word in enumerate(value))


def evaluate_strip():
    variables=[variable(i,16) for i in range(4)]
    sources={(0,0,0):(variables[0],0,(1<<16)-1),
             (0,-14,0):tuple(variables[1:])}
    at=direct(sources,packed=True)
    initial={key:at(key[0],(key[1],0,key[2])) for key in KEYS}
    states=[initial]
    for n in range(1,254):
        states.append(advance(states[-1]))
    # Actual two-source direct controls, including the meeting at tick7 and
    # Q arrival at the old source at tick14. Signed positions, all16 lanes.
    checks=0
    for n in range(5):
        for ell,a,b in KEYS:
            need(states[n][ell,a,b]==at(n+ell,(a,n,b)), 'two-upper-source direct strip')
            checks+=1
    need(P%(12*840**14)==0, 'L14 exact giant period divisibility')
    mappings=[]
    correction=[]
    for u in (0,1):
        mapping=[code(states[245][14,0,0],u+2*q) for q in range(8)]
        need(len(set(mapping))==8,'actual incoming map is permutation')
        old=triple(states[246][12,0,0],u)
        need(old==(1,1,1), 'old local triple upper only')
        wanted=mapping[0] ^ (u*old[0]) ^ (u<<2)
        choices=[q for q,z in enumerate(mapping) if z==wanted]
        need(len(choices)==1, 'unique exact initial correction')
        mappings.append(mapping)
        correction.append(choices[0])
        need(all(triple(states[246][12,0,0],u+2*q)==old for q in range(8)), 'pivot cannot change old target')
    need(correction==[0,5], 'correction payload is (u,0,u)')
    print('O1: signed L14 two-source strip, %d direct positions x16 lanes; actual incoming permutations=%s; old local triple111; unique correction Q=[000,101]: PASS' % (checks,mappings))
    return states


def evaluate_endpoint(states,correction=False,operand='qY'):
    variables=[variable(i,32) for i in range(5)]
    x,u,my,mr,p=variables
    ones=(1<<32)-1
    controls=(((0,-S,-68),x),((0,S,-68),my^mr),((T,P,-68),my),((-T,P,-68),mr))
    def base(tau,pos):
        a,b,z=pos
        n=R-z
        ell=tau+z
        result=Z
        if ell>=abs(a)+abs(b) and (ell-a-b)%2==0:
            need((ell,a,b) in KEYS and 0<=n-P<len(states),'upper pre-collision coverage')
            value=states[n-P][ell,a,b]
            lane1=11 if correction else 1
            result=tuple((ones if word&1 else 0) ^ (u if ((word&1)^((word>>lane1)&1)) else 0)
                         for word in value)
        for source,bit in controls:
            disp=tuple(abs(v-w) for v,w in zip(pos,source))
            need(sum(disp)>=R+tau,'lower controls are first fronts')
            if sum(disp)==R+tau and odd(disp):
                field=hp(2,R+tau)
                result=xx(result,tuple(bit if field>>i&1 else 0 for i in range(3)))
        return result
    old={pos:base(-2,pos) for pos in ball(7,(0,0,7))}
    now={pos:base(-1,pos) for pos in ball(8,(0,0,7))}
    for tick in range(8):
        nxt=native_update(old,now,7-tick,(0,0,7))
        if tick==0:
            need(nxt[0,0,0]==(x,ones,x^u),'qY native before diagnostic')
            if operand=='qY':
                nxt[0,0,0]=(x,ones,p)
        if tick==2 and operand=='q2':
            q=nxt[0,0,2]
            need(q==(x^u,x^u,ones^(x&(x^u))),'q2 native before diagnostic')
            nxt[0,0,2]=(p,q[1],q[2])
        old,now=now,nxt
    return now[0,0,7]


def check_geometry_and_algebra():
    target=(0,S,75)
    deadline=R+7
    pivot=(0,S,S+150)
    upper=(0,S,S+136)
    need(norm(tuple(a-b for a,b in zip(pivot,target)))==deadline,'pivot first arrival at target')
    need(norm(tuple(a-b for a,b in zip(pivot,upper)))==14,'two-upper separation')
    lowers=((0,0,0),(0,2*S,0),(T,P+S,0),(-T,P+S,0))
    for loc in lowers:
        need(norm(tuple(a-b for a,b in zip(target,loc)))==deadline,'all lower target distances')
        for height in (1,2,7,14,deadline):
            ray=(target[0],target[1],target[2]+height)
            need(norm(tuple(a-b for a,b in zip(ray,loc)))==deadline+height,'lower sources outside correction ray past')
    need(norm(tuple(a-b for a,b in zip(target,(0,-2,0))))==deadline+2,'M2 outside q7 cone')
    need(norm(tuple(a-b for a,b in zip(target,(0,S,-S-136))))>deadline,'opposite pulse excluded')
    need(11*R>deadline,'all radius-R remote blocks excluded by x separation')
    need(norm(tuple(a-b for a,b in zip(pivot,target)))>deadline-1,'pivot outside previous ready ball')
    old_regions=(((0,T,0),T),((T,0,0),T),((-T,0,0),T),((4*T,0,0),T),((0,0,-8*T),T),
                 ((0,S,0),S),((T,P,0),S),((-T,P,0),S),((4*T,P,0),S),
                 ((0,S,68),R),((0,S,-68),R),((0,S,70),R+2),((0,S,71),R+3),
                 ((12*R,0,0),R),((-12*R,0,0),R))
    for center,radius in old_regions:
        distance=norm(tuple(a-b for a,b in zip(pivot,center)))
        need(distance>radius and distance>deadline,'pivot outside old ready balls and old histories through N')
    need(norm(tuple(a-b for a,b in zip(pivot,(0,S-1,70))))>deadline,'prior history sidecar also unaffected')
    for k in range(1,7):
        need(norm(tuple(a-b for a,b in zip(pivot,(0,S,68+k))))>R+k,'earlier outward endpoint unchanged')
    geo_candidates=(HERE.parent/'repo_checkpoint/payload/parallel_v3/history_control/SOURCE-GEOMETRY.json',
                    HERE.parent.parent/'parallel_v3/history_control/SOURCE-GEOMETRY.json')
    geo_path=next((p for p in geo_candidates if p.exists()),None)
    need(geo_path is not None,'inherited source geometry available')
    geo_bytes=geo_path.read_bytes()
    need(sha256(geo_bytes).hexdigest()=='2642e1a68825faa5d3bb1049e8722adec1ec33bd3f56b9e4416b2c902a85ec5d','source geometry digest')
    sources=json.loads(geo_bytes)['sources']
    boundary=[]
    for row in sources:
        pos=tuple(row['position'])
        distance=norm(tuple(a-b for a,b in zip(pos,target)))
        need(pos!=pivot and distance>=deadline,'no old source overwritten or added to cold interior')
        if distance==deadline:
            boundary.append((pos,row['field'],row['mask']))
    need(len(sources)==1479 and boundary==[((0,0,0),1,64)],'only origin inherited boundary source')
    # These equalities are the all-j affine distance formulas, evaluated at
    # representatives as a guard. The positive sign regions hold for every j>0.
    for j in (1,2,7,T,P,R):
        banks=(((0,-j,0),j),((0,0,-9*T-j),9*T+j),
               ((0,2*S+j,0),j),((T,P+S+j,0),j),
               ((-T,P+S+j,0),j),((4*T,P+S+j,0),3*T+j))
        for pos,slack in banks:
            need(norm(tuple(a-b for a,b in zip(pos,target)))-deadline==slack,'positive all-index frontier slack')
            need(pos!=pivot,'controlled pivot does not overwrite a fair bank')
    need(hp(4,R-7)==4 and hp(5,R-7)==7,'unchanged informative early prefix (u,u,1)')
    # Prove the update identity by complete finite enumeration of W,V,u.
    HT=V['HT']
    for old in range(8):
        for neighbors in range(8):
            original=old^HT[neighbors]
            for u in range(2):
                delta=(u*(old&1))|(u<<2)
                changed=old^HT[neighbors^delta]
                need(changed^original==((u<<1)|((u*(original&1))<<2)), 'general final-update correction identity')
    print('O2: unique axial pivot,1479 old sources,15 ready/old-history regions,all-index bank slack formulas and unchanged informative prefix; all128 update identities give delta output=(0,u,u*old_output.A): PASS')


if __name__=='__main__':
    author=HERE.parent if (HERE.parent/'model.py').exists() else HERE.parent/'repo_checkpoint/payload/outward_v6'
    for name,digest in json.loads((HERE/'INPUT-HASHES.json').read_text()).items():
        path=author/name
        if not path.exists():
            path=HERE.parent/'outward_v6_geometry'/name
        need(path.exists() and sha256(path.read_bytes()).hexdigest()==digest,'reviewed author digest: '+name)
    check_geometry_and_algebra()
    states=evaluate_strip()
    original=evaluate_endpoint(states)
    corrected=evaluate_endpoint(states,True)
    original2=evaluate_endpoint(states,False,'q2')
    corrected2=evaluate_endpoint(states,True,'q2')
    for lane in range(32):
        x,u,my,mr,p=(lane>>i&1 for i in range(5))
        expected=(x*(1-u)*(1-p),x*(1-p)^(u*p),p)
        need(triple(original,lane)==expected,'unmodified whole qY diagnostic formula')
        expected_corrected=(expected[0],expected[1]^u,expected[2])
        need(triple(corrected,lane)==expected_corrected,'corrected whole qY diagnostic formula')
        if p==x^u:
            need(triple(corrected,lane)==(0,0,p),'corrected native clean code')
        q2_expected=(x^(x*u)^p^(u*p),x^p,x^(x*u)^p^(x*p)^(x*u*p))
        need(triple(original2,lane)==q2_expected,'q2-only diagnostic baseline')
        q2_corrected=(q2_expected[0],q2_expected[1]^u,q2_expected[2]^(u*q2_expected[0]))
        need(triple(corrected2,lane)==q2_corrected,'q2-only correction response')
    pword=variable(4,32)
    ones=(1<<32)-1
    raw_q2=[i for i,field in enumerate(corrected2) if field in (pword,pword^ones)]
    need(raw_q2==[], 'corrected q7 is not raw q2-only operand transfer')
    print('O3: independent full eight-step q7 assembly; all32 original/corrected qY and q2 diagnostic triples; corrected native code00y, qY diagnostic D=p, no raw q2-only field: PASS')
    print('SCOPE: ACCEPT modified initial q7 readout and stated readiness geometry; private access and147 extra old-port fair bits remain required. No arbitrary-input clean socket, joint-record certification, or native reset.')
