"""rv_p2 -- independent reviewer check of the one-step identity behind ASSESS-1049 row 3c
(WIP / UNVERIFIED, model-written). Imports nothing from probes/.

Identity checked (an algebraic identity of a generic map over F_2, one step, no dynamics run):
  for symmetric zero-diagonal K, any offset b, the step (u, v) -> (K u + b - v, u) satisfies
  Q(step) = Q(u, v) + b.u   with Q(u, v) = sum_i u_i v_i (mod 2).
Control: with b = 0 the identity is QP Lemma Q(i) (conservation).
Countercontrol: a nonzero diagonal (centre term) breaks conservation at b = 0.
"""
import itertools, sys

def Q(u, v):
    return sum(a & b for a, b in zip(u, v)) & 1

ok = True
for n in (3, 4):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    vecs = list(itertools.product((0, 1), repeat=n))
    n_cases = 0
    for bits in itertools.product((0, 1), repeat=len(pairs)):
        K = [[0] * n for _ in range(n)]
        for (i, j), w in zip(pairs, bits):
            K[i][j] = K[j][i] = w
        for b in vecs:
            for u in vecs:
                Ku = [sum(K[i][j] & u[j] for j in range(n)) & 1 for i in range(n)]
                bu = sum(x & y for x, y in zip(b, u)) & 1
                for v in vecs:
                    u2 = tuple((Ku[i] + b[i] + v[i]) & 1 for i in range(n))
                    if Q(u2, u) != (Q(u, v) + bu) & 1:
                        ok = False
                    n_cases += 1
    print(f"n={n}: identity Q(step) = Q + b.u checked on {n_cases} cases: {'PASS' if ok else 'FAIL'}")
    # complement rule b = 1 breaks conservation somewhere
    one = (1,) * n
    broke = any(Q(tuple((v[i] + 1) & 1 for i in range(n)), u) != Q(u, v)  # K = 0 instance
                for u in vecs for v in vecs if sum(u) & 1)
    print(f"n={n}: uniform b=1 breaks Q-conservation: {'PASS' if broke else 'FAIL'}")
    ok &= broke
    # countercontrol: centre term at b = 0
    Kc = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    broke_c = any(Q(tuple((u[i] + v[i]) & 1 for i in range(n)), u) != Q(u, v) for u in vecs for v in vecs)
    print(f"n={n}: centre-term countercontrol breaks conservation: {'PASS' if broke_c else 'FAIL'}")
    ok &= broke_c
print("ALL PASS" if ok else "SOME FAIL")
sys.exit(0 if ok else 1)
