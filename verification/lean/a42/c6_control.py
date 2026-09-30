"""C6: the exact class-support method against brute force on random 6 x 6 instances. The exact value is attained by an
exhibited representative, so it can only be below a boxed brute force; any gap must close when the box is enlarged."""
import random, time, numpy as np
import minsupp_exact as M
t0 = time.time(); rng = random.Random(7); tried = 0; eq = 0; closed = 0; wrong = 0; widened = []
while tried < 150:
    n = 6; s = rng.randint(3, 16)
    E = np.zeros((n, n), dtype=np.int64)
    for p in rng.sample(range(n * n), s): E[p // n, p % n] = rng.choice([-1, 1])
    E = E + np.array([rng.randint(-2, 2) for _ in range(n)])[:, None] + np.array([rng.randint(-2, 2) for _ in range(n)])[None, :]
    try: sup, al, be, _ = M.class_support(E)
    except ValueError: continue
    tried += 1
    bf = M.brute(E, 4)
    if bf == sup: eq += 1; continue
    if bf < sup: wrong += 1; continue
    bf8 = M.brute(E, 8); widened.append((sup, bf, bf8)); closed += (bf8 == sup); wrong += (bf8 < sup)
print('C6: %d instances; %d equal at box 4; %d gaps, %d closed at box 8; exact above brute: %d (%.0fs)' % (tried, eq, len(widened), closed, wrong, time.time() - t0))
print('  widened:', widened)
