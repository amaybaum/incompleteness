"""Native two-front operand route; adapted credited signed-strip native evaluator."""
import argparse
from collections import Counter
from functools import lru_cache
from itertools import product
from pathlib import Path
import hashlib
import json


T = 185
P = 12*840**185
S = P+T
R = S+68
L = R+9
BASE = T+68
BUDGET = 20
ZERO = (0, 0, 0)
TR = tuple(product((0, 1), repeat=3))
UR = tuple((u, a, b, n) for u, a, b in product((0, 1), repeat=3) for n in range(8))
ROWS = tuple((x, u, my, mr, a, b, e, n)
             for x, u, my, mr, a, b in product((0, 1), repeat=6)
             for e, n in product(range(8), repeat=2))
UF = (1 << len(UR))-1
FULL = (1 << len(ROWS))-1
UINDEX = {r: i for i, r in enumerate(UR)}
RINDEX = {r: i for i, r in enumerate(ROWS)}
XM, UM, MY, MR = tuple(sum(r[j] << i for i, r in enumerate(ROWS)) for j in range(4))


def need(ok, label):
    if not ok:
        raise RuntimeError(label)


def xx(*qs):
    a = b = d = 0
    for q in qs:
        a ^= q[0]
        b ^= q[1]
        d ^= q[2]
    return a, b, d


def h(q):
    a, b, d = q
    return b, d, a ^ (b & d)


def hp(q, n):
    for _ in range(n % 12):
        q = h(q)
    return q


def lane(q, i):
    return tuple((w >> i) & 1 for w in q)


def code(q):
    return 4*q[0]+2*q[1]+q[2]


def dist(p, q):
    return sum(abs(x-y) for x, y in zip(p, q))


def ball(radius, center):
    for a in range(-radius, radius+1):
        for b in range(-radius+abs(a), radius-abs(a)+1):
            for d in range(-radius+abs(a)+abs(b), radius-abs(a)-abs(b)+1):
                yield center[0]+a, center[1]+b, center[2]+d


def odd(parts):
    total = 0
    for value in parts:
        if total & value:
            return False
        total |= value
    return True


def pack(function):
    return tuple(sum(function(*r)[j] << i for i, r in enumerate(UR)) for j in range(3))


SOURCES = {
    (0, 0, 0): pack(lambda u, a, b, n: (u, 0, 1)),
    (0, 0, -14): pack(lambda u, a, b, n: (u, 0, u)),
    (0, 0, -16): pack(lambda u, a, b, n: (u, 1 ^ u, 1)),
    (0, 0, -18): pack(lambda u, a, b, n: (u ^ b, a, u ^ a)),
    (1, 0, -17): pack(lambda u, a, b, n: (a ^ b, 0, a ^ b)),
    (-1, 0, -17): pack(lambda u, a, b, n: (a ^ b, a ^ b, a ^ b)),
    (0, 0, -20): pack(lambda u, a, b, n: TR[n]),
}


@lru_cache(None)
def direct_upper(t, x, y, z):
    if t < 0 or (t-x-y-z) % 2:
        return ZERO
    if min(abs(x-a)+abs(y-b)+abs(z-c) for a, b, c in SOURCES) > t:
        return ZERO
    if t == 0:
        return SOURCES.get((x, y, z), ZERO)
    ns = [direct_upper(t-1, x-1, y, z), direct_upper(t-1, x+1, y, z),
          direct_upper(t-1, x, abs(y-1), z), direct_upper(t-1, x, y+1, z),
          direct_upper(t-1, x, y, z-1), direct_upper(t-1, x, y, z+1)]
    return xx(direct_upper(t-2, x, y, z), h(xx(*ns)))


