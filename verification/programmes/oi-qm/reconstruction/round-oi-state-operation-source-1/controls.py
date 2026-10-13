#!/usr/bin/env python3
"""Prospective native source-audit controls; design mode is --self-test.

Object checks use a named commit and frozen control-plane objects. Saved
computations are never substituted for a new run. Written proofs stay [W].
"""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction
import argparse
import copy
import json
import re
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[5]
R='verification/programmes/oi-qm/reconstruction/round-oi-state-operation-source-1/'
D='dee3b5ae6fd3fb20fa1bad3337963e5af947f3a4'
ROUND='OI-STATE-OPERATION-SOURCE-1'
HASHES={
    'probe.py':'ac740098cd100aca32b6ac0ff19d1c1dcb5a42a081863319e1ff0fac7b2b7e01',
    'fixture_check.py':'b8e316ee44c80e366a65c5d95bf4a5ef699d8bc556583c1fe9bac4c314750532',
    'argument.md':'158e2e42f3ade89653f080b259903fb89de27ccd26a78445b2d9c37626894b38'}
WORKFLOW='4210a0ca30ab724cddfa10cecf69ef73c5a7f584a52a9fda5213b4c7446b840c'
EARNED=('Local product-test and rank-one update consistency does not imply preservation of the given pair cone; '
        'complete-dual-test pullback closure restates that preservation; product-test state saturation grants Q3 inclusion '
        'and fails the quantum PSD comparison. No physical compatibility source is derived by this bounded audit.')


def require(condition, name):
    if not condition:raise AssertionError(name)


def git(*args):
    return subprocess.check_output(['git','-C',str(ROOT),*args])


def obj(c,path):
    return git('show',c+':'+path)


def execute(name,*args):
    p=subprocess.run([sys.executable,'-I','-B',str(ROOT/R/name),*args],capture_output=True)
    require(p.returncode==0 and not p.stderr,'fresh computation exit/stderr: '+name)
    return p.stdout


def validate(data):
    require(data['witness_operation']=='Phi1' and data['availability_theorem']=='finite_protocol_spectator',
            'uniform inventory-independent witness')
    require(len(data['uniform_phi1_separators'])==2 and all(Fraction(v)<0 for v in data['uniform_phi1_separators']),
            'both qualified fixture separations')
    require(data['quantum_positive'] and data['classical_positive'],'both positive controls')
    require(all(data[k] for k in ('classical_protocol_fixed','classical_filters',
                                  'classical_product_saturation','classical_dual_pullbacks')),
            'classical checks test the actual readings')
    require(data['LO_available_local_operations'].startswith('Phi1 is a one-token operation'),
            'general local-operation reading explicit')
    require(data['readout_cases']==5*2*8*8 and data['filter_cases']==5*2*2*8*2,'declared finite coverage')
    require(data['controls']>0,'nonvacuous controls')
    require(data['P1_local_consistency'].startswith('INSUFFICIENT:'),'local-consistency assessment')
    require('written evidence' in data['P2_complete_dual_tests'] and 'written evidence' in data['P3_product_saturation'],
            'universal evidence boundaries')


def self_test():
    raw=execute('probe.py');data=json.loads(raw);validate(data)
    fixture=execute('fixture_check.py')
    require(b'INDEPENDENT CHECK: PASS; 53 exact controls' in fixture,'independent fixture checker')
    program_mutations={'identity':'uniform protocol negative witnesses',
                       'phase':'uniform protocol negative witnesses',
                       'unnormalized':'normalized sharp frame',
                       'positive_control':'quantum PSD positive control'}
    for mutation,expected in program_mutations.items():
        p=subprocess.run([sys.executable,'-I','-B',str(ROOT/R/'probe.py'),'--mutation',mutation],capture_output=True)
        require(p.returncode!=0 and not p.stdout and expected.encode() in p.stderr,'mutation rejected: '+mutation)
    for name,change in [('inventory-only replacement',lambda x:x.update(availability_theorem='instAvail_fullClass_of_krausFamily')),
                        ('missing quantum positive',lambda x:x.update(quantum_positive=False)),
                        ('missing classical positive',lambda x:x.update(classical_positive=False)),
                        ('missing fixture',lambda x:x.update(uniform_phi1_separators=['-1/4'])),
                        ('missing readout coverage',lambda x:x.update(readout_cases=1)),
                        ('upgraded written proof',lambda x:x.update(P2_complete_dual_tests='kernel theorem')),
                        ('missing classical protocol',lambda x:x.update(classical_protocol_fixed=False)),
                        ('missing classical filters',lambda x:x.update(classical_filters=False)),
                        ('missing classical saturation',lambda x:x.update(classical_product_saturation=False)),
                        ('missing classical dual',lambda x:x.update(classical_dual_pullbacks=False))]:
        bad=copy.deepcopy(data);change(bad)
        try:validate(bad)
        except AssertionError:pass
        else:raise AssertionError('accepted metadata mutation: '+name)
    print(raw.decode(),end='')
    print(fixture.decode(),end='')
    print('DESIGN CONTROLS: PASS; positive fixture; 4 construction mutations; 10 policy mutations')


