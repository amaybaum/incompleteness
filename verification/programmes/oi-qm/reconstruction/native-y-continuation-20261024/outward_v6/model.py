"""Exact bounded-lag upper strip and packed actual-geometry outward diamond."""
from functools import lru_cache
from itertools import product
from pathlib import Path
import json
ZERO=(0,0,0)
T=185;P=12*840**T;S=T+P;d=68;R=S+d;BASE=T+d
ROWS=tuple(product((0,1),repeat=5)) # x,u,mY,mR,p
ALL=(1<<len(ROWS))-1
MASKS=tuple(sum(row[j]<<i for i,row in enumerate(ROWS)) for j in range(5))
XM,UM,MY,MR,PM=MASKS

def H(v):a,b,d=v;return b,d,a^(b&d)
def X(*vs):
 a=b=d=0
 for v in vs:a^=v[0];b^=v[1];d^=v[2]
 return a,b,d

def hp(v,n):
 for _ in range(n%12):v=H(v)
 return v

def indices(L):
 return tuple((ell,a,b) for ell in range(L+1) for a in range(ell+1) for b in range(a+1) if a+b<=ell and ell+a+b<=L and (ell-a-b)%2==0)

@lru_cache(None)
def pulse(t,a,b,c):
 """Direct native pulse recursion, packed u=0,1, using cubic symmetry."""
 if t<0 or a+b+c>t or (t-a-b-c)%2:return ZERO
 if t==0:return (2,0,3) if (a,b,c)==(0,0,0) else ZERO
 vals=[]
 for j in range(3):
  for sign in (-1,1):
   pos=[a,b,c];pos[j]+=sign;pos=sorted(map(abs,pos),reverse=True)
   vals.append(pulse(t-1,*pos))
 return X(pulse(t-2,a,b,c),H(X(*vals)))

@lru_cache(None)
def strip(L):
 """Layer-first evaluation. Future n+1 terms live two layers lower."""
 values={}
 def get(ell,a,b,n):
  if ell<0:return ZERO
  a,b=sorted((abs(a),abs(b)),reverse=True)
  key=(ell,a,b)
  if a+b>ell or (ell-a-b)%2 or ell+a+b>L:return ZERO
  return values[key][n]
 for ell,a,b in indices(L):
  cap=BASE+(L-ell)//2
  arr=[pulse(ell,*sorted((a,b,0),reverse=True))]
  values[ell,a,b]=arr
  for n in range(1,cap+1):
   trans=X(get(ell-1,a-1,b,n),get(ell-1,a+1,b,n),get(ell-1,a,b-1,n),get(ell-1,a,b+1,n))
   arr.append(X(get(ell-2,a,b,n),H(X(arr[n-1],get(ell-2,a,b,n+1),trans))))
 return values

def upper(L,t,v):
 a,b,n=map(abs,v);a,b=sorted((a,b),reverse=True);ell=t-n
 if ell<0 or a+b>ell or (ell-a-b)%2:return ZERO
 if ell+a+b>L:raise RuntimeError(('uncovered upper lag',ell,a,b,L))
 nr=n-P
 if nr<0:raise RuntimeError('invalid period reduction')
 val=strip(L)[ell,a,b][nr]
 return tuple((ALL^UM if b&1 else 0)^(UM if b&2 else 0) for b in val)

def odd(parts):
 acc=0
 for p in parts:
  if acc&p:return 0
  acc|=p
 return 1

def ball(r,center):
 for a in range(-r,r+1):
  for b in range(-r+abs(a),r-abs(a)+1):
   for c in range(-r+abs(a)+abs(b),r-abs(a)-abs(b)+1):
    yield center[0]+a,center[1]+b,center[2]+c

def calc(k,operand_site="qY"):
 end=(0,0,k);L=2*k
 controls=[((0,-S,-d),XM),((0,S,-d),MY^MR),((T,P,-d),MY),((-T,P,-d),MR)]
 def base(t,v):
  value=upper(L,t,(v[0],v[1],R-v[2]))
  for pos,bits in controls:
   ds=tuple(abs(a-b) for a,b in zip(pos,v))
   if sum(ds)<=t:
    if sum(ds)!=t:raise RuntimeError('lower source behind front')
    if odd(ds):value=X(value,hp((0,bits,0),t))
  return value
 old={v:base(R-2,v) for v in ball(k,end)}
 now={v:base(R-1,v) for v in ball(k+1,end)}
 records={}
 for tau in range(k+1):
  nxt={}
  for v in ball(k-tau,end):
   ns=[]
   for axis in range(3):
    for sign in (-1,1):
     w=list(v);w[axis]+=sign;ns.append(now[tuple(w)])
   nxt[v]=X(old[v],H(X(*ns)))
  if tau==0:
   if nxt[(0,0,0)]!=(XM,ALL,XM^UM):raise RuntimeError('original qY changed')
   if operand_site=="qY":nxt[(0,0,0)]=(XM,ALL,PM) # diagnostic replaces only D
  if tau==2 and operand_site=="q2":
   q=nxt[(0,0,2)]
   if q!=(XM^UM,XM^UM,ALL^(XM&(XM^UM))):raise RuntimeError("q2 natural code changed")
   nxt[(0,0,2)]=(PM,q[1],q[2]) # separate diagnostic replaces only A
  records[tau]=nxt
  old,now=now,nxt
 return now[end],records

def lane(v,i):return tuple((w>>i)&1 for w in v)

def describe(k):
 out,_=calc(k)
 raw=[]
 for field in range(3):
  for c in (0,1):
   if out[field]==(PM^(ALL*c)):raw.append((field,c))
 native={}
 for i,(x,u,my,mr,p) in enumerate(ROWS):
  if p==x^u:native[x,u,my,mr]=lane(out,i)
 yonly=all(v==native[0,x^u,0,0] for (x,u,my,mr),v in native.items())
 return {'k':k,'raw_p_fields':raw,'native_y_only':yonly,'native_x_u_table':[native[x,u,0,0] for x,u in product((0,1),repeat=2)],'packed_output':out}

if __name__=='__main__':
 for k in range(1,13):print(json.dumps(describe(k)),flush=True)
