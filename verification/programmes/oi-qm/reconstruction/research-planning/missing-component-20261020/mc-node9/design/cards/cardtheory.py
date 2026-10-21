"""Option B exploratory design probe: an operational theory generated from card rules (book Sec. 1.11, card-table
engine at 17115cc), decided exactly (Fractions). Design evidence only; renders no M0-M5 verdict.

Ontic state: (slots, decks). slots: tuple over named positions, value None (empty) or a colour 0..k-1.
decks: tuple of decks, each a tuple of colours, top first. Initial condition: every deck uniform over all
orderings of its distinct physical cards (counting measure) = uniform over distinct colour sequences.

Generators (each applied only when its applicability pattern -- which slots are empty, deck lengths -- holds,
which is common to the whole support because no generator acts on content):
  deal(s,d)       top card of deck d into empty slot s                     [content-independent]
  move(s,t)       card from slot s to empty slot t, same system            [content-independent]
  swap(s,t)       exchange two filled slots of the same system             [content-independent]
  cycle(d)        top card of deck d to the bottom (a deterministic shuffle)[content-independent]
  peek(s)         reveal colour of slot s (outcome); the card leaves play  [book rule 3, destructive]
  peekdeck(d)     reveal the top card of deck d; it leaves play            [destructive]
  discard(s)      slot s emptied, colour not revealed (marginalisation)
  discarddeck(d)  deck d emptied unrevealed
Perturbations (flags):
  NDP             reveal colour of slot s without removing it (non-destructive peek; = peek + reinsert)
  VIS             each system has one visible slot read freely (outcome, no change), swaps visible<->hidden
                  (the book's hole card / engine's (v,h) swap core); K-CLASSICAL
  MARK            line-game marker: reads the sum of +1/-1 values of a system's filled hidden slots, no change
  CSWAP           content-controlled joint bijection: if colour(a1)==0 then swap(b1,b2)
Heralding (g6): every outcome of nonzero probability yields its normalised post-operation conditional state.
"""
import sys, itertools, hashlib, json
from fractions import Fraction as F
from collections import defaultdict
from exactlp import feasible

