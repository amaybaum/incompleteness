"""POS-SEP candidate gate: the squeezed gate G = G_eps o (I (x) K_lam) on two copies of eball(2k+1).

Data (all at d = 2k+1, k >= 1, matching OddChar's nK k / zK k):
  odd(mu)   = mu > k                       (OddChar.oddK); homMap (nK k) = diag sign (-1)^odd
  z         = last coordinate, hom index d (OddChar.zK)
  C = {0, d}            classical control indices  (hom 0 and lift z)
  T = {1..d-1}          control tangent indices; T+ = {1..k}, T- = {k+1..2k}
  permT                 mu <-> mu + k  (exchanges T+ and T-)
  sigma (target)        0 <-> 1, d <-> k+1, identity elsewhere (parity preserving)
  K_lam                 diag(1, lam, ..., lam, 1) on HVec (fixes hom 0 and lift z, scales the tangent)

  G_eps(e_mu (x) e_nu) = e_{mu'} (x) e_nu          mu in C,  mu' = mu if nu even, d - mu if nu odd
                       = eps * e_{mu''} (x) e_{sigma nu}   mu in T,  mu'' = mu if nu even, permT mu if nu odd
  G = G_eps o (I (x) K_lam),  i.e.  G(omega) = G_eps(omega with column nu scaled by K_lam[nu]).
"""
from fractions import Fraction as Fr
from possep_core import zeros, ONE, ZERO


class Squeezed:
    def __init__(self, k, eps, lam):
        assert k >= 1
        self.k, self.d, self.n = k, 2 * k + 1, 2 * k + 2
        self.eps, self.lam = Fr(eps), Fr(lam)

    # -- data --
    def odd(self, mu):
        return mu > self.k

    def signs(self):
        return [-ONE if self.odd(m) else ONE for m in range(self.n)]

    def c_signs(self):  # diagSign coefficients on the d coordinates
        return [-ONE if self.odd(j + 1) else ONE for j in range(self.d)]

    def z(self):
        return [ONE if j == self.d - 1 else ZERO for j in range(self.d)]

    def Kdiag(self):
        return [ONE] + [self.lam] * (self.d - 1) + [ONE]

    def permT(self, mu):
        return mu + self.k if mu <= self.k else mu - self.k

    def sigma(self, nu):
        d, k = self.d, self.k
        return {0: 1, 1: 0, d: k + 1, k + 1: d}.get(nu, nu)

    # -- the gate --
    def g_eps(self, om):
        n, d = self.n, self.d
        out = zeros(n)
        for mu in range(n):
            for nu in range(n):
                c = om[mu][nu]
                if c == 0:
                    continue
                if mu in (0, d):
                    m2 = mu if not self.odd(nu) else d - mu
                    out[m2][nu] += c
                else:
                    m2 = mu if not self.odd(nu) else self.permT(mu)
                    out[m2][self.sigma(nu)] += self.eps * c
        return out

    def __call__(self, om):
        K = self.Kdiag()
        return self.g_eps([[om[m][v] * K[v] for v in range(self.n)] for m in range(self.n)])
