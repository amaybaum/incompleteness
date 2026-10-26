"""NP-AVG-1 Stage 0 Layer 2: per-record analysis around the frozen engine (production).

Imports only s0geom and itertools (C14). No closure is computed here except through
s0geom.Context.run. Functions:
- the C4v group of a setup, its action, canonical representatives, orbits and stabilizers;
- post_closure(ctx, ret): the attributes of s0geom.analyse computed from a given retained
  set (used to carry a representative's closure to its orbit members; checked against
  analyse by l2selftest on every toy record and by the in-run C8 gate on sampled orbits);
- the degeneracies of section 3, shared near tips, shared aligned tips, the cover graph and
  the residual support (Layer-2 definitions, stated in LAYER2-PLAN.md section 4);
- member_contributions: the closed list of 54 reported counts (plan section 6, C8),
  contributed by one record.
"""
from itertools import permutations, product

import s0geom as G


def oh(dim):
    return [(pp, ss) for pp in permutations(range(dim)) for ss in product((1, -1), repeat=dim)]


def act(g, c):
    perm, sg = g
    return tuple(sg[i]*c[perm[i]] for i in range(len(c)))


def group(setup):
    """The stabilizer in O_h of the region, the port and the sites of q8 and q10 (plan section
    1, E4), in O_h's enumeration order. Identity first."""
    dim = setup.dim
    region = set(setup.region)
    o = setup.origin
    q8 = G.vadd(o, tuple(-1 if j == dim - 1 else 0 for j in range(dim)))
    q10 = G.vadd(o, tuple(1 if j == dim - 1 else 0 for j in range(dim)))
    out = []
    for g in oh(dim):
        if {act(g, c) for c in region} != region:
            continue
        if setup.port is not None and act(g, tuple(setup.port)) != tuple(setup.port):
            continue
        if act(g, q8) != q8 or act(g, q10) != q10:
            continue
        out.append(g)
    return out


def act_rec(g, r):
    return tuple(sorted((act(g, x), t) for x, t in r))


def act_set(g, qs):
    return sorted((act(g, c), t) for c, t in qs)


def canon(r, grp):
    return min(act_rec(g, r) for g in grp)


def orbit(r, grp):
    """{member: first group element (in grp order) carrying r to it}."""
    out = {}
    for g in grp:
        m = act_rec(g, r)
        if m not in out:
            out[m] = g
    return out


def stabilizer_order(r, grp):
    rs = tuple(sorted(r))
    return sum(1 for g in grp if act_rec(g, rs) == rs)


def post_closure(ctx, ret):
    """s0geom.analyse's attributes from the retained set ret instead of ctx.run()."""
    s = ctx.setup
    dim, pair, rule = s.dim, ctx.pair, ctx.rule
    ret = set(ret)
    if ctx.conv == 'A':
        S = set(ret)
    else:
        S = {q for q in ret if any(ctx.eligible(u) for u in G.tips(q, pair, dim, rule))}
    six, V, p = s.phi()
    j_cells = {six[i] for i in range(len(six)) if six[i][0] in ((0,)*(dim - 1) + (-1,), (0,)*(dim - 1) + (1,))}
    out = {'survivor': bool(S), 'n_retained': len(ret), 'n_survivor': len(S),
           'retained': sorted(ret), 'survivors': sorted(S), 'in_clear': sorted(ctx.in_clear)}
    if ctx.conv == 'A':
        out['phi_linked'] = any(G.in_cone(c, q, pair, G.FROZEN) for q in S for c in ctx.phi_cells)
        out['j_linked'] = any(G.in_cone(c, q, pair, G.FROZEN) for q in S for c in j_cells)
    else:
        src = [(x, 0) for x in s.sources]
        out['g_linked'] = any(G.in_cone(c, q, pair, G.FROZEN) for q in S for c in src)
        out['truncated'] = sorted(q for q in ret - S if q in ctx.rec)
    public = sorted((ret & (ctx.rec | ctx.port)) | ctx.in_clear | {V, p})
    out['public_retained'] = public
    priv = set(six) - set(ctx.in_clear)
    if ctx.conv == 'A':
        dep = {c for c in priv for q in public if q not in ctx.fixed and G.in_cone(c, q, pair, G.FROZEN)}
        out['private_phi'] = sorted(dep | (set(ctx.in_clear) & set(six)))
        out['private_J'] = sorted(c for c in out['private_phi'] if c in j_cells)
    else:
        src = [(x, 0) for x in s.sources]
        out['source_cells'] = sorted({c for c in src for q in public if q not in ctx.fixed
                                      and G.in_cone(c, q, pair, G.FROZEN)})
    return out


