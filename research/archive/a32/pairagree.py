"""Exploration only (exact, symbolic): for each circle r != 0 find relabellings (pi,tau) whose
feature map agrees with phi on C0 u C_r, i.e. (pi,tau)F(z) has the features of F(conj z) and
(pi,tau) r F(w) has the features of r F(w), for all unit z, w (symbol-wise identities).
Also the conj-composed variant (shape 2)."""
import itertools
import cover as C
perms = C.perms
out = {}
for r in range(1, 9):
    sols = []
    for pt, s in C.S_ALL.items():
        ok0 = all(C.data[0][s[n]] == C.cj(C.data[0][n]) for n in range(4096))
        if not ok0: continue
        okr = all(C.data[r][s[n]] == C.data[r][n] for n in range(4096))
        if okr: sols.append(pt)
    sols2 = []
    for pt, s in C.S_ALL.items():
        ok0 = all(C.cj(C.data[0][s[n]]) == C.cj(C.data[0][n]) for n in range(4096))
        if not ok0: continue
        okr = all(C.cj(C.data[r][s[n]]) == C.data[r][n] for n in range(4096))
        if okr: sols2.append(pt)
    print("circle", r, C.R[r], "pure relabellings:", len(sols), sols[:4], "| conj-composed:", len(sols2), sols2[:2])
