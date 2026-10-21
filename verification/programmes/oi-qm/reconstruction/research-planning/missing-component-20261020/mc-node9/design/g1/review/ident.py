from eng import *
import pickle
res=pickle.load(open('alph.pkl','rb')); fdF,_=pickle.load(open('fd_full.pkl','rb'))
C=Cards()
def nm(k): a,b=divmod(k,4); return NM[a]+'_A'+NM[b]+'_B'
def W(t,word):
    th=QM(lift_tables(*t)); S=th.init()
    for op in word: S=th.gate(op,S)
    r=th.read('rB',S); return r.get(1,(0,))[0]
W6=['sA','c']*3; W7=W6+['sA']
for name in ['no sB {sA,c,4 flips,rA,rB}','K-G1 {sA,c,rB}']:
    fd,eq=res[name]
    groups={}
    for t in TRIPLES: groups.setdefault((fd[t],eq[t]),set()).add((t[0],t[2]))
    print('==',name)
    for key in sorted(groups,key=lambda k:(k[0] is None,k[0] or 0)):
        if key[0] is None or key[0]>=5:
            ps=sorted(groups[key])
            print('  fd=%s ==stdQM(alph)=%s (sA,c) pairs:'%key,[(nm(a),nm(c)) for a,c in ps][:8],
                  ' W6,W7:',sorted({(W((a,0,c),W6),W((a,0,c),W7)) for a,c in ps}),
                  ' full-alphabet fd with sB=std:',sorted({fdF[(a,0,c)] for a,c in ps}))
