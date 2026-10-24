from functools import lru_cache
from itertools import product
from diamond_strip import H,X,Z,initial,advance,indices
from inherited_core import hp,odd,ball
T=185;P=12*840**T;S=T+P;d=68;R=S+d
@lru_cache(None)
def orbit(q):
 s=initial(q,6);start=s;states=[]
 while True:
  states.append(s);s=advance(s,6)
  if s==start:return tuple(states)
  if len(states)>10000:raise RuntimeError('orbit bound')

def upper(q,t,v):
 a,b,n=map(abs,v);a,b=sorted((a,b),reverse=True);l=t-n
 if l<0 or a+b>l or (l-a-b)%2:return Z
 if (l,a,b) not in indices(6):raise RuntimeError(('uncovered',l,a,b))
 states=orbit(q);return states[n%len(states)][indices(6).index((l,a,b))]

def calc(x,u,my=0,mr=0,p=None):
 end=(0,0,3)
 controls=[((0,-S,-d),x),((0,S,-d),my^mr),((T,P,-d),my),((-T,P,-d),mr)]
 def base(t,v):
  val=upper((u,0,1),t,(v[0],v[1],R-v[2]))
  for loc,bit in controls:
   ds=tuple(abs(a-b) for a,b in zip(v,loc))
   if sum(ds)<=t:
    if sum(ds)!=t:raise RuntimeError('behind lowerfront')
    if odd(ds):val=X(val,hp((0,bit,0),t))
  return val
 old={v:base(R-2,v) for v in ball(3,end)}
 now={v:base(R-1,v) for v in ball(4,end)}
 records={}
 for tick in range(R,R+4):
  nxt={}
  for v in ball(R+3-tick,end):
   ns=[]
   for axis in range(3):
    for sign in (-1,1):
     w=list(v);w[axis]+=sign;ns.append(now[tuple(w)])
   nxt[v]=X(old[v],H(X(*ns)))
  if tick==R and p is not None:nxt[(0,0,0)]=(x,1,p)
  records[tick-R]=nxt
  old,now=now,nxt
 return now[end],records
if __name__=='__main__':
 for u in (0,1):print('period',u,len(orbit((u,0,1))),'phaseR',R%len(orbit((u,0,1))))
 for x,u in product((0,1),repeat=2):print('native',x,u,calc(x,u)[0])
 for x,u,p in product((0,1),repeat=3):print('diagnostic',x,u,p,calc(x,u,p=p)[0])
