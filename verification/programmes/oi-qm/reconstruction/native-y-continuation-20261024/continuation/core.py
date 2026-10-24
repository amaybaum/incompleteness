"""Exact single-pulse bounded-lag recurrence and local late-collision diamond."""
from functools import lru_cache
from itertools import product
ZERO=(0,0,0)
def H(v):
 a,b,d=v;return b,d,a^(b&d)
def X(*vs):return tuple(sum(v[i] for v in vs)%2 for i in range(3))
def hp(v,n):
 for _ in range(n%12):v=H(v)
 return v

def initial(q):
 f=q;z=H(q);l=H(z);j=X(H(q),H(X(q,hp(q,2))));g=q
 return 0,f,z,l,j,g

def advance(q,state):
 phase,f,z,l,j,g=state;n=phase+1
 fn=X(hp(q,n),H(X(f,hp(q,n+1))))
 zn=H(X(z,hp(q,n)));ln=H(X(l,zn))
 zfuture=H(X(zn,hp(q,n+1)))
 jn=X(zn,H(X(j,zfuture,fn,ln)))
 ffuture=X(hp(q,n+1),H(X(fn,hp(q,n+2))))
 gn=X(fn,H(X(g,ffuture)))
 return n%12,fn,zn,ln,jn,gn

@lru_cache(None)
def orbit(q):
 states=[];seen={};v=initial(q)
 while v not in seen:
  seen[v]=len(states);states.append(v);v=advance(q,v)
  if len(states)>500000:raise RuntimeError('orbit limit')
 return tuple(states),seen[v],len(states)-seen[v]

def state(q,n):
 states,start,period=orbit(q)
 if n>=len(states):n=start+(n-start)%period
 return states[n]

def upper(q,t,pos):
 a,b,n=map(abs,pos);a,b=sorted((a,b),reverse=True)
 lag=t-a-b-n
 if lag<0 or lag%2:return ZERO
 f,z,l,j,g=state(q,n)[1:]
 if (a,b,lag)==(0,0,0):return hp(q,n)
 if (a,b,lag)==(1,0,0):return z
 if (a,b,lag)==(2,0,0):return l
 if (a,b,lag)==(1,1,0):return ZERO
 if (a,b,lag)==(0,0,2):return f
 if (a,b,lag)==(1,0,2):return j
 if (a,b,lag)==(0,0,4):return g
 raise RuntimeError(('uncovered pulse displacement',a,b,n,lag))

def odd(parts):
 seen=0
 for p in parts:
  if seen&p:return 0
  seen|=p
 return 1

def ball(r,center):
 for a in range(-r,r+1):
  for b in range(-r+abs(a),r-abs(a)+1):
   for c in range(-r+abs(a)+abs(b),r-abs(a)-abs(b)+1):
    yield center[0]+a,center[1]+b,center[2]+c

def native_second(T,P,d,x,my,mr,u,p=None):
 S=T+P;R=S+d;q=(u,0,1);end=(0,0,2)
 # Coordinates relative qY. Every lower source is on end's R+2 boundary.
 controls=[((0,-S,-d),x),((0,S,-d),my^mr),((T,P,-d),my),((-T,P,-d),mr)]
 def base(t,v):
  val=upper(q,t,(v[0],v[1],R-v[2]))
  for loc,bit in controls:
   dist=tuple(abs(a-b) for a,b in zip(v,loc))
   if sum(dist)<=t:
    if sum(dist)!=t:raise RuntimeError('lower source already behind front')
    if odd(dist):val=X(val,hp((0,bit,0),t))
  return val
 old={v:base(R-2,v) for v in ball(2,end)}
 now={v:base(R-1,v) for v in ball(3,end)}
 records={}
 for tick in range(R,R+3):
  nxt={}
  for v in ball(R+2-tick,end):
   neighbours=[]
   for axis in range(3):
    for sign in (-1,1):
     w=list(v);w[axis]+=sign;neighbours.append(now[tuple(w)])
   nxt[v]=X(old[v],H(X(*neighbours)))
  if tick==R and p is not None:nxt[(0,0,0)]=(x,1,p)
  records[tick-R]=dict(nxt)
  old,now=now,nxt
 return now[end],records