# ---------------------------------------------------------------- model
class Model:
    def __init__(self, decks, sysslots, flags=(), k=2, name=""):
        """decks: list of colour-count tuples; sysslots: dict system -> list of slot names (hidden first);
        visible slots are named with suffix 'v' when VIS in flags."""
        self.k = k; self.flags = set(flags); self.name = name
        self.deck_counts = [tuple(c) for c in decks]
        self.systems = {}
        for sname, hs in sysslots.items():
            vs = [sname + "v"] if ("VIS" in self.flags or "VISNOSWAP" in self.flags) else []
            self.systems[sname] = {"hidden": list(hs), "visible": vs}
        self.slots = []
        for sname, d in self.systems.items():
            self.slots += d["hidden"] + d["visible"]
        self.idx = {s: i for i, s in enumerate(self.slots)}
        self.sys_of = {s: n for n, d in self.systems.items() for s in d["hidden"] + d["visible"]}
        self.ops = self._ops()

    def initial(self):
        decks = []
        for cnt in self.deck_counts:
            seq = [c for c, n in enumerate(cnt) for _ in range(n)]
            decks.append(sorted(set(itertools.permutations(seq))))
        dist = {}
        combos = list(itertools.product(*decks))
        w = F(1, len(combos))
        empty = tuple([None] * len(self.slots))
        for dk in combos:
            dist[(empty, tuple(dk))] = w
        return dist

    def _ops(self):
        ops = []
        nd = len(self.deck_counts)
        for s in self.slots:
            if s.endswith("v") and "VIS" in self.flags:
                pass
            for d in range(nd):
                ops.append(("deal", s, d))
        for sname, d in self.systems.items():
            allsl = d["hidden"] + d["visible"]
            for s, t in itertools.permutations(allsl, 2):
                if "VISNOSWAP" in self.flags and (s in d["visible"]) != (t in d["visible"]): continue
                ops.append(("move", s, t))
            for s, t in itertools.combinations(allsl, 2):
                if "VISNOSWAP" in self.flags and (s in d["visible"]) != (t in d["visible"]): continue
                ops.append(("swap", s, t))
            if "MARK" in self.flags:
                ops.append(("mark", sname))
        for d in range(nd):
            ops.append(("cycle", d)); ops.append(("peekdeck", d)); ops.append(("discarddeck", d))
        for s in self.slots:
            ops.append(("peek", s)); ops.append(("discard", s))
            if "NDP" in self.flags:
                ops.append(("ndp", s))
            if ("VIS" in self.flags or "VISNOSWAP" in self.flags) and s.endswith("v"):
                ops.append(("read", s))
        if "CSWAP" in self.flags:
            ops.append(("cswap", "a1", "b1", "b2"))
        return ops

    # pattern = emptiness of slots and deck lengths (deterministic over a node's support)
    @staticmethod
    def pattern(state):
        slots, decks = state
        return (tuple(x is None for x in slots), tuple(len(d) for d in decks))

    def applicable(self, op, pat):
        empt, dl = pat; I = self.idx
        t = op[0]
        if t == "deal": return empt[I[op[1]]] and dl[op[2]] > 0
        if t == "move": return (not empt[I[op[1]]]) and empt[I[op[2]]]
        if t == "swap": return (not empt[I[op[1]]]) and (not empt[I[op[2]]])
        if t in ("cycle",): return dl[op[1]] > 1
        if t in ("peekdeck", "discarddeck"): return dl[op[1]] > 0
        if t in ("peek", "discard", "ndp", "read"): return not empt[I[op[1]]]
        if t == "mark":
            hs = self.systems[op[1]]["hidden"]; return all(not empt[I[s]] for s in hs)
        if t == "cswap": return all(not empt[I[s]] for s in op[1:])
        raise ValueError(op)

    def apply(self, op, state):
        """returns (outcome, newstate) -- deterministic"""
        slots, decks = state; sl = list(slots); dk = list(decks); I = self.idx; t = op[0]
        if t == "deal":
            d = dk[op[2]]; sl[I[op[1]]] = d[0]; dk[op[2]] = d[1:]; return None, (tuple(sl), tuple(dk))
        if t == "move":
            sl[I[op[2]]] = sl[I[op[1]]]; sl[I[op[1]]] = None; return None, (tuple(sl), tuple(dk))
        if t == "swap":
            a, b = I[op[1]], I[op[2]]; sl[a], sl[b] = sl[b], sl[a]; return None, (tuple(sl), tuple(dk))
        if t == "cycle":
            d = dk[op[1]]; dk[op[1]] = d[1:] + d[:1]; return None, (tuple(sl), tuple(dk))
        if t == "peekdeck":
            d = dk[op[1]]; o = d[0]; dk[op[1]] = d[1:]; return o, (tuple(sl), tuple(dk))
        if t == "discarddeck":
            dk[op[1]] = (); return None, (tuple(sl), tuple(dk))
        if t == "peek":
            o = sl[I[op[1]]]; sl[I[op[1]]] = None; return o, (tuple(sl), tuple(dk))
        if t == "discard":
            sl[I[op[1]]] = None; return None, (tuple(sl), tuple(dk))
        if t in ("ndp", "read"):
            return sl[I[op[1]]], state
        if t == "mark":
            return sum(1 if sl[I[s]] == 0 else -1 for s in self.systems[op[1]]["hidden"]), state
        if t == "cswap":
            if sl[I[op[1]]] == 0:
                a, b = I[op[2]], I[op[3]]; sl[a], sl[b] = sl[b], sl[a]
            return None, (tuple(sl), tuple(dk))
        raise ValueError(op)

def canon(dist):
    return tuple(sorted(dist.items(), key=lambda kv: repr(kv[0])))

def normalise(dist):
    tot = sum(dist.values()); return {k: v / tot for k, v in dist.items()}

