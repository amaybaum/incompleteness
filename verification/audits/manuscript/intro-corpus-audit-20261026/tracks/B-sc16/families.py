"""Explicit model families for SC-16 (exact).  State index s = x * nH + h."""
from fractions import Fraction as F
from oi_exact import Model

def uniform(n):
    return [F(1, n)] * n

def swap22():
    # phi(x,h) = (h,x)
    phi = [h * 2 + x for x in range(2) for h in range(2)]
    return Model(2, 2, phi, uniform(2), name='swap(2,2)')

def xor22():
    # phi(x,h) = (h, x xor h): X_0 = x, X_1 = h, X_2 = x xor h, period 3
    phi = [h * 2 + (x ^ h) for x in range(2) for h in range(2)]
    return Model(2, 2, phi, uniform(2), name='xor(2,2)')

def iid_coin22():
    # control without memory? phi(x,h)=(h,x) is swap (memory at order 0 via X_2=X_0); use a no-gap coin below.
    raise NotImplementedError

def static_shift(m, hs=None):
    """Static bath: phi(x,h) = (x + s_h mod m, h), hidden never changes (tau_B = infinity).
    hs: list of shifts s_h (default all of Z_m, nH = m)."""
    hs = list(range(m)) if hs is None else list(hs)
    nH = len(hs)
    phi = [((x + hs[h]) % m) * nH + h for x in range(m) for h in range(nH)]
    return Model(m, nH, phi, uniform(nH), name=f'static_shift(m={m},shifts={hs})')

def lfsr(mbits):
    """Visible bit x, hidden register (b1..bm) as integer h = sum b_i 2^{i-1}.
    phi(x, b1..bm) = (b1, (b2, .., bm, x xor b1)): X_{t+m+1} = X_t xor X_{t+1}."""
    nH = 2 ** mbits
    phi = [0] * (2 * nH)
    for x in range(2):
        for h in range(nH):
            b = [(h >> i) & 1 for i in range(mbits)]
            nb = b[1:] + [x ^ b[0]]
            nh = sum(v << i for i, v in enumerate(nb))
            phi[x * nH + h] = b[0] * nH + nh
    return Model(2, nH, phi, uniform(nH), name=f'lfsr(m={mbits})')
