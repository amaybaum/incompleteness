"""Controls, edge cases and tightness family (all decisions in interval arithmetic)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as F
from mpmath import iv
from cmi_iv import *

LN2 = iv.log(iv.mpf(2))
ok = True


def report(name, cond):
    global ok
    ok &= bool(cond)
    print(('PASS ' if cond else 'FAIL ') + name)


def overlap(I, q):
    Q = ivq(q)
    return I.a <= Q.b and Q.a <= I.b


def bits(x):
    return x / LN2


# --- C0: the two CMI formulas agree (overlapping intervals) on the probe's instances
# Q1 of the probe: X0 uniform, X1 uniform indep, X2 = X0  (k=1)
q1 = {((x0,), x1, (x0,)): F(1, 4) for x0 in (0, 1) for x1 in (0, 1)}
I1, I1b = cmi_nats(q1), cmi_nats_entropy(q1)
report('Q1: formulas overlap', I1.a <= I1b.b and I1b.a <= I1.b)
report('Q1: I = 1 bit (interval contains 1)', bits(I1).a <= 1 <= bits(I1).b)
hp = hypothesis_pairs(q1)
report('Q1: p0=1/4, delta=1 at both presents', all(h['p0'] == F(1, 4) and h['delta'] == 1 for h in hp) and len(hp) == 2)
report('Q1: bound holds', all(decide(I1, h['p0'] * h['delta'] ** 2) == 'holds' for h in hp))

# Q2: revival bijection, k=1, uniform over the 6 states
phiR = {(0, 0): (0, 0), (0, 1): (0, 1), (1, 0): (1, 0), (1, 1): (2, 0), (2, 0): (1, 1), (2, 1): (2, 1)}
q2 = {}
for s in phiR:
    s1 = phiR[s]; s2 = phiR[s1]
    key = ((s[0],), s1[0], (s2[0],))
    q2[key] = q2.get(key, F(0)) + F(1, 6)
I2, I2b = cmi_nats(q2), cmi_nats_entropy(q2)
report('Q2: formulas overlap', I2.a <= I2b.b and I2b.a <= I2.b)
report('Q2: I = 2/3 bit', overlap(bits(I2), F(2, 3)))
hp2 = hypothesis_pairs(q2)
best2 = max(hp2, key=lambda h: h['p0'] * h['delta'] ** 2)
report('Q2: best pair p0=1/6, delta=1', best2['p0'] == F(1, 6) and best2['delta'] == 1)
report('Q2: bound holds for every pair', all(decide(I2, h['p0'] * h['delta'] ** 2) in ('holds', 'tie0') for h in hp2))
print('    Q2 pairs:', [(h['c'], str(h['w1']), str(h['w2']), str(h['delta'])) for h in hp2])

# Q5: small-gap family
q5 = {}
for x0 in (0, 1):
    s = F(1, 8) if x0 == 0 else F(-1, 8)
    for x1 in (0, 1):
        for x2 in (0, 1):
            q5[((x0,), x1, (x2,))] = F(1, 4) * ((F(1, 2) + s) if x2 == 0 else (F(1, 2) - s))
I5 = cmi_nats(q5)
hp5 = hypothesis_pairs(q5)
report('Q5: p0=1/4, delta=1/4', all(h['p0'] == F(1, 4) and h['delta'] == F(1, 4) for h in hp5))
report('Q5: bound holds', all(decide(I5, h['p0'] * h['delta'] ** 2) == 'holds' for h in hp5))
print('    Q5: I_bits in', bits(I5), ' bound_bits =', bits(ivq(F(1, 64))))

# --- C1: tightness family.  Present c with P(c)=2 p0, two pasts of joint mass p0 each,
# laws ((1+d)/2,(1-d)/2) and ((1-d)/2,(1+d)/2); slack mass 1-2p0 on another present (I contribution 0).
def tight(p0, d):
    t = {}
    for a, sgn in ((0, 1), (1, -1)):
        t[(a, 'c', 0)] = p0 * (1 + sgn * d) / 2
        t[(a, 'c', 1)] = p0 * (1 - sgn * d) / 2
    if 1 - 2 * p0:
        t[(0, 'other', 0)] = 1 - 2 * p0
    return {k: v for k, v in t.items() if v}

print('Tightness family: ratio bound/I  (-> 1 as delta -> 0; = 1/(2 ln 2) at delta = 1)')
for d in (F(1), F(1, 2), F(1, 10), F(1, 100), F(1, 1000)):
    p0 = F(1, 2)
    t = tight(p0, d)
    I = cmi_nats(t)
    r = ivq(p0 * d * d) / I
    print(f'    delta={str(d):>7}  I_bits in [{float(bits(I).a):.10g}, {float(bits(I).b):.10g}]   ratio in [{float(r.a):.12f}, {float(r.b):.12f}]')
    report(f'tight delta={d}: bound holds (ratio < 1)', r.b < 1)
# closed form check: I_bits = 2 p0 (1 - h2((1+d)/2))
d = F(1, 10); p0 = F(1, 3)
I = cmi_nats(tight(p0, d))
x = ivq((1 + d) / 2); y = ivq((1 - d) / 2)
closed = 2 * ivq(p0) * (LN2 + x * iv.log(x) + y * iv.log(y))
report('tight family closed form 2p0(ln2 - h((1+d)/2)) matches', I.a <= closed.b and closed.a <= I.b)
# 1.01 x bound fails on the family at small delta: the constant 1/ln2 cannot be enlarged
d = F(1, 100); t = tight(F(1, 2), d)
report('constant is sharp: 1.0001 * p0 d^2 exceeds I at delta=1/100', decide(cmi_nats(t), F(10001, 10000) * F(1, 2) * d * d) == 'VIOLATION')

# --- C2: edge cases
# delta = 0
t = {(0, 'c', 0): F(1, 4), (0, 'c', 1): F(1, 4), (1, 'c', 0): F(1, 4), (1, 'c', 1): F(1, 4)}
h = hypothesis_pairs(t)[0]
report('delta=0: bound is 0 and I = 0 (tie at 0; strict ">0" of Main.md:168 fails)', h['delta'] == 0 and decide(cmi_nats(t), F(0)) == 'tie0' and cmi_nats(t).b == 0)
# delta = 1, p0 = 1/2 (its maximum): I = 1 bit, bound = 1/(2 ln 2)
t = tight(F(1, 2), F(1))
I = cmi_nats(t)
report('p0=1/2 (max), delta=1: I = 1 bit', bits(I).a <= 1 <= bits(I).b)
report('p0=1/2, delta=1: bound 1/(2ln2)=0.7213 bits < 1 = H(B|C) max for binary B', bits(ivq(F(1, 2))).b < 1)
# tiny P(c)
eps = F(1, 1000)
t = tight(eps / 2, F(1))
I = cmi_nats(t)
report('tiny P(c)=1e-3, disjoint laws: I = P(c) bits = 1e-3', overlap(bits(I), eps))
report('tiny P(c): stated bound (joint p0) holds', decide(I, eps / 2) == 'holds')
report('tiny P(c): CONDITIONAL-p0 variant (p0=1/2) is violated', decide(I, F(1, 2)) == 'VIOLATION')
# unequal weights: average-weight variant fails, min-weight (stated) holds
w1, w2 = F(1, 1000), F(999, 1000)
t = {(0, 'c', 0): w1, (1, 'c', 1): w2}
I = cmi_nats(t)
report('w=(1e-3, 0.999), disjoint: stated bound (min weight) holds', decide(I, min(w1, w2)) == 'holds')
report('w=(1e-3, 0.999), disjoint: average-weight variant violated', decide(I, (w1 + w2) / 2) == 'VIOLATION')
report('w=(1e-3, 0.999), disjoint: harmonic form 2w1w2/(w1+w2) holds', decide(I, 2 * w1 * w2 / (w1 + w2)) == 'holds')
# l1 convention: delta_1 = 2 TV -> p0 delta_1^2 = 4 p0 TV^2 fails on the tight family
t = tight(F(1, 2), F(1, 10))
report('l1-norm reading (delta = ||.||_1) of the bound is violated', decide(cmi_nats(t), F(1, 2) * (2 * F(1, 10)) ** 2) == 'VIOLATION')
# more than two pasts: extra past with arbitrary law at the same present
t = {(0, 'c', 0): F(1, 5), (1, 'c', 1): F(1, 5), (2, 'c', 0): F(3, 10), (2, 'c', 1): F(3, 10)}
I = cmi_nats(t)
report('three pasts at c: every pair satisfies the bound', all(decide(I, hh['p0'] * hh['delta'] ** 2) in ('holds', 'tie0') for hh in hypothesis_pairs(t)))

print('\nALL CONTROLS PASS' if ok else '\nSOME CONTROL FAILED')
sys.exit(0 if ok else 1)
