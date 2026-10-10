"""V2: record_fast.run_all equals record_sim.run (validated by V0, V1) on every protocol checked."""
import random
import time
from itertools import product
from record_sim import run
from record_fast import run_all

random.seed(11)
INJ = [(x, y) for x in range(4) for y in range(4) if x != y]


def prots(alph, L):
    return [''.join(p) for l in range(L + 1) for p in product(alph, repeat=l)]


sets = []
# full Level-1 Stage-A protocol set (prep + effect concatenations) for two interfaces
l1 = sorted({a + b for a in prots('oi', 3) for b in prots('oim', 3)})
sets.append(('L1-full', l1, [((1, 0), (2, 3)), ((2, 3), (0, 1))]))
# random Level-2 protocols up to 7 letters, random invasive interfaces
l2 = sorted({''.join(random.choice('oimfsp') for _ in range(random.randint(0, 7))) for _ in range(400)})
sets.append(('L2-random', l2, [(random.choice(INJ), random.choice(INJ)) for _ in range(3)]))
ok = True
for name, ps, kappas in sets:
    for rule in ('linear', 'nonlinear', 'majority'):
        for kappa in kappas:
            t = time.time()
            fast = run_all(ps, rule, kappa)
            tf = time.time() - t
            bad = sum(1 for p in ps if fast[p] != run(p, rule, kappa))
            ok = ok and bad == 0
            print(f'V2 {name} {rule} {kappa}: {len(ps)} protocols, mismatches {bad}, fast {tf:.1f}s', flush=True)
print('V2', 'OK' if ok else 'FAILED')
