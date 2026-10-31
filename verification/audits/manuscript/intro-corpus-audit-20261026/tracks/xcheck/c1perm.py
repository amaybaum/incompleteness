# V={0,1}, H={0,1}, index 2x+h; (x,0)->(x,1), (x,1)->(1-x,0); prior delta_0 on H.
def phi(x,h): return (x,1) if h==0 else (1-x,0)
for t in range(5):
    G=[]
    for a in range(2):
        s=(a,0)
        for _ in range(t): s=phi(*s)
        G.append(s[0])
    print(t,G)
# C1 literal: reachable states (c,h) with successor visible depending on h
print([(c,h,phi(c,h)[0]) for c in range(2) for h in range(2)])
