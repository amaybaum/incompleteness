#!/usr/bin/env python3
"""Main.md:496 last sentence: 'the equivalence is between rational laws and finite realizations
with rational priors'.  If 'prior' means mu_H (the object the theorem names), the reverse
direction fails: rational kernels + uniform tape + IRRATIONAL visible initial law give a finite
realization with rational mu_H whose law is irrational.  The construction itself needs only
rational CONDITIONAL kernels; P(x_0) is never routed through the tape."""
import sympy as sp
q = 1/sp.sqrt(2)
init = {0: q, 1: 1 - q}            # irrational visible initial law
# K = 1, kernel X1 = X0 (rational, D = 1): C_H = ledger x tape x clock = 3 * 1 * 2; mu_H = point mass (rational)
# phi on well-formed clock-0 states: (x, [PAD], 0, 0) -> (x, [x], 0, 1); realized joint:
joint = {(x, x): init[x] for x in (0, 1)}
print("mu_H = point mass (rational); realized P(x0=0,x1=0) =", joint[(0, 0)], "irrational:", not joint[(0, 0)].is_rational)
# and the converse obstruction that DOES hold: under any prior with rational masses, every
# conditional P(x_1..x_k | x_0) is a finite sum of those masses -> rational.  So the uniform-tape
# form cannot realize an irrational KERNEL, whatever D: the extension is needed exactly there.
