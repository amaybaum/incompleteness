"""Thread P: the test bodies (exact rational vertex lists of polytopes) shared by the probes."""
from fractions import Fraction as F

H = F(1, 2)

BODIES = {
    # name: (vertices, description)
    "seg": ([(F(-1),), (F(1),)], "segment = eball 1 = classical bit (2-vertex simplex)"),
    "tri": ([(F(1), F(0), F(0)), (F(0), F(1), F(0)), (F(0), F(0), F(1))],
            "classical trit, simplex 3 of KInfFoundations"),
    "tet": ([tuple(F(int(i == j)) for j in range(4)) for i in range(4)], "classical 4-simplex"),
    "square": ([(F(a), F(b)) for a in (1, -1) for b in (1, -1)], "square (gbit)"),
    # Spekkens toy bit: epistemic states = uniform on a pair of the 4 ontic states, i.e. the
    # midpoints of the six edges of the tetrahedron simplex 4: an octahedron.
    "spekkens_oct": ([tuple(H if k in (i, j) else F(0) for k in range(4))
                      for i in range(4) for j in range(i + 1, 4)],
                     "Spekkens toy bit: conv of edge midpoints of simplex 4 (octahedron), a classical HV model"),
    "pyramid": ([(F(a), F(b), F(0)) for a in (1, -1) for b in (1, -1)] + [(F(0), F(0), F(1))],
                "pyramid over square = free join square (+) point"),
}
