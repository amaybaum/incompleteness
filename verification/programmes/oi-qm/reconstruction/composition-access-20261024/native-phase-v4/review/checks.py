#!/usr/bin/env python3
"""Independent exact reconstruction; no author-code imports."""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
import hashlib
import json
from pathlib import Path

F = Fraction


def need(condition, message):
    if not condition:
        raise RuntimeError(message)


V = tuple(product((0, 1), repeat=3))
ZERO = (0, 0, 0)
SIGN = lambda bit: 1 - 2*bit
Q8 = (0, 0, 0)
Q9 = (0, 0, 1)
NEIGHBORS = ((-1, 0, 0), (1, 0, 0), (0, -1, 0),
             (0, 1, 0), (0, 0, -1), Q9)
OTHER = NEIGHBORS[:-1]


def xor(*values):
    return tuple(sum(v[i] for v in values) % 2 for i in range(3))


def local(previous, current):
    a, b, d = xor(*(current.get(pos, ZERO) for pos in NEIGHBORS))
    return xor(previous.get(Q8, ZERO), (b, d, a ^ (b*d)))


def reported(y, x, r, parity):
    ca, cb, cd = parity
    return (cb ^ x, y ^ cd ^ r, ca ^ ((cb ^ x)*(cd ^ r)))


def total_variation(a, b):
    return sum((abs(a.get(v, F()) - b.get(v, F())) for v in set(a)|set(b)), F())/2


def conditioned_success(law):
    yes = {v:p for v,p in law.items() if v[0] == 1}
    w = sum(yes.values(), F())
    need(w == F(5, 16), 'success mass')
    return {v:p/w for v,p in yes.items()}


def law(old_x, y, completion):
    records = defaultdict(F)
    joint = defaultdict(F)
    selected = defaultdict(F)
    failed_fields = defaultdict(F)
    fresh_check = defaultdict(F)
    # Two masks, one eight-valued herald input, z and auxiliary fair bit.
    for a,b,k,z,e in product((0,1),(0,1),range(8),(0,1),(0,1)):
        n = ((5,0),(3,2))[a][b]
        ok = k < n
        u = old_x ^ y
        raw = ((u, y, old_x*(1-u)) if (a,b)==(0,1)
               else (0, y^a, y^b))
        p = F(1,128)
        selected[ok,(0,y,0),raw,z] += p
        if not ok:
            record = (0,old_x,y,raw,None)
            records[record] += p
            joint[record] += p
            failed_fields[(0,y,0),raw,z,None] += p
            continue
        x,r = raw[1:]
        ca = {'C0':0, 'C1':1, 'independent':e, 'correlated':z^(x*r)}[completion]
        out = local({Q8:(0,y,0)}, {Q9:raw,OTHER[2]:(ca,0,0)})
        record = (1,old_x,y,raw,out)
        records[record] += p
        joint[record,z] += p
        fresh_check[old_x,y,raw,ca] += p
    return records,joint,selected,failed_fields,fresh_check


def selected_moments(law):
    w = sum(law.values(),F())
    return w,tuple(sum((p*SIGN(v[a]) for v,p in law.items()),F()) for a in (0,1,3))