@lru_cache(None)
def upper_strip():
    values = {}

    def get(ell, x, y, n):
        y = abs(y)
        if ell < 0 or abs(x)+y > ell or (ell-abs(x)-y) % 2 or ell+abs(x)+y > BUDGET:
            return ZERO
        return values[ell, x, y][n]

    for ell in range(BUDGET+1):
        for x in range(-ell, ell+1):
            for y in range(ell-abs(x)+1):
                if (ell-abs(x)-y) % 2 or ell+abs(x)+y > BUDGET:
                    continue
                arr = [direct_upper(ell, x, y, 0)]
                values[ell, x, y] = arr
                for n in range(1, BASE+(BUDGET-ell)//2+1):
                    transverse = xx(*(get(ell-1, x+dx, y+dy, n)
                                      for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1))))
                    arr.append(xx(get(ell-2, x, y, n),
                                  h(xx(arr[n-1], get(ell-2, x, y, n+1), transverse))))
    return values


@lru_cache(None)
def expand_upper(q):
    return tuple(sum(((w >> UINDEX[u, a, b, n]) & 1) << i
                     for i, (x, u, my, mr, a, b, e, n) in enumerate(ROWS)) for w in q)


@lru_cache(None)
def upper(t, pos):
    x, y, n = pos[0], abs(pos[1]), R-pos[2]
    ell = t-n
    if ell < 0 or abs(x)+y > ell or (ell-abs(x)-y) % 2:
        return ZERO
    need(ell+abs(x)+y <= BUDGET, 'signed upper strip coverage')
    return expand_upper(upper_strip()[ell, x, y][n-P])


LOWER_ROWS = tuple(product((0,1),range(8)))
LOWER_FULL = (1 << len(LOWER_ROWS))-1
LOWER_O = tuple(sum((0,x,0)[j] << i for i,(x,e) in enumerate(LOWER_ROWS)) for j in range(3))
LOWER_W = (LOWER_FULL,)*3
LOWER_E = tuple(sum(TR[e][j] << i for i,(x,e) in enumerate(LOWER_ROWS)) for j in range(3))


def front_initial(gap_w=76, gap_e=78):
    # All initial sources lie on t=y+z=0. No superposition is used.
    row = {0: LOWER_O, gap_w: LOWER_W, gap_e: LOWER_E}
    initial = {}
    for t in range(gap_e+1):
        if t in (gap_w,gap_w+1,gap_e):
            initial[t] = row.get(t,ZERO)
        row = {z:h(xx(row.get(z,ZERO),row.get(z-1,ZERO)))
               for z in range(gap_e+1)}
    return tuple(initial[z] for z in (gap_w,gap_w+1,gap_e))


@lru_cache(None)
def lower_levels(j):
    levels = list(front_initial())
    for k in range(1,j+1):
        forcing = hp(LOWER_O,k+75) if not(k & 75) else ZERO
        levels[0] = h(xx(levels[0],forcing))
        for ell in (1,2):
            levels[ell] = h(xx(levels[ell],levels[ell-1]))
    return tuple(levels)


@lru_cache(None)
def direct_lower(t,x,y,z):
    if t < 0 or (t-x-y-z)%2:
        return ZERO
    if min(abs(x)+abs(y)+abs(z), abs(x)+abs(y+76)+abs(z-76),
           abs(x)+abs(y+78)+abs(z-78)) > t:
        return ZERO
    if t == 0:
        return {(0,0,0):LOWER_O,(0,-76,76):LOWER_W,(0,-78,78):LOWER_E}.get((x,y,z),ZERO)
    ns = [direct_lower(t-1,abs(x-1),y,z),direct_lower(t-1,x+1,y,z),
          direct_lower(t-1,x,y-1,z),direct_lower(t-1,x,y+1,z),
          direct_lower(t-1,x,y,z-1),direct_lower(t-1,x,y,z+1)]
    return xx(direct_lower(t-2,x,y,z),h(xx(*ns)))


def expand_lower(q):
    return tuple(sum(((w >> (8*x+e))&1) << i
                     for i,(x,u,my,mr,a,b,e,n) in enumerate(ROWS)) for w in q)


CONTROLS = [((0, -S, -68), XM), ((0, S, -68), MY ^ MR),
            ((T, P, -68), MY), ((-T, P, -68), MR)]
