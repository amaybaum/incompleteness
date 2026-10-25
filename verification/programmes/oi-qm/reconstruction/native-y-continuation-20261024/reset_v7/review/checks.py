"""Independent native q7 interface and Q/C/G one-step continuation audit.

Stdlib only; no author dynamics imports. Stdout is structured JSON. Author
results are comparison targets, never inputs to the native evolution.
"""
from contextlib import redirect_stdout
from hashlib import sha256
from itertools import product
from pathlib import Path
import io
import json
import runpy

HERE=Path(__file__).resolve().parent


def locate(suffixes):
    for base in (HERE,*HERE.parents):
        for suffix in suffixes:
            path=base/suffix
            if path.exists():
                return path
    raise RuntimeError('Missing dependency: '+str(suffixes))


HELPER=locate(('six_source_v5_review/checks.py','six_source_v5/review/checks.py'))
if sha256(HELPER.read_bytes()).hexdigest()!='467fbff795407b2a2744465166ac6fd0958dbef768606b2a40a9ed6b97120728':
    raise RuntimeError('Prior independent native helper changed')
V=runpy.run_path(str(HELPER),run_name='independent_native_helpers')
for name in ('need','Z','E','xx','hh','variable','direct','strip_keys','ball','norm','hp','odd','native_update','T','P','S','R'):
    globals()[name]=V[name]
AUTHOR=HERE.parent if (HERE.parent/'probe.py').exists() else locate(('repo_checkpoint/payload/reset_v7/probe.py','reset_v7/probe.py')).parent
KEYS=strip_keys(16)
GROUPS={ell:[key for key in KEYS if key[0]==ell] for ell in range(17)}
N=R+7


