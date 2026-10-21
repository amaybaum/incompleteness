"""C-i exhaustive record-safe search, vectorized (numpy integer bit operations only; exact).

Same word, observer-operation classes, class quotient, pruning and acceptance rules as
search3.py (which is the reference implementation; `--crosscheck` compares the two on every
configuration where both run).  Coordinates are relabelled internally so that bit order is
    hidden idle (Z)  >  designated hidden (u0, v0, P)  >  visible,
which makes one canonical reduced echelon form of L give the learnable space of (q, p, P):
the qpP-parts of the echelon rows whose leading bit is a designated hidden bit.

Usage: python3 search4.py NMIN NMAX MODES CLASSES [GLMAX] [--crosscheck]
"""
import sys, time
import numpy as np
from itertools import product, permutations
from f2 import lattice_update, gl_elements, perm_elements
from search2 import all_graphs, configs, Cfg

KMAX = 4


def vec_rref(A, nb):
    """Canonical fully reduced row echelon form, rows sorted by decreasing leading bit,
    zero rows last.  A: (m, r) int64.  Returns a new array."""
    A = A.copy()
    m, r = A.shape
    piv = np.zeros(m, dtype=np.int64)
    ar = np.arange(r)[None, :]
    idx = np.arange(m)
    for b in range(nb - 1, -1, -1):
        bit = np.int64(1) << b
        has_bit = (A & bit) != 0
        valid = has_bit & (ar >= piv[:, None])
        has = valid.any(axis=1)
        if not has.any():
            continue
        sel = np.argmax(valid, axis=1)
        ii = idx[has]
        s = sel[has]
        p = piv[has]
        rs = A[ii, s].copy()
        rp = A[ii, p].copy()
        A[ii, s] = rp
        A[ii, p] = rs
        prow = A[ii, p]
        hb = (A[ii] & bit) != 0
        hb[np.arange(len(ii)), p] = False
        A[ii] ^= np.where(hb, prow[:, None], 0)
        piv[has] += 1
    return A


class VCfg:
    def __init__(self, cfg):
        self.cfg = cfg
        N = cfg.N
        Z = [c for c in cfg.hid if c not in (0, cfg.n, cfg.Pc)]
        D = [0, cfg.n, cfg.Pc]
        V = list(cfg.vis)
        order_high_to_low = Z + D + V
        self.pos = {c: N - 1 - i for i, c in enumerate(order_high_to_low)}
        self.N = N
        self.Zbits = sum(1 << self.pos[c] for c in Z)
        self.Dbits = sum(1 << self.pos[c] for c in D)
        self.Pbit = 1 << self.pos[cfg.Pc]
        self.Vbits = sum(1 << self.pos[c] for c in V)
        self.M = [self.remap(cfg.M[o]) for o in range(N)]   # indexed by ORIGINAL output coord
        self.hid = cfg.hid
        self.vis = cfg.vis

    def remap(self, row):
        r = 0
        for c in range(self.N):
            if (row >> c) & 1:
                r |= 1 << self.pos[c]
        return r

    def unmap(self, row):
        r = 0
        for c in range(self.N):
            if (row >> self.pos[c]) & 1:
                r |= 1 << c
        return r


def op_bits(cls, d):
    if cls == "GL":
        els = gl_elements(d)
    elif cls == "cell":
        els = perm_elements(d)
    else:
        els = [tuple(1 << i for i in range(d))]
    G = np.zeros((len(els), d, d), dtype=np.int64)
    for m, g in enumerate(els):
        for i in range(d):
            for j in range(d):
                G[m, i, j] = (g[i] >> j) & 1
    return els, G


def vkey_np(cls, Xv, nb):
    if cls == "GL":
        return vec_rref(Xv, nb)
    if cls == "cell":
        return -np.sort(-Xv, axis=1)
    return Xv


