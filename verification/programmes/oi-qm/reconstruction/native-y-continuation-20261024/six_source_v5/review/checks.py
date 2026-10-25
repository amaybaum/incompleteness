"""Independent actual-scale six-source endpoint audit (standard library only).

No author dynamics imports. Author lower slices and RESULT are comparison
targets only. Direct raw-coordinate two-source recursion, exact giant integer
selector parity, sparse shrinking-cone evolution, and signed upper strip.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import product
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
AUTHOR = HERE.parent if (HERE.parent / 'lower.cpp').exists() else HERE.parent / 'repo_checkpoint/payload/six_source_v5'
T = 185
P = 12 * 840**T
S = P + T
R = S + 68
N = R + 3
Z = (0, 0, 0)
HT = (0, 4, 1, 5, 2, 6, 7, 3)  # A is bit zero, D bit two.
E = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))


def need(condition, description):
    if not condition:
        raise RuntimeError(description)


def norm(v):
    return sum(map(abs, v))


def add(v, w):
    return (v[0]+w[0], v[1]+w[1], v[2]+w[2])


def xx(*values):
    a = b = d = 0
    for x, y, z in values:
        a ^= x
        b ^= y
        d ^= z
    return a, b, d


def hh(v):
    return v[1], v[2], v[0] ^ (v[1] & v[2])


def variable(i, lanes):
    return sum(((j >> i) & 1) << j for j in range(lanes))


def ball(radius, center=(0,0,0)):
    for a in range(-radius, radius+1):
        for b in range(-radius+abs(a), radius-abs(a)+1):
            for c in range(-radius+abs(a)+abs(b), radius-abs(a)-abs(b)+1):
                yield add((a,b,c), center)


def odd(parts):
    occupied = 0
    for part in parts:
        if occupied & part:
            return False
        occupied |= part
    return True


def hp(q, t):
    for _ in range(t % 12):
        q = HT[q]
    return q


def direct(sources, packed=False):
    zero = Z if packed else 0
    @lru_cache(None)
    def at(t, v):
        if t < 0 or (t - sum(v)) % 2 or all(norm(tuple(a-b for a,b in zip(v,q))) > t for q in sources):
            return zero
        if t == 0:
            return sources.get(v, zero)
        if packed:
            return xx(at(t-2,v), hh(xx(*(at(t-1,add(v,e)) for e in E))))
        total = 0
        for e in E:
            total ^= at(t-1, add(v,e))
        return at(t-2,v) ^ HT[total]
    return at


# Signed transverse coordinates; unlike author code there is no reflection
# quotient or recursive call to advance a truncated radial strip.
def strip_keys(budget):
    return tuple((ell,a,b) for ell in range(budget+1)
                 for a in range(-budget,budget+1)
                 for b in range(-budget,budget+1)
                 if abs(a)+abs(b) <= ell and ell+abs(a)+abs(b) <= budget
                 and (ell-a-b) % 2 == 0)


def strip_step(old, budget):
    look = [{} for _ in range(budget//2+2)]
    for ell in range(budget+1):
        for jump in range((budget-ell)//2+1):
            for layer,a,b in old:
                if layer != ell or ell+abs(a)+abs(b) > budget-2*jump:
                    continue
                prior = old[ell,a,b] if jump == 0 else look[jump-1][ell,a,b]
                inside = prior ^ look[jump+1].get((ell-2,a,b),0)
                for aa,bb in ((a-1,b),(a+1,b),(a,b-1),(a,b+1)):
                    inside ^= look[jump].get((ell-1,aa,bb),0)
                look[jump][ell,a,b] = look[jump].get((ell-2,a,b),0) ^ HT[inside]
    return look[0]


def check_period_and_geometry():
    need(all(hp(q,12)==q for q in range(8)), 'H exponent')
    need(P % (12*840**144) == 0, 'giant delay divides strip exponent')
    # General triangle diagonal maps are all permutations on the eight triples.
    need(all(len({a ^ HT[z ^ b] for z in range(8)})==8 for a,b in product(range(8),repeat=2)), 'diagonal bijections')
    need(all(840 % k == 0 for k in range(1,9)), 'all possible permutation cycle lengths')
    # Independent signed recurrence tested against the actual interacting dipole.
    count = 0
    keys = strip_keys(6)
    for x,m in product(range(2),range(8)):
        at = direct({(0,0,0):2*x, (0,-2,0):m})
        state = {key:at(key[0], (key[1],0,key[2])) for key in keys}
        for n in range(9):
            for (ell,a,b),value in state.items():
                need(value == at(n+ell,(a,n,b)), 'signed interacting strip')
                count += 1
            state = strip_step(state,6)
    controls = ((0,2*S,0),(T,P+S,0),(-T,P+S,0))
    upper = (0,S,S+136)
    for loc in ((0,0,0),)+controls:
        need(norm(tuple(a-b for a,b in zip(upper,loc)))==2*R, 'upper lower separation')
    need(norm(tuple(a-b for a,b in zip(upper,(0,-2,0))))==2*R+2, 'upper M2 separation')
    for loc in controls:
        need(norm(loc)==2*S and norm(add(loc,(0,2,0)))==2*S+2, 'selector dipole separation')
    print('V1: signed dipole strip agrees at %d native values; triangular bijections, universal exponent divisibility, source separations: PASS' % count)


def lower_evolution():
    v = [variable(i,64) for i in range(6)]
    # Raw signed positions: this deliberately avoids the C++ reflected cache.
    cluster = direct({(0,0,0):(0,v[0],0), (0,-2,0):tuple(v[1:4])}, packed=True)
    controls = (((0,2*S,0),v[4]^v[5]), ((T,P+S,0),v[4]), ((-T,P+S,0),v[5]))
    slices = []
    geometry = []
    boundary_count = 0
    for c,radius in ((-2,71),(-1,72)):
        sparse = {}
        count = maxweight = 0
        minaxial = T
        for local in ball(radius):
            a,dy,dz = local
            j,z = dy-1,70+dz
            ell = c-j
            value = Z
            if ell >= abs(a)+abs(z) and (ell-a-z)%2 == 0:
                count += 1
                weight = ell+abs(a)+abs(z)
                maxweight = max(maxweight,weight)
                minaxial = min(minaxial,T+j)
                need(weight <= 144 and T+j>0 and ell-abs(a)-abs(z) in (0,2), 'physical strip budget')
                value = cluster(T+c,(a,T+j,z))
            position = (a,S+j,z)
            for source,bit in controls:
                disp = tuple(abs(p-q) for p,q in zip(position,source))
                need(sum(disp)>=S+c, 'selector ahead or exactly on first arrival')
                if sum(disp)==S+c:
                    boundary_count += 1
                    # No low-bit truncation here: actual 1800+-bit displacement.
                    if odd(disp):
                        field = hp(2,S+c)
                        value = xx(value,tuple(bit if field>>i&1 else 0 for i in range(3)))
            if value != Z:
                sparse[local] = value
        geometry.append([c,count,maxweight,minaxial])
        slices.append(sparse)
    need(geometry == [[-2,71,140,113],[-1,286,142,112]], 'exact slice inventory')
    need(boundary_count==5467, 'selector boundary count')
    old,now = slices
    supports = [len(old),len(now)]
    # Candidate set is old support union neighbors of present support. Every
    # other point has zero old value and zero neighbor sum, hence remains zero.
    for tick in range(68):
        radius = 71-tick
        sums = {}
        for p,value in now.items():
            for e in E:
                q = add(p,e)
                if norm(q) <= radius:
                    sums[q] = xx(sums.get(q,Z),value)
        nxt = {p:value for p,value in old.items() if norm(p)<=radius}
        for p,total in sums.items():
            value = xx(nxt.get(p,Z),hh(total))
            if value == Z:
                nxt.pop(p,None)
            else:
                nxt[p] = value
        old,now = now,nxt
        supports.append(len(now))
    # The author retains a smaller old slice (radius3 instead of available5).
    computed = {}
    for tau,grid,radius in ((-2,old,3),(-1,now,4)):
        for a,b,c in ball(radius):
            computed[tau,(a,b-1,c+2)] = grid.get((a,b,c),Z)
    expected = {(tau,tuple(p)):tuple(int(word,16) for word in val)
                for tau,p,val in json.loads((AUTHOR/'lower-slices.json').read_text())}
    need(computed==expected, 'independent actual-scale lower slices')
    print('V2: exact giant-integer controls (%d boundary terms), strip budgets %s; raw-coordinate dipole cache %d entries; 68 sparse updates (peak support %d) reproduce all192x64 lower triples: PASS' % (boundary_count,geometry,cluster.cache_info().currsize,max(supports)))
    return computed,supports


@lru_cache(None)
def upper_orbit(q):
    at = direct({(0,0,0):q})
    first = {key:at(key[0],(key[1],key[2],0)) for key in strip_keys(6)}
    state = first
    states = []
    while not states or state != first:
        need(len(states)<10001, 'upper orbit bound')
        states.append(state)
        state = strip_step(state,6)
    # Direct small-time control covers all signed entries of the same map.
    for n in range(9):
        for (ell,a,b),value in states[n].items():
            need(value==at(n+ell,(a,b,n)), 'upper signed direct control')
    return states


def upper(t,p,u):
    a,b = p[0],p[1]
    n = R-p[2]
    ell = t-n
    if ell<abs(a)+abs(b) or (ell-a-b)%2:
        return 0
    need((ell,a,b) in strip_keys(6), 'upper budget six')
    orbit = upper_orbit(4+u)
    return orbit[n%len(orbit)][ell,a,b]


def native_update(old,now,radius,center):
    return {p:xx(old[p],hh(xx(*(now[add(p,e)] for e in E))))
            for p in ball(radius,center)}


def final_assembly(lower):
    vv = [variable(i,256) for i in range(8)]
    ones = (1<<256)-1
    def upvalue(t,p):
        a,b = upper(t,p,0),upper(t,p,1)
        return tuple((ones if a>>i&1 else 0) ^ (vv[6] if (a^b)>>i&1 else 0) for i in range(3))
    pre = {-2:{},-1:{}}
    for (tau,p),value in lower.items():
        replicated = tuple(sum(word << offset for offset in (0,64,128,192)) for word in value)
        pre[tau][p] = xx(replicated,upvalue(R+tau,p))
    old,now = pre[-2],pre[-1]
    records = []
    for tick in range(4):
        nxt = native_update(old,now,3-tick,(0,-1,2))
        if tick==0:
            need(nxt[0,0,0]==(vv[0],ones,vv[0]^vv[6]), 'qY native triple')
            nxt[0,0,0]=(vv[0],ones,vv[7])
        records.append(nxt)
        old,now=now,nxt
    need(records[1][0,-1,2]==(0,ones^vv[0]^vv[6],vv[0]), 'native history sidecar')
    need(records[2][0,0,2][0]==vv[7], 'q2 raw operand positive control')
    # Separate baseline q2 cone. Here the old lower origin and controls are all
    # first-front pulses, and M2 is outside. No prepared lower data is reused.
    original = (((0,-S,-68),vv[0]), ((0,S,-68),vv[4]^vv[5]),
                ((T,P,-68),vv[4]), ((-T,P,-68),vv[5]))
    def baseline(t,p):
        value=upvalue(t,p)
        for source,bit in original:
            disp=tuple(abs(a-b) for a,b in zip(p,source))
            need(sum(disp)>=t,'q2 lower first fronts')
            if sum(disp)==t and odd(disp):
                field=hp(2,t)
                value=xx(value,tuple(bit if field>>i&1 else 0 for i in range(3)))
        return value
    old={p:baseline(R-2,p) for p in ball(2,(0,0,2))}
    now={p:baseline(R-1,p) for p in ball(3,(0,0,2))}
    for tick in range(3):
        nxt=native_update(old,now,2-tick,(0,0,2))
        if tick==0:
            nxt[0,0,0]=(vv[0],ones,vv[7])
        old,now=now,nxt
    need(now[0,0,2]==records[2][0,0,2], 'complete q2 baseline triple')
    need([len(upper_orbit(4+u)) for u in (0,1)]==[3600,2940], 'independent upper periods')
    need(R%3600==R%2940==253, 'actual upper phases')
    print('V3: independent signed upper periods3600/2940, giant phases253; final four native updates preserve qY, sidecar and entire q2 triple in all256 diagnostic assignments: PASS')
    return records[-1][0,-1,2]


def classify(out):
    table=[sum(((word>>j)&1)<<(2-i) for i,word in enumerate(out)) for j in range(256)]
    expected=json.loads((AUTHOR/'RESULT.json').read_text())
    need(table==expected['diagnostic_table'], 'complete diagnostic truth table')
    anfs=[]
    for field in range(3):
        coeff=[(code>>(2-field))&1 for code in table]
        for i in range(8):
            for j in range(256):
                if j>>i&1:
                    coeff[j] ^= coeff[j^(1<<i)]
        anfs.append([j for j,c in enumerate(coeff) if c])
    need(anfs==expected['output_anf'], 'all Boolean polynomials')
    counts={}
    for x,u in product(range(2),repeat=2):
        row=Counter(table[j] for j in range(256) if j&1==x and j>>6&1==u and j>>7==x^u)
        counts[str(x)+str(u)]=[row[i] for i in range(8)]
        need(sum(row.values())==32, 'complete native background count')
    need(counts==expected['native_counts_per_32_by_xu'], 'all native marginal counts')
    errors=[Fraction(sum(min(a,b) for a,b in zip(counts[str(x)+'0'],counts[str(x)+'1'])),64) for x in (0,1)]
    need(errors==[Fraction(1,16),Fraction(9,32)], 'local equal-prior Bayes errors')
    for a,b in ((0,216),(129,87)):
        need(table[a]==table[b]==3 and a&1==b&1 and a>>7 != b>>7, 'native overlap witness')
        need(a>>7==((a&1)^(a>>6&1)) and b>>7==((b&1)^(b>>6&1)), 'native witness inputs')
    need(all(table[j]!=table[j+128] for j in range(128)), 'no fixed-background diagnostic erasure')
    p=variable(7,256)
    need(all(word not in (p,p^((1<<256)-1)) for word in out), 'no raw diagnostic field')
    print('V4: all256 output triples and ANFs,128 native assignments,4 marginal rows and native overlap witnesses agree; equal-prior local errors=%s; all128 p-pairs distinct: PASS' % [str(e) for e in errors])
    print('VERDICT: ACCEPT this six-source endpoint obstruction only. Full-history decoding, later processing, other preparations and native reset remain OPEN.')


if __name__=='__main__':
    # Bind exact inspected input bytes before doing any scientific computation.
    hashes=json.loads((HERE/'INPUT-HASHES.json').read_text())
    for relative,digest in hashes.items():
        need(sha256((AUTHOR/relative).read_bytes()).hexdigest()==digest, 'input digest: '+relative)
    print('INPUTS: %d exact author files match reviewed SHA256 digests.' % len(hashes))
    check_period_and_geometry()
    lower,supports=lower_evolution()
    classify(final_assembly(lower))
