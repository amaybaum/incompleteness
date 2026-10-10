"""EQ-B / B3: the role-exchange symmetry (principle shape (c)), exact search over signed permutations.

(c1) ROLEX(h):  SWAP . G . SWAP = (h (x) h) . G . (h (x) h)^-1   for one reversible map h of the copy
     (homogenized, fixing the unit), i.e. exchanging the copies is implemented by a local symmetry.
In QT the Hadamard (Bloch x <-> z, y -> -y) does this for CNOT.
We search h among the homogenized signed permutations of the d coordinates (2^d d! candidates) for
  cnot (d = 3), cnot1 (d = 1), gC5 (d = 5).
Also checked: the double frame (z-frame A -> B and the reversed frame B -> A on the corners +-hz).
Run: python3 -I -B b3_rolex.py
"""
import os
import sys
import itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from blib import *   # noqa: E402

checks = []


def chk(name, cond):
    checks.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)


def swap_op(n):
    S = zeros(n * n, n * n)
    for a in range(n):
        for b in range(n):
            S[b * n + a][a * n + b] = Fr(1)
    return S


def signed_perms(d):
    for perm in itertools.permutations(range(d)):
        for signs in itertools.product([1, -1], repeat=d):
            M = zeros(d, d)
            for i in range(d):
                M[perm[i]][i] = Fr(signs[i])
            yield M


def rolex_solutions(G, d):
    n = d + 1
    S = swap_op(n)
    lhs = matmul(S, matmul(G, S))
    sols = []
    for h in signed_perms(d):
        H = homMap(h)
        HH = kron(H, H)
        HHinv = kron(transpose(H), transpose(H))   # orthogonal
        if meq(matmul(HH, matmul(G, HHinv)), lhs):
            sols.append(h)
    return sols


def main():
    for name, d, G, z in (("cnot1", 1, cnot1(), Z1), ("cnot", 3, cnot3(), Z3), ("gC5", 5, gC5(), Z5)):
        sols = rolex_solutions(G, d)
        print(f"     {name}: {len(sols)} signed-permutation h with SWAP G SWAP = (h(x)h) G (h(x)h)^-1")
        for h in sols[:4]:
            print("        h =", [[int(x) for x in r] for r in h], " h z =", [str(t) for t in matvec(h, [Fr(t) for t in z])])
        if name == "cnot":
            chk("B3 control: cnot (QT CNOT) has a role-exchange symmetry (Hadamard-type signed permutation)",
                len(sols) > 0)
        if name == "cnot1":
            chk("B3 control: the classical gate cnot1 has NO role-exchange symmetry (its corners are the whole "
                "ball; the classical CNOT is not symmetric)", len(sols) == 0)
        if name == "gC5":
            gC5_sols = sols
            chk("B3 gC5 (d = 5, fails relC) HAS a role-exchange symmetry among signed permutations",
                len(sols) > 0)
    # double frame for gC5: B's +-x controls A's x-flip, x = e_1 (hom index 1)
    G = gC5()
    x5 = [1, 0, 0, 0, 0]
    hx, hmx = homvec(x5), homvec([-1, 0, 0, 0, 0])
    cor = [hx, hmx]
    ok = True
    for a in (0, 1):
        for b in (0, 1):
            # A (first slot) in corner b, B (second slot) in corner a: B controls A
            img = apply(G, outer(cor[b], cor[a]))
            if not meq(img, outer(cor[(a + b) % 2], cor[a])):
                ok = False
    chk("B3 gC5 has the reversed frame on the corners +-e_x (copy B controls copy A)", ok)
    nfail = sum(1 for _, okk in checks if not okk)
    print(f"b3_rolex: {len(checks) - nfail}/{len(checks)} checks PASS")
    print("VERDICT", "B3-GREEN" if nfail == 0 else "B3-RED")
    return 0 if nfail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