# ---------------------------------------------------------------- closure (reachability layer)
def closure(model, s_max=300000, d_max=None):
    start = model.initial()
    seen = {canon(start): 0}; nodes = [start]; depth = [0]; branchp = set()
    frontier = [0]; d = 0
    while frontier:
        if d_max is not None and d >= d_max:
            return nodes, depth, branchp, {"status": "PARKED", "reason": f"d_max={d_max} reached", "depth": d}
        nxt = []
        for ni in frontier:
            dist = nodes[ni]; pat = Model.pattern(next(iter(dist)))
            for op in model.ops:
                if not model.applicable(op, pat):
                    continue
                split = defaultdict(dict)
                for st, p in dist.items():
                    o, ns = model.apply(op, st)
                    split[o][ns] = split[o].get(ns, F(0)) + p
                for o, sub in split.items():
                    tot = sum(sub.values())
                    if tot != 1: branchp.add(tot)
                    c = normalise(sub); key = canon(c)
                    if key not in seen:
                        seen[key] = len(nodes); nodes.append(c); depth.append(d + 1); nxt.append(len(nodes) - 1)
                        if len(nodes) > s_max:
                            return nodes, depth, branchp, {"status": "PARKED", "reason": f"s_max={s_max}", "depth": d + 1}
        frontier = nxt; d += 1
    return nodes, depth, branchp, {"status": "FIXED POINT", "depth": d - 1}

# ---------------------------------------------------------------- marginals and operational states
def marginal(dist, model, slotnames):
    ix = [model.idx[s] for s in slotnames]; out = {}
    for (slots, decks), p in dist.items():
        key = tuple(slots[i] for i in ix); out[key] = out.get(key, F(0)) + p
    return out

def full_states(nodes, depth, model, slotnames, require_filled=()):
    """preparable states of the system on slotnames (rest discarded): node marginals with all of slotnames
    filled (and require_filled slots filled). Returns dict canon -> (dist, min depth)."""
    out = {}
    for n, dpt in zip(nodes, depth):
        st0 = next(iter(n))
        if any(st0[0][model.idx[s]] is None for s in list(slotnames) + list(require_filled)):
            continue
        m = marginal(n, model, slotnames); key = canon(m)
        if key not in out or out[key][1] > dpt:
            out[key] = (m, dpt)
    return out

def all_arrangements(model, slotnames):
    return list(itertools.product(range(model.k), repeat=len(slotnames)))

def vec(dist, basis):
    return [dist.get(b, F(0)) for b in basis]

def in_hull(target, cands, basis):
    """exact: is target in conv(cands)? restrict to candidates with support inside target's support."""
    supp = {b for b in basis if target.get(b, 0) != 0}
    cs = [c for c in cands if all(b in supp for b, v in c.items() if v != 0)]
    rows = sorted(supp, key=repr)
    lam = feasible([[c.get(r, F(0)) for r in rows] for c in cs], [target[r] for r in rows])
    return (lam is not None), (cs, lam)

def is_extreme(target, pool, basis):
    others = [c for c in pool if canon(c) != canon(target)]
    inside, _ = in_hull(target, others, basis)
    return not inside

def pair_decomp(target, pool, basis, gen=None):
    """budget reading: target = w r1 + (1-w) r2, r1 != r2 in pool, 0<w<1. Returns (w, r1, r2) or None.
    If gen (a set of generated weights) is given, a decomposition whose w or 1-w lies in gen is preferred."""
    supp = {b for b in basis if target.get(b, 0) != 0}
    cs = [c for c in pool if canon(c) != canon(target) and all(b in supp for b, v in c.items() if v != 0)]
    tv = vec(target, basis)
    dirs = {}
    for c in cs:
        d = [t - x for t, x in zip(tv, vec(c, basis))]
        piv = next(x for x in d if x != 0); key = tuple(x / abs(piv) for x in d)
        dirs.setdefault(key, []).append((c, d))
    first = None
    for key, lst in dirs.items():
        neg = tuple(-x for x in key)
        if neg not in dirs: continue
        for r1, d1 in lst:
            for r2, d2 in dirs[neg]:
                n1 = sum(abs(x) for x in d1); n2 = sum(abs(x) for x in d2)
                w = n2 / (n1 + n2)
                mix = [w * a + (1 - w) * b for a, b in zip(vec(r1, basis), vec(r2, basis))]
                assert mix == tv
                if gen is None or w in gen or (1 - w) in gen:
                    return (w, r1, r2)
                if first is None: first = (w, r1, r2)
    return first

