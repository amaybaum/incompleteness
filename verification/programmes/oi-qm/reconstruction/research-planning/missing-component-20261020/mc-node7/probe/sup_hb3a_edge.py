"""Supplementary to HB-3alpha (not decision-bearing): glued-graph mesoscopic Ollivier curvature on the lattice edge (A, A+e1) at the long-edge endpoint, options 1 (w = 1) and 2 (w = 1/2) of amendment A-3. Exact min-cost-flow W1 from p7.py. Run: python3 -I -B sup_hb3a_edge.py p7.py"""
import sys
src=open(sys.argv[1]).read().replace("if __name__ == '__main__':\n    main()","")
g={'__name__':'x','__file__':sys.argv[1]}; exec(src,g)
F=g['F']
for L in (10,12,14):
    adj,A,B=g['torus'](L,glue=True); c={}
    def d(x):
        if x not in c: c[x]=g['bfs'](adj,x)
        return c[x]
    for dl in (1,2,3):
        for y in [(1,0,0)]:
            for w in (F(1),F(1,2)):
                adjr,_,_=g['torus'](L); cr={}
                def dr(x):
                    if x not in cr: cr[x]=g['bfs'](adjr,x)
                    return cr[x]
                def mix(x):
                    m={}
                    for v,p in g['unif'](g['ball'](dr(x),dl)).items(): m[v]=m.get(v,0)+(1-w)*p
                    for v,p in g['unif'](g['ball'](d(x),dl)).items(): m[v]=m.get(v,0)+w*p
                    return m
                W=g['w1_exact'](mix(A),mix(y),d)
                print(L,dl,w,'kappa(A,A+e1)=',1-W)
