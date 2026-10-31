#!/usr/bin/env python3
"""Original-key geometry and full-packet operand fibres; no native field replay."""
import argparse
from fractions import Fraction
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path

D = ((-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1))
ORDER = (1,2,4,0,3,5)
LAUNCH = (D[0],D[3],D[0],D[3],D[3],D[5])
Z = (0,0,0)


def need(ok, reason):
    if not ok:
        raise RuntimeError(reason)


def pinned(path, digest):
    raw = path.read_bytes()
    need(hashlib.sha256(raw).hexdigest() == digest, 'input pin '+str(path))
    return raw


def xor(values):
    result = 0
    for value in values:
        result ^= value
    return result


def h(code):
    a, b, d = code >> 2, (code >> 1) & 1, code & 1
    return 4*b+2*d+(a ^ (b & d))


def hinv(code):
    a, b, d = code >> 2, (code >> 1) & 1, code & 1
    return 4*(d ^ (a & b))+2*a+b


def packet(q, labels):
    need(len(labels) == 13, 'all thirteen free output labels retained')
    previous = [0]*6
    current = [0]*6
    for j, direction in enumerate(ORDER):
        previous[direction] = labels[1+j]
        current[direction] = labels[7+j]
    return (q ^ h(xor(previous)),)+tuple(current)+(labels[0],)+tuple(previous)


def recover(k):
    return k[0] ^ h(xor(k[8:14]))


def unlabel(k):
    return (k[7],)+tuple(k[8+i] for i in ORDER)+tuple(k[1+i] for i in ORDER)