def run(vc, cls, Gbits, kmax=KMAX, keep_paths=False):
    N, dv = vc.N, len(vc.vis)
    hid, vis = vc.hid, vc.vis
    dh = len(hid)
    # initial class: X = I
    H0 = np.array([[1 << vc.pos[c] for c in hid]], dtype=np.int64)
    V0 = np.array([[1 << vc.pos[c] for c in vis]], dtype=np.int64)
    L0 = vec_rref(np.concatenate([V0, np.zeros((1, N), dtype=np.int64)], axis=1), N)[:, :N]
    Vk0 = vkey_np(cls, V0, N)
    level = np.concatenate([H0, Vk0, L0], axis=1)      # rows: classes; cols: dh + dv + N
    parents = [] if keep_paths else None
    # M as selector: for each output coord o, which input coords (hidden positions / visible positions)
    Mh = np.zeros((N, dh), dtype=np.int64)
    Mv = np.zeros((N, dv), dtype=np.int64)
    for o in range(N):
        row = vc.cfg.M[o]
        for j, c in enumerate(hid):
            Mh[o, j] = (row >> c) & 1
        for j, c in enumerate(vis):
            Mv[o, j] = (row >> c) & 1
    hid_out = list(hid)
    vis_out = list(vis)
    m_ops = Gbits.shape[0]
    per_k = {}
    for k in range(1, kmax + 1):
        outs = []
        par = []
        for ci in range(level.shape[0]):
            H = level[ci, :dh]
            Vb = level[ci, dh:dh + dv]
            L = level[ci, dh + dv:]
            # Yv[m, i] = XOR_j G[m, i, j] * Vb[j]
            Yv = np.bitwise_xor.reduce(Gbits * Vb[None, None, :], axis=2)
            # X'_o = XOR_j Mh[o,j] H[j]  XOR  XOR_j Mv[o,j] Yv[:, j]
            hconst = np.array([np.bitwise_xor.reduce(Mh[o] * H) for o in range(N)], dtype=np.int64)
            Xn = np.bitwise_xor.reduce(Mv[None, :, :] * Yv[:, None, :], axis=2) ^ hconst[None, :]
            Xh = Xn[:, hid_out]
            Xv = Xn[:, vis_out]
            Ln = vec_rref(np.concatenate([np.broadcast_to(L, (m_ops, N)), Xv], axis=1), N)[:, :N]
            # prune: learnable (q,p,P) rows = echelon rows whose leading bit is a D bit
            lead_in_D = np.zeros(Ln.shape, dtype=bool)
            for b in range(N):
                bit = np.int64(1) << b
                if vc.Dbits & int(bit):
                    lead_in_D |= (Ln >= bit) & (Ln < (bit << 1))
            cnt = lead_in_D.sum(axis=1)
            hasP = (lead_in_D & ((Ln & np.int64(vc.Pbit)) != 0)).any(axis=1)
            keep = (cnt <= 1) & (~hasP)
            if not keep.any():
                continue
            Vk = vkey_np(cls, Xv[keep], N)
            rows = np.concatenate([Xh[keep], Vk, Ln[keep]], axis=1)
            if keep_paths:
                outs.append(rows)
                par.append(np.stack([np.full(keep.sum(), ci), np.nonzero(keep)[0]], axis=1))
            else:
                # incremental de-duplication (memory bound); identical resulting set of classes
                outs.append(np.unique(rows, axis=0))
                if sum(o.shape[0] for o in outs) > 400000:
                    outs = [np.unique(np.concatenate(outs, axis=0), axis=0)]
        if not outs:
            level = np.zeros((0, dh + dv + N), dtype=np.int64)
            per_k[k] = level
            for kk in range(k + 1, kmax + 1):
                per_k[kk] = level
            if keep_paths:
                parents.append(np.zeros((0, 2), dtype=np.int64))
            break
        allrows = np.concatenate(outs, axis=0)
        level, first = np.unique(allrows, axis=0, return_index=True)
        if keep_paths:
            parents.append(np.concatenate(par, axis=0)[first])
        per_k[k] = level
    return per_k, parents


def span_list(basis):
    s = [0]
    for b in basis:
        if b:
            s += [x ^ b for x in s]
    return s


