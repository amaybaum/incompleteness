#!/usr/bin/env python3
"""Balanced source interface: preserve the local computation; test full input."""
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


BITS = tuple(itertools.product(range(2), repeat=6))
PARAMS = tuple(itertools.product(range(2), repeat=5))  # u,a,b,mR,mY
MODES = (0, 2, 4, 6)  # zero D component
D = tuple(tuple(s if j == a else 0 for j in range(3))
          for a in range(3) for s in (-1, 1))


def enc(a, b, d): return 4*a+2*b+d
def triple(v): return (v >> 2, (v >> 1) & 1, v & 1)
def h(v):
    a, b, d = triple(v)
    return enc(b, d, a ^ (b & d))
def xor(values):
    out = 0
    for v in values:
        out ^= v
    return out
def index(values, sizes):
    out = 0
    for value, size in zip(values, sizes):
        out = size*out+value
    return out
def dist(a, b): return sum(abs(x-y) for x, y in zip(a, b))


def pinned(path, digest):
    raw = path.read_bytes()
    need(hashlib.sha256(raw).hexdigest() == digest, 'input pin '+path.name)
    return raw.decode()


def response(root, functions, candidate, w=0, v=0):
    # Repack the unchanged retained evaluator into64 source contexts. Only
    # original-time source payload data and bit-lane indexing are varied.
    spec = importlib.util.spec_from_file_location('balanced_delivery_route', root/'native_route_v13/checks.py')
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    m.UR = PARAMS
    m.ROWS = tuple((x,u,my,mr,a,b,7-2*my,(u ^ a ^ mr) if candidate else (4*my+2+(1 ^ my)))
                   for x,u,my,mr,a,b in BITS)
    m.UF, m.FULL = (1 << 32)-1, (1 << 64)-1
    m.UINDEX = {r: i for i, r in enumerate(PARAMS)}
    m.XM, m.UM, m.MY, m.MR = tuple(sum(r[j] << i for i, r in enumerate(m.ROWS)) for j in range(4))
    old_keys = set(m.SOURCES)
    def source(key, args):
        u,a,b,mr,my = args
        n = (u ^ a ^ mr) if candidate else (4*my+2+(1 ^ my))
        original_key = (-key[0], key[1], key[2]) if candidate and key in ((1,0,-17),(-1,0,-17)) else key
        value = enc(*functions[original_key](u,a,b,n))
        if candidate and key in ((1,0,-17),(-1,0,-17)):
            value ^= w ^ (v if mr else 0)
        return value
    for key in old_keys:
        zero = source(key, (0,)*5)
        coefficients = [source(key, tuple(int(i == j) for i in range(5))) ^ zero for j in range(5)]
        need(all(source(key, row) == zero ^ xor(c for bit,c in zip(row, coefficients) if bit)
                 for row in PARAMS), 'all proposed initial payloads are affine')
    m.SOURCES = {key: tuple(sum(((source(key,row) >> (2-f)) & 1) << i
                                for i,row in enumerate(PARAMS)) for f in range(3)) for key in old_keys}
    need(set(m.SOURCES) == old_keys, 'no source site added or removed')
    @lru_cache(None)
    def expand(q):
        return tuple(sum(((word >> m.UINDEX[u,a,b,mr,my]) & 1) << i
                         for i,(x,u,my,mr,a,b,e,n) in enumerate(m.ROWS)) for word in q)
    m.expand_upper = expand
    for f in (m.direct_upper, m.upper_strip, m.upper):
        f.cache_clear()
    m.CONTROLS = [((0,-m.S,-68),m.XM), ((0,m.S,-68),m.MY ^ m.MR),
                  ((m.T,m.P,-68),m.MY), ((-m.T,m.P,-68),m.MR)]
    need(m.P % (12*840**m.BUDGET) == 0 and m.BUDGET == 20 and m.P % (384*840**3) == 0,
         'retained upper/lower period reduction')
    local = direct = 0
    if candidate:
        two = m.direct_upper(2,0,0,-18)
        for u,a,b,mr in itertools.product(range(2), repeat=4):
            got = m.code(m.lane(two, m.UINDEX[u,a,b,mr,0]))
            need(got == enc(1 ^ a ^ b ^ mr, 1 ^ (a & mr), mr ^ u ^ (u & a) ^ (u & a & mr)),
                 'balanced source terms preserve all three computed J fields')
            local += 1
        for key in ((18,0,0),(18,-1,1),(18,1,1),(20,0,0)):
            ell,x,y = key
            arr = m.upper_strip()[key]
            for n in (0,1):
                need(arr[n] == m.direct_upper(n+ell,x,y,n), 'modified strip/direct native control')
                direct += 32
    out, records = m.native_compute()
    return ([m.code(m.lane(out,i)) for i in range(64)],
            [m.code(m.lane(records[9][0,0,9],i)) for i in range(64)], local, direct)


