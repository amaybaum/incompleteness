"""Independent v2 interface/local-stencil audit. No author imports, no I/O writes."""
from functools import lru_cache
from itertools import product
from collections import Counter


def need(ok, label):
    if not ok:
        raise RuntimeError(label)

# Scalar bit0=A, bit1=B, bit2=D. A literal permutation table avoids shared H code.
H = (0, 4, 1, 5, 2, 6, 7, 3)

def hp(v, n):
    for _ in range(n % 12):
        v = H[v]
    return v

for v in range(8):
    need(hp(v, 12) == v, 'H order')

@lru_cache(None)
def sequence(q):
    # Independently evaluated named near-front quantities, phase retained.
    state = (0, q, H[q], hp(q, 2), H[q] ^ H[q ^ hp(q, 2)], q)
    out = []
    while state not in out:
        out.append(state)
        n, f, z, ell, j, g = state
        n += 1
        nf = hp(q, n) ^ H[f ^ hp(q, n + 1)]
        nz = H[z ^ hp(q, n)]
        nl = H[ell ^ nz]
        nj = nz ^ H[j ^ H[nz ^ hp(q, n + 1)] ^ nf ^ nl]
        ng = nf ^ H[g ^ (hp(q, n + 1) ^ H[nf ^ hp(q, n + 2)])]
        state = (n % 12, nf, nz, nl, nj, ng)
        need(len(out) < 500001, 'bounded orbit')
    need(state == out[0], 'no transient')
    return out

def upper(q, t, v):
    a, b = sorted((abs(v[0]), abs(v[1])), reverse=True)
    n = abs(v[2])
    lag = t - a - b - n
    if lag < 0 or lag % 2:
        return 0
    orbit = sequence(q)
    _, f, z, ell, j, g = orbit[n % len(orbit)]
    mapping = {(0,0,0):hp(q,n), (1,0,0):z, (2,0,0):ell,
               (1,1,0):0, (0,0,2):f, (1,0,2):j, (0,0,4):g}
    need((a,b,lag) in mapping, 'covered lag')
    return mapping[a,b,lag]

steps = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
def add(a,b):
    return tuple(x+y for x,y in zip(a,b))
def norm(v):
    return sum(map(abs,v))
def distance(a,b):
    return sum(abs(x-y) for x,y in zip(a,b))
def sphere(r, centre=(0,0,2)):
    return [add(v,centre) for v in product(range(-r,r+1),repeat=3) if norm(v)<=r]

comparisons=0
for q in range(8):
    @lru_cache(None)
    def direct(t,v):
        if t<0 or norm(v)>t:return 0
        if t==0:return q if v==(0,0,0) else 0
        s=0
        for e in steps:s ^= direct(t-1,add(v,e))
        return direct(t-2,v)^H[s]
    for n in range(10):
        for a,b,lag in ((0,0,0),(1,0,0),(2,0,0),(1,1,0),(0,0,2),(1,0,2),(0,0,4)):
            need(upper(q,n+a+b+lag,(a,b,n))==direct(n+a+b+lag,(a,b,n)), 'direct 3D near-front')
            comparisons+=1
print('R1: 560 independent direct-native comparisons across all pulse triples: PASS')

T=185; P=12*840**T; S=T+P; R=S+68
need(len(sequence(4))==720 and len(sequence(5))==84, 'actual periods')
need((R%720,R%84)==(253,1), 'actual phases')
print('R2: independent actual-pulse orbit periods720/84 and large-integer phases: PASS')

# Boolean polynomials, monomials as frozensets of names, coefficient arithmetic F2.
ZERO=frozenset(); ONE=frozenset([frozenset()])
def variable(name):return frozenset([frozenset([name])])
def xor(*polys):
    out=set()
    for p in polys:out.symmetric_difference_update(p)
    return frozenset(out)
def mul(a,b):
    counts=Counter(ma|mb for ma in a for mb in b)
    return frozenset(m for m,c in counts.items() if c%2)
def constant(b):return ONE if b else ZERO
def ph(v):return v[1],v[2],xor(v[0],mul(v[1],v[2]))
def px(*vs):return tuple(xor(*(v[j] for v in vs)) for j in range(3))
def parity(parts):
    # Factorial valuation of multinomial, rather than bit-intersection code.
    return sum(p.bit_count() for p in parts)==sum(parts).bit_count()
