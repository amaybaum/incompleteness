"""Layer-2 design evidence: the production path's 58 reported counts on the toy class (sharded,
orbit-reduced, merged: toyrun/result.json) against full per-record computations independent of
the production path.
- The 54 counts of L1 C8: the control suite's full per-record computation (s0controls C8
  'counts', retained in toyrun/preflight.json), as in r2.
- The four counts erratum E1 adds (E1-F6), N_ME,c and N_ST,c: computed here on every toy record
  with stage0/code-r5/s0ref.py (the frozen design-evidence reference, not the Layer-2 copy): each
  record's survivor status from its full reference closure (A: a non-fixed quantity retained;
  G: a retained quantity with an eligible tip), masking equivalence by grouping the records'
  reference contexts, and the stabilizer by this script's own enumeration of C4v.
masking_equivalent_records is compared in both readings: the merge's (contexts with E1 merges)
and code-r5's (record samples), which coincide on the toy class.
Usage: python3 -I -B crosscheck.py <toyrun dir> <stage0/code-r5>. Prints JSON; exit 0 iff every
count agrees."""
import json
import os
import sys
from itertools import permutations, product

d, r5 = sys.argv[1], sys.argv[2]
sys.path.insert(0, r5)
import s0ref as REF  # noqa: E402  (code-r5's frozen design-evidence reference)

with open(os.path.join(d, 'result.json')) as f:
    res = json.load(f)
with open(os.path.join(d, 'preflight.json')) as f:
    full = json.load(f)['controls_counts_C8']
merged = res['counts']

# the toy class, written from the plan text (3D, n = 2, ball(1), slices -1..6, port (0, 0, -2))
DIM, N_, RHO, TLAST, PORT = 3, 2, 1, 6, (0, 0, -2)
if (DIM, N_, PORT) == (3, 6, (0, 0, -3)):
    raise SystemExit('refusing: v8 configuration class')
region = sorted(c for c in product(range(-RHO, RHO + 1), repeat=DIM) if sum(abs(x) for x in c) <= RHO)
slices = list(range(-1, TLAST + 1))
items = [(x, t) for x in region for t in slices]
records = [(it,) for it in items] + [((a, t1), (b, t2)) for i, a in enumerate(region) for b in region[i + 1:]
                                     for t1 in slices for t2 in slices]


def c4v():
    q8, q10 = (0, 0, -1), (0, 0, 1)
    out = []
    for pp in permutations(range(DIM)):
        for ss in product((1, -1), repeat=DIM):
            def g(c, pp=pp, ss=ss):
                return tuple(ss[i]*c[pp[i]] for i in range(DIM))
            if {g(c) for c in region} == set(region) and g(PORT) == PORT and g(q8) == q8 and g(q10) == q10:
                out.append(g)
    return out


grp = c4v()
surv = {'A': {}, 'G': {}}
ctxkey = {}
for r in records:
    for conv in ('A', 'G'):
        fixed, quants, geo, elig = REF.ref_context(DIM, N_, PORT, r, conv)
        ret, _ = REF.greatest(fixed, quants, geo, elig, 8)
        surv[conv][r] = bool(ret) if conv == 'A' else any(elig(u) for q in ret for u in geo.tipset(q))
        if conv == 'A':
            ctxkey[r] = frozenset(quants)
cls = {}
for r, k in ctxkey.items():
    cls.setdefault(k, []).append(r)
me = {r: len(cls[ctxkey[r]]) >= 2 for r in records}
st = {r: sum(1 for g in grp if tuple(sorted((g(x), t) for x, t in r)) == tuple(sorted(r))) > 1 for r in records}
added = {}
for conv in ('A', 'G'):
    added['%s:deg:masking_equivalent:survivor=True' % conv] = sum(1 for r in records if me[r] and surv[conv][r])
    added['%s:deg:nontrivial_stabilizer:survivor=True' % conv] = sum(1 for r in records if st[r] and surv[conv][r])
indep = dict(full, **added)
diff = {k: [merged.get(k), indep[k]] for k in sorted(indep) if merged.get(k) != indep[k]}
extra = sorted(set(merged) - set(indep))
reading = [res['masking_equivalent_records_record_sample_reading'], full['masking_equivalent_records']]
marginals = {'masking_equivalent_records': sum(me.values()), 'nontrivial_stabilizer': sum(st.values())}
marg_ok = all(merged[k] == v for k, v in marginals.items())
nonzero = sum(1 for v in indep.values() if v)
out = {'compared': len(indep), 'from_control_suite': len(full), 'independent_added': added,
       'independent_marginals': marginals, 'records': len(records), 'differences': diff,
       'keys_only_in_merge': extra, 'record_sample_reading_vs_code_r5': reading, 'counts_nonzero': nonzero,
       'counts_identically_zero': len(indep) - nonzero, 'label': res['label'],
       'pass': len(full) == 54 and len(indep) == 58 and res.get('n_counts') == 58 and not diff and not extra and
       reading[0] == reading[1] and marg_ok}
print(json.dumps(out, indent=1, sort_keys=True))
sys.exit(0 if out['pass'] else 2)