def plane_controls():
    side = 7
    sites = tuple(itertools.product(range(side), repeat=3))
    neighbors = {p: [tuple((p[j]+d[j]) % side for j in range(3)) for d in D] for p in sites}
    mirror = {p: ((-p[0]) % side,p[1],p[2]) for p in sites}
    def step(now, old): return {p: old[p] ^ h(xor(now[w] for w in neighbors[p])) for p in sites}, now
    checks = 0
    for seed in range(3):
        now = {p: (min(p[0],side-p[0])*p[1]+3*p[2]+seed) % 8 for p in sites}
        old = {p: (min(p[0],side-p[0])+p[1]*p[2]+3*seed) % 8 for p in sites}
        changed = {p: now[p] ^ (1+(p[1]+2*p[2]+seed) % 7 if p[0] else 0) for p in sites}
        past = {p: old[p] ^ (1+(3*p[1]+p[2]+seed) % 7 if p[0] else 0) for p in sites}
        need(now != changed and old != past, 'nonvacuous off-plane differences')
        for _ in range(4):
            need(all(now[p] == now[mirror[p]] and changed[p] == changed[mirror[p]] for p in sites),
                 'native reflection symmetry retained')
            need(all(now[p] == changed[p] and old[p] == past[p] for p in sites if p[0] == 0),
                 'complete current/previous central plane independent of symmetric exterior')
            checks += side*side
            now,old = step(now,old)
            changed,past = step(changed,past)
        # A genuine asymmetric native perturbation reaches the plane.
        other = dict(now)
        other[1,0,0] ^= 4
        left,_ = step(now,old)
        right,_ = step(other,old)
        need(left[0,0,0] ^ right[0,0,0] == 1, 'asymmetric native positive control')
    return checks