def advance(old):
    look=[{} for _ in range(10)]
    for ell in range(17):
        for jump in range((16-ell)//2+1):
            for _,a,b in GROUPS[ell]:
                if ell+abs(a)+abs(b)>16-2*jump:
                    continue
                prior=old[ell,a,b] if jump==0 else look[jump-1][ell,a,b]
                terms=[prior,look[jump+1].get((ell-2,a,b),Z)]
                terms.extend(look[jump].get((ell-1,aa,bb),Z)
                             for aa,bb in ((a-1,b),(a+1,b),(a,b-1),(a,b+1)))
                look[jump][ell,a,b]=xx(look[jump].get((ell-2,a,b),Z),hh(xx(*terms)))
    return look[0]


def triple(value,lane):
    return tuple(word>>lane&1 for word in value)


def index(row):
    x,u,my,mr,p,g=row
    return x+2*u+4*my+8*mr+16*p+32*(g[0]+2*g[1]+4*g[2])


def strips():
    u=variable(0,16)
    sources={(0,0,0):(u,0,65535),(0,-14,0):(u,0,u),
             (0,-16,0):tuple(variable(i,16) for i in (1,2,3))}
    at=direct(sources,packed=True)
    states=[{key:at(key[0],(key[1],0,key[2])) for key in KEYS}]
    for n in range(1,254):
        states.append(advance(states[-1]))
    comparisons=0
    for n in range(6):
        for ell,a,b in KEYS:
            need(states[n][ell,a,b]==at(n+ell,(a,n,b)),'full interacting tripole direct recursion')
            comparisons+=16
    need(P%(12*840**16)==0,'actual universal strip exponent')
    prior=locate(('outward_v6_review/checks.py','outward_v6/review/checks.py'))
    need(sha256(prior.read_bytes()).hexdigest()=='ef730e8102c89e79e5a3974c3bdf9bc7ddaba6d23f7fb50ba35aba6dd03f9e5e','prior independent correction checker digest')
    old=runpy.run_path(str(prior),run_name='independent_correction_helpers')
    with redirect_stdout(io.StringIO()):
        dipole=old['evaluate_strip']()
    regression=0
    for n in (0,3,100,245):
        for key in strip_keys(14):
            for uu in (0,1):
                expected=triple(dipole[n][key],uu+10*uu)
                # G cannot influence any layer<=14; check every G, not only G=0.
                for g in range(8):
                    need(triple(states[n][key],uu+2*g)==expected,'prior independent Q/C projection')
                    regression+=1
    return states,comparisons,regression


def calculate(states,site):
    x,u,my,mr,p=(variable(i,256) for i in range(5))
    ones=(1<<256)-1
    controls=(((0,-S,-68),x),((0,S,-68),my^mr),((T,P,-68),my),((-T,P,-68),mr))
    def upper(tau,pos):
        a,b,z=pos
        ell=tau+z
        if ell<abs(a)+abs(b) or (ell-a-b)%2:
            return Z
        axial=R-z-P
        need((ell,a,b) in KEYS and 0<=axial<len(states),'L16 initial upper slice coverage')
        val=states[axial][ell,a,b]
        result=[0,0,0]
        for lane in range(256):
            src=((lane>>1)&1)+2*(lane>>5)
            for field in range(3):
                result[field]|=((val[field]>>src)&1)<<lane
        return tuple(result)
    def base(tau,pos):
        val=upper(tau,pos)
        for source,bit in controls:
            disp=tuple(abs(a-b) for a,b in zip(source,pos))
            need(sum(disp)>=R+tau,'lower sources cannot be behind first front')
            if sum(disp)==R+tau and odd(disp):
                field=hp(2,R+tau)
                val=xx(val,tuple(bit if field>>i&1 else 0 for i in range(3)))
        return val
    old={p:base(-2,p) for p in ball(8,(0,0,8))}
    now={p:base(-1,p) for p in ball(9,(0,0,8))}
    records=[]
    for tick in range(9):
        nxt=native_update(old,now,8-tick,(0,0,8))
        if tick==0:
            need(nxt[0,0,0]==(x,ones,x^u),'qY native inherited control')
            if site=='qY':
                nxt[0,0,0]=(x,ones,p)
        if tick==2 and site=='q2':
            q=nxt[0,0,2]
            need(q==(x^u,x^u,ones^(x&(x^u))),'q2 native inherited control')
            nxt[0,0,2]=(p,q[1],q[2])
        if tick==7 and site=='q7':
            need(nxt[0,0,7]==(0,0,x^u),'q7 native inherited control')
            nxt[0,0,7]=(0,0,p)
        records.append(nxt)
        old,now=now,nxt
    return now[0,0,8],records


def geometry():
    distance=lambda a,b:norm(tuple(x-y for x,y in zip(a,b)))
    q7=(0,S,75)
    q8=(0,S,76)
    q9=(0,S,77)
    f=(0,S,S+150)
    g=(0,S,S+152)
    need((distance(g,q7),distance(g,q8),distance(g,q9))==(N+2,N+1,N),'G first arrival distances')
    need(distance(g,q7)>N and distance(g,q7)>N-1,'G outside adopted current/previous q7 readiness')
    need(distance(g,f)==2 and distance(f,q8)==N-1,'C preserved inside extended cone')
    need(distance(q7,q8)==1,'depth8 cone contains depth7 cone on both slices')
    old_regions=(((0,T,0),T),((T,0,0),T),((-T,0,0),T),((4*T,0,0),T),((0,0,-8*T),T),
                 ((0,S,0),S),((T,P,0),S),((-T,P,0),S),((4*T,P,0),S),
                 ((0,S,68),R),((0,S,-68),R),((0,S,70),R+2),((0,S,71),R+3),
                 ((12*R,0,0),R),((-12*R,0,0),R))
    need(all(distance(g,c)>max(radius,N+1) for c,radius in old_regions),'G-only preserves old preparation and receiver histories')
    need(distance(g,(0,S-1,70))>N+1,'old sidecar unaffected by G')
    need(distance(g,q8)>N-1,'q8 old local term independent of G')
    for e in E:
        neighbor=tuple(a+b for a,b in zip(q8,e))
        need(distance(g,neighbor)==(N if neighbor==q9 else N+2),'only upper neighbor affected at N')
    lowers=((0,0,0),(0,2*S,0),(T,P+S,0),(-T,P+S,0))
    upper=(0,S,S+136)
    for loc in lowers:
        need(distance(loc,q8)==N+1 and distance(loc,upper)==2*R,'lower front and earliest interaction')
        need(distance(loc,g)==2*(N+1),'lower sources outside incoming G ray')
    need(distance((0,0,0),q8)>N and distance((0,S,-S-136),q8)>N+1,'previous unknown and opposite pulse excluded')
    need(11*R>N+1 and 76<T,'remote and original-source exclusion bounds')
    # Each sign in these L1 distances remains fixed for all j>0. Therefore
    # the stated affine equality, not a finite j census, is the general proof.
    for j in (1,2,8,T,P,R):
        banks=(((0,-j,0),j),((0,0,-9*T-j),9*T+j),((0,2*S+j,0),j),
               ((T,P+S+j,0),j),((-T,P+S+j,0),j),((4*T,P+S+j,0),3*T+j))
        for pos,slack in banks:
            need(distance(pos,q8)-(N+1)==slack,'protected all-index frontier slack')
            need(pos!=g and pos!=f,'upper controls do not overwrite reserved bank')
    geo=locate(('parallel_v3/history_control/SOURCE-GEOMETRY.json',
                'repo_checkpoint/payload/parallel_v3/history_control/SOURCE-GEOMETRY.json'))
    data=geo.read_bytes()
    need(sha256(data).hexdigest()=='2642e1a68825faa5d3bb1049e8722adec1ec33bd3f56b9e4416b2c902a85ec5d','source geometry digest')
    sources=json.loads(data)['sources']
    boundary=[]
    for entry in sources:
        pos=tuple(entry['position'])
        need(distance(pos,q8)>=N+1 and pos!=g,'original-source exclusions')
        if distance(pos,q8)==N+1:
            boundary.append((pos,entry['field'],entry['mask']))
    need(len(sources)==1479 and boundary==[((0,0,0),1,64)],'only original input on boundary')
    return {'original_sources':1479,'prior_ready_regions':15,'G_current_q7_slack':2,
            'public_bits_beyond_R_if_extended':7*3*8,'additional_bits_beyond_q7':7*3,
            'joint_history_certified':False}


def main():
    hashes=json.loads((HERE/'INPUT-HASHES.json').read_text())
    for name,digest in hashes.items():
        need(sha256((AUTHOR/name).read_bytes()).hexdigest()==digest,'author input digest: '+name)
    geom=geometry()
    states,direct_count,projection_count=strips()
    outputs={}
    records={}
    for site in ('qY','q2','q7'):
        outputs[site],records[site]=calculate(states,site)
    # Compare the entire independent output and actual q7 input neighborhoods.
    retained=json.loads((AUTHOR/'results.json').read_text())
    comparisons=0
    for site,entries in retained['q8_diagnostics'].items():
        for entry in entries:
            need(triple(outputs[site],index(entry['row']))==tuple(entry['q8']),'published full diagnostic table')
            comparisons+=1
    incoming_comparisons=0
    for site,entries in retained['q7_interface'].items():
        rec=records[site]
        for entry in entries:
            row=tuple(entry['row'])
            lane=index(row+((0,0,0),))
            need(triple(rec[5][0,0,7],lane)==tuple(entry['old_local']),'actual q7 old local')
            for position,value in entry['incoming'].items():
                pos=tuple(map(int,position.split(',')))
                need(triple(rec[6][pos],lane)==tuple(value),'actual q7 incoming neighbor')
                incoming_comparisons+=1
            need(triple(rec[7][0,0,7],lane)==tuple(entry['endpoint']),'actual q7 endpoint')
            for g in product((0,1),repeat=3):
                need(triple(rec[7][0,0,7],index(row+(g,)))==tuple(entry['endpoint']),'G does not change q7')
            x,u,my,mr,p=row
            known=(x*(1-u)*(1-p),(x^u)*(1-p),p) if site=='qY' else ((x^p)*(1-u),x^u^p,x^(x*u)^p^(x*p)^(x*u*p))
            need(triple(rec[7][0,0,7],lane)==known,'previously independently checked full q7 diagnostic')
    # Verify concise native interface directly, including all selector masks.
    for x,u,my,mr in product((0,1),repeat=4):
        lane=index((x,u,my,mr,x^u,(0,0,0)))
        expected={(-1,0,7):(1^u,1,u*mr),(1,0,7):(1^u,1,u*my),
                  (0,-1,7):(1^u,1,x*u),(0,1,7):(1^u,1,u*(my^mr)),
                  (0,0,6):(1^x,0,1^(x*u)),(0,0,8):(1^u,1,0)}
        need(triple(records['qY'][5][0,0,7],lane)==(1,1,1),'native old local not blank')
        for pos,value in expected.items():
            need(triple(records['qY'][6][pos],lane)==value,'mask-bearing native incoming formula')
    need(comparisons==768 and incoming_comparisons==384,'complete published comparison counts')
    triples=tuple(product((0,1),repeat=3))
    permutations=[]
    for row in product((0,1),repeat=5):
        values=[triple(outputs['qY'],index(row+(g,))) for g in triples]
        need(len(set(values))==8,'G-to-q8 permutation')
        permutations.append(values)
    route={str(u):[] for u in (0,1)}
    socket={str(u):[] for u in (0,1)}
    for u,g in product((0,1),triples):
        if all(triple(outputs['qY'],index((x,u,my,mr,x^u,g)))==(0,x^u,0)
               for x,my,mr in product((0,1),repeat=3)):
            route[str(u)].append(g)
        if all(triple(outputs['q7'],index((x,u,my,mr,p,g)))==(0,p,0)
               for x,my,mr,p in product((0,1),repeat=4)):
            socket[str(u)].append(g)
    common={}
    for site in ('qY','q7'):
        candidates=[]
        for g0,g1 in product(triples,repeat=2):
            codes={0:set(),1:set()}
            for x,u,my,mr,p in product((0,1),repeat=5):
                if site=='qY' and p!=x^u:
                    continue
                codes[p].add(triple(outputs[site],index((x,u,my,mr,p,(g0,g1)[u]))))
            if len(codes[0])==len(codes[1])==1 and codes[0]!=codes[1]:
                candidates.append({'G0':g0,'G1':g1,'codes':[next(iter(codes[p])) for p in (0,1)]})
        common[site]=candidates
    # Derive incoming deltas from the full tripole; verify the full p7 formula.
    formula_rows=0
    for x,u,my,mr,p,g in product((0,1),(0,1),(0,1),(0,1),(0,1),triples):
        gcode=g[0]+2*g[1]+4*g[2]
        delta=xx(triple(states[244][16,0,0],u+2*gcode),triple(states[244][16,0,0],u))
        a,b,c=delta
        expected=(x^b,1^x^u^(x*u)^p^c,
                  x^u^(x*u)^(p*(1^x^u))^a^(b*(x^u^(x*u)^p))^(c*(x^1^u))^(b*c))
        lane=index((x,u,my,mr,p,g))
        need(triple(outputs['q7'],lane)==expected,'full p7-input expression')
        need(triple(records['q7'][6][0,0,8],lane)==(1^u,1,0),'q8 actual old local term')
        formula_rows+=1
        if p==x^u:
            native=triple(outputs['qY'],lane)
            need(native[0]==x^b and native[1]==1^(x*u)^c,'native obstruction coordinates')
    measured={'native_route_G_by_u':route,'q7_socket_G_by_u':socket,'common_two_code_G_pairs':common}
    need(json.loads(json.dumps(measured))==retained['measurements'],'all measured candidate sets match author')
    verdict={'q8_from_q7_only':'underdetermined' if len(permutations)==32 else 'not_established',
             'specified_native_route':'exists' if all(route.values()) else 'excluded_in_family',
             'specified_q7_socket':'exists' if all(socket.values()) else 'excluded_in_family',
             'common_native_two_code':'exists' if common['qY'] else 'excluded_in_family',
             'common_q7_two_code_socket':'exists' if common['q7'] else 'excluded_in_family',
             'native_reset':'not_constructed','joint_history':'not_certified'}
    result={'schema':'oi.review-native-reset.v1','author_input_hashes':hashes,
            'controls':{'signed_strip_coordinates':len(KEYS),'direct_scalar_comparisons':direct_count,
                        'prior_independent_QC_projection_values':projection_count,'actual_period_divisibility':True,
                        'published_q8_triples':comparisons,'published_q7_incoming_triples':incoming_comparisons,
                        'q7_old_and_endpoint_rows':64,'native_mask_bearing_interfaces':16,
                        'G_output_permutations':32,'q7_formula_rows':formula_rows,
                        'source_pairs_per_encoding_test':64,'geometry':geom},
            'measurements':measured,'verdict':verdict}
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__=='__main__':
    main()
