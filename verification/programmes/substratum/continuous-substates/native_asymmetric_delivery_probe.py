#!/usr/bin/env python3
"""Asymmetric constant K offsets: local computation, early witness, full input."""
import argparse
import ast
from functools import lru_cache
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path


def need(ok, why):
    if not ok:
        raise RuntimeError(why)


BITS = tuple(itertools.product(range(2),repeat=6))
D = tuple(tuple(s if j == a else 0 for j in range(3))
          for a in range(3) for s in (-1,1))
Z = (0,0,0)
def enc(a,b,d): return 4*a+2*b+d
def decode(v): return (v >> 2,(v >> 1) & 1,v & 1)
def h(v):
    a,b,d = decode(v)
    return enc(b,d,a ^ (b & d))
def xor(values):
    out=0
    for value in values:
        out ^= value
    return out
def index(values,sizes):
    out=0
    for value,size in zip(values,sizes):
        out=size*out+value
    return out
def add(a,b): return tuple(x+y for x,y in zip(a,b))


def pinned(path,digest):
    raw=path.read_bytes()
    need(hashlib.sha256(raw).hexdigest() == digest,'input pin '+path.name)
    return raw.decode()


def payloads(functions,bits,p,q,reference=False):
    x,u,my,mr,a,b=bits
    n=(4*my+2+(1 ^ my)) if reference else (u ^ a ^ mr)
    values={key:enc(*fn(u,a,b,n)) for key,fn in functions.items()}
    if not reference:
        values[1,0,-17],values[-1,0,-17] = values[-1,0,-17] ^ p, values[1,0,-17] ^ q
    return values,n


def local_output(functions,u,a,b,mr,p,q):
    values,_=payloads(functions,(0,u,0,mr,a,b),p,q)
    physical={(key[0],key[1],-(key[2]+18)):v for key,v in values.items()}
    @lru_cache(None)
    def at(t,site):
        if t < 0: return 0
        if t == 0: return physical.get(site,0)
        return at(t-2,site) ^ h(xor(at(t-1,add(site,d)) for d in D))
    return at(2,Z)


def native_response(root,functions,scenarios,pt):
    # One native bit lane per explicit original source programme/context;
    # no change to the retained native update, geometry or period theorem.
    spec=importlib.util.spec_from_file_location('asymmetric_delivery_route',root/'native_route_v13/checks.py')
    m=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    values=[];rowdata=[]
    for bits,p,q,reference in scenarios:
        sources,n=payloads(functions,bits,p,q,reference)
        values.append(sources)
        rowdata.append(bits+(7-2*bits[2],n))
    count=len(scenarios)
    m.ROWS=tuple(rowdata)
    m.UR=tuple(range(count))
    m.FULL=m.UF=(1 << count)-1
    m.XM,m.UM,m.MY,m.MR=tuple(sum(row[j] << i for i,row in enumerate(rowdata)) for j in range(4))
    keys=set(m.SOURCES)
    need(all(set(v) == keys for v in values),'unchanged source sites')
    m.SOURCES={key:tuple(sum(((row[key] >> (2-f)) & 1) << i for i,row in enumerate(values))
                            for f in range(3)) for key in keys}
    m.expand_upper=lambda q:q
    m.CONTROLS=[((0,-m.S,-68),m.XM),((0,m.S,-68),m.MY ^ m.MR),
                ((m.T,m.P,-68),m.MY),((-m.T,m.P,-68),m.MR)]
    need(m.BUDGET == 20 and m.P % (12*840**20) == 0 and m.P % (384*840**3) == 0,
         'retained actual-scale period reduction')
    direct=0
    for key in ((18,0,0),(18,-1,1),(18,1,1),(20,0,0)):
        ell,x,y=key
        arr=m.upper_strip()[key]
        for n in (0,1):
            need(arr[n] == m.direct_upper(n+ell,x,y,n),'source-profile strip/direct native control')
            direct += count
    output,records=m.native_compute()
    out=[m.code(m.lane(output,i)) for i in range(count)]
    old=[m.code(m.lane(records[9][0,0,9],i)) for i in range(count)]
    # Independent table addressing: delta'=1 lets the general old controller
    # table encode exactly the physical J/K values, with the same x/u/pads.
    for i,((bits,p,q,reference),sources) in enumerate(zip(scenarios,values)):
        x,u,my,mr,a,b=bits
        c=sources[0,0,-18] ^ enc(u ^ 1,1,u ^ 1)
        address=(x,u,my,mr,1,0,c,sources[1,0,-17],sources[-1,0,-17])
        need(old[i] == int(pt[index(address,(2,)*6+(8,)*3)],16),'whole q9 source-table control')
    return out,old,direct


