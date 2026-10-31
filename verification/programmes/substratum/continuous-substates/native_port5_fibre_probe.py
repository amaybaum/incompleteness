#!/usr/bin/env python3
"""Exact fibre-law controls, not a native full-carrier or 78-tick replay."""
from fractions import Fraction as F
from itertools import product
import json


def require(ok, reason):
    if not ok:
        raise AssertionError(reason)


def h(v):
    a,b,d=(v>>2)&1,(v>>1)&1,v&1
    return (b<<2)|(d<<1)|(a^(b&d))


def main():
    contexts=list(product(range(8),repeat=2))
    joint={}
    for a,b in contexts:
        out=[a^h(k^b) for k in range(8)]
        require(len(set(out))==8,"native local permutation family")
        for k,y in enumerate(out):
            joint[((a,b),k,y)]=F(1,len(contexts)*8)
    # Exact uniform endpoint law conditional on each fixed complementary context.
    for c in contexts:
        for y in range(8):
            p=sum((v for (cc,k,yy),v in joint.items() if cc==c and yy==y),F(0))
            require(p==F(1,len(contexts)*8),"Y independent of complementary context")
            ks=[k for cc,k,yy in joint if cc==c and yy==y]
            require(len(ks)==1,"key fibre singleton given context and endpoint")
    # Uniform marginal does not imply independence of an invertible full-state label.
    # The label (c,k) is an abstract diagnostic for a bijectively relabelled full cut.
    total_variation=F(0)
    for c,k,y in product(contexts,range(8),range(8)):
        actual=joint.get((c,k,y),F(0))
        independent=F(1,len(contexts)*64)
        total_variation+=abs(actual-independent)/2
    require(total_variation==F(7,8),"must reject record/full-state independence")
    # Countercontrol1: Y=H(k); key is fully disclosed by Y.
    disclosed={y:[] for y in range(8)}
    for k in range(8):
        disclosed[h(k)].append(k)
    require(all(len(v)==1 for v in disclosed.values()),"known-permutation key disclosure")
    # Countercontrol2: Y=H(k XOR c), c private/uniform. Y stays uniform,
    # yet each observed Y has one pair per k, so posterior key is uniform.
    hidden={(k,c,h(k^c)):F(1,64) for k,c in product(range(8),repeat=2)}
    for k,y in product(range(8),repeat=2):
        p=sum((v for (kk,c,yy),v in hidden.items() if kk==k and yy==y),F(0))
        require(p==F(1,64),"private-context key not disclosed")
    # An abstract context-measurable enable flag tests terminal accounting.
    # This does not replace the actual native source's success/failure law.
    observed={}
    for (c,k,y),mass in joint.items():
        enabled=(c[0]%2==0)
        result=y if enabled else None
        observed[(c,k,result)]=mass
    require(sum(observed.values(),F(0))==1,"guarded total mass")
    terminal=sum((mass for (c,k,y),mass in observed.items() if y is None),F(0))
    require(terminal==F(1,2),"terminal mass retained")
    for c in contexts:
        if c[0]%2:
            require(all(y is None for cc,k,y in observed if cc==c),"no read after terminal failure")
        else:
            for y in range(8):
                mass=sum((v for (cc,k,yy),v in observed.items() if cc==c and yy==y),F(0))
                require(mass==F(1,len(contexts)*8),"enabled uniform branches")
    print(json.dumps({"status":"PASS","local_permutation_contexts":len(contexts),
         "joint_rows":len(joint),"guarded_terminal_mass":str(terminal),"record_full_state_TV_from_product":str(total_variation),
         "uniform_record_key_disclosure_countercontrols":["full when permutation known","none with balanced private context"],
         "scope":"conditional fibre algebra; native operational quotient and two settings absent"},sort_keys=True))


if __name__=="__main__":
    main()
