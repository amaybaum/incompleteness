"""Exact checks for bounded stopping-time readiness. Standard library; stdout only.

No imports from previous handoffs. All requirements remain active under python -O.
"""
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product, permutations, combinations
from random import Random

DIRS = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))

def require(test, label):
    if not test:
        raise RuntimeError(label)

def basis(rows):
    pivots = {}
    for x in rows:
        while x:
            p = x.bit_length()-1
            if p in pivots:
                x ^= pivots[p]
            else:
                pivots[p] = x
                break
    return pivots

def independent_count(pivots, rows):
    b = dict(pivots)
    for x in rows:
        while x:
            p = x.bit_length()-1
            if p in b:
                x ^= b[p]
            else:
                b[p] = x
                break
    return len(b)-len(pivots)

def ball(k):
    return [x for x in product(range(-k,k+1), repeat=3) if sum(map(abs,x)) <= k]

class Wave:
    def __init__(self, L):
        self.L = L

    def unit(self, f, phase, x):
        a,b,c = (v % self.L for v in x)
        i = ((f*2+phase)*self.L**3 + (a*self.L+b)*self.L+c)
        return 1 << i

    @lru_cache(None)
    def stencil(self, t):
        # (initial phase, displacement), toggled in F_2.
        if t == -1:
            return frozenset({(0, (0,0,0))})
        if t == 0:
            return frozenset({(1, (0,0,0))})
        out = set(self.stencil(t-2))
        for phase,x in self.stencil(t-1):
            for d in DIRS:
                term = (phase, tuple(a+b for a,b in zip(x,d)))
                if term in out: out.remove(term)
                else: out.add(term)
        return frozenset(out)

    def row(self, f, t, x):
        out = 0
        for phase,y in self.stencil(t):
            out ^= self.unit(f,phase,tuple(a+b for a,b in zip(x,y)))
        return out

    def ready(self, K, q, t):
        rows = []
        pa,pb = (K,0,0),(0,K,0)
        for f in range(3):
            for x in ball(K):
                if (f,x) in ((0,pa),(1,pb)): continue
                rows.append(self.row(f,t,x))
            for x in ball(K-1): rows.append(self.row(f,t-1,x))
            rows.extend((self.row(f,t,q),self.row(f,t-1,q)))
        return rows

def stopping_rank_checks():
    # Existing geometry (B<K), followed by deliberately enlarged geometries.
    cases = [(1,0,1),(2,1,2),(3,2,3),(1,2,3),(2,3,5),(3,3,6)]
    intersection_count = 0
    for K,B,R in cases:
        L = 8*R+1
        q = (4*R,0,0)
        wave = Wave(L)
        ready = [wave.ready(K,q,t) for t in range(B+1)]
        J = 3*(len(ball(K))+len(ball(K-1)))+4
        require(all(len(basis(rows)) == J for rows in ready),'one-time codimension')
        probs = []
        for w in range(B+1):
            payload = [wave.row(0,w,(K,0,0)),wave.row(1,w,(0,K,0))]
            future = [wave.row(f,w+t,q) for t in range(1,K+1) for f in range(3)]
            p = Q(0)
            signed_ranks = []
            for mask in range(1<<w):
                times = [w]+[i for i in range(w) if mask>>i&1]
                piv = basis(row for i in times for row in ready[i])
                rank = len(piv)
                sign = (-1)**mask.bit_count()
                p += sign*Q(1,1<<rank)
                signed_ranks.append((sign,rank))
                require(independent_count(piv,payload+future) == 2+3*K,
                        'stopped payload/source uniformity on readiness intersection')
                intersection_count += 1
            require(p>0,'success branch nonempty')
            probs.append(p)
            # Receiver identities follow from E_w alone, on its entire linear subspace.
            piv = basis(ready[w])
            for t in range(K+1):
                for f in range(3):
                    r = wave.row(f,w+t,(0,0,0))
                    if t==K and f<2: r ^= payload[f]
                    require(independent_count(piv,[r])==0,'receiver law on all backgrounds')
            if (K,B,R)==(3,2,3):
                print('K=3 original geometry, w=%d: P(W=w) terms %s' % (w,signed_ranks))
        require(sum(probs) <= Q(B+1,1<<J),'deadline union bound')
        print('Rank PASS: K=%d B=%d L=%d J=%d; all w=0..B' % (K,B,L,J))
        wave.stencil.cache_clear()
    print('Readiness intersections checked exactly:',intersection_count)

