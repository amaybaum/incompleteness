from core import *
from itertools import product
T=185;P=12*840**T;S=T+P;d=68;R=S+d
end=(0,0,2)
ports=[(R+2,0,2),(-R-2,0,2),(0,R+2,2),(0,-R-2,2)]
def calc(x,u,my,mr,mask,p=None):
 controls=[((0,-S,-d),x),((0,S,-d),my^mr),((T,P,-d),my),((-T,P,-d),mr)]+[(v,(mask>>i)&1) for i,v in enumerate(ports)]
 def base(t,v):
  val=upper((u,0,1),t,(v[0],v[1],R-v[2]))
  for loc,bit in controls:
   ds=tuple(abs(a-b) for a,b in zip(v,loc))
   if sum(ds)<=t:
    if sum(ds)!=t:raise RuntimeError('late lower front')
    if odd(ds):val=X(val,hp((0,bit,0),t))
  return val
 old={v:base(R-2,v) for v in ball(2,end)}
 now={v:base(R-1,v) for v in ball(3,end)}
 records={}
 for tick in range(R,R+3):
  nxt={}
  for v in ball(R+2-tick,end):
   ns=[]
   for axis in range(3):
    for sign in (-1,1):
     w=list(v);w[axis]+=sign;ns.append(now[tuple(w)])
   nxt[v]=X(old[v],H(X(*ns)))
  if tick==R and p is not None:nxt[(0,0,0)]=(x,1,p)
  records[tick-R]=dict(nxt)
  old,now=now,nxt
 return now[end],records
for mask in range(16):
 vals=[calc(x,u,0,0,mask)[0] for x,u in product((0,1),repeat=2)]
 print(mask, vals)
