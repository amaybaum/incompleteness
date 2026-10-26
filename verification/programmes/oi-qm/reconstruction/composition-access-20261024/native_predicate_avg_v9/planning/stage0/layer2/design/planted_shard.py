"""Layer-2 design evidence: the survivor path of the production shard code (l2enum.Shard.rep)
on planted records of the toy geometry. The toy class has no survivors, so its enumeration
never reaches the per-survivor gates (C7, C8 on the full orbit, C11 (i) and (ii), C17, C18 on
survivors), the residue detail or the minimal-witness path. This script drives them with
planted records of the toy setup (not records of the toy index space, and not v8's class):

- the constraint-block record: the item (c0, L + 1) together with the six items (c0 + e, L),
  for the toy A pair (E, L) = (3, 4) and c0 = (5, 0, 0) (C3's block, read as a 7-item record);
- the same with the item (c0, L) in place of (c0, L + 1) (the block without its top).

Positive run: the bound is the union of the planted contexts, so C9 holds by construction;
every gate must hold, and the reference gates must run on every member of each survivor orbit
in both conventions (L2-R2); C7 runs per record on set 1 (erratum E1, item E1-F3), each with its
own C0 check, and the shard reports the per-set coverage. The planted orbits have a nontrivial
stabilizer, so E1-F6's survivor cell N_ST is nonzero under A and G (non-vacuity of that path). Negative control: the same record with one retained quantity
removed from the A bound; C9 must fail, and the shard's running minimum witness (L2-R1),
confirmed by direct closure, must be the C16-minimal record among the candidates. Usage: python3 -I -B planted_shard.py <layer2/code>. Prints JSON; exit 0 iff
both runs behave as stated.
"""
import json
import sys

sys.path.insert(0, sys.argv[1])
import s0geom as G        # noqa: E402
import l2analysis as AN   # noqa: E402
import l2enum as ENUM     # noqa: E402
import l2config as CFG    # noqa: E402

setup = CFG.make_setup(G, 'toy')
grp = AN.group(setup)
pairA = G.Pair(setup.n + 1)
c0 = (5, 0, 0)
L = pairA.L
blk = tuple(sorted([(c0, L + 1)] + [(G.vadd(c0, e), L) for e in G.axes(3)]))
blk_minus_top = tuple(sorted([(c0, L)] + [(G.vadd(c0, e), L) for e in G.axes(3)]))
records = [(-1, blk), (-2, blk_minus_top)]


def universe(recs):
    out = {}
    for conv in ('A', 'G'):
        qs = set()
        for _, r in recs:
            for m in AN.orbit(r, grp):
                qs |= G.Context(setup, m, conv).quants
        out[(conv, 'L3prime')] = set(qs)
        out[(conv, 'L3')] = set(qs)
    return out


def run(bound):
    base = {conv: set(G.Context(setup, (), conv).run()) for conv in ('A', 'G')}
    sh = ENUM.Shard(setup, CFG.profile('toy'), bound, base, None, None)
    for idx, r in records:
        sh.rep(idx, r, AN.orbit(r, grp))
    return sh


pos = run(universe(records))
po = pos.output()
summary = []
for det in po['survivors']:
    summary.append({'index': det['index'], 'orbit_size': det['orbit_size'],
                    'A': {k: det['A'][k] for k in ('survivor', 'n_survivor', 'rule_dependence', 'cover_components',
                                                   'residual_support_bits', 'exceeds_S_max', 'phi_linked')}
                    | {'shared_aligned_tips': len(det['A']['shared_aligned_tips'])},
                    'G': {k: det['G'][k] for k in ('survivor', 'n_survivor', 'rule_dependence')}})
members = sum(len(AN.orbit(r, grp)) for _, r in records)
pos_ok = len(po['survivors']) == po['survivor_representatives'] >= 1 and \
    all(v['failed'] == 0 for v in po['gates'].values()) and po['gates']['C11ii']['checked'] > 0 and \
    po['gates']['C8']['checked'] >= 1 and \
    all(po['gates'][k]['checked'] == 2*members for k in ('C7', 'C11i', 'C17', 'C18')) and \
    po['gates']['C0_context']['checked'] == 4*members and \
    all(po['C7_scope_coverage'][c]['1_Surv']['records_checked'] == members for c in ('A', 'G')) and \
    all(po['counts_additive']['%s:deg:nontrivial_stabilizer:survivor=True' % c] == members for c in ('A', 'G'))

# negative control: remove one retained quantity of the block from the A bound
retA = G.Context(setup, blk, 'A').run()
drop = sorted(retA)[0]
bound = universe(records)
bound[('A', 'L3prime')].discard(drop)
bound[('A', 'L3')].discard(drop)
neg = run(bound).output()
w = neg['witness_min']
neg_ok = neg['gates']['C9']['failed'] > 0 and neg['witness_candidates_seen'] > 0 and w is not None and \
    any(c.startswith('C9') for c in w['conditions'])
out = {'planted_records': {'block': [[list(x), t] for x, t in blk], 'block_minus_top': [[list(x), t] for x, t in blk_minus_top]},
       'positive': {'gates': po['gates'], 'survivor_representatives': po['survivor_representatives'],
                    'C7_scope_coverage': po['C7_scope_coverage'],
                    'orbit_members': members, 'summary': summary,
                    'counts_nonzero': {k: v for k, v in po['counts_additive'].items() if v}, 'pass': pos_ok},
       'negative_C9': {'dropped_from_A_bound': [list(drop[0]), drop[1]], 'gates_C9': neg['gates']['C9'],
                       'witness_candidates_seen': neg['witness_candidates_seen'], 'minimal_witness': w,
                       'pass': neg_ok},
       'pass': pos_ok and neg_ok}
print(json.dumps(out, sort_keys=True, indent=1))
sys.exit(0 if out['pass'] else 2)
