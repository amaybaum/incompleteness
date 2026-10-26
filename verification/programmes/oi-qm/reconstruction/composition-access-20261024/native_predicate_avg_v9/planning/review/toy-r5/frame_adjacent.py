"""Reviewer probe (toy G setup only): r4's frame-adjacent G family contains its own in-frame
-x tip quantity, which covers that tip. Compare with the same family minus that quantity."""
import sys, json
sys.path.insert(0, sys.argv[1])
import s0geom as G, s0controls as C
ctx = G.Context(C.TOYG, (), 'G')
pair = ctx.pair
out = {}
for name in ['frozen', 'decide_frame_ignore_minus_x', 'blind_G_minus_y', 'ignore_fixed_minus_y']:
    rule = C.MUTANTS[name]
    rows = []
    for d in range(1, 5):
        q = ((C.TOYG.n + 2 + d, 0, 0), d)
        fam = C.family(q, pair, 3)
        tip = ((C.TOYG.n + 2, 0, 0), 0)
        assert tip in fam and not ctx.eligible(tip)
        r_full, _ = G.closure(ctx.fixed, fam, pair, 3, rule, ctx.eligible)
        r_less, _ = G.closure(ctx.fixed, fam - {tip}, pair, 3, rule, ctx.eligible)
        f_less, _ = G.closure(ctx.fixed, fam - {tip}, pair, 3, G.FROZEN, ctx.eligible)
        rows.append({'d': d, 'r4_family_retained': '%d/%d' % (len(r_full), len(fam)),
                     'minus_inframe_tip_retained': '%d/%d' % (len(r_less), len(fam) - 1),
                     'frozen_minus_inframe_tip': len(f_less)})
    out[name] = rows
print(json.dumps(out, indent=0))
