"""Reviewer probe (toy setup only): a planted family adjacent to Phi, whose near tip in
direction e is a Phi site-time (so a fixed quantity is the only other cover of that tip).
Frozen rule must retain it; does any direction mutant over-eliminate it, and does
P_A-dir (with its Phi clause) hold on the retained set?"""
import sys, json
sys.path.insert(0, sys.argv[1])
import s0geom as G, s0controls as C, s0ref as REF
ctx = G.Context(C.TOY, (), 'A')
pair, fixed = ctx.pair, ctx.fixed           # toy pair (3, 4); Phi six at slice 3, V at 4, p at 2
geo = REF.RefGeometry(3, pair.E)
out = {}
for name in ['frozen', 'rv_dir_ignore_fixed', 'rv_decide_ignore_fixed_y', 'blind_dir_minus_y', 'rv_decide_blind_y']:
    rule = C.MUTANTS[name]
    rows = []
    for d in (1, 2):                      # toy B depth d: slice E - d >= -1
        q = ((0, d - 1, 0), pair.E - d)   # B type; its -y near tip is ((0,-1,0), E): a Phi cell
        assert G.even(q)
        fam = C.family(q, pair, 3) - fixed   # the -y tip quantity IS Phi (E1), so Phi alone covers it
        ret, log = G.closure(fixed, fam, pair, 3, rule)
        ret_frozen, _ = G.closure(fixed, fam, pair, 3, G.FROZEN)
        pdir = REF.pa_dir_violations(ret, geo, lambda u: True, set(ctx.phi_cells)) if ret else []
        rows.append({'d': d, 'family_nonfixed': len(fam), 'retained': len(ret), 'frozen_retained': len(ret_frozen),
                     'pa_dir_violations': len(pdir)})
    out[name] = rows
print(json.dumps(out, indent=1))
