import json,sys,re
aid,out=sys.argv[1:3]
best=None
for line in open(f'/tmp/claude-0/-home-user-incompleteness/8a0f23ba-ffa7-50df-a785-676e090e9917/tasks/{aid}.output'):
    try:o=json.loads(line)
    except:continue
    c=o.get('message',{}).get('content')
    if isinstance(c,list):
        for b in c:
            if b.get('type')=='tool_use' and 'andback' in b.get('name',''): best=b['input']
t=next(v for v in best.values() if isinstance(v,str) and len(v)>1500)
m=re.search(r"```[a-z]*\n(?:[^\n`]*\.md\n\n)?(# .*?)\n```",t,re.S)
p=m.group(1)+'\n'
assert '```' not in p and '@' not in p and '<!' not in p and '\r' not in p
open(out,'w',encoding='utf-8',newline='').write(p)
print(len(p.splitlines()),'lines;',p.splitlines()[0][:90])
