"""Eight-port finite-horizon frontier audit; Python standard library only."""
from functools import lru_cache
from itertools import product
import hashlib
import json


def require(ok, label):
    if not ok:
        raise RuntimeError(label)


def dist(a, b):
    return sum(abs(x-y) for x, y in zip(a, b))


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def geometry():
    T = 185
    P = 12*840**185
    S = T+P
    d = 68
    R = S+d
    L = R+9
    H = 2*L
    torus = 256*L+64*T+1
    ports = [(0,T,0), (0,0,-8*T), (T,P,0), (-T,P,0),
             (4*T,P,0), (0,S,0), (12*R,0,0), (48*L,0,0)]
    deadlines = [T,T,S,S,S,S,R,L]
    axes = [1,2,1,1,1,1,0,0]
    signs = [-1,-1,1,1,1,1,-1,1]

    def frontier(i, t):
        a = list(ports[i])
        a[axes[i]] += signs[i]*t
        return tuple(a)

    ready = [(p,a) for p,a in zip(ports,deadlines)]
    ready += [((T,0,0),T), ((-T,0,0),T), ((4*T,0,0),T)]
    ready += [((0,S,-68),R), ((-12*R,0,0),R)]
    ready += [((0,S,68+k),R+k) for k in range(10)]
    ready += [((-48*L,0,0),L)]
    # All these are original-time source exceptions or enclosing ready balls.
    local_pins = [(0,0,0), (0,-76,76), (0,S,S+136),
                  (0,S,S+150), (0,S,S+152), (0,S,S+154),
                  (1,S,S+153), (-1,S,S+153)]
    selected = [((0,S,76),L-1), ((0,S,77),L),
                ((-48*L,0,0),L), ((48*L,0,0),L)]

    def points(i, center):
        lo, hi = deadlines[i]+1, H
        root = (center[axes[i]]-ports[i][axes[i]])*signs[i]
        return {lo,hi} | ({root} if lo <= root <= hi else set())

    edges = set()
    chronological = 0
    for i in range(8):
        for j,p in enumerate(ports):
            vals = [dist(frontier(i,t),p)-t for t in points(i,p)]
            require(min(vals) >= 0, 'bank arrives at another port too early')
            if i != j and min(vals) == 0:
                edges.add((i,j))
                require(i < j, 'same-time cycle or reverse edge')
            chronological += len(vals)
        for center,radius in ready:
            require(min(dist(frontier(i,t),center)-radius for t in points(i,center)) > 0,
                    'bank overwrites declared ready cone')
        for center,radius in selected:
            require(min(dist(frontier(i,t),center)-radius for t in points(i,center)) > 0,
                    'selected deadline phase depends on bank')
        for pin in local_pins:
            require(min(dist(frontier(i,t),pin) for t in points(i,pin)) > 0,
                    'bank aliases named initial source')
        for t in (deadlines[i]+1,H):
            require(dist(frontier(i,t),ports[i]) == t, 'own axial first front')
    require(edges == {(2,5),(3,5)}, 'complete equal-time edge set')

    # Solve possible intersections of the affine integer rays exactly.
    distinct = 0
    for i in range(8):
        for j in range(i+1,8):
            ai,aj = axes[i],axes[j]
            if ai == aj:
                if any(ports[i][k] != ports[j][k] for k in range(3) if k != ai):
                    distinct += 1
                    continue
                ri = sorted((frontier(i,deadlines[i]+1)[ai],frontier(i,H)[ai]))
                rj = sorted((frontier(j,deadlines[j]+1)[ai],frontier(j,H)[ai]))
                require(ri[1] < rj[0] or rj[1] < ri[0], 'collinear banks overlap')
            else:
                if any(ports[i][k] != ports[j][k] for k in range(3) if k not in (ai,aj)):
                    distinct += 1
                    continue
                ti = (ports[j][ai]-ports[i][ai])*signs[i]
                tj = (ports[i][aj]-ports[j][aj])*signs[j]
                require(not (deadlines[i] < ti <= H and deadlines[j] < tj <= H),
                        'crossing bank rays overlap')
            distinct += 1

    # Bound every relevant source/ready/target coordinate. Coordinate-wise
    # differences below half the torus side preserve the integer distances.
    endpoints = [frontier(i,t) for i in range(8) for t in (deadlines[i]+1,H)]
    extrema = endpoints + local_pins + ports
    for center,radius in ready:
        for axis in range(3):
            for sign in (-1,1):
                p = list(center)
                p[axis] += sign*radius
                extrema.append(tuple(p))
    spans = [max(p[k] for p in extrema)-min(p[k] for p in extrema) for k in range(3)]
    require(all(2*span < torus for span in spans), 'torus coordinate wrap')
    require(2*H < torus, 'nonunique axial shortest path')

    triples_L = sum(L-a for a in deadlines[:7])
    require(3*triples_L == 6*P+18*d+189, 'retained bit count')
    triples_H = sum(H-a for a in deadlines)
    require(3*(triples_H-triples_L) == 24*L, 'eight-port extension count')
    return {'horizon':'H=L+Delta, 1<=Delta<=L; maximal interval checked at H=2L',
            'port_families':8, 'ready_cones':len(ready),
            'ready_family_pairs':8*len(ready), 'selected_phase_family_pairs':32,
            'pairwise_distinct_family_pairs':distinct,
            'piecewise_chronology_cases':chronological,
            'same_tick_edges':[list(x) for x in sorted(edges)],
            'total_bits':'6*P+18*d+189+24*Delta',
            'additional_bits_per_tick':24,
            'torus_coordinate_span_bounds_pass':True}


