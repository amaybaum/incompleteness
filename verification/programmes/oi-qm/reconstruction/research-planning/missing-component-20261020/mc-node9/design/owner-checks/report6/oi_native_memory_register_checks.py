#!/usr/bin/env python3
"""Exact native memory-register calibration. Standard library only.
Graph: memory 3 -- visible 0 -- hidden 1 -- visible 2.
One fixed binary lattice update, no controlled copy/swap or external history.
Initial core: uniform on all six bits. Memory: an independent affine subset
of its two bits. Read all current visible cells after a declared wait.
"""
from collections import defaultdict, Counter
from itertools import combinations
from fractions import Fraction as F
import json

def emit(k,x):print(k+' '+json.dumps(x,sort_keys=True))
def bits(s):return tuple(s>>i&1 for i in range(8))
def pack(xs):return sum(x<<i for i,x in enumerate(xs))
def native(s,coupled=True):
    a,b,c,d,e,f,q,p=bits(s)
    return pack((b^d^(q if coupled else 0),a^c^e,b^f,
                 a,b,c,p^(a if coupled else 0),q))
def visible(s):return tuple(bits(s)[i] for i in (0,2,3,5,6,7))
def hidden(s):return (bits(s)[1],bits(s)[4])
def rank2(rows):
    piv={}
    for row in rows:
        while row:
            j=row.bit_length()-1
            if j in piv:row^=piv[j]
            else:piv[j]=row;break
    return len(piv)
def rows_of(g):
    return [sum(((g[1<<j]>>i)&1)<<j for j in range(8)) for i in range(8)]
def powers(fn):
    ident=tuple(range(256));g=ident;out=[]
    while g not in out:
        out.append(g);g=tuple(fn(s) for s in g)
    assert g==ident
    return out
def apply_row(row,s):return (row&s).bit_count()%2
def pairing(s,t):
    pairs=[(0,3),(1,4),(2,5),(6,7)]
    return sum(((s>>a)&1)*((t>>b)&1)+((s>>b)&1)*((t>>a)&1)
               for a,b in pairs)%2

G=powers(native);D=powers(lambda s:native(s,False))
assert len(G)==10 and len(D)==8
assert sorted(G[1])==list(range(256))
for i in range(8):
    for j in range(8):
        assert pairing(G[1][1<<i],G[1][1<<j])==pairing(1<<i,1<<j)
emit('FIXED_NATIVE_PROTOCOL',{'graph_edges':[[0,1],[1,2],[0,3]],
 'visible_sites':[0,2,3],'hidden_site':1,'memory_site':3,
 'input_bit_order':['a=u0','b=u1','c=u2','d=v0','e=v1','f=v2','q=u3','p=v3'],
 'native_period':10,'binary_symplectic_pairing_preserved':True,
 'extra_copy_or_exchange_operations':0,'retained_external_history':False,
 'initial_core_distribution':'uniform on 64 configurations',
 'read':'current six visible coordinates after three updates'})

# Exhaust all nonempty affine subsets of F2^2: four points, six lines, full plane.
memstates=[(0,0),(0,1),(1,0),(1,1)]
menus=[tuple([x]) for x in memstates]+list(combinations(memstates,2))+[tuple(memstates)]
assert len(menus)==11
R=rows_of(G[3]);H=[R[i] for i in (0,2,3,5,6,7)];T=[R[1],R[4]]
assert rank2(H)==6
summary=Counter();branches=0
for menu in menus:
    known_rank=2-(len(menu).bit_length()-1)
    # Linear rows constant on this affine menu; offsets do not affect ranks.
    A=[]
    for z in [1,2,3]:
        vals={((z&1)*q+((z>>1)&1)*p)%2 for q,p in menu}
        if len(vals)==1:A.append(((z&1)<<6)|(((z>>1)&1)<<7))
    assert rank2(A)==known_rank
    assert rank2(A+H)==6+known_rank
    assert rank2(A+H+T)-rank2(A+H)==2-known_rank
    assert rank2(A+H+[1<<i for i in range(6)])-rank2(A+H)==2-known_rank
    fibers=defaultdict(list)
    for s in range(256):
        if bits(s)[6:] in menu:fibers[visible(G[3][s])].append(s)
    assert len(fibers)==64
    for rec,ss in fibers.items():
        assert len(ss)==len(menu)
        assert len({s%64 for s in ss})==len(menu)
        assert len({hidden(G[3][s]) for s in ss})==len(menu)
        # Explicit inverse parameterized only by the original memory (q,p).
        U0,U2,V0,V2,Q,P=rec
        decoded=[]
        for q,p in menu:
            d=U2^q;b=P^d;f=U0^P;c=V0^V2^p;e=Q^c;a=V2^e
            s=pack((a,b,c,d,e,f,q,p));decoded.append(s)
            assert hidden(G[3][s])==(V2^p,U0^q)
        assert sorted(decoded)==sorted(ss)
        branches+=1
    summary[known_rank]+=1
