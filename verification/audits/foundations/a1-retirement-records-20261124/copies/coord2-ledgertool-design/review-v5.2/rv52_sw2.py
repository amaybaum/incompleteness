"""SW2 under DESIGN-v5.2's corrected expectation, run with the Stage 1 engine (8c1e628a, from `git archive`
into toolcopy/; the worktree is not touched). For each of the 584 sites unchanged in E..H: delete the last token
of its line at H; run coverage with segments E..H (hp) and H..X (unledgered). Predicate, items compared by
(obligation, class, segment, fingerprint): exactly one new FAIL naming the site, obligation RET, class
unauthorized-change, segment H..X; every item naming the site at the unmutated H still present."""
import sys, os, json, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'toolcopy', 'tools'))
sys.dont_write_bytecode = True
from ledger_coverage.adapters import a1_controls as ac
from ledger_coverage.engine import pipeline as pl, gitobj, context as ctxmod, cli
REPO = '<repo>'; IMPL = '8c1e628a08272ad9414929fa8e003020e1cc2234'
CFG = 'verification/audits/foundations/ledger-coverage-tool-20261123/a1exit-retirement-config.json'
E, H = ac.E, ac.H
a = ac.A1(REPO, '%s:%s' % (IMPL, CFG), os.path.join(HERE, 'sw2out'))
loaded = ac.cfgmod_loaded(a); cfg = loaded.config
sm = cli.load_adapter_input(a.repo, loaded, 'sitemap')
ctx = pl.RunContext(a.repo, cfg, loaded.profiles, [], {}, ctxmod.Indicators(cfg['indicators']), sitemap=sm)
sites = pl.build_sites(ctx)
chain = gitobj.first_parent_chain(a.repo, E, H); par = {}; prev = E
for c in chain: par[c] = prev; prev = c
merges = {m['commit'] for m in cfg['hp_obligations'][0]['merges']}
hp_seg = {'from': E, 'to': H, 'kind': 'hp', 'chain': chain, 'parent_of': par, 'merges': merges, 'obligation': 'HP'}
base_cv = pl.Coverage(ctx, H, [dict(hp_seg)], None, {}, []).run()
hp_sites = {k for k, so in base_cv.site_out.items() if so.get('hp_steps')}
key = lambda i: (i['obligation'], i['class'], i['segment'] or '', i['fingerprint'])
base_items = {}
for i in base_cv.items: base_items.setdefault(i['subject'], set()).add(key(i))
todo = [s for s in sites if s['site_id'] not in hp_sites]
bad = []; with_hp = []; t0 = time.time()
for s in todo:
    f = s['file']; lines = list(ctx.ft(H, f).lines)
    idx = [st.start for st in base_cv.states if st.site['site_id'] == s['site_id']][0]
    toks = lines[idx].split(' '); nz = [k for k, x in enumerate(toks) if x]; k = nz[-1]
    lines[idx] = ' '.join(toks[:k] + toks[k + 1:])
    x = a.repo.derive(H, {f: ('\n'.join(lines) + '\n').encode()}, parents=[H])
    cv = pl.Coverage(ctx, x, [dict(hp_seg), {'from': H, 'to': x, 'kind': 'unledgered'}], None, {}, []).run()
    now = {key(i): i for i in cv.items if i['subject'] == s['site_id']}
    before = base_items.get(s['site_id'], set())
    new = [i for kk, i in now.items() if kk not in before]
    newfail = [i for i in new if i['decision'] == 'FAIL']
    lost = [kk for kk in before if kk not in now]
    ok = (len(newfail) == 1 and newfail[0]['obligation'] == 'RET' and newfail[0]['class'] == 'unauthorized-change'
          and (newfail[0]['segment'] or '').startswith(H) and not lost and len(new) == 1)
    if before: with_hp.append(s['site_id'])
    if not ok: bad.append({'site': s['site_id'], 'new': [(i['obligation'], i['class'], i['segment']) for i in new], 'lost': lost})
    ctx._ft = {k_: v for k_, v in ctx._ft.items() if k_[0] in (E, H) or k_[0] in par}
res = {'sites': len(todo), 'holds': len(todo) - len(bad), 'violations': bad, 'sites_with_items_at_unmutated_H': with_hp,
       'seconds': round(time.time() - t0, 1)}
json.dump(res, open(os.path.join(HERE, 'out52-sw2.json'), 'w'), indent=1)
print(json.dumps({k: v for k, v in res.items() if k != 'violations'}, indent=0), 'violations', len(bad), bad[:3])
