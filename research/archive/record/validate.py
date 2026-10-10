"""V0: the window simulator with the passive interface reproduces the midpoint simulator of QUOTIENT exactly."""
import sys, random
from fractions import Fraction as Fr
sys.path.insert(0, '../quotient'); sys.path.insert(0, '../rank')
from quotient import joint
from record_sim import run
random.seed(3)
prots = ['p', 'pp', 'pip', 'pfp', 'psp', 'ppp', 'pipp', 'spfp', 'ppppp', 'pifsp', 'ppspp', 'pppppp', 'ipipip', 'sppsfpi']
prots += [''.join(random.choice('pifs') for _ in range(random.randint(1, 7))) for _ in range(20)]
ok = True
for rule in ('linear', 'nonlinear', 'majority'):
    bad = 0
    for pr in prots:
        c, tot = run(pr, rule, None if False else ((0, 1), (2, 3)))
        new = [Fr(x, tot) for x in c]
        old = joint(pr.replace('p', 'o'), rule)
        if new != old:
            bad += 1
    print(f'V0 {rule}: {len(prots)} protocols, mismatches {bad}')
    ok = ok and bad == 0
print('V0', 'OK' if ok else 'FAILED')
