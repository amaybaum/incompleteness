"""MIXED-PATH-1 Stage 2: the two steppers (full-field, class-restricted) and their neighbour sums.

Each stepper is one function that takes the F table as a parameter (STAGE2-PREREG.md section 5).
Integers only.
"""
import numpy as np


def thin_sites(L):
    return [(x, y, z) for x in range(L) for y in range(2) for z in range(2)]


def class_geometry(L):
    """Sublattices of the thin torus Z/L x Z/2 x Z/2 and, for each target parity, the rows of the
    source sublattice read by the neighbour sum (x+1, x-1, y-flip, z-flip)."""
    subs = {par: [s for s in thin_sites(L) if (s[0] + s[1] + s[2]) % 2 == par] for par in (0, 1)}
    pos = {par: {s: i for i, s in enumerate(subs[par])} for par in (0, 1)}
    nbr = {}
    for tgt in (0, 1):
        src = pos[1 - tgt]
        nxp = [src[((x + 1) % L, y, z)] for (x, y, z) in subs[tgt]]
        nxm = [src[((x - 1) % L, y, z)] for (x, y, z) in subs[tgt]]
        nyf = [src[(x, 1 - y, z)] for (x, y, z) in subs[tgt]]
        nzf = [src[(x, y, 1 - z)] for (x, y, z) in subs[tgt]]
        nbr[tgt] = tuple(np.array(v, dtype=np.intp) for v in (nxp, nxm, nyf, nzf))
    return subs, pos, nbr


def full_sigma(u):
    """Neighbour sum on the thin torus, last three axes (L,2,2):
    u(x+1)+u(x-1)+2u(x,y+1,z)+2u(x,y,z+1)."""
    return (np.roll(u, -1, axis=-3) + np.roll(u, 1, axis=-3)
            + 2 * u[..., ::-1, :] + 2 * u[..., :, ::-1])


def full_step(u, v, table, q):
    """(u, v) -> (F(u) - v mod q, u) on the full two-slice field; table[s] = F mod q at sum s."""
    sig = full_sigma(u)
    new = (np.take(np.asarray(table, dtype=np.int64), sig) - v) % q
    return new, u


def class_sigma(cur, nb):
    """Neighbour sum of the class-restricted stepper: cur holds the source sublattice rows."""
    return cur[nb[0]] + cur[nb[1]] + 2 * (cur[nb[2]] + cur[nb[3]])


def class_step(cur, prv, table, q, nb):
    """One step of one space-time parity class: cur (source sublattice, current slice),
    prv (target sublattice, retarded slice) -> (F(cur) - prv mod q on the target sublattice, cur)."""
    lut = np.array([(int(table[s]) - w) % q for s in range(len(table)) for w in range(q)],
                   dtype=np.uint8)
    idx = class_sigma(cur, nb)
    idx *= q
    idx += prv
    new = np.take(lut, idx)
    return new, cur