ENTRIES = {(0, -9, 8): (176, 0), (0, -10, 9): (175, 1), (0, -11, 10): (174, 2)}


def base(t, pos):
    out = upper(t, pos)
    for source, bits in CONTROLS:
        ds = tuple(abs(x-y) for x, y in zip(source, pos))
        if sum(ds) <= t:
            need(sum(ds) == t, 'pre-R lower only at first front')
            if odd(ds):
                out = xx(out, hp((0, bits, 0), t))
    if t == R-1 and pos in ENTRIES:
        j, ell = ENTRIES[pos]
        expected = hp((0, XM, 0), t) if odd((0, S+pos[1], 68+pos[2])) else ZERO
        need(out == expected, 'entry has only isolated original-origin background')
        out = expand_lower(lower_levels(j)[ell])
    return out


def native_compute():
    end = (0, 0, 10)
    old = {pos: base(R-2, pos) for pos in ball(10, end)}
    now = {pos: base(R-1, pos) for pos in ball(11, end)}
    records = {}
    for tau in range(11):
        nxt = {}
        for pos in ball(10-tau, end):
            neighbors = [now[tuple(pos[j]+(sign if j == axis else 0) for j in range(3))]
                         for axis in range(3) for sign in (-1, 1)]
            nxt[pos] = xx(old[pos], h(xx(*neighbors)))
        records[tau] = nxt
        if tau == 0:
            need(nxt[0, 0, 0] == (XM, FULL, XM ^ UM), 'original qY preserved')
        if tau == 7:
            need(nxt[0, 0, 7] == (0, 0, XM ^ UM), 'q7 preserved')
        if tau == 8:
            need(nxt[0, 0, 8] == (0, XM ^ UM, 0), 'q8 preserved')
        old, now = now, nxt
    return now[end], records



def geometry(root):
    target=(0,S,78)
    epos=(0,-78,78)
    npos=(0,S,S+156)
    deadline=L+1
    need(dist(epos,target)==deadline and dist(npos,target)==deadline,'two native first arrivals')
    need(dist(epos,(0,S,77))==L+2,'E does not reach old q9 by L')
    need(dist(epos,(0,S,76))==L+3,'E does not reach earlier q8')
    inventory=json.loads((root/'parallel_v3/history_control/SOURCE-GEOMETRY.json').read_text())['sources']
    need(len(inventory)==1479,'inherited source inventory')
    need(all(dist(tuple(v['position']),target)>=deadline for v in inventory),'q10 ready cone preserves sources')
    need(all(tuple(v['position']) not in (epos,npos) for v in inventory),'new sources overwrite no old source')
    ports=[(0,T,0),(0,0,-8*T),(T,P,0),(-T,P,0),(4*T,P,0),(0,S,0),(12*R,0,0),(48*L,0,0)]
    deadlines=[T,T,S,S,S,S,R,L]
    ready=list(zip(ports,deadlines))
    ready += [((T,0,0),T),((-T,0,0),T),((4*T,0,0),T),((0,S,-68),R),((-12*R,0,0),R)]
    ready += [((0,S,68+k),R+k) for k in range(10)]
    ready += [((-48*L,0,0),L)]
    for source in (epos,npos):
        need(all(dist(source,c)>r for c,r in ready),'new source avoids old ready pins')
        need(all(dist(source,c)>r for c,r in zip(ports,deadlines)),'all informative records preserved at own deadlines')
    directions=[(0,-1,0),(0,0,-1),(0,1,0),(0,1,0),(0,1,0),(0,1,0),(-1,0,0),(1,0,0)]
    bank_cases=0
    for port,d,start in zip(ports,directions,deadlines):
        axis=next(i for i in range(3) if d[i])
        times={start+1,deadline}
        zero=(target[axis]-port[axis])*d[axis]
        if start+1<=zero<=deadline: times.add(zero)
        for t in times:
            bank=tuple(v+t*w for v,w in zip(port,d))
            need(dist(bank,target)>deadline and bank not in(epos,npos),'old banks not overwritten or pinned')
            bank_cases+=1
        for source in(epos,npos):
            potential=(source[axis]-port[axis])*d[axis]
            if start+1<=potential<=deadline:
                bank=tuple(v+potential*w for v,w in zip(port,d))
                need(bank!=source,'new source not on entire old bank ray')
    entries=[]
    for time,radius in((R-2,10),(R-1,11)):
        for pos in ball(radius,(0,0,10)):
            absolute=(pos[0],S+pos[1],68+pos[2])
            if dist(epos,absolute)<=time:
                entries.append([time-R,list(pos),dist(epos,absolute)-time])
    need(entries==[[-1,[0,-11,10],0]],'E enters exactly final coupled lower level')
    return {'source_inventory_rows':len(inventory),'earlier_ready_exclusions':2*len(ready),
            'informative_record_deadline_exclusions':2*len(ports),'bank_breakpoint_cases':bank_cases,
            'new_E_lower_entry':entries,'F10_uniform_factor_replaced':True,
            'late_noise_background_pointwise_equal':'not claimed; conditional chronological bank theorem retained'}


