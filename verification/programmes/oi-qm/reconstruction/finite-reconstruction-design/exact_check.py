#!/usr/bin/env python3
"""Exact k=3 design controls; finite evidence, not a universal/kernel verdict.

Run with SymPy 1.14.0. No existing probe or Lean module is imported.
The five --self-test mutations must fail at their named control.
"""
import argparse
from itertools import product, permutations
import sympy as s

Q, I = s.Rational, s.I
E = s.eye(2)
X = s.Matrix([[0, 1], [1, 0]])
Y = s.Matrix([[0, -I], [I, 0]])
Z = s.diag(1, -1)
PAULI = (E, X, Y, Z)


def tensor(*xs):
    out = s.Matrix([[1]])
    for x in xs:
        out = s.kronecker_product(out, x)
    return out


def eq(a, b):
    return all(s.simplify(x) == 0 for x in a - b)


def ket(n, a):
    return s.eye(n)[:, a]


def projector(v):
    return v * v.H


def local(g, j, k=3):
    return tensor(*(g if t == j else E for t in range(k)))


def cnot(i, j, k=3):
    out = s.zeros(2**k)
    for a in range(2**k):
        b = a ^ (1 << (k - 1 - j)) if (a >> (k - 1 - i)) & 1 else a
        out[b, a] = 1
    return out


def ptran(a, token, k=3):
    out = s.zeros(2**k)
    bit = 1 << (k - 1 - token)
    for i, j in product(range(2**k), repeat=2):
        ii, jj = (i ^ bit, j ^ bit) if bool(i & bit) != bool(j & bit) else (i, j)
        out[ii, jj] = a[i, j]
    return out


def pure_product(v):
    return all(s.Matrix([[v[a] for a in range(8) if ((a >> (2-j)) & 1) == b]
                         for b in (0, 1)]).rank() == 1 for j in range(3))


