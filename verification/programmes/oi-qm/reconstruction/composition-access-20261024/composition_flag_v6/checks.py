#!/usr/bin/env python3
"""Exact reversible logical acceptance control; no native-gate availability claim."""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import product
import hashlib
import json

# Current V, then previous Q8,Q10,M,C0,C1,C2, in A/B/D order.
PHASE = 21
S, AA, BB, FLAG = 21, 22, 23, 24
SCRATCH = (25, 26, 27)
PA, PB, PD = 28, 29, 30
WIDTH = 31
S_INPUTS = (1, 5, 8, 11, 14, 17, 20)
Y, RSIGN, Z, K0, K1, K2 = 4, 8, 7, 3, 5, 6
WORK = tuple(range(21, 28))
H = (0, 2, 4, 7, 1, 3, 5, 6)
N = {(0, 0): 5, (0, 1): 0, (1, 0): 4, (1, 1): 1}

def need(value, message):
    if not value:
        raise RuntimeError(message)

def bit(value, i):
    return value >> i & 1

def component(value, i):
    return value >> (2-i) & 1

def gate(controls, target):
    need(len(set(controls)) == len(controls) and target not in controls,
         'invalid elementary gate')
    need(len(controls) <= 2, 'gate not elementary')
    return sum(1 << c for c in controls), 1 << target

def apply(state, instruction):
    controls, target = instruction
    return state ^ target if state & controls == controls else state

def multi(controls, target):
    if len(controls) <= 2:
        return [gate(tuple(controls), target)]
    need(len(controls) == 5, 'unregistered multi-control size')
    chain = [gate((controls[0], controls[1]), SCRATCH[0]),
             gate((SCRATCH[0], controls[2]), SCRATCH[1]),
             gate((SCRATCH[1], controls[3]), SCRATCH[2])]
    return chain + [gate((SCRATCH[2], controls[4]), target)] + list(reversed(chain))

def term(controls, negatives, target):
    flips = [gate((), c) for c in negatives]
    return flips + multi(controls, target) + list(reversed(flips))

def circuit():
    compute = [gate((c,), S) for c in S_INPUTS]
    compute += [gate((Y,), AA), gate((S,), AA),
                gate((RSIGN,), BB), gate((S,), BB)]
    # Three disjoint terms, independently compared with the integer threshold.
    compute += term((BB, K2), (BB, K2), FLAG)
    compute += term((AA, BB, K2, K1, K0), (AA, BB, K1, K0), FLAG)
    compute += term((AA, BB, K2, K1, K0), (K2, K1, K0), FLAG)
    return compute, compute + [gate((FLAG,), PB)] + list(reversed(compute))

COMPUTE, GATES = circuit()
COPY_TICK = len(COMPUTE) + 1

def pointer(state):
    return 4*bit(state, PA) + 2*bit(state, PB) + bit(state, PD)

def run(state, gates=GATES, trace=False):
    history = [pointer(state)] if trace else None
    for instruction in gates:
        state = apply(state, instruction)
        if trace:
            history.append(pointer(state))
    return (state, tuple(history)) if trace else state

def pack_phase(values):
    need(len(values) == 7, 'phase tuple shape')
    state = 0
    for offset, triple in enumerate(values):
        for c in range(3):
            state |= component(triple, c) << (3*offset+c)
    return state

def selected(state):
    s = 0
    for i in S_INPUTS:
        s ^= bit(state, i)
    return (s, bit(state, Y), bit(state, RSIGN), bit(state, Z))

def threshold(state):
    s, y, r, z = selected(state)
    k = bit(state, K0) + 2*bit(state, K1) + 4*bit(state, K2)
    return int(k < N[y ^ s, r ^ s])

def expected_history(accept, pads):
    p = 4*bit(pads, 1) + bit(pads, 0)
    return tuple(p + (2*accept if t >= COPY_TICK else 0)
                 for t in range(len(GATES)+1))

