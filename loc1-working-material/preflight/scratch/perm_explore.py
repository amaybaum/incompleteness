import sys, time
sys.path.insert(0, sys.argv[1])
from c21_engine import Engine, SM64
from c21_search import perm_of_type, perm_matrix, product_type_formula, partitions
adm = {product_type_formula(a,b) for a in partitions(4) for b in partitions(4)}
types = [(2,2,2)+(1,)*10, (2,)*5+(1,)*6, (2,)*7+(1,)*2, (3,3)+(1,)*10, (3,3,3)+(1,)*7, (3,2)+(1,)*11,
         (4,)+(1,)*12, (4,4)+(1,)*8, (2,2,2,2,2,2)+(1,)*4, (6,3,3,2,1,1), (3,3,3,3,3,1), (5,1)+(1,)*10]
rng = SM64(99)
for ct in types:
    pi = perm_of_type(list(ct), rng.shuffle(range(16)))
    E = Engine([perm_matrix(pi)], 4, 4)
    t = time.perf_counter(); st, f, s = E.run("exist", budget=3*10**7); t = time.perf_counter() - t
    print(ct, "admitted" if ct in adm else "excluded", st, s, "%.1fs" % t, flush=True)