def run(mutation=None, quiet=False):
    checks = []

    def check(label, yes):
        if not yes:
            raise AssertionError(label)
        checks.append(label)

    paulis = [tensor(*(PAULI[t] for t in mu)) for mu in product(range(4), repeat=3)]
    # Inverse applied to a Hermitian matrix with complex off-diagonal entries.
    v = s.Matrix([1, 2+I, -I, 3, 1-I, 2, -1, I])
    a = projector(v) - 2 * projector(ket(8, 3))
    coeff = [s.trace(a * p) for p in paulis]
    factor = 4 if mutation == "trace-factor" else 8
    reconstructed = sum((c*p for c, p in zip(coeff, paulis)), s.zeros(8)) / factor
    check("DICT3", eq(reconstructed, a))
    check("REAL3", all(s.simplify(s.im(c)) == 0 for c in coeff))
    check("ORTHOGONALITY-LOCAL", all(s.trace(p*q) == (2 if i == j else 0)
          for i, p in enumerate(PAULI) for j, q in enumerate(PAULI)))
    for j, p in enumerate(paulis):
        check(f"PAULI3-{j}", p.H == p and p*p == s.eye(8))
    for j, ranks in enumerate(((1,1,1), (1,1,2), (1,2,2), (2,2,2))):
        parts = [s.diag(1, r-1) for r in ranks]
        p = tensor(*parts)
        check(f"PRODUCT3-{j}", p.is_positive_semidefinite and p.rank() == s.prod(ranks))

    # A direct finite gate circuit versus independent branchwise signed products.
    # Both one-axis families obey X R X = R^-1, with rational Q(i) entries.
    circles = [(Q(3,5),Q(4,5)), (Q(5,13),Q(12,13)),
               (Q(8,17),Q(15,17)), (Q(7,25),Q(24,25))]
    gray = [0, 1, 3, 2]
    for axis in ("y", "z"):
        rots = [s.Matrix([[c,-t],[t,c]]) if axis == "y" else s.diag(c+I*t,c-I*t)
                for c,t in circles]
        u = s.eye(8)
        for j, r in enumerate(rots):
            u = local(r, 2) * u
            if mutation == "open-gray" and j == 3:
                continue
            changed = gray[j] ^ gray[(j+1) % 4]
            control = 1 if changed == 1 else 0
            u = cnot(control, 2) * u
        blocks = []
        for b in range(4):
            block = E
            for g, r in zip(gray, rots):
                odd = (b & g).bit_count() % 2
                if mutation == "mux-sign":
                    odd = 0
                block = (r.H if odd else r) * block
            blocks.append(block)
        check(f"DEMUX3-{axis}", eq(u, s.diag(*blocks)))
        adj = u.T if mutation == "adjoint" else u.H
        check(f"ADJOINT3-{axis}", eq(adj*u, s.eye(8)))
        check(f"MUX-PREPARATION-{axis}", eq(u * s.Matrix([1,0,2,0,3,0,4,0]),
              s.Matrix.vstack(*(b*s.Matrix([j+1,0]) for j,b in enumerate(blocks)))))

    # Independently construct the arbitrary SU(2) family in the written recursion.
    for j, x in enumerate((s.zeros(8,1), ket(8,0), ket(8,7),
                           ket(8,0)+ket(8,7), v)):
        bs, rs = [], []
        for b in range(4):
            p, q = x[2*b], x[2*b+1]
            r = s.sqrt(s.expand_complex(p*s.conjugate(p)+q*s.conjugate(q)))
            su = E if r == 0 else s.Matrix([[p,-s.conjugate(q)],[q,s.conjugate(p)]])/r
            check(f"SU-BLOCK-{j}-{b}", eq(su.H*su,E) and s.simplify(su.det()-1)==0)
            bs.append(su)
            rs.extend((r,0))
        check(f"REACH3-BLOCK-{j}", eq(s.diag(*bs)*s.Matrix(rs),x))

    # Hypothesis failures are literal witnesses; family claims are in argument.md.
    check("ZERO3", s.zeros(8) != projector(ket(8,0)))
    check("SCALE3", s.trace(projector(ket(8,0))/2) < 1)
    a2 = s.diag(1,1,0,0,0,0,0,0)
    a1 = projector(ket(8,2))
    check("ADD3", a2.rank() in (0,1,2,4,8) and a1.rank() in (0,1,2,4,8)
          and (a1+a2).rank() == 3)
    shift = s.eye(8)-2*projector(ket(8,0))
    check("SHIFT3", (shift+s.trace(shift)*s.eye(8)/6).is_positive_semidefinite
          and (ket(8,0).H*shift*ket(8,0))[0] == -1)
    cp = cnot(0,1) * tensor(s.Matrix([1,1])/s.sqrt(2),ket(2,0),ket(2,0))
    check("SEP3", ptran(projector(cp),0).extract([2,4],[2,4]).det()==-Q(1,4))
    bell01 = (ket(8,0)+ket(8,6))/s.sqrt(2)
    cutgate = cnot(2,1) if mutation == "cut-direction" else cnot(1,2)
    ghz = cutgate*bell01
    check("CUT3", ptran(projector(ghz),2).extract([1,6],[1,6]).det()==-Q(1,4))

    # Exhaust all invertible binary 3x3 maps: the actual CNOT orbit group.
    maps = []
    for columns in permutations(range(1,8),3):
        perm = [0]*8
        for t in range(8):
            for j in range(3):
                if (t >> j) & 1:
                    perm[t] ^= columns[j]
        if len(set(perm)) == 8:
            maps.append(perm)
    check("GROUP3", len(maps)==168 and len({tuple(p) for p in maps})==168)
    source = tensor(s.Matrix([3,4]),s.Matrix([5,12]),s.Matrix([1,2]))
    source = cnot(1,2)*cnot(0,1)*source
    cyc = s.Matrix([[(1-I)/2,(-1-I)/2],[(1-I)/2,(1+I)/2]])
    for token in (1,2):
        dest = local(cyc,token)*source
        check(f"ORBIT3-{token}", all(not pure_product(s.Matrix([dest[p[t]] for t in range(8)]))
                                      for p in maps))

    g = ket(8,0)+ket(8,7)
    w = s.eye(8)-Q(3,4)*projector(g)
    check("SLICE3-NEGATIVE", (g.H*w*g)[0] == -1)
    unitvectors = (ket(2,0),ket(2,1),s.Matrix([3,4])/5,
                   s.Matrix([3,4*I])/5,s.Matrix([1,1])/s.sqrt(2))
    for j, p in enumerate(product(unitvectors, repeat=3)):
        q = tensor(*p)
        check(f"SLICE3-PRODUCT-{j}", s.simplify((q.H*w*q)[0]-Q(1,4)) >= 0)
    drive = cnot(0,2)*cnot(0,1)
    test = tensor(s.Matrix([1,1])/s.sqrt(2),ket(2,0),ket(2,0))
    check("SLICE3-EXPOSED", (test.H*drive*w*drive.H*test)[0]==-Q(1,2))

    # Literal spectator/relabel/block construction, with an arbitrary complex K.
    for small, large in ((3,4),(3,8),(5,8)):
        embedding = list(range(large-small,large))
        partial = {(0,embedding[j]): (j,0) for j in range(small)}
        old = list(product(range(small),range(large)))
        new = list(product(range(small),range(large)))
        restold = [r for r in old if r not in partial]
        restnew = [r for r in new if r not in partial.values()]
        relabel = dict(partial)
        relabel.update(zip(restold,restnew))
        inverse = {v:k for k,v in relabel.items()}
        k = s.Matrix(large,large,lambda a,b: a+2*b+I*(a-b))
        block = s.Matrix(small,small,lambda a,b:
                  (1 if inverse[(a,0)][0]==inverse[(b,0)][0] else 0)
                  * k[inverse[(a,0)][1],inverse[(b,0)][1]])
        check(f"COMPRESS-{small}-{large}", len(inverse)==small*large
              and block==k.extract(embedding,embedding))
    check("NONUNITARY-COMPRESSION", cnot(0,1,k=2).extract([0,2],[0,2]).det()==0)
    if not quiet:
        for label in checks:
            print("PASS",label)
        print(f"checks: {len(checks)}, failures: 0")
        print("DESIGN EVIDENCE: exact k=3 controls; no all-k kernel certification")
    return len(checks)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test",action="store_true")
    args = parser.parse_args()
    run()
    if args.self_test:
        for mutation, label in (("trace-factor","DICT3"),("adjoint","ADJOINT3-z"),
                                ("open-gray","DEMUX3-y"),("mux-sign","DEMUX3-y"),
                                ("cut-direction","CUT3")):
            try:
                run(mutation,quiet=True)
            except AssertionError as exc:
                if str(exc) != label:
                    raise AssertionError(f"{mutation}: expected {label}, got {exc}") from exc
                print(f"REJECTED {mutation}: {label}")
            else:
                raise AssertionError(f"accepted mutation: {mutation}")
        print("mutations: 5 rejected, 0 accepted")


if __name__ == "__main__":
    main()
