"""Task 3/6: M1 over the bounded grid, for the base card theory (Pi_B) and each perturbation; exact.
Grid: one shared two-colour deck of n = 2..6 cards, every composition (r red, n-r black; r in {0,n} is the
one-colour deck); system A with 1-2 hidden slots, purifier/partner B with 1-2 hidden slots."""
import sys, time, json, itertools
from fractions import Fraction as F
from cardtheory import *

OUT = []
def out(s=""):
    print(s, flush=True); OUT.append(s)

LOCAL_OPS = {"BASE": {"peek", "swap"}, "NDP": {"peek", "swap", "ndp"}, "VIS": {"peek", "swap", "read"},
             "MARK": {"peek", "swap", "mark"}, "CSWAP": {"peek", "swap", "cswap"}, "SPECT": {"peek", "swap"}, "VISNOSWAP": {"peek", "swap", "read"}}

def exchangeable_all(nodes, model):
    """formula/invariant check: each node's distribution is invariant under every transposition of two filled
    positions (slots and deck positions) -- i.e. a mixture of exchangeable deals E(M)."""
    bad = 0
    for n in nodes:
        st0 = next(iter(n)); slots, decks = st0
        flat_len = len(slots) + sum(len(d) for d in decks)
        filled = [i for i, x in enumerate(slots) if x is not None] + list(range(len(slots), flat_len))
        def flat(st):
            return list(st[0]) + [c for d in st[1] for c in d]
        def unflat(v, st):
            sl = tuple(v[:len(slots)]); rest = v[len(slots):]; dk = []; o = 0
            for d in st[1]: dk.append(tuple(rest[o:o + len(d)])); o += len(d)
            return (sl, tuple(dk))
        key = canon(n)
        for i, j in itertools.combinations(filled, 2):
            img = {}
            for st, p in n.items():
                v = flat(st); v[i], v[j] = v[j], v[i]; img[unflat(v, st)] = p
            if canon(img) != key:
                bad += 1; break
    return bad

def grid(variant, nmax=6, Aset=(1, 2), Bset=(1, 2), s_max=300000):
    flags = () if variant in ("BASE", "SPECT") else (variant,)
    rows = []
    for n in range(2, nmax + 1):
        for r in range(0, n + 1):
            for na in Aset:
                for nb in Bset:
                    if variant == "CSWAP" and nb < 2: continue
                    need = na + nb + (1 if variant == "SPECT" else 0)
                    if n < need: continue
                    A = [f"a{i+1}" for i in range(na)]; B = [f"b{i+1}" for i in range(nb)]
                    sysslots = {"a": A, "b": B}
                    if variant == "SPECT": sysslots["c"] = ["c1"]
                    m = Model([(r, n - r)], sysslots, flags)
                    t = time.time()
                    nodes, depth, bp, st = closure(m, s_max=s_max)
                    req = ("c1",) if variant == "SPECT" else ()
                    res, extreme, PAB, PA, margA = analyse(m, A, B, nodes, depth, bp, require_filled=req, verbose=False)
                    wr = lemma_w_rank(m, A + B, LOCAL_OPS[variant])
                    exch = exchangeable_all(nodes, m)
                    row = dict(variant=variant, deck=f"{r}R{n-r}B", A=na, B=nb, status=st["status"], depth=st["depth"],
                               nodes=len(nodes), W_rank_filled=f"{wr[0]}/{wr[1]}", nonexchangeable_nodes=exch,
                               **res, secs=round(time.time() - t, 2))
                    rows.append(row)
                    out(f"  {variant:5s} deck={row['deck']:5s} A={na} B={nb} {st['status']}@{st['depth']:2d} nodes={len(nodes):6d} "
                        f"W={row['W_rank_filled']:6s} nonexch={exch} |PAB|={res['n_PAB']:3d} ext={res['n_extreme']:3d} "
                        f"M1wit(ext)={res['n_M1_witness_extreme']:2d} M1wit(bud)={res['n_M1_witness_budget']:2d} "
                        f"P(a1=R)={','.join(res['witness_P(a1=R) values'])}")
    return rows

if __name__ == "__main__":
    variants = sys.argv[1:] or ["BASE", "NDP", "VIS", "MARK", "CSWAP", "SPECT"]
    allrows = []
    for v in variants:
        out(f"== variant {v} ==")
        rows = grid(v)
        allrows += rows
        nw = sum(1 for r in rows if r["n_M1_witness_extreme"] > 0)
        nontriv = sum(1 for r in rows if r["n_M1_witness_extreme"] > 0 and r["n_PAB"] > 1)
        has34 = sorted({r["deck"] + f"/A{r['A']}B{r['B']}" for r in rows if "3/4" in r["witness_P(a1=R) values"]})
        parked = sum(1 for r in rows if r["status"] != "FIXED POINT")
        out(f"  SUMMARY {v}: realizations={len(rows)} parked={parked} with M1 witness={nw} "
            f"(of which |Prep(AB)|>1: {nontriv}); witnesses giving P(a1=R)=3/4 in: {has34}")
    json.dump(allrows, open("run_m1." + "_".join(variants) + ".json", "w"), indent=1, default=str)