# ---------------------------------------------------------------- Lemma W on a system alone (deck discarded)
def lemma_w_rank(model, slotnames, ops_kinds):
    """W iteration on the system's own ontic space (each slot empty or a colour), with the system-local ops of
    the given kinds; returns (rank of W restricted to fully filled arrangements, number of arrangements)."""
    vals = [None] + list(range(model.k))
    space = list(itertools.product(vals, repeat=len(slotnames)))
    pos = {s: i for i, s in enumerate(space)}
    ix = {s: i for i, s in enumerate(slotnames)}
    sysof = model.sys_of
    def local_ops():
        ops = []
        for s in slotnames:
            if "peek" in ops_kinds: ops.append(("peek", s))
            if "ndp" in ops_kinds: ops.append(("ndp", s))
            if "read" in ops_kinds and s.endswith("v"): ops.append(("read", s))
        for s, t in itertools.combinations(slotnames, 2):
            if sysof[s] == sysof[t] and "swap" in ops_kinds: ops.append(("swap", s, t))
        if "mark" in ops_kinds:
            for sname, d in model.systems.items():
                if all(h in ix for h in d["hidden"]): ops.append(("mark", sname))
        if "cswap" in ops_kinds and all(x in ix for x in ("a1", "b1", "b2")): ops.append(("cswap",))
        return ops
    def act(op, st):
        st = list(st); t = op[0]
        if t == "peek":
            i = ix[op[1]]; o = st[i]; st[i] = None; return o, tuple(st)
        if t in ("ndp", "read"):
            return st[ix[op[1]]], tuple(st)
        if t == "swap":
            a, b = ix[op[1]], ix[op[2]]; st[a], st[b] = st[b], st[a]; return None, tuple(st)
        if t == "mark":
            hs = model.systems[op[1]]["hidden"]
            if any(st[ix[h]] is None for h in hs): return "na", tuple(st)
            return sum(1 if st[ix[h]] == 0 else -1 for h in hs), tuple(st)
        if t == "cswap":
            if st[ix["a1"]] == 0:
                a, b = ix["b1"], ix["b2"]; st[a], st[b] = st[b], st[a]
            return None, tuple(st)
    # transition functionals: w T_{a,o}: (wT)(x) = sum_y w(y) T(y|x) with deterministic y = f(x) and outcome o(x)
    N = len(space)
    ops = local_ops()
    def apply_func(w, op, o):
        out = [F(0)] * N
        for x in space:
            oo, y = act(op, x)
            if oo == o: out[pos[x]] = w[pos[y]]
        return out
    outcomes = {}
    for op in ops:
        outcomes[op] = sorted({act(op, x)[0] for x in space}, key=repr)
    basis = []  # row-reduced
    def reduce(v):
        v = list(v)
        for (pc, bv) in basis:
            if v[pc] != 0:
                f = v[pc] / bv[pc]; v = [a - f * b for a, b in zip(v, bv)]
        return v
    def add(v):
        r = reduce(v)
        pc = next((i for i, x in enumerate(r) if x != 0), None)
        if pc is None: return False
        basis.append((pc, r)); return True
    W = [[F(1)] * N]; add(W[0]); frontier = [W[0]]
    while frontier:
        nf = []
        for w in frontier:
            for op in ops:
                for o in outcomes[op]:
                    v = apply_func(w, op, o)
                    if add(v): nf.append(v)
        frontier = nf
    filled = [pos[x] for x in space if all(c is not None for c in x)]
    # rank of W restricted to filled coordinates
    rows = [[bv[i] for i in filled] for _, bv in basis]
    rb = []
    for r in rows:
        r = list(r)
        for (pc, bv) in rb:
            if r[pc] != 0:
                f = r[pc] / bv[pc]; r = [a - f * b for a, b in zip(r, bv)]
        pc = next((i for i, x in enumerate(r) if x != 0), None)
        if pc is not None: rb.append((pc, r))
    return len(rb), len(filled), len(basis)

