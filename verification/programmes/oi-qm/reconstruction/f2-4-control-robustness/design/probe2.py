exec(open('probe.py').read().split('for q,N in [(3,2),(3,3),(5,2)]:')[0])
import time
for q,N in [(7,2)]:
    run(q,N)
# orbit counts and single-site coverage at N=3,4
for q,N in [(3,3),(5,3),(3,4),(7,3)]:
    t0=time.time(); orbs,where=orbits(symp_gens_cf(q,N),q,N)
    single=[any(sum(1 for i in range(N) if (v[i],v[N+i])!=(0,0))==1 for v in o) for o in orbs]
    print(f"(q,N)=({q},{N}) R_cf orbits {len(orbs)} sizes {sorted(len(o) for o in orbs)[:6]} every orbit has a single-site vector: {all(single)} [{time.time()-t0:.1f}s]")