CONTEXTS=tuple(k for k in product((0,1),repeat=5) if(k[3],k[4])!=(0,1))
FEATURES=tuple(1+sum(v<<(j+1) for j,v in enumerate(k)) for k in CONTEXTS)
AFFINE_VALUES=tuple(tuple((c&f).bit_count()%2 for f in FEATURES) for c in range(64))
ALL_COEFF=(1<<64)-1
ONE_COEFF=tuple(sum(AFFINE_VALUES[c][j]<<c for c in range(64)) for j in range(len(CONTEXTS)))


def affine_E_candidates(allowed):
    # Every one of the 64^3 coefficient triples is represented; bit-set
    # filtering eliminates impossible D coefficients without enumerating them.
    for ca in range(64):
        av=AFFINE_VALUES[ca]
        for cb in range(64):
            bv=AFFINE_VALUES[cb]
            possible=ALL_COEFF
            for j in range(len(CONTEXTS)):
                base=4*av[j]+2*bv[j]
                zero=bool(allowed[j]&(1<<base))
                one=bool(allowed[j]&(1<<(base+1)))
                if not zero and not one:
                    possible=0;break
                if not zero: possible &= ONE_COEFF[j]
                elif not one: possible &= ALL_COEFF ^ ONE_COEFF[j]
                if not possible: break
            while possible:
                bit=possible&-possible
                cd=bit.bit_length()-1
                yield ca,cb,cd
                possible ^= bit


def source_coefficients(ca,cb,cd):
    return tuple(sum(((c>>i)&1)<<(2-j) for j,c in enumerate((ca,cb,cd))) for i in range(6))


def evaluate_affine(coeff,k):
    v=coeff[0]
    for bit,c in zip(k,coeff[1:]):
        if bit:v ^= c
    return v


def fit_affine(values):
    solutions=[]
    for field in range(3):
        pivots={}
        for feature,value in zip(FEATURES,values):
            mask=feature;rhs=(value>>(2-field))&1
            while mask:
                pivot=mask.bit_length()-1
                if pivot in pivots:
                    old,oldrhs=pivots[pivot];mask^=old;rhs^=oldrhs
                else:
                    pivots[pivot]=(mask,rhs);break
            if not mask and rhs:return None
        out=0
        for pivot in sorted(pivots):
            mask,rhs=pivots[pivot]
            if rhs^((mask&out).bit_count()%2):out|=1<<pivot
        solutions.append(out)
    coeff=source_coefficients(*solutions)
    need(all(evaluate_affine(coeff,k)==v for k,v in zip(CONTEXTS,values)),'fitted affine source')
    return coeff