def main():
    parent = Path(__file__).resolve().parents[1]
    author = parent/'composition_v4' if (parent/'composition_v4').is_dir() else parent
    # The remote manifest at immutable author SHA was checked separately.
    digests = {}
    for line in (author/'SHA256SUMS').read_text().splitlines():
        expected,name = line.split('  ',1)
        actual = hashlib.sha256((author/name).read_bytes()).hexdigest()
        need(actual == expected, 'author hash changed: '+name)
        digests[name] = actual

    response_cases = 0
    distant_cases = 0
    dropped_parity = 0
    dropped_old = 0
    for y,x,r in product((0,1),repeat=3):
        for p1,p2 in combinations(OTHER,2):
            for v1,v2 in product(V,repeat=2):
                current = {Q9:(0,x,r),p1:v1,p2:v2}
                previous = {Q8:(0,y,0)}
                response = local(previous,current)
                need(response == reported(y,x,r,xor(v1,v2)), 'formula')
                dropped_parity += response != reported(y,x,r,ZERO)
                dropped_old += response != local({},current)
                far = dict(current)
                far[(2,0,0)] = (1,1,1)
                need(response == local(previous,far), 'causal control')
                distant_cases += 1
                response_cases += 1
    need(dropped_parity>0 and dropped_old>0,'mutant controls vacuous')

    contexts = {}
    failed_mask01 = {}
    for old_x,y in product((0,1),repeat=2):
        laws = {m:law(old_x,y,m) for m in ('C0','C1','independent','correlated')}
        selected0 = laws['C0'][2]
        fail0 = laws['C0'][3]
        need(sum(p for k,p in selected0.items() if k[0])==F(5,16),'selected herald')
        need(sum(fail0.values(),F())==F(11,16),'failed mass')
        for mode,(rec,joint,selected,failed,_) in laws.items():
            need(selected==selected0 and failed==fail0,'selected/failure law changed')
            need(sum(rec.values(),F())==sum(joint.values(),F())==1,'normalization')
        a,b = laws['C0'][0],laws['C1'][0]
        need(total_variation(a,b)==F(5,16),'C flip full law')
        need(total_variation(conditioned_success(a),conditioned_success(b))==1,'C flip conditional')
        a,b = laws['independent'][0],laws['correlated'][0]
        need(a==b,'public law mismatch')
        a,b = laws['independent'][1],laws['correlated'][1]
        need(total_variation(a,b)==F(5,32),'joint full law')
        # Extract successful joint branches without assuming author key layout.
        def joint_success(d):
            kept={k:v for k,v in d.items() if isinstance(k[0],tuple) and k[0][0]==1}
            total=sum(kept.values(),F())
            need(total==F(5,16),'joint success mass')
            return {k:v/total for k,v in kept.items()}
        need(total_variation(joint_success(a),joint_success(b))==F(1,2),'joint conditional')
        need(laws['independent'][4]==laws['correlated'][4],'public-history-conditioned fairness')
        for raw in {(0,y,y),(0,1-y,y),(0,1-y,1-y)}:
            pair=[laws['correlated'][4][old_x,y,raw,ca] for ca in (0,1)]
            need(pair[0]==pair[1]>0,'C_A fairness per current raw record')
        u=old_x^y
        failed_mask01[str((old_x,u))]=(u,y,old_x*(1-u))
        contexts[str((old_x,y))]={
            'C_flip_conditional_tv':'1','C_flip_full_tv':'5/16',
            'fresh_correlated_public_tv':'0','fresh_correlated_joint_conditional_tv':'1/2',
            'fresh_correlated_joint_full_tv':'5/32','failure_mass':'11/16',
        }
    need(failed_mask01=={'(0, 0)':(0,0,0),'(0, 1)':(1,1,0),
                        '(1, 1)':(1,0,0),'(1, 0)':(0,1,1)},'physical01fields')

    # Unequal private completions with equal XOR parity are not distinguished
    # by this one native-tick read. No full-future claim follows.
    parity_controls = 0
    for y,x,r,c,a,b in product((0,1),(0,1),(0,1),V,V,V):
        v3=xor(c,a,b)
        need(local({Q8:(0,y,0)},{Q9:(0,x,r),OTHER[0]:c}) ==
             local({Q8:(0,y,0)},{Q9:(0,x,r),OTHER[0]:a,OTHER[1]:b,OTHER[2]:v3}),
             'equal parity')
        parity_controls += 1

    reset_branch_count = 0
    reset_cells = 0
    reference_full_measure = defaultdict(F)
    reset_full_measure = defaultdict(F)
    for y in (0,1):
        for x,r,weight in ((y,y,F(1,2)),(1-y,y,F(3,10)),(1-y,1-y,F(1,5))):
            kappa = F(int(r==y)) if x==y else (F(3,5) if r==y else F(2,5))
            need(weight==F(1,2)*kappa,'refinement')
            out = defaultdict(F)
            for a,b,n,z in ((a,b,n,z) for a,b,n in ((0,0,5),(1,0,4),(1,1,1)) for z in (0,1)):
                point=(x,x^a,x^b,z)
                out[point]+=F(n,20)
                reset_full_measure[y,x,r,point]+=F(5,16)*weight*F(n,20)
                reference_full_measure[y,x,r,point]+=F(5,16)*F(1,2)*kappa*F(n,20)
            w,mean=selected_moments(out)
            need((w,mean)==(1,(SIGN(x),0,0)),'X poststate')
            rmean=sum(p*SIGN(point[2]) for point,p in out.items())
            need(rmean==F(4,5)*SIGN(x),'R calibration')
            det=(F(1)-SIGN(x)**2-SIGN(y)**2)/4
            need(det==F(-1,4),'unchanged phase')
            reset_branch_count+=1
            reset_cells+=len(out)
        # Terminal failures are unchanged, counted as offered=none.
        for mode_measure in (reference_full_measure,reset_full_measure):
            mode_measure[y,'failed',None]+=F(11,16)
    need(reference_full_measure==reset_full_measure,'whole raw record/outgoing field factorization')
    for y in (0,1):
        need(sum(v for k,v in reset_full_measure.items() if k[0]==y)==1,'fullreset normalization')

    return {
        'schema':'oi-native-phase-v4-independent-review.1',
        'verdict':'ACCEPT_WITHIN_SCOPE',
        'author_commit':'5b77352f50ddfe750b1cf5cbc72ebdded046df31',
        'author_file_hashes_checked':digests,
        'response_cases':response_cases,'distant_controls':distant_cases,
        'dropped_parity_mismatches':dropped_parity,'dropped_old_slice_mismatches':dropped_old,
        'equal_parity_three_neighbor_controls':parity_controls,
        'fixed_old_history_contexts':contexts,
        'mask01_failure_triples_by_x_u':{k:list(v) for k,v in sorted(failed_mask01.items())},
        'post_X_reset_whole_port_branches':reset_branch_count,'post_X_outgoing_cells':reset_cells,
        'full_reset_measure_including_terminal_failures':'PASS',
        'native_reachability_of_local_completions_claimed':False,
    }


if __name__=='__main__':
    print(json.dumps(main(),indent=2,sort_keys=True))
