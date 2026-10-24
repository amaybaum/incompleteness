#!/usr/bin/env python3
"""Read-only OI handoff: exact calibrations and a bounded reversible compiler.
Standard library only. Quantum update rules are explicitly programmed.
No claim of autonomous lattice realization or derivation of those rules.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import permutations, product
from math import comb
import hashlib
import json

def emit(name, value):
    print(name + ' ' + json.dumps(value, sort_keys=True))

class Circuit:
    """Boolean expression compiler; each nontrivial node gets clean workspace.
    Wire indices are integers; Boolean constants are Python bools.
    Primitives are tuples (target,), (control,target), (c1,c2,target).
    Every primitive is a classical reversible NOT, CNOT, or Toffoli.
    """
    def __init__(self, inputs):
        self.nin = self.n = inputs
        self.gates = []
        self.cache = {}
    def fresh(self):
        q = self.n
        self.n += 1
        return q
    def inv(self, a):
        if type(a) is bool: return not a
        key = ('not', a)
        if key not in self.cache:
            t = self.fresh()
            self.gates.extend([(a,t),(t,)])
            self.cache[key] = t
        return self.cache[key]
    def xor(self, a, b):
        if type(a) is bool: return self.inv(b) if a else b
        if type(b) is bool: return self.inv(a) if b else a
        if a == b: return False
        key = ('xor', min(a,b), max(a,b))
        if key not in self.cache:
            t = self.fresh()
            self.gates.extend([(a,t),(b,t)])
            self.cache[key] = t
        return self.cache[key]
    def land(self, a, b):
        if type(a) is bool: return b if a else False
        if type(b) is bool: return a if b else False
        if a == b: return a
        key = ('and', min(a,b), max(a,b))
        if key not in self.cache:
            t = self.fresh()
            self.gates.append((a,b,t))
            self.cache[key] = t
        return self.cache[key]
    def mux(self, c, yes, no):
        return self.xor(no,self.land(c,self.xor(yes,no)))
    def add(self,a,b,carry=False):
        assert len(a)==len(b)
        out=[]
        for x,y in zip(a,b):
            s=self.xor(x,y)
            out.append(self.xor(s,carry))
            carry=self.xor(self.land(x,y),self.land(s,carry))
        return out,carry
    def neg(self,a):
        return self.add([self.inv(x) for x in a],[False]*len(a),True)[0]
    def sub(self,a,b):
        return self.add(a,[self.inv(x) for x in b],True)
    def square(self,a):
        # Absolute value, then ordinary unsigned schoolbook multiplication.
        mag=[self.mux(a[-1],x,y) for x,y in zip(self.neg(a),a)]
        w=len(a); out=[False]*(2*w)
        for i,b in enumerate(mag):
            row=[False]*i+[self.land(x,b) for x in mag]+[False]*(w-i)
            out=self.add(out,row)[0]
        return out
    def finish(self, values):
        work_end=self.n
        outputs=[self.fresh() for _ in values]
        copy=[]
        for v,t in zip(values,outputs):
            if type(v) is bool:
                if v: copy.append((t,))
            else: copy.append((v,t))
        forward=list(self.gates)
        gates=forward+copy+list(reversed(forward))
        assert all(len(set(g))==len(g) for g in gates)
        return gates,outputs,work_end,forward,copy

def bits(x,w): return [(x>>i)&1 for i in range(w)]
def integer(a): return sum(x<<i for i,x in enumerate(a))
def apply(gates,state):
    for g in gates:
        if len(g)==1: state[g[0]]^=1
        elif len(g)==2: state[g[1]]^=state[g[0]]
        else: state[g[2]]^=state[g[0]]&state[g[1]]

def compile_demo():
    # 3-bit signed x,y; one intervention bit z; 8-bit residual seed j.
    c=Circuit(15)
    x=list(range(3))+[2,2]
    y=list(range(3,6))+[5,5]
    z=6; j=list(range(7,15))+[False,False]
    a=c.add(x,y)[0]; b=c.sub(x,y)[0]  # unnormalized H
    b=[c.mux(z,u,v) for u,v in zip(c.neg(b),b)]
    a,b=c.add(a,b)[0],c.sub(a,b)[0]  # second unnormalized H
    width=c.square(a)
    residual,ge=c.sub(j,width)  # carry-out means j>=width
    residual=[c.mux(ge,u,v) for u,v in zip(residual,j)]
    post0=[c.land(c.inv(ge),v) for v in a]
    post1=[c.land(ge,v) for v in b]
    values=a+b+[ge]+residual+post0+post1
    return c,c.finish(values)

c,(gates,outputs,wend,forward,copy)=compile_demo()
def reference(x,y,z,j):
    a,b=x+y,x-y
    if z: b=-b
    a,b=a+b,a-b
    r=int(j>=a*a)
    jr=j-r*a*a
    return bits(a,5)+bits(b,5)+[r]+bits(jr,10)+bits(a if not r else 0,5)+bits(b if r else 0,5)

tested=0; xor_tested=0; mutation_witness=None
removed=next(i for i,g in enumerate(forward) if len(g)==3)
bad_forward=forward[:removed]+forward[removed+1:]
# Paired deletion preserves reversibility but changes the computed function.
bad_gates=bad_forward+copy+list(reversed(bad_forward))
unclear_witness=None
for x,y,z in product(range(-4,4),range(-4,4),range(2)):
    if x==y==0: continue
    norm=4*(x*x+y*y)
    for j in range(norm):
        initial=bits(x,3)+bits(y,3)+[z]+bits(j,8)
        state=initial+[0]*(c.n-c.nin)
        apply(gates,state)
        expect=reference(x,y,z,j)
        assert state[:c.nin]==initial
        assert not any(state[c.nin:wend])
        assert [state[q] for q in outputs]==expect,(x,y,z,j)
        tested+=1
        # Nonzero output destination tests XOR-oracle behavior, not overwrite.
        if j==0:
            mask=[(i+x+y+z)%2 for i in range(len(outputs))]
            state2=initial+[0]*(c.n-c.nin)
            for q,v in zip(outputs,mask): state2[q]=v
            apply(gates,state2)
            assert [state2[q] for q in outputs]==[a^b for a,b in zip(mask,expect)]
            assert not any(state2[c.nin:wend])
            xor_tested+=1
        if mutation_witness is None:
            bad=initial+[0]*(c.n-c.nin); apply(bad_gates,bad)
            if [bad[q] for q in outputs]!=expect:
                mutation_witness={'x':x,'y':y,'z':z,'seed':j,'removed_forward_gate':removed}
        if unclear_witness is None:
            dirty=initial+[0]*(c.n-c.nin); apply(forward+copy,dirty)
            if any(dirty[c.nin:wend]):
                unclear_witness={'x':x,'y':y,'z':z,'seed':j,'dirty_workspace_bits':sum(dirty[c.nin:wend])}
assert mutation_witness is not None and unclear_witness is not None
gate_counts=Counter({{1:'NOT',2:'CNOT',3:'Toffoli'}[k]:v for k,v in Counter(map(len,gates)).items()})
digest=hashlib.sha256(json.dumps(gates,separators=(',',':')).encode()).hexdigest()
emit('REVERSIBLE_COMPILER',{'admissible_inputs':tested,'nonzero_output_targets':xor_tested,
 'input_bits':c.nin,'workspace_clean_bits':wend-c.nin,'output_bits':len(outputs),
 'total_data_bits':c.n,'gates':dict(gate_counts),'gate_total':len(gates),
 'serial_schedule_positions':len(gates)+1,'explicit_clock_index_bits':len(gates).bit_length(),
 'naive_program_word_bits':2+3*(c.n-1).bit_length(),
 'naive_program_table_bits':len(gates)*(2+3*(c.n-1).bit_length()),
 'gate_list_sha256':digest,'carry_mutant_detected':mutation_witness,
 'omitted_uncompute_detected':unclear_witness})
for z in (0,1):
    out=Counter()
    for j in range(4):
        state=bits(1,3)+bits(0,3)+[z]+bits(j,8)+[0]*(c.n-c.nin)
        apply(gates,state); out[state[outputs[10]]]+=1
    assert out=={z:4}
    emit('COMPILED_HZH_'+str(z),dict(out))

# A fixed, autonomous GLOBAL permutation, with a programmed schedule in its
# transition rule. This supplies abstract clocking, not a local lattice controller.
# One terminal idle phase allows the output to be inspected at a named phase.
period=len(gates)+1
clock_bits=(period-1).bit_length()
def clocked_step(clock,state,backward=False):
    if clock>=period:return clock  # unused binary clock words are fixed
    if backward:
        clock=(clock-1)%period
        if clock<len(gates):apply([gates[clock]],state)
        return clock
    if clock<len(gates):apply([gates[clock]],state)
    return (clock+1)%period
for phase in range(1<<clock_bits):
    data=[((i*17+phase*13)^(i//3))&1 for i in range(c.n)]
    before=data[:]
    afterclock=clocked_step(phase,data)
    restoredclock=clocked_step(afterclock,data,True)
    assert restoredclock==phase and data==before
for z in (0,1):
    for seed in range(4):
        data=bits(1,3)+bits(0,3)+[z]+bits(seed,8)+[0]*(c.n-c.nin)
        before=data[:]; clock=0
        for _ in range(len(gates)):clock=clocked_step(clock,data)
        assert clock==len(gates) and data[outputs[10]]==z
        terminal=data[:]
        clock=clocked_step(clock,data)
        assert clock==0 and data==terminal
        # A second full cycle restores the XOR output, rather than halting.
        for _ in range(period):clock=clocked_step(clock,data)
        assert clock==0 and data==before
emit('AUTONOMOUS_GLOBAL_PERMUTATION',{'clock_bits':clock_bits,
 'clock_words_inverse_checked':1<<clock_bits,'complete_basis_runs':8,
 'data_plus_clock_bits':c.n+clock_bits,'terminal_phase':len(gates),
 'local_lattice_controller_built':False,'absorbing_halt':False,
 'next_cycle_erases_XOR_output':True})

# The SAME compiler can implement a PR-box response table. This is a selection
# countercontrol, not a claimed spatially local model or C1-C4 witness.
# Inputs are x,y,r with one initial fair r independent of both settings.
pr=Circuit(3)
prvalues=[2,pr.xor(2,pr.land(0,1))]
prg,pro,prwend,_,_=pr.finish(prvalues)
table={}; correlations={}
for x,y in product(range(2),repeat=2):
    outcomes=Counter()
    for r in range(2):
        initial=[x,y,r]; data=initial+[0]*(pr.n-pr.nin)
        apply(prg,data)
        assert data[:3]==initial and not any(data[3:prwend])
        a,b=(data[q] for q in pro)
        assert (a^b)==x*y
        outcomes[(a,b)]+=1
    assert all(sum(n for ab,n in outcomes.items() if ab[k]==0)==1 for k in (0,1))
    table[str(x)+str(y)]={str(a)+str(b):n for (a,b),n in sorted(outcomes.items())}
    correlations[(x,y)]=sum((1 if a==b else -1)*n for (a,b),n in outcomes.items())//2
chsh=correlations[0,0]+correlations[0,1]+correlations[1,0]-correlations[1,1]
assert chsh==4
emit('SAME_COMPILER_PR_COUNTERCONTROL',{'gates':len(prg),'data_bits':pr.n,
 'CHSH':chsh,'each_local_marginal_uniform':True,'table_counts_out_of_2':table,
 'uses_global_settings':True,'C1_C4_witness_claimed':False})

# Full-state Gaussian-integer interpreter, not the compiled one-qubit circuit.
class Machine:
    def __init__(self,n,budget,seed):
        self.n=n; self.B=budget; self.h=0; self.j=seed
        self.a=[(0,0)]*(1<<n); self.a[0]=(1,0); self.records=[]
        self.valid()
    def valid(self):
        assert self.h<=self.B
        assert 0<=self.j<sum(x*x+y*y for x,y in self.a)*(1<<(self.B-self.h))
    def H(self,q):
        m=1<<(self.n-1-q); old=self.a[:]
        for i in range(len(old)):
            if not i&m:
                x,y=old[i],old[i|m]
                self.a[i]=(x[0]+y[0],x[1]+y[1])
                self.a[i|m]=(x[0]-y[0],x[1]-y[1])
        self.h+=1; self.valid()
    def S(self,q):
        m=1<<(self.n-1-q)
        self.a=[(-y,x) if i&m else (x,y) for i,(x,y) in enumerate(self.a)]
        self.valid()
    def flip(self,controls,target):
        masks=[1<<(self.n-1-q) for q in controls]; t=1<<(self.n-1-target)
        out=[None]*len(self.a)
        for i,a in enumerate(self.a): out[i^t if all(i&m for m in masks) else i]=a
        self.a=out; self.valid()
    def read(self,q):
        mask=1<<(self.n-1-q)
        width=sum(x*x+y*y for i,(x,y) in enumerate(self.a) if not i&mask)*(1<<(self.B-self.h))
        r=int(self.j>=width)
        if r:self.j-=width
        self.a=[a if bool(i&mask)==bool(r) else (0,0) for i,a in enumerate(self.a)]
        self.records.append(r); self.valid(); return r

def prepare(seed,budget=6):
    t=Machine(6,budget,seed)
    for q in (0,1,2): t.H(q)
    t.flip([0],3); t.flip([1,2],3)
    t.flip([0,1],4); t.flip([4,2],5); t.flip([0,1],4)
    if t.read(5): return 'reject-flag'
    for q in (0,1,2): t.H(q)
    for q in (0,1,2):
        if t.read(q): return 'reject-address'
    return 'success-'+str(t.read(3))
prep=Counter(prepare(j) for j in range(64))
assert prep=={'reject-flag':8,'reject-address':31,'success-0':9,'success-1':16}
assert all(prepare(2*j+d,7)==prepare(j,6) for j in range(64) for d in range(2))
emit('BINARY_SEED_PREPARATION',dict(prep))
emit('BUDGET_COMPATIBILITY',{'refinements_checked':128,'all_record_labels_match':True})

for setting in ('XZ','ZX'):
    counts=Counter()
    for j in range(8):
        t=Machine(2,3,j); t.H(0); t.flip([0],1); t.H(0)
        t.H(0 if setting=='XZ' else 1)
        counts[''.join(str(t.read(q)) for q in range(2))]+=1
    assert counts=={'00':4,'11':4}
    emit('GRAPH_STATE_'+setting,dict(counts))

# Derive the retained-work control by summing the amplitudes in each branch,
# independently of the seed-counting interpreter. Tuples are (a,b,c,t,w,f).
def preparation_gram(uncompute=True,dephase=False):
    vectors=Counter()
    for a,b,c in product(range(2),repeat=3):
        t=a^(b&c); w=a&b; f=w&c
        if uncompute:w^=a&b
        if f:continue
        # Projection onto X+++ contributes the same positive amplitude from
        # each address. A retained orthogonal address prevents their addition.
        env=(w,a,b,c) if dephase else (w,)
        vectors[(env,t)]+=1
    envs={key[0] for key in vectors}
    return [[sum(vectors[(e,i)]*vectors[(e,j)] for e in envs) for j in range(2)] for i in range(2)]
good=preparation_gram(); dirty=preparation_gram(False); dephased=preparation_gram(True,True)
assert good==[[9,12],[12,16]] and dirty==[[9,9],[9,10]] and dephased==[[3,0],[0,4]]
assert sum(dirty[i][j]*dirty[j][i] for i in range(2) for j in range(2))==343
emit('PREPARATION_CONTROLS',{'correct_success':'25/64','uncomputed_target_density_numerator':good,
 'omit_work_uncompute_success':'19/64','omit_work_density_numerator':dirty,
 'omit_work_purity':'343/361','dephase_address_success':'7/64','dephase_target':['3/7','4/7']})

# Injection: exact matrices without sqrt(2) normalization.
Rnum=[[3,-4],[4,3]]; Rinv=[[3,4],[-4,3]]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
assert mm(Rnum,Rinv)==[[25,0],[0,25]]
J=[[0,-1],[1,0]]
I=[[1,0],[0,1]]
for sign,expected in ((1,Rnum),(-1,Rinv)):
    assert [[3*I[i][j]+sign*4*J[i][j] for j in range(2)] for i in range(2)]==expected
choi=[3,-4,4,3]
assert sum(x*x for x in choi)==50
assert [[sum(choi[2*i+b]*choi[2*j+b] for b in range(2)) for j in range(2)] for i in range(2)]==[[25,0],[0,25]]
emit('INJECTION_MATRIX',{'branch_probability':'1/2','correct_branch':'R','other_branch':'R_inverse','prepared_resource_plus_correct_injection':'25/128','Choi_integer_vector':choi})
walk={0:1}; successes=0
for n in range(1,256):
    nxt=Counter()
    successes*=2
    for x,count in walk.items():
        for d in (-1,1):
            if x+d==1: successes+=count
            else:nxt[x+d]+=count
    walk=nxt
    assert sum(walk.values())==comb(n,n//2)
    assert successes+sum(walk.values())==2**n
emit('INJECTION_RANDOM_WALK',{'steps_checked':255,'failure_formula':'binom(N,floor(N/2))/2^N','finite_mean_hitting_time':False})

# Local nonlinear primitive: exact 64-input Toffoli decomposition.
def lattice(s):
    u0,u1,u2,v0,v1,v2=s
    return (v0^u1^u2^(u1&u2),v1^u0,v2^u0,u0,u1,u2)
def inverse(s):
    U0,U1,U2,V0,V1,V2=s
    return (V0,V1,V2,U0^V1^V2^(V1&V2),U1^V0,U2^V0)
for s in product(range(2),repeat=6):
    assert inverse(lattice(s))==s
    t=lattice(s); u=t[3:]; v=t[:3]
    result=tuple(u)+(v[0]^u[1]^u[2],v[1]^u[0],v[2]^u[0])
    want=list(s); want[3]^=s[1]&s[2]
    assert result==tuple(want)
emit('LATTICE_PRIMITIVE',{'bijection_and_Toffoli_inputs':64,'additional_controls':'pair swaps, linear shear correction, addressing/timing NOT supplied'})
histories=[]
for b in (0,1):
    s=(b,0,0,0,0,0); history=[s]
    for _ in range(4):s=lattice(s);history.append(s)
    histories.append(history)
assert histories[0][3][0]==histories[1][3][0]==0
assert histories[0][3][3]==histories[1][3][3]==0
assert [h[2][4] for h in histories]==[0,1]
assert [h[3][1] for h in histories]==[0,1]
assert [h[4][0] for h in histories]==[0,1]
emit('SEPARATE_HIDDEN_READBACK_WITNESS',{'visible_at_t3':[0,0],'next_visible_u_equals_initial_bit':True,'structural_memory_retained':True,'slow_memory_not_tested':True,'same_witness_as_quantum_compiler':False})

card_vertices=[(0,1),(1,0),(-1,0),(0,-1)]
assert all(x1*z2+z1*x2<=1 for x1,z1 in card_vertices for x2,z2 in card_vertices)
emit('PRODUCT_CARD_CONTROL',{'product_vertices':16,'XZ_plus_ZX_upper_bound':1,'graph_state_value':2,'scope':'affine mixtures of products of the declared card vertices'})

# Diagonal-record no-go calibration with coherent ancilla (3,4)/5.
plus=[3,4,3,4]; minus=[3,4,-3,-4]
cnt=0
for p in permutations(range(4)):
    for mask in range(16):
        assert sum(plus[p[i]]**2 for i in range(4) if mask>>i&1)==sum(minus[p[i]]**2 for i in range(4) if mask>>i&1)
        cnt+=1
emit('DIAGONAL_RECORD_CONTROL',{'permutation_event_pairs':cnt,'worst_input_H_then_Z_error_lower_bound':'1/2'})

# Stabilizer-octahedron exact closest point and readout gap.
dx=F(24,25)-F(21,25); dz=-F(7,25)+F(4,25)
assert (dx*dx+dz*dz)/4==F(9,1250)
assert F(49,50)-F(9,25)-F(1,2)==F(3,25)
emit('STABILIZER_BARRIER',{'trace_distance_squared':'9/1250','worst_of_XZ_probability_error':'3/50'})
emit('PASS',{'scope':'bounded reversible circuit plus explicitly programmed quantum calibrations; no OI equivalence theorem'})