def affine_inconsistency(values):
    # A dependent set of affine feature rows must XOR to zero in every
    # source field. Retain a short explicit violating relation.
    for field in range(3):
        pivots={}
        for index,(feature,value) in enumerate(zip(FEATURES,values)):
            mask=feature;rhs=(value>>(2-field))&1;relation=1<<index
            while mask:
                pivot=mask.bit_length()-1
                if pivot in pivots:
                    old,oldrhs,oldrel=pivots[pivot]
                    mask^=old;rhs^=oldrhs;relation^=oldrel
                else:
                    pivots[pivot]=(mask,rhs,relation);break
            if not mask and rhs:
                indices=[j for j in range(len(CONTEXTS)) if(relation>>j)&1]
                feature_xor=0;source_xor=0
                for j in indices:feature_xor^=FEATURES[j];source_xor^=values[j]
                need(feature_xor==0 and((source_xor>>(2-field))&1),'explicit affine rejection relation')
                return {'N_field':['A','B','D'][field],
                        'contexts_u_mY_mR_a_b':[list(CONTEXTS[j]) for j in indices],
                        'required_N_codes':[values[j] for j in indices],
                        'feature_row_xor':feature_xor,'required_N_code_xor':source_xor}
    raise RuntimeError('missing affine inconsistency witness')

def kernel_value(out,s,k,e,n):
    u,my,mr,a,b=k
    return code(lane(out,RINDEX[s^u^a,u,my,mr,a,b,e,n]))


def controller_search(out):
    known = []
    pair_sets=[]
    intersections=[]
    common=None
    for k in CONTEXTS:
        lookup={}
        for e in range(8):
            for n in range(8):
                pair=tuple(kernel_value(out,s,k,e,n) for s in(0,1))
                if pair[0]!=pair[1]: lookup.setdefault(pair,[]).append((e,n))
        known.append(lookup)
        pair_sets.append(set(lookup))
        common=set(lookup) if common is None else common&set(lookup)
        intersections.append(len(common))
    # The credited old single-front limit remains a countercontrol at E=0.
    old_common=None
    for k in CONTEXTS:
        old_pairs={tuple(kernel_value(out,s,k,0,n) for s in(0,1)) for n in range(8)}
        old_pairs={p for p in old_pairs if p[0]!=p[1]}
        old_common=old_pairs if old_common is None else old_common&old_pairs
    need(not old_common,'old single-N exclusion retained')
    survivors=[]
    per_pair=[]
    for pair in sorted(common):
        allowed=[]; n_given=[]
        for lookup in known:
            ens=dict(lookup[pair])
            need(len(ens)==len(lookup[pair]),'own-N uniqueness for required first output')
            allowed.append(sum(1<<e for e in ens));n_given.append(ens)
        e_affine_count=0;both_count=0;witness=None;rejection=None
        for ca,cb,cd in affine_E_candidates(allowed):
            e_affine_count+=1
            ecoeff=source_coefficients(ca,cb,cd)
            evalues=[evaluate_affine(ecoeff,k) for k in CONTEXTS]
            nvalues=[n_given[j][e] for j,e in enumerate(evalues)]
            ncoeff=fit_affine(nvalues)
            if ncoeff is not None:
                both_count+=1
                item={'raw_pair_s0_s1':list(pair),'E_coeff_constant_u_mY_mR_a_b':list(ecoeff),
                      'N_coeff_constant_u_mY_mR_a_b':list(ncoeff)}
                for k,e,n in zip(CONTEXTS,evalues,nvalues):
                    need(tuple(kernel_value(out,s,k,e,n) for s in(0,1))==pair,'affine candidate complete native law')
                survivors.append(item)
                if witness is None:witness=item
            elif rejection is None:
                rejection={'E_coeff_constant_u_mY_mR_a_b':list(ecoeff),
                           'N_affine_inconsistency':affine_inconsistency(nvalues)}
        per_pair.append({'raw_pair':list(pair),'affine_E_maps_after_constraints':e_affine_count,
                         'joint_affine_E_N_maps':both_count,'first_witness':witness,
                         'first_N_rejection':rejection})
    fresh=[]
    groups={}
    for row in survivors:
        ec=row['E_coeff_constant_u_mY_mR_a_b'];nc=row['N_coeff_constant_u_mY_mR_a_b']
        key=tuple(ec[1:]+nc[1:])
        for other in groups.get(key,[]):
            pair0=other['raw_pair_s0_s1'];pair1=row['raw_pair_s0_s1']
            if pair0==pair1:continue
            eco=other['E_coeff_constant_u_mY_mR_a_b'];nco=other['N_coeff_constant_u_mY_mR_a_b']
            ec_delta=ec[0]^eco[0];nc_delta=nc[0]^nco[0]
            codes=[pair0[0],pair1[0],pair0[1],pair1[1]]
            witness={'c0_source':other,'c1_source':row,'fresh_c_E_coefficient':ec_delta,
                     'fresh_c_N_coefficient':nc_delta,'codes_s0c0_s0c1_s1c0_s1c1':codes,
                     'four_code_injective':len(set(codes))==4}
            # Keep one useful four-code witness, or the first nonvacuous c witness.
            if not fresh or(len(set(codes))==4 and not fresh[0]['four_code_injective']): fresh=[witness]
            if len(set(codes))==4:break
        groups.setdefault(key,[]).append(row)
    return {'accepted_context_count':len(CONTEXTS),'common_pair_intersection_sizes':intersections,
            'common_raw_pairs':sorted(common),'affine_E_coefficient_maps_represented_per_pair':64**3,
            'per_pair_affine_results':per_pair,'total_joint_affine_maps':len(survivors),
            'fresh_c_witnesses':fresh,'old_E0_common_pairs':sorted(old_common),
            'verdict':'affine native X operand exists' if survivors else
                      ('no common raw binary X code from affine E,N in this geometry' if common else
                       'no common raw X pair for any seed-only E/N in this geometry')}