def determinant(counts):
    mass = sum(counts.values())
    need(mass > 0, 'empty state posterior')
    means = [sum(F(n, mass)*(1-2*j[i]) for j, n in counts.items())
             for i in (0, 1, 3)]
    return (1-sum(m*m for m in means))/4

def target_count(s, accept, j):
    if j[0] != s:
        return 0
    n = N[j[1] ^ s, j[2] ^ s]
    return n if accept else 8-n

def tv(a, b):
    return sum((abs(a.get(k, F())-b.get(k, F())) for k in a.keys() | b.keys()), F())/2

def elementary_controls():
    tables = inverse_states = 0
    bad_differences = 0
    for n in (2, 5):
        controls = tuple(range(n))
        target = 10
        instructions = multi(controls, target)
        for values in range(1 << (n+1)):
            state = sum(bit(values, i) << i for i in range(n)) | (bit(values, n) << target)
            wanted = state ^ ((1 << target) if values & ((1 << n)-1) == (1 << n)-1 else 0)
            actual = run(state, instructions)
            need(actual == wanted, 'multi-control decomposition truth table')
            tables += 1
            if n == 5:
                broken = run(state, instructions[1:])
                bad_differences += int(broken != wanted)
        active = controls + (target,) + (SCRATCH if n == 5 else ())
        for values in range(1 << len(active)):
            state = sum(bit(values, i) << wire for i, wire in enumerate(active))
            need(run(run(state, instructions), list(reversed(instructions))) == state,
                 'multi-control dirty inverse')
            inverse_states += 1
    need(bad_differences > 0, 'broken multi-control test vacuous')
    return tables, inverse_states, bad_differences

def truth_controls():
    relevant = sorted(set(S_INPUTS) | {Y, RSIGN, K0, K1, K2})
    need(all(not (target & ((1 << PA) | (1 << PD))) for controls, target in GATES),
         'padding wire unexpectedly changed')
    need(sum(target == (1 << PB) for controls, target in GATES) == 1,
         'pointer B not single-copy')
    outputs = 0
    for values in range(1 << len(relevant)):
        phase = sum(bit(values, i) << wire for i, wire in enumerate(relevant))
        actual, history = run(phase, trace=True)
        a = threshold(phase)
        need(bit(actual, PB) == a and (actual & ((1 << PHASE)-1)) == phase,
             'phase truth table')
        need(all(bit(actual, w) == 0 for w in WORK), 'workspace not restored')
        need(history == expected_history(a, 0), 'whole pointer prefix truth table')
        outputs += 1
    dirty_cases = 0
    mask = (1 << WIDTH)-1
    x = 0x5A17F23
    samples = [0, mask] + [1 << i for i in range(WIDTH)]
    for i in range(4096):
        x ^= x << 13
        x ^= x >> 17
        x ^= x << 5
        x &= mask
        samples.append(x)
    for state in samples:
        need(run(run(state), list(reversed(GATES))) == state, 'global dirty-register inverse')
        dirty_cases += 1
    padded_cases = 0
    for phase_seed, pads in product(range(32), range(4)):
        phase = ((phase_seed * 0x15A7B) ^ (phase_seed << 11)) & ((1 << PHASE)-1)
        state = phase | bit(pads, 1) << PA | bit(pads, 0) << PD
        actual, history = run(state, trace=True)
        need(history == expected_history(threshold(phase), pads), 'explicit padded pointer history')
        need(actual & ((1 << PHASE)-1) == phase, 'padded input restoration')
        padded_cases += 1
    return len(relevant), outputs, dirty_cases, padded_cases

