"""Exact, standard-library checks for the OI interface investigation, 2026-10-21.

Calibration only: the operation menu, preparation menu and fresh read resources
are declared here, not derived from the OI lattice. No repository is accessed.
"""
from fractions import Fraction as F
from itertools import permutations, product
import json


def insert(basis, vector):
    v = list(map(F, vector))
    for pivot, row in basis:
        c = v[pivot]
        if c:
            v = [a - c * b for a, b in zip(v, row)]
    p = next((i for i, x in enumerate(v) if x), None)
    if p is None:
        return False
    c = v[p]
    basis.append((p, [x / c for x in v]))
    basis.sort()
    return True


def pull(row, matrix):
    return tuple(sum(row[i] * matrix[i][j] for i in range(len(row)))
                 for j in range(len(row)))


def pm(p):
    return tuple(tuple(F(i == p[j]) for j in range(len(p)))
                 for i in range(len(p)))


def closure(ops, size):
    basis = []
    one = (F(1),) * size
    insert(basis, one)
    words = [(one, ())]
    dims = [1]
    while True:
        old = list(words)
        for row, word in old:
            for name, matrix in ops:
                r = pull(row, matrix)
                if insert(basis, r):
                    words.append((r, (name,) + word))
        dims.append(len(words))
        if len(old) == len(words):
            return basis, words, dims


def bit(s, k):
    return (s >> k) & 1


def coordinates(s, site=0):
    u, v = (-1) ** bit(s, 2 * site), (-1) ** bit(s, 2 * site + 1)
    return F(u - v, 2), F(u + v, 2)


def rotate(s, site=0):
    k = 2 * site
    a, b = bit(s, k), bit(s, k + 1)
    return (s & ~(3 << k)) | (b << k) | ((1 - a) << (k + 1))


def interaction(s):
    # (a_A,b_A,a_B,b_B) -> (a_A,b_A XOR b_B,a_B XOR a_A,b_B)
    return s ^ (bit(s, 0) << 2) ^ (bit(s, 3) << 1)


def omega(s, t):
    return sum(bit(s, 2*k)*bit(t, 2*k+1) +
               bit(s, 2*k+1)*bit(t, 2*k) for k in range(2)) % 2


def operations(n, passive=False, interacting=False):
    size = 4 ** n
    ops = [("R_" + "AB"[k], pm([rotate(s, k) for s in range(size)]))
           for k in range(n)]
    if interacting:
        assert n == 2
        ops.append(("G", pm([interaction(s) for s in range(size)])))
    for k in range(n):
        for axis, name in enumerate(("X", "Z")):
            for sign in (1, -1):
                target = next(r for r in range(4)
                              if coordinates(r)[axis] == sign)
                matrix = [[F(0)] * size for _ in range(size)]
                for s in range(size):
                    out = s if passive else (s & ~(3 << (2*k))) | (target << (2*k))
                    matrix[out][s] = (1 + sign * coordinates(s, k)[axis]) / 2
                ops.append((name + "_" + "AB"[k] + ("+" if sign == 1 else "-"), matrix))
    return ops


def probability(row, prep):
    return sum(x * y for x, y in zip(row, prep))


def rho(v):
    x, z = v
    return ((F(1+z, 2), F(x, 2)), (F(x, 2), F(1-z, 2)))


