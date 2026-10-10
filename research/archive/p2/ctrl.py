# control: the table-driven partition equals the direct one on every subset of every matrix and block shape used
import itertools, time
src = open('wt-probe2/verification/lean/dita_hierarchy_probe.py', encoding='utf-8').read()
head = src[:src.index("print('== 1.")]                     # definitions and the matrices SIG, P, U60, W
exec(head)
U5 = G(Fr(3, 5), Fr(4, 5)); P5 = [[SIG[i][j] * gpow(U5, W[i * 16 + j]) for j in range(16)] for i in range(16)]
exec(src[src.index('def is_unitary_s'):src.index('PT = [list(c)')])
def prop_direct(H, S):
    keys = {}
    for i in range(16):
        base = H[i][S[0]]
        keys.setdefault(tuple((H[i][s] * base.conj()).key() for s in S), []).append(i)
    return sorted(tuple(v) for v in keys.values())
T = lambda H: [list(c) for c in zip(*H)]
bad = 0; n_ = 0; t = time.time()
for H in (P, P5, SIG, T(P), T(P5), T(SIG)):
    RT = ratio_table(H)
    for n in (4, 2, 8):
        for S in itertools.combinations(range(16), n):
            n_ += 1
            if prop_partition(RT, S) != prop_direct(H, S): bad += 1
print('subsets compared', n_, 'disagreements', bad, '(%.0fs)' % (time.time() - t))
