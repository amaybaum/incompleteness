import sys, itertools
sys.path.insert(0, sys.argv[1])
from pe01 import observers as O
forms = O.canonical_passive(8)
keys = set()
for k, (r0, r1) in forms:
    keys.add((k, tuple(r0), tuple(r1)))
print("forms", len(forms), "distinct", len(keys))
def canon(r0, r1, V):
    # BFS relabelling of the component reachable from 0
    lab = {0: 0}; order = [0]; i = 0
    while i < len(order):
        s = order[i]
        for r in (r0, r1):
            t = r[s]
            if t not in lab:
                lab[t] = len(order); order.append(t)
        i += 1
    k = len(order)
    return (k, tuple(lab[r0[s]] for s in order), tuple(lab[r1[s]] for s in order))
# completeness for pairs on V = 4 points (covers every class with k <= 4)
V = 4
seen = set()
for r0 in itertools.permutations(range(V)):
    for r1 in itertools.permutations(range(V)):
        seen.add(canon(r0, r1, V))
mine = {x for x in keys if x[0] <= 4}
print("k<=4 classes from Sym(4)^2:", len(seen), "generated:", len(mine), "equal:", seen == mine)
# every generated form is reachable and canonical
bad = sum(1 for (k, a, b) in keys if canon(list(a), list(b), k) != (k, a, b))
print("non-canonical or unreachable forms:", bad)
