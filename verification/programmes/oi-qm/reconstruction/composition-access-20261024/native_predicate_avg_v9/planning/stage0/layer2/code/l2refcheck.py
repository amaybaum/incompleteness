"""NP-AVG-1 Stage 0 Layer 2: in-run reference gates (C7, C11 (i), C11 (ii), C17, C18).

Independent of the production code: imports only s0ref (C14). Every check takes plain
data (sets of site-times and the production closure's logs and tables, as data) and
recomputes what it needs with s0ref's explicit cone sets and tip enumeration.
"""
import s0ref as REF


class CachedGeo(REF.RefGeometry):
    """s0ref's geometry with each explicit cone set built once."""

    def __init__(self, dim, earlier):
        REF.RefGeometry.__init__(self, dim, earlier)
        self._cones = {}

    def cone(self, q):
        c = self._cones.get(q)
        if c is None:
            c = REF.RefGeometry.cone(self, q)
            self._cones[q] = c
        return c


def ref_tip_cells(q, geo):
    """{(e, 'near'|'far'): cell} from the plan text (as in s0ref.ref_direction_table)."""
    c = q[0]
    _, d, near, far = geo.kind(q)
    out = {}
    for i in range(geo.dim):
        for s in (1, -1):
            e = REF.unit(geo.dim, i, s)
            out[(e, 'near')] = (REF.shift(c, e, d), near)
            if d >= 1:
                out[(e, 'far')] = (REF.shift(c, e, d - 1), far)
    return out


def c7(fixed, quants, ret_prod, geo, elig, brute_limit):
    ref, how = REF.greatest(fixed, quants, geo, elig, brute_limit)
    return set(ref) == set(ret_prod), how


def c11i(fixed, quants, log, final_tables, geo, elig):
    """C11 (i): tables at every elimination and at the fixed point equal the reference's, and
    every decision agrees with its table. log: [(q, u, table)]. Returns (tables_checked,
    mismatches, inconsistencies)."""
    alive = set(quants) | set(fixed)
    checked, mism, incons = 0, 0, 0
    for q, u, tb in log:
        ref = REF.ref_direction_table(q, alive - {q}, geo, elig)
        checked += 1
        mism += tb != ref
        labs = [lab for lab, cell in ref_tip_cells(q, geo).items() if cell == u]
        if not any(tb.get(lab) == 'free' and ref.get(lab) == 'free' for lab in labs):
            incons += 1
        alive.discard(q)
    for q, tb in sorted(final_tables.items()):
        ref = REF.ref_direction_table(q, alive - {q}, geo, elig)
        checked += 1
        mism += tb != ref
        incons += ('free' in tb.values()) or ('free' in ref.values())
    return checked, mism, incons


def c17(ret, fixed, geo, elig):
    """C17: no retained quantity has a free eligible tip (reference cones and tips)."""
    pool = set(ret) | set(fixed)
    for q in sorted(ret):
        for u in geo.tipset(q):
            if elig(u) and not any(u in geo.cone(o) for o in pool if o != q):
                return False
    return True


def c18(log, fixed, quants, geo, elig):
    """C18: every logged elimination (q, u) is justified: u is a reference tip of q, eligible,
    and in the cone of no quantity alive at that moment."""
    alive = set(quants) | set(fixed)
    for q, u, _ in log:
        if q not in alive or u not in geo.tipset(q) or not elig(u) or \
                any(u in geo.cone(o) for o in alive if o != q):
            return False
        alive.discard(q)
    return True


def props(S, geo, elig, phi_cover):
    """C11 (ii): P_A-dir / P_G-dir and the aggregate P_A / P_G (s0ref, as stated in section 4)."""
    return (REF.pa_dir_violations(S, geo, elig, phi_cover),
            REF.pa_aligned_violations(S, geo, elig, phi_cover))


# Streaming forms for the S1a global bound (about 1,600 quantities): one explicit cone is
# held at a time.

def cover_index(cells, pool, geo):
    """{cell: sorted list of the quantities of pool whose reference cone contains it}."""
    cells = set(cells)
    out = {u: [] for u in cells}
    for o in sorted(pool):
        cone = REF.RefGeometry.cone(geo, o)
        for u in cells & cone:
            out[u].append(o)
    return out


def tipset(q, geo, near_only=False):
    """The reference tips of q: near and far (L3prime), or near only (L3)."""
    if not near_only:
        return geo.tipset(q)
    return {cell for lab, cell in ref_tip_cells(q, geo).items() if lab[1] == 'near'}


def c17_stream(ret, fixed, geo, elig, near_only=False):
    tips = {u for q in ret for u in tipset(q, geo, near_only) if elig(u)}
    idx = cover_index(tips, set(ret) | set(fixed), geo)
    bad = 0
    for q in sorted(ret):
        if any(elig(u) and not any(o != q for o in idx[u]) for u in tipset(q, geo, near_only)):
            bad += 1
    return bad


def c18_stream(log, fixed, quants, geo, elig, near_only=False):
    alive = set(quants) | set(fixed)
    logged = {u for _, u, _ in log}
    idx = cover_index(logged, alive, geo)
    bad = 0
    for q, u, _ in log:
        if q not in alive or u not in tipset(q, geo, near_only) or not elig(u) or \
                any(o != q and o in alive for o in idx[u]):
            bad += 1
        alive.discard(q)
    return bad
