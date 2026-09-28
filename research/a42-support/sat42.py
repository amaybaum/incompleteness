"""SAT encoding (CNF) of: E in {-1,0,1}^{16x16} straight at SIG, with optional side constraints. Used as an
independent cross-check of the exhaustive searches and for the no-zero-line case. Vanishing of a level set is
encoded through the exact pair-structure lemma (pairtypes.py): antipodally balanced, or (gamma pairs only) equal to one
of the exceptional vanishing sets."""
import itertools
from pysat.formula import CNF, IDPool
from pysat.card import CardEnc, EncType
from pairtypes import pair_structure

class Enc:
    def __init__(self):
        self.pool = IDPool(); self.cnf = CNF()
        V = self.pool.id
        self.p = [[V(('p', i, j)) for j in range(16)] for i in range(16)]
        self.n = [[V(('n', i, j)) for j in range(16)] for i in range(16)]
        self.z = [[V(('z', i, j)) for j in range(16)] for i in range(16)]
        for i in range(16):
            for j in range(16):
                p, n, z = self.p[i][j], self.n[i][j], self.z[i][j]
                self.cnf.extend([[-p, -n], [z, p, n], [-z, -p], [-z, -n]])
    def AND(self, a, b):
        x = self.pool.id(('and', a, b))
        self.cnf.extend([[-x, a], [-x, b], [x, -a, -b]]); return x
    def OR(self, lits):
        x = self.pool.id(('or',) + tuple(lits))
        self.cnf.append([-x] + list(lits))
        for l in lits: self.cnf.append([x, -l])
        return x
    def card(self, lits, bound, kind):
        f = {'eq': CardEnc.equals, 'le': CardEnc.atmost, 'ge': CardEnc.atleast}[kind]
        enc = f(lits=lits, bound=bound, vpool=self.pool, encoding=EncType.seqcounter if kind != 'eq' else EncType.totalizer)
        self.cnf.extend(enc.clauses)
    def cond_card_eq(self, sel, lits, bound):
        """sel -> (sum lits == bound)"""
        f = CardEnc.equals(lits=lits, bound=bound, vpool=self.pool, encoding=EncType.totalizer)
        for cl in f.clauses: self.cnf.append([-sel] + cl)
    def straight(self):
        P, N, Z = self.p, self.n, self.z
        for i in range(16):
            for i2 in range(i + 1, 16):
                cps, exc = pair_structure(i, i2)
                for t in (2, 1, -1, -2):
                    L = []
                    for k in range(16):
                        a, b, c, d, e, f = P[i][k], N[i][k], Z[i][k], P[i2][k], N[i2][k], Z[i2][k]
                        if t == 2: L.append(self.AND(a, e))
                        elif t == -2: L.append(self.AND(b, d))
                        elif t == 1: L.append(self.OR([self.AND(a, f), self.AND(c, e)]))
                        else: L.append(self.OR([self.AND(b, f), self.AND(c, d)]))
                    lits_bal = lambda: [(L[k] if (A >> k) & 1 else -L[k]) for A, B in cps for k in range(16) if ((A | B) >> k) & 1]
                    if not exc:
                        for A, B in cps:
                            ks = [k for k in range(16) if (A >> k) & 1]; ls = [k for k in range(16) if (B >> k) & 1]
                            self.card([L[k] for k in ks] + [-L[k] for k in ls], len(ls), 'eq')
                    else:
                        bal = self.pool.id(('bal', i, i2, t))
                        for A, B in cps:
                            ks = [k for k in range(16) if (A >> k) & 1]; ls = [k for k in range(16) if (B >> k) & 1]
                            self.cond_card_eq(bal, [L[k] for k in ks] + [-L[k] for k in ls], len(ls))
                        sels = [bal]
                        for m in exc:
                            x = self.pool.id(('exc', i, i2, t, m)); sels.append(x)
                            for k in range(16): self.cnf.append([-x, L[k] if (m >> k) & 1 else -L[k]])
                        self.cnf.append(sels)
    def nz(self, i, j): return self.OR([self.p[i][j], self.n[i][j]])
    def mode0(self):
        for i in range(16):
            for lines in ([(i, j) for j in range(16)], [(j, i) for j in range(16)]):
                zs = [self.z[a][b] for a, b in lines]
                self.card(zs + [-self.p[a][b] for a, b in lines], 16, 'ge')
                self.card(zs + [-self.n[a][b] for a, b in lines], 16, 'ge')
    def support_le(self, B):
        self.card([self.nz(i, j) for i in range(16) for j in range(16)], B, 'le')
    def lines_ge(self, m):
        for i in range(16):
            self.card([self.nz(i, j) for j in range(16)], m, 'ge')
            self.card([self.nz(j, i) for j in range(16)], m, 'ge')
    def row_le(self, i, m):
        self.card([self.nz(i, j) for j in range(16)], m, 'le')
    def fix(self, E):
        for i in range(16):
            for j in range(16):
                self.cnf.append([self.p[i][j] if E[i][j] == 1 else (self.n[i][j] if E[i][j] == -1 else self.z[i][j])])
    def decode(self, model):
        S = set(x for x in model if x > 0)
        return [[1 if self.p[i][j] in S else (-1 if self.n[i][j] in S else 0) for j in range(16)] for i in range(16)]