def conditional_kernel():
    physical_worlds = padded_worlds = cells = positive = guards = rejected = 0
    key_negative = 0
    key_min = F()
    key_example = None
    workspace_min = F()
    missing_uncompute_dirty = 0
    phase_hash = hashlib.sha256()
    for old, complement in product(range(8), repeat=2):
        s = component(old, 1)
        counts = Counter()
        key_counts = defaultdict(Counter)
        work_counts = defaultdict(Counter)
        for q8, q10, m in product(range(8), repeat=3):
            v = old ^ H[q8 ^ q10 ^ m ^ complement]
            phase = pack_phase((v, q8, q10, m, complement, 0, 0))
            before = selected(phase)
            need(before == (s, component(q8,1), component(q10,2), component(q10,1)),
                 'actual phase operand identification')
            out, history = run(phase, trace=True)
            a = threshold(phase)
            need(bit(out, PB) == a and history == expected_history(a,0),
                 'kernel circuit flag/history')
            need(out & ((1 << PHASE)-1) == phase and all(bit(out,w) == 0 for w in WORK),
                 'kernel preservation')
            mid = run(phase, COMPUTE)
            no_uncompute = apply(mid, gate((FLAG,), PB))
            missing_uncompute_dirty += int(any(bit(no_uncompute, w) for w in WORK))
            if a:
                key_counts[v,m][before] += 1
                work_counts[bit(mid, AA)][before] += 1
            for pads in range(4):
                full_history = tuple(raw | 4*bit(pads,1) | bit(pads,0) for raw in history)
                need(full_history == expected_history(a,pads), 'complete padded prefix')
                counts[v,pads,a,before] += 1
                padded_worlds += 1
            phase_hash.update(bytes((old,complement,q8,q10,m,v,a)))
            physical_worlds += 1
        for v, pads, a, j in product(range(8), range(4), range(2), product(range(2), repeat=4)):
            wanted = target_count(s,a,j)
            need(counts[v,pads,a,j] == wanted, 'complete raw-prefix/flag/physical-carrier kernel')
            cells += 1
            if not a and wanted:
                rejected += 1
        if component(old,0) == 0:
            for v,pads in product(range(8),range(4)):
                law = {j:counts[v,pads,1,j] for j in product(range(2),repeat=4)
                       if counts[v,pads,1,j]}
                need(sum(law.values()) == 20 and determinant(law) == 0,
                     'accepted complete-record posterior not positive X')
                need(all(j[0] == s for j in law), 'accepted wrong X sign')
                positive += 1
            for key, law in key_counts.items():
                det = determinant(law)
                if det < 0:
                    key_negative += 1
                    if det < key_min:
                        key_min = det
                        key_example = {'old':old,'complement':complement,'V':key[0],
                                       'M':key[1],'determinant':str(det)}
            for exposed_a,law in work_counts.items():
                det = determinant(law)
                need(det < 0, 'workspace exposure countercontrol vacuous')
                workspace_min = min(workspace_min,det)
        # The old failure can coexist with every actual old triple. Successful
        # quantum offers are checked only on the stipulated A=0 old-triple sector.
        for oldflag in (0,1):
            if oldflag and component(old,0):
                continue
            offered = sum(n for (v,pads,a,j),n in counts.items() if oldflag and a)
            need(offered == (640 if oldflag else 0), 'old flag or offer mass')
            for (v,pads,a,j),n in counts.items():
                if not oldflag:
                    need(not (oldflag and a), 'old terminal failure revived')
            guards += 1
    need(key_negative > 0 and workspace_min < 0 and missing_uncompute_dirty > 0,
         'leak/reset countercontrol vacuous')
    return {'conditional_native_phase_worlds':physical_worlds,
            'whole_pointer_padding_worlds':padded_worlds,
            'full_kernel_cells_including_zeros':cells,
            'positive_accepted_whole_record_posteriors':positive,
            'rejected_physical_cells_retained':rejected,
            'valid_old_flag_contexts':guards,
            'key_exposure_negative_posteriors':key_negative,
            'key_exposure_min_determinant':str(key_min),
            'key_exposure_example':key_example,
            'workspace_a_exposure_min_determinant':str(workspace_min),
            'omitted_uncompute_dirty_worlds':missing_uncompute_dirty,
            'phase_kernel_sha256':phase_hash.hexdigest()}

