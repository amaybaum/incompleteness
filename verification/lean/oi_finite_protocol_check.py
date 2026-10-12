#!/usr/bin/env python3
"""Exact controls for round OI-FINITE-PROTOCOL-1. Exact physical reset, attempt and stopped-loop maps.

Arithmetic is in Q(i). The actual circuit and uniformly attached ancilla are evaluated
before branch maps and stopped-loop maps are compared with their stated formulas.
"""
from fractions import Fraction as R
from dataclasses import dataclass
from itertools import product
import sys


@dataclass(frozen=True)
class C:
    r: R = R(0)
    i: R = R(0)

    @classmethod
    def cast(cls, x):
        return x if isinstance(x, cls) else cls(R(x))

    def __add__(self, other):
        b = C.cast(other)
        return C(self.r + b.r, self.i + b.i)

    __radd__ = __add__

    def __neg__(self):
        return C(-self.r, -self.i)

    def __sub__(self, other):
        return self + -C.cast(other)

    def __rsub__(self, other):
        return C.cast(other) + -self

    def __mul__(self, other):
        b = C.cast(other)
        return C(self.r*b.r-self.i*b.i, self.r*b.i+self.i*b.r)

    __rmul__ = __mul__

    def conj(self):
        return C(self.r, -self.i)


I = C(R(0), R(1))


def tab(n, f):
    return tuple(tuple(C.cast(f(a,b)) for b in range(n)) for a in range(n))


def ident(n):
    return tab(n, lambda a,b: int(a == b))


def unit(n, a, b):
    return tab(n, lambda x,y: int((x,y) == (a,b)))


def scale(c, a):
    return tuple(tuple(c*x for x in row) for row in a)


def plus(a, b):
    return tuple(tuple(x+y for x,y in zip(ra,rb)) for ra,rb in zip(a,b))


def mm(a,b):
    return tuple(tuple(sum((a[x][k]*b[k][y] for k in range(len(b))), C())
                       for y in range(len(b[0]))) for x in range(len(a)))


def dagger(a):
    return tuple(tuple(a[y][x].conj() for y in range(len(a))) for x in range(len(a[0])))


def apply(u,x):
    return mm(mm(u,x),dagger(u))


def tensor(a,b):
    return tuple(tuple(a[s][t]*b[f][e] for t in range(len(a)) for e in range(len(b)))
                 for s in range(len(a)) for f in range(len(b)))


def total(xs,n):
    out = scale(0,ident(n))
    for x in xs:
        out = plus(out,x)
    return out


def trace_anc(x):
    return tab(2,lambda s,t: sum((x[4*s+f][4*t+f] for f in range(4)),C()))


P = [tab(8,lambda x,y: int(x == y and x%4 == j)) for j in range(4)]
reset = [tab(8,lambda x,y: int(x == 4*(y//4)+(0 if y%4 == j else j if y%4 == 0 else y%4)))
         for j in range(4)]
Z = tab(2,lambda s,t: (1 if s == 0 else -1) if s == t else 0)
correct = [ident(8) if j == 0 else tensor(Z,ident(4)) for j in range(4)]
D = tab(2,lambda s,t: (1 if s == 0 else C(R(3,5),R(4,5))) if s == t else 0)

# Construct U from the permitted finite circuit, not from its desired channel formula.
hraw = tab(2,lambda s,t: -1 if s == t == 1 else 1)
hh = scale(R(1,2),tensor(ident(2),tensor(hraw,hraw)))
tof = tab(8,lambda x,y: int(x == (y ^ 4 if y%4 == 3 else y)))
phase = tab(8,lambda x,y: (1 if x//4 == 0 else I) if x == y else 0)
U = mm(mm(mm(mm(hh,tof),phase),tof),hh)
v = (1,-1,-1,1)
Utable = tab(8,lambda x,y: 0 if x//4 != y//4 else
    ((1 if x//4 == 0 else I) if x%4 == y%4 else 0) +
    R(1,4)*(I-1 if x//4 == 0 else 1-I)*v[x%4]*v[y%4])


def reset_state(x):
    attached = tensor(x,scale(R(1,4),ident(4)))
    return total((apply(reset[j],apply(P[j],attached)) for j in range(4)),8)


def branches(x, do_reset=True, do_correct=True):
    seed = reset_state(x) if do_reset else tensor(x,scale(R(1,4),ident(4)))
    ran = apply(U,seed)
    return tuple(trace_anc(apply(correct[j] if do_correct else ident(8),apply(P[j],ran)))
                 for j in range(4))


def stopped(k,x):
    if k == 0:
        return x
    bs = branches(x)
    return plus(bs[0],stopped(k-1,total(bs[1:],2)))


def formula(k,x):
    q = R(3,8)**k
    return plus(scale(1-q,apply(D,x)),scale(q,x))


checks = []


def check(name, passed):
    checks.append(bool(passed))
    print(name + (': PASS' if passed else ': FAIL'))


units = tuple(unit(2,a,b) for a,b in product(range(2),repeat=2))
check('CIRCUIT-TABLE',U == Utable)
check('UNITARY',mm(dagger(U),U) == ident(8) and mm(U,dagger(U)) == ident(8))
check('RESET-ISOMETRIES',all(mm(dagger(r),r) == ident(8) for r in reset))
check('PROJECTOR-RESOLUTION',total(P,8) == ident(8))
check('ACTUAL-UNIFORM-RESET',all(reset_state(x) == tensor(x,unit(4,0,0)) for x in units))
check('ACTUAL-CORRECTED-BRANCHES',all(
    branches(x)[0] == scale(R(5,8),apply(D,x)) and
    all(b == scale(R(1,8),x) for b in branches(x)[1:]) for x in units))
check('STOPPED-DEPTHS-0-8',all(stopped(k,x) == formula(k,x) for k in range(9) for x in units))
e01 = unit(2,0,1)
check('CONTROL-REMOVE-RESET',total(branches(e01,do_reset=False),2) != formula(1,e01))
check('CONTROL-REMOVE-CORRECTION',total(branches(e01,do_correct=False),2) != formula(1,e01))
check('CONTROL-CONTINUE-SUCCESS',total(branches(total(branches(e01),2)),2) != formula(2,e01))
if not all(checks):
    print('NO VERDICT: a required control failed')
    sys.exit(1)
print('FINITE-PROTOCOL: PASS; 10 groups; 36 stopped matrix-unit cases')