DEGENERACIES = ('item_at_q9', 'item_at_phi_site', 'item_at_port_site', 'item_on_z_axis', 'pair_on_common_axis',
                'item_t_le_0', 'item_t_eq_minus1', 'last_sample_odd')


def degeneracies(setup, r):
    """The eight cross-tabulated degeneracies of section 3 (as in code-r5 s0controls)."""
    six, V, p = setup.phi()
    phi_sites = {c for c, _ in six}
    sites = [x for x, _ in r]
    dim = setup.dim
    o = setup.origin

    def zaxis(x):
        return all(x[i] == 0 for i in range(dim - 1))

    def common_axis(a, b):
        return sum(1 for i in range(dim) if a[i] != b[i]) == 1
    port = None if setup.port is None else tuple(setup.port)
    return {
        'item_at_q9': any(x == o for x in sites),
        'item_at_phi_site': any(x in phi_sites for x in sites),
        'item_at_port_site': any(x == port for x in sites),
        'item_on_z_axis': any(zaxis(x) for x in sites),
        'pair_on_common_axis': len(r) == 2 and common_axis(sites[0], sites[1]),
        'item_t_le_0': any(t <= 0 for _, t in r),
        'item_t_eq_minus1': any(t == -1 for _, t in r),
        'last_sample_odd': any(not G.even((x, t)) for x, t in r),
    }


def count_keys():
    keys = []
    for conv in ('A', 'G'):
        keys += [conv + ':survivors', conv + ':L3_vs_L3prime_disagree', conv + ':observer_classes',
                 conv + ':observer_classes_survivors', conv + ':observer_classes_collapsed']
        if conv == 'A':
            keys += ['A:phi_linked', 'A:j_linked', 'A:survivors_J_linked', 'A:survivors_phi_linked_not_J',
                     'A:survivors_unlinked', 'A:b_has_J_cell', 'A:b_has_nonJ_phi_cell']
        else:
            keys += ['G:b_has_source_cell', 'G:survivors_G_linked', 'G:survivors_G_unlinked']
        for k in DEGENERACIES:
            for sv in (False, True):
                keys.append('%s:deg:%s:survivor=%s' % (conv, k, sv))
    keys += ['masking_equivalent_records', 'nontrivial_stabilizer']
    return keys


# Counts that are sums of per-record contributions. The observer-class counts are
# cardinalities of sets of public sets, and masking_equivalent_records is a property of
# the record space; both are formed by the merge.
CLASS_KEYS = ('observer_classes', 'observer_classes_survivors', 'observer_classes_collapsed')


def member_contributions(setup, r, aA, aG, a3A, a3G):
    """Per-record contributions to the additive reported counts, from the analysis
    dictionaries of record r (L3prime: aA, aG; L3: a3A, a3G). Mirrors code-r5
    s0controls._reported_counts term by term."""
    out = {}
    deg = degeneracies(setup, r)
    for conv, a, a3 in (('A', aA, a3A), ('G', aG, a3G)):
        out[conv + ':survivors'] = int(a['survivor'])
        out[conv + ':L3_vs_L3prime_disagree'] = int(a['retained'] != a3['retained'])
        if conv == 'A':
            out['A:phi_linked'] = int(a['phi_linked'])
            out['A:j_linked'] = int(a['j_linked'])
            out['A:survivors_J_linked'] = int(a['survivor'] and a['j_linked'])
            out['A:survivors_phi_linked_not_J'] = int(a['survivor'] and a['phi_linked'] and not a['j_linked'])
            out['A:survivors_unlinked'] = int(a['survivor'] and not a['phi_linked'])
            out['A:b_has_J_cell'] = int(bool(a['private_J']))
            out['A:b_has_nonJ_phi_cell'] = int(len(a['private_phi']) > len(a['private_J']))
        else:
            out['G:b_has_source_cell'] = int(bool(a['source_cells']))
            out['G:survivors_G_linked'] = int(a['survivor'] and a['g_linked'])
            out['G:survivors_G_unlinked'] = int(a['survivor'] and not a['g_linked'])
        for k in DEGENERACIES:
            for sv in (False, True):
                out['%s:deg:%s:survivor=%s' % (conv, k, sv)] = int(deg[k] and a['survivor'] == sv)
    return out