assert branches==704
emit('EXHAUSTIVE_AFFINE_MEMORY_MENUS',{'menus':11,
 'menus_by_known_relation_rank':dict(summary),'record_branches':branches,
 'each_menu_has_64_equiprobable_records':True,
 'conditional_support_both_initial_core_and_current_hidden':'2^(2-r)',
 'rank_formula':'rank[A;H;T]-rank[A;H] = 2-r',
 'r_0_unknown_pair_support':4,'r_1_known_coordinate_or_parity_support':2,
 'r_2_known_pair_support':1})

names={'known_pair':((0,0),),'known_Q':((0,0),(0,1)),
       'known_P':((0,0),(1,0)),'known_parity':((0,0),(1,1)),
       'unknown_pair':tuple(memstates)}
emit('NAMED_RESOURCE_CONTROLS',{k:{'memory_values':v,'remaining_hidden_support':len(v)}
                               for k,v in names.items()})

# General prior identity: every terminal record is uniform and independent of
# the original memory pair. The conditional hidden distribution is exactly
# that memory prior, with its two coordinates exchanged and shifted by record.
priors=[(F(1),F(0),F(0),F(0)),(F(1,2),F(1,2),F(0),F(0)),
        (F(3,4),F(1,4),F(0),F(0)),(F(1,2),F(0),F(0),F(1,2)),
        (F(1,10),F(2,10),F(3,10),F(4,10))]
for prior in priors:
    joint=defaultdict(lambda:defaultdict(F))
    for s in range(256):
        q,p=bits(s)[6:];w=prior[memstates.index((q,p))]/64
        joint[visible(G[3][s])][hidden(G[3][s])]+=w
    assert len(joint)==64
    for rec,post in joint.items():
        assert sum(post.values())==F(1,64)
        U0,U2,V0,V2,Q,P=rec
        for q,p in memstates:
            assert post[(V2^p,U0^q)]*64==prior[memstates.index((q,p))]
emit('GENERAL_MEMORY_PRIOR_IDENTITY',{
 'formula':'P(hidden=(h1,h2)|record)=mu(q=h2 XOR U0, p=h1 XOR V2)',
 'all_record_probabilities':'1/64','exact_nonuniform_prior_controls':len(priors),
 'record_branches_checked':64*len(priors),
 'entropy_identity':'H(current hidden | current record)=H(initial memory)',
 'full_support_biased_memory_example':['1/10','2/10','3/10','4/10'],
 'biased_example_best_guess_probability':'2/5',
 'uniform_full_support_best_guess_probability':'1/4',
 'support_rank_alone_does_not_quantify_nonuniform_information':True})

# Timing/retention: all cells keep evolving, including the memory.
timing=[]
for t,g in enumerate(G):
    fibers=defaultdict(list)
    for s in range(64):fibers[visible(g[s])].append(s)
    c={len({hidden(g[s]) for s in ss}) for ss in fibers.values()}
    assert len(c)==1
    initial_support={len({s%64 for s in ss}) for ss in fibers.values()}
    assert initial_support==c
    timing.append({'time':t,'visible_records':len(fibers),'hidden_support':next(iter(c))})
assert [x['hidden_support'] for x in timing]==[4,4,2,1,2,4,2,1,2,4]
emit('RECORD_RETENTION_WINDOWS',{'known_pair_timing':timing,
 'perfect_current_record_times_mod_10':[3,7],
 'permanent_record_without_further_control':False})

# Background subtraction: same elapsed time, coupling edge removed in control.
# Memory is still a native isolated site, swapping q,p at each step.
changes=[]
for t in range(4):
    changes.append(sum((G[t][s]&63)!=(D[t%8][s]&63) for s in range(64)))
assert changes[0]==changes[1]==0 and changes[2]>0 and changes[3]>0
for t,g in enumerate(D):
    fibers=defaultdict(list)
    for s in range(64):fibers[visible(g[s])].append(s)
    assert len(fibers)==16
    assert all(len({hidden(g[s]) for s in ss})==4 for ss in fibers.values())
emit('COUPLING_AND_BACKACTION_CONTROLS',{
 'core_states_differing_from_disconnected_control_times_0_to_3':changes,
 'control_core_inputs_checked':64,
 'disconnected_clean_memory_hidden_support_all_times':4,
 'background_subtraction':'identical elapsed native updates; only memory edge removed',
 'current_hidden_determination_is_not_only_overwrite':
 'the same record also reconstructs all six initial core bits'})

# Capacity: for an arbitrary six-bit initial core, four current core-visible
# bits and k additional final memory bits provide at most 2^(4+k) records.
assert 2**(4+1)<64 and 2**(4+2)==64
emit('CAPACITY_SCOPE',{'single_run_arbitrary_initial_core_requires_extra_record_bits_at_least':2,
 'construction_extra_memory_bits':2,
 'memory_cleanliness_lower_bound_is_not_inferred_from_this_count':True,
 'uniform_prior_entropy':'H(total)=8-r, H(visible)<=6, so H(hidden|visible)>=2-r',
 'all_branches_support_formula_scope':'uniform affine preparation and this linear protocol'})
emit('VERDICT',{'exact_checks':'PASS','native_memory_coupling_and_evolution':True,
 'clean_memory_preparation_sourced':False,'terminal_read_apparatus_derived':False,
 'future_postselected_preparation_after_read_backaction_derived':False,
 'new_C5_or_QM_reconstruction':False,'status':'exploratory calibration'})