def run(root):
    need(len(BITS) == 64 and sum(bits[4:6] == (0,1) for bits in BITS) == 16,'complete reference source/terminal coverage')
    source=pinned(root/'native_route_v13/checks.py',
                  '8c1bbc37f47b6ff7ad7ee67d719f058067e2e15e9a6a967adfb78ef57d1ed856')
    qt=json.loads((root/'native_route_v13/result.json').read_text())['q10_table_hex']
    pt=json.loads((root/'branch_v10/local-controller/symmetric-result.json').read_text())['q9_table_hex']
    need(hashlib.sha256(qt.encode()).hexdigest() == 'b2f32466113dede2fa9e43469f5c209fde5d610180ed748dcd025d4cd2a4b3cc','q10 pin')
    need(hashlib.sha256(pt.encode()).hexdigest() == 'dcb150b528926e6fa7f8eb2f4e3d36f5a60742090df63fc899db97d9a365cbcf','q9 pin')
    tree=ast.parse(source)
    node=next(n.value for n in tree.body if isinstance(n,ast.Assign) and
              any(isinstance(t,ast.Name) and t.id == 'SOURCES' for t in n.targets))
    functions={ast.literal_eval(k):eval(compile(ast.Expression(v.args[0]),'<pinned affine sources>','eval'),
                                        {'TR':tuple(itertools.product(range(2),repeat=3)),'__builtins__':{}})
               for k,v in zip(node.keys,node.values)}
    preserved=[];local_checks=0
    for p,q in itertools.product(range(8),repeat=2):
        good=True
        pa,pb,pd=decode(p);qa,qb,qd=decode(q)
        for u,a,b,mr in itertools.product(range(2),repeat=4):
            got=local_output(functions,u,a,b,mr,p,q)
            target=enc(1 ^ a ^ b ^ mr,1 ^ (a & mr),mr ^ u ^ (u & a) ^ (u & a & mr))
            delta=a ^ b
            predicted=((1 ^ u) & (pd ^ qd)) ^ (delta & qd) ^ ((1 ^ delta) & (pb ^ qb)) ^ (pb & qd) ^ (qb & pd)
            need(((got ^ target) >> 1) & 1 == predicted,'general asymmetric B-difference identity')
            good &= got == target
            local_checks += 1
        need(good == (pd == qd and (pb ^ qb) == pd),'exact local-computation-preserving classification')
        if good:preserved.append((p,q))
    need(len(preserved) == 16 and sum(p != q for p,q in preserved) == 12,'nonvacuous asymmetric family')
    # Independent offsets are constants. Their XORs with the original affine
    # source payloads remain affine in the permitted known source variables.
    for p,q in preserved:
        for key in functions:
            def field(bits):return payloads(functions,(0,bits[0],bits[4],bits[3],bits[1],bits[2]),p,q)[0][key]
            zero=field((0,)*5)
            basis=[field(tuple(int(i == j) for i in range(5))) ^ zero for j in range(5)]
            need(all(field(bits) == zero ^ xor(v for bit,v in zip(bits,basis) if bit)
                     for bits in itertools.product(range(2),repeat=5)),'initial source fields affine; no nonlinear preload')
    target=[int(qt[index(bits+(7-2*bits[2],4*bits[2]+2+(1 ^ bits[2])),(2,)*6+(8,8))],16) for bits in BITS]
    baseline=[(bits,0,0,True) for bits in BITS]
    base,oldbase,direct=native_response(root,functions,baseline,pt)
    need(base == target,'complete retained baseline reproduced')
    early=[((0,)*6,p,q,False) for p,q in preserved]+[((0,)*6,0,0,True)]
    outputs,old,d=native_response(root,functions,early,pt);direct += d
    need(outputs[-1] == target[0] and old[-1] == oldbase[0],'common-context reference control')
    zero_index=preserved.index((0,0))
    need(outputs[zero_index] == int(qt[index((0,)*6+(7,0),(2,)*6+(8,8))],16),'accepted zero-shift candidate control')
    survivors=[];early_rows=[]
    for pair,out,raw in zip(preserved,outputs[:-1],old[:-1]):
        early_rows.append({'plus_offset':pair[0],'minus_offset':pair[1],'Q':out,'old_q9':raw})
        if out == target[0] and raw == oldbase[0]:survivors.append(pair)
    need(survivors and all(p != q for p,q in survivors),'asymmetry genuinely escapes the old common witness')
    rows=[]
    for p,q in survivors:
        out,raw,d=native_response(root,functions,[(bits,p,q,False) for bits in BITS],pt);direct += d
        differences=[(bits,a,b) for bits,a,b in zip(BITS,out,target) if a != b and bits[4:6] != (0,1)]
        first=differences[0] if differences else None
        rows.append({'plus_offset':p,'minus_offset':q,
                     'all_Q_mismatches':sum(a != b for a,b in zip(out,target)),
                     'continuing_Q_mismatches':len(differences),
                     'all_old_q9_mismatches':sum(a != b for a,b in zip(raw,oldbase)),
                     'continuing_old_q9_mismatches':sum(a != b and bits[4:6] != (0,1) for bits,a,b in zip(BITS,raw,oldbase)),
                     'first_continuing_Q_change':{'bits':first[0],'candidate_Q':first[1],'reference_Q':first[2]} if first else None,
                     'Q_table_hex':''.join(format(v,'x') for v in out)})
    need(rows and len(rows) == len(survivors) and all(len(r['Q_table_hex']) == 64 for r in rows),
         'every early survivor undergoes the complete source-context comparison')
    return {'status':'PASS','verdict':'ASYMMETRY_ESCAPES_COMMON_WITNESS_BUT_FAILS_FULL_INPUT' if all(r['continuing_Q_mismatches'] for r in rows) else 'FULL_INPUT_UNRESOLVED',
            'local_constant_offset_pairs':64,'local_context_checks':local_checks,
            'complete_J_preserving_pairs':len(preserved),'asymmetric_preserving_pairs':12,
            'common_context_reference_Q':target[0],'early_screen_rows':early_rows,'early_screen_survivors':survivors,
            'full_source_rows_per_survivor':64,'continuing_rows_per_survivor':48,'terminal_diagnostic_rows_per_survivor':16,
            'continuing_whole_Q_screen_passes':sum(r['continuing_Q_mismatches'] == 0 for r in rows),
            'matched_full_input':'NOT_ESTABLISHED',
            'upper_direct_scalar_lanes':direct,'survivor_results':rows,
            'measurement_output_tests':0,'new_reads':0,'native_selection_or_reuse':'NOT_ESTABLISHED'}


if __name__ == '__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source-root',type=Path,default=Path(__file__).resolve().parents[2] /
                    'oi-qm/reconstruction/native-y-continuation-20261024')
    args=ap.parse_args()
    try:result=run(args.source_root)
    except (RuntimeError,ValueError,KeyError,OSError,StopIteration,TypeError) as exc:
        print(json.dumps({'status':'VOID','reason':str(exc)},sort_keys=True));raise SystemExit(2)
    print(json.dumps(result,sort_keys=True,separators=(',',':')))
