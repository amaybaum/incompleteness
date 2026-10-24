"""Independent signed-position lookahead strip and third outward step."""
from checks import H,hp,parity,need,R,S,P,T,steps,add,norm,x,u,my,mr,ONE,ZERO,variable,xor,mul,px,ph,constant
from functools import lru_cache

keys=tuple((l,a,b) for l in range(7) for a in range(-6,7) for b in range(-6,7) if abs(a)+abs(b)<=l and l+abs(a)+abs(b)<=6 and (l-a-b)%2==0)
def step(old):
 look=[{} for _ in range(5)]
 for l in range(7):
  for j in range((6-l)//2+1):
   for ll,a,b in keys:
    if ll!=l or l+abs(a)+abs(b)>6-2*j:continue
    prev=old[l,a,b] if j==0 else look[j-1][l,a,b]
    future=look[j+1].get((l-2,a,b),0);trans=0
    for aa,bb in ((a-1,b),(a+1,b),(a,b-1),(a,b+1)):trans ^= look[j].get((l-1,aa,bb),0)
    look[j][l,a,b]=look[j].get((l-2,a,b),0)^H[prev^future^trans]
 return look[0]
def direct(q):
 @lru_cache(None)
 def f(t,v):
  if t<0 or norm(v)>t:return 0
  if t==0:return q if v==(0,0,0) else 0
  z=0
  for e in steps:z ^= f(t-1,add(v,e))
  return f(t-2,v)^H[z]
 return f
def initial(q):
 f=direct(q);return {(l,a,b):f(l,(a,b,0)) for l,a,b in keys}
@lru_cache(None)
def orbit(q):
 first=initial(q);s=first;out=[]
 while True:
  out.append(s);s=step(s)
  if s==first:return out
  need(len(out)<10001,'sixlag orbit bound')
count=0
for q in (4,5):
 f=direct(q);s=initial(q)
 for n in range(9):
  for (l,a,b),value in s.items():
   need(value==f(n+l,(a,b,n)),'signed strip direct comparison');count+=1
  s=step(s)
need(len(orbit(4))==3600 and len(orbit(5))==2940,'sixlag periods')
need(R%3600==253 and R%2940==253,'sixlag phases')
print('GEO1: %d direct-native signed-strip comparisons; independently reproduce periods3600/2940 and residues253: PASS'%count)
def pulse(q,t,v):
 a,b,n=v;n=abs(n);l=t-n
 if l<0 or l<abs(a)+abs(b) or (l-a-b)%2:return 0
 need((l,a,b) in keys,'covered lag')
 data=orbit(q);return data[n%len(data)][l,a,b]
lower=[((0,-S,-68),x),((0,S,-68),xor(my,mr)),((T,P,-68),my),((-T,P,-68),mr)]
def base(t,v):
 a=pulse(4,t,(v[0],v[1],R-v[2]));b=pulse(5,t,(v[0],v[1],R-v[2]))
 out=[xor(constant((a>>j)&1),u if ((a^b)>>j)&1 else ZERO) for j in range(3)]
 for loc,bit in lower:
  ds=tuple(abs(a-b) for a,b in zip(v,loc));need(sum(ds)>=t,'lower front')
  if sum(ds)==t and parity(ds):
   field=hp(2,t)
   for j in range(3):
    if field>>j&1:out[j]=xor(out[j],bit)
 return tuple(out)
@lru_cache(None)
def ev(t,v,diag):
 if t<=R-1:return base(t,v)
 if diag and t==R and v==(0,0,0):return x,ONE,variable('p')
 return px(ev(t-2,v,diag),ph(px(*(ev(t-1,add(v,e),diag) for e in steps))))
need(ev(R+3,(0,0,3),False)==(u,mul(x,u),u),'third native triple')
p=variable('p');xp=xor(x,p)
expected=(xor(u,xp,mul(u,xp)),xor(x,p,mul(u,p),mul(mul(u,x),p)),mul(u,xp))
need(ev(R+3,(0,0,3),True)==expected,'complete third diagnostic triple')
print('GEO2: independent symbolic stencil gives q3=(u,xu,u), and complete p-diagnostic formula, all masks: PASS')
print('SCOPE: accepted local third-step formula under inherited source reduction and extended ready cone; no Y-only extraction or reset follows.')
