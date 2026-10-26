# ch01 §1.11 card game: hole h, burn b in {0,1}; shuffle = swap (h,b)->(b,h). Exact.
from fractions import Fraction as F
from itertools import product
sw=lambda s:(s[1],s[0])
def match(protocol):
    tot=F(0);n=0
    for h0,b0,f1,f2 in product((0,1),repeat=4):   # f1,f2: fresh cards for re-burn rules (16 cases)
        s=(h0,b0)
        s=protocol(s,f1,f2)
        tot+= (s[0]==h0); n+=1
    return tot/n
one=lambda s,f1,f2: sw(s)
two=lambda s,f1,f2: sw(sw(s))
# peek rule A: revealed hole card is burned onto the burn position (old burn discarded), fresh card dealt as hole
peekA=lambda s,f1,f2: sw((f1,s[0]))
# peek rule B: revealed hole card discarded and replaced by fresh card; burn untouched
peekB=lambda s,f1,f2: sw((f1,s[1]))
# peek rule C: burn card (the record) replaced by a fresh card; hole kept
peekC=lambda s,f1,f2: sw((s[0],f1))
# apply first shuffle, then peek rule, then second shuffle
def with_peek(rule): return lambda s,f1,f2: rule(sw(s),f1,f2)
print("one shuffle:",match(one)); print("two shuffles:",match(two))
G1=[[F(1,2)]*2 for _ in range(2)]
print("chained through middle (G1*G1)[0][0]:",sum(G1[0][k]*G1[k][0] for k in range(2)))
for nm,r in (("A burn<-revealed",peekA),("B hole<-fresh, burn kept",peekB),("C burn<-fresh",peekC)):
    print("peek rule",nm,":",match(with_peek(r)))
