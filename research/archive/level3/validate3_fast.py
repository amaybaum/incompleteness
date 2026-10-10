"""PREREG-3A section 6 item 3: record3_fast.run_all3 == record3_sim.run3 on the full Stage-A protocol set for
kappa = ((0,1),(0,1)) and ((1,3),(0,2)) (linear), and on 300 random protocols of length <= 7 for three kappa
(all three rules, rule-generic code)."""
import random
import time
from itertools import product
from record3_sim import run3
from record3_fast import run_all3

random.seed(11)
INJ = [(x, y) for x in range(4) for y in range(4) if x != y]


def prots(alph, L):
    return [''.join(p) for l in range(L + 1) for p in product(alph, repeat=l)]


full = sorted({a + b for a in prots('oifsc', 3) for b in prots('oimfsc', 3)})
rnd = sorted({''.join(random.choice('oimfscp') for _ in range(random.randint(0, 7))) for _ in range(330)})[:300]
sets = [('3A-full', full, [((0, 1), (0, 1)), ((1, 3), (0, 2))], ('linear',)),
        ('3A-random', rnd, [(random.choice(INJ), random.choice(INJ)) for _ in range(3)],
         ('linear', 'nonlinear', 'majority'))]
ok = True
for name, ps, kappas, rules in sets:
    for rule in rules:
        for kappa in kappas:
            t = time.time()
            fast = run_all3(ps, rule, kappa)
            tf = time.time() - t
            bad = sum(1 for p in ps if fast[p] != run3(p, rule, kappa))
            ok = ok and bad == 0
            print(f"V0' {name} {rule} {kappa}: {len(ps)} protocols, mismatches {bad}, fast {tf:.1f}s", flush=True)
print("V0'", 'OK' if ok else 'FAILED')
