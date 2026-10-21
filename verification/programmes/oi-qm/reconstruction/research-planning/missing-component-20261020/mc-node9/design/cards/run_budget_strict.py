"""Budget reading with generated weights only: psi is impure at budget iff psi = w r1 + (1-w) r2 with r1 != r2 in
Prep(AB) and w (or 1-w) a branch probability printed by the reachability layer. Counts M1 witnesses under this
stricter reading (more states count as pure) for the variants where the extreme reading gave M1 FAIL."""
import sys
from cardtheory import *
def strict(variant, req=()):
    flags = () if variant in ("BASE", "SPECT") else (variant,)
    tot = 0; wit = 0; extra_pure = 0
    for n in range(2, 7):
        for r in range(0, n + 1):
            for na in (1, 2):
                for nb in (1, 2):
                    need = na + nb + (1 if variant == "SPECT" else 0)
                    if n < need: continue
                    A = [f"a{i+1}" for i in range(na)]; B = [f"b{i+1}" for i in range(nb)]
                    ss = {"a": A, "b": B}
                    if variant == "SPECT": ss["c"] = ["c1"]
                    m = Model([(r, n - r)], ss, flags)
                    nodes, depth, bp, st = closure(m)
                    AB = A + B
                    PAB = full_states(nodes, depth, m, AB); PA = full_states(nodes, depth, m, A)
                    CAND = full_states(nodes, depth, m, AB, ("c1",)) if variant == "SPECT" else PAB
                    bAB = all_arrangements(m, AB); bA = all_arrangements(m, A)
                    pool = [v[0] for v in PAB.values()]; poolA = [v[0] for v in PA.values()]
                    for c in [v[0] for v in CAND.values()]:
                        dec = pair_decomp(c, pool, bAB, bp)
                        gen_ok = dec is not None and (dec[0] in bp or (1 - dec[0]) in bp)
                        if gen_ok: continue
                        if is_extreme(c, pool, bAB) is False: extra_pure += 1
                        mA = {}
                        for k, v in c.items(): mA[k[:na]] = mA.get(k[:na], F(0)) + v
                        mA = {k: v for k, v in mA.items() if v}
                        if pair_decomp(mA, poolA, bA, None) is not None: wit += 1
                    tot += 1
    print(f"  {variant}: realizations={tot}; states pure only under the generated-weight budget reading={extra_pure}; "
          f"M1 witnesses under that reading={wit}", flush=True)
for v in sys.argv[1:]:
    strict(v)
