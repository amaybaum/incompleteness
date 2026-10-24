"""Coordinator check of the one line of indep_degree_qm.out that indep_degree_qm.py does not print: the weight of
the degree-2 flag 1 + sum_{i<10} x_{2i} x_{2i+1} on 20 bits, by enumeration and by the closed form (4^10 + 2^10)/2."""
from itertools import product

w = sum(1 for x in product((0, 1), repeat=20) if (1 + sum(x[2 * i] * x[2 * i + 1] for i in range(10))) % 2)
closed = (4 ** 10 + 2 ** 10) // 2
print('weight of 1+sum_{i<10} x_{2i}x_{2i+1} on 20 bits:', w, w == closed == 2 ** 9 * 1025, w % 50)
