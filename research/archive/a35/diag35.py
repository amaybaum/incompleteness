"""Diagnosis of the frozen probe's floating-point stabilizer count for F4⊗F4: the rounded-bytes comparison against a tolerance comparison,
and how many rounded matrices differ from the reference only by the sign of a zero."""
import numpy as np, itertools, re
src = open('dita_defect_probe.py.frozen', encoding='utf-8').read()
head = src[:src.index("print('== 1.")]
sec1 = src[src.index("print('== 1."):src.index("print('== 2.")]
defs = '\n'.join(l for l in sec1.split('\n') if re.match(r'^[A-Za-z_][A-Za-z0-9_]* = ', l) and 'check(' not in l)
ns = {}; exec(head + '\n' + defs, ns)
F4F4 = ns['F4F4']
def to_np(H): return np.array([[complex(float(x.a), float(x.b)) for x in row] for row in H]) / 4
def dephase(H):
    H = H / (H[:, :1] / np.abs(H[:, :1])); return H / (H[:1, :] / np.abs(H[:1, :]))
S4 = list(itertools.permutations(range(4)))
def prod_perm(p, q): return [4 * p[a] + q[b] for a in range(4) for b in range(4)]
SW = [4 * b + a for a in range(4) for b in range(4)]
col_perms = np.array([prod_perm(t1, t2) for t1 in S4 for t2 in S4])
Hn = to_np(F4F4); c0m = np.round(dephase(Hn) * 4, 6); c0 = c0m.tobytes()
bytes_eq = tol_eq = zero_sign_only = 0
for sw in (False, True):
    for cj in (False, True):
        for tr in (False, True):
            H1 = Hn.copy()
            if sw: H1 = H1[np.ix_(SW, SW)]
            if cj: H1 = np.conj(H1)
            if tr: H1 = H1.T
            for p1 in S4:
                for p2 in S4:
                    B = H1[prod_perm(p1, p2), :][:, col_perms]; B = np.transpose(B, (1, 0, 2))
                    B = B / (B[:, :, :1] / np.abs(B[:, :, :1])); B = B / (B[:, :1, :] / np.abs(B[:, :1, :]))
                    Bc = np.round(B * 4, 6)
                    close = np.abs(Bc - c0m).max(axis=(1, 2)) < 1e-9
                    tol_eq += int(close.sum())
                    for m in np.nonzero(close)[0]:
                        if Bc[m].tobytes() == c0: bytes_eq += 1
                        else: zero_sign_only += 1
print('rounded-bytes equal:', bytes_eq, ' tolerance equal:', tol_eq, ' equal up to the sign of a zero:', zero_sign_only)
