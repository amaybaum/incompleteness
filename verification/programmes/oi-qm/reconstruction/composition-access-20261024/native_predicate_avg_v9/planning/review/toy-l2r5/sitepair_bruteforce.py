"""Reviewer probe (non-v8 analogues only): l2sitepairs.count against a brute-force canonical-image count
written independently (every slice pair of every site pair; the record order is (site, slice, site,
slice) with sites in lexicographic order; a representative is the minimum of its images).
Usage: python3 -I -B sitepair_bruteforce.py <layer2/code> RHO NT"""
import sys, itertools, json
code, rho, nt = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
assert rho != 4
sys.path.insert(0, code)
import l2sitepairs as C
reg = sorted(c for c in itertools.product(range(-rho, rho + 1), repeat=3) if sum(map(abs, c)) <= rho)
idx = {c: i for i, c in enumerate(reg)}
G = []
for sw in (False, True):
    for sx in (1, -1):
        for sy in (1, -1):
            G.append([idx[(sx*c[1], sy*c[0], c[2]) if sw else (sx*c[0], sy*c[1], c[2])] for c in reg])
ns = len(reg)
pairs = []
for i in range(ns):
    for j in range(i + 1, ns):
        n = 0
        for t1 in range(nt):
            for t2 in range(nt):
                me = (i, t1, j, t2)
                if all(((a, t1, b, t2) if a < b else (b, t2, a, t1)) >= me for a, b in ((p[i], p[j]) for p in G)):
                    n += 1
        pairs.append(n)
singles = [nt if all(p[i] >= i for p in G) else 0 for i in range(ns)]
c = C.count({'dim': 3, 'rho': rho, 'tlast': nt - 2, 'port': (0, 0, -2)})
kinds = {k: sum(1 for v in pairs if v == val) for k, val in (('none', 0), ('all', nt*nt), ('upper', nt*(nt+1)//2), ('strict', nt*(nt-1)//2))}
print(json.dumps({'rho': rho, 'nt': nt, 'sites': ns, 'pairs_equal': pairs == c['pairs_representatives'],
                  'singles_equal': singles == c['singles_representatives'], 'R': sum(pairs) + sum(singles),
                  'R_module': c['representatives_total'], 'burnside': c['burnside_orbits'], 'kinds': kinds,
                  'mismatched_pairs': sum(1 for a, b in zip(pairs, c['pairs_representatives']) if a != b)}))