x,u,my,mr=map(variable, ('x','u','mY','mR'))
y=xor(x,u)
ctrls={(a,b,z):variable('c_%d_%d_%d'%(a,b,z)) for z,r in ((1,2),(2,3)) for a in range(-r,r+1) for b in range(-r,r+1) if abs(a)+abs(b)==r}
need(len(ctrls)==20,'twenty geometric entries')
lower=[((0,-S,-68),x),((0,S,-68),xor(my,mr)),((T,P,-68),my),((-T,P,-68),mr)]
def base(t,v):
    z0=upper(4,t,(v[0],v[1],R-v[2])); z1=upper(5,t,(v[0],v[1],R-v[2]))
    result=[xor(constant((z0>>j)&1),u if ((z0^z1)>>j)&1 else ZERO) for j in range(3)]
    for loc,bit in lower:
        ds=tuple(abs(a-b) for a,b in zip(v,loc))
        need(sum(ds)>=t,'firstfront reduction')
        if sum(ds)==t and parity(ds):
            field=hp(2,t)
            for j in range(3):
                if (field>>j)&1:result[j]=xor(result[j],bit)
    if t==R-1 and v in ctrls:
        need(hp(2,t)==2,'actual incoming controls in B')
        result[1]=xor(result[1],ctrls[v])
    return tuple(result)
@lru_cache(None)
def evaluate(t,v):
    if t<=R-1:return base(t,v)
    return px(evaluate(t-2,v),ph(px(*(evaluate(t-1,add(v,e)) for e in steps))))
actual=evaluate(R+2,(0,0,2))
k=xor(*(ctrls[v] for v in ((0,2,1),(0,-2,1),(2,0,1),(-2,0,1))))
ell=xor(*(bit for (a,b,z),bit in ctrls.items() if z==2))
expected=(y,xor(y,mul(u,k),ell),xor(ONE,mul(x,y),mul(mul(u,xor(ONE,x)),k),mul(y,ell)))
need(actual==expected, 'full symbolic local-stencil formula')
# y=1 => u=1+x, substitute polynomial directly.
def substitute_u(poly):
    result=ZERO
    for monomial in poly:
        term=ONE
        for name in monomial:term=mul(term,xor(ONE,x) if name=='u' else variable(name))
        result=xor(result,term)
    return result
need(substitute_u(actual[0])==ONE and substitute_u(xor(actual[1],actual[2]))==x,'history invariant')
print('R3: independent memoized polynomial stencil derives full20-control formula and y=1 => A=1,B XOR D=x: PASS')

# Geometry: exhaustive modest radii audit the general triangle/geodesic argument.
geo=0
for r in range(3,25):
    for z in (1,2):
        radius=r+z
        for a in range(-radius,radius+1):
            for b in set((radius-abs(a),-(radius-abs(a)))):
                loc=(a,b,z)
                need(distance(loc,(0,0,2))==r+2,'boundary')
                need(norm(loc)==r+2*z,'qY protection')
                need(distance(loc,(0,0,r))==2*r,'upper separation')
                need(all(distance(loc,v)>r-2 for v in sphere(2)),'old slice unchanged')
                for v in sphere(3):
                    if distance(loc,v)<=r-1:
                        need(distance(loc,v)==r-1 and v in ctrls,'all new incoming support in20')
                geo+=1
print('R4: geometric support argument checked on %d entire plane-boundary source positions; symbolic triangle proof in report: PASS'%geo)

# All states, not only the reachable native domain.
def f(v):a,b,d,e=v;return e,a^b,a,1^d
def fi(v):a,b,d,e=v;return d,b^d,1^e,a
def g(v):x,a,b,d=v;return x,b^a,d^1^(x&a),a
def gi(v):x,a,b,d=v;return x,d,a^d,b^1^(x&d)
for fn,inv in ((f,fi),(g,gi)):
    domain=list(product((0,1),repeat=4))
    need(len({fn(v) for v in domain})==16,'permutation')
    need(all(inv(fn(v))==v for v in domain),'inverse')
for bx,by in product((0,1),repeat=2):
    need(f((by,by,1^(bx&by),0))==(0,0,by,bx&by),'native F')
    need(g((bx,by,by,1^(bx&by)))==(bx,0,0,by),'native G')
print('R5: both total interface permutations, inverses, native restriction and clean-workspace claim: PASS')
# Genuine limited-scope counterexample: varying x at y=1 cannot have identical full codes.
for bx,k0,l0 in product((0,1),repeat=3):
    bu=1^bx; B=1^(bu&k0)^l0; D=1^bx^(bu&(1^bx)&k0)^l0
    need(B^D==bx,'all reduced controls')
print('SCOPE: ACCEPT v2 local algebra and relaxed-plane obstruction; native integrated reset and wider transport proof remain OPEN.')
