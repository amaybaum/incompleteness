exec(open('corr2.py').read().split("std=G_of")[0])
W6=('sA','c')*3+('rB',); W7=('sA','c')*3+('sA','rB')
for t in [(0,0,0),(0,3,8),(12,0,0),(12,3,8)]:
    G=G_of(*t)
    p=lambda w: sum(v for rec,v in qm_records(w,G).items() if rec[-1]==1)
    print(t,'P(q_B=1): W6',p(W6),'W7',p(W7))
print('cards: W6',sum(v for rec,v in card_records(W6).items() if rec[-1]==1),'W7',sum(v for rec,v in card_records(W7).items() if rec[-1]==1))