def object_checks(subject,freeze):
    receipt_path='verification/receipts/'+ROUND+'.json'
    archived=subprocess.run(['git','-C',str(ROOT),'show',subject+':'+receipt_path],capture_output=True)
    if archived.returncode==0:
        receipt=json.loads(archived.stdout)
        require(receipt['status']=='complete' and receipt['d']==D,'archive identity')
        subject,freeze=receipt['e'],receipt['f']
    if freeze is None:
        freeze=git('log','-1','--format=%H',subject,'--',R+'preregistration.md',R+'amendments/').decode().strip()
    require(re.fullmatch('[0-9a-f]{40}',freeze or '') is not None,'freeze object')
    pre=obj(freeze,R+'preregistration.md')
    require(obj(subject,R+'preregistration.md')==pre,'control plane unchanged')
    require(('D: '+D).encode() in pre,'drafting snapshot')
    frozen_cp=git('ls-tree','-r','--name-only',freeze,'--',R+'amendments/').decode().splitlines()
    actual_cp=git('ls-tree','-r','--name-only',subject,'--',R+'amendments/').decode().splitlines()
    require(frozen_cp==actual_cp,'amendment population')
    for path in frozen_cp:require(obj(subject,path)==obj(freeze,path),'amendment unchanged: '+path)
    names=git('diff','--name-only',D,subject).decode().splitlines()
    require(all(p.startswith(R) or p=='.github/workflows/verify.yml' for p in names),'bounded execution paths')
    for name,digest in HASHES.items():
        require(sha256(obj(subject,R+name)).hexdigest()==digest,'frozen bytes: '+name)
        require(sha256((ROOT/R/name).read_bytes()).hexdigest()==digest,'working bytes: '+name)
    match=re.search(rb'^Controls SHA256: ([0-9a-f]{64})$',pre,re.M)
    require(match and sha256(obj(subject,R+'controls.py')).hexdigest()==match.group(1).decode(),'frozen controls bytes')
    require(match and sha256(Path(__file__).read_bytes()).hexdigest()==match.group(1).decode(),'working controls bytes')
    require(sha256(obj(subject,'.github/workflows/verify.yml')).hexdigest()==WORKFLOW,'predicted workflow')
    allowed={R+'preregistration.md',R+'probe.py',R+'fixture_check.py',R+'argument.md',R+'controls.py',
             R+'probe-output.json',R+'fixture-output.txt',R+'result.md'}|set(frozen_cp)
    population=set(git('ls-tree','-r','--name-only',subject,'--',R).decode().splitlines())
    require(population<=allowed,'bounded record population')
    raw=execute('probe.py');data=json.loads(raw);validate(data)
    require(raw==obj(subject,R+'probe-output.json'),'fresh probe versus saved output')
    require(execute('fixture_check.py')==obj(subject,R+'fixture-output.txt'),'fresh independent versus saved output')
    if R+'result.md' in population:
        result=obj(subject,R+'result.md').decode()
        require(result.startswith('# OI state-operation source audit\n\nOutcome: '+ROUND+'-READ\n'),'scoped outcome')
        require(result.count(EARNED)==1,'earned reading exactly once')
        require('SOURCE-DERIVATION' not in result,'no physical-source promotion')
    print('NATIVE SOURCE CONTROLS: PASS; frozen bytes; bounded paths; fresh evidence; scoped reading')


def main():
    p=argparse.ArgumentParser();p.add_argument('subject',nargs='?');p.add_argument('--freeze');p.add_argument('--self-test',action='store_true')
    args=p.parse_args()
    if args.self_test:self_test();return
    require(args.subject is not None,'named subject required')
    subject=git('rev-parse',args.subject+'^{commit}').decode().strip()
    object_checks(subject,args.freeze)


if __name__=='__main__':main()