def record_mutants():
    fresh = {(a,b):F(1,16) for a,b in product(range(4),repeat=2)}
    reused = {(a,a):F(1,4) for a in range(4)}
    reuse_tv = tv(fresh,reused)
    need(reuse_tv > 0, 'padding-reuse record control vacuous')
    flag_tv = []
    for s in (0,1):
        intended = defaultdict(F)
        fake = defaultdict(F)
        for q8,q10 in product(range(8),repeat=2):
            j=(s,component(q8,1),component(q10,2),component(q10,1))
            k=component(q8,0)+2*component(q8,2)+4*component(q10,0)
            a=int(k<N[j[1]^s,j[2]^s])
            intended[a,j if a else None] += F(1,64)
            for seed in range(16):
                f=int(seed<5)
                fake[f,j if f else None] += F(1,1024)
        need(sum(w for (a,j),w in intended.items() if a)==F(5,16), 'intended flag rate')
        need(sum(w for (a,j),w in fake.items() if a)==F(5,16), 'fake flag rate')
        d=tv(intended,fake)
        need(d>0, 'rate-only flag control vacuous')
        flag_tv.append(str(d))
    return {'two_operation_padding_reuse_full_record_tv':str(reuse_tv),
            'correct_rate_unrelated_flag_offered_kernel_tv':flag_tv,
            'padding_reuse_alone_claimed_to_leak_carrier':False,
            'omitted_uncompute_public_pointer_alone_detects_error':False}

def recording_dilation_controls():
    # Optional explicit storage of every one of the ninety logical raw triples.
    # Record wires are retained; no sample is erased or treated as a free register.
    expanded=[]
    for t in range(len(GATES)+1):
        for c,wire in enumerate((PA,PB,PD)):
            expanded.append(gate((wire,),WIDTH+3*t+c))
        if t<len(GATES):
            expanded.append(GATES[t])
    total_width=WIDTH+3*(len(GATES)+1)
    # Initial three recording CNOTs, then each core gate follows three recordings.
    expanded_copy_tick=4*COPY_TICK
    cases=0
    for phase_seed,pads in product(range(64),range(4)):
        phase=((phase_seed*0x15A7B)^(phase_seed<<11))&((1<<PHASE)-1)
        initial=phase|bit(pads,1)<<PA|bit(pads,0)<<PD
        out,history=run(initial,expanded,trace=True)
        wanted=expected_history(threshold(phase),pads)
        for t,raw in enumerate(wanted):
            actual=4*bit(out,WIDTH+3*t)+2*bit(out,WIDTH+3*t+1)+bit(out,WIDTH+3*t+2)
            need(actual==raw,'explicit retained raw recording bank')
        pad_raw=4*bit(pads,1)+bit(pads,0)
        need(history==tuple(pad_raw+(2*threshold(phase) if t>=expanded_copy_tick else 0)
                            for t in range(len(expanded)+1)),
             'full pointer prefix during recording dilation')
        need(run(out,list(reversed(expanded)))==initial,'recording dilation inverse')
        need(all(bit(out,w)==0 for w in WORK),'recording dilation dirty temporary')
        cases+=1
    need(all(0<=wire.bit_length()-1<total_width for controls,wire in expanded),
         'recording-bank width')
    kinds=Counter(controls.bit_count() for controls,target in expanded)
    return {'additional_initially_clean_record_bits':total_width-WIDTH,
            'total_register_bits_including_raw_record_bank':total_width,
            'total_elementary_ticks':len(expanded),
            'complete_pointer_prefix_samples_including_record_copy_ticks':len(expanded)+1,
            'flag_copy_tick':expanded_copy_tick,
            'CNOT':kinds[1],'NOT':kinds[0],'Toffoli':kinds[2],
            'complete_recording_and_inverse_control_rows':cases,
            'autonomous_native_clock_constructed':False}