# ---------------------------------------------------------------- milestone analysis
def fmt(d):
    return "{" + ", ".join(f"{''.join('RB'[c] if c is not None else '_' for c in k)}:{v}" for k, v in sorted(d.items(), key=lambda kv: repr(kv[0])) if v) + "}"

def analyse(model, Aslots, Bslots, nodes, depth, branchp, require_filled=(), verbose=True, out=print):
    AB = list(Aslots) + list(Bslots)
    # pools: every preparable state of AB / of A (everything else discarded), unrestricted.
    # candidates: AB states from preparations meeting require_filled (e.g. a spectator card left in play).
    PAB = full_states(nodes, depth, model, AB)
    PA = full_states(nodes, depth, model, Aslots)
    CAND = full_states(nodes, depth, model, AB, require_filled) if require_filled else PAB
    basisAB = all_arrangements(model, AB); basisA = all_arrangements(model, Aslots)
    poolAB = [v[0] for v in PAB.values()]; poolA = [v[0] for v in PA.values()]
    cands = [v[0] for v in CAND.values()]
    # pure (convex-closure reading: extreme) composite states
    extreme = [c for c in cands if is_extreme(c, poolAB, basisAB)]
    budget_pure = [c for c in cands if pair_decomp(c, poolAB, basisAB) is None]
    extA = {canon(c) for c in poolA if is_extreme(c, poolA, basisA)}
    def margA(c):
        m = {}
        for k, v in c.items():
            kk = k[:len(Aslots)]; m[kk] = m.get(kk, F(0)) + v
        return {k: v for k, v in m.items() if v}
    witnesses = []
    for c in extreme:
        mA = margA(c)
        if canon(mA) not in extA:
            dec = pair_decomp(mA, poolA, basisA, branchp)
            witnesses.append((c, mA, dec, PAB[canon(c)][1]))
    bw = []
    for c in budget_pure:
        mA = margA(c)
        if pair_decomp(mA, poolA, basisA) is not None:
            bw.append(c)
    res = {"n_cand": len(cands), "n_PAB": len(poolAB), "n_PA": len(poolA), "n_extreme": len(extreme), "n_budget_pure": len(budget_pure),
           "n_M1_witness_extreme": len(witnesses), "n_M1_witness_budget": len(bw)}
    # best biased witness: accessible binary measurement = peek a1 (colour 0)
    best = None
    for c, mA, dec, dp in witnesses:
        p0 = sum(v for k, v in mA.items() if k[0] == 0)
        if best is None or abs(p0 - F(1, 2)) > abs(best[0] - F(1, 2)) or (p0 == F(3, 4)):
            if best is None or best[0] != F(3, 4): best = (p0, c, mA, dec, dp)
    res["witness_P(a1=R) values"] = sorted({str(sum(v for k, v in mA.items() if k[0] == 0)) for c, mA, dec, dp in witnesses})
    if verbose:
        out(f"    |Prep(AB)| = {len(poolAB)}, |Prep(A)| = {len(poolA)}; extreme AB = {len(extreme)}; "
            f"budget-pure AB (no pair decomposition in Prep(AB)) = {len(budget_pure)}")
        out(f"    M1 witnesses: extreme AB with mixed A-marginal = {len(witnesses)}; budget-pure AB with pair-decomposable A-marginal = {len(bw)}")
        if witnesses:
            out(f"    witness P(a1=R) values: {res['witness_P(a1=R) values']}")
            p0, c, mA, dec, dp = best
            out(f"    sample witness (depth {dp}): psi_AB = {fmt(c)}")
            out(f"      A-marginal = {fmt(mA)}, P(a1=R) = {p0}")
            if dec:
                w, r1, r2 = dec
                out(f"      A-marginal = {w} * {fmt(r1)} + {1-w} * {fmt(r2)}  (weight in branch probs: {w in branchp or (1-w) in branchp})")
    return res, extreme, PAB, PA, margA

