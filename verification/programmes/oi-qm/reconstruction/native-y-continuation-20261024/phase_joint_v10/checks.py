"""Exact joint law from retained native source data; no author evaluator imports."""
import argparse, hashlib, json
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from pathlib import Path

H=(0,2,4,7,1,3,5,6)
WITNESS=(4,5,7)

def need(ok, message):
    if not ok: raise RuntimeError(message)

def unpack(v): return (v>>2,(v>>1)&1,v&1)

def tv(a,b):
    return sum((abs(a.get(k,F())-b.get(k,F())) for k in a.keys()|b.keys()),F())/2

def kernel_raw(table,x,u,my,mr,a,b):
    i=0
    for v,n in zip((x,u,my,mr,a,b,*WITNESS),(2,2,2,2,2,2,8,8,8)):
        i=i*n+v
    return unpack(int(table[i],16))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--source-root',type=Path,default=Path(__file__).resolve().parent.parent)
    root=ap.parse_args().source_root
    p=Path(__file__).resolve().parent
    prov=json.loads((p/'PROVENANCE.json').read_text())
    for path,digest in prov['inputs'].items():
        need(hashlib.sha256((root/path).read_bytes()).hexdigest()==digest,'input bytes '+path)
    local=json.loads((root/'branch_v10/local-controller/symmetric-result.json').read_text())
    need(list(WITNESS) in local['accepted_three_mask_witnesses'],'retained native witness')
    need(local['table_order']=='x,u,mY,mR,a,b,Ccode,Vpluscode,Vminuscode; all selector masks retained','native table order')
    table=local['q9_table_hex'];need(len(table)==32768,'complete native table')
    program=json.loads((root/'parallel_v3/direct_reset/herald.json').read_text())['program']
    word=program[:2684]; flags={}
    for a,b,k in product((0,1),(0,1),range(8)):
        seed=a+2*b+4*k; state=0
        for constant,terms in word:
            control=constant
            for bit,mask in terms:
                if seed>>bit&1:control^=mask
            state=H[state^control]
        state=H[H[state]]
        need(state in (0,2),'complete native herald triple')
        flags[a,b,k]=state//2
    need(sum(flags.values())==10,'native herald acceptance count')
    target_planes={(0,0):5,(1,0):3,(1,1):2}
    rejected_planes={(0,0):3,(0,1):8,(1,0):5,(1,1):6}
    worlds=0; branches=0; raw_cells=0; fail_rows=[]
    for x,u,my,mr in product((0,1),repeat=4):
        y=x^u; success=defaultdict(F); failure=defaultdict(F)
        for a,b,k,z in product((0,1),(0,1),range(8),(0,1)):
            worlds+=1
            raw=kernel_raw(table,x,u,my,mr,a,b)
            phase=((0,y,0),raw,(0,0,z))
            if flags[a,b,k]: success[phase]+=F(1,64)
            else: failure[phase]+=F(1,64)
        reference={((0,y,0),(0,y^a,y^b),(0,0,z)):F(n,64)
                   for (a,b),n in target_planes.items() for z in (0,1)}
        need(dict(success)==reference,'entire success physical phase law')
        need(sum(success.values())==F(5,16),'success mass')
        need(sum(failure.values())==F(11,16),'failure mass retained')
        need(sum(success.values())+sum(failure.values())==1,'no discarded runs')
        expected_failure=defaultdict(F)
        for (a,b),n in rejected_planes.items():
            raw=(u,y,x&(1^u)) if (a,b)==(0,1) else (0,y^a,y^b)
            need(kernel_raw(table,x,u,my,mr,a,b)==raw,'actual raw failure fields')
            for z in (0,1):expected_failure[((0,y,0),raw,(0,0,z))]+=F(n,64)
        need(dict(failure)==dict(expected_failure),'entire physical failure distribution retained')
        # Same native source row must remain independent of ciphertext pads.
        need(all(kernel_raw(table,x,u,my,mr,a,b)==kernel_raw(table,x,u,0,0,a,b)
                 for a,b in product((0,1),repeat=2)),'no hidden pad conditioning')
        branches+=2;raw_cells+=len(success)+len(failure)
        if my==mr==0:
            fail_rows.append({'x':x,'u':u,'pattern01':kernel_raw(table,x,u,0,0,0,1)})
    # Exact terminal law countercontrols; these are controls, not alternative native constructions.
    correct={(a,b,z):F(n,20) for (a,b),n in target_planes.items() for z in (0,1)}
    swapped={(a,b,z):F(n,20) for (a,b),n in {(0,0):5,(1,0):2,(1,1):3}.items() for z in (0,1)}
    need(tv(correct,swapped)==F(1,10),'calibration mutant full-law difference')
    shared={(a,b,a):F(n,10) for (a,b),n in target_planes.items()}
    need(tv(correct,shared)==F(1,2),'shared-z joint defect')
    need(all(sum(v for (a,b,z),v in shared.items() if z==r)==F(1,2) for r in (0,1)),'shared-z fair marginal control')
    need(sum(F(1,64) for a,b,k,z in product((0,1),(0,1),range(8),(0,1)) if flags[a,b,k])!=1,'dropped failures rejected')
    # Reusing old u as a gives deterministic X=x even when the total herald mass still agrees.
    for x,u in product((0,1),repeat=2):
        y=x^u; law=defaultdict(F);mass=F()
        for b,k,z in product((0,1),range(8),(0,1)):
            if flags[u,b,k]:
                mass+=F(1,32);law[y^u]+=F(1,32)
        need(mass==F(5,16),'reuse control same herald rate')
        law={r:w/mass for r,w in law.items()}
        need(tv(law,{0:F(1,2),1:F(1,2)})==F(1,2),'used-seed output defect')
    # Actual combined source geometry: late local controller and separated remote programs.
    T=185;P=12*840**T;S=T+P;R=S+68;L=R+9
    ports=[(0,T,0),(0,0,-8*T),(T,P,0),(-T,P,0),(4*T,P,0),(0,S,0),(12*R,0,0)]
    controls=[(0,S,S+154),(1,S,S+153),(-1,S,S+153)]
    dist=lambda a,b:sum(abs(c-d) for c,d in zip(a,b))
    need(all(dist(q,p)>L for q in controls for p in ports),'controller leaves all old histories through L unchanged')
    need(all(dist(q,(0,S,76))>R+8 for q in controls),'controller cannot alter earlier Y read')
    need(all(dist(q,(0,S,77))==L for q in controls),'actual current-boundary exceptions')
    need(47*L>13*R and 48*L-13*R>L,'remote/new versus old cone separation')
    need(96*L>2*L and 196*L<256*L+64*T+1,'remote cross cones and no wrap')
    need(L%3==1 and H[4]==1,'native pure-A to D z phase')
    # Conditional old-noise theorem applies to both selected slices: their initial cones exclude its bank.
    need(dist((0,-1,0),(0,S,76))>R+8,'representative old frontier excluded from previous Y cone')
    result={'schema':'oi.native-y.joint-phase-v10','verdict':'PASS_CONDITIONAL_NATIVE_FAMILY_PHASE_PREPARATION',
        'old_rows':16,'complete_seed_worlds':worlds,'success_failure_branches':branches,
        'raw_phase_cells_checked':raw_cells,'fresh_bits':6,'success':'5/16','failure':'11/16',
        'success_plane_counts':[5,3,2],'fair_z_joint':True,'failure_pattern01_raw':fail_rows,
        'calibration_mutant_tv':'1/10','shared_z_joint_tv':'1/2','old_seed_reuse_X_tv':'1/2',
        'noise_factor':'2^(-(6*P+18*d+189)) under retained bank theorem',
        'phase_decoder':'(previous q8.B,current q9.B,current q9.D,current z.D), reordered X,Y,R,Z',
        'readout_and_reuse':'OPEN; previous-slice Y and whole-port X/R access require native protocols',
        'arbitrary_q8_socket':'FAILS retained intervention check',
        'scope':'Conditional original-time native-family phase preparation with explicit terminal failures; no reusable instrument or OI-QM equivalence.'}
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__':main()