def multiply(a, b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def physical_read(s, site, axis, coin):
    """Restricted input of an explicitly reversible apparatus circuit.

    Fresh outcome register r=0 and garbage registers g,h=0. Compute outcome
    into r, swap old a,b into g,h, then XOR the reset pattern into a,b.
    These are reversible XOR/swap steps on the full register space.
    Only s and the outcome record are accessible afterward; old bits and coin
    are retained in inaccessible registers. Every read uses fresh registers.
    """
    a, b = bit(s, 2*site), bit(s, 2*site+1)
    r = a if coin == 0 else b ^ (axis == "X")
    new_a, new_b = r, r ^ (axis == "X")
    out = (s & ~(3 << (2*site))) | (new_a << (2*site)) | (new_b << (2*site+1))
    return out, r, (a, b, coin)


def run():
    result = {}
    M, Mt = ((1, -1), (1, 1)), ((1, 1), (-1, 1))
    for s in range(4):
        t = multiply(multiply(M, rho(coordinates(s))), Mt)
        assert tuple(tuple(x/2 for x in row) for row in t) == rho(coordinates(rotate(s)))
    result["coherent_rotation_intertwining"] = "4/4 exact"
    b1, w1, d1 = closure(operations(1), 4)
    _, _, dp = closure(operations(1, passive=True), 4)
    assert d1 == [1, 3, 3] and dp == [1, 3, 4, 4]
    result["reset_read_span"] = d1
    result["passive_read_span"] = dp
    kz = tuple((-1)**s.bit_count() for s in range(4))
    good = []
    for p in permutations(range(4)):
        if all(sum(x*y for x,y in zip(pull(row, pm(p)), kz)) == 0 for row,_ in w1):
            good.append(p)
    assert len(good) == 8
    result["single_system_compatible_permutations"] = "8/24"
    pz = tuple(F(1,2) if s in (0,3) else F(0) for s in range(4))
    px = tuple(F(1,2) if s in (1,2) else F(0) for s in range(4))
    ex = tuple((1+coordinates(s)[0])/2 for s in range(4))
    ez = tuple((1+coordinates(s)[1])/2 for s in range(4))
    assert (probability(tuple(x*x for x in ex), pz),
            probability(tuple(x*x for x in ex), px)) == (F(1,4), F(1,2))
    # In the previous cyclic labels, this is the swap of labels 1 and 2.
    row = pull(ez, pm((0,1,3,2)))
    assert (probability(row,pz),probability(row,px)) == (F(3,4),F(1,4))
    result["passive_X_plus_plus"] = ["1/4", "1/2"]
    result["swap_then_Z_plus"] = ["3/4", "1/4"]
    # Exact projector certificate for all compatible two-system permutations.
    masks = [0,1,2,4,8,5,9,6,10]
    W = [[(-1)**((m&s).bit_count()%2) for s in range(16)] for m in masks]
    assert all(sum(a*b for a,b in zip(W[i],W[j])) == (16 if i==j else 0)
               for i in range(9) for j in range(9))
    G = [[sum(w[i]*w[j] for w in W) for j in range(16)] for i in range(16)]
    autos = []
    def visit(mapping, unused):
        if not unused:
            autos.append(tuple(mapping[i] for i in range(16)))
            return
        best, choices = None, None
        for i in range(16):
            if i in mapping:
                continue
            cand = [j for j in unused if all(G[i][k] == G[j][v] for k,v in mapping.items())]
            if not cand:
                return
            if choices is None or len(cand) < len(choices):
                best, choices = i, cand
        for j in choices:
            mapping[best] = j
            visit(mapping, unused - {j})
            del mapping[best]
    visit({}, set(range(16)))
    expected = set()
    for swap, fa, fb in product((0,1), repeat=3):
        order = ([1,0] if fa else [0,1]) + ([3,2] if fb else [2,3])
        if swap:
            order = order[2:] + order[:2]
        for shifts in range(16):
            expected.add(tuple(sum((bit(s,order[k]) ^ bit(shifts,k)) << k for k in range(4))
                               for s in range(16)))
    assert len(autos) == 128 and set(autos) == expected
    result["product_quotient_automorphisms"] = "128 = 8*8*2; local symmetries and system exchange only"
    assert all(interaction(interaction(s)) == s for s in range(16))
    assert all(omega(interaction(s),interaction(t)) == omega(s,t)
               for s in range(16) for t in range(16))
    result["interaction"] = "bijective involution; preserves binary symplectic form"
    _, _, db = closure(operations(2),16)
    bi, wi, di = closure(operations(2,interacting=True),16)
    assert db == [1,5,9,9] and di == [1,5,9,10,16,16]
    result["product_protocol_span"] = db
    result["interacting_protocol_span"] = di
    # With only reversible words before a final product test, the span is 10.
    basis=[]; actual=[]
    for row in W:
        if insert(basis,row): actual.append(tuple(row))
    perms = operations(2,interacting=True)[:3]
    while True:
        old=list(actual)
        for row in old:
            for _,K in perms:
                v=pull(row,K)
                if insert(basis,v):actual.append(v)
        if len(old)==len(actual):break
    assert len(actual)==10
    result["reversible_words_then_product_tests_span"] = 10
    A = tuple(F(1,8) if bit(s,0)==bit(s,1) else F(0) for s in range(16))
    B = tuple(F(1,8) if bit(s,0)!=bit(s,1) else F(0) for s in range(16))
    op = dict(operations(2,interacting=True))
    word = ("X_B+", "G", "X_B+", "X_A+")
    row = (F(1),)*16
    for step in reversed(word):row=pull(row,op[step])
    probs = (probability(row,A),probability(row,B))
    assert probs == (F(1,4),F(3,16))
    result["four_step_witness"] = {"word":word,"probabilities":[str(x) for x in probs]}
    # Independent finite-seed enumeration of the same apparatus experiment.
    counts=[]
    for parity in (0,1):
        count=total=0
        for s in range(16):
            if (bit(s,0)^bit(s,1)) != parity:continue
            for coins in product((0,1), repeat=3):
                t,r1,_=physical_read(s,1,"X",coins[0])
                t=interaction(t)
                t,r2,_=physical_read(t,1,"X",coins[1])
                t,r3,_=physical_read(t,0,"X",coins[2])
                count += (r1,r2,r3)==(0,0,0)
                total += 1
        counts.append((count,total))
    assert counts == [(16,64),(12,64)]
    result["independent_seed_enumeration"] = counts
    assert max(abs(a*c+a*d+b*c-b*d) for a,b,c,d in product((-1,1), repeat=4))==2
    result["local_classical_CHSH_bound"] = 2
    return result


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
