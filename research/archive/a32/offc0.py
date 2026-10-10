"""Exploration only: for each circle r != 0, a coordinate constant on C0 (m = 0) at which the
test class r F(i) takes a different value -> r F(i) is on no Fourier-circle class."""
from circles import COORDS, R, coord_data
d0 = coord_data(*R[0])
for r in range(1, 9):
    dr = coord_data(*R[r])
    hits = [p for p in COORDS if d0[p][1] == 0 and (dr[p][0] * (1j ** (dr[p][1] % 4))) != d0[p][0]]
    core = [p for p in hits if p[0] == (0, 0, 0)]
    print(r, R[r], "witness coords:", len(hits), "e.g.", (core or hits)[:2])
