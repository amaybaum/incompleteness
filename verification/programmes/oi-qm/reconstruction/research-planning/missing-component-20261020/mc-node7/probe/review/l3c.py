import sys
src=open(sys.argv[1]).read().replace("if __name__ == '__main__':\n    main()","")
g={'__name__':'x','__file__':sys.argv[1]}; exec(src,g)
from itertools import product
F=g['F']
for n,k in ((1,1),(2,1)):
    T=5; steps=g['le_steps'](k)
    for a,b in product((0,1),repeat=2):
        phi=lambda st:((st[0]+1)%T, steps[st[0]](st[1]))
        union=set()
        for lam in (0,1):
            for u in range(n):
                s0=(0,(a,b,0,0,0,0,lam,u)); s=s0
                while True:
                    union.add(s); s=phi(s)
                    if s==s0: break
        rp=[s for s in union if s[0]==0]
        vis={}
        for s in rp:
            key=s[1][:6]; vis[key]=vis.get(key,0)+F(1,len(rp))
        print(f'LE({n},{k}) a={a} b={b}: orbit lengths total {len(union)}, phase-0 points {len(rp)}, visible marginal at phase 0: {dict(vis)}')