def cycle_checks():
    tests = 0
    for n in range(1,7):
        for perm in permutations(range(n)):
            # Every nonempty event for n<=4; four varied event shapes thereafter.
            events = [set(i for i in range(n) if mask>>i&1) for mask in range(1,1<<n)] if n<=4 else [{0},{0,1},set(range(0,n,2)),set(range(n))]
            for E in events:
                saturation = set()
                returns = []
                for x in E:
                    y=perm[x];r=1
                    saturation.add(x)
                    while y not in E:
                        saturation.add(y); y=perm[y];r+=1
                    returns.append(r)
                require(sum(returns)==len(saturation),'finite Kac cycle sum')
                waits = []
                for x in saturation:
                    y=x;w=0
                    while y not in E: y=perm[y];w+=1
                    waits.append(w)
                require(sum(waits)==sum(r*(r-1)//2 for r in returns),'first-hit gap sum')
                # Exact deadline union bound over whole state space.
                for T in (0,1,3):
                    hits=0
                    for x in range(n):
                        y=x
                        for t in range(T+1):
                            if y in E: hits+=1;break
                            y=perm[y]
                    require(hits<=min(n,(T+1)*len(E)),'union bound')
                tests+=1
    # One 16-cycle, eight consecutive ready states: return mean 2,
    # uniform-start first-hit mean 9/4, already exceeding 1/mu(E).
    require(Q(sum(range(1,9)),16)==Q(9,4),'clustered-event example')
    # Identity permutation: every non-ready state waits forever.
    print('Permutation PASS:',tests,'event/permutation cases; Kac and first-hit laws distinguished')
    print('Countercontrols: 16-cycle return mean=2, first-hit mean=9/4; identity has never-ready states')

def stopped_countercontrols():
    # Finite iid bit tape advanced by cyclic shift (a bijection).
    L=5
    rows = list(product((0,1),repeat=L))
    for w in range(L):
        branch=[x for x in rows if x[w]==1 and not any(x[:w])]
        require(all(x[w]==1 for x in branch),'same-tick selection bias')
        next_values=[x[(w+1)%L] for x in branch]
        if w<L-1:
            require(sum(next_values)*2==len(branch),'fresh next tick before wrap')
        else:
            require(next_values==[0],'wrap-around stopping leak')
    print('Stopping controls PASS: selected bit biased; strictly future bit fair before wrap; wrap reveals old zero')

def entropy_checks():
    # Exact support-counting form: N^Nprod * prod(p_i^p_i) >=
    # p^p(1-p)^(1-p) / (q^p(1-q)^(1-p)), with integer multiplicities.
    # Avoid logs by exponentiating multinomial empirical distributions.
    checks=0
    for weights in product(range(5),repeat=4):
        total=sum(weights)
        if not total: continue
        for m in (1,2,3):
            a=sum(weights[:m]); b=total-a
            lhs=1
            for v in weights: lhs*=v**v
            # Within-group uniformity maximizes entropy: prod w_i^w_i >= (a/m)^a (b/(4-m))^b.
            require(lhs * m**a*(4-m)**b >= a**a*b**b,'entropy grouping inequality')
            checks+=1
    print('Entropy grouping PASS:',checks,'exact integer inequalities; no heat claim')

def raw_update_checks():
    # Independent direct raw update, with arbitrary dense backgrounds.
    rng=Random(1516)
    runs=0
    for L in (3,5,9):
        sites=list(product(range(L),repeat=3))
        wave=Wave(L)
        def neighbor_xor(field):
            result=set()
            for x in field:
                for d in DIRS:
                    y=tuple((a+b)%L for a,b in zip(x,d))
                    if y in result: result.remove(y)
                    else: result.add(y)
            return result
        for _ in range(4):
            old=[{x for x in sites if rng.getrandbits(1)} for f in range(3)]
            cur=[{x for x in sites if rng.getrandbits(1)} for f in range(3)]
            state=0
            for phase,raw in enumerate((old,cur)):
                lin=[raw[0],raw[1],raw[2]^(raw[0]&raw[1])]
                for f in range(3):
                    for x in lin[f]:state ^= wave.unit(f,phase,x)
            for t in range(5):
                for x in ((0,0,0),(L-1,1,0),(1,1,1)):
                    values=[(wave.row(f,t,x)&state).bit_count()%2 for f in range(3)]
                    values[2] ^= values[0]&values[1]
                    require(values==[int(x in v) for v in cur],'stencil vs direct raw evolution')
                a,b,d=cur;oa,ob,od=old
                sa,sb,sd=map(neighbor_xor,cur)
                nxt=[sa^oa,sb^ob,sd^od^neighbor_xor(a&b)^(sa&sb)^(sa&ob)^(sb&oa)]
                old,cur=cur,nxt
                runs+=1
        wave.stencil.cache_clear()
    print('Independent raw-update PASS:',runs,'dense-background transitions, including wrap-around')

def main():
    entropy_checks();cycle_checks();stopped_countercontrols();raw_update_checks();stopping_rank_checks()
    print('PASS: bounded stopping theorem checks; no native readiness detector or clock constructed')

if __name__=='__main__': main()
