"""Independent history sidecar audit using reviewer's polynomial dynamics."""
from checks import *

def native_base(t,v):
    return tuple(frozenset(m for m in poly if not any(name.startswith('c_') for name in m)) for poly in base(t,v))

@lru_cache(None)
def native_eval(t,v):
    if t<=R-1:return native_base(t,v)
    return px(native_eval(t-2,v),ph(px(*(native_eval(t-1,add(v,e)) for e in steps))))

@lru_cache(None)
def diagnostic_eval(t,v):
    if t<=R-1:return native_base(t,v)
    if t==R and v==(0,0,0):return x,ONE,variable('p')
    return px(diagnostic_eval(t-2,v),ph(px(*(diagnostic_eval(t-1,add(v,e)) for e in steps))))

s=(0,-1,2)
value=native_eval(R+1,s)
need(value==(ZERO,xor(ONE,y),x),'history sidecar native formula')
need(diagnostic_eval(R+1,s)==value,'sidecar cannot depend on p intervention outside cone')
need(diagnostic_eval(R+2,(0,0,2))[0]==variable('p'),'q2 actual operand')
print('H1: actual sidecar U_(R+1)(0,-1,2)=(0,1 XOR y,x), all masks: PASS')
print('H2: x sidecar survives arbitrary qY operand replacement p; its y-related B field is NOT a diagnostic transfer of p: PASS')
# No original lower source can reach s before R+1; upper pulse first arrives at R-1.
need(all(distance(loc,s)>=R+1 for loc,_ in lower),'lower first arrival R+1 or later')
need(distance((0,0,R),s)==R-1,'upper firstarrival sidecar')
need(upper(4,R-1,(0,-1,R-2))==0 and upper(5,R-1,(0,-1,R-2))==0,'first pulse front cancels')
need(upper(4,R,(0,-1,R-2))==0 and upper(5,R,(0,-1,R-2))==0,'following parity blank')
print('H3: sidecar prefix through R is blank under retained ready cone; pulse front at R-1 cancels and R has wrong parity: PASS')
print('H4: sidecar is a specific earlier spacetime register; simultaneous control access and native gate integration remain unproved.')
