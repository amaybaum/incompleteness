import json, sys, subprocess, re, collections
S=sys.argv[1]; A=sys.argv[2]
ns={}; exec(open(f'{S}/C-completeness-data.py').read(), ns); CMP=ns['ROWS']
ns2={}; exec(open(f'{S}/C-consistency-data.py').read(), ns2); CON=ns2['ROWS']
# validate sites
def lines_of(path):
    p=f'{S}/tree939/{path}'
    try: return open(p,encoding='utf-8').read().split('\n')
    except FileNotFoundError:
        out=subprocess.run(['git','-C',f'{S}/icaudit','-c','gc.auto=0','show',f'eae01647:{path}'],capture_output=True,text=True)
        return out.stdout.split('\n') if out.returncode==0 else None
bad=[]
def chk(site):
    m=re.match(r'^(.*):(\d+)@eae01647$',site)
    if not m: return
    L=lines_of(m.group(1))
    if L is None or int(m.group(2))>len(L) or not L[int(m.group(2))-1].strip(): bad.append(site)
for r in CMP:
    for x in r['sources']: chk(x)
for r in CON:
    for x in r['sites']: chk(x['site'])
    chk(r['anchor']['site'])
print('bad sites:', bad)
meta=dict(audit_step="5 (completeness) and 4 (corpus consistency)", author="mapper C", corpus_commit="eae01647f50d9e2aa90957fbd6c59d8cf44e7681",
          introduction_commit="4a260ca9d6414e4d504a629ba5a0eb3c70bd4704", site_format="file:line@commit; lean:Module.lean:line:decl")
json.dump(dict(meta=meta, rows=CMP), open(f'{A}/completeness.json','w'), ensure_ascii=False, indent=1)
json.dump(dict(meta=meta, rows=CON), open(f'{A}/consistency.json','w'), ensure_ascii=False, indent=1)
print(len(CMP), collections.Counter(r['recommendation'] for r in CMP), collections.Counter(r['priority'] for r in CMP))
print(len(CON), collections.Counter(r['severity'] for r in CON), sum(r['touches_intro'] for r in CON))