def geometry(v, inventory):
    _, balls = v.ready_balls()
    q = v.Q10
    labels = [('N', v.L+2, q, v.add(q,D[3],v.L+2))]
    for off in (2,3):
        labels += [(str(off)+':'+str(i),v.L+off,v.add(q,D[i]),
                    v.add(v.add(q,D[i]),LAUNCH[i],v.L+off)) for i in ORDER]
    keys = [row[3] for row in labels]
    need(len(keys) == len(set(keys)) == 13, 'thirteen distinct original keys')
    triangle = []
    conservative = []
    summaries = []
    for i,(name,time,site,key) in enumerate(labels):
        need(v.classify(key,inventory,balls) == ('FREE','complement'), 'key outside pins and sources')
        need(all(any(key[j] != port[j] for j in range(3) if axis[j] == 0)
                 for port,axis,deadline in v.PORTS), 'key outside full bank lines')
        need(v.dist(key,site) == time and sum(a != b for a,b in zip(key,site)) == 1,
             'own uniquely axial first arrival')
        need(v.dist(key,q) > v.L+1 and v.dist(key,v.Q9) > v.L,
             'keys absent original q10 and old q9 phases')
        need(min(v.dist(key,p) for p,_,_ in v.PORTS) > v.L+3,
             'keys absent complete raw public-port history through cut')
        affected = [j for j,(_,t,s,_) in enumerate(labels)
                    if v.dist(key,s) <= t and (t-v.dist(key,s)) % 2 == 0]
        full_cone = [j for j,(_,t,s,_) in enumerate(labels) if v.dist(key,s) <= t]
        need(i in affected and min(affected) == i and min(full_cone) == i,
             'later keys cannot affect any earlier label')
        triangle.append(affected)
        conservative.append(full_cone)
        summaries.append({'label':name,'ready_slack':min(v.dist(key,c)-r for c,r in balls),
                          'earliest_port_over_L':min(v.dist(key,p) for p,_,_ in v.PORTS)-v.L})
    # Whole-V q9 at L+2, if included, is a packet coordinate, not independent past.
    v_keys = [i for i,key in enumerate(keys) if v.dist(key,v.Q9) <= v.L+2]
    need(v_keys == [3] and labels[3][2] == v.Q9, 'stipulated V read is retained label 3')
    port,axis,deadline = v.PORTS[5]
    bank_key = v.add(port,axis,v.S+4)
    need(v.bank_index(bank_key) == (5,4) and v.classify(bank_key,inventory,balls)[0] == 'BANK',
         'setting record uses existing port5 bank block')
    need(bank_key not in keys and bank_key not in inventory and
         bank_key not in v.local_sources().values(), 'bank key distinct from sources and packet keys')
    need(v.dist(bank_key,port) == v.S+4 and
         min(v.dist(bank_key,p) for p,_,_ in v.PORTS) == v.S+4,
         'port5 bank own first arrival absent earlier public history')
    need(v.dist(bank_key,q) > v.L+1, 'bank setting label cannot affect original Q')
    side = 256*v.L+64*v.T+1
    points = keys+[bank_key,q]+list(inventory)+list(v.local_sources().values())
    need(all(max(p[j] for p in points)-min(p[j] for p in points) < side//2 for j in range(3)),
         'no torus wrap in audited separations')
    # A shorter axial key violates the unchanged preparation.
    inward = v.add(q,D[3],v.L+1)
    need(v.classify(inward,inventory,balls)[0] == 'PINNED', 'inward-key preparation countercontrol')
    return summaries,triangle,conservative


def run(root, contract):
    raw = pinned(root/'native_route_v13/result.json',
                 '762b9799db7448c4eecf2c994c8c68ff94e1be83a7f6884b4a36385505df5a02')
    table = json.loads(raw)['q10_table_hex']
    need(hashlib.sha256(table.encode()).hexdigest() ==
         'b2f32466113dede2fa9e43469f5c209fde5d610180ed748dcd025d4cd2a4b3cc', 'native table pin')
    source_raw = pinned(root/'parallel_v3/history_control/SOURCE-GEOMETRY.json',
                        '2642e1a68825faa5d3bb1049e8722adec1ec33bd3f56b9e4416b2c902a85ec5d')
    sources = json.loads(source_raw)['sources']
    need(len(sources) == 1479, 'complete inherited source inventory')
    pinned(contract,'1a0b34ebb0c7115dd5faae11d2ab20c25ecf8a6f091ea292eb184e4311be7633')
    path = root/'native_vread_v15/checks.py'
    pinned(path,'93b4161f32e02874769d57d8a670d1a460d26fa2c953d517db5c6564fb649824')
    spec = importlib.util.spec_from_file_location('original_preparation',path)
    v = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(v)
    need(all(h(code) == v.h(code) and hinv(h(code)) == code for code in range(8)), 'native bijection')
    geo,edges,cones = geometry(v,{tuple(row['position']) for row in sources})
    # Exhaustive one-step bijectivity for every old-local/neighbor background.
    for old,bg in itertools.product(range(8),repeat=2):
        need(len({old ^ h(code ^ bg) for code in range(8)}) == 8, 'every axial diagonal map bijective')
    # Abstract triangular controls test the proof's bookkeeping, not native fields.
    def transform(keys):
        out = []
        for i,key in enumerate(keys):
            out.append((3*i+xor(out)) % 8 ^ h(key ^ ((5*i+sum(out)) % 8)))
        return tuple(out)
    def inverse(out):
        result = []
        for i,value in enumerate(out):
            old,bg = (3*i+xor(out[:i])) % 8, (5*i+sum(out[:i])) % 8
            result.append(hinv(value ^ old) ^ bg)
        return tuple(result)
    triangular_controls = 0
    for seed in (0,1):
        fixed = [(i+3*seed) % 8 for i in range(13)]
        for i in range(13):
            outs = []
            for value in range(8):
                keys = fixed[:]
                keys[i] = value
                out = transform(keys)
                need(inverse(out) == tuple(keys), 'triangular inverse retains all original key correlations')
                outs.append(out)
                triangular_controls += 1
            need(len({o[:i] for o in outs}) == 1 and len({o[i] for o in outs}) == 8,
                 'abstract triangular diagonal and earlier-label controls')
    pair = {(a,h(b)) for a,b in itertools.product(range(8),repeat=2)}
    correlated = {(a,h(a)) for a in range(8)}
    need(len(pair) == 64 and len(correlated) == 8 and
         all(len({p[j] for p in correlated}) == 8 for j in (0,1)), 'shared-key fair-marginal countercontrol')
    tv = Fraction(1,2)*sum(abs(Fraction(int(p in correlated),8)-Fraction(1,64)) for p in pair)
    need(tv == Fraction(7,8), 'joint product-law premise is essential')
    small_outputs = {transform(keys) for keys in itertools.product(range(8),repeat=3)}
    need(len(small_outputs) == 8**3, 'complete small triangular bijection')
    need(all(len({(a,c) for a,b,c in small_outputs if b == record}) == 8**2
             for record in range(8)), 'condition on retained record output, not independent source keys')
    lookup = {}
    terminal = 0
    for bits in itertools.product((0,1),repeat=6):
        x,u,my,mr,a,b = bits
        e,n = 7-2*my,4*my+2+(1 ^ my)
        q = int(table[v.q10_index(*bits,e,n)],16)
        if (a,b) == (0,1):
            terminal += 1
        else:
            need(q >> 2 == x ^ u ^ a, 'retained original sign encoding')
            lookup[bits] = q
    samples = []
    for seed in range(3):
        labels = tuple((5*i+seed) % 8 for i in range(13))
        for q in range(8):
            k = packet(q,labels)
            need(len(k) == 14 and recover(k) == q and unlabel(k) == labels,
                 'full42-bit fibre bijection, all fields retained')
            need(k[12] == labels[3], 'whole-V record is actual packet component')
        samples.append(labels)
    collisions = []
    for x,u,my,a,b in itertools.product((0,1),repeat=5):
        if (a,b) == (0,1):
            continue
        left,right = (x,u,my,0,a,b),(x,u,my,1,a,b)
        if lookup[left] == lookup[right] and a:
            k0,k1 = packet(lookup[left],samples[0]),packet(lookup[right],samples[0])
            need(k0 == k1 and (1 ^ (a & 0)) != (1 ^ (a & 1)), 'full-packet target collision')
            collisions.append({'x':x,'u':u,'mY':my,'a':a,'b':b,'Q_code':lookup[left]})
    need(len(lookup) == 48 and terminal == 16, 'all original continuing and terminal rows retained')
    return {'schema':'oi.native-packet-operand.v1','status':'PASS',
            'verdict':'PACKET_INFORMATION_EQUALS_Q_UNDER_RETAINED_JOINT_PRODUCT_PRIOR',
            'parent':'6e25dd8460a58f6ca4ae924a24b32e56e9ee49a1',
            'original_key_triples':len(geo),'packet_bits':42,'conditional_fibre_bits':3*len(geo),
            'packet_mass_given_remainder':'8^-%d' % len(geo),
            'packet_mass_given_remainder_and_stipulated_V':'8^-%d' % (len(geo)-1),
            'key_geometry':geo,'exact_dependency_edges':edges,'conservative_dependency_edges':cones,
            'whole_V_label':3,'raw_port_key_exclusion_horizon':
                'through tau=L+3 only; stipulated V retained; not future H=L+79',
            'continuing_source_rows':len(lookup),'terminal_diagnostic_rows':terminal,
            'target_sensitive_equal_packet_law_pairs':collisions,
            'public_port5_source':'existing independent bank block at S+4',
            'public_setting_actuator':'NOT_COMPILED_BY_DECLARED_PASSIVE_INTERFACE',
            'outgoing_environment':'GLOBAL_NATIVE_PUSHFORWARD_FORMULA_ONLY; NO_REUSE_CERTIFICATE',
            'triangular_bookkeeping_controls':triangular_controls,'shared_key_TV':str(tv),
            'native_field_simulations':0,'new_reads_writes_resets':0,'terminal_new_reads_or_offers':0,
            'preparation_or_access_adoption':False,'microscopic_matching_benchmark_changed':False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root',type=Path,default=Path(__file__).resolve().parents[2] /
                        'oi-qm/reconstruction/native-y-continuation-20261024')
    parser.add_argument('--contract',type=Path)
    args = parser.parse_args()
    try:
        result = run(args.source_root,args.contract or args.source_root/'shared_v12/INTERFACE-CONTRACT.md')
    except (RuntimeError,ValueError,KeyError,OSError,TypeError) as exc:
        print(json.dumps({'status':'VOID','reason':str(exc)},sort_keys=True))
        raise SystemExit(2)
    print(json.dumps(result,sort_keys=True,separators=(',',':')))