TRIPLES = tuple(product((0,1),repeat=3))
STEPS = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))


def native(frontiers, assignments, outputs, background):
    full = (1 << len(assignments))-1
    packed = {p:tuple(sum(row[j][k] << lane for lane,row in enumerate(assignments))
                      for k in range(3)) for j,p in enumerate(frontiers)}

    @lru_cache(None)
    def field(t,p):
        if t in (-1,0):
            if t == 0 and p in packed:
                return packed[p]
            b = hashlib.sha256(repr((background,t,p)).encode()).digest()[0]
            return tuple(full if (b >> k)&1 else 0 for k in range(3))
        acc = [0,0,0]
        for step in STEPS:
            v = field(t-1,add(p,step))
            for k in range(3):
                acc[k] ^= v[k]
        old = field(t-2,p)
        a,b,c = acc
        h = (b,c,a^(b&c))
        return tuple(old[k]^h[k] for k in range(3))

    words = [field(t,p) for t,p in outputs]
    return [tuple(tuple((v[k] >> lane)&1 for k in range(3)) for v in words)
            for lane in range(len(assignments))]


def controls():
    p2,p5,g = (1,2,0),(0,3,0),(48,0,0)
    frontiers = [(1,7,0),(0,8,0),(53,0,0),(54,0,0)]
    outputs = [(5,p2),(5,p5),(5,g),(6,g)]
    assignments = list(product(TRIPLES,repeat=4))
    full_words = 0
    diagonal_checks = 0
    for background in (17,41):
        out = native(frontiers,assignments,outputs,background)
        require(len(set(out)) == 8**4, 'whole chronological native block is not bijective')
        full_words += len(out)
        # Conditional own-block permutations and no later-source dependence.
        for k in range(4):
            buckets = {}
            for row,word in zip(assignments,out):
                prefix = row[:k]
                buckets.setdefault(prefix,{}).setdefault(row[k],set()).add(word[k])
            for choices in buckets.values():
                require(all(len(v) == 1 for v in choices.values()), 'later source affects earlier output')
                require(len({next(iter(v)) for v in choices.values()}) == 8,
                        'diagonal map not a permutation')
                diagonal_checks += 1
        # The next herald-noise source cannot change its earlier public record.
        prefix = native(frontiers,assignments,[(t,g) for t in range(5)],background)
        require(len(set(prefix)) == 1, 'frontier corrupts earlier herald prefix')

    pinned_rows = [(a,b,c,TRIPLES[0]) for a,b,c in product(TRIPLES,repeat=3)]
    shared_rows = [(a,b,c,c) for a,b,c in product(TRIPLES,repeat=3)]
    pinned = native(frontiers,pinned_rows,outputs,17)
    shared = native(frontiers,shared_rows,outputs,17)
    require(len(set(pinned)) == 512, 'pinned source countercontrol')
    require(len(set(shared)) == 512, 'shared source countercontrol')
    # Reading an initially private new bank triple is an access change. Its
    # later raw record is a permutation, hence cannot remain independent of it.
    own = native([frontiers[2]],[(x,) for x in TRIPLES],[(5,g)],17)
    require(len(set(own)) == 8, 'extra-read deterministic response')
    require(len({(x,o[0]) for x,o in zip(TRIPLES,own)}) == 8,
            'extra-read dependence support')
    return {'complete_native_assignments':full_words,
            'conditional_diagonal_permutations':diagonal_checks,
            'herald_prefix_backgrounds':2,
            'pinned_support':len(set(pinned)), 'shared_support':len(set(shared)),
            'required_uniform_support':4096,
            'extra_private_bank_read_joint_support':8,
            'independent_extra_read_support_would_be':64}


def main():
    result = {'schema':'oi.native-y.history-v11.v1', 'geometry':geometry(),
              'native_controls':controls(),
              'verdict':'PASS_CONDITIONAL_EIGHT_PORT_HISTORY_EXTENSION',
              'scope':'Specified raw streams and initial bank complement only; no future full-boundary independence or native reusable instrument.'}
    print(json.dumps(result,sort_keys=True,separators=(',',':')))


if __name__ == '__main__':
    main()