def small_full_control():
    old={};now={(0,0,0):LOWER_O,(0,-2,2):LOWER_W,(0,-4,4):LOWER_E}
    front=dict(now)
    comparisons=0
    for t in range(1,9):
        sites=set(old)|set(now)
        for pos in now:
            sites.update(tuple(pos[j]+(sgn if j==axis else 0) for j in range(3))
                         for axis in range(3) for sgn in(-1,1))
        nxt={}
        for pos in sites:
            ns=[now.get(tuple(pos[j]+(sgn if j==axis else 0) for j in range(3)),ZERO)
                for axis in range(3) for sgn in(-1,1)]
            value=xx(old.get(pos,ZERO),h(xx(*ns)))
            if value!=ZERO:nxt[pos]=value
        # Independently advance only the oriented first-front dynamic program.
        fnext={}
        for z in range(5):
            y=t-z
            fnext[(0,y,z)]=h(xx(front.get((0,y-1,z),ZERO),front.get((0,y,z-1),ZERO)))
            need(nxt.get((0,y,z),ZERO)==fnext[(0,y,z)],'full3D/oriented-front control')
            comparisons+=len(LOWER_ROWS)
        old,now=now,nxt;front=fnext
    return comparisons


def main():
    ap=argparse.ArgumentParser()
    default=Path(__file__).resolve().parent.parent
    if not(default/'parallel_v3').exists():default=default/'checkpoint_v12'
    ap.add_argument('--source-root',type=Path,default=default)
    args=ap.parse_args();here=Path(__file__).resolve().parent
    prov=json.loads((here/'PROVENANCE.json').read_text())
    for rel,digest in prov['inputs'].items():
        need(hashlib.sha256((args.source_root/rel).read_bytes()).hexdigest()==digest,'source pin '+rel)
    need(P%(12*840**BUDGET)==0,'actual upper period')
    need(P%(384*840**3)==0,'actual lower period')
    upper_controls=0
    for (ell,x,y),arr in upper_strip().items():
        for n in range(3):
            need(arr[n]==direct_upper(n+ell,x,y,n),'upper full native direct control')
            upper_controls+=len(UR)
    lower_controls=0
    for j in(0,1,3):
        for ell in range(3):
            need(lower_levels(j)[ell]==direct_lower(j+76+ell,0,j,76+ell),'lower first front full3D recursion')
            lower_controls+=len(LOWER_ROWS)
    sm=small_full_control()
    g=geometry(args.source_root)
    out,records=native_compute()
    old_result=json.loads((args.source_root/'native_seed_v12/result.json').read_text())
    old_hex=old_result['q10_table_hex']
    e0=[];old_rows=0;changed=0;own_e=own_n=0
    prior=json.loads((args.source_root/'branch_v10/local-controller/symmetric-result.json').read_text())['q9_table_hex']
    for i,(x,u,my,mr,a,b,e,n) in enumerate(ROWS):
        prior_index=0
        for value,size in zip((x,u,my,mr,a,b,4,5,7),(2,2,2,2,2,2,8,8,8)):
            prior_index=size*prior_index+value
        need(lane(records[9][0,0,9],i)==TR[int(prior[prior_index],16)],'old q9 unchanged')
        old_rows+=1
        if not e:e0.append(format(code(lane(out,i)),'x'))
        changed += lane(out,i)!=lane(out,RINDEX[x,u,my,mr,a,b,0,n])
    need(''.join(e0)==old_hex,'all512 old E0 q10 rows reproduced')
    need(changed>0,'omitting new E changes actual native output')
    for context in product((0,1),repeat=6):
        for e in range(8):
            need(len({lane(out,RINDEX[*context,e,n]) for n in range(8)})==8,'own-N first-arrival permutation')
            own_n+=1
        for n in range(8):
            need(len({lane(out,RINDEX[*context,e,n]) for e in range(8)})==8,'own-E first-arrival permutation')
            own_e+=1
    # Independent finite affine-solver controls, outside the native response data.
    known=(9,23,50)
    allowed=[1<<(4*AFFINE_VALUES[known[0]][j]+2*AFFINE_VALUES[known[1]][j]+AFFINE_VALUES[known[2]][j])
             for j in range(len(CONTEXTS))]
    need(list(affine_E_candidates(allowed))==[known],'affine filter recovers unique prescribed map')
    malformed=list(allowed);malformed[0]=1<<((malformed[0].bit_length()-1)^1)
    need(not list(affine_E_candidates(malformed)),'affine filter rejects inconsistent constraint')
    fit=source_coefficients(37,12,55)
    need(fit_affine([evaluate_affine(fit,k) for k in CONTEXTS])==fit,'N affine fitting exact control')
    c=controller_search(out)
    table=''.join(format(code(lane(out,i)),'x') for i in range(len(ROWS)))
    result={'schema':'oi.native-two-front-operand.v13','source_revision':prov['source_revision'],
            'table_order':'x,u,mY,mR,a,b,Ecode,Ncode lexicographic; code=4A+2B+D',
            'q10_table_hex':table,'table_sha256':hashlib.sha256(table.encode()).hexdigest(),
            'checks':{'upper_direct_scalar_lanes':upper_controls,'lower_direct_scalar_rows':lower_controls,
                      'small_full3D_scalar_front_comparisons':sm,'q9_preserved_rows':old_rows,
                      'old_E0_q10_rows':len(e0),'own_E_permutation_contexts':own_e,
                      'own_N_permutation_contexts':own_n,'omitted_E_changed_rows':changed,
                      'affine_solver_controls':3,'geometry':g},
            'controller':c,'verdict':{'native_X_operand':c['verdict'],'physical_acceptance':'not constructed',
                      'full_instrument':'not constructed','access_rule':'not adopted','arbitrary_redundant_q10_decoder':'not tested',
                      'full_A1_A2_equivalence':'not established'}}
    print(json.dumps(result,sort_keys=True,separators=(',',':')))


if __name__=='__main__':main()