def run(root):
    source = pinned(root/'native_route_v13/checks.py',
                    '8c1bbc37f47b6ff7ad7ee67d719f058067e2e15e9a6a967adfb78ef57d1ed856')
    vread = pinned(root/'native_vread_v15/checks.py',
                   '93b4161f32e02874769d57d8a670d1a460d26fa2c953d517db5c6564fb649824')
    inventory = json.loads(pinned(root/'parallel_v3/history_control/SOURCE-GEOMETRY.json',
                                  '2642e1a68825faa5d3bb1049e8722adec1ec33bd3f56b9e4416b2c902a85ec5d'))['sources']
    qt = json.loads((root/'native_route_v13/result.json').read_text())['q10_table_hex']
    pt = json.loads((root/'branch_v10/local-controller/symmetric-result.json').read_text())['q9_table_hex']
    need(hashlib.sha256(qt.encode()).hexdigest() == 'b2f32466113dede2fa9e43469f5c209fde5d610180ed748dcd025d4cd2a4b3cc', 'q10 table pin')
    need(hashlib.sha256(pt.encode()).hexdigest() == 'dcb150b528926e6fa7f8eb2f4e3d36f5a60742090df63fc899db97d9a365cbcf', 'q9 table pin')
    tree = ast.parse(source)
    node = next(n.value for n in tree.body if isinstance(n,ast.Assign) and
                any(isinstance(t,ast.Name) and t.id == 'SOURCES' for t in n.targets))
    functions = {ast.literal_eval(k): eval(compile(ast.Expression(v.args[0]),'<pinned affine source>','eval'),
                                          {'TR': tuple(itertools.product(range(2),repeat=3)), '__builtins__': {}})
                 for k,v in zip(node.keys,node.values)}
    # Check the actual deadline cone used in the reflection-plane argument.
    T=185;P=12*840**185;S=P+T;R=S+68;L=R+9;q=(0,S,78)
    env={'T':T,'P':P,'S':S,'R':R,'L':L,'__builtins__':{}}
    data=ast.parse(vread)
    fn=next(n for n in data.body if isinstance(n,ast.FunctionDef) and n.name == 'local_sources')
    named=eval(compile(ast.Expression(next(n.value for n in fn.body if isinstance(n,ast.Return))),'<named geometry>','eval'),env)
    ports=eval(compile(ast.Expression(next(n.value for n in data.body if isinstance(n,ast.Assign) and
                                          any(isinstance(t,ast.Name) and t.id == 'PORTS' for t in n.targets))),'<banks>','eval'),env)
    need(len(named) == 17 and len(inventory) == 1479 and len(ports) == 8, 'primary inventory counts')
    need([tuple(s['position']) for s in inventory if dist(tuple(s['position']),q) <= L+1] == [(0,0,0)],
         'only invariant compiled origin in deadline cone')
    need({k for k,p in named.items() if dist(p,q) <= L+1 and p[0] != 0} ==
         {'Kplus','Kminus','selector_plus','selector_minus','F10_pin'}, 'paired or zero off-plane exceptions only')
    for a,b in (('Kplus','Kminus'),('selector_plus','selector_minus')):
        need((-named[a][0],named[a][1],named[a][2]) == named[b], 'primary reflected pairs')
    for port,direction,deadline in ports:
        axis=next(i for i,d in enumerate(direction) if d)
        optimum=(q[axis]-port[axis])*direction[axis]
        times=(deadline+1,2*L,min(2*L,max(deadline+1,optimum)))
        need(min(dist(tuple(v+t*d for v,d in zip(port,direction)),q) for t in times) > L+1,
             'all bank rays excluded from deadline cone')
    # Exact identity explaining why zero-D paired shifts preserve the local circuit.
    identity_checks=0
    for delta,z,t in itertools.product(range(2),range(8),range(8)):
        plus,minus=enc(delta,delta,delta),enc(delta,0,delta)
        need(h(z ^ plus ^ t) ^ h(z ^ minus ^ t) ^ h(z ^ plus) ^ h(z ^ minus) == (delta & (t & 1)),
             'complete native paired-shift identity')
        identity_checks += 1
    plane=plane_controls()
    target=[int(qt[index(bits+(7-2*bits[2],4*bits[2]+2+(1 ^ bits[2])),(2,)*6+(8,8))],16) for bits in BITS]
    old_target=[int(pt[index(bits+(4,5,7),(2,)*6+(8,)*3)],16) for bits in BITS]
    base,old,_,_=response(root,functions,False)
    need(base == target and old == old_target, 'repacked evaluator reproduces complete retained baseline')
    rows=[];local_checks=direct_checks=0
    for w,v in itertools.product(MODES,repeat=2):
        out,old,local,direct=response(root,functions,True,w,v)
        local_checks += local;direct_checks += direct
        if (w,v) == (0,0):
            reflected=[int(qt[index((x,u,mr,my,a,b,7-2*my,u ^ a ^ mr),(2,)*6+(8,8))],16)
                       for x,u,my,mr,a,b in BITS]
            need(out == reflected, 'zero-shift programme reproduces accepted nonlinear candidate')
        need(old[0] == old_target[0], 'complete old-record common witness retained')
        rows.append({'constant_W':w,'mR_coefficient_V':v,
                     'continuing_Q_mismatches':sum(a != b and bits[4:6] != (0,1) for bits,a,b in zip(BITS,out,target)),
                     'all_Q_mismatches':sum(a != b for a,b in zip(out,target)),
                     'old_q9_mismatches':sum(a != b for a,b in zip(old,old_target)),
                     'common_witness_Q':out[0]})
    witness={r['common_witness_Q'] for r in rows}
    need(len(rows) == 16 and local_checks == 256 and direct_checks == 4096, 'nonvacuous family/native controls')
    need(len(witness) == 1 and target[0] not in witness, 'common plane-symmetry counterexample')
    return {'status':'PASS','verdict':'BALANCED_INTERFACE_FAILS_MATCHED_INPUT',
            'programme_count':16,'native_programme_rows':1024,'paired_identity_cases':identity_checks,
            'preserved_full_J_field_checks':local_checks,'upper_direct_scalar_lanes':direct_checks,
            'dense_plane_scalar_checks':plane,'asymmetric_positive_controls':3,
            'first_gate_passes':sum(r['continuing_Q_mismatches'] == 0 for r in rows),
            'minimum_continuing_Q_mismatches':min(r['continuing_Q_mismatches'] for r in rows),
            'common_context_x_u_mY_mR_a_b':[0]*6,'common_baseline_Q':target[0],
            'common_old_q9':old_target[0],
            'common_candidate_Q':next(iter(witness)),'programmes':rows,
            'new_reads':0,'measurement_output_tests':0,'native_selection_or_reuse':'NOT_ESTABLISHED'}


if __name__ == '__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source-root',type=Path,default=Path(__file__).resolve().parents[2] /
                    'oi-qm/reconstruction/native-y-continuation-20261024')
    args=ap.parse_args()
    try:
        result=run(args.source_root)
    except (RuntimeError,ValueError,KeyError,OSError,StopIteration,TypeError) as exc:
        print(json.dumps({'status':'VOID','reason':str(exc)},sort_keys=True));raise SystemExit(2)
    print(json.dumps(result,sort_keys=True,separators=(',',':')))