def final_check(vc, cls, row):
    cfg = vc.cfg
    dh, dv, N = len(vc.hid), len(vc.vis), vc.N
    H = [vc.unmap(int(x)) for x in row[:dh]]
    Vb = [int(x) for x in row[dh:dh + dv]]
    L = [int(x) for x in row[dh + dv:]]
    Hd = dict(zip(vc.hid, H))
    if cls == "GL":
        Qc = [vc.unmap(f) for f in span_list(Vb) if f]
    elif cls == "cell":
        Qc = list({vc.unmap(f) for f in Vb})
    else:
        Qc = [vc.unmap(Vb[vc.vis.index(cfg.Qc)])]
    lam = []
    for f in L:
        if f == 0:
            continue
        lead = 1 << (f.bit_length() - 1)
        if lead & vc.Dbits:
            lam.append(vc.unmap(f & vc.Dbits))
    hard = cfg.qpP
    out = []
    for lab, t, wu in cfg.tgts():
        if not (len(lam) == 1 and lam[0] == wu):
            continue
        dev = 0
        ok = True
        for c in (0, cfg.n, cfg.Pc):
            d = Hd[c] ^ t[c]
            if d & hard:
                ok = False
                break
            dev |= d
        if not ok:
            continue
        best = None
        for f in Qc:
            d = f ^ t[cfg.Qc]
            if d & hard:
                continue
            a = dev | d
            cl = "E" if a == 0 else ("AH" if a & cfg.Zmask else "AV")
            if best is None or "E AV AH".split().index(cl) < "E AV AH".split().index(best):
                best = cl
        if best:
            out.append((lab, best))
    return out


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    cross = "--crosscheck" in sys.argv
    nmin, nmax = int(args[0]), int(args[1])
    modes = args[2].split(",")
    classes = args[3].split(",")
    GLMAX = int(args[4]) if len(args) > 4 else 4
    CELLMAX = int(__import__("os").environ.get("CELLMAX", "6"))
    opcache = {}
    t0 = time.time()
    if cross:
        import search3
    for mode in modes:
        for n in range(nmin, nmax + 1):
            for cls in classes:
                ncfg = skipped = 0
                tally, examples = {}, {}
                maxlev = 0
                mismatches = 0
                for edges in all_graphs(n):
                    for (lab, vis, Qc, Pc) in configs(n, mode):
                        cfg = Cfg(n, edges, vis, Qc, Pc, lab)
                        if (cls == "GL" and cfg.dv > GLMAX) or (cls == "cell" and cfg.dv > CELLMAX):
                            skipped += 1
                            continue
                        ncfg += 1
                        if (cls, cfg.dv) not in opcache:
                            opcache[(cls, cfg.dv)] = op_bits(cls, cfg.dv)
                        vc = VCfg(cfg)
                        per_k, _ = run(vc, cls, opcache[(cls, cfg.dv)][1])
                        for k in range(1, KMAX + 1):
                            lev = per_k[k]
                            maxlev = max(maxlev, lev.shape[0])
                            cats = {}
                            for row in lev:
                                for (tl, d) in final_check(vc, cls, row):
                                    cats.setdefault(d, tl)
                            for d, tl in cats.items():
                                tally[(k, d)] = tally.get((k, d), 0) + 1
                                ex = examples.setdefault((k, d), [])
                                if len(ex) < 3:
                                    ex.append((edges, lab, tl))
                        if cross:
                            pk3, _ = search3.run_cfg(cfg, cls)
                            for k in range(1, KMAX + 1):
                                a = per_k[k].shape[0]
                                b = pk3[k][0]
                                c3 = sorted(set((tl, d) for (tl, d, key) in pk3[k][1]))
                                c4 = sorted(set(x for row in per_k[k] for x in final_check(vc, cls, row)))
                                if a != b or c3 != c4:
                                    mismatches += 1
                print(f"[{mode}] n={n} ops={cls}: configurations={ncfg} skipped(visible dim)={skipped} "
                      f"max record-safe classes/level={maxlev}" + (f" crosscheck mismatches={mismatches}" if cross else ""))
                for k in range(1, KMAX + 1):
                    cs = [f"{d}:{tally[(k, d)]}" for d in ("E", "AV", "AH") if (k, d) in tally]
                    print(f"    k={k}: record-safe designated matches: {', '.join(cs) if cs else 'none'}")
                for (k, d), ex in sorted(examples.items()):
                    for e in ex[:3]:
                        print(f"      example k={k} {d}: edges={e[0]} {e[1]} target {e[2]}")
                sys.stdout.flush()
    print(f"elapsed {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