def neighbors(p):
    for axis in range(3):
        for delta in (-1,1):
            q=list(p)
            q[axis]+=delta
            yield tuple(q)

def native_step(previous,current):
    points=set(previous)
    for p in current:
        points.update(neighbors(p))
    out={}
    for p in points:
        parity=0
        for q in neighbors(p):
            parity^=current.get(q,0)
        value=previous.get(p,0)^H[parity]
        if value:
            out[p]=value
    return out

def delay_control():
    q=(0,0,0)
    ports=((0,0,-1),(0,0,1),(-1,0,0),(1,0,0),(0,-1,0),(0,1,0))
    source=((0,0,0),(-1,0,-1),(-1,0,1),(-2,0,0))
    cases=wrong_sign=wrong_pool=0
    for old,left,right,mask in product(range(8),repeat=4):
        initial={p:v for p,v in zip(source,(old,left,right,mask)) if v}
        first=native_step({},initial)
        second=native_step(initial,first)
        third=native_step(first,second)
        phase2=pack_phase((second.get(q,0),*(first.get(p,0) for p in ports)))
        phase3=pack_phase((third.get(q,0),*(second.get(p,0) for p in ports)))
        need(selected(phase2)[0]==component(old,1), 'two-tick source sign control')
        delayed=selected(phase3)
        need(delayed==(0,0,0,0), 'three-tick scoped source response')
        wrong_sign+=int(delayed[0] != selected(phase2)[0])
        wrong_pool+=int(delayed[1:] != selected(phase2)[1:])
        cases+=1
    need(wrong_sign>0 and wrong_pool>0,'uncontrolled delay control vacuous')
    return {'small_source_worlds':cases,'unchanged_phase_decoder_wrong_sign_worlds':wrong_sign,
            'unchanged_phase_decoder_changed_pool_worlds':wrong_pool,
            'actual_L_delay_simulated':False,
            'scope':'one additional full native tick in the retained two-tick small-source control'}

def main():
    for value in range(8):
        a,b,d=(component(value,i) for i in range(3))
        need(H[value]==4*b+2*d+(a^(b&d)), 'H scalar Boolean definition')
    decomposition=elementary_controls()
    truth=truth_controls()
    kernel=conditional_kernel()
    mutants=record_mutants()
    delay=delay_control()
    recording=recording_dilation_controls()
    kinds=Counter(controls.bit_count() for controls,target in GATES)
    result={'schema':'oi-reversible-acceptance-composition-v6.1',
            'scope':'logical reversible circuit on the actual distributed phase representation',
            'native_H_gate_compilation_established':False,
            'native_operand_preservation_through_delay_established':False,
            'observer_access_rule_adopted':False,
            'phase_input_bits':PHASE,'clean_workspace_bits':len(WORK),
            'clean_public_flag_bits':1,'initial_fair_public_padding_bits':2,
            'logical_register_bits':WIDTH,'fixed_elementary_gate_ticks':len(GATES),
            'copy_tick':COPY_TICK,'whole_pointer_prefix_samples_including_initial':len(GATES)+1,
            'gates':{'NOT':kinds[0],'CNOT':kinds[1],'Toffoli':kinds[2]},
            'global_inverse':'reverse the listed elementary involutions on all register states',
            'multi_control_truth_rows':decomposition[0],
            'multi_control_dirty_inverse_rows':decomposition[1],
            'broken_decomposition_changed_rows':decomposition[2],
            'relevant_phase_bits_exhausted':truth[0],'complete_boolean_truth_rows':truth[1],
            'dirty_register_inverse_control_rows':truth[2],
            'explicit_four_padding_trace_rows':truth[3],
            'conditional_kernel':kernel,'record_and_workspace_mutants':mutants,
            'uncontrolled_native_delay_countercontrol':delay,
            'optional_complete_raw_recording_dilation':recording,
            'all_required_controls_pass':True}
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
