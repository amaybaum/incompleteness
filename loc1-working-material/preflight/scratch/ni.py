import sys
sys.path.insert(0, sys.argv[1])
from c21_engine import *
I = [[1 if i==j else 0 for j in range(16)] for i in range(16)]
NI = [r[:] for r in I]; NI[14][15] = 1
for order in ("rare","greedy"):
    E = Engine([NI],4,4,order=order)
    print(order, E.order)
    st,f,s = E.run("exist", budget=300000)
    print(st, s)
    # depth profile: count accepted per depth via knuth single probe
    E.reset(); E.mode="exist"; E.budget=10**9
    d=0
    for d in range(16):
        i=E.order[d]; c=E.candidates(d); ok=[]
        for a,b in c:
            mk=len(E.U)
            if E.place(i,a,b): ok.append((a,b)); E.undo(mk)
        print(d, i, len(c), ok[:6])
        if not ok: break
        a,b=ok[0]; E.place(i,a,b); E._commit_state(a,b); E.assigned.append(i)