def pur_analysis(model, Aslots, Bslots, nodes, depth, out=print, extra_states=()):
    """Pur-E and Pur-U for system A with purifier B (same realization)."""
    AB = list(Aslots) + list(Bslots)
    PAB = full_states(nodes, depth, model, AB); PA = full_states(nodes, depth, model, Aslots)
    basisAB = all_arrangements(model, AB)
    poolAB = [v[0] for v in PAB.values()]
    pure = [c for c in poolAB if is_extreme(c, poolAB, basisAB)]
    nA = len(Aslots)
    def margA(c):
        m = {}
        for k, v in c.items():
            m[k[:nA]] = m.get(k[:nA], F(0)) + v
        return {k: v for k, v in m.items() if v}
    by_marg = defaultdict(list)
    for c in pure: by_marg[canon(margA(c))].append(c)
    states = [v[0] for v in PA.values()] + list(extra_states)
    have, lack = [], []
    for s in states:
        (have if canon({k: v for k, v in s.items() if v}) in by_marg else lack).append(s)
    nAB = len(AB)
    def why(s):
        # classify the obstruction for a state with no purification (pure AB states are E(M) on all AB slots)
        p = {k: v for k, v in s.items() if v}
        sym = all(p.get(k, 0) == p.get(tuple(k[i] for i in perm), 0) for k in p for perm in itertools.permutations(range(nA)))
        if not sym: return "not exchangeable (never an E(M) marginal)"
        if nA == 2:
            pr = sum(v for k, v in p.items() if k[0] == 0); prr = p.get((0, 0), 0)
            if prr > pr * pr or (prr == pr * pr and pr not in (0, 1)): return "P(RR) >= P(R)^2, not monochrome: no E(M) of any size"
        # does some E(M) with |M| = nAB have this marginal (deck permitting)?
        for r in range(nAB + 1):
            seqs = set(itertools.permutations([0] * r + [1] * (nAB - r)))
            mm = {}
            for q in seqs: mm[q[:nA]] = mm.get(q[:nA], F(0)) + F(1, len(seqs))
            if canon({k: v for k, v in mm.items() if v}) == canon(p): return f"E(M) with {r}R exists but is not preparable in this deck"
        return f"no E(M) on {nAB} slots has this marginal (purifier too small)"
    reasons = defaultdict(int)
    for s in lack: reasons[why(s)] += 1
    out(f"    Pur-E: {len(have)} of {len(states)} preparable A-states have a purification in B={Bslots}; lacking: "
        + ", ".join(fmt(s) for s in lack[:8]) + (" ..." if len(lack) > 8 else ""))
    if lack: out("      obstruction classes: " + "; ".join(f"{k}: {v}" for k, v in sorted(reasons.items())))
    # Pur-U: B-local reversible ops = permutations of B's slots within each B-system
    bsys = defaultdict(list)
    for s in Bslots: bsys[model.sys_of[s]].append(s)
    perms = [()]
    groups = []
    for sname, sl in bsys.items():
        groups.append([list(p) for p in itertools.permutations(range(len(sl)))])
    unconnected = 0; pairs = 0
    for key, lst in by_marg.items():
        for c1, c2 in itertools.combinations(lst, 2):
            pairs += 1; ok = False
            for perm in itertools.permutations(range(len(Bslots))):
                # restrict to permutations within B systems
                if any(model.sys_of[Bslots[i]] != model.sys_of[Bslots[perm[i]]] for i in range(len(Bslots))):
                    continue
                img = {}
                for k, v in c1.items():
                    b = k[nA:]; nb = tuple(b[perm[i]] for i in range(len(b)))
                    img[k[:nA] + nb] = v
                if canon(img) == canon(c2): ok = True; break
            if not ok: unconnected += 1
    out(f"    Pur-U: pure AB states = {len(pure)}; pairs with equal A-marginal = {pairs}; unconnected by B-local reversible ops = {unconnected}")
    return {"reasons": dict(reasons), "purE_have": len(have), "purE_total": len(states), "purE_lack": [fmt(s) for s in lack],
            "purU_pairs": pairs, "purU_unconnected": unconnected}
