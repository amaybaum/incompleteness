# Reviewer's lint: S1 rules.lint_rule on the PROPOSED v2 file (as written) and on v1 with recorded_at in {T1',H,main}.
import sys, json, subprocess, copy
TC, REPO, CFG, V2 = sys.argv[1:5]
sys.path.insert(0, TC + '/tools')
from ledger_coverage.engine import util, rules as R, profiles as PR
def show(c, p):
    r = subprocess.run(['git','-C',REPO,'show','%s:%s'%(c,p)],capture_output=True); return r.stdout if r.returncode==0 else None
P='4c79be642ca631573f06b444903be75ec4f5e2b6'
cfg = json.load(open(CFG)); ABBR = cfg['sentence']['abbreviations']
def read_source(src):
    # staged config: commit P or None -> read at P (F would hold the same blob)
    if 'ledger-coverage-tool-20261123' in src['path']: return open(TC+'/'+src['path'],'rb').read()
    return show(src.get('commit') or P, src['path'])
profs = {}
for sp in cfg['profiles']:
    p, h = PR.load_profile(sp, read_source)
    assert h == sp['pattern_sha256'], sp['name']
    profs[sp['name']] = p
deny = [p for p in profs.values() if p.kind == 'deny' and p.applies_to == 'tree']
cache = {}
def look(commit, f, ssha):
    k=(commit,f)
    if k not in cache:
        b=show(commit,f); cache[k]=util.sentences_of(util.lines_of(util.decode(b,f)),ABBR,2) if b else []
    ss=cache[k]
    for j,(s,_,_) in enumerate(ss):
        if util.sha256(s)==ssha:
            return s, [ss[i][0] for i in (j-1,j+1) if 0<=i<len(ss)], R.sentence_context_sha(ss,j)
    return None
v1 = json.load(open(TC+'/verification/audits/foundations/ledger-coverage-tool-20261123/rules/w1-w2-allow-v1.json'))
v2 = json.load(open(V2))
for name, c in [('T1p','14ac71b4b0a0c0aa2d7068d6799a73f474097060'),('H','53c6601a10419b6b333cc992474272501ab542af'),('main','9deb69568d8231210c7f39cb65be943dea566371')]:
    tot=[]
    for r in v1['rules']:
        r2=copy.deepcopy(r); r2['recorded_at']=c; tot+=R.lint_rule(r2, profs.get, look, deny, {})
    print('v1@%s problems=%d %s'%(name,len(tot),tot[:4]))
tot=[]
for r in v2['rules']: tot+=R.lint_rule(r, profs.get, look, deny, {})
print('v2-as-proposed (recorded_at=%s) problems=%d %s'%(v2['rules'][0]['recorded_at'][:8],len(tot),tot))
# per-fingerprint sentence/context reproduction
for r in v2['rules']:
    for fp in r['fingerprints']:
        row=[r['id'],fp['file'].split('/')[-1],'ctx_req=%s'%r['context_required'],'allow=%s'%fp.get('negative_allowance')]
        for n,c in [('T1p','14ac71b4b0a0c0aa2d7068d6799a73f474097060'),('H','53c6601a10419b6b333cc992474272501ab542af'),('main','9deb69568d8231210c7f39cb65be943dea566371')]:
            g=look(c,fp['file'],fp['sentence_sha256'])
            row.append('%s:%s%s'%(n,'S' if g else '-','C' if g and g[2]==fp['context_sha256'] else '-'))
        print(' '.join(row))
# D1 self-pass with own neighbours at H for all rules (not skipped on context difference)
H='53c6601a10419b6b333cc992474272501ab542af'
for r in v2['rules']:
    for fp in r['fingerprints']:
        s,neigh,ctx=look(H,fp['file'],fp['sentence_sha256'])
        spans=[(a,b) for pn in r['profiles'] for _,a,b in profs[pn].matches(s)]
        dh=any(dp.matches(s) for dp in deny)
        print('selfpass@H',r['id'],fp['file'].split('/')[-1],R.apply_allow([r], fp['file'], s, neigh, ctx, spans, dh, {}, None, None))
