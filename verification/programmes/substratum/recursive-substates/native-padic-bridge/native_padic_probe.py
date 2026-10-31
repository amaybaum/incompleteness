#!/usr/bin/env python3
"""NATIVE-PADIC-1: exact modular reduction controls for the OI cubic wave.

Research-only finite regression on the alpha=1 reference rule (wave_eqn.c),
the integer-coefficient two-slice wave formula; the substratum coefficient
is open (SM 4.1). Not exhaustive over microscopic configurations.
The general all-state reduction theorem is a separate algebraic proof.
No continuous quantum, nonabelian gauge or physical scale coupling.
"""
import json

L = 3
SITES = tuple((x,y,z) for x in range(L) for y in range(L) for z in range(L))
AXES = ((1,0,0),(0,1,0),(0,0,1))
ORIGIN = SITES.index((0,0,0))
N = len(SITES)


def require(ok, label):
    if not ok:
        raise AssertionError(label)


def neighbors(p):
    out=[]
    for d in AXES:
        out.append(SITES.index(tuple((p[i]+d[i])%L for i in range(3))))
        out.append(SITES.index(tuple((p[i]-d[i])%L for i in range(3))))
    return tuple(out)


NB = tuple(neighbors(p) for p in SITES)


def F(now, mod):
    return tuple(sum(now[j] for j in NB[i]) % mod for i in range(N))


def native_step(state, mod, mutated=False):
    now, prev = state
    out = list((sum(now[j] for j in NB[i])-prev[i]) % mod for i in range(N))
    if mutated:
        out[ORIGIN]=(out[ORIGIN]+((now[ORIGIN]>>1)&1))%mod
    return (tuple(out), now)


def native_unstep(state, mod, mutated=False):
    now, prev = state
    old_prev=list((sum(prev[j] for j in NB[i])-now[i])%mod for i in range(N))
    if mutated:
        old_prev[ORIGIN]=(old_prev[ORIGIN]+((prev[ORIGIN]>>1)&1))%mod
    return (prev, tuple(old_prev))


def project(state, mod):
    return tuple(tuple(x%mod for x in layer) for layer in state)


def source(k, mod):
    def field(p, previous=False):
        x,y,z=p
        if k==0:
            return 0
        if k==1:
            return 1
        if k==2:
            return int(p==(0,0,0)) if not previous else 0
        if k==3:
            return int(p==(0,0,0)) if previous else 0
        if k==4:
            return x+y+z if not previous else x*y+z
        if k==5:
            return x*x+2*y+3*z if not previous else x+2*y*y
        if k==6:
            return 3*x*y+z*z if not previous else y*z+2*x
        if k==7:
            return x+4*y+9*z if not previous else x*y*z
        if k==8:
            return 7*x+11*y+13*z if not previous else 17*x+19*y+23*z
        if k==9:
            return x*y+y*z+z*x if not previous else (x+1)*(y+1)*(z+1)
        if k==10:
            return (x+2*y+3*z+5)**3 if not previous else (7*x+3*y+z+1)**2
        return ((x+1)*127+(y+3)*511+(z+5)*97)**2 if not previous else ((x+13)*(y+17)*31+z*59)**3
    return (tuple(field(p)%mod for p in SITES),
            tuple(field(p,True)%mod for p in SITES))


def run():
    checks=0
    stages=[]
    for n in range(1,7):
        q=1<<n
        for k in range(12):
            initial=source(k,q)
            require(native_unstep(native_step(initial,q),q)==initial, "native inverse n=%d k=%d"%(n,k))
            require(native_step(native_unstep(initial,q),q)==initial, "native other inverse")
            checks+=2
            # Both time orientations: each projected trajectory is the
            # exact native trajectory of its reduced q-state.
            for m in range(1,n):
                low=1<<m
                for direction in ("forward","backward"):
                    now=initial
                    reduced=project(initial,low)
                    for t in range(17):
                        require(project(now,low)==reduced, "projection n=%d m=%d k=%d t=%d %s"%(n,m,k,t,direction))
                        checks+=1
                        if t<16:
                            fn=native_step if direction=="forward" else native_unstep
                            now=fn(now,q)
                            reduced=fn(reduced,low)
            # Difference at or above digit m must never change lower
            # digit history at any of these times.
            for m in range(1,n):
                mask=1<<m
                higher_now=list(initial[0])
                higher_now[ORIGIN]=(higher_now[ORIGIN]+mask)%q
                pair=(tuple(higher_now),initial[1])
                require(project(pair,mask)==project(initial,mask), "same low source")
                a,b=initial,pair
                for t in range(17):
                    require(project(a,mask)==project(b,mask), "inert higher bit n=%d m=%d t=%d"%(n,m,t))
                    checks+=1
                    if t<16:
                        a=native_step(a,q)
                        b=native_step(b,q)
        if n>=2:
            lowq=2
            allzero=source(0,q)
            high_now=list(allzero[0])
            high_now[ORIGIN]=2
            higher=(tuple(high_now),allzero[1])
            require(project(higher,lowq)==project(allzero,lowq),"mutant prep low bits match")
            native_a=native_step(allzero,q)
            native_b=native_step(higher,q)
            mutant_a=native_step(allzero,q,True)
            mutant_b=native_step(higher,q,True)
            require(native_a[0][ORIGIN]%2==native_b[0][ORIGIN]%2,"native no higher->low")
            require(mutant_a[0][ORIGIN]%2 != mutant_b[0][ORIGIN]%2,"mutant visible witness")
            require(native_unstep(mutant_a,q,True)==allzero and native_unstep(mutant_b,q,True)==higher,"mutant reversible")
            checks+=4
        stages.append({"n":n,"q":q,"sites":N,"sources":12,
                       "lower_projections_tested":list(range(1,n)),
                       "forward_backward_horizon":16,
                       "modified_higher_to_lower_witness":n>=2,
                       "native_reversible":True})
    require(len(stages)==6,"all stages")
    return {"status":"PASS_NATIVE_CONGRUENCE_NO_BACKFLOW",
            "reference":"alpha=1 reference rule: six-neighbor cubic two-slice integer-coefficient wave equation of wave_eqn.c; substratum coefficient open",
            "dimension":3,"lattice_side":L,"sites":N,"controls":checks,
            "stages":stages,
            "all_state_theorem":"integer coefficients commute with ring reductions modulo 2^m; induction for all times",
            "non_native_positive_control":"fixed bit1-to-bit0 reversible source-site kick",
            "native_deeper_digit_can_change_low_bit":False,
            "general_nonlinear_padic_readouts_excluded":False,
            "native_Y_or_intervention_sourcing_derived":False,
            "quantum_operational_completion_derived":False,
            "Yang_Mills_action_derived":False}


if __name__=="__main__":
    print(json.dumps(run(),sort_keys=True,indent=2))
