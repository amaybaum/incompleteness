import json,subprocess,sys,re,unicodedata
R='repos/amaybaum/incompleteness'
def gh(*a,inp=None):
    return subprocess.run(['gh','api',*a],input=inp,capture_output=True,text=True,check=True).stdout
def check(t):
    assert '\r' not in t
    bad=[c for c in t if unicodedata.category(c)=='Cf' or (c.isspace() and ord(c)>127)]
    assert not bad, bad
    for m in re.finditer(r'https?://github\.com/[^\s)\]>`]+',t):
        u=m.group(0)
        if re.search(r'/(blob|tree)/',u) and len(u)>101 and '#' not in u: raise SystemExit('LONG LINK '+u)
def edit(num, reps, add=(), remove=()):
    body=json.loads(gh(f'{R}/issues/{num}'))['body']
    new=body
    for o,n in reps:
        assert new.count(o)==1, (num,o)
        new=new.replace(o,n)
    check(new)
    open(f'<scratch>/blocks/{num}.before','w').write(body)
    gh('-X','PATCH',f'{R}/issues/{num}','--input','-',inp=json.dumps({'body':new}))
    rb=json.loads(gh(f'{R}/issues/{num}'))['body']
    print(num,'body match',rb==new)
    if add: gh('-X','POST',f'{R}/issues/{num}/labels','--input','-',inp=json.dumps({'labels':list(add)}))
    for l in remove: gh('-X','DELETE',f'{R}/issues/{num}/labels/'+l.replace(' ','%20').replace(':','%3A'))
    print(num,'labels',[l['name'] for l in json.loads(gh(f'{R}/issues/{num}'))['labels']])