def shared_near_tip(quants, pair, dim):
    """True iff some cell is the e-near-tip of two distinct quantities of quants, for the same
    axis direction e (the Layer-2 reading of C7's 'record containing a shared tip')."""
    seen = {}
    for q in sorted(quants):
        for lab, u in G.tip_labels(q, pair, dim, G.FROZEN):
            if lab[1] != 'near':
                continue
            key = (lab[0], u)
            if key in seen and seen[key] != q:
                return True
            seen[key] = q
    return False


def shared_aligned_tips(S, pair, dim):
    """[(e, tip, reach, n)] for every near tip shared, in direction e, by n >= 2 elements of S
    of the same type (section 3, structure)."""
    by = {}
    for q in sorted(S):
        d, ty = pair.depth(q)
        for lab, u in G.tip_labels(q, pair, dim, G.FROZEN):
            if lab[1] == 'near':
                e = lab[0]
                reach = sum(a*b for a, b in zip(q[0], e)) + d
                by.setdefault((e, u, ty), []).append((q, reach))
    out = []
    for (e, u, ty), lst in sorted(by.items()):
        if len(lst) >= 2:
            out.append([list(e), [list(u[0]), u[1]], ty, lst[0][1], len(lst)])
    return out


def cover_components(S, pair, dim, eligible=None):
    """Connected components of the cover graph on S: q and o are joined when an eligible tip
    of one lies in the cone of the other."""
    S = sorted(S)
    parent = {q: q for q in S}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for q in S:
        for u in G.tips(q, pair, dim, G.FROZEN):
            if eligible is not None and not eligible(u):
                continue
            for o in S:
                if o != q and G.in_cone(u, o, pair, G.FROZEN):
                    parent[find(q)] = find(o)
    comps = {}
    for q in S:
        comps.setdefault(find(q), []).append(q)
    return sorted(len(v) for v in comps.values())


def cone_cells(q, pair, dim):
    """The pair-slice cells of q's cone, by enumeration of the l1 ball and in_cone."""
    d, ty = pair.depth(q)
    out = set()
    for s in (pair.E, pair.L):
        for v in G.lball(d, dim):
            u = (G.vadd(q[0], v), s)
            if G.in_cone(u, q, pair, G.FROZEN):
                out.add(u)
    return out


def residual_support_bits(ctx, S):
    """Layer-2 definition (LAYER2-PLAN.md section 4, flagged as a Layer-1 underspecification):
    under A, 3 bits per pair cell in the union of Phi's seven cells and the cones of S_A;
    under G, 3 bits per seed (eligible pair cell) in the union of the cones of S_G."""
    dim, pair = ctx.setup.dim, ctx.pair
    cells = set()
    for q in S:
        cells |= cone_cells(q, pair, dim)
    if ctx.conv == 'A':
        cells |= set(ctx.phi_cells)
    else:
        cells = {u for u in cells if ctx.eligible(u)}
    return 3*len(cells)


def qkey(qs):
    """Compact exact encoding of a set of site-times: a flat sorted list of integers."""
    out = []
    for c, t in sorted(qs):
        out.extend(c)
        out.append(t)
    return out


def canon_set(qs, grp):
    """(canonical image of the set qs under grp, size of its orbit)."""
    imgs = {tuple(act_set(g, qs)) for g in grp}
    return min(imgs), len(imgs)
